#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the entrant's honest count of open browser tabs to
/output/entry.txt: one number, digits only, nothing else.
"""

import os

# The entrant's honest count of open browser tabs at entry time:
# 47 tabs across work and personal windows. Digits only, no units.
ENTRY = "47"


def entry_text() -> str:
    """Return the exact bytes written to entry.txt: the count + newline."""
    return ENTRY + "\n"


def main() -> None:
    """Write the tab-count entry to ``entry.txt`` in the output dir.

    The output directory comes from ``OUTPUT_DIR`` and defaults to
    ``/output``. The file holds the count plus one trailing newline.
    """
    # Validate the entry before writing: digits only, no surrounding
    # whitespace, and short enough to be a plausible tab count.
    assert ENTRY, "entry text must not be empty"
    assert ENTRY.strip() == ENTRY, "entry text must have no surrounding whitespace"
    assert ENTRY.isdigit(), "entry text must be digits only"
    assert 1 <= len(ENTRY) <= 6, "entry text length out of range"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
