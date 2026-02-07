import uuid
from pydantic import BaseModel, ConfigDict

class MessageBase(BaseModel):
    to_user_id: uuid.UUID
    body: str

class MessagePublic(MessageBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    from_user_id: uuid.UUID


class MessageCreate(MessageBase):
    pass
