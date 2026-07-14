from sqlalchemy import table
from sqlmodel import SQLModel, Field

class Post(SQLModel, table = True):
    id: str = Field(primary_key=True)
    title: str
    content: str
    user_id: str = Field(foreign_key="users.id")
    created_at: str

class User(SQLModel, table = True):
    id: str = Field(primary_key=True)
    username: str
    email: str
    registered_at: str