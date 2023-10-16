from datetime import datetime
from enum import Enum

from pydantic import BaseModel, constr, Field
from typing import Annotated


class UserBase(BaseModel):
    username: Annotated[str, Field(..., min_length=1)]
    email: str
    password: Annotated[str, Field(..., min_length=5)]


class UserDisplay(BaseModel):
    username: str
    email: str


class ImageUrlTypes(str, Enum):
    absolute = 'absolute'
    relative = 'relative'


class PostBase(BaseModel):
    image_url: str
    image_url_type: ImageUrlTypes
    caption: str
    creator_id: int


class User(BaseModel):
    username: str


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User


class UserAuth(BaseModel):
    id: int
    username: str
    email: str
