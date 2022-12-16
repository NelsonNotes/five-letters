from typing import Any, List
from app.db.tables import User
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session


from app.schemas.user import UserCreate, UserUpdate, UserModel
from app.services.user import userService
from app.api import deps
from app.config import get_config

settings = get_config()
router = APIRouter()


@router.post("/", response_model=UserModel)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user: UserModel = Depends(deps.get_current_superuser),
) -> Any:
    """
    Create new user.
    """
    user = userService.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = userService.create(db, obj_in=user_in)
    return user


@router.get("/", response_model=UserModel)
def get_user_with_attempts(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new user.
    """
    user: UserModel = userService.get_with_client_attempts(
        db=db, user_id=current_user.id)
    return user
