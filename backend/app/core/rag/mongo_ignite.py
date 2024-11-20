import logging
import math
import re
from collections import Counter, namedtuple
from typing import Callable, List

from langchain_core.documents import Document
from pymongo.results import DeleteResult

from pymongo.synchronous.collection import Collection
from pymongo.synchronous.command_cursor import CommandCursor
from pymongo.typings import _CollationIn, _DocumentType, _DocumentTypeArg, _Pipeline

from pymongo import MongoClient
from langchain_community.vectorstores import MongoDBAtlasVectorSearch

from app.core.config import settings
from app.core.rag.document_processor import load_and_split_document
from app.core.rag.embeddings import get_embedding_model

logger = logging.getLogger(__name__)

class IgniteStore:
    def __init__(self) -> None:
        self.collection_name = settings.QDRANT_COLLECTION
        self.url = settings.MONGODB_URL
        self.embedding_model = get_embedding_model('raw_text')

        logger.debug(f"Initializing QdrantStore with URL: {self.url}")

        self.client = MongoClient(self.url)
        logger.debug("QdrantClient initialized successfully")
        self.collection: Collection[_DocumentType] = None
        self._initialize_vector_store()

    def _initialize_vector_store(self):
        try:
            collections = self.client.get_default_database().list_collection_names()
            if self.collection_name not in [
                collection for collection in collections
            ]:
                logger.debug(f"Creating new collection: {self.collection_name}")
                self.collection = self.client.get_default_database().create_collection(
                    self.collection_name,
                )
                logger.debug("Creating payload index for user_id and upload_id")
                self.collection.create_index(
                    [('user_id','1'),('upload_id','1')]
                )
                logger.debug("Creating payload index for text")
                self.collection.create_index([('text','text')])
                self.collection.create_index([('embedding','knnVector')])
            else:
                logger.debug(f"Using existing collection: {self.collection_name}")
                self.collection = self.client.get_default_database()[self.collection_name]

            logger.debug(f"Collection info: {self.collection}")

            self.vector_store = MongoDBAtlasVectorSearch(
                self.collection,
                self.embedding_model,
            )
        except Exception as e:
            logger.error(f"Error initializing vector store: {str(e)}", exc_info=True)
            raise

    def count(self,count_filter):
        result = self.collection.aggregate([{"$match":count_filter},{"$count":"count"}])
        for r in result:
            return r['count']
        return 0

    def add(
        self,
        file_path_or_url: str,
        upload_id: int,
        user_id: int,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        callback: Callable[[], None] | None = None,
    ) -> None:
        try:
            docs = load_and_split_document(
                file_path_or_url, user_id, upload_id, chunk_size, chunk_overlap
            )
            # Ensure metadata is correctly set
            for doc in docs:
                doc.metadata["user_id"] = user_id
                doc.metadata["upload_id"] = upload_id

            initial_count = self.count(
                count_filter={"user_id":user_id, "upload_id":upload_id}
            )

            self.vector_store.add_documents(docs)
            final_count = self.count(
                count_filter={"user_id":user_id, "upload_id":upload_id}
            )

            added_count = final_count - initial_count
            logger.info(
                f"Added {added_count} documents for upload_id: {upload_id}, user_id: {user_id}"
            )

            if callback:
                callback()
        except Exception as e:
            logger.error(f"Error adding document: {str(e)}", exc_info=True)
            raise

    def delete(self, upload_id: int, user_id: int) -> bool:
        try:
            logger.debug(
                f"Attempting to delete points for upload_id: {upload_id}, user_id: {user_id}"
            )
            filter_condition = {"user_id":user_id, "upload_id":upload_id}
            logger.debug(f"Delete filter condition: {filter_condition}")

            initial_count = self.count(
                count_filter=filter_condition,
            )
            logger.debug(f"Initial document count: {initial_count}")

            result: DeleteResult = self.collection.delete_many(
                filter=filter_condition,
            )
            logger.debug(f"Delete operation result: {result}")

            if isinstance(result, DeleteResult) and result.deleted_count>0:
                final_count = self.count(
                    count_filter=filter_condition,
                )
                logger.debug(f"Final document count: {final_count}")

                deleted_count = initial_count - final_count

                if deleted_count > 0:
                    logger.info(
                        f"Successfully deleted {deleted_count} points for upload_id: {upload_id}, user_id: {user_id}"
                    )
                    return True
                elif initial_count == 0:
                    logger.info(
                        f"No documents found to delete for upload_id: {upload_id}, user_id: {user_id}"
                    )
                    return True  # Consider this a successful operation as there's nothing to delete
                else:
                    logger.warning(
                        f"No points were deleted for upload_id: {upload_id}, user_id: {user_id}"
                    )
                    return False
            else:
                logger.error(
                    f"Delete operation failed or returned unexpected result: {result}"
                )
                return False
        except Exception as e:
            logger.error(f"Error deleting documents: {str(e)}", exc_info=True)
            return False

    def update(
        self,
        file_path_or_url: str,
        upload_id: int,
        user_id: int,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        callback: Callable[[], None] | None = None,
    ) -> None:
        deletion_successful = self.delete(upload_id, user_id)
        if not deletion_successful:
            logger.warning(
                f"Failed to delete existing documents for upload_id: {upload_id}, user_id: {user_id}. Proceeding with add operation."
            )
        self.add(file_path_or_url, upload_id, user_id, chunk_size, chunk_overlap)
        if callback:
            callback()

    def search(self, user_id: int, upload_ids: List[int], query: str) -> List[Document]:
        filter_condition = {"user_id":user_id, "upload_id":upload_ids}
        logger.debug(f"Search filter condition: {filter_condition}")

        search_results = self.vector_store.similarity_search_with_score(
            query,
            pre_filter=filter_condition,
            k=4,
        )

        documents = []
        for result,score in search_results:
            result.id = result.metadata["_id"]
            result.metadata["score"] = score
            documents.append(result)

        return documents

    def retriever(self, user_id: int, upload_id: int):
        logger.debug(
            f"Creating retriever for user_id: {user_id}, upload_id: {upload_id}"
        )
        filter_condition = {"user_id":user_id, "upload_id":upload_id}
        retriever = self.vector_store.as_retriever(
            search_kwargs={"filter": filter_condition, "k": 5},
            search_type="similarity",
        )
        logger.debug(f"Retriever created: {retriever}")
        return retriever

    def debug_retriever(self, user_id: int, upload_id: int, query: str):
        logger.debug(
            f"Debug retriever for user_id: {user_id}, upload_id: {upload_id}, query: '{query}'"
        )

        # 使用过滤器的搜索
        filtered_docs = self.search(user_id, [upload_id], query)
        logger.debug(f"Filtered search found {len(filtered_docs)} documents")
        for doc in filtered_docs:
            logger.debug(f"Filtered doc metadata: {doc.metadata}")

        # 不使用过滤器的搜索
        unfiltered_docs = self.vector_store.similarity_search(query, k=5)
        logger.debug(f"Unfiltered search found {len(unfiltered_docs)} documents")

        # 打印所有文档的元数据
        for i, doc in enumerate(unfiltered_docs):
            logger.debug(f"Unfiltered doc {i} metadata: {doc.metadata}")

        return filtered_docs

    def get_collection_info(self):
        collection_info = self.client.get_default_database().get_collection(self.collection_name)
        logger.debug(f"Collection info: {collection_info}")
        return collection_info

    def vector_search(
        self,
        user_id: int,
        upload_ids: List[int],
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.5,
    ):
        filter_condition = {"user_id":user_id, "upload_id":upload_ids}
        search_results = self.collection.find(filter={
                'embedding':{'$knnVector':query,'$limit':top_k,'$score_threshold': score_threshold},
                "user_id":user_id,
                "upload_id":upload_ids,
            },
            limit = top_k
        )
        return [self._convert_to_document(result) for result in search_results]

    def fulltext_search(
        self,
        user_id: int,
        upload_ids: List[int],
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.05,
    ):
        filter_condition = {"user_id":user_id, "upload_id":upload_ids}
        # 为全文搜索生成一个空的查询向量
        search_results = self.collection.find(filter={
                '$text':{'$search':query, '$limit':top_k, '$score_threshold': score_threshold},
                "user_id":user_id,
                "upload_id":upload_ids,
            },
            limit = top_k
        )

        # 改进的相关性评分
        query_terms = Counter(re.findall(r"\w+", query.lower()))
        filtered_results = []
        for result in search_results:
            content = result.get("text", "").lower()
            content_terms = Counter(re.findall(r"\w+", content))

            # 计算改进的 TF-IDF 相似度分数
            score = result.get("_meta", {}).get('searchScore',0)
            for term, query_count in query_terms.items():
                if term in content_terms:
                    tf = content_terms[term] / len(content_terms)
                    idf = 10.0
                    score += (tf * idf) * query_count

            if score > 0:
                filtered_results.append((result, score))

        # 归一化分数
        if filtered_results:
            max_score = max(score for _, score in filtered_results)
            filtered_results = [
                (result, score / max_score) for result, score in filtered_results
            ]

        # 应用 score threshold
        filtered_results = [
            (result, score)
            for result, score in filtered_results
            if score >= score_threshold
        ]

        # 按分数排序并选择前 top_k 个结果
        filtered_results.sort(key=lambda x: x[1], reverse=True)
        top_results = filtered_results[:top_k]

        return [
            self._convert_to_document(result, score) for result, score in top_results
        ]

    def _convert_to_document(self, result, score=None):
        if score is None:
            score = result.get("_meta", {}).get('vectorSearchScore')
            if score is None:
                score = result.get("_meta", {}).get('searchScore')
        result['score'] = score
        return Document(
            page_content=result.pop("text", ""),
            metadata=result,
        )

    def hybrid_search(
        self,
        user_id: int,
        upload_ids: List[int],
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.5,
    ):
        vector_results = self.vector_search(
            user_id, upload_ids, query, top_k, score_threshold
        )
        fulltext_results = self.fulltext_search(
            user_id, upload_ids, query, top_k, score_threshold
        )

        # 合并结果并按分数排序
        combined_results = vector_results + fulltext_results
        combined_results.sort(key=lambda x: x.metadata["score"], reverse=True)
        return combined_results[:top_k]
