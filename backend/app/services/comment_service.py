from sqlalchemy.orm import Session
from app.models.comment import Comment


def list_comments(db: Session, post_id, limit: int = 50, offset: int = 0):
    return (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .offset(offset)
        .limit(limit)
        .all()
    )


def create_comment(db: Session, *, post_id, user_id, body: str):
    comment = Comment(post_id=post_id, user_id=user_id, body=body)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment
