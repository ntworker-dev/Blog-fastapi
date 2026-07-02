import sqlite3
from contextlib import contextmanager

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    @contextmanager
    def _get_connection(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
            raise
        finally:
            connection.close()

    def init_schema(self):
        query = """
            CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

    def create_post(self, title: str, content: str, author: str) -> dict[str, str]:
        query = "INSERT INTO posts (title, content, author) VALUES (?, ?, ?)"
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query,(title, content, author))
            return {
                "title": title,
                "content": content,
                "author": author
            }

    def get_posts(self):
        query = """SELECT id, title, content, author, created_at FROM posts"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]