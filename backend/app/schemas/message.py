from pydantic import BaseModel

class MessageBase(BaseModel):
    to_user_id: str
    body: str

class MessagePublic(MessageBase):
    id: str
    from_user_id: str
