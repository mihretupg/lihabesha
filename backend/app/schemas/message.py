import uuid
from pydantic import BaseModel

class MessageBase(BaseModel):
    to_user_id: uuid.UUID
    body: str

class MessagePublic(MessageBase):
    id: uuid.UUID
    from_user_id: uuid.UUID


class MessageCreate(MessageBase):
    from_user_id: uuid.UUID
