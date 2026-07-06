from fastapi import APIRouter

from backend.api.schemas.request import SearchRequest

from backend.services.rag_service import RAGService

router = APIRouter()

rag = RAGService()


@router.post("/search")
def search(
    request: SearchRequest
):

    results = rag.search(

        query=request.query,

        top_k=request.top_k

    )

    return {

        "query": request.query,

        "results": results

    }