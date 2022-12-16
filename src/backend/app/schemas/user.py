from typing import Optional, List
from pydantic import BaseModel


from app.schemas.mixins import DateTimeSchemaMixin, IDSchemaMixin
from app.schemas.attempt import AttemptModel, AttemptForClient


# Properties to receive on User creation
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        orm_mode = True


# Properties to receive on User update
class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    avatar_url: Optional[str]
    hash_password: Optional[str]
    current_word_id: Optional[int]

    class Config:
        orm_mode = True


class UserModel(BaseModel, DateTimeSchemaMixin, IDSchemaMixin):
    first_name: str
    last_name: str
    email: str
    avatar_url:  Optional[str] = None
    current_word_id:  int
    attempts: List[AttemptForClient]

    class Config:
        orm_mode = True

    class Config:
        orm_mode = True
