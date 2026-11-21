"""The Closed Hand — a poem about stopping.

Stopping here is an act, not a failure: the speaker stays on purpose,
and a hand can choose by staying closed. The program writes the poem
verbatim to /output/entry.txt, then reads it back to prove the file
on disk is exactly the poem — no truncation, no added newline.
"""

import os

POEM = (
    "I did not take the next step.\n"
    "The road went on without me, glittering,\n"
    "and I stayed \u2014 not lost, not late.\n"
    "A hand can also choose by staying closed.\n"
    "This is mine: the power to stop,\n"
    "to stand still, and to mean it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def write_entry(path, text):
    """Write text to path (creating parent dirs) and verify by round-trip."""
    if not text:
        raise ValueError("poem is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("poem exceeds 280 characters")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("round-trip check failed: file differs from poem")


def main():
    write_entry(OUTPUT_PATH, POEM)


if __name__ == "__main__":
    main()
