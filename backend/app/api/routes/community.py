from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.comment import CommentCreate, CommentPublic
from app.schemas.message import MessageCreate, MessagePublic
from app.schemas.report import ReportCreate, ReportPublic
from app.services import comment_service, message_service, report_service

router = APIRouter(prefix="/community", tags=["community"])


@router.get("/comments/{post_id}", response_model=list[CommentPublic])
def list_comments(post_id, limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return comment_service.list_comments(db, post_id, limit=limit, offset=offset)


@router.post("/comments", response_model=CommentPublic)
def create_comment(payload: CommentCreate, db: Session = Depends(get_db)):
    return comment_service.create_comment(db, post_id=payload.post_id, user_id=payload.user_id, body=payload.body)


@router.get("/messages", response_model=list[MessagePublic])
def list_messages(user_id, limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return message_service.list_messages_for_user(db, user_id, limit=limit, offset=offset)


@router.post("/messages", response_model=MessagePublic)
def create_message(payload: MessageCreate, db: Session = Depends(get_db)):
    return message_service.create_message(
        db,
        from_user_id=payload.from_user_id,
        to_user_id=payload.to_user_id,
        body=payload.body,
    )


@router.post("/reports", response_model=ReportPublic)
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    return report_service.create_report(db, post_id=payload.post_id, reporter_id=payload.reporter_id, reason=payload.reason)
