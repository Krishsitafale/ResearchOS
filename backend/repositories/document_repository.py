"""
Document Repository

Handles all database operations related to documents.
"""

from backend.database.database import database
from backend.models.document import Document


class DocumentRepository:

    def __init__(self):
        self.db = database

    # -----------------------------------------------------

    def create(self, document: Document) -> int:

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            INSERT INTO documents
            (
                filename,
                filepath,
                upload_time,
                total_pages,
                total_chunks
            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                document.filename,
                document.filepath,
                document.upload_time,
                document.total_pages,
                document.total_chunks,
            ),
        )

        self.db.commit()

        return cursor.lastrowid

    # -----------------------------------------------------

    def get_by_id(self, document_id: int):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            SELECT *
            FROM documents
            WHERE id = ?
            """,
            (document_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Document(
            id=row["id"],
            filename=row["filename"],
            filepath=row["filepath"],
            upload_time=row["upload_time"],
            total_pages=row["total_pages"],
            total_chunks=row["total_chunks"],
        )

    # -----------------------------------------------------

    def get_all(self):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            SELECT *
            FROM documents
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        documents = []

        for row in rows:

            documents.append(
                Document(
                    id=row["id"],
                    filename=row["filename"],
                    filepath=row["filepath"],
                    upload_time=row["upload_time"],
                    total_pages=row["total_pages"],
                    total_chunks=row["total_chunks"],
                )
            )

        return documents

    # -----------------------------------------------------

    def delete(self, document_id: int):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            DELETE FROM documents
            WHERE id = ?
            """,
            (document_id,),
        )

        self.db.commit()