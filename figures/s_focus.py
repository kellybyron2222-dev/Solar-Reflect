"""S-focus — D_min at f=h; extra curve opens D. Sun hits the shiny face."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import load_constants, solar_image

H_M = 625_000.0
A_M = 55.0  # M55 marker side; illustration, not an architecture
F_OVER_M = 10_000.0  # too-tight example; not the hemispherical D_max
HALF_DMIN = 0.82


def ground_patch_D_m(h_m: float, alpha: float, A_m: float, f_m: float | None) -> float:
    """1D geometric lit width. f_m=None is the flat limit f→∞."""
    D_min = h_m * alpha
    if f_m is None:
        return D_min + A_m
    if f_m <= 0:
        raise ValueError("f_m must be positive")
    return D_min + A_m * abs(1.0 - h_m / f_m)


def D_hemisphere_m(h_m: float, alpha: float, A_m: float) -> float:
    """Geometric cap: hemisphere R=A/2, f=A/4, ψ=90°."""
    return ground_patch_D_m(h_m, alpha, A_m, A_m / 4.0)


def cap_half_angle_rad(A_m: float, f_m: float) -> float:
    """Spherical-cap half-angle ψ from sinψ = A/(4f)."""
    s = A_m / (4.0 * f_m)
    if s >= 1.0:
        return math.pi / 2.0
    return math.asin(s)


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


def _flat_foil(ax, mx, my) -> None:
    mlen, thick = 0.40, 0.10
    tx, ty = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    p1 = (mx - mlen * tx, my - mlen * ty)
    p2 = (mx + mlen * tx, my + mlen * ty)
    p3 = (p2[0] - thick * nx, p2[1] - thick * ny)
    p4 = (p1[0] - thick * nx, p1[1] - thick * ny)
    ax.add_patch(Polygon([p3, p4, p1, p2], closed=True, facecolor="#d4d4d4", edgecolor="none", zorder=3))
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=INK, lw=2.6, solid_capstyle="butt", zorder=4)


def _curved_foil(ax, mx, my, bulge: float) -> None:
    mlen, thick = 0.40, 0.10
    tx, ty = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    shiny, back = [], []
    n = 16
    for i in range(-n, n + 1):
        t = mlen * i / n
        sag = bulge * (t / mlen) ** 2
        sx = mx + t * tx + sag * nx
        sy = my + t * ty + sag * ny
        shiny.append((sx, sy))
        back.append((sx - thick * nx, sy - thick * ny))
    ax.add_patch(Polygon(back[::-1] + shiny, closed=True, facecolor="#d4d4d4", edgecolor="none", zorder=3))
    xs, ys = zip(*shiny)
    ax.plot(xs, ys, color=INK, lw=2.6, solid_capstyle="butt", zorder=4)


def _panel(
    ax,
    title: str,
    kind: str,
    D_km: float,
    half: float,
    formula: list[str],
) -> None:
    ax.set_aspect("equal", adjustable="box", anchor="N")
    ax.axis("off")
    ax.set_xlim(-3.25, 2.40)
    ax.set_ylim(-1.05, 3.15)
    ax.set_title(title, fontsize=11, pad=8)

    mx, my = 0.0, 2.05
    sun = (-2.50, my)
    r_sun = 0.20
    dy = 0.26
    hx = max(1.52, half + 0.28)

    ax.plot([-2.10, 1.85], [0, 0], color=INK, lw=1.1)
    ax.plot([-half, half], [0, 0], color=PATCH, lw=7, solid_capstyle="butt", zorder=3)
    ax.annotate(
        "",
        xy=(half, -0.16),
        xytext=(-half, -0.16),
        arrowprops=dict(arrowstyle="<->", color=PATCH, lw=1.1),
    )
    if kind == "dmin":
        d_label = r"$D_{\min}$"
    elif kind == "over":
        d_label = r"$D_{\max}$"
    else:
        d_label = r"$D$"
    ax.text(0.0, -0.34, d_label, ha="center", color=PATCH, fontsize=10)

    if kind == "flat":
        _flat_foil(ax, mx, my)
        ax.add_patch(Ellipse((-half, 0), 0.26, 0.10, facecolor=PATCH, edgecolor="none", alpha=0.55, zorder=4))
        ax.add_patch(Ellipse((half, 0), 0.26, 0.10, facecolor=PATCH, edgecolor="none", alpha=0.55, zorder=4))
        ax.plot([mx, -half], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)
        ax.plot([mx, half], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)
    elif kind == "dmin":
        _curved_foil(ax, mx, my, bulge=0.11)
        ax.plot(-half, 0, "o", color=PATCH, ms=7, zorder=5)
        ax.plot(half, 0, "o", color=PATCH, ms=7, zorder=5)
        ax.plot([mx, -half], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)
        ax.plot([mx, half], [my, 0.04], color=ACCENT, lw=1.2, zorder=2)
    else:
        _curved_foil(ax, mx, my, bulge=0.22)
        # Crossing is enlarged: real f/h = 10/625 sits almost on the foil.
        xf, yf = 0.0, 1.12
        ax.plot(xf, yf, "o", color=INK, ms=4.5, zorder=5)
        ax.text(0.12, yf + 0.08, "focus", fontsize=7.5, color=MUTED, ha="left")
        ax.plot([mx, xf, -half], [my, yf, 0.04], color=ACCENT, lw=1.15, zorder=2)
        ax.plot([mx, xf, half], [my, yf, 0.04], color=ACCENT, lw=1.15, zorder=2)
        ax.add_patch(Ellipse((-half, 0), 0.34, 0.11, facecolor=PATCH, edgecolor="none", alpha=0.50, zorder=4))
        ax.add_patch(Ellipse((half, 0), 0.34, 0.11, facecolor=PATCH, edgecolor="none", alpha=0.50, zorder=4))

    ax.add_patch(Circle(sun, r_sun, fill=False, ec=INK, lw=1.3))
    ax.plot(sun[0], sun[1] + 0.14, "o", color=INK, ms=3.5)
    ax.plot(sun[0], sun[1] - 0.14, "o", color=INK, ms=3.5)
    ax.plot([sun[0], sun[0]], [sun[1] - 0.14, sun[1] + 0.14], color=ACCENT, lw=1.0)
    ax.text(sun[0], sun[1] + 0.40, "Sun", ha="center", fontsize=8)
    ax.text(sun[0] + 0.30, sun[1], r"$\alpha$", fontsize=10, color=ACCENT, va="center")

    _arrow(ax, -2.10, my + dy, -0.22, my + 0.06, ACCENT)
    _arrow(ax, -2.10, my - dy, -0.22, my - 0.06, ACCENT)
    ax.text(-1.50, my + dy + 0.16, "sunlight", fontsize=7.5, color=ACCENT, ha="center")

    nx, ny = -math.sqrt(0.5), -math.sqrt(0.5)
    ax.plot([mx, mx + 0.48 * nx], [my, my + 0.48 * ny], color=MUTED, ls="--", lw=0.9)
    ax.add_patch(Arc((mx, my), 0.58, 0.58, angle=0, theta1=180, theta2=225, color=MUTED, lw=1.0))
    ax.add_patch(Arc((mx, my), 0.58, 0.58, angle=0, theta1=225, theta2=270, color=MUTED, lw=1.0))
    ax.text(-0.70, 1.96, r"$i$", fontsize=8.5, color=MUTED, ha="right")
    ax.text(-0.14, 1.50, r"$r$", fontsize=8.5, color=MUTED, ha="right")
    ax.plot([0, 0.16, 0.16], [0.16, 0.16, 0], color=INK, lw=1.3, solid_joinstyle="miter")
    ax.text(0.24, 0.24, r"$\varepsilon=90^\circ$", fontsize=8.5, color=INK)

    ax.annotate("", xy=(hx, 0.02), xytext=(hx, my), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(hx + 0.10, my / 2, r"$h$", fontsize=10, va="center")

    ax.text(0.0, -0.50, "\n".join(formula), ha="center", va="top", fontsize=8.6, linespacing=1.20)


def main() -> None:
    apply_style()
    c = load_constants()
    alpha = c["alpha_rad"]
    img = solar_image(H_M)
    D_min_m = img.D_m
    D_min_km = D_min_m / 1000.0
    D_flat_m = ground_patch_D_m(H_M, alpha, A_M, None)
    D_over_m = ground_patch_D_m(H_M, alpha, A_M, F_OVER_M)
    D_over_km = D_over_m / 1000.0
    D_hem_km = D_hemisphere_m(H_M, alpha, A_M) / 1000.0
    psi_over_deg = math.degrees(cap_half_angle_rad(A_M, F_OVER_M))
    psi_opt_deg = math.degrees(cap_half_angle_rad(A_M, H_M))

    fig, axes = plt.subplots(1, 3, figsize=(14.6, 5.15))
    fig.subplots_adjust(left=0.02, right=0.99, top=0.82, bottom=0.08, wspace=0.10)

    fig.suptitle(r"Minimum $D$ is $h\alpha$. Extra curve opens the patch.", fontsize=13, y=0.97)
    fig.text(
        0.5,
        0.90,
        r"Terminator-nadir: sunlight is horizontal, $i=r=45^\circ$, ground hit $90^\circ$. "
        r"$D_{\min}$ at $f=h$. Tighter dish: focus above the ground, then the cone opens.",
        ha="center",
        fontsize=8.5,
        color=MUTED,
    )

    _panel(
        axes[0],
        "Flat foil",
        "flat",
        D_min_km,
        HALF_DMIN,
        [
            rf"$D = h\alpha = {D_min_km:.3f}\,\mathrm{{km}}$",
            r"no $f$  ($f\to\infty$)",
            r"$A\ll D$, so kernel omits $+A$",
        ],
    )
    _panel(
        axes[1],
        r"Dish, $D_{\min}$  ($f=h$)",
        "dmin",
        D_min_km,
        HALF_DMIN,
        [
            rf"$D_{{\min}}=h\alpha={D_min_km:.3f}\,\mathrm{{km}}$",
            r"$f=h \;\;\Rightarrow\;\; |1-h/f|=0$",
            r"$R=2f$ is not in $D$",
        ],
    )
    half_over = HALF_DMIN * (D_over_m / D_min_m)
    _panel(
        axes[2],
        r"Dish, $D_{\max}$  ($f<h$)",
        "over",
        D_over_km,
        half_over,
        [
            r"$D_{\max}=h\alpha+A|1-h/f|$",
            rf"$f={F_OVER_M/1000:.0f}\,\mathrm{{km}}<h$",
            rf"$D_{{\max}}={D_over_km:.3f}\,\mathrm{{km}}$  (M55)",
        ],
    )
    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in axes)
    stamp(fig, r"$D_{\min}=h\alpha$   $D_{\max}=h\alpha+A|1-h/f|$", y=y0 - 0.006, va="top")
    paths = save(fig, "s-focus")
    plt.close(fig)

    print(f"S-focus  D_min(625 km) = {D_min_km:.3f} km")
    print(f"  D_flat = h*alpha + A = {D_flat_m/1000:.3f} km  (kernel still D_min)")
    print(f"  D(f={F_OVER_M/1000:.0f} km) = {D_over_km:.3f} km  (panel 3; psi={psi_over_deg:.3f} deg)")
    print(f"  D_max(hemisphere) = {D_hem_km:.0f} km  (not drawn; psi=90 deg)")
    print(f"  psi_opt(f=h) = {psi_opt_deg:.5f} deg")
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
