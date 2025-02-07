# backend/app/main.py

from fastapi import FastAPI
from  app.utils.db_utils import init_db

async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to the backend system!"}