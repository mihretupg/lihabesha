from pydantic import BaseModel

class ReportBase(BaseModel):
    post_id: str
    reason: str

class ReportPublic(ReportBase):
    id: str
    reporter_id: str
