# Carry E3 → E4

## Conclusions (what we actually found)

- Kernel table in `results/e3.md`. \(A_\mathrm{req}=I^* A_\text{image}/(E_0\eta\cos\gamma)\).
- Invert check: \(I=0.1097\,\mathrm{W/m^2}\) at 625 km, \(\eta=1\) recovers M55 (\(3025\,\mathrm{m}^2\)).
- \(A_\mathrm{req}\propto h^2\). Fill fraction \(A/A_\text{image}=I^*/(E_0\eta\cos\gamma)\) is independent of \(h\).
- C-day \(I^*=1000\): \(A_\mathrm{req}>A_\text{image}\) even at \(\eta=1\). Linear invert; no clip.
- S-A-req: `figures/working/s-a-req.svg`. A5 \(I^*\) only. No \(T^*\).

## Keep in E4 (still needed)

- \(T_\text{period}\), \(T_\text{horizon}\), \(T_\text{useful}\) vs \(h\) from `pass_window`. Stamp “as implemented in spec” (\(T\) was weakly tested in C).
- Fluence upper bound \(F_\mathrm{pass}=I_\text{peak}\times T_\text{useful}\) for each E2 marker cell. Units J/m² and Wh/m².
- Derived \(N_\text{train}(T^*)\approx T^*/T_\text{useful}\) for parked \(T^*\) that are not “n/a.” Multiplier table, not a constellation.
- Build S-dwell.

## Cut or defer in E4

- Saying a single satellite “provides 3 hours.”
- Implying eclipse/umbra is subtracted.
- Folding \(T^*\) back into E3’s area story.
- lux.

## Watch (assumptions that E4 must not contradict)

- \(F_\mathrm{pass}\) is an **upper bound** (flat \(I\) for the whole useful window is optimistic).
- \(T_\text{useful}\) is geometric overhead access, \(\varepsilon>30^\circ\), no umbra.
- Area from E3 does not buy hours.

## Must not reopen without returning to E3 (or E2)

- \(I^*\) set remains A5.
- No new \(I^*\).
- 625 km M55 ideal \(I=0.1097\,\mathrm{W/m^2}\).
