import uuid
from pydantic import BaseModel

class ReportBase(BaseModel):
    post_id: uuid.UUID
    reason: str

class ReportPublic(ReportBase):
    id: uuid.UUID
    reporter_id: uuid.UUID


class ReportCreate(ReportBase):
    reporter_id: uuid.UUID
