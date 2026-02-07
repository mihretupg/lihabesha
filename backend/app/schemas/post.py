from enum import Enum
import uuid
from pydantic import BaseModel, Field
from pydantic import ConfigDict
from datetime import date

class PostType(str, Enum):
    housing = "housing"
    job = "job"
    travel = "travel"

class PostBase(BaseModel):
    title: str
    description: str
    city: str | None = None
    price: float | None = None

class HousingPost(PostBase):
    availability_date: date | None = None
    room_type: str | None = None


class HousingPostCreate(HousingPost):
    pass

class JobPost(PostBase):
    category: str | None = None


class JobPostCreate(JobPost):
    pass

class TravelPost(PostBase):
    travel_date: date | None = None
    route: str | None = None


class TravelPostCreate(TravelPost):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    city: str | None = None
    price: float | None = None
    availability_date: date | None = None
    room_type: str | None = None
    category: str | None = None
    travel_date: date | None = None
    route: str | None = None

class PostPublic(PostBase):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: uuid.UUID
    post_type: PostType
    availability_date: date | None = None
    room_type: str | None = None
    category: str | None = Field(default=None, alias="job_category")
    travel_date: date | None = None
    route: str | None = None
