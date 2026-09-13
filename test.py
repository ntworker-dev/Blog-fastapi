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
#     CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE,
#     birthdate TEXT NOT NULL DEFAULT "1970-01-01" 
# )
# """

# delete_query = """DROP TABLE users"""

# name = "Иван"
# email = "vo1ce@example.com"

# insert_query = """
#     INSERT INTO users (name, email) VALUES (?, ?);
# """

# select_query = """
#     SELECT * FROM users WHERE name = "Анна";
# """

# select_query_limited = """
#     SELECT * FROM users LIMIT 3;
# """

# update_query = """
#     UPDATE users SET birthdate = "2010-22-06" WHERE id = 2;
# """

# delete_anna_query = """
#     DELETE FROM users WHERE name = "Анна";
# """

# products = """
#     CREATE TABLE products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         title TEXT NOT NULL,
#         price REAL NOT NULL CHECK(price >= 0),
#         FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE 
#     )
# """

# users_products = """
#     SELECT * FROM products WHERE user_id = 2
# """

# users_products2 = """
#     SELECT products.title, products.price FROM products
#     JOIN users ON products.user_id = users.id
#     WHERE users.id = 4;
# """

# with _get_connection() as connection:
#     cursor = connection.cursor()
#     #cursor.execute(insert_query, (name, email))
#     cursor.execute(users_products2)
#     rows = cursor.fetchall()
#     print([dict(row) for row in rows])

















