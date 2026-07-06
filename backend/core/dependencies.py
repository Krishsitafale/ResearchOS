from backend.services.embedding_service import EmbeddingService
from backend.services.vector_store import VectorStore
from backend.services.reranker_service import RerankerService

reranker_service = RerankerService()

embedding_service = EmbeddingService()

vector_store = VectorStore()

# Imported after vector_store to avoid circular dependency
from backend.services.bm25_service import BM25Service

bm25_service = BM25Service()