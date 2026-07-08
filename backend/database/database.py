"""
Database Manager

Responsible for:

- Opening SQLite connection
- Creating database
- Creating tables
- Returning database connection

ResearchOS V3
"""

from pathlib import Path
import sqlite3

from backend.core.logger import logger

DATABASE_DIR = Path("backend/storage")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "researchos.db"


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        logger.info(
            f"SQLite database initialized at: {DATABASE_PATH}"
        )

    # ----------------------------------------------------

    def get_connection(self):

        return self.connection

    # ----------------------------------------------------

    def get_cursor(self):

        return self.connection.cursor()

    # ----------------------------------------------------

    def commit(self):

        self.connection.commit()

    # ----------------------------------------------------

    def close(self):

        self.connection.close()


database = DatabaseManager()