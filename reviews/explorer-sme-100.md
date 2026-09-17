# Explorer SME-100 — rendering vs kernel

Simulated, clustered, after F18/O26 and the civil-night 3D explorer. **Not** 100 interviewed humans. Freeze rule: union of FATAL/MAJOR on the **drawing**, not a vote to unfreeze A or edit `physics.py`.

Question: does `figures/explorer/` represent F15–F18 and O22–O26, or does it teach the wrong picture?

## Tally (10 blocks × 10)

| Block | Personas | Approve | Nits | Reject |
|---|---|---|---|---|
| 1 optics / solar image / ellipse | 10 | 6 | 3 | 1 |
| 2 irradiance / fill / I* | 10 | 7 | 2 | 1 |
| 3 fleet N_I vs N_T / F18 layout | 10 | 3 | 4 | 3 |
| 4 orbits / terminator / 24°/rev | 10 | 5 | 4 | 1 |
| 5 atmosphere / terminator match | 10 | 4 | 4 | 2 |
| 6 clock / site / one-city | 10 | 2 | 5 | 3 |
| 7 shutter T_useful vs visual pack | 10 | 2 | 3 | 5 |
| 8 foil scale / photoreal | 10 | 6 | 4 | 0 |
| 9 400 km / no-pass / umbra | 10 | 8 | 2 | 0 |
| 10 honesty / captions | 10 | 4 | 5 | 1 |
| **Total** | **100** | **47** | **36** | **17** |

Rejects are almost all **drawing**, not kernel arithmetic. They do not move \(D=d\alpha\), \(N=N_I N_T\), or civil-night \(I\).

## Union FATAL (drawing)

| Issue | Disposition |
|---|---|
| EST clock ~12 h off (noon meridian was +X = Greenwich, formula treated u=0 as noon) | **Fixed.** Local solar time at 75°W. t=0 is ~7:00 AM EST, not 5:00 PM. |
| Atmosphere used view-space normals with world `sunDir` — limb terminator did not match the globe | **Fixed.** World-space normals. |

## Union MAJOR (drawing)

| Issue | Disposition |
|---|---|
| \(N_T\) train packed to foil-width, not \(\Delta\psi=2\pi T_\text{useful}/T\) (~1272 km / 10.4° at 625 km). Contradicted F18/O26 | **Fixed.** Abutting useful windows. Cap 14 still samples the energy train. |
| Ground ellipse floored to ~0.007 rad / 0.22 scene (~40 km) vs true 8.7×13.9 km | **Fixed.** True F15 \(D\). Shader and disc aligned to the look plane (major along the elevation stretch). |
| Packed string read as a “square about the focus.” Moonlight \(N_I\approx 1.7\) drew one foil | **Fixed.** If \(N_T=1\) and \(N_I>1\), draw a tight co-aimed cluster (cap 6). Street-class still draws the train only. |
| Lede said “slightly west.” Successive dusk crossings are **24.3°** west at 625 km | **Fixed.** Caption + HUD `° west/rev`. |
| Patch walks with dusk; clock labeled 75°W. Readers thought the lit site *was* EST | **Fixed.** Stamp: snapshot ≠ city. Clock subtitle: solar time at 75°W, not the walking patch. |

## Nits (do not reopen kernel)

90° polar ≠ SSO \(i\approx 98^\circ\) at 625 km (already analog). J2 not integrated separately (terminator lock is the SSO idealization). Sun sprite not 0.53°. Foils 900× (stamped). Beams are aim lines, not étendue. \(I/I^*\) tints the patch, not a lux scale. Kernel `pass_window` has no Earth rotation; a 20 min train on one plane lets the site drift ~5°. Unsteered \(D/v\sim 1\,\mathrm{s}\) still not drawn (O21). C-day omitted (no \(T^*\)). Stars were square points (fixed earlier).

## Keep (do not “fix”)

- Continents fixed, sun walks, trail in ECEF: that *is* the 24° ground-track story.
- \(N\) is one site, not Earth coverage.
- 400 km: one grey foil, no patch — \(\varepsilon_\max=27^\circ<30^\circ\).
- No umbra cone on the sat: a dawn–dusk polar foil stays sunlit.
- Do not draw \(N_I\times N_T\) as a 2D grid (F18).
- Do not pin a photoreal searchlight to \(I^*\).

## Game plan

### Done this pass

1. EST noon meridian.
2. Atmosphere terminator frame.
3. Train spacing = \(T_\text{useful}\) arc.
4. True-scale look-aligned ellipse.
5. Cluster only when the job is \(N_I\) (\(N_T=1\)).
6. Copy/HUD/stamp/README.
7. This file; O27.

### Later (not a silent kernel edit)

- Fixed-city mode: hold 75°W, beam only inside \(\varepsilon\ge 30^\circ\), show Earth rotation walking the snapshot off the site.
- Real SSO inclination.
- Umbra on a non-terminator comparison orbit.

### Out of scope

- Cost, constellation optimization, photoreal product cinema.
- New \(I^*\) / A5 class.
- Treating 100 simulated personas as a vote to unfreeze A.
