from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers import posts

from app.routers import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app.router.lifespan_context = lifespan
app.include_router(posts.router)
app.include_router(users.router)
# @app.get("/")
# async def hello_world():
#     return {"test": "hello, world!"}

