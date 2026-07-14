from fastapi import APIRouter
from app.database import Database
from app.models import Post

router = APIRouter()
db = Database("database.db")
db.init_schema()

@router.get("/posts")
def get_posts():
    return db.get_posts()

@router.post("/posts")
def add_post(data: Post):
    pass

