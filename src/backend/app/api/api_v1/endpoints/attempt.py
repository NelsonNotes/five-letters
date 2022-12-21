from typing import List, Any
from app.db.tables import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.attempt import AttemptForClient, AttemptMake, AttemptCreate
from app.schemas.user import UserUpdate
from app.services.attempt import attemptService
from app.services.user import userService
from app.api import deps
from app.config import get_config

settings = get_config()
router = APIRouter()


@router.post("/", response_model=AttemptForClient)
def make_attempt(
    *,
    db: Session = Depends(deps.get_db),
    attempt_in: AttemptMake,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Make an attempt.
    """
    if len(attempt_in.attempt) != 5:
        raise HTTPException(
            status_code=400, detail="Word length must be 5 letters")
    obj_in = AttemptCreate(
        user_id=current_user.id, word_id=current_user.current_word_id, attempt=attempt_in.attempt)
    attempt = attemptService.create(db=db, obj_in=obj_in)
    letters_status_list = attemptService.check_attempt(attempt=attempt)
    attempt_response = AttemptForClient(
        attempt=attempt.attempt, letters_status=letters_status_list)

    if userService.check_next_word(db=db, user_id=current_user.id):
        user_obj_update = UserUpdate(
            current_word_id=current_user.current_word_id+1
        )
        userService.update(db=db, db_obj=current_user, obj_in=user_obj_update)
    return attempt_response
