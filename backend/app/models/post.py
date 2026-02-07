import uuid
from sqlalchemy import String, DateTime, Text, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_type: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # housing, job, travel
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    city: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    price: Mapped[float | None] = mapped_column(Float, nullable=True)

    # housing fields
    availability_date: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    room_type: Mapped[str | None] = mapped_column(String(60), nullable=True)

    # job fields
    job_category: Mapped[str | None] = mapped_column(String(120), nullable=True)

    # travel fields
    travel_date: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    route: Mapped[str | None] = mapped_column(String(200), nullable=True)

    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), index=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)

    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    reports = relationship("Report", back_populates="post")
