import sqlite3
from contextlib import contextmanager

# from test import query


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
        posts_query = """
            CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """

        users_query = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                registered_at DATETIME DEFAULT CURRENT_TIMESTAMP 
            )
        """

        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(posts_query)
            cursor.execute(users_query)

    def create_post(self, title: str, content: str, user_id) -> dict[str, str]:
        query = "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)"
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query,(title, content, user_id))
            return {
                "title": title,
                "content": content,
            }

    def get_posts(self):
        query = """SELECT * FROM posts"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_post_by_id(self, id: str) -> dict | None:
        query = """SELECT * FROM posts WHERE id = ?"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def update_post(self, id: str, title: str, content: str) -> dict | None:
        query = """UPDATE posts SET title = ?, content = ? WHERE id = ?"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (title, content, id))
        return self.get_post_by_id(id)

    def create_user(self, user: dict[str, str]) -> dict[str, str]:
        query = """INSERT INTO users (username, email, password) VALUES (?, ?, ?)"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query,(user["username"], user["email"], user["password"]))
            return {
                "username": user["username"],
                "email": user["email"],
            }

    def get_user_by_email(self, email: str) -> dict | None:
        query = """SELECT id, username, email FROM users WHERE email = ?"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_users(self) -> list:
        query = """SELECT id, username, email FROM users"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_user_by_id(self, id: int) -> dict:
        query = """SELECT username, email FROM users WHERE id = ?"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def delete_post(self, id: int):
        query = """DELETE FROM posts WHERE id = ?"""
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
