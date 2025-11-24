# Week 1 — Core Python & Engineering Hygiene (100% COMPLETE)

**Goal achieved:** Confident with Python idioms, packaging, testing, typing, Git workflows, and CLI tools.

**Finished in 5 real days** (21 Nov 2025) — ahead of schedule.

## Overview of Tasks

| Day | Task                                                                      | Status | Key Learnings & Proof                                 |
|-----|---------------------------------------------------------------------------|--------|--------------------------------------------------------|
| 1   | 5 small functions + pytest tests                                          | Done   | Clean utils, 100% coverage                             |
| 2   | OOP — BankAccount class with validation + tests                           | Done   | Encapsulation, `__str__`, proper exceptions            |
| 3   | Full type hints (PEP 484) + black + ruff                                  | Done   | Zero lint errors, `black .` → All done!                |
| 4   | pytest advanced — parametrize, fixtures, monkeypatch mocking             | Done   |  Fixtures, parametrize, Mocking, Monkey patch
| 5   | Mini-challenge: CSV → JSON summarizer CLI + tests                         | Done   | Professional `src/` layout, `pyproject.toml`, beautiful output |

## Highlights (senior-level polish)

- Every day has its own `README.md` + personal `NOTES.md`
- Proper project structure (`src/`, `tests/`, `data/`)
- All tests passing (`pytest -v` → 100% green)
- Zero lint/style issues (`black .` + `ruff` clean)
- Root-level `WEEK1_PROGRESS.md` + `LEARNING_LOG.md`
- Clean Git history with descriptive commits

## How to run everything

```bash
# From week1-python-foundation root
black .                     # formatting
ruff check --fix .          # linting
pytest                      # all tests → should pass
python -m src.main          # Day 5 CLI (in day5 folder)
