"""
BM25 Sparse Retrieval Service
"""

from rank_bm25 import BM25Okapi

from backend.core.dependencies import vector_store
from backend.core.logger import logger


class BM25Service:

    def __init__(self):

        self.bm25 = None

        self.documents = []

        self.build_index()

    # ---------------------------------------------------------

    def build_index(self):

        self.documents = vector_store.documents

        if len(self.documents) == 0:

            logger.warning(
                "No documents available for BM25."
            )

            return

        tokenized = [

            doc.lower().split()

            for doc in self.documents

        ]

        self.bm25 = BM25Okapi(
            tokenized
        )

        logger.info(
            f"BM25 index built using {len(self.documents)} chunks."
        )

    # ---------------------------------------------------------

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        if self.bm25 is None:

            return []

        query_tokens = query.lower().split()

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked = sorted(

            enumerate(scores),

            key=lambda x: x[1],

            reverse=True

        )[:top_k]

        results = []

        for idx, score in ranked:

            results.append(

                {

                    "id": int(idx),

                    "chunk": self.documents[idx],

                    "score": float(score),

                    "retriever": "bm25"

                }

            )

        return results