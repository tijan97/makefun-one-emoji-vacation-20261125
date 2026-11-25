#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji, the beach with umbrella, to entry.txt
inside the output directory the grader provides.
"""

import os

EMOJI = "\U0001F3D6"  # U+1F3D6 BEACH WITH UMBRELLA


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Validate what we just wrote: exactly one non-whitespace character.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        raise SystemExit(f"invalid entry output: {written!r}")


if __name__ == "__main__":
    main()
