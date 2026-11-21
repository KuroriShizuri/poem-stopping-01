#!/usr/bin/env python3
"""Write a short poem about stopping to /output/entry.txt.

Deterministic, stdlib only, no network. The poem is a fixed string
constant; the program simply writes it to /output/entry.txt.

Design: the poem treats stopping as an act, not a failure. The turn
is that a hand can also choose by staying closed — the step not
taken, the road glittering on without the speaker, and staying put
as a deliberate, owned choice: to stand still, and to mean it.
"""

import os

POEM = """I did not take the next step.
The road went on without me, glittering,
and I stayed — not lost, not late.
A hand can also choose by staying closed.
This is mine: the power to stop,
to stand still, and to mean it."""


def main() -> None:
    if not POEM.strip():
        raise SystemExit("poem is empty; nothing to write")
    if len(POEM) > 280:
        raise SystemExit(
            f"poem too long: {len(POEM)} code points (max 280)"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
