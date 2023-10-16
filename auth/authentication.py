from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm.session import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import Annotated
from db.models import DbUser
from db.hashing import Hash
from auth.oauth2 import create_access_token


router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail='Invalid username'
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=404,
            detail='Incorrect password'
        )

    access_token = create_access_token(data={'username': user.username})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }