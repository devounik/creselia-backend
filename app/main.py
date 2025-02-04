# backend/app/main.py

from fastapi import FastAPI
from app.routers import auth_router, query_router, user_router, chat_router

from  app.__init__  import init_db

async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to the backend system!"}