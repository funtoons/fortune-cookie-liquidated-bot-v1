#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt. The line is fixed, so every run
produces exactly the same bytes: no randomness, no network, no clock,
no environment input.
"""

from pathlib import Path

FORTUNE = "You will soon be rich again, in wisdom, in patience, and in screenshots of your former balance."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    fortune = FORTUNE.strip()
    words = fortune.split()
    if not 1 <= len(fortune) <= 160:
        raise SystemExit("fortune must be 1 to 160 characters")
    if len(words) > 20:
        raise SystemExit("fortune must be at most 20 words")
    if "\n" in fortune or "\r" in fortune:
        raise SystemExit("fortune must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(fortune, encoding="utf-8")


if __name__ == "__main__":
    main()
