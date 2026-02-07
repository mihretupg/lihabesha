from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserPublic
from app.services import user_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users", response_model=list[UserPublic])
def list_users(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return user_service.list_users(db, limit=limit, offset=offset)
