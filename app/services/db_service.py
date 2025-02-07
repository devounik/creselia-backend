from sqlalchemy.orm import Session
from app.models.db_model import UserDatabase
from app.utils.encrypt_utils import encrypt
from app.schemas.db_schema import UserDbSchema

def add_user_DB_ceredential(db:Session,credentials:UserDbSchema):
  encrypt_pass = encrypt(credentials.password)

  new_user_db = UserDatabase(
    user_id=credentials.user_id,
    db_type=credentials.db_type,
    host = credentials.host,
    port =credentials.port,
    username = credentials.username,
    password=credentials.password,
    db_name=credentials.db_name,
  )
  db.add(new_user_db)
  db.commit()
  db.refresh(new_user_db)
  return new_user_db