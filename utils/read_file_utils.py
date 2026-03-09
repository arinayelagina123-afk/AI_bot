from pathlib import Path

REAL_DIR = Path(__file__).resolve().parent.parent


def read_file(file):
    with open(REAL_DIR / file, "r", encoding="utf-8") as f:
        return f.read()
