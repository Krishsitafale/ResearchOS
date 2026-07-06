"""
Request Models
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    query: str = Field(
        ...,
        min_length=1,
        description="User query"
    )


class SearchRequest(BaseModel):

    query: str = Field(
        ...,
        min_length=1,
        description="Semantic search query"
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20
    )