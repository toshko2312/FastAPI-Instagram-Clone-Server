from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import Annotated, List
from db.database import get_db
from db.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user
from services.comment_services import create_service, get_all_service

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.get('/all/{post_id}', status_code=200)
def comments(post_id: int, db: Annotated[Session, Depends(get_db)]):
    return get_all_service(post_id, db)


@router.post('/', status_code=201)
def create(request: CommentBase,
           db: Annotated[Session, Depends(get_db)], current_user: Annotated[UserAuth, Depends(get_current_user)]):
    create_service(request, db, current_user.username)