from typing import List
from sqlalchemy.orm import Session
from typing import Optional, List


from app.core.security import get_password_hash, verify_password
from app.schemas.user import UserCreate, UserUpdate, UserModel
from app.schemas.attempt import AttemptForClient
from app.db.tables import User
from app.services.base import BaseService
from app.services.attempt import attemptService


class UserService(BaseService[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hash_password=get_password_hash(obj_in.password),
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            current_word_id=1
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: UserUpdate
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "password" in update_data:
            if update_data["password"]:
                hash_password = get_password_hash(update_data["password"])
                del update_data["password"]
                update_data["hash_password"] = hash_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hash_password):
            return None
        return user

    def get_with_client_attempts(self, db: Session, *, user_id: int) -> UserModel:
        user = self.get(db=db, id=user_id)
        attemptsForClient: List[AttemptForClient] = []
        for attempt in user.attempts:
            if attempt.word_id == user.current_word_id:
                newAttemptForClient = AttemptForClient(
                    attempt=attempt.attempt,
                    letters_status=attemptService.check_attempt(attempt)
                )
                attemptsForClient.append(newAttemptForClient)
        user_model = UserModel(first_name=user.first_name, last_name=user.last_name, email=user.email,
                               avatar_url=user.avatar_url, current_word_id=user.current_word_id, attempts=attemptsForClient)
        return user_model

    def check_next_word(self, db: Session, *, user_id: int) -> bool:
        user_with_attempts = userService.get_with_client_attempts(
            db=db, user_id=user_id)
        attempts_as_list: List[List[int]] = []
        for attempt in user_with_attempts.attempts:
            attempts_as_list.append(attempt.letters_status)
        return len(user_with_attempts.attempts) >= 6 or [2, 2, 2, 2, 2] in attempts_as_list


userService = UserService(User)
