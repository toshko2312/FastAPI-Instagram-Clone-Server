from datetime import datetime

from db.schemas import CommentBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbComment
from auth.oauth2 import get_current_user
from typing import Annotated
from fastapi import Depends


def create_service(request: CommentBase, db: Session, user_username):
    new_comment = DbComment(
        text=request.text,
        username=user_username,
        post_id=request.post_id,
        timestamp=datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_service(post_id: int, db: Session):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()
