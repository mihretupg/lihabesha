from sqlalchemy import String, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

class ModerationAction(Base):
    __tablename__ = "moderation_actions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    actor_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    target_post_id: Mapped[str] = mapped_column(String(36), ForeignKey("posts.id"))
    action: Mapped[str] = mapped_column(String(50))  # approved, removed, flagged
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    actor = relationship("User", back_populates="moderation_actions")
    target_post = relationship("Post")
