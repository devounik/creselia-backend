from sqlalchemy import Column,String,ForeignKey,Text,Integer
from app.utils.db_utils import Base
from sqlalchemy.orm import relationship

class UserDatabase(Base):
  __tablename__ = "users_database_info"

  id = Column(Integer,nullable=False,autoincrement=True)
  user_id = Column(String(255),ForeignKey('users.uid',ondelete='CASCADE'),nullable=False)
  db_type = Column(String(255),nullable=False)
  host=Column(String(255),nullable=False)
  port = Column(String(255),nullable=False)
  username=Column(String(255),nullable=False)
  password=Column(Text,nullable=False)
  db_name=Column(String(255),nulable=False)

  user = relationship('User',back_populates='users_database_info')
