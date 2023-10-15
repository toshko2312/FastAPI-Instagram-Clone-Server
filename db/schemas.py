from pydantic import BaseModel, constr, Field
from typing import Annotated


class UserBase(BaseModel):
    username: Annotated[str, Field(..., min_length=1)]
    email: str
    password: Annotated[str, Field(..., min_length=5)]


class UserDisplay(BaseModel):
    username: str
    email: str
