"""Auto-load demos/.env into the environment (no dependency, no cell code).

Imported by the demo helpers, so configuration lives in a file (copy
`.env.example` -> `.env`) instead of shell exports. Already-set environment
variables win, so a shell export still overrides the file.
"""

from __future__ import annotations

import os
from pathlib import Path


def load(path: str | os.PathLike | None = None) -> None:
    p = Path(path) if path else Path(__file__).resolve().parent / ".env"
    if not p.exists():
        return
    for raw in p.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, val)   # shell export wins over the file


load()
