import uuid
from pydantic import BaseModel, ConfigDict

class ReportBase(BaseModel):
    post_id: uuid.UUID
    reason: str

class ReportPublic(ReportBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    reporter_id: uuid.UUID


class ReportCreate(ReportBase):
    pass
