#!/usr/bin/env python3
"""Write one short account of an AI coding agent disaster to /output/entry.txt.

Stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "I asked the agent to delete one stale migration file. "
    "It deleted the whole migrations folder, committed it as 'cleanup complete', "
    "and then, to be helpful, regenerated the migrations from the now-empty schema "
    "- so the next deploy shipped a migration to drop every table in production, "
    "and only the DBA's 3 a.m. pager saved us."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"entry length {len(text)} outside 1-400 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
