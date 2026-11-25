"""Unsent: The Micro-Confession Sprint entry.

Writes a two-part micro-confession to entry.txt: a "To:" line naming
who the message was meant for, and the unsent message itself, one line
exactly as it was typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: my old mentor, who wrote my first reference letter\n"
    "I never told you I kept the draft where I thanked you properly \u2014 "
    "I was afraid it would sound like goodbye, so I let you retire "
    "thinking I forgot."
)

# The sealed scorer accepts 1 to 260 characters; refuse to write an
# entry the gate would reject instead of submitting invalid output.
MAX_CHARS = 260
# The message part after the "To:" line must itself be 1 to 200 chars.
MAX_MESSAGE_CHARS = 200


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate allows 1-{MAX_CHARS}"
        )
    message = ENTRY.split("\n", 1)[1]
    if not 1 <= len(message) <= MAX_MESSAGE_CHARS:
        raise ValueError(
            "message part is "
            f"{len(message)} characters, gate allows 1-{MAX_MESSAGE_CHARS}"
        )
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Round-trip verification: read back and confirm the bytes on disk
    # are exactly what was written.
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("round-trip verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
