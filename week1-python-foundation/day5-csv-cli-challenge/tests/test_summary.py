# tests/test_summary.py
from src.summarizer import csv_to_summary
from pathlib import Path


def test_summary_works():
    result = csv_to_summary(Path("data/people.csv"))
    
    assert result["total_rows"] == 4
    assert result["total_columns"] == 3
    assert "age" in result["numeric_summary"]
    assert result["numeric_summary"]["age"]["average"] == 26.0
    assert result["numeric_summary"]["salary"]["max"] == 60000