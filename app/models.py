# from sqlmodel import SQLModel, Field
from pydantic import BaseModel, Field

class Post(BaseModel):
    id: int | None = Field(default=None)
    title: str
    content: str
    # user_id: str = Field(foreign_key="users.id")

class User(BaseModel):
    id: int | None
    username: str
    email: str
    # registered_at: str | None = Field(default=None)

class CreateUser(BaseModel):
    username: str
    email: str
    password: str