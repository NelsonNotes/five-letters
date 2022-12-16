from sqlalchemy import Column, Integer, String, Boolean
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
    current_word_id = Column(Integer, ForeignKey(
        "word.id"), server_default='1')
    attempts = relationship("Attempt", back_populates="user")
    is_admin = Column(Boolean, nullable=False, server_default='false')


class Word(Base, IDMixin, DateTimeMixin):
    __tablename__ = "word"

    word = Column(String, nullable=False)


class Attempt(Base, IDMixin, DateTimeMixin):
    __tablename__ = "attempt"

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="attempts")
    word_id = Column(Integer, ForeignKey("word.id"))
    word = relationship("Word")
    attempt = Column(String, nullable=False)
