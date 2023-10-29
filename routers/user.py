from fastapi import APIRouter, Depends
from db.schemas import UserDisplay, UserBase
from services.user_services import create_user_service
from sqlalchemy.orm import Session
from db.database import get_db
from typing import Annotated

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay, summary='Create user.')
def create_user(request: UserBase, db: Annotated[Session, Depends(get_db)]):
    return create_user_service(db, request)
