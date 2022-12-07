from sqlalchemy import Column, Integer, DateTime, func


class IDMixin:
    id = Column(Integer, primary_key=True)


class DateTimeMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
