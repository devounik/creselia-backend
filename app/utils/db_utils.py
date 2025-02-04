# Contains utility functions for common tasks.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from contextlib import contextmanager
from app.config import prod_db_url


Base = declarative_base()

engine = create_engine(prod_db_url,echo=True)

def init_db():
  Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

@contextmanager
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

