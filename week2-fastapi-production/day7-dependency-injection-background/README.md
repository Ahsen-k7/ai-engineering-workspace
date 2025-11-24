# Week 2 – Day 2: Dependency Injection + Background Tasks + File Upload  
**STATUS: 100% COMPLETE** — Solo

**Official topics covered (exactly as per plan):**
- Dependency injection → Pydantic Settings + root .env + Depends()
- Background tasks → Welcome email runs after response (simulated)
- File uploads → Instant accept + background processing
- Real-world patterns (no hardcoding, production config)

**Features implemented:**
- Single root `.env` at workspace level (used by all days)
- Config injected safely (ADMIN_EMAIL, DEBUG, etc.)
- Background tasks using `BackgroundTasks.add_task`
- File upload with `UploadFile` + background processing
- Automatic OpenAPI docs at http://127.0.0.1:8000/docs
- Poetry + clean src/ layout

**How to run:**
```bash
cd backend
poetry install
poetry run uvicorn src.main:app --reload