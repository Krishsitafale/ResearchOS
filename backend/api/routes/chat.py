from fastapi import APIRouter

from backend.api.schemas.request import ChatRequest

from backend.services.rag_service import RAGService

router = APIRouter()

rag = RAGService()


@router.post("/chat")
def chat(

    request: ChatRequest

):

    return rag.answer(

        request.query

    )