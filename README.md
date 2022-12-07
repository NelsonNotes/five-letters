# five-letters

## bootstrap

```bash
poetry install
```

## migrations

### new (autogenerate by changing /app/db/entities/tables.py):

```bash
poetry run alembic revision --autogenerate -m 'add users table'
```

### run all:

```bash
poetry run alembic upgrade head
```
