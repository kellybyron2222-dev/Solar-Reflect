"""S-spot-h — D = hα. Numbers from physics.py. GEO is a callout, not an axis point."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, apply_style, save, stamp
from src.physics import load_constants, solar_image

H_GRID_KM = (400.0, 625.0, 1000.0, 2000.0)
H_MIN_KM, H_MAX_KM = 300.0, 2000.0
GEO_H_KM = 35786.0
HAND_D_625_KM = 5.812


def D_km(h_km: float) -> float:
    return solar_image(h_km * 1000.0).D_m / 1000.0


def main() -> None:
    apply_style()
    c = load_constants()
    alpha = c["alpha_rad"]

    h = np.linspace(H_MIN_KM, H_MAX_KM, 80)
    D = np.array([D_km(x) for x in h])

    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    fig.subplots_adjust(left=0.12, right=0.97, top=0.86, bottom=0.16)

    ax.plot(h, D, color=ACCENT, lw=2.0, label=r"$D = h\alpha$")
    for hk in H_GRID_KM:
        dk = D_km(hk)
        ax.axvline(hk, color=MUTED, lw=0.6, ls=":", zorder=0)
        ax.plot(hk, dk, "o", color=INK, ms=5, zorder=3)
        ax.annotate(
            f"{hk:.0f} km\n{dk:.2f} km",
            xy=(hk, dk),
            xytext=(8, 8 if hk < 1500 else -28),
            textcoords="offset points",
            fontsize=8,
            color=INK,
        )

    d625 = D_km(625.0)
    ax.set_xlim(H_MIN_KM, H_MAX_KM)
    ax.set_ylim(0, D_km(H_MAX_KM) * 1.12)
    ax.set_xlabel("altitude $h$ (km)")
    ax.set_ylabel("solar-image diameter $D$ (km)")
    ax.set_title("How the ground patch grows with altitude")
    ax.legend(frameon=False, loc="upper left")
    ax.grid(True, color="#e6e6e6", lw=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    geo_D = D_km(GEO_H_KM)
    ax.text(
        0.98,
        0.06,
        f"GEO ({GEO_H_KM:.0f} km) is off this axis:\n"
        rf"$D = {geo_D:.0f}\,\mathrm{{km}}$  (hand band 320–340 km)",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=8.5,
        color=MUTED,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#d0d0d0", lw=0.6),
    )

    stamp(fig, r"$D=h\alpha$  (nadir; $\alpha$ full solar angular diameter)")
    paths = save(fig, "s-spot-h")
    plt.close(fig)

    rel = abs(d625 - HAND_D_625_KM) / HAND_D_625_KM
    print(f"S-spot-h  D(625 km) = {d625:.3f} km  hand {HAND_D_625_KM} km  rel {rel:.4%}")
    print(f"  alpha = {alpha}  GEO D = {geo_D:.1f} km")
    if rel > 0.01:
        raise SystemExit("S-spot-h 625 km D does not match the hand sheet to 1%")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
