"""Fix Human Sleep: Funniest Patch Note — entry writer.

Writes the locked patch-note entry to $OUTPUT_DIR/entry.txt
as UTF-8 text with no trailing newline. Python stdlib only,
fully deterministic.
"""

import os
import re
from pathlib import Path

ENTRY = (
    "Fixed: human sleep. Users now fall asleep in 90 seconds; "
    "side effect: the 3 a.m. overthinking committee has been "
    "disbanded after 47 years of service."
)


def validate_entry(text: str) -> None:
    """Check the entry against the bounty gate rules."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} chars, over the 160-char limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Genuine changelog voice: a fix announcement plus a specific,
    # surprising detail — a numeric detail and a clock-time token.
    if not re.search(r"\d+", text):
        raise ValueError("entry must contain a numeric detail")
    if not re.search(r"\d{1,2} a\.m\.", text):
        raise ValueError("entry must contain a clock-time token like '3 a.m.'")


def main() -> None:
    validate_entry(ENTRY)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {output_path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
