from cryptography.fernet import  Fernet
import os
from dotenv import load_dotenv
from app.config import SECRET_KEY

load_dotenv()
"""
def generate_key():
  key = Fernet.generate_key()
"""


SECRET_KEY = SECRET_KEY


if not SECRET_KEY:
  raise ValueError("Secret key not found in .env file")

fernet = Fernet(SECRET_KEY.encode())

def encrypt(data:str)->str:
  return fernet.encrypt(data.encode()).decode()

def decrpyt(data:str)->str:
  return fernet.decrypt(data.encode()).decode()
