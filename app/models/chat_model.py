#Defines chat model for database
from sqlalchemy import Column,Text,String,ForeignKey,Integer,TIMESTAMP,text
from sqlalchemy.orm import relationship
from app.utils.db_utils import Base

class ChatSession(Base):
  __tablename__ = 'chat_sessions'

  session_id = Column(Integer,primary_key=True,autoincrement=True)
  user_id=Column(String(255),ForeignKey('users.uid',ondelete='CASCADE'),nullable=False)
  session_name=Column(Text,nullable=False)
  created_at=Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))

  user=relationship('User',back_populates='chat_sessions')
  chats = relationship('Chat', back_populates='session')
  queries = relationship('Query', back_populates='session')


class Chats(Base):
  __tablename__='chats'

  chat_id = Column(Integer,primary_key=True,autoincrement=True)
  session_id =Column(Integer,ForeignKey('chat_sessions.session_id',ondelete='CASCADE'),nullable=False)
  user_id = Column(String(255),ForeignKey('users.uid',ondelete='CASCADE'),nullable=False)
  message = Column(Text,nullable=False)
  response = Column(Text,nullable=False)
  timestamp = Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))

  session = relationship('ChatSession',back_populates='chats')
  user = relationship('User',back_populates='chats')


class Query(Base):
  __tablename__ = 'queries'

  query_id=Column(Integer,primary_key=True,autoincrement=True)
  session_id=Column(Integer,ForeignKey('chat_sessions.id',ondelete='CASCADE'),nullable=False)
  user_id=Column(String(255),ForeignKey('users.uid',ondelete='CASCADE'),nullable=False)
  natural_query = Column(Text,nullable=False)
  sql_query = Column(Text,nullable=False)
  timestamp = Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))


  session = relationship('ChatSession', back_populates='queries')
  user = relationship('User', back_populates='queries')
