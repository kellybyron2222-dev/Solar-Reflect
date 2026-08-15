"""S-focus — focusing does not shrink D_min = dα. Numbers from physics.py."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import solar_image

H_M = 625_000.0


def _panel(ax, title: str, curved: bool) -> None:
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-0.85, 3.15)
    ax.set_title(title, fontsize=11, pad=6)

    ax.plot([-1.9, 1.9], [0, 0], color=INK, lw=1.2)
    half = 1.15
    ax.plot([-half, half], [0, 0], color=PATCH, lw=6, solid_capstyle="butt")
    ax.annotate(
        "",
        xy=(half, -0.22),
        xytext=(-half, -0.22),
        arrowprops=dict(arrowstyle="<->", color=PATCH, lw=1.1),
    )
    ax.text(0, -0.48, r"$D_{\min}=d\alpha$", ha="center", color=PATCH, fontsize=10)

    mx, my = 0.0, 2.15
    if curved:
        ax.add_patch(Arc((0, 2.55), 1.15, 0.85, angle=0, theta1=200, theta2=340, color=INK, lw=2.4))
        ax.text(0.0, 2.72, r"concave, $f=d$", ha="center", fontsize=8.5, color=MUTED)
    else:
        ax.plot([-0.45, 0.45], [my, my], color=INK, lw=2.8, solid_capstyle="butt")
        ax.text(0.0, 2.42, "flat", ha="center", fontsize=8.5, color=MUTED)

    # Two solar-limb points, three rays each (left limb, right limb, center)
    for x0, y0 in ((-1.55, 3.00), (1.55, 3.00)):
        ax.plot(x0, y0, "o", color=INK, ms=3.5)
        ax.plot([x0, mx], [y0, my], color=ACCENT, lw=1.05)
    ax.plot([-1.55, 1.55], [3.00, 3.00], color=INK, lw=1.0)
    ax.text(0, 3.05, r"solar disk ($\alpha$)", ha="center", fontsize=8, color=MUTED)

    ax.plot([mx, -half], [my, 0], color=ACCENT, lw=1.05)
    ax.plot([mx, half], [my, 0], color=ACCENT, lw=1.05)
    ax.plot([mx, 0], [my, 0], color=MUTED, ls=":", lw=0.9)

    ax.annotate(
        "",
        xy=(1.75, 0.02),
        xytext=(1.75, my),
        arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0),
    )
    ax.text(1.88, my / 2, r"$d$", fontsize=9, va="center")


def main() -> None:
    apply_style()
    img = solar_image(H_M)
    D_km = img.D_m / 1000.0

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 5.0))
    fig.subplots_adjust(left=0.04, right=0.98, top=0.78, bottom=0.16, wspace=0.08)
    fig.suptitle("Focusing does not shrink the solar image", fontsize=13, y=0.96)
    fig.text(
        0.5,
        0.88,
        rf"Same $D_{{\min}}={D_km:.3f}\,\mathrm{{km}}$ at $h=625\,\mathrm{{km}}$. "
        r"A shorter focus ($f<d$) makes an image early, then the cone opens again.",
        ha="center",
        va="top",
        fontsize=9,
        color=MUTED,
    )

    _panel(axes[0], "Flat mirror", curved=False)
    _panel(axes[1], "Focusing mirror", curved=True)

    stamp(fig, r"$D_{\min}=d\alpha$  (flat and focusing)")
    paths = save(fig, "s-focus")
    plt.close(fig)
    print(f"S-focus  D_min(625 km) = {D_km:.3f} km")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
