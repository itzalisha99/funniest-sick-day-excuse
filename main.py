#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line, under 200 characters, to /output/entry.txt:
a sick-day excuse a boss might half believe and a coworker would laugh at.
"""

import os

ENTRY = (
    "Sorry, can't come in. I woke up with a crick in my neck so bad "
    "I can only nod, which my boss would take as agreement to everything."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: refuse to write an invalid entry.

    The sealed scorer gives Valid 0 (no prize, no judge) unless the file
    is UTF-8 text of 1 to 200 characters and not only white space, so
    check the same conditions here before anything is written.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")  # raises if the entry is not valid UTF-8
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
