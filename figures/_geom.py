"""Circular-foil geometry for illustrations (F12). Not the kernel."""

from __future__ import annotations

import math

from src.physics import irradiance, solar_image


def foil_diameter_m(A_m2: float) -> float:
    if A_m2 < 0:
        raise ValueError("A_m2 must be non-negative")
    return 2.0 * math.sqrt(A_m2 / math.pi)


def A_lit_m2(A_m2: float, A_image_m2: float) -> float:
    """Outer lit area: Minkowski sum of two disks. (√A + √A_image)²."""
    if A_m2 < 0 or A_image_m2 <= 0:
        raise ValueError("areas must be valid")
    return (math.sqrt(A_m2) + math.sqrt(A_image_m2)) ** 2


def D_lit_m(A_m2: float, D_sun_m: float) -> float:
    return D_sun_m + foil_diameter_m(A_m2)


def I_peak_W_m2(A_m2: float, h_m: float, eta: float) -> float:
    """Centre I: kernel until A = A_image, then E_c. Not a kernel clip."""
    img = solar_image(h_m)
    I_kern = irradiance(A_m2, h_m, eta)
    I_ceil = irradiance(img.A_image_m2, h_m, eta)
    return min(I_kern, I_ceil)


def I_mean_W_m2(A_m2: float, h_m: float, eta: float) -> float:
    """Area-average I over the outer lit disk. P / A_lit."""
    img = solar_image(h_m)
    P = irradiance(A_m2, h_m, eta) * img.A_image_m2
    return P / A_lit_m2(A_m2, img.A_image_m2)
