"""S-A-req — collecting area required for parked I*. Numbers from physics.py.

Lines are A5 I* only. No T*. Linear invert; no 1-sun clip.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import load_constants, required_area

H_GRID_KM = (400.0, 625.0, 1000.0, 2000.0)
H_MIN_KM, H_MAX_KM = 300.0, 2000.0
ETA_IDEAL = 1.0
ETA_REAL = 0.675
I_STARS = (0.003, 0.1, 50.0, 200.0, 1000.0)
I_COLORS = (MUTED, ACCENT, INK, PATCH, "#6b6b6b")
I_LABELS = (
    r"$I^*=0.003$",
    r"$I^*=0.1$",
    r"$I^*=50$",
    r"$I^*=200$",
    r"$I^*=1000$",
)
HAND_A_55 = 3025.0
HAND_I_55 = 0.1097


def _panel(ax, eta: float, title: str) -> None:
    h = np.linspace(H_MIN_KM, H_MAX_KM, 80)
    for I_star, color, lab in zip(I_STARS, I_COLORS, I_LABELS):
        A = np.array([required_area(I_star, hk * 1000.0, eta) for hk in h])
        ax.plot(h, A, color=color, lw=2.0, label=lab)
        for hk in H_GRID_KM:
            ax.plot(hk, required_area(I_star, hk * 1000.0, eta), "o", color=color, ms=4.0, zorder=3)

    for hk in H_GRID_KM:
        ax.axvline(hk, color="#e6e6e6", lw=0.8, zorder=0)

    ax.set_yscale("log")
    ax.set_xlim(H_MIN_KM, H_MAX_KM)
    ax.set_ylim(1.0e1, 5.0e8)
    ax.set_xlabel(r"altitude $h$ (km)")
    ax.set_ylabel(r"required collecting area $A$ (m$^2$)")
    ax.set_title(title, fontsize=11)
    ax.legend(frameon=False, loc="upper left", fontsize=8)
    ax.grid(True, which="both", color="#e6e6e6", lw=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main() -> None:
    apply_style()
    c = load_constants()
    assert tuple(c["h_grid_km"]) == H_GRID_KM

    A_check = required_area(HAND_I_55, 625_000.0, ETA_IDEAL)
    rel = abs(A_check - HAND_A_55) / HAND_A_55

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 5.2), sharey=True)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.82, bottom=0.14, wspace=0.12)
    fig.suptitle(r"Required $A$ for parked $I^*$. Area does not buy hours.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.90,
        r"Terminator-nadir, $\gamma=45^\circ$. Linear invert of $I=E_0\eta A\cos\gamma/A_{\mathrm{image}}$. "
        r"$I^*$ set = A5. No $T^*$. No 1-sun clip.",
        ha="center",
        fontsize=8.5,
        color=MUTED,
    )

    _panel(ax1, ETA_IDEAL, r"Ideal  $\eta=1$")
    _panel(ax2, ETA_REAL, r"Realistic  $\eta=0.675$")
    ax2.set_ylabel("")

    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in (ax1, ax2))
    stamp(fig, r"$A_{\mathrm{req}}=I^* A_{\mathrm{image}}/(E_0\eta\cos\gamma)$", y=y0 - 0.04, va="top")
    paths = save(fig, "s-a-req")
    plt.close(fig)

    print(f"S-A-req  A_req(I=0.1097, 625 km, ideal) = {A_check:.1f} m2  M55={HAND_A_55}  rel {rel:.4%}")
    if rel > 0.01:
        raise SystemExit("S-A-req invert does not recover M55 to 1%")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
