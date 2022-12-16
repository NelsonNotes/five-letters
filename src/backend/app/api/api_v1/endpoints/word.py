from typing import Any, List
from app.db.tables import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.schemas.word import WordCreate, WordModel
from app.schemas.user import UserModel

from app.services.word import wordService

from app.api import deps
from app.config import get_config

settings = get_config()
router = APIRouter()


@router.post("/", response_model=WordModel)
def create_word(
    *,
    db: Session = Depends(deps.get_db),
    word_in: WordCreate,
    current_user: UserModel = Depends(deps.get_current_superuser),
) -> Any:
    """
    Create new word.
    """
    word = wordService.create(db, obj_in=word_in)
    return word
