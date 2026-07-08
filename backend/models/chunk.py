"""
Chunk Model

Represents one chunk belonging to a document.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Chunk:

    id: Optional[int] = None

    document_id: int = 0

    page_number: int = 0

    chunk_number: int = 0

    chunk_text: str = ""