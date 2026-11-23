#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes the exact 93-character entry to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, no network.
"""

import os

ENTRY = "Today a stray cat picked my lap over three empty chairs and stayed until my coffee went cold."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verify: exactly one line, exactly 93 characters, UTF-8.
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    assert content == ENTRY, "entry.txt does not match ENTRY"
    assert "\n" not in content, "entry.txt must be a single line"
    assert len(content) == 93, f"entry must be 93 chars, got {len(content)}"


if __name__ == "__main__":
    main()
