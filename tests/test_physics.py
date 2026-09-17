"""Phase C diligence: identities and 625 km hand sheet. No applications, no plots."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.physics import (  # noqa: E402
    fleet_count,
    fluence_envelope,
    irradiance,
    irradiance_night,
    load_constants,
    night_snapshot,
    pass_window,
    pass_window_offtrack,
    required_area,
    required_area_night,
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
HAND_T_625_MIN = 97.06
HAND_T_HORIZON_625_MIN = 13.16
HAND_T_USEFUL_625_MIN = 4.281
HAND_T_HORIZON_1000_MIN = 17.61
HAND_T_USEFUL_1000_MIN = 6.727
HAND_I_55_NIGHT = 0.01642
HAND_T_USEFUL_NIGHT_625_MIN = 2.809


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


def test_pass_window_vs_hand_sheet():
    pw = pass_window(H_625)
    assert pw.T_period_s / 60.0 == pytest.approx(HAND_T_625_MIN, rel=0.01)
    assert pw.T_horizon_s / 60.0 == pytest.approx(HAND_T_HORIZON_625_MIN, rel=0.01)
    assert pw.T_useful_s / 60.0 == pytest.approx(HAND_T_USEFUL_625_MIN, rel=0.01)
    pw1000 = pass_window(1_000_000.0)
    assert pw1000.T_horizon_s / 60.0 == pytest.approx(HAND_T_HORIZON_1000_MIN, rel=0.01)
    assert pw1000.T_useful_s / 60.0 == pytest.approx(HAND_T_USEFUL_1000_MIN, rel=0.01)


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


def test_night_zero_depression_is_nadir():
    snap = night_snapshot(H_625, depression_rad=0.0)
    img = solar_image(H_625)
    assert snap.d_m == pytest.approx(H_625, rel=1e-12)
    assert snap.D_minor_m == pytest.approx(img.D_m, rel=1e-12)
    assert snap.A_image_m2 == pytest.approx(img.A_image_m2, rel=1e-9)
    assert snap.cos_i == pytest.approx(math.sqrt(0.5), rel=1e-9)
    assert irradiance_night(A_55, H_625, ETA_IDEAL, depression_rad=0.0) == pytest.approx(
        irradiance(A_55, H_625, ETA_IDEAL), rel=1e-9
    )


def test_offtrack_zero_is_overhead():
    pw = pass_window(H_625)
    off = pass_window_offtrack(H_625, 0.0)
    assert off.T_period_s == pytest.approx(pw.T_period_s, rel=1e-12)
    assert off.T_horizon_s == pytest.approx(pw.T_horizon_s, rel=1e-12)
    assert off.T_useful_s == pytest.approx(pw.T_useful_s, rel=1e-12)


def test_night_625_vs_hand_sheet():
    dep = math.radians(6.0)
    assert irradiance_night(A_55, H_625, ETA_IDEAL, dep) == pytest.approx(
        HAND_I_55_NIGHT, rel=0.01
    )
    assert pass_window_offtrack(H_625, dep).T_useful_s / 60.0 == pytest.approx(
        HAND_T_USEFUL_NIGHT_625_MIN, rel=0.01
    )


def test_fleet_count_matches_e7_and_has_small_foil_min():
    dep = math.radians(6.0)
    n625 = fleet_count(0.1, 20 * 60, A_18, H_625, ETA_IDEAL, dep)
    assert n625 == pytest.approx(404.8, rel=0.01)
    n1500 = fleet_count(0.1, 20 * 60, A_18, 1_500_000.0, ETA_IDEAL, dep)
    n2000 = fleet_count(0.1, 20 * 60, A_18, 2_000_000.0, ETA_IDEAL, dep)
    assert n1500 < n625
    assert n1500 < n2000
    n_sized = fleet_count(0.1, 20 * 60, 1.842e4, H_625, ETA_IDEAL, dep)
    assert n_sized == pytest.approx(7.120, rel=0.01)


def test_fleet_product_is_two_ratios():
    dep = math.radians(6.0)
    I_one = irradiance_night(A_55, H_625, ETA_IDEAL, dep)
    T_u = pass_window_offtrack(H_625, dep).T_useful_s / 60.0
    n_I = 0.1 / I_one
    n_T = 20.0 / T_u
    assert n_I * n_T == pytest.approx(43.36, rel=0.01)
    assert required_area_night(0.1, H_625, ETA_IDEAL, dep) / A_55 == pytest.approx(n_I, rel=1e-9)


def test_night_graze_useful_is_zero():
    a = C["R_earth"] + H_625
    theta_u = math.acos((C["R_earth"] / a) * math.cos(math.radians(30.0))) - math.radians(30.0)
    pw = pass_window_offtrack(H_625, theta_u)
    assert pw.T_useful_s == pytest.approx(0.0, abs=1e-9)
    assert pw.T_horizon_s > 0.0
