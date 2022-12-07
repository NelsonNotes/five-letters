from app.schemas.attempt import AttemptCreate, AttemptUpdate
from app.db.tables import Attempt
from app.db.entities.repository.base import CRUDBase


class CRUDAttempt(CRUDBase[Attempt, AttemptCreate, AttemptUpdate]):
    pass


attemptRepository = CRUDAttempt(Attempt)
