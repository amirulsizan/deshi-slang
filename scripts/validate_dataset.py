#!/usr/bin/env python3
"""Simple dataset validator for deshi-slang JSONL files."""
import sys
import json
from pathlib import Path

REQUIRED_FIELDS = {"id", "text", "labels", "language", "split"}
ALLOWED_LABELS = {"abusive", "slur", "derogatory", "sexual", "slang", "neutral"}


def validate_line(obj, line_no):
    missing = REQUIRED_FIELDS - obj.keys()
    if missing:
        return False, f"Line {line_no}: missing fields {missing}"
    if not isinstance(obj["labels"], list):
        return False, f"Line {line_no}: 'labels' must be a list"
    for l in obj["labels"]:
        if l not in ALLOWED_LABELS:
            return False, f"Line {line_no}: unknown label '{l}'"
    if not obj.get("language"):
        return False, f"Line {line_no}: empty language"
    return True, None


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_dataset.py path/to/file.jsonl")
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(2)

    errors = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception as e:
            errors.append(f"Line {i}: JSON parse error: {e}")
            continue
        ok, msg = validate_line(obj, i)
        if not ok:
            errors.append(msg)

    if errors:
        print("Validation failed with the following issues:")
        for e in errors[:100]:
            print(" -", e)
        sys.exit(1)
    print("Validation passed: no issues found.")


if __name__ == "__main__":
    main()
