from pydantic import BaseModel

class CommentBase(BaseModel):
    post_id: str
    body: str

class CommentPublic(CommentBase):
    id: str
    user_id: str
