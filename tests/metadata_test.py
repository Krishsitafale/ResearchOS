"""
Metadata Service

Responsible for storing and retrieving
document metadata.
"""

from datetime import datetime

from backend.models.document import Document
from backend.models.chunk import Chunk

from backend.repositories.document_repository import (
    DocumentRepository,
)

from backend.repositories.chunk_repository import (
    ChunkRepository,
)

from backend.core.logger import logger


class MetadataService:

    def __init__(self):

        self.document_repository = DocumentRepository()

        self.chunk_repository = ChunkRepository()

    # --------------------------------------------------

    def save_document(
        self,
        filename: str,
        filepath: str,
        total_pages: int,
        chunks: list[str],
    ) -> int:

        logger.info("Saving document metadata...")

        document = Document(

            filename=filename,

            filepath=filepath,

            upload_time=datetime.now().isoformat(),

            total_pages=total_pages,

            total_chunks=len(chunks),

        )

        document_id = self.document_repository.create(
            document
        )

        logger.info(
            f"Document stored with ID {document_id}"
        )

        chunk_models = []

        for index, chunk in enumerate(chunks):

            chunk_models.append(

                Chunk(

                    document_id=document_id,

                    page_number=0,

                    chunk_number=index,

                    chunk_text=chunk,

                )

            )

        self.chunk_repository.create_many(
            chunk_models
        )

        logger.info(
            f"Stored {len(chunk_models)} chunks."
        )

        return document_id

    # --------------------------------------------------

    def get_document(
        self,
        document_id: int,
    ):

        return self.document_repository.get_by_id(
            document_id
        )

    # --------------------------------------------------

    def list_documents(self):

        return self.document_repository.get_all()

    # --------------------------------------------------

    def get_chunks(
        self,
        document_id: int,
    ):

        return self.chunk_repository.get_by_document(
            document_id
        )

    # --------------------------------------------------

    def delete_document(
        self,
        document_id: int,
    ):

        self.chunk_repository.delete_by_document(
            document_id
        )

        self.document_repository.delete(
            document_id
        )

        logger.info(
            f"Deleted document {document_id}"
        )

service = MetadataService()

document_id = service.save_document(
    filename="demo.pdf",
    filepath="backend/storage/uploads/demo.pdf",
    total_pages=12,
    chunks=[
        "Chunk One",
        "Chunk Two",
        "Chunk Three"
    ]
)

print(document_id)

print(service.list_documents())

print(service.get_chunks(document_id))