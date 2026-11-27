#!/usr/bin/env python3
"""One funny sick-day excuse, written to the grader's file.

Running this program writes a single fixed line to /output/entry.txt
and prints it. The line never changes between runs.

The joke: a back injury is half-believable, but the cause is pure
celebration. The day off itself hurt the back, so the cure is
another day off, and the twist lands on the last words.
"""

import os
from pathlib import Path

# One line, 117 characters: short enough for the gate, long enough
# for the setup, the injury, and the punchline at the end.
EXCUSE = (
    "Calling in sick \u2014 my back went out celebrating that I finally "
    "had a day off, so now I need a day off from my day off."
)


def entry_path() -> Path:
    """Return the file the grader reads, honouring OUTPUT_DIR."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def gate(text: str) -> None:
    """Fail loudly unless the text fits the competition's gate."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def run() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    saved = target.read_text(encoding="utf-8")
    if saved != EXCUSE:
        raise SystemExit("written entry differs from EXCUSE")
    gate(saved)
    print(EXCUSE)


run()
