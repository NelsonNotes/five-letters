from typing import Optional, List
from pydantic import BaseModel


from app.schemas.mixins import DateTimeSchemaMixin, IDSchemaMixin
from app.schemas.attempt import AttemptModel


# Properties to receive on User creation
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


# Properties to receive on User update
class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    avatar_url: str
    hash_password: str
    progress: int


class UserModel(BaseModel, DateTimeSchemaMixin, IDSchemaMixin):
    first_name: str
    last_name: str
    email: str
    avatar_url: str
    hash_password: str
    progress: int
    attempts: Optional[List[AttemptModel]] = None

    class Config:
        orm_mode: True
