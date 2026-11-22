"""Plan missing publication slots and validate candidate Python projects."""
import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = date(2026, 11, 22)
CATEGORIES = {
    "A": ["retrieval evaluation", "machine learning", "NLP", "computer vision", "deep learning", "Python automation", "model deployment"],
    "B": ["ERP accounts payable", "developer utility", "ERP procurement", "business application", "ERP inventory", "database reporting", "ERP general ledger"],
}


def slots(until, track, records):
    day = START
    while day <= until:
        if (day.isoformat(), track) not in records:
            categories = CATEGORIES[track]
            yield day.isoformat(), track, categories[(day - START).days % len(categories)]
        day += timedelta(days=1)


def validate(root):
    for name in ["README.md", "faq.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", ".gitignore"]:
        if not (root / name).read_text().strip():
            raise ValueError(f"Empty required file: {name}")
    entries = re.split(r"(?m)^## (\d+)\. ", (root / "faq.md").read_text())[1:]
    if entries[::2] != list(map(str, range(1, 26))):
        raise ValueError("Number FAQ headings from 1 to 25")
    for entry in entries[1::2]:
        question, _, answer = entry.strip().partition("\n")
        if not question.endswith("?") or not answer.strip():
            raise ValueError("Each FAQ entry needs a question and an answer")


def index(records):
    lines = ["# Project index", "", "| Date | Track | Category | Project | Language | Stack | Build | Tests | Publication |", "|---|---|---|---|---|---|---|---|---|"]
    for row in sorted(records, key=lambda r: (r["date"], r["track"])):
        lines.append("| {date} | {track} | {category} | [{name}]({url}) | {language} | {stack} | {build} | {tests} | {publication} |".format(**row))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan")
    plan.add_argument("track", choices=CATEGORIES)
    plan.add_argument("until", type=date.fromisoformat)
    commands.add_parser("index")
    check = commands.add_parser("validate")
    check.add_argument("project", type=Path)
    args = parser.parse_args()
    records = [json.loads(path.read_text()) for path in (ROOT / "history").glob("*.json")]
    if args.command == "validate":
        validate(args.project)
    elif args.command == "index":
        print(index(records), end="")
    else:
        complete = {(r["date"], r["track"]) for r in records if r["publication"] == "verified"}
        for slot in slots(args.until, args.track, complete):
            print(*slot, sep=" | ")
