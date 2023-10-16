from sqlalchemy.orm import Session
from db.models import DbUser
from db.schemas import UserBase
from db.hashing import Hash
from fastapi import HTTPException


def create_user_service(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username_service(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User with username {username} not found'
        )
    return user

