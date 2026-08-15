"""Phase C diligence: identities and 625 km hand sheet. No applications, no plots."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.physics import (  # noqa: E402
    fluence_envelope,
    irradiance,
    load_constants,
    pass_window,
    required_area,
    solar_image,
)

C = load_constants()
H_625 = 625_000.0
H_400 = 400_000.0
GEO_H = 35_786_000.0
ETA_IDEAL = 1.0
ETA_REAL = 0.675
A_18 = 18.0 ** 2
A_55 = 55.0 ** 2

# Hand sheet (tests/hand_625.md) — four significant figures; code must match to 1%.
HAND_D_M = 5.812e3
HAND_A_IMAGE = 2.653e7
HAND_I_18_IDEAL = 0.01175
HAND_I_18_REAL = 0.007932
HAND_I_55_IDEAL = 0.1097
HAND_I_55_REAL = 0.07406


def test_T_D_identity():
    img = solar_image(H_625)
    expected = H_625 * C["alpha_rad"]
    assert img.D_m == pytest.approx(expected, rel=1e-12)


def test_T_energy_identity():
    img = solar_image(H_625)
    I = irradiance(A_55, H_625, ETA_IDEAL)
    lhs = I * img.A_image_m2
    rhs = C["E0"] * A_55 * math.cos(math.radians(C["gamma_deg"]))
    assert lhs == pytest.approx(rhs, rel=0.01)


def test_T_invert():
    I = irradiance(A_55, H_625, ETA_IDEAL)
    A_back = required_area(I, H_625, ETA_IDEAL)
    assert A_back == pytest.approx(A_55, rel=0.01)


def test_T_GEO():
    D_km = solar_image(GEO_H).D_m / 1000.0
    assert 320.0 <= D_km <= 340.0


def test_T_diffraction_then_drop():
    lam = 550e-9
    D_ap = 10.0
    d = H_625
    airy = 1.22 * lam * d / D_ap
    solar_D = solar_image(H_625).D_m
    assert solar_D / airy > 1e4


@pytest.mark.parametrize(
    "A, eta, hand_I",
    [
        (A_18, ETA_IDEAL, HAND_I_18_IDEAL),
        (A_18, ETA_REAL, HAND_I_18_REAL),
        (A_55, ETA_IDEAL, HAND_I_55_IDEAL),
        (A_55, ETA_REAL, HAND_I_55_REAL),
    ],
)
def test_worked_625_vs_hand_sheet(A, eta, hand_I):
    I = irradiance(A, H_625, eta)
    assert I == pytest.approx(hand_I, rel=0.01)


def test_hand_sheet_D_and_A_image():
    img = solar_image(H_625)
    assert img.D_m == pytest.approx(HAND_D_M, rel=0.01)
    assert img.A_image_m2 == pytest.approx(HAND_A_IMAGE, rel=0.01)


def test_pass_window_horizon_identity():
    R = C["R_earth"]
    a = R + H_625
    theta0 = math.acos(R / a)
    pw = pass_window(H_625)
    T = pw.T_period_s
    assert pw.T_horizon_s == pytest.approx(T * theta0 / math.pi, rel=1e-12)
    assert pw.T_useful_s < pw.T_horizon_s < pw.T_period_s


def test_period_400km_leo_band():
    T_min = pass_window(H_400).T_period_s / 60.0
    assert 90.0 <= T_min <= 95.0


def test_fluence_is_product():
    I = irradiance(A_55, H_625, ETA_IDEAL)
    T_u = pass_window(H_625).T_useful_s
    assert fluence_envelope(I, T_u) == pytest.approx(I * T_u, rel=1e-12)


def test_no_eta_stacking():
    I_eta = irradiance(A_55, H_625, ETA_REAL)
    I_id = irradiance(A_55, H_625, ETA_IDEAL)
    assert I_eta == pytest.approx(I_id * ETA_REAL, rel=1e-12)
