"""S-geo-2d — terminator-nadir fold and solar-image width."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import load_constants, solar_image

H_M = 625_000.0


def _arrow(ax, x0, y0, x1, y1, color, lw=1.3) -> None:
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=11,
            lw=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def _right_angle(ax, x, y, s=0.20) -> None:
    ax.plot([x, x + s, x + s], [y + s, y + s, y], color=INK, lw=1.6, solid_joinstyle="miter")


def _mirror(ax, mx, my) -> None:
    mlen, thick = 0.48, 0.11
    tx, ty = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    p1 = (mx - mlen * tx, my - mlen * ty)
    p2 = (mx + mlen * tx, my + mlen * ty)
    p3 = (p2[0] - thick * nx, p2[1] - thick * ny)
    p4 = (p1[0] - thick * nx, p1[1] - thick * ny)
    ax.add_patch(Polygon([p3, p4, p1, p2], closed=True, facecolor="#d4d4d4", edgecolor="none", zorder=3))
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=INK, lw=3.0, solid_capstyle="butt", zorder=4)


def panel_fold(ax) -> None:
    ax.set_aspect("equal", adjustable="box", anchor="N")
    ax.axis("off")
    ax.set_xlim(-3.4, 2.35)
    ax.set_ylim(-0.98, 3.25)
    ax.set_title("1.  Center ray hits the local ground at $90^\\circ$", fontsize=11, pad=10)

    mx, my = 0.0, 2.05
    ax.add_patch(Arc((0.0, -6.4), 12.8, 12.8, angle=0, theta1=73, theta2=107, color="#c8c8c8", lw=1.4, zorder=0))
    ax.plot([-2.35, 1.75], [0, 0], color=INK, lw=1.3, zorder=2)
    ax.text(-2.25, 0.12, "ground", fontsize=8, color=MUTED)

    _mirror(ax, mx, my)
    ax.text(0.50, 2.38, "back", fontsize=8, color=MUTED)
    ax.text(-0.12, 1.55, "shiny", fontsize=8, color=INK, ha="right")

    for y in (1.75, 2.05, 2.35):
        _arrow(ax, -3.10, y, -0.55, y, ACCENT, lw=1.05)
    ax.text(-2.40, 2.58, "sunlight", fontsize=8, color=ACCENT, ha="center")

    _arrow(ax, -2.20, my, -0.14, my, INK, lw=1.6)
    ax.plot([0, 0], [my - 0.08, 0.02], color=INK, lw=2.0, zorder=3)
    _arrow(ax, 0.0, 0.50, 0.0, 0.08, INK, lw=1.7)

    _right_angle(ax, 0.0, 0.0, 0.20)
    ax.plot(0, 0, "o", color=PATCH, ms=7, zorder=5)
    ax.text(0.28, 0.28, r"$\varepsilon=90^\circ$", fontsize=10, color=INK)
    ax.text(0.0, -0.24, "patch center", ha="center", fontsize=8.5, color=PATCH)

    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    ax.plot([mx, mx + 0.58 * nx], [my, my + 0.58 * ny], color=MUTED, ls="--", lw=1.0)
    ax.add_patch(Arc((mx, my), 0.70, 0.70, angle=0, theta1=180, theta2=225, color=MUTED, lw=1.0))
    ax.add_patch(Arc((mx, my), 0.70, 0.70, angle=0, theta1=225, theta2=270, color=MUTED, lw=1.0))
    ax.text(-0.82, 1.98, r"$i$", fontsize=9, color=MUTED, ha="right")
    ax.text(-0.18, 1.42, r"$r$", fontsize=9, color=MUTED, ha="right")

    ax.annotate("", xy=(1.50, 0.02), xytext=(1.50, my), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(1.60, my / 2, r"$h$", fontsize=10, va="center")
    ax.text(
        0.0,
        -0.36,
        "\n".join(
            [
                r"$i = r = 45^\circ$  (from the normal)",
                r"turn $= 180^\circ-2i = 90^\circ$",
                r"$\varepsilon = 90^\circ$,  $d = h$",
            ]
        ),
        ha="center",
        va="top",
        fontsize=9.5,
        linespacing=1.22,
    )


def panel_width(ax, d_km: float, D_km: float, alpha: float, alpha_deg: float, D_tan_km: float) -> None:
    ax.set_aspect("equal", adjustable="box", anchor="N")
    ax.axis("off")
    ax.set_xlim(-2.875, 2.875)
    ax.set_ylim(-0.98, 3.25)
    ax.set_title("2.  Patch width: the Sun is a disk", fontsize=11, pad=10)

    mx, my = 0.0, 2.05
    half = 1.10

    ax.add_patch(Circle((-0.55, 2.92), 0.20, fill=False, ec=INK, lw=1.35))
    ax.plot([-0.55], [2.92 + 0.14], "o", color=INK, ms=3)
    ax.plot([-0.55], [2.92 - 0.14], "o", color=INK, ms=3)
    ax.plot([-0.55, -0.55], [2.92 - 0.14, 2.92 + 0.14], color=ACCENT, lw=1.1)
    ax.text(-0.55, 3.20, "Sun", ha="center", fontsize=8.5)
    ax.text(-0.22, 2.92, r"$\alpha$", fontsize=12, color=ACCENT)
    ax.annotate(
        "",
        xy=(-0.12, 2.22),
        xytext=(-0.42, 2.74),
        arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=0.9, mutation_scale=8),
    )

    ax.plot([-1.85, 1.85], [0, 0], color=INK, lw=1.3)
    ax.plot([-half, half], [0, 0], color=PATCH, lw=7, solid_capstyle="butt", zorder=3)
    ax.annotate("", xy=(half, -0.16), xytext=(-half, -0.16), arrowprops=dict(arrowstyle="<->", color=PATCH, lw=1.1))
    ax.text(0.0, -0.30, r"$D$", ha="center", fontsize=10, color=PATCH)

    ax.plot(mx, my, "o", color=INK, ms=5, zorder=4)
    ax.text(0.12, 2.18, "foil", fontsize=8, color=MUTED)
    _arrow(ax, mx, my, -half, 0.06, ACCENT, lw=1.15)
    _arrow(ax, mx, my, half, 0.06, ACCENT, lw=1.15)
    ax.plot([0, 0], [my, 0.04], color=MUTED, ls=":", lw=1.0)
    ax.add_patch(Arc((mx, my), 0.80, 0.80, angle=0, theta1=252, theta2=288, color=ACCENT, lw=1.2))
    ax.text(0.70, 1.48, r"$\alpha$", fontsize=11, color=ACCENT, ha="left", va="center", zorder=5)
    ax.annotate("", xy=(1.55, 0.02), xytext=(1.55, my), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(1.64, my / 2, rf"$h={d_km:.0f}\,\mathrm{{km}}$", fontsize=9, va="center")
    ax.text(
        0.0,
        -0.40,
        "\n".join(
            [
                rf"$\alpha = {alpha:.4f}\,\mathrm{{rad}} = {alpha_deg:.2f}^\circ$",
                rf"$D = h\alpha = {D_km:.3f}\,\mathrm{{km}}$",
                rf"$D = 2h\tan(\alpha/2) = {D_tan_km:.3f}\,\mathrm{{km}}$",
            ]
        ),
        ha="center",
        va="top",
        fontsize=9.5,
        linespacing=1.22,
    )


def main() -> None:
    apply_style()
    c = load_constants()
    img = solar_image(H_M)
    D_km = img.D_m / 1000.0
    d_km = img.d_m / 1000.0
    alpha = c["alpha_rad"]
    alpha_deg = math.degrees(alpha)
    D_tan_km = 2.0 * d_km * math.tan(alpha / 2.0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 5.05))
    fig.subplots_adjust(left=0.04, right=0.98, top=0.84, bottom=0.08, wspace=0.14)

    fig.suptitle("The $45^\\circ$ is at the foil. The ground hit is $90^\\circ$.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.905,
        r"Local ground is the tangent. The center ray is the Earth radius, so it meets that tangent at $\varepsilon=90^\circ$.",
        ha="center",
        fontsize=8.5,
        color=MUTED,
    )

    panel_fold(ax1)
    panel_width(ax2, d_km, D_km, alpha, alpha_deg, D_tan_km)
    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in (ax1, ax2))
    stamp(fig, r"$D=h\alpha$", y=y0 - 0.006, va="top")
    paths = save(fig, "s-geo-2d", lock=True)
    plt.close(fig)
    print(f"S-geo-2d  D(625 km) = {D_km:.3f} km")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
