"""
SQLite Database Manager

Responsible for:

- Creating database
- Creating tables
- Providing database connections
"""

import sqlite3
from pathlib import Path
DATABASE_PATH = Path("backend/storage/researchos.db")

print("SQLite module imported")

class Database:

    def __init__(self):

        DATABASE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    # --------------------------------------------------

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                filename TEXT NOT NULL,

                filepath TEXT NOT NULL,

                upload_time TEXT NOT NULL,

                num_pages INTEGER,

                num_chunks INTEGER

            );
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS chunks (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                document_id INTEGER NOT NULL,

                page_number INTEGER,

                chunk_number INTEGER,

                text TEXT NOT NULL,

                FOREIGN KEY(document_id)
                REFERENCES documents(id)
            );
            """
        )

        self.connection.commit()

    # --------------------------------------------------

    def cursor(self):

        return self.connection.cursor()

    # --------------------------------------------------

    def commit(self):

        self.connection.commit()


database = Database()