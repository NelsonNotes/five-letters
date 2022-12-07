from typing import Optional
from pydantic import BaseModel


# from app.schemas.user import UserModel
from app.schemas.word import WordModel
from app.schemas.mixins import DateTimeSchemaMixin, IDSchemaMixin


# Shared properties
class AttemptBase(BaseModel):
    userId: Optional[int] = None
    # user: Optional[UserModel] = None
    wordId: Optional[int] = None
    word: Optional[WordModel] = None
    attempt: Optional[str] = None


# Properties to receive on Attempt creation
class AttemptCreate(AttemptBase):
    userId: int
    wordId: int
    attempt: str


class AttemptModel(AttemptBase, DateTimeSchemaMixin, IDSchemaMixin):
    userId: int
    # user: UserModel
    wordId: int
    word: WordModel
    attempt: int

    class Config:
        orm_mode: True
