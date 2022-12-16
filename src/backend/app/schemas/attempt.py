from typing import Optional, List
from pydantic import BaseModel


# from app.schemas.user import UserModel
from app.schemas.word import WordModel
from app.schemas.mixins import DateTimeSchemaMixin, IDSchemaMixin


# Shared properties
class AttemptBase(BaseModel):
    user_id: Optional[int] = None
    word_id: Optional[int] = None
    attempt: Optional[str] = None


# Properties to receive on Attempt creation
class AttemptCreate(AttemptBase):
    user_id: int
    word_id: int
    attempt: str


class AttemptMake(BaseModel):
    attempt: str


# Properties to receive on Word update
class AttemptUpdate(AttemptBase):
    pass


class AttemptForClient(BaseModel):
    attempt: str
    letters_status: List[int]

    class Config:
        orm_mode = True


class AttemptModel(AttemptBase, DateTimeSchemaMixin, IDSchemaMixin):
    user_id: int
    word_id: int
    attempt: str

    class Config:
        orm_mode = True
