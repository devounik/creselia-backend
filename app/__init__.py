from sqlalchemy.ext.declarative import declarative_base
from app.config import prod_db_url
from sqlalchemy import create_engine


Base = declarative_base()

engine = create_engine(prod_db_url,echo=True)