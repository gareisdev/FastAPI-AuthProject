import sys
sys.path.append("..")

from sqlalchemy import Column
from sqlalchemy import String, Integer
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, auto_increment = True)
    username = Column(String, max_length=50, unique=True)
    password_hash = Column(String, max_length=128)

