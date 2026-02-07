from sqlalchemy.orm import Session
from app.models.report import Report


def list_reports(db: Session, limit: int = 50, offset: int = 0):
    return db.query(Report).offset(offset).limit(limit).all()


def create_report(db: Session, *, post_id, reporter_id, reason: str):
    report = Report(post_id=post_id, reporter_id=reporter_id, reason=reason)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
