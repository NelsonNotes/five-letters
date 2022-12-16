from app.schemas.word import WordCreate, WordUpdate
from app.db.tables import Word
from app.services.base import BaseService


class WordService(BaseService[Word, WordCreate, WordUpdate]):
    pass


wordService = WordService(Word)
