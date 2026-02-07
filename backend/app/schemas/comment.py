import uuid
from pydantic import BaseModel, ConfigDict

class CommentBase(BaseModel):
    post_id: uuid.UUID
    body: str

class CommentPublic(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID


class CommentCreate(CommentBase):
    pass
