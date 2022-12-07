from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship, declarative_base

from app.db.mixins import IDMixin, DateTimeMixin


Base = declarative_base()


class User(Base, IDMixin, DateTimeMixin):
    __tablename__ = "user"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    avatar_url = Column(String)
    hash_password = Column(String, nullable=False)
    progress = Column(Integer, nullable=False)
    attempts = relationship("Attempt", back_populates="user")

    class Config:
        orm_mode: True


class Word(Base, IDMixin, DateTimeMixin):
    __tablename__ = "word"

    word = Column(String, nullable=False)

    class Config:
        orm_mode: True


class Attempt(Base, IDMixin, DateTimeMixin):
    __tablename__ = "attempt"

    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="attempts")
    wordId = Column(Integer, ForeignKey("word.id"))
    word = relationship("Word")
    attempt = Column(String, nullable=False)

    class Config:
        orm_mode: True
