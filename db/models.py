from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__: str = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(150))
    posts = relationship('DbPost', back_populates='user')


class DbPost(Base):
    __tablename__: str = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(300))
    image_url_type = Column(String(25))
    caption = Column(String(100))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DbUser', back_populates='posts')



