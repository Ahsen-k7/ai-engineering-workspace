# src/summarizer.py
import csv
from pathlib import Path
from typing import Dict, Any, List


def csv_to_summary(csv_path: Path) -> Dict[str, Any]:
    """
    Reads a CSV file and returns a summary dictionary
    """
    # 1. Read the CSV
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)          # all rows as list of dicts

    if not rows:
        return {"error": "CSV is empty"}

    # 2. Basic info
    columns = list(rows[0].keys())
    result = {
        "total_rows": len(rows),
        "total_columns": len(columns),
        "columns": columns,
        "numeric_summary": {}
    }

    # 3. Find numeric columns and calculate min/max/avg
    for col in columns:
        # Try to convert all values in this column to numbers
        numbers = []
        for row in rows:
            value = row[col].strip()
            try:
                numbers.append(float(value))
            except ValueError:
                pass  # not a number, skip

        if numbers:  # only if we found at least one number
            result["numeric_summary"][col] = {
                "min": min(numbers),
                "max": max(numbers),
                "average": round(sum(numbers) / len(numbers), 2)
            }

    return result