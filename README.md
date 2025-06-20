# FastAPI-Experiments

Experimenting building a basic CRUD API following a TDD dev style with CI/CD tools

## Technologies Used

Python 3.13, FastAPI, SQLAlchemy, Alembic, Pydantic, Pytest, Poetry w/ taskipy & ruff

## Shortcuts

### Install Dependencies

```bash
poetry install
```

### Check linter (Ruff)

```bash
poetry run task lint
```

### Format code (Ruff)

```bash
poetry run task format
```

### Test code (PyTest)

```bash
poetry run task test
```

### Run the API

```bash
poetry run task run
```
