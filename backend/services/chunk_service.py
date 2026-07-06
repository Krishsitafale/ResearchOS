"""
Text Chunking Service

Splits extracted text into overlapping chunks.
"""

from backend.core.logger import logger


class ChunkService:

    def __init__(

        self,

        chunk_size: int = 800,

        chunk_overlap: int = 150

    ):

        self.chunk_size = chunk_size

        self.chunk_overlap = chunk_overlap

    # --------------------------------------------------------

    def chunk_text(

        self,

        text: str

    ) -> list[str]:

        logger.info(

            "Starting text chunking..."

        )

        text = text.strip()

        if not text:

            return []

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(

                chunk.strip()

            )

            start += (

                self.chunk_size

                - self.chunk_overlap

            )

        logger.info(

            f"Generated {len(chunks)} chunks."

        )

        return chunks