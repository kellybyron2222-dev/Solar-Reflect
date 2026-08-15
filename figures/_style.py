"""Shared figure style. No physics here — only stamp, fonts, save."""

from __future__ import annotations

import hashlib
from datetime import date
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
WORKING = Path(__file__).resolve().parent / "working"
FINAL = Path(__file__).resolve().parent / "final"
CONSTANTS_PATH = ROOT / "constants.yaml"

INK = "#1c1c1c"
MUTED = "#5a5a5a"
ACCENT = "#1f4e79"
PATCH = "#b45309"


def constants_hash() -> str:
    raw = CONSTANTS_PATH.read_bytes()
    return hashlib.sha256(raw).hexdigest()[:8]


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "mathtext.fontset": "dejavusans",
            "axes.edgecolor": INK,
            "axes.labelcolor": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "text.color": INK,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.bbox": "tight",
            "savefig.dpi": 160,
        }
    )


def stamp_text(equation: str) -> str:
    return (
        f"terminator-nadir  ·  γ = 45° collector  ·  ε = 90°  ·  {equation}  ·  "
        f"constants {constants_hash()}  ·  {date.today().isoformat()}"
    )


def stamp(fig: plt.Figure, equation: str, y: float = 0.01, va: str = "bottom") -> None:
    fig.text(
        0.5,
        y,
        stamp_text(equation),
        ha="center",
        va=va,
        fontsize=7.5,
        color=MUTED,
    )


def save(fig: plt.Figure, scene_id: str, *, lock: bool = False) -> list[Path]:
    WORKING.mkdir(parents=True, exist_ok=True)
    paths = []
    for ext in ("svg", "png"):
        path = WORKING / f"{scene_id}.{ext}"
        fig.savefig(path)
        paths.append(path)
    if lock:
        FINAL.mkdir(parents=True, exist_ok=True)
        for ext in ("svg", "png"):
            src = WORKING / f"{scene_id}.{ext}"
            dest = FINAL / f"{scene_id}.{ext}"
            dest.write_bytes(src.read_bytes())
            paths.append(dest)
    return paths
