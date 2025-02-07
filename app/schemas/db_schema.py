from pydantic import BaseModel

class UserDbSchema(BaseModel):
  user_id:str
  db_type:str
  host:str
  port:str
  username:str
  password:str
  db_name:str