# Carry E → F

## Conclusions (what E actually found)

- E1–E5 books exist: \(D(h)\), \(I(A,h)\), \(A_\mathrm{req}(I^*,h)\), \(T(h)\), \(F_\mathrm{pass}\) upper bound, marker vs \((I^*,T^*)\).
- Trusted: \(D\) and \(I\) at 625 km (C). Weak: \(T_\text{useful}\) (as implemented in spec).
- M1km @ 400 km: \(A/A_\text{image}=0.092\); filled-image is an approximation (E2). Only cell that clears \(I^*=50\) (ideal).
- \(F_\mathrm{pass}\) is an **upper bound**. Çelik/McInnes \(T_\text{pass}(1000\,\mathrm{km})=17.6\,\mathrm{min}\) = our **horizon** window, not \(T_\text{useful}=6.73\,\mathrm{min}\).
- E5 is readout only. Peak and duration were never combined.

## What F may bind

| Bind | Available? | Pointer |
|---|---|---|
| Energy (E) | Yes | E2 \(I\) vs A5 \(I^*\); E3 \(A_\mathrm{req}\); E5 \(N_\text{overlap}\) |
| Shutter (T) | Yes, with weak-\(T\) stamp | E4 \(T_\text{useful}\); E5 \(N_\text{train}\). No cell has \(T_\text{useful}\ge 20\,\mathrm{min}\) |
| Ω (spot too small) | Mostly N/A | A5 classes accept the solar image unless F reopens that |

## What F must not say

- \(F_\mathrm{pass}\) as farm output or night-delivery energy.
- One satellite provides 3 hours.
- Umbra subtracted; midnight street lighting from this snapshot.
- New \(I^*\) or new class.
- Cost, 3D, constellation optimization.
- Combining peak+duration into “feasible” without showing both tests.

## Open (not conclusions)

Off-nadir dark-site lighting; \(I(\varepsilon)\); spectral \(\tau(\varepsilon)\); clouds; light curve; daytime \(\gamma\).
