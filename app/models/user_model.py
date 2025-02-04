from sqlalchemy import Column,String
from app.utils.db_utils import Base
from sqlalchemy.orm import relationship


class User(Base):
  __tablename__="users"

  uid = Column(String(255),primary_key=True)
  email=Column(String(255),unique=True,nullable=False)
  name = Column(String(255),nullable=False)
  profile_pic = Column(String(255),nullable=True)

  chat_sessions = relationship('ChatSession',back_populates='users')
  chats = relationship('Chats', back_populates='users')
  queries = relationship('Query', back_populates='users')
  userDB = relationship('UserDatabase',back_populates='users')