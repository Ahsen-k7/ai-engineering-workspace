# Day 5 – Mini-challenge: CSV → Summarised JSON CLI Tool (100% COMPLETE)

**Task:** Build a CLI tool that reads any CSV file and outputs a clean JSON summary with:
- Row & column count
- List of columns
- Min / Max / Average for every numeric column

### Features
- Proper `src/` layout (real project structure)
- Uses `pathlib`, `csv`, type hints
- Smart numeric column detection
- Beautiful indented JSON output
- Works from any directory thanks to `PROJECT_ROOT`
- Fixed classic import errors with `pyproject.toml` + `__init__.py`

### How to run
```bash
# From the day5 folder
python -m src.main                     # prints pretty JSON
pytest -v                              # 100% tests pass
