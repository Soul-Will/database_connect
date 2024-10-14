from database.database import Base
from sqlalchemy import Column, Integer , String

class User(Base):
    __tablename__ = "User_data"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True)
    mobile = Column(String(10),unique=True)