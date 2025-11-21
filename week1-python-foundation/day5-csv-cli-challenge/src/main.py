# src/main.py
import json
from pathlib import Path
from src.summarizer import csv_to_summary


def main():
    # Change this path to your CSV file
    csv_file = Path("data/people.csv")

    if not csv_file.exists():
        print("File not found!")
        return

    summary = csv_to_summary(csv_file)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()