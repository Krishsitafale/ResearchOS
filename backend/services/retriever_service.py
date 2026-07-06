"""
Retriever Service

Generates query embeddings and
retrieves the most relevant chunks
from FAISS.
"""

from backend.core.dependencies import (
    embedding_service,
    vector_store,
)

from backend.core.logger import logger


class RetrieverService:

    def __init__(self):
        pass

    # --------------------------------------------------------

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):

        logger.info("=" * 60)
        logger.info("Semantic Search Started")
        logger.info("=" * 60)

        logger.info(f"Query: {query}")

        # ----------------------------------------
        # Generate Query Embedding
        # ----------------------------------------

        query_embedding = embedding_service.generate_embeddings(
            [query]
        )

        logger.info(
            f"Query embedding shape: {query_embedding.shape}"
        )

        # ----------------------------------------
        # Search FAISS
        # ----------------------------------------

        results = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        logger.info(
            f"Retrieved {len(results)} chunks."
        )

        logger.info("=" * 60)
        logger.info("Semantic Search Complete")
        logger.info("=" * 60)

        return results