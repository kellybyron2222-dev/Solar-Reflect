"""S-I-A — I_peak vs collecting area. Numbers from physics.py. No I* lines."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._geom import I_mean_W_m2
from figures._style import ACCENT, INK, MUTED, apply_style, save, stamp
from src.physics import irradiance, load_constants, solar_image

H_GRID_KM = (400.0, 625.0, 1000.0, 2000.0)
H_COLORS = {400.0: ACCENT, 625.0: INK, 1000.0: MUTED, 2000.0: "#6b6b6b"}
MARKERS_M = (18.0, 55.0, 1000.0)
MARKER_NAMES = ("M18", "M55", "M1km")
ETA_IDEAL = 1.0
ETA_REAL = 0.675
HAND_I_55_IDEAL = 0.1097
A_MIN, A_MAX = 1.0e2, 3.0e6


def _panel(ax, eta: float, title: str) -> None:
    A = np.logspace(math.log10(A_MIN), math.log10(A_MAX), 80)
    for h_km in H_GRID_KM:
        h_m = h_km * 1000.0
        I = np.array([irradiance(a, h_m, eta) for a in A])
        I_mean = np.array([I_mean_W_m2(a, h_m, eta) for a in A])
        ax.plot(A, I, color=H_COLORS[h_km], lw=2.0, label=rf"$h={h_km:.0f}\,\mathrm{{km}}$")
        ax.plot(A, I_mean, color=H_COLORS[h_km], lw=1.2, ls=(0, (4.0, 2.4)))
        for side in MARKERS_M:
            Am = side * side
            ax.plot(Am, irradiance(Am, h_m, eta), "o", color=H_COLORS[h_km], ms=4.5, zorder=3)

    for side, name in zip(MARKERS_M, MARKER_NAMES):
        Am = side * side
        ax.axvline(Am, color="#e6e6e6", lw=0.8, zorder=0)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(A_MIN, A_MAX)
    ax.set_ylim(5.0e-4, 2.0e2)
    ax.set_xlabel(r"collecting area $A$ (m$^2$)")
    ax.set_ylabel(r"irradiance $I$ (W/m$^2$)")
    ax.set_title(title, fontsize=11)
    ax.legend(frameon=False, loc="upper left", fontsize=8)
    ax.grid(True, which="both", color="#e6e6e6", lw=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main() -> None:
    apply_style()
    c = load_constants()
    assert tuple(c["h_grid_km"]) == H_GRID_KM
    I_check = irradiance(55.0 ** 2, 625_000.0, ETA_IDEAL)
    rel = abs(I_check - HAND_I_55_IDEAL) / HAND_I_55_IDEAL

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 5.2), sharey=True)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.82, bottom=0.14, wspace=0.12)

    fig.suptitle(r"Peak $I$ tracks $A$ on this range. Mean $I$ bends once the patch grows.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.90,
        r"Solid = kernel peak $I=P/A_{\mathrm{image}}$ (F7).  Dashed = mean $I=P/A_{\mathrm{lit}}$ (F12, circular).  "
        r"Same centre for flat and $f=h$.  Realistic is $\eta=0.675$, not a new model.",
        ha="center",
        fontsize=8.3,
        color=MUTED,
    )

    _panel(ax1, ETA_IDEAL, r"Ideal  $\eta=1$")
    _panel(ax2, ETA_REAL, r"Realistic  $\eta=0.675$")
    ax2.set_ylabel("")

    # Marker names: redraw after ylim is set
    for ax in (ax1, ax2):
        for side, name in zip(MARKERS_M, MARKER_NAMES):
            Am = side * side
            ax.text(Am, 6.5e-4, name, ha="center", va="bottom", fontsize=7.5, color=MUTED)

    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in (ax1, ax2))
    stamp(fig, r"$I_{\mathrm{peak}}=E_0\eta A\cos\gamma / A_{\mathrm{image}}$   $I_{\mathrm{mean}}=P/A_{\mathrm{lit}}$  (F12)", y=y0 - 0.04, va="top")
    paths = save(fig, "s-i-a")
    plt.close(fig)

    img400 = solar_image(400_000.0)
    fill = (1000.0 ** 2) / img400.A_image_m2
    print(f"S-I-A  I(M55, 625 km, ideal) = {I_check:.4f} W/m^2  hand {HAND_I_55_IDEAL}  rel {rel:.4%}")
    print(f"  M1km / A_image at 400 km = {fill:.4f}")
    if rel > 0.01:
        raise SystemExit("S-I-A M55 625 km I does not match the hand sheet to 1%")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
