# Week 1 — Day 3: Typing + Linting (complete)

**Task**: add type hints + run black/ruff on the entire week1 folder

### Done:
- Added full PEP 484 type hints to **all** Day 1 functions and Day 2 `BankAccount` class  
  (see updated files in `day1-small-functions/` and `day2-oop/`)
- Installed and ran `black .` → 3 files reformatted, “All done!”
- Installed and ran `ruff check --fix .` → “All checks passed!” (zero issues)
- Updated `requirements.txt` with black + ruff + mypy

### Proof (terminal output)
```bash
$ black .
reformatted ... (3 files)
All done!

$ ruff check --fix .
All checks passed!