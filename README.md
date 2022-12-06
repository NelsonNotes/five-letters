# five-letters

## bootstrap

```bash
poetry install
```

## migrations

### new:

```bash
poetry run alembic revision --autogenerate -m 'add users table'
```

### run all:

```bash
poetry run alembic upgrade head
```
