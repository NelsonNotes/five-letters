from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session


from app.schemas.user import UserCreate, UserUpdate, UserModel
from app.db.entities.repository.user import userRepository
from app.api import deps
from app.config import get_config

settings = get_config()
router = APIRouter()


@router.post("/", response_model=UserModel)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user: UserModel = Depends(deps.get_current_user),
) -> Any:
    """
    Create new user.
    """
    user = userRepository.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = userRepository.create(db, obj_in=user_in)
    return user


@router.get("/", response_model=UserModel)
def get_users(
    *,
    db: Session = Depends(deps.get_db),
    current_user: UserModel = Depends(deps.get_current_user),
) -> List[UserModel]:
    """
    Get all users.
    """
    users = userRepository.get_multi(db)
    if not len(users):
        raise HTTPException(
            status_code=404,
            detail="No one users found.",
        )
    return users


@router.get("/no-auth")
def open_route(current_user=Depends(deps.get_current_user)):
    return {"detail": "Yeeeeah man dat's open route"}
