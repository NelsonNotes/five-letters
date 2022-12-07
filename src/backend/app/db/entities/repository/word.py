from app.schemas.word import WordCreate, WordUpdate
from app.db.tables import Word
from app.db.entities.repository.base import CRUDBase


class CRUDWord(CRUDBase[Word, WordCreate, WordUpdate]):
    pass


wordRepository = CRUDWord(Word)
