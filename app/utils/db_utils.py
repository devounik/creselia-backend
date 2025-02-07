# Contains utility functions for common tasks.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from contextlib import contextmanager
from app.config import prod_db_url
from app.__init__ import Base,engine
#from app.models.chat_model import Chats,ChatSession,Query
#from app.models.db_model import UserDatabase
#from app.models.user_model import User


def init_db():
  print("Initializing the  database")
  Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

@contextmanager
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

