from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from services.post_services import create_post_service, get_all_posts_service
from db.schemas import PostBase, PostDisplay, UserAuth
from db.database import get_db
from typing import Annotated, List
import random
import string
import shutil
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/', response_model=PostDisplay)
def create(request: PostBase,
           db: Annotated[Session, Depends(get_db)],
           current_user: Annotated[UserAuth, Depends(get_current_user)]):
    return create_post_service(request, db)


@router.get('/all', response_model=List[PostDisplay])
def posts(db: Annotated[Session, Depends(get_db)]):
    return get_all_posts_service(db)


@router.post('/image')
def upload_image(image: Annotated[UploadFile, File(...)], current_user: Annotated[UserAuth, Depends(get_current_user)]):
    rand_str = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}