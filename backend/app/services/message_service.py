from sqlalchemy.orm import Session
from app.models.message import Message


def list_messages_for_user(db: Session, user_id, limit: int = 50, offset: int = 0):
    return (
        db.query(Message)
        .filter((Message.from_user_id == user_id) | (Message.to_user_id == user_id))
        .offset(offset)
        .limit(limit)
        .all()
    )


def create_message(db: Session, *, from_user_id, to_user_id, body: str):
    message = Message(from_user_id=from_user_id, to_user_id=to_user_id, body=body)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
