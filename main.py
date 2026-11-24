#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message, the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM, to /output/entry.txt.
"""

import os

MESSAGE = "fix: prod is down. I tested this in my head and it worked"


def validate(message: str) -> None:
    """Mirror the competition gate: UTF-8, 1-200 chars, not only whitespace."""
    message.encode("utf-8")
    if not 1 <= len(message) <= 200:
        raise ValueError(f"message must be 1-200 chars, got {len(message)}")
    if not message.strip():
        raise ValueError("message must not be only whitespace")


def main() -> None:
    validate(MESSAGE)
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
