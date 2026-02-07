from enum import Enum
import uuid
from pydantic import BaseModel, EmailStr, ConfigDict

class UserRole(str, Enum):
    guest = "guest"
    user = "user"
    moderator = "moderator"
    admin = "admin"

class UserBase(BaseModel):
    email: EmailStr
    phone: str | None = None
    name: str | None = None
    city: str | None = None
    language: str | None = None

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    role: UserRole = UserRole.user


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
