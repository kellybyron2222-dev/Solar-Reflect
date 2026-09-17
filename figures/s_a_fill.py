"""S-a-fill — circular foil vs growing sun-shadow (F12). Kernel D = hα unchanged."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from figures._geom import A_lit_m2, D_lit_m, I_mean_W_m2, I_peak_W_m2, foil_diameter_m
from figures._style import ACCENT, INK, MUTED, PATCH, apply_style, save, stamp
from src.physics import irradiance, load_constants, solar_image

H_M = 625_000.0
ETA = 1.0
FILLS = (0.1, 1.0, 10.0)
TITLES = (
    r"$A = (1/10)\,A_{\mathrm{image}}$",
    r"$A = A_{\mathrm{image}}$",
    r"$A = 10\,A_{\mathrm{image}}$",
)


def _fmt_I(I: float) -> str:
    if I >= 100.0:
        return rf"{I:.0f}"
    if I >= 10.0:
        return rf"{I:.1f}"
    return rf"{I:.2f}"


def _panel(
    ax,
    title: str,
    D_sun_km: float,
    w_km: float,
    D_lit_km: float,
    A_km2: float,
    A_lit_km2: float,
    I_peak: float,
    I_mean: float,
    I_kern: float,
    P_W: float,
    lim_km: float,
) -> None:
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_xlim(-lim_km, lim_km)
    ax.set_ylim(-lim_km * 1.20, lim_km * 1.08)
    ax.set_title(title, fontsize=11, pad=8)

    R_lit = D_lit_km / 2.0
    R_sun = D_sun_km / 2.0
    R_foil = w_km / 2.0

    ax.add_patch(Circle((0.0, 0.0), R_lit, facecolor="#f4d0a8", edgecolor="none", zorder=1))
    ax.add_patch(Circle((0.0, 0.0), R_sun, facecolor="none", edgecolor=PATCH, lw=1.15, ls=(0, (4.0, 2.4)), zorder=3))
    ax.add_patch(
        Circle((0.0, 0.0), R_foil, facecolor="none", edgecolor=ACCENT, lw=2.2, hatch="////", zorder=4)
    )
    ax.add_patch(Circle((0.0, 0.0), R_lit, facecolor="none", edgecolor=PATCH, lw=2.0, zorder=5))

    d_y = -R_lit - 0.50
    ax.annotate(
        "",
        xy=(R_lit, d_y),
        xytext=(-R_lit, d_y),
        arrowprops=dict(arrowstyle="<->", color=PATCH, lw=1.05),
        zorder=6,
    )
    ax.text(
        0.0,
        d_y - 0.50,
        rf"$D_{{\mathrm{{lit}}}}=h\alpha+w={D_lit_km:.2f}\,\mathrm{{km}}$",
        ha="center",
        va="top",
        color=PATCH,
        fontsize=8.3,
    )

    formula = [
        rf"$w={w_km:.2f}\,\mathrm{{km}}$,  $A={A_km2:.2f}\,\mathrm{{km}}^2$",
        rf"$A_{{\mathrm{{lit}}}}={A_lit_km2:.1f}\,\mathrm{{km}}^2$,  $P={P_W/1e9:.2f}\,\mathrm{{GW}}$",
        rf"$I_{{\mathrm{{peak}}}}={_fmt_I(I_peak)}\,\mathrm{{W/m}}^2$  (centre)",
        rf"$I_{{\mathrm{{mean}}}}={_fmt_I(I_mean)}\,\mathrm{{W/m}}^2$  ($P/A_{{\mathrm{{lit}}}}$)",
        rf"kernel, fixed $D$: ${_fmt_I(I_kern)}$",
    ]
    ax.text(0.0, -lim_km * 0.90, "\n".join(formula), ha="center", va="top", fontsize=8.0, linespacing=1.22, color=INK)


def main() -> None:
    apply_style()
    c = load_constants()
    img = solar_image(H_M)
    D_sun_m = img.D_m
    D_sun_km = D_sun_m / 1000.0
    A_image_km2 = img.A_image_m2 / 1.0e6
    E_c = c["E0"] * math.cos(math.radians(c["gamma_deg"])) * ETA

    rows = []
    for fill in FILLS:
        A = fill * img.A_image_m2
        w_m = foil_diameter_m(A)
        D_m = D_lit_m(A, D_sun_m)
        Alit = A_lit_m2(A, img.A_image_m2)
        P = E_c * A
        Ipk = I_peak_W_m2(A, H_M, ETA)
        Imn = I_mean_W_m2(A, H_M, ETA)
        Ik = irradiance(A, H_M, ETA)
        if abs(D_m - (D_sun_m + w_m)) > 1e-9:
            raise SystemExit("D_lit is not hα + w")
        if abs(Alit - (math.sqrt(A) + math.sqrt(img.A_image_m2)) ** 2) > 1e-3:
            raise SystemExit("A_lit identity failed")
        if D_m <= w_m or Alit <= A:
            raise SystemExit("lit disk must contain the foil plus the blur")
        rows.append((A, w_m, D_m, Alit, Ipk, Imn, Ik, P))

    lim_km = 1.14 * (rows[-1][2] / 2.0) / 1000.0

    fig, axes = plt.subplots(1, 3, figsize=(14.6, 5.85))
    fig.subplots_adjust(left=0.02, right=0.99, top=0.76, bottom=0.11, wspace=0.08)
    fig.suptitle(
        r"Larger foil, larger sun-shadow — and more W/m$^2$ until the Sun is filled.",
        fontsize=13,
        y=0.97,
    )
    fig.text(
        0.5,
        0.865,
        rf"Circular foil at $h=625\,\mathrm{{km}}$.  Orange = lit ground $D=h\alpha+w$.  "
        rf"Dashed = solar blur $h\alpha={D_sun_km:.3f}\,\mathrm{{km}}$.  Blue = foil.  "
        rf"Peak $I$ is the centre; mean $I$ is $P$ over the whole lit disk.  "
        rf"Kernel stays $D=h\alpha$ ($A_{{\mathrm{{image}}}}={A_image_km2:.2f}\,\mathrm{{km}}^2$).",
        ha="center",
        fontsize=8.0,
        color=MUTED,
    )

    for ax, title, row in zip(axes, TITLES, rows):
        A, w_m, D_m, Alit, Ipk, Imn, Ik, P = row
        _panel(
            ax,
            title,
            D_sun_km,
            w_m / 1000.0,
            D_m / 1000.0,
            A / 1.0e6,
            Alit / 1.0e6,
            Ipk,
            Imn,
            Ik,
            P,
            lim_km,
        )

    bar_y = -lim_km * 0.68
    bar_x0 = -lim_km + 0.55
    axes[0].plot([bar_x0, bar_x0 + 5.0], [bar_y, bar_y], color=MUTED, lw=1.8, solid_capstyle="butt")
    axes[0].plot([bar_x0, bar_x0], [bar_y - 0.22, bar_y + 0.22], color=MUTED, lw=1.4)
    axes[0].plot([bar_x0 + 5.0, bar_x0 + 5.0], [bar_y - 0.22, bar_y + 0.22], color=MUTED, lw=1.4)
    axes[0].text(bar_x0 + 2.5, bar_y + 0.42, r"$5\,\mathrm{km}$", ha="center", fontsize=8, color=MUTED)

    handles = [
        Line2D([0], [0], color="#f4d0a8", lw=8, label=r"lit ground  $D=h\alpha+w$"),
        Line2D([0], [0], color=PATCH, lw=1.2, ls=(0, (4.0, 2.4)), label=r"solar blur  $h\alpha$"),
        Line2D([0], [0], color=ACCENT, lw=2.2, label="circular foil"),
    ]
    fig.legend(handles=handles, loc="upper right", bbox_to_anchor=(0.99, 0.80), frameon=False, fontsize=8)

    fig.canvas.draw()
    y0 = min(ax.get_position().y0 for ax in axes)
    stamp(fig, r"$D=h\alpha+w$,  $A_{\mathrm{lit}}=(\sqrt{A}+\sqrt{A_{\mathrm{image}}})^2$  (F12).  Kernel $D=h\alpha$.", y=y0 - 0.006, va="top")
    paths = save(fig, "s-a-fill")
    plt.close(fig)

    print("S-a-fill  circular  h=625 km  eta=1")
    for fill, row in zip(FILLS, rows):
        A, w_m, D_m, Alit, Ipk, Imn, Ik, P = row
        print(
            f"  fill={fill:g}  w={w_m/1000:.3f}  D={D_m/1000:.3f}  "
            f"A_lit={Alit/1e6:.2f}  Ipeak={Ipk:.2f}  Imean={Imn:.2f}  Ikern={Ik:.2f}"
        )
    for p in paths:
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
