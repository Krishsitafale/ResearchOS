from backend.core.dependencies import (
    reranker_service
)

from backend.services.hybrid_retriever import HybridRetriever
from backend.services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.retriever = HybridRetriever()

        self.llm = LLMService()

    # -----------------------------------------------------

    def answer(

        self,

        query: str

    ):

        candidates = self.retriever.retrieve(

            query=query,

            top_k=20

        )

        reranked = reranker_service.rerank(

            query=query,

            chunks=candidates,

            top_k=5

        )

        context = "\n\n".join(

            [

                chunk["chunk"]

                for chunk in reranked

            ]

        )

        answer = self.llm.generate(

            query=query,

            context=context

        )

        return {

            "answer": answer,

            "sources": reranked

        }