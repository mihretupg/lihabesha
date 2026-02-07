from enum import Enum
import uuid
from pydantic import BaseModel
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
    owner_id: uuid.UUID

class JobPost(PostBase):
    category: str | None = None


class JobPostCreate(JobPost):
    owner_id: uuid.UUID

class TravelPost(PostBase):
    travel_date: date | None = None
    route: str | None = None


class TravelPostCreate(TravelPost):
    owner_id: uuid.UUID


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
    id: uuid.UUID
    post_type: PostType
