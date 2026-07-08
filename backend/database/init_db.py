"""
Database Initialization

Creates all ResearchOS tables.
"""

from backend.database.database import database
from backend.core.logger import logger


def initialize_database():

    cursor = database.get_cursor()

    # ----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT NOT NULL,

            filepath TEXT NOT NULL,

            upload_time TEXT NOT NULL,

            total_pages INTEGER,

            total_chunks INTEGER

        );
        """
    )

    # ----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chunks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            document_id INTEGER NOT NULL,

            page_number INTEGER,

            chunk_number INTEGER,

            chunk_text TEXT NOT NULL,

            FOREIGN KEY(document_id)
            REFERENCES documents(id)

        );
        """
    )

    database.commit()

    logger.info("SQLite tables initialized successfully.")