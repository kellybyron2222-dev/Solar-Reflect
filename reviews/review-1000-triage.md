# 1000-persona review — synthesis and triage

Simulated, clustered, after E5 + literature pass, then an independent recompute of `physics.py` against E1–E5. **Not** 1000 interviewed humans and **not** a poll. Freeze rule is the same as A/B/C: union of FATAL/MAJOR, not vote count.

Living professionals (Canady, McInnes, Çelik, Fraas, Ehricke’s corpus) were read as **published work**, not queried live.

## Tally (10 blocks × 100)

Parent pass vs later independent pass (same session). Freeze is the **union of issues**, not either count.

| Block | Personas | Approve | Nits | Reject |
|---|---|---|---|---|
| 1 optics / étendue / solar image | 100 | 55 | 40 | 5 |
| 2 irradiance / 1-sun / energy | 100 | 50 | 42 | 8 |
| 3 large-foil \(D=h\alpha+w\) vs kernel | 100 | 40 | 50 | 10 |
| 4 orbits / shutter / umbra | 100 | 48 | 45 | 7 |
| 5 atmosphere / photometry / lux | 100 | 35 | 55 | 10 |
| 6 A5 applications | 100 | 42 | 48 | 10 |
| 7 methods / tests / hand sheet | 100 | 70 | 28 | 2 |
| 8 figures / twilight vs midnight | 100 | 52 | 40 | 8 |
| 9 process / honesty / scope | 100 | 60 | 35 | 5 |
| 10 modern OSR literature | 100 | 45 | 48 | 7 |
| **Parent total** | **1000** | **497** | **431** | **72** |
| Independent recompute (union, not a second vote) | 1000 | 459 | 449 | 92 |

Rejects are mostly worldview (want night-lighting kernel, want cost, want a clip in `irradiance`, want GEO product, “20 min so your 6.7 is a bug”). They do not move \(D=h\alpha\) or the energy identity. Arithmetic check: E1–E4 match `physics.py`; Çelik \(A_\text{image}(1000\,\mathrm{km})=67.93\,\mathrm{km}^2\) and \(T_\text{pass}=17.6\,\mathrm{min}\) match.

## Union FATAL

**None on arithmetic.** Hand sheet, C identities, Canady nadir special case, and Çelik period/horizon all match.

One **near-fatal process risk** (not a formula bug): a reader who uses \(T_\text{useful}\) where the OSR literature says “pass duration” will think we are \(2.5\times\) short at 1000 km (\(6.73\) vs \(\sim 20\,\mathrm{min}\)). That is \(\varepsilon_\min=30^\circ\) plus literature rounding of \(T_\text{horizon}=17.61\,\mathrm{min}\). **Mitigated in E5 §3.3, F13, S-dwell caption, hand sheet.**

## Union MAJOR

| Issue | Disposition |
|---|---|
| Literature \(T_\text{pass}\) = our \(T_\text{horizon}\) | **Now:** E5, F13, S-dwell, hand sheet. Horizon at 2000 km would pass \(20\,\mathrm{min}\); useful does not |
| \(F_\mathrm{pass}\) looks like farm energy | **Now:** F5.6; already E4 upper bound. Do not loosen |
| Kernel \(D=h\alpha\) vs F12 \(D=h\alpha+w\) looks like a flip | **Now:** F2 1% cut + F12; keep both. Do not put \(+w\) in `solar_image` |
| Peak \(I\) vs mean \(I\) at PV fills | **Now:** E3 note (centre \(I^*\)); S-I-A dashed. No further mix |
| F11 962 as “étendue 1-sun ceiling” | **Now:** F11/O15: 962 is the small-\(A\) formula at fill, not radiance. No clip in code. Do not say C-day is unreachable by étendue |
| E5 \(N_\text{overlap}\) past fill (C-day 27.57 × M1km) | **Now:** E5 §3.4 footnote. Linear invert, not stacked suns |
| Unsteered \(D/v\sim 1\,\mathrm{s}\) vs steered \(T_\text{useful}\) | **Now:** E4 / F13. Pointing still deferred |
| C-day \(I^*=1000\) past fill | **Keep:** linear invert, no clip (A/E policy) |
| M55 realistic vs C-light \(0.1\) | **Now:** F2 η-sensitive. Not a new \(I^*\) |
| No \(I(\varepsilon)\) / light curve | **Later:** parked. Çelik’s Fraas critique is why \(F\) stays an envelope |
| \(\tau=0.75\) vs Hottel zenith \(\approx 0.64\) (\(\sim 17\%\) high) | **Later:** optional E-sens. Do not retune the frozen constant |
| M1km square \(10^6\,\mathrm{m}^2\) \(\neq\) Canady 1 km disk | **Now:** named in literature note. Marker stays a square illustration |
| Canady 8 lux GEO is 16 craft, not one M1km | **Now:** literature note. lux still not a kernel output |
| M1km @ 400 km \(A/A_\text{image}=0.092\) | **Keep caveat.** Only cell that clears \(I^*=50\) |
| Terminator-nadir vs “light the night” | **Keep A.** Hostile 85-class reject already frozen |
| \(T_\text{useful}\) weakly tested while F binds on it | **Now:** hand sheet + 1% test for 625 km and 1000 km pair |
| F12 \(+w\) vs Canady \(+D_m\cos\gamma\) vs Çelik RSS | **Later:** one table. Three finite-size stories; centre \(I\) still kernel until fill ~1 |

## Nits (do not reopen kernel)

Off-track passes shorter; Earth rotation \(\sim 4^\circ\) in a 1000 km pass (Çelik 2023); square markers on circular F12 curves; S-geo-2d panel 2 Sun-above composition (O11); S-focus \(D_\max\) illustration vs hemisphere; MASTER leftover \(A_\text{farm}\); no STK; S-I-A \(I^*\) lines wait for an E5 *copy* (not drawn).

## Game plan

### Do now (this pass)

1. E5 readout tables — **done** (`results/e5.md`).
2. Literature stamp on dwell — **done** (E5, F13, S-dwell, hand sheet).
3. Close E and write F map — **done** (`carry/E_to_F.md`, `assessment.md`).
4. Honesty from independent recompute — **done** (F11 962 language; E5 \(N_\text{overlap}\); E3 centre vs mean; unsteered \(D/v\); \(T\) oracle).
5. This triage file.

### Consider later (v1.1 / v2, not a silent kernel edit)

- Off-nadir dark-site \(I(\varepsilon)\) and umbra (the actual night-lighting geometry).
- Light-curve integral vs \(F_\mathrm{pass}\) (Çelik-style; their Fraas correction is \(4\)–\(6\times\)).
- Optional E-sens: \(\tau=0.75\) vs Hottel \(0.64\); \(\varepsilon_\min=0^\circ/15^\circ/30^\circ\) (show the 2000 km 20 min flip).
- Canady eq. (14) \(+D_m\cos\gamma\) vs F12 \(+w\) vs Çelik RSS at M1km.
- E5 copy of S-I-A with \(I^*\) horizontals.
- Photometric lux with Canady’s \(9.96\,\mathrm{mW\,m^{-2}\,lx^{-1}}\), labeled derived.
- Tracked vs unsteered dwell as a caption series, not a new kernel.

### Remove as out of scope (do not do)

- Cost, launch, constellation optimization, company evaluation.
- Clouds inside peak \(I\); spectral MODTRAN kernel.
- `min()` clip in `irradiance()`.
- New \(I^*\) or new A5 class.
- 3D / GUI / photoreal.
- Treating 1000 simulated personas as a vote to unfreeze A.
- Claiming live interviews with Canady, McInnes, Çelik, or Fraas.
- Replacing \(D=h\alpha\) in `solar_image` with \(h\alpha+w\).

## Freeze on the review itself

Kernel stays. Small-foil \(D\) and \(I\) at 625 km stay trusted. \(T_\text{useful}\) stays the \(30^\circ\) shutter, now with a hand-sheet oracle. Report (G/H) may not invent a third time window. If a sentence says “20 min at 1000 km,” it means **horizon / literature \(T_\text{pass}\)**, not `pass_window`’s default useful column. Next human call: whether to open G (figure list) or stop at `assessment.md`.
