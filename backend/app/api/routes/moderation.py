from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.report import ReportPublic
from app.services import report_service

router = APIRouter(prefix="/moderation", tags=["moderation"])


@router.get("/reports", response_model=list[ReportPublic])
def list_reports(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return report_service.list_reports(db, limit=limit, offset=offset)
