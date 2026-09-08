from fastapi import APIRouter
from app.database import Database
from app.models import CreateUser
from app.auth import get_password_hash

router = APIRouter()
db = Database("database.db")
db.init_schema()

@router.get("/users")
def get_users():
    return db.get_users()

@router.post("/register")
def register(user: CreateUser):
    existing_user = db.get_user_by_email(user["email"])
    if existing_user:
        print("Email already registered")
        return
    new_user = {
        "username": user["username"],
        "email": user["email"],
        "password": get_password_hash(user["password"]),
    }
    db.create_user(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login():
    return