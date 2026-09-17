# Carry E2 → E3

## Conclusions (what we actually found)

- Kernel table in `results/e2.md`. \(I=E_0\eta A\cos\gamma/A_\text{image}\) at terminator-nadir, \(\gamma=45^\circ\).
- C3 check: M55, 625 km, ideal \(I=0.1097\,\mathrm{W/m^2}\) (rel \(0.011\%\)).
- Realistic is \(\times 0.675\). Centre \(I\) is the same for flat and \(f=h\).
- M1km at 400 km: \(A/A_\text{image}=0.092\). Filled-image formula is then an approximation. Kernel not switched.
- S-I-A: `figures/working/s-i-a.svg`. No \(I^*\) lines.
- S-i-two: `figures/working/s-i-two.svg` — two collecting areas, same \(D\), flat foil, \(I\propto A\) (F7). Not a catalog ID.

## Keep in E3 (still needed)

- Invert E2’s envelope: `required_area(I_star, h, eta)` for each A5 \(I^*\) except handle C-day the same way; both \(\eta\) columns.
- Build S-A-req. Lines = \(I^*\) from A5 only.
- \(T^*\) is not in this table (area does not buy hours).

## Cut or defer in E3

- New \(I^*\) (“because 50 felt low”).
- Mixing duration into required \(A\).
- lux.
- Switching the kernel because M1km at 400 km is 9% of \(A_\text{image}\). Carry the caveat; do not `min()`.

## Watch (assumptions that E3 must not contradict)

- \(I^*\) set === A5 set (moonlight-class 0.003, street/work 0.1, weak PV 50, energy 200, daylight 1000).
- Linear invert even if the target exceeds \(E_0\eta\cos\gamma\).
- Markers remain illustrations.

## Must not reopen without returning to E2 (or E1/C)

- 625 km M55 ideal \(I=0.1097\,\mathrm{W/m^2}\).
- No \(I^*\) horizontals on the E2 copy of S-I-A.
- No lamp \(1/r^2\). No midnight caption.
