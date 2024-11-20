import logging

from app.core.rag.mongo_ignite import IgniteStore as QdrantStore

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_delete_operation(user_id: int, upload_id: int):
    qdrant_store = QdrantStore()

    # 1. 首先，检查当前的文档数量
    logger.info("Checking initial document count:")
    initial_count = check_document_count(qdrant_store, user_id, upload_id)

    # 2. 执行删除操作
    logger.info(
        f"Attempting to delete documents for user_id: {user_id}, upload_id: {upload_id}"
    )
    deletion_result = qdrant_store.delete(upload_id, user_id)
    logger.info(f"Deletion result: {deletion_result}")

    # 3. 再次检查文档数量
    logger.info("Checking document count after deletion:")
    final_count = check_document_count(qdrant_store, user_id, upload_id)

    # 4. 比较结果
    if initial_count > final_count:
        logger.info(f"Successfully deleted {initial_count - final_count} documents")
    elif initial_count == final_count:
        logger.warning("No documents were deleted")
    else:
        logger.error("Unexpected result: document count increased after deletion")


def check_document_count(
    qdrant_store: QdrantStore, user_id: int, upload_id: int
) -> int:
    filter_condition = {
        "user_id": user_id,
        "upload_id": upload_id
    }
    count_result = qdrant_store.count(
        count_filter=filter_condition
    )
    count = count_result
    logger.info(
        f"Document count for user_id: {user_id}, upload_id: {upload_id}: {count}"
    )
    return count


def inspect_documents(qdrant_store: QdrantStore, user_id: int, upload_id: int):
    logger.info(f"Inspecting documents for user_id: {user_id}, upload_id: {upload_id}")
    filter_condition = {
        "user_id": user_id,
        "upload_id": upload_id
    }
    # filter_condition = {}
    search_results = qdrant_store.collection.find(
        filter=filter_condition,
        limit=10,
    )
    for point in search_results:
        logger.info(f"Point ID: {point['_id']}")
        logger.info(f"Payload: {point['text']}")
        logger.info("---")


if __name__ == "__main__":
    user_id = 1  # 替换为实际的用户ID
    upload_id = 20  # 替换为实际的上传ID

    qdrant_store = QdrantStore()
    # 检查集合信息
    collection_info = qdrant_store.get_collection_info()
    logger.info(f"Collection info: {collection_info}")

    count = check_document_count(qdrant_store, user_id, upload_id)
    if count==0:
        # 上传文档
        qdrant_store.add("uploads/README_cn.md",upload_id,user_id)

        qdrant_store.debug_retriever(user_id,upload_id,"安装")

    result1 = qdrant_store.search(user_id,[upload_id],"安装步骤")
    result2 = qdrant_store.vector_search(user_id,[upload_id],"安装步骤")
    result3 = qdrant_store.hybrid_search(user_id,[upload_id],"安装")

    # 检查并显示文档
    inspect_documents(qdrant_store, user_id, upload_id)

    # 执行删除测试
    test_delete_operation(user_id, upload_id)

    # 再次检查文档
    inspect_documents(qdrant_store, user_id, upload_id)

    # qdrant_store.client.get_default_database().drop_collection(collection_info.name)