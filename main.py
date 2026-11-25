#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line -- a review of my own Monday -- to /output/entry.txt.
Deterministic: the same fixed string on every run, no randomness,
no clock, no input, no network. Standard library only.
"""

import os
import stat

ENTRY = (
    "Monday: my alarm showed up, my motivation didn't, "
    "and the 9 a.m. 'quick sync' is still holding my soul hostage."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
