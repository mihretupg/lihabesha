import uuid
from pydantic import BaseModel

class CommentBase(BaseModel):
    post_id: uuid.UUID
    body: str

class CommentPublic(CommentBase):
    id: uuid.UUID
    user_id: uuid.UUID


class CommentCreate(CommentBase):
    user_id: uuid.UUID
