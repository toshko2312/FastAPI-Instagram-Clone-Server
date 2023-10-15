from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from sqlalchemy import Column, Integer, String, Table


class DbUser(Base):
    __tablename__: str = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(150))


