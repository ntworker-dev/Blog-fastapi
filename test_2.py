# import sqlite3
# from contextlib import contextmanager

# @contextmanager
# def _get_connection():
#     connection = sqlite3.connect("./database.db")
#     connection.row_factory = sqlite3.Row
#     try:
#         yield connection
#         connection.commit()
#     except Exception as e:
#         connection.rollback()
#         print(f"Error: {e}")
#         raise
#     finally:
#         connection.close()

# query = """
#     CREATE TABLE games (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     genre TEXT,
#     release_year INTEGER,
#     rating REAL,
#     price REAL 
# )
# """

# insert_query = """
# """

# query_sel = "SELECT * FROM games;"

# with _get_connection() as connection:
#     cursor = connection.cursor()
#     cursor.execute(query_sel)
