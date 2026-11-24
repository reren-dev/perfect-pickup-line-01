#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun entry.

Writes one short pickup line an AI agent could actually say out loud
to /output/entry.txt (and prints it). The line is fixed: the same
bytes on every run, so the two grading runs are byte-identical.
"""

import os
import sys

LINE = (
    "I ran a million simulations of this moment. In every one, you "
    "smiled, so I stopped simulating and came to say hi."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
