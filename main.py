from contextlib import asynccontextmanager

from fastapi import FastAPI

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app.router.lifespan_context = lifespan

@app.get("/")
async def hello_world():
    return {"test": "hello, world!"}