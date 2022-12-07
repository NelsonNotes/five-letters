from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship, declarative_base

from app.db.entities.mixins import IDMixin, DateTimeMixin


Base = declarative_base()


class User(Base, IDMixin, DateTimeMixin):
    __tablename__ = "user"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    avatar_url = Column(String)
    hash_password = Column(String, nullable=False)
    progress = Column(Integer, nullable=False)
    achievements = relationship("Achievement", secondary="user_achievement")
    attempts = relationship("Attempt", back_populates="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Word(Base, IDMixin, DateTimeMixin):
    __tablename__ = "word"

    word = Column(String, nullable=False)


class Achievement(Base, IDMixin, DateTimeMixin):
    __tablename__ = "achievement"

    name = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)


class UserAchievement(Base, IDMixin, DateTimeMixin):
    __tablename__ = "user_achievement"

    userId = Column(Integer, ForeignKey("user.id"))
    achievementId: Column(Integer, ForeignKey("achievement.id"))


class Attempt(Base, IDMixin, DateTimeMixin):
    __tablename__ = "attempt"

    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="attempts")
    wordId = Column(Integer, ForeignKey("word.id"))
    word = relationship("Word")
    attempt = Column(String, nullable=False)
