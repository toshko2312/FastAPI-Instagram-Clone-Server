from sqlalchemy.orm import Session
from db.models import DbUser
from db.schemas import UserBase


def create_user_service(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
