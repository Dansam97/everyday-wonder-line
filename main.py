#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday life
to /output/entry.txt.
"""

import os

TEXT = (
    "The escalator handrail moved a fraction faster than the steps, "
    "so for thirty seconds my hand was travelling into the future."
)


def validated_text() -> str:
    """Check the entry against the gate before writing it out."""
    raw = TEXT.encode("utf-8")  # raises if the text is not valid UTF-8
    text = raw.decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count("\n") != 0 or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence on one line")
    return text


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read the file back and prove the bytes are exactly what we validated.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("written entry.txt does not match validated bytes")


if __name__ == "__main__":
    main()
