"""Orbital-sunlight physics kernel (Phase B).

Implements spec.md. No plots, no application classes, no binder classifier.
Internal units: metres, seconds, radians, watts.
"""

from __future__ import annotations

import math
from functools import lru_cache
from pathlib import Path
from types import MappingProxyType
from typing import NamedTuple

import yaml

_CONSTANTS_PATH = Path(__file__).resolve().parent.parent / "constants.yaml"


class SolarImage(NamedTuple):
    d_m: float
    D_m: float
    A_image_m2: float


class PassWindow(NamedTuple):
    T_period_s: float
    T_horizon_s: float
    T_useful_s: float


class NightSnapshot(NamedTuple):
    """Terminator-sunlit foil, night-side site at closest approach.

    theta_rad is the Earth-central offset from the terminator track toward night
    (equal to solar depression at the site if the nadir is on the terminator).
    Midnight nadir is not this state: that sat is usually in umbra.
    """

    theta_rad: float
    epsilon_rad: float
    d_m: float
    D_minor_m: float
    D_major_m: float
    A_image_m2: float
    i_rad: float
    cos_i: float
    sin_eps: float


@lru_cache(maxsize=1)
def load_constants(path: str | None = None) -> dict:
    p = Path(path) if path else _CONSTANTS_PATH
    with p.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    out = {}
    for key, entry in raw.items():
        val = entry["value"]
        if isinstance(val, list):
            val = tuple(val)
        elif isinstance(val, str):
            try:
                val = float(val)
            except ValueError:
                pass
        out[key] = val
    return MappingProxyType(out)


def _const() -> dict:
    return load_constants()


def _gamma_default_rad() -> float:
    return math.radians(_const()["gamma_deg"])


def _epsilon_nadir_rad() -> float:
    return math.radians(_const()["epsilon_nadir_deg"])


def _epsilon_min_rad() -> float:
    return math.radians(_const()["epsilon_min_deg"])


def solar_image(h_m: float, alpha_rad: float | None = None) -> SolarImage:
    """Nadir solar image. h_m is orbital altitude (not orbit radius)."""
    if h_m <= 0:
        raise ValueError("h_m must be positive")
    alpha = _const()["alpha_rad"] if alpha_rad is None else alpha_rad
    d_m = h_m
    D_m = d_m * alpha
    A_image_m2 = math.pi * (D_m / 2.0) ** 2
    return SolarImage(d_m=d_m, D_m=D_m, A_image_m2=A_image_m2)


def irradiance(
    A_m2: float,
    h_m: float,
    eta: float,
    E0: float | None = None,
    alpha_rad: float | None = None,
) -> float:
    """Filled-image irradiance at the terminator-nadir envelope.

    I = E0 * eta * A * cos(gamma) * sin(epsilon) / A_image
    gamma = 45° collector incidence, epsilon = 90° (nadir), d = h.
    Pass eta as a single factor (ideal 1 or rho*tau). Do not also multiply rho and tau.
    There is no off-nadir I(epsilon) in this kernel.
    """
    if A_m2 < 0:
        raise ValueError("A_m2 must be non-negative")
    if eta < 0:
        raise ValueError("eta must be non-negative")
    c = _const()
    gamma = _gamma_default_rad()
    epsilon = _epsilon_nadir_rad()
    e0 = c["E0"] if E0 is None else E0
    img = solar_image(h_m, alpha_rad=alpha_rad)
    return (
        e0
        * eta
        * A_m2
        * math.cos(gamma)
        * math.sin(epsilon)
        / img.A_image_m2
    )


def required_area(
    I_star: float,
    h_m: float,
    eta: float,
    E0: float | None = None,
    alpha_rad: float | None = None,
) -> float:
    """Linear inversion of irradiance at the terminator-nadir snapshot. No 1-sun clip."""
    if I_star < 0:
        raise ValueError("I_star must be non-negative")
    if eta <= 0:
        raise ValueError("eta must be positive")
    I_one = irradiance(
        1.0,
        h_m,
        eta,
        E0=E0,
        alpha_rad=alpha_rad,
    )
    if I_one <= 0:
        raise ValueError("irradiance for unit area is not positive; check geometry")
    return I_star / I_one


def _central_angle_rad(a_m: float, R_e: float, epsilon_rad: float) -> float:
    """Earth-central angle θ(ε) = arccos((R_E/a) cos ε) − ε."""
    x = (R_e / a_m) * math.cos(epsilon_rad)
    if x < -1.0 or x > 1.0:
        raise ValueError("elevation is not visible at this altitude")
    return math.acos(x) - epsilon_rad


def pass_window(
    h_m: float,
    epsilon_min_rad: float | None = None,
    mu: float | None = None,
    R_earth: float | None = None,
) -> PassWindow:
    """Circular Kepler geometric visibility. No umbra, no Earth rotation.

    Period uses a = R_E + h, not h. Horizon and useful window share one ε law.
    Returns the overhead (zenith-track) full window: T * theta / pi with theta one-sided.
    Takes no inclination or LTAN.
    """
    if h_m <= 0:
        raise ValueError("h_m must be positive")
    c = _const()
    mu_e = c["mu_earth"] if mu is None else mu
    R_e = c["R_earth"] if R_earth is None else R_earth
    eps_min = _epsilon_min_rad() if epsilon_min_rad is None else epsilon_min_rad
    a_m = R_e + h_m
    T_period_s = 2.0 * math.pi * math.sqrt(a_m**3 / mu_e)
    theta_h = _central_angle_rad(a_m, R_e, 0.0)
    theta_u = _central_angle_rad(a_m, R_e, eps_min)
    T_horizon_s = T_period_s * theta_h / math.pi
    T_useful_s = T_period_s * theta_u / math.pi
    return PassWindow(
        T_period_s=T_period_s,
        T_horizon_s=T_horizon_s,
        T_useful_s=T_useful_s,
    )


def _depression_default_rad() -> float:
    c = _const()
    if "night_depression_deg" in c:
        return math.radians(float(c["night_depression_deg"]))
    return math.radians(6.0)


def night_snapshot(
    h_m: float,
    depression_rad: float | None = None,
    alpha_rad: float | None = None,
    R_earth: float | None = None,
) -> NightSnapshot:
    """Filled-image geometry at closest approach on a night-side site.

    Satellite on the terminator (sunlit, incoming horizontal). Site is
    `depression` into the night, so the ground Sun is that far below the
    horizon. Recovers terminator-nadir at depression = 0: i = 45°, d = h.
    """
    if h_m <= 0:
        raise ValueError("h_m must be positive")
    c = _const()
    R_e = c["R_earth"] if R_earth is None else R_earth
    alpha = c["alpha_rad"] if alpha_rad is None else alpha_rad
    theta = _depression_default_rad() if depression_rad is None else depression_rad
    if theta < 0:
        raise ValueError("depression must be non-negative (night side)")
    a_m = R_e + h_m
    theta_horizon = _central_angle_rad(a_m, R_e, 0.0)
    if theta > theta_horizon + 1e-12:
        raise ValueError("site is below the horizon from a terminator satellite")
    d_m = math.sqrt(a_m**2 + R_e**2 - 2.0 * a_m * R_e * math.cos(theta))
    sin_eps = (a_m * math.cos(theta) - R_e) / d_m
    sin_eps = min(1.0, max(0.0, sin_eps))
    epsilon = math.asin(sin_eps)
    # 2D terminator plane: sat (0, a), site (−R sinθ, R cosθ), sun +x.
    sx, sy = 0.0, a_m
    gx, gy = -R_e * math.sin(theta), R_e * math.cos(theta)
    tx, ty = gx - sx, gy - sy
    tnorm = math.hypot(tx, ty)
    ux, uy = 1.0, 0.0
    rx, ry = tx / tnorm, ty / tnorm
    nx, ny = ux + rx, uy + ry
    nnorm = math.hypot(nx, ny)
    cos_i = (nx * ux + ny * uy) / nnorm
    cos_i = min(1.0, max(0.0, cos_i))
    i_rad = math.acos(cos_i)
    D_minor_m = d_m * alpha
    D_major_m = D_minor_m / sin_eps if sin_eps > 0 else float("inf")
    A_image_m2 = math.pi * (D_minor_m / 2.0) ** 2 / sin_eps if sin_eps > 0 else float("inf")
    return NightSnapshot(
        theta_rad=theta,
        epsilon_rad=epsilon,
        d_m=d_m,
        D_minor_m=D_minor_m,
        D_major_m=D_major_m,
        A_image_m2=A_image_m2,
        i_rad=i_rad,
        cos_i=cos_i,
        sin_eps=sin_eps,
    )


def irradiance_night(
    A_m2: float,
    h_m: float,
    eta: float,
    depression_rad: float | None = None,
    E0: float | None = None,
    alpha_rad: float | None = None,
) -> float:
    """Canady filled-image I at the night-value snapshot (closest approach).

    I = E0 η A cos(i) sinε / (π (d α/2)²) = E0 η A cos(i) / A_image_ellipse.
    """
    if A_m2 < 0:
        raise ValueError("A_m2 must be non-negative")
    if eta < 0:
        raise ValueError("eta must be non-negative")
    c = _const()
    e0 = c["E0"] if E0 is None else E0
    snap = night_snapshot(h_m, depression_rad=depression_rad, alpha_rad=alpha_rad)
    return e0 * eta * A_m2 * snap.cos_i / snap.A_image_m2


def required_area_night(
    I_star: float,
    h_m: float,
    eta: float,
    depression_rad: float | None = None,
    E0: float | None = None,
    alpha_rad: float | None = None,
) -> float:
    """Linear invert of irradiance_night. No 1-sun clip."""
    if I_star < 0:
        raise ValueError("I_star must be non-negative")
    if eta <= 0:
        raise ValueError("eta must be positive")
    I_one = irradiance_night(
        1.0, h_m, eta, depression_rad=depression_rad, E0=E0, alpha_rad=alpha_rad
    )
    if I_one <= 0:
        raise ValueError("night irradiance for unit area is not positive")
    return I_star / I_one


def pass_window_offtrack(
    h_m: float,
    theta_off_rad: float,
    epsilon_min_rad: float | None = None,
    mu: float | None = None,
    R_earth: float | None = None,
) -> PassWindow:
    """Geometric window for a site offset from the ground track.

    Recover overhead when theta_off = 0. If the site never reaches ε_min,
    T_useful is 0. No umbra, no Earth rotation.
    """
    if h_m <= 0:
        raise ValueError("h_m must be positive")
    if theta_off_rad < 0:
        raise ValueError("theta_off_rad must be non-negative")
    c = _const()
    mu_e = c["mu_earth"] if mu is None else mu
    R_e = c["R_earth"] if R_earth is None else R_earth
    eps_min = _epsilon_min_rad() if epsilon_min_rad is None else epsilon_min_rad
    a_m = R_e + h_m
    T_period_s = 2.0 * math.pi * math.sqrt(a_m**3 / mu_e)
    theta_h = _central_angle_rad(a_m, R_e, 0.0)
    theta_u = _central_angle_rad(a_m, R_e, eps_min)

    def _half_window(theta_lim: float) -> float:
        if theta_off_rad > theta_lim + 1e-12:
            return 0.0
        if theta_off_rad <= 1e-15:
            return theta_lim
        ratio = math.cos(theta_lim) / math.cos(theta_off_rad)
        if ratio >= 1.0:
            return 0.0
        if ratio <= -1.0:
            return math.pi
        return math.acos(ratio)

    T_horizon_s = T_period_s * _half_window(theta_h) / math.pi
    T_useful_s = T_period_s * _half_window(theta_u) / math.pi
    return PassWindow(
        T_period_s=T_period_s,
        T_horizon_s=T_horizon_s,
        T_useful_s=T_useful_s,
    )


def fleet_count(
    I_star: float,
    T_star_s: float,
    A_m2: float,
    h_m: float,
    eta: float,
    depression_rad: float | None = None,
) -> float:
    """Satellites for one site: N = (T*/T_u) * max(1, I*/I).

    Civil-night snapshot. If T_useful is 0, returns +inf.
    A >= A_req ⇒ N = N_T only. Not Earth coverage. Not an integer ceil.
    """
    if I_star < 0 or T_star_s < 0:
        raise ValueError("I_star and T_star_s must be non-negative")
    theta = _depression_default_rad() if depression_rad is None else depression_rad
    tu = pass_window_offtrack(h_m, theta).T_useful_s
    if tu <= 0:
        return float("inf")
    I = irradiance_night(A_m2, h_m, eta, depression_rad=theta)
    if I <= 0:
        return float("inf")
    return (T_star_s / tu) * max(1.0, I_star / I)


def fluence_envelope(I_peak: float, T_useful_s: float) -> float:
    """Upper-bound fluence F = I_peak * T_useful (J/m²).

    I is not constant on the window; T_useful is geometric (no umbra cut).
    """
    if I_peak < 0 or T_useful_s < 0:
        raise ValueError("I_peak and T_useful_s must be non-negative")
    return I_peak * T_useful_s
