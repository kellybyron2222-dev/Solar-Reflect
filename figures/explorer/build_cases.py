"""Emit cases.json from the kernel. Run from repo root: python figures/explorer/build_cases.py"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.physics import (  # noqa: E402
    fleet_count,
    irradiance_night,
    night_snapshot,
    pass_window_offtrack,
    required_area_night,
)

DEP = math.radians(6.0)
HEIGHTS_KM = (400, 625, 1000, 1500, 2000, 3000)
FOILS = (("M18", 324.0), ("M55", 3025.0), ("M1km", 1.0e6), ("sized", None))
CLASSES = (
    ("C-moon", 0.003, None),
    ("C-light", 0.1, 20 * 60.0),
    ("C-weak", 50.0, 20 * 60.0),
    ("C-energy", 200.0, 180 * 60.0),
)
ETAS = (("ideal", 1.0), ("realistic", 0.675))


def main() -> None:
    rows = []
    for h_km in HEIGHTS_KM:
        h = h_km * 1000.0
        try:
            snap = night_snapshot(h, DEP)
            pw = pass_window_offtrack(h, DEP)
        except ValueError:
            continue
        tu = pw.T_useful_s
        for class_id, i_star, t_star in CLASSES:
            t_use = tu if t_star is None else t_star
            for foil_id, A_fixed in FOILS:
                for eta_id, eta in ETAS:
                    if A_fixed is None:
                        if tu <= 0:
                            A = 0.0
                        else:
                            A = required_area_night(i_star, h, eta, DEP)
                    else:
                        A = A_fixed
                    if tu <= 0 or A <= 0:
                        I = 0.0
                        n = float("inf")
                        n_i = float("inf")
                        n_t = float("inf")
                    else:
                        I = irradiance_night(A, h, eta, DEP)
                        n = fleet_count(i_star, t_use, A, h, eta, DEP)
                        n_i = max(1.0, i_star / I) if I > 0 else float("inf")
                        n_t = t_use / tu
                    rows.append(
                        {
                            "h_km": h_km,
                            "class_id": class_id,
                            "foil_id": foil_id,
                            "eta_id": eta_id,
                            "A_m2": A,
                            "I": I,
                            "I_star": i_star,
                            "T_useful_min": tu / 60.0,
                            "T_star_min": None if t_star is None else t_star / 60.0,
                            "N": None if n == float("inf") else n,
                            "N_I": None if n_i == float("inf") else n_i,
                            "N_T": None if n_t == float("inf") else n_t,
                            "d_km": snap.d_m / 1000.0,
                            "eps_deg": math.degrees(snap.epsilon_rad),
                            "i_deg": math.degrees(snap.i_rad),
                            "D_minor_km": snap.D_minor_m / 1000.0,
                            "D_major_km": snap.D_major_m / 1000.0,
                            "no_pass": tu <= 0,
                        }
                    )
    out = Path(__file__).with_name("cases.json")
    out.write_text(json.dumps({"depression_deg": 6.0, "cases": rows}, indent=2), encoding="utf-8")
    print(f"wrote {out} ({len(rows)} cases)")


if __name__ == "__main__":
    main()
