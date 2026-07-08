"""
Document Model

Represents a document stored in ResearchOS.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Document:

    id: Optional[int] = None

    filename: str = ""

    filepath: str = ""

    upload_time: str = ""

    total_pages: int = 0

    total_chunks: int = 0