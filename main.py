#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse.

Writes one razor-sharp sick-day excuse, 200 characters or fewer,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "Calling in sick \u2014 my back went out celebrating that I finally "
    "had a day off, so now I need a day off from my day off."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check gate: the file must hold exactly the entry, inside the
    # competition gate (UTF-8, 1-200 chars, not only whitespace, one line).
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry outside 1-200 characters"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"
    print(ENTRY)


if __name__ == "__main__":
    main()
