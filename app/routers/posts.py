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
    db.create_post(data.title, data.content, 2)
    return {"status": "OK"}

@router.get("/posts/{id}")
def show_post(id):
    return db.get_post_by_id(id)

@router.patch("/posts/{id}")
def update_post(data: Post, id: str):
    return db.update_post(id, data.title, data.content)

@router.delete("/posts/{id}")
def delete_post(id):
    try:
        db.delete_post(id)
        return {"deleted": True}
    except Exception as e:
        print(f"Ошибка удаления поста {id} \n {e}")
        return {"deleted": False}