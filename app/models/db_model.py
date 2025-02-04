from sqlalchemy import Column,String,ForeignKey,Text
from app.utils.db_utils import Base


class Database(Base):
  __tablename__ = "users_database_info"
  id = Column(String(255),nullable=False,autoincrement=True)
  user_id = Column(String(255),ForeignKey('users.uid',ondelete='CASCADE'),nullable=False)
  db_type = Column(String(255),nullable=False)
  host=Column(String(255),nullable=False)
  port = Column(String(255),nullable=False)
  username=Column(String(255),nullable=False)
  password=Column(Text,nullable=False)
  db_name=Column(String(255),nulable=False)
