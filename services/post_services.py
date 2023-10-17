from db.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost
from datetime import datetime
from fastapi import HTTPException


def create_post_service(request: PostBase, db: Session, user_id: int):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts_service(db: Session):
    return db.query(DbPost).all()


def delete_post_service(id: int, db: Session, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f'Post with id {id} not found.')
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail='Only post creator can delete post')
    db.delete(post)
    db.commit()
    return
