# Carry E4 → E5

## Conclusions (what we actually found)

- Kernel table in `results/e4.md`. `pass_window` as implemented in spec (C: \(T\) weakly tested).
- 625 km: \(T_\text{period}=97.06\,\mathrm{min}\), \(T_\text{horizon}=13.16\,\mathrm{min}\), \(T_\text{useful}=4.281\,\mathrm{min}\).
- 400 km period \(92.41\,\mathrm{min}\) in the C band 90–95.
- \(F_\mathrm{pass}=I_\text{peak}T_\text{useful}\) is an **upper bound**. M55 @ 625 km ideal: \(28.18\,\mathrm{J/m^2}\) (\(7.828\times 10^{-3}\,\mathrm{Wh/m^2}\)).
- For a fixed foil, \(F_\mathrm{pass}\) falls with \(h\) (\(I\propto 1/h^2\) beats the slow rise in \(T_\text{useful}\)).
- \(N_\text{train}(20\,\mathrm{min})\) at 625 km \(\approx 4.67\). \(N_\text{train}(3\,\mathrm{h})\approx 42\). One useful pass \(\Rightarrow N=1\). C-day \(T^*\) is n/a.
- S-dwell: `figures/working/s-dwell.svg`. Area does not buy hours.

## Keep in E5 (still needed)

- Place E2 markers on parked \((I^*,T^*)\) from A5.
- Two columns: peak test \(I\gtrless I^*\); duration test \(T_\text{useful}\gtrless T^*\) (or \(N_\text{train}\)).
- Optional \(N_\text{overlap}=I^*/I_\text{one}\) at that \(h\).
- Do **not** combine into a single feasible bit (that is F).
- Prefer a table. \(I^*\) horizontals only on a *copy* of S-I-A if drawn; not on the E2 S-I-A.

## Cut or defer in E5

- New \(I^*\) or new class.
- Treating \(F_\mathrm{pass}\) as delivered farm energy.
- Saying one satellite provides 3 hours.
- Umbra / midnight lighting captions.
- lux unless labeled derived photometric readout.

## Watch (assumptions that E5 must not contradict)

- \(F_\mathrm{pass}\) upper bound; no light curve.
- \(T_\text{useful}\) geometric overhead, \(\varepsilon>30^\circ\), no umbra.
- M1km @ 400 km: \(A/A_\text{image}=0.092\) (E2 approximation note).
- C-day \(T^*\) is n/a; \(I^*=1000\) already past fill even at \(\eta=1\) (E3).
- Markers are illustrations, not architectures.

## Must not reopen without returning to E4 (or E3/E2)

- No new \(T^*\) or \(I^*\).
- Kernel still has no \(N_\text{train}\).
- 625 km M55 ideal \(I=0.1097\,\mathrm{W/m^2}\).
