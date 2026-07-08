"""
Chunk Repository

Handles all chunk database operations.
"""

from backend.database.database import database
from backend.models.chunk import Chunk


class ChunkRepository:

    def __init__(self):
        self.db = database

    # -----------------------------------------------------

    def create_many(self, chunks: list[Chunk]):

        cursor = self.db.get_cursor()

        cursor.executemany(
            """
            INSERT INTO chunks
            (
                document_id,
                page_number,
                chunk_number,
                chunk_text
            )

            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    chunk.document_id,
                    chunk.page_number,
                    chunk.chunk_number,
                    chunk.chunk_text,
                )
                for chunk in chunks
            ],
        )

        self.db.commit()

    # -----------------------------------------------------

    def get_by_document(self, document_id: int):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            SELECT *
            FROM chunks
            WHERE document_id = ?
            ORDER BY chunk_number
            """,
            (document_id,),
        )

        rows = cursor.fetchall()

        result = []

        for row in rows:

            result.append(
                Chunk(
                    id=row["id"],
                    document_id=row["document_id"],
                    page_number=row["page_number"],
                    chunk_number=row["chunk_number"],
                    chunk_text=row["chunk_text"],
                )
            )

        return result

    # -----------------------------------------------------

    def delete_by_document(self, document_id: int):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            DELETE FROM chunks
            WHERE document_id = ?
            """,
            (document_id,),
        )

        self.db.commit()