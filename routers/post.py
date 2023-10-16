from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.post_services import create_post_service
from db.schemas import PostBase, PostDisplay
from db.database import get_db
from typing import Annotated

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/', response_model=PostDisplay)
def create(request: PostBase, db: Annotated[Session, Depends(get_db)]):
    return create_post_service(request, db)