import logging
import math
import re
from collections import Counter
from typing import Callable, List

from langchain_core.documents import Document

from app.core.rag.mongo_ignite import IgniteStore as QdrantStore

