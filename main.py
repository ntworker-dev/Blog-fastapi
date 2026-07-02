from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import posts

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app.router.lifespan_context = lifespan
app.include_router(posts.router)

@app.get("/")
async def hello_world():
    return {"test": "hello, world!"}

