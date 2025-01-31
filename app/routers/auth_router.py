#fastapi routers for different functionalities 

# backend/app/routers/auth_router.py

from fastapi import APIRouter

# Create a router instance
router = APIRouter()

@router.post("/signup")
async def signup():
    return {"message": "Signup endpoint"}

@router.post("/login")
async def login():
    return {"message": "Login endpoint"}