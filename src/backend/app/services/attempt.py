from typing import List

from app.core.game import check_word
from app.schemas.attempt import AttemptCreate, AttemptUpdate
from app.db.tables import Attempt
from app.services.base import BaseService


class AttemptService(BaseService[Attempt, AttemptCreate, AttemptUpdate]):
    def check_attempt(self, attempt: Attempt) -> List[int]:
        return check_word(attempt=attempt.attempt, word=attempt.word.word)


attemptService = AttemptService(Attempt)
