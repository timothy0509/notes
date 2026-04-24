# AGENTS.md - Trial SBA Backend

## Critical Architecture Gotcha

**`models.py` and `routes.py` use incompatible database patterns.**
- `models.py` defines plain Python classes with **raw PyMySQL SQL** via `db.py`.
- `routes.py` treats the same imports as **Flask-SQLAlchemy ORM** models (`.query`, `.to_dict()`, `db.session`).
- `app.py` calls `db.create_all()` on import, but the classes in `models.py` are not SQLAlchemy models, so no tables are auto-generated from them.
- **Implication:** Changing one file without aligning the other will break the app at runtime. If you need to change the data layer, decide on ONE pattern and make both files consistent.

## Environment & Commands

All commands run from `backend/`:

| Task | Command |
|------|---------|
| Install deps | `pip install -r requirements.txt` |
| Create DB | `python init_db.py` |
| Run server | `python app.py` |

- Server starts at `http://localhost:5000` with `debug=True`.
- **Required order:** install deps → create DB → run server.

## Database

- **Engine:** MySQL via PyMySQL
- **Hardcoded config** (repeated in `app.py`, `db.py`, `init_db.py`):
  - Host: `localhost`
  - Port: `3307` (non-standard; default is 3306)
  - DB: `todo_db`
  - User: `root`
  - Password: `usbw`
- `init_db.py` only creates the database schema; it does **not** create tables. Table creation is left to `db.create_all()` in `app.py`, which currently has no effect because `models.py` lacks SQLAlchemy model definitions.

## API Conventions

- Base path: `/api/`
- JSON request/response throughout.
- **Task `due_date`:** accepts `%Y-%m-%d` string, stored as `date`.
- **Reminder `reminder_time`:** accepts ISO format string (`datetime.fromisoformat`).
- `POST` endpoints return `201` on success.
- `GET /api/health` exists for a basic health check.

## Project Boundaries

- This repo contains **only the Flask backend** (`backend/`). No frontend code, no build pipeline, no tests.
- `ER Diagram.md` at repo root defines the intended schema and is the source of truth for relationships.

## Operational Notes

- **CORS** is enabled globally (`Flask-CORS`) in `app.py`.
- No test suite exists; verify changes by running the server and hitting endpoints manually or with curl.
- If adding SQLAlchemy models, define them in `models.py` using `db.Model` (from `extensions.py`) so `db.create_all()` in `app.py` actually creates tables, and ensure `routes.py` method signatures stay in sync.
