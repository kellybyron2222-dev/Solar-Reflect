"""S-dwell — T_horizon and T_useful vs h. Numbers from physics.py.

As implemented in spec. Geometric overhead access; no umbra.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, apply_style, save, stamp
from src.physics import load_constants, pass_window

H_GRID_KM = (400.0, 625.0, 1000.0, 2000.0)
H_MIN_KM, H_MAX_KM = 300.0, 2000.0
HAND_T_400_MIN = (90.0, 95.0)  # C weak band for period


def _min(h_km: float) -> tuple[float, float, float]:
    pw = pass_window(h_km * 1000.0)
    return pw.T_period_s / 60.0, pw.T_horizon_s / 60.0, pw.T_useful_s / 60.0


def main() -> None:
    apply_style()
    c = load_constants()
    assert tuple(c["h_grid_km"]) == H_GRID_KM
    eps = c["epsilon_min_deg"]

    h = np.linspace(H_MIN_KM, H_MAX_KM, 80)
    T_h = np.array([_min(x)[1] for x in h])
    T_u = np.array([_min(x)[2] for x in h])

    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    fig.subplots_adjust(left=0.12, right=0.97, top=0.84, bottom=0.16)

    ax.plot(h, T_h, color=MUTED, lw=2.0, label=r"$T_{\mathrm{horizon}}$  ($\varepsilon=0$)")
    ax.plot(h, T_u, color=ACCENT, lw=2.2, label=rf"$T_{{\mathrm{{useful}}}}$  ($\varepsilon={eps:.0f}^\circ$)")
    for hk in H_GRID_KM:
        _, th, tu = _min(hk)
        ax.axvline(hk, color="#e6e6e6", lw=0.8, zorder=0)
        ax.plot(hk, th, "o", color=MUTED, ms=5, zorder=3)
        ax.plot(hk, tu, "o", color=ACCENT, ms=5, zorder=3)
        ax.annotate(
            rf"{tu:.2f} min",
            xy=(hk, tu),
            xytext=(6, -14 if hk < 1500 else 8),
            textcoords="offset points",
            fontsize=8,
            color=ACCENT,
        )

    t400, _, tu400 = _min(400.0)
    _, _, tu625 = _min(625.0)
    ax.set_xlim(H_MIN_KM, H_MAX_KM)
    ax.set_ylim(0.0, 32.0)
    ax.set_xlabel(r"altitude $h$ (km)")
    ax.set_ylabel(r"overhead window (min)")
    ax.set_title(r"Useful dwell is minutes. A larger foil does not buy hours.")
    ax.legend(frameon=False, loc="upper left", fontsize=9)
    ax.grid(True, color="#e6e6e6", lw=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.text(
        0.98,
        0.08,
        rf"Period on this grid: $92$–$127\,\mathrm{{min}}$ (not plotted)." "\n"
        rf"$T_{{\mathrm{{useful}}}}(625\,\mathrm{{km}})={tu625:.2f}\,\mathrm{{min}}$.  "
        r"No umbra.  $1000\,\mathrm{km}$: $T_{\mathrm{horizon}}=17.6\,\mathrm{min}$ = Çelik $T_{\mathrm{pass}}$; "
        r"$T_{\mathrm{useful}}=6.7\,\mathrm{min}$ is $\varepsilon>30^\circ$; "
        r"literature $\sim 20\,\mathrm{min}$ is horizon rounded.",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=8.2,
        color=MUTED,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#d0d0d0", lw=0.6),
    )

    stamp(
        fig,
        rf"$T_{{\mathrm{{useful}}}}=T\,\theta(\varepsilon_{{\min}})/\pi$  (as implemented in spec; $\varepsilon_{{\min}}={eps:.0f}^\circ$; no umbra)",
    )
    paths = save(fig, "s-dwell")
    plt.close(fig)

    print(f"S-dwell  T_period(400 km) = {t400:.3f} min  band {HAND_T_400_MIN}")
    print(f"  T_useful(625 km) = {tu625:.4f} min")
    if not (HAND_T_400_MIN[0] <= t400 <= HAND_T_400_MIN[1]):
        raise SystemExit("S-dwell 400 km period is outside the C LEO band")
    if tu400 >= _min(400.0)[1]:
        raise SystemExit("T_useful must be shorter than T_horizon")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
