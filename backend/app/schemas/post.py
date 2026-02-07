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

class JobPost(PostBase):
    category: str | None = None

class TravelPost(PostBase):
    travel_date: date | None = None
    route: str | None = None

class PostPublic(PostBase):
    id: uuid.UUID
    post_type: PostType
