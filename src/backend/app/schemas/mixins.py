import datetime


class IDSchemaMixin:
    id: int


class DateTimeSchemaMixin:
    created_at: datetime.datetime
    updated_at: datetime.datetime
