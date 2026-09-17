# Phase E — build loop log

## Scope

`carry/E_scoped.md`. E1 now. E2–E5 after each mini look-back.

## E1

- `results/e1.md` — \(D(h)\), \(A_\text{image}(h)\) from `solar_image`
- Figures cited, not redrawn: S-geo-2d, S-spot-h, S-focus
- Check: C1 identity; C3 625 km \(D\) and \(A_\text{image}\)
- Carry: `carry/E1_to_E2.md`

## E2

- `results/e2.md` — \(I_\text{peak}(A,h)\) from `irradiance`
- `figures/s_I_A.py` → `figures/working/s-i-a.svg`
- `figures/s_i_two.py` → `figures/working/s-i-two.svg` (F7 illustration; not a catalog ID)
- F7–F8, O12–O13: centre \(I\) same for flat and \(f=h\); \(I\propto A\) linear
- Check: C3 M55 @ 625 km ideal \(0.1097\,\mathrm{W/m^2}\)
- M1km @ 400 km: \(A/A_\text{image}=0.092\) (approximation note)
- Carry: `carry/E2_to_E3.md`

## E3

- `results/e3.md` — \(A_\mathrm{req}(I^*,h)\) from `required_area`
- `figures/s_A_req.py` → `figures/working/s-a-req.svg`
- Check: invert of M55 @ 625 km recovers \(3025\,\mathrm{m}^2\)
- F9: invert of F7
- Carry: `carry/E3_to_E4.md`

## E4

- `results/e4.md` — \(T_\text{period}\), \(T_\text{horizon}\), \(T_\text{useful}\) from `pass_window`; \(F_\mathrm{pass}=I_\text{peak}T_\text{useful}\) upper bound; \(N_\text{train}\approx T^*/T_\text{useful}\)
- `figures/s_dwell.py` → `figures/working/s-dwell.svg`
- Check: 400 km period \(92.41\,\mathrm{min}\) in 90–95; M55 @ 625 km \(F=28.18\,\mathrm{J/m^2}\)
- F13–F14, O19: useful dwell is minutes; area does not buy hours; no umbra
- Carry: `carry/E4_to_E5.md`

## E5

- `results/e5.md` — readout only. Peak and duration in different columns. No combined feasible bit.
- Check: E2 \(I\); E3 \(N\times A=A_\mathrm{req}\); E4 \(N_\text{train}\); 1000 km \(T_\text{horizon}=17.61\,\mathrm{min}\) = Çelik \(T_\text{pass}\)
- Carry: `carry/E_to_F.md`; look-back `carry/E_lookback.md`

## Extra (F10 / F12)

- `figures/s_a_fill.py` → `figures/working/s-a-fill.svg` — circular foils \(0.1\), \(1\), \(10\) of the solar image; \(D=h\alpha+w\). Not a catalog ID.
- `figures/s_a_shadow.py` → `figures/working/s-a-shadow.svg` — \(D(A)\) and \(A_\text{lit}(A)\).
- S-I-A dashed: mean \(I=P/A_\text{lit}\) (F12). Solid remains kernel peak.

## Gate

Look-back E **passes**. F opens `carry/E_to_F.md`. Assessment: `assessment.md`.
