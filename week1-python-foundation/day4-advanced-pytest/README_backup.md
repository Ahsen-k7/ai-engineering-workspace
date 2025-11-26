# Day 4 — Advanced Pytest: Parametrization, Fixtures & Mocking

## 📌 Topics Covered
- Parametrized tests
- Advanced fixtures
- Mocking with `unittest.mock.patch`
- Monkeypatching external APIs
- Creating fake responses for APIs
- Testing without internet or real API calls

## 📁 Project Structure
```
day4-advanced-pytest/
│── src/
│     ├── calculator.py
│     └── external_api.py
│── tests/
│     ├── calculator_test.py
│     ├── test_external_api_patch.py
│     └── test_external_api_monkeypatch.py
│── requirements.txt
│── pyproject.toml
```

## 🧪 How to Run Tests
```bash
pytest -v
```

## 🧠 Concepts Learned
- How to test multiple inputs with one test function
- How fixtures simplify repeated setups
- How to mock API calls using:
  - `patch`
  - `monkeypatch`
- Why mocking is essential for reliable tests
- How to test external dependencies safely

This day covers professional testing patterns used in backend & AI engineering.
