from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.post_services import create_post_service, get_all_posts_service
from db.schemas import PostBase, PostDisplay
from db.database import get_db
from typing import Annotated, List

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/', response_model=PostDisplay)
def create(request: PostBase, db: Annotated[Session, Depends(get_db)]):
    return create_post_service(request, db)


@router.get('/all', response_model=List[PostDisplay])
def posts(db: Annotated[Session, Depends(get_db)]):
    return get_all_posts_service(db)