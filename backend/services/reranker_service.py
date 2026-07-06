"""
Cross Encoder Reranker
"""

from sentence_transformers import CrossEncoder

from backend.core.config import CROSS_ENCODER_MODEL
from backend.core.logger import logger


class RerankerService:

    def __init__(self):

        logger.info(
            "Loading Cross Encoder..."
        )

        self.model = CrossEncoder(
            CROSS_ENCODER_MODEL
        )

        logger.info(
            "Cross Encoder Loaded."
        )

    # --------------------------------------------------

    def rerank(

        self,

        query: str,

        chunks: list,

        top_k: int = 5

    ):

        if len(chunks) == 0:

            return []

        sentence_pairs = [

            (

                query,

                chunk["chunk"]

            )

            for chunk in chunks

        ]

        scores = self.model.predict(
            sentence_pairs
        )

        reranked = []

        for chunk, score in zip(

            chunks,

            scores

        ):

            reranked.append(

                {

                    "id": chunk["id"],

                    "chunk": chunk["chunk"],

                    "retriever": chunk["retriever"],

                    "retrieval_score": chunk["score"],

                    "reranker_score": float(score)

                }

            )

        reranked.sort(

            key=lambda x: x["reranker_score"],

            reverse=True

        )

        logger.info(

            f"Reranked {len(reranked)} chunks."

        )

        return reranked[:top_k]