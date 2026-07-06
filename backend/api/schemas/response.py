"""
Response Models
"""

from pydantic import BaseModel


class UploadResponse(BaseModel):

    status: str

    filename: str

    characters: int

    num_chunks: int

    embedding_dimension: int


class SearchResult(BaseModel):

    id: int

    chunk: str

    score: float

    retriever: str


class SearchResponse(BaseModel):

    query: str

    top_k: int

    results: list[SearchResult]

class ChatResponse(BaseModel):

    query: str

    answer: str

    sources: list