"""S-a-shadow — collecting area vs sun-shadow size (F12). Kernel D = hα overlaid."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._geom import A_lit_m2, D_lit_m, foil_diameter_m
from figures._style import ACCENT, INK, MUTED, apply_style, save, stamp
from src.physics import solar_image

H_GRID_KM = (400.0, 625.0, 1000.0, 2000.0)
H_COLORS = {400.0: ACCENT, 625.0: INK, 1000.0: MUTED, 2000.0: "#6b6b6b"}
MARKERS_M = (18.0, 55.0, 1000.0)
MARKER_NAMES = ("M18", "M55", "M1km")
A_MIN, A_MAX = 1.0e2, 3.0e8


def main() -> None:
    apply_style()
    A = np.logspace(math.log10(A_MIN), math.log10(A_MAX), 160)

    fig, (ax_d, ax_a) = plt.subplots(1, 2, figsize=(10.8, 5.25))
    fig.subplots_adjust(left=0.08, right=0.98, top=0.80, bottom=0.14, wspace=0.18)
    fig.suptitle(r"Sun-shadow grows with the foil once the sheet is no longer small.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.885,
        r"Circular foil.  Solid = $D=h\alpha+w$ and $A_{\mathrm{lit}}=(\sqrt{A}+\sqrt{A_{\mathrm{image}}})^2$ (F12).  "
        r"Dashed = kernel (height only).  Markers are square sides, plotted at $A=w^2$.",
        ha="center",
        fontsize=8.2,
        color=MUTED,
    )

    for h_km in H_GRID_KM:
        h_m = h_km * 1000.0
        img = solar_image(h_m)
        D = np.array([D_lit_m(a, img.D_m) for a in A])
        Alit = np.array([A_lit_m2(a, img.A_image_m2) for a in A])
        color = H_COLORS[h_km]
        label = rf"$h={h_km:.0f}\,\mathrm{{km}}$"
        ax_d.plot(A, D / 1000.0, color=color, lw=2.0, label=label)
        ax_d.axhline(img.D_m / 1000.0, color=color, lw=1.0, ls=(0, (4.0, 2.5)), alpha=0.85)
        ax_a.plot(A, Alit / 1.0e6, color=color, lw=2.0, label=label)
        ax_a.axhline(img.A_image_m2 / 1.0e6, color=color, lw=1.0, ls=(0, (4.0, 2.5)), alpha=0.85)
        ax_a.axvline(img.A_image_m2, color=color, lw=0.6, ls=":", alpha=0.45)
        for side in MARKERS_M:
            Am = side * side
            ax_d.plot(Am, D_lit_m(Am, img.D_m) / 1000.0, "o", color=color, ms=4.5, zorder=3)
            ax_a.plot(Am, A_lit_m2(Am, img.A_image_m2) / 1.0e6, "o", color=color, ms=4.5, zorder=3)

    for ax in (ax_d, ax_a):
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(A_MIN, A_MAX)
        ax.set_xlabel(r"collecting area $A$ (m$^2$)")
        ax.grid(True, which="both", color="#e6e6e6", lw=0.6)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        for side in MARKERS_M:
            ax.axvline(side * side, color="#eeeeee", lw=0.8, zorder=0)

    ax_d.set_ylim(2.0, 80.0)
    ax_d.set_ylabel(r"sun-shadow width $D$ (km)")
    ax_d.set_title(r"$D$ vs $A$", fontsize=11)
    ax_d.legend(frameon=False, loc="upper left", fontsize=8)
    ax_d.text(1.4e2, 3.3, r"dashed $=h\alpha$", fontsize=7.5, color=MUTED)

    ax_a.set_ylim(5.0, 2.0e3)
    ax_a.set_ylabel(r"lit area $A_{\mathrm{lit}}$ (km$^2$)")
    ax_a.set_title(r"$A_{\mathrm{lit}}$ vs $A$", fontsize=11)
    ax_a.text(1.4e2, 8.5, r"dashed $=A_{\mathrm{image}}$", fontsize=7.5, color=MUTED)

    for ax in (ax_d, ax_a):
        y0 = ax.get_ylim()[0]
        for side, name in zip(MARKERS_M, MARKER_NAMES):
            ax.text(side * side, y0 * 1.08, name, ha="center", va="bottom", fontsize=7.5, color=MUTED)

    # Identity check at 625 km, circular A = A_image
    img = solar_image(625_000.0)
    Aeq = img.A_image_m2
    if abs(D_lit_m(Aeq, img.D_m) / img.D_m - 2.0) > 1e-9:
        raise SystemExit("at A = A_image, D_lit must be 2 hα")
    if abs(A_lit_m2(Aeq, Aeq) / Aeq - 4.0) > 1e-9:
        raise SystemExit("at A = A_image, A_lit must be 4 A_image")
    if abs(foil_diameter_m(Aeq) - img.D_m) > 1e-6:
        raise SystemExit("circular foil of area A_image must have diameter hα")

    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in (ax_d, ax_a))
    stamp(fig, r"$D=h\alpha+w$   $A_{\mathrm{lit}}=(\sqrt{A}+\sqrt{A_{\mathrm{image}}})^2$  (F12; circular)", y=y0 - 0.04, va="top")
    paths = save(fig, "s-a-shadow")
    plt.close(fig)

    print("S-a-shadow  circular")
    print(f"  625 km  A=A_image => D_lit={D_lit_m(Aeq, img.D_m)/1000:.3f} km  A_lit={A_lit_m2(Aeq, Aeq)/1e6:.2f} km2")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
