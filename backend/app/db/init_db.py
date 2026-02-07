from app.db.session import engine
from app.db.base import Base
from app.models import user, post, message, comment, report, moderation_action


def init_db():
    # Import models above so they are registered with Base.metadata
    Base.metadata.create_all(bind=engine)
