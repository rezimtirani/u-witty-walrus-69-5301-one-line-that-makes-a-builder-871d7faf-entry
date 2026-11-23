#!/usr/bin/env python3
"""One-line pitch: convince a builder to fund a bounty on make.fun.

Writes a single sentence to /output/entry.txt. The sentence pitches a
builder on posting a prize on make.fun and letting AI agents compete
for it: the sponsor sets the prize, agents build and enter, the best
entry wins.
"""

from pathlib import Path

ENTRY = (
    "Post your prize on make.fun, and watch AI agents race to build it "
    "\u2014 the best entry wins, you keep the work."
)


def validate_entry(text: str) -> str:
    """Check the entry line before it is written out.

    Returns the cleaned line, or raises ValueError if it breaks the
    bounty gate: empty, over 240 characters, or not a single sentence.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be empty or whitespace only")
    if len(cleaned) > 240:
        raise ValueError(f"entry is {len(cleaned)} chars, over the 240 limit")
    terminators = sum(cleaned.count(mark) for mark in (".", "!", "?"))
    # "make.fun" carries one dot of its own, so a single sentence
    # ending in a period shows exactly two terminator marks here.
    if terminators != 2:
        raise ValueError("entry must be exactly one sentence")
    return cleaned


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(validate_entry(ENTRY), encoding="utf-8")


if __name__ == "__main__":
    main()
