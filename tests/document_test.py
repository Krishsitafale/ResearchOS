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

doc = Document(
    filename="Transformer.pdf",
    filepath="backend/storage/uploads/Transformer.pdf",
    upload_time="2026-07-06T14:30:00",
    total_pages=15,
    total_chunks=42
)

print(doc)