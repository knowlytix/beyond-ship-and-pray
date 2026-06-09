"""Shared GMS wiring for the demos — loads the licensed knowlytix backend.

This is the *real* GMS "after". The open baseline (glassloop + proofloop) runs
with no license; when `knowlytix` is installed and a trained store is present,
these helpers load it so the demos can show the geometric gate / judge live.

Nothing here is imported at module load unless GMS is actually used, so the
open-baseline demos keep running with `knowlytix` absent.

Store resolution order:
  1. $GMS_BANKING_STORE  (explicit path)
  2. demos/data/gms_banking_store   (gitignored local copy — licensed data)

The store is a portable knowlytix artifact (model.pt + triples + calibration);
it is *not* redistributed with the open repo.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import glassloop.gms as gms

_DEMOS_DIR = Path(__file__).resolve().parent
_DEFAULT_STORE = _DEMOS_DIR / "data" / "gms_banking_store"


def available() -> bool:
    """True when the licensed knowlytix backend is importable."""
    return gms.available()


def store_path() -> Path:
    """Resolve the banking-store path (env override, else the local copy)."""
    env = os.environ.get("GMS_BANKING_STORE")
    return Path(env) if env else _DEFAULT_STORE


def store_present() -> bool:
    return (store_path() / "model.pt").exists()


def load_banking_store() -> tuple[Any, float]:
    """Load the trained GMS banking store and its calibrated gate threshold.

    Returns (store, theta). Raises if knowlytix is absent or the store is
    missing — callers should gate on `available()` / `store_present()` first.
    """
    if not available():
        raise RuntimeError("knowlytix backend not installed; " + gms.INSTALL_HINT)
    path = store_path()
    if not (path / "model.pt").exists():
        raise FileNotFoundError(
            f"no trained GMS store at {path} — set $GMS_BANKING_STORE or copy the "
            "licensed store into demos/data/gms_banking_store"
        )

    import contextlib
    import io

    # The knowlytix backend prints a license banner + store stats on import/load.
    # Suppress that chatter so the demo output stays clean; errors still raise.
    with contextlib.redirect_stdout(io.StringIO()):
        import torch
        from knowlytix.knowledge.query import DocGMSConfig, GMSExpertStore

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        store = GMSExpertStore(DocGMSConfig(store_path=str(path)), device=device)
        loaded = store.load()
    if not loaded:
        raise RuntimeError(f"failed to load GMS store at {path}")
    theta = float(
        json.loads((path / "calibration.json").read_text())["plausibility_gate"]["threshold"]
    )
    return store, theta
