import sys
sys.path.append("..")

from sqlalchemy import Column
from sqlalchemy import String, Integer, Boolean
from sqlalchemy_utils import EmailType
from database import Base
from passlib.hash import bcrypt

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, auto_increment = True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(128))
    email_address = Column(EmailType, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)

    def orm_to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hashed": self.password_hash,
            "email_address": self.email_address
        }

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.password_hash)