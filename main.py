#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single original line roasting our own fridge to /output/entry.txt.
Pure stdlib; deterministic.
"""

import os
import sys

LINE = (
    "My fridge's ice maker growls, rattles, then drops two cubes "
    "like it's doing me a favour — the laziest employee in the house."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"line length {len(text)} out of gate range", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
