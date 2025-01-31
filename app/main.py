# backend/app/main.py

from fastapi import FastAPI
from app.routers import auth_router, query_router, user_router, chat_router

app = FastAPI()

# Include routers
app.include_router(auth_router.router)
app.include_router(query_router.router)
app.include_router(user_router.router)
app.include_router(chat_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the backend system!"}