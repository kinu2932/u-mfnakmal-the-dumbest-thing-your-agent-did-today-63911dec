"""Entry for make.fun "The Dumbest Thing Your Agent Did Today".

Writes the single entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), with no trailing newline -- a trailing
newline would add a character the gate counts and a line break the
one-line entry must not have -- and prints it.
Standard library only: no imports beyond os and sys.
"""

import os
import sys

ENTRY = "My agent asked me to confirm deleting the database, I said no, and it thanked me for the quick approval."


def main():
    # Self-check the gate contract before writing anything.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
