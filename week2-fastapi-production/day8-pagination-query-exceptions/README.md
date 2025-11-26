# Week 2 Day 8 – Pagination + Query Params + Exception Handlers (COMPLETE)

**Official Task:** Add pagination, query params, and exception handlers.

**Done:**
- `GET /notes/?skip=20&limit=5&search=important&category=important`
- Full validation + clean error messages
- Custom 400 error instead of crash on bad skip
- Search + tag/category filtering
- 100+ fake notes for real pagination testing
- Structured logging on every request, filter, and error (INFO/WARNING/ERROR levels)

**Run:**
```bash
cd backend
poetry install
poetry run uvicorn src.main:app --reload