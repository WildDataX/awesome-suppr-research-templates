from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".csv", ".txt"}
MOJIBAKE_MARKERS = [
    "\ufffd",
    "锛",
    "鐮",
    "绉",
    "璁",
    "鎻",
    "鈥",
    "歨ttps",
]


def validate_text_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "runs" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                errors.append(f"{path.relative_to(ROOT)} contains mojibake marker {marker!r}")
                break
    return errors


def validate_csv_files() -> list[str]:
    errors: list[str] = []
    seen_terms: dict[str, Path] = {}
    for path in ROOT.rglob("*.csv"):
        if ".git" in path.parts or "runs" in path.parts:
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            errors.append(f"{path.relative_to(ROOT)} has no rows")
            continue
        if "English" in rows[0]:
            for row in rows:
                term = row.get("English", "").strip().lower()
                if not term:
                    errors.append(f"{path.relative_to(ROOT)} has empty English term")
                    continue
                if term in seen_terms:
                    errors.append(
                        f"duplicate glossary term {term!r}: {path.relative_to(ROOT)} and {seen_terms[term].relative_to(ROOT)}"
                    )
                seen_terms[term] = path
    return errors


def validate_index() -> list[str]:
    errors: list[str] = []
    index = json.loads((ROOT / "resource-index.json").read_text(encoding="utf-8-sig"))
    for pack in index.get("packs", []):
        for key in ["path", "download"]:
            target = ROOT / pack[key]
            if not target.exists():
                errors.append(f"resource-index missing {key}: {pack[key]}")
    return errors


def main() -> None:
    errors = validate_text_files() + validate_csv_files() + validate_index()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("content validation passed")


if __name__ == "__main__":
    main()
