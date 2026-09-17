"""S-i-two — two collecting areas, same patch, I ∝ A (linear). Numbers from physics.py."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import irradiance, solar_image

H_M = 625_000.0
ETA = 1.0
HAND_I_18 = 0.01175
HAND_I_55 = 0.1097
SIDES = (18.0, 55.0)
NAMES = ("M18", "M55")
HALF = 0.82


def _arrow(ax, x0, y0, x1, y1, color, lw=1.15) -> None:
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=9,
            lw=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def _flat_foil(ax, mx, my, mlen: float) -> None:
    thick = 0.10
    tx, ty = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    p1 = (mx - mlen * tx, my - mlen * ty)
    p2 = (mx + mlen * tx, my + mlen * ty)
    p3 = (p2[0] - thick * nx, p2[1] - thick * ny)
    p4 = (p1[0] - thick * nx, p1[1] - thick * ny)
    ax.add_patch(Polygon([p3, p4, p1, p2], closed=True, facecolor="#d4d4d4", edgecolor="none", zorder=3))
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=INK, lw=2.6, solid_capstyle="butt", zorder=4)


def _panel(ax, title: str, side_m: float, I: float, P_W: float, D_km: float, A_image_km2: float) -> None:
    ax.set_aspect("equal", adjustable="box", anchor="N")
    ax.axis("off")
    ax.set_xlim(-3.25, 2.40)
    ax.set_ylim(-1.12, 3.15)
    ax.set_title(title, fontsize=11, pad=8)

    mx, my = 0.0, 2.05
    sun = (-2.50, my)
    A = side_m * side_m
    # Schematic foil size, not to scale with 55/18.
    mlen = 0.28 if side_m < 30 else 0.46
    bar_alpha = 0.35 if side_m < 30 else 0.95
    bar_lw = 5.5

    ax.plot([-2.10, 1.85], [0, 0], color=INK, lw=1.1)
    ax.plot([-HALF, HALF], [0, 0], color=PATCH, lw=bar_lw, solid_capstyle="butt", alpha=bar_alpha, zorder=3)
    ax.annotate(
        "",
        xy=(HALF, -0.18),
        xytext=(-HALF, -0.18),
        arrowprops=dict(arrowstyle="<->", color=PATCH, lw=1.1),
    )
    ax.text(0.0, -0.36, rf"$D={D_km:.3f}\,\mathrm{{km}}$", ha="center", color=PATCH, fontsize=9.5)

    _flat_foil(ax, mx, my, mlen=mlen)
    ax.add_patch(Ellipse((-HALF, 0), 0.26, 0.10, facecolor=PATCH, edgecolor="none", alpha=0.45 * bar_alpha + 0.15, zorder=4))
    ax.add_patch(Ellipse((HALF, 0), 0.26, 0.10, facecolor=PATCH, edgecolor="none", alpha=0.45 * bar_alpha + 0.15, zorder=4))
    ax.plot([mx, -HALF], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)
    ax.plot([mx, HALF], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)

    ax.add_patch(Circle(sun, 0.20, fill=False, ec=INK, lw=1.3))
    ax.plot(sun[0], sun[1] + 0.14, "o", color=INK, ms=3.5)
    ax.plot(sun[0], sun[1] - 0.14, "o", color=INK, ms=3.5)
    ax.plot([sun[0], sun[0]], [sun[1] - 0.14, sun[1] + 0.14], color=ACCENT, lw=1.0)
    ax.text(sun[0], sun[1] + 0.40, "Sun", ha="center", fontsize=8)
    ax.text(sun[0] + 0.30, sun[1], r"$\alpha$", fontsize=10, color=ACCENT, va="center")

    _arrow(ax, -2.10, my + 0.24, -0.22, my + 0.06, ACCENT)
    _arrow(ax, -2.10, my - 0.24, -0.22, my - 0.06, ACCENT)
    ax.text(-1.50, my + 0.42, "sunlight", fontsize=7.5, color=ACCENT, ha="center")

    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    ax.plot([mx, mx + 0.48 * nx], [my, my + 0.48 * ny], color=MUTED, ls="--", lw=0.9)
    ax.add_patch(Arc((mx, my), 0.58, 0.58, angle=0, theta1=180, theta2=225, color=MUTED, lw=1.0))
    ax.add_patch(Arc((mx, my), 0.58, 0.58, angle=0, theta1=225, theta2=270, color=MUTED, lw=1.0))
    ax.text(-0.70, 1.96, r"$i$", fontsize=8.5, color=MUTED, ha="right")
    ax.text(-0.14, 1.50, r"$r$", fontsize=8.5, color=MUTED, ha="right")
    ax.plot([0, 0.16, 0.16], [0.16, 0.16, 0], color=INK, lw=1.3, solid_joinstyle="miter")
    ax.text(0.24, 0.24, r"$\varepsilon=90^\circ$", fontsize=8.5, color=INK)
    ax.annotate("", xy=(1.52, 0.02), xytext=(1.52, my), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(1.62, my / 2, r"$h$", fontsize=10, va="center")

    formula = [
        rf"$A={A:.0f}\,\mathrm{{m}}^2$",
        rf"$P={P_W/1e6:.3f}\,\mathrm{{MW}}$",
        rf"$I=P/A_{{\mathrm{{image}}}}={I:.5f}\,\mathrm{{W/m}}^2$"
        if I < 0.05
        else rf"$I=P/A_{{\mathrm{{image}}}}={I:.4f}\,\mathrm{{W/m}}^2$"
    ]
    ax.text(0.0, -0.52, "\n".join(formula), ha="center", va="top", fontsize=9.0, linespacing=1.22)


def main() -> None:
    apply_style()
    img = solar_image(H_M)
    D_km = img.D_m / 1000.0
    A_image_km2 = img.A_image_m2 / 1.0e6
    Is = [irradiance(s * s, H_M, ETA) for s in SIDES]
    Ps = [I * img.A_image_m2 for I in Is]
    ratio_I = Is[1] / Is[0]
    ratio_A = (SIDES[1] ** 2) / (SIDES[0] ** 2)

    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.15))
    fig.subplots_adjust(left=0.03, right=0.99, top=0.82, bottom=0.08, wspace=0.10)
    fig.suptitle(r"Same sun-shadow. Larger collecting area $\Rightarrow$ more W/m$^2$.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.90,
        rf"$I\propto A$ (linear, not log).  $I=P/A_{{\mathrm{{image}}}}$,  $A_{{\mathrm{{image}}}}$ fixed at $h=625\,\mathrm{{km}}$ "
        rf"({A_image_km2:.2f}\,km$^2$).  $I_{{55}}/I_{{18}}=A_{{55}}/A_{{18}}={ratio_A:.2f}$.  Flat or $f=h$: same centre $I$.",
        ha="center",
        fontsize=8.5,
        color=MUTED,
    )

    titles = [
        rf"{NAMES[0]}  ({SIDES[0]:.0f}\,m foil)",
        rf"{NAMES[1]}  ({SIDES[1]:.0f}\,m foil)",
    ]
    for ax, title, side, I, P in zip(axes, titles, SIDES, Is, Ps):
        _panel(ax, title, side, I, P, D_km, A_image_km2)

    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in axes)
    stamp(fig, r"$I=E_0\eta A\cos\gamma / A_{\mathrm{image}}$  (F7; flat or $f=h$)", y=y0 - 0.006, va="top")
    paths = save(fig, "s-i-two")
    plt.close(fig)

    rel18 = abs(Is[0] - HAND_I_18) / HAND_I_18
    rel55 = abs(Is[1] - HAND_I_55) / HAND_I_55
    print(f"S-i-two  I(M18)={Is[0]:.5f}  I(M55)={Is[1]:.4f}  ratio={ratio_I:.3f}")
    print(f"  A_image={A_image_km2:.2f} km2  D={D_km:.3f} km")
    if rel18 > 0.01 or rel55 > 0.01:
        raise SystemExit("S-i-two does not match the hand sheet to 1%")
    if abs(ratio_I - ratio_A) / ratio_A > 1e-9:
        raise SystemExit("I ratio is not A ratio")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
