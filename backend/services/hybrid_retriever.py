"""
Hybrid Retriever

Combines:

1. Dense Retrieval (FAISS)

2. Sparse Retrieval (BM25)

using Reciprocal Rank Fusion (RRF).
"""

from collections import defaultdict

from backend.services.retriever_service import RetrieverService

from backend.core.dependencies import (
    bm25_service
)

from backend.core.logger import logger


class HybridRetriever:

    def __init__(self):

        self.dense = RetrieverService()

    # -----------------------------------------------------

    def retrieve(

        self,

        query: str,

        top_k: int = 5

    ):

        logger.info("=" * 60)

        logger.info("Hybrid Retrieval Started")

        logger.info("=" * 60)

        # ---------------------------------------

        dense_results = self.dense.retrieve(

            query=query,

            top_k=top_k * 2

        )

        # ---------------------------------------

        bm25_results = bm25_service.search(

            query=query,

            top_k=top_k * 2

        )

        logger.info(

            f"Dense : {len(dense_results)}"

        )

        logger.info(

            f"BM25 : {len(bm25_results)}"

        )

        # ---------------------------------------
        # Reciprocal Rank Fusion
        # ---------------------------------------

        rrf_scores = defaultdict(float)

        merged = {}

        k = 60

        # Dense

        for rank, item in enumerate(

            dense_results

        ):

            chunk_id = item["id"]

            merged[chunk_id] = item

            rrf_scores[chunk_id] += (

                1 / (k + rank + 1)

            )

        # BM25

        for rank, item in enumerate(

            bm25_results

        ):

            chunk_id = item["id"]

            merged[chunk_id] = item

            rrf_scores[chunk_id] += (

                1 / (k + rank + 1)

            )

        # ---------------------------------------

        ranked = sorted(

            merged.values(),

            key=lambda x: rrf_scores[x["id"]],

            reverse=True

        )

        # ---------------------------------------

        results = []

        for item in ranked[:top_k]:

            results.append(

                {

                    "id": item["id"],

                    "chunk": item["chunk"],

                    "score": float(

                        rrf_scores[item["id"]]

                    ),

                    "retriever": "hybrid"

                }

            )

        logger.info(

            f"Returning {len(results)} hybrid chunks."

        )

        logger.info("=" * 60)

        logger.info("Hybrid Retrieval Complete")

        logger.info("=" * 60)

        return results