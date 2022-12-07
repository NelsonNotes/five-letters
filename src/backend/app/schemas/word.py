from typing import Optional
from app.schemas.mixins import DateTimeSchemaMixin, IDSchemaMixin

from pydantic import BaseModel


# Shared properties
class WordBase(BaseModel):
    word: Optional[str] = None


# Properties to receive on Word creation
class WordCreate(WordBase):
    word: str


# Properties to receive on Word update
class WordUpdate(WordBase):
    pass


class WordModel(WordBase, DateTimeSchemaMixin, IDSchemaMixin):
    word: str

    class Config:
        orm_mode: True
