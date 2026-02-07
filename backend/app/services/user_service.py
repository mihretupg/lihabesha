from sqlalchemy.orm import Session
from app.models.user import User


def get_user(db: Session, user_id):
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def list_users(db: Session, limit: int = 50, offset: int = 0):
    return db.query(User).offset(offset).limit(limit).all()


def create_user(db: Session, *, email: str, password_hash: str, phone: str | None = None,
                name: str | None = None, city: str | None = None,
                language: str | None = None, role: str = "user"):
    user = User(
        email=email,
        password_hash=password_hash,
        phone=phone,
        name=name,
        city=city,
        language=language,
        role=role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
