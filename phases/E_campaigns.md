# Phase E — Analysis campaigns (detailed outline)

**Depends on:** Look-back D (S-geo-2d, S-spot-h) and passing C  
**Produces:** `results_book.md` (or `results/e1.md` … `e5.md`) + working figures for remaining scenes  
**Do not produce:** verdicts, report prose, new physics, new \(I^*\)

---

## Why this phase exists

This is the analysis. Everything after is interpretation or summary. Observations here are descriptive (“at 625 km, M55 ideal \(I\) is …”). Binding language waits for F.

After **each** campaign, run the **mini look-back** and write a short carry into the next campaign (`carry/E1_to_E2.md`, etc.). The next campaign’s first step is to re-scope from that carry.

---

## E0. Re-evaluate from D (before E1)

D’s actual figures set what E1 can cite. C’s trusted numbers set what E may treat as quantitative.

1. Open `carry/D_to_E.md` and `carry/C_to_D.md`. If D→E is missing, stop.
2. Write `carry/E_scoped.md`: campaign order still E1→E5 unless D/C force a skip (example: no S-focus file → E1 must carry focusing in prose; do not skip E1).
3. Do not add E6. Do not drop E4 because visuals skipped S-dwell — build S-dwell in E4 from the kernel.

Typical D→E impacts:

| If D/C concluded… | Then E… |
|---|---|
| Only S-geo-2d and S-spot-h exist | E1 proceeds; S-focus in prose if needed; later scenes built in their campaigns |
| S-I-A already exists without I* lines | E2 uses it; still no horizontals |
| T_useful weakly tested | E4 still runs; observation must say “as implemented in spec” |
| M1km A vs A_image flagged in B | E2 includes that caveat |

---

## Shared results-book template (every campaign)

1. Question (one sentence)  
2. Inputs (grid, \(\eta\), geometry)  
3. Table (numbers from kernel)  
4. Figure IDs  
5. Check cited (C1 / C3 / identity)  
6. Observation (≤5 sentences, no verdict)

---

## E1 — Geometry

**Question.** What is \(D(h)\) and \(A_\text{image}(h)\)? What ground target is forbidden?

**Compute.** For \(h\) in {400, 625, 1000, 2000} km (and GEO one-liner): \(D\), \(A_\text{image}\).

**Figures.** S-geo-2d, S-spot-h, S-focus.

**Observation must include:** the forbidden region \(A_\text{target} < A_\text{image}\) cannot be repaired with more \(A\); focusing does not reduce \(D_\min\).

**Mini look-back E1**

- [ ] \(D\) treated as \(h\alpha\), not as a pointing spec
- [ ] GEO is a callout, not a fifth campaign
- [ ] No “so farms cannot…” sentence (that is E5/F)

**Go to E2** only if the table exists and S-focus (or equivalent prose) states \(D_\min\) for focusing. Write `carry/E1_to_E2.md` (patch law locked; do not treat D as a knob in E2).

---

## E2 — Peak irradiance

**First:** read `carry/E1_to_E2.md`. If E1 found the filled-image assumption thin at some h, E2 must note it — not ignore it.

**Question.** What is \(I_\text{peak}(A,h)\) at the default snapshot, ideal and realistic?

**Compute.** For each \(h\) × each marker {M18, M55, M1km} × {ideal, realistic}: \(I_\text{peak}\). Also enough of a curve vs \(A\) to draw S-I-A.

**Figures.** Build S-I-A now. No \(I^*\) horizontals.

**Check.** One cell vs C3 hand sheet (M55, 625 km).

**Mini look-back E2**

- [ ] \(\gamma=45^\circ\) labeled on the table
- [ ] Realistic is \(\times 0.675\), not a new model
- [ ] M1km at 400 km: note whether \(A \ll A_\text{image}\) still holds; if not, one sentence that the filled-image formula is then an approximation (mirror size starts to matter). Do not silently switch formulas.
- [ ] No application names in the observation

**Go to E3** when S-I-A exists and the marker table is complete. Write `carry/E2_to_E3.md` (I(A,h) table is the invert input; no new I*).

---

## E3 — Required area

**First:** read `carry/E2_to_E3.md`. Required A is the invert of E2’s envelope, not a new model.

**Question.** What \(A\) is required for each parked \(I^*\) vs \(h\)?

**Compute.** `required_area(I_star, h, eta)` for each A5 \(I^*\) except handle C-day the same way; both \(\eta\) columns.

**Figures.** Build S-A-req now. Lines = \(I^*\) from A5 only.

**Mini look-back E3**

- [ ] \(I^*\) set === A5 set
- [ ] No new threshold “because 50 felt low”
- [ ] \(T^*\) not mixed into this table (area does not buy hours)

**Go to E4** when the required-\(A\) table exists. Write `carry/E3_to_E4.md` (A_req is about I* only; hours are not in this table).

---

## E4 — Time window and fluence envelope

**First:** read `carry/E3_to_E4.md`. Do not fold T* into E3’s area story.

**Question.** What dwell does circular LEO allow, and what fluence upper bound follows?

**Compute.** For each \(h\): \(T_\text{period}\), \(T_\text{horizon}\), \(T_\text{useful}\).  
For each E2 marker cell: \(F_\text{pass} = I_\text{peak} \times T_\text{useful}\) (convert units explicitly; state J/m² and Wh/m²).

**Also compute, as derived not as a new model:** \(N_\text{train}(T^*) \approx T^* / T_\text{useful}\) for parked \(T^*\) that are not “n/a.” This is a multiplier table, not a constellation design.

**Figures.** Build S-dwell.

**Mini look-back E4**

- [ ] \(F_\text{pass}\) called **upper bound** (flat \(I\) for the whole useful window is optimistic)
- [ ] Single satellite is not said to “provide 3 hours”
- [ ] Eclipse not implied

**Go to E5** when dwell + fluence tables exist. Write `carry/E4_to_E5.md` (F_pass is an upper bound; N_train is a multiplier; single sat ≠ T*).

---

## E5 — Application readout (last)

**First:** read `carry/E4_to_E5.md` plus E1–E3 tables. E5 only places markers on parked (I*, T*). If upstream said peak and duration are separate, E5 keeps two columns.

**Question.** Where do the named markers sit relative to parked \((I^*, T^*)\)?

**Compute, separately:**

- Peak test: \(I_\text{peak} \gtrless I^*\)
- Duration test: \(T_\text{useful} \gtrless T^*\) (or \(N_\text{train}\) needed)
- Optional: \(N_\text{overlap} = I^* / I_\text{one}\) at that \(h\)

**Do not** combine into a single “feasible” bit. That combination is F.

**Figures.** Optional: \(I^*\) horizontals on a *copy* of S-I-A, or a simple classification table only. Prefer a table over a new scene.

**Mini look-back E5**

- [ ] Kernel unchanged
- [ ] No new class
- [ ] Peak and duration in different columns
- [ ] Markers used as illustrations, not as “the system”

---

## Optional E-sens (not a gate)

If E2/E4 left a doubt about \(\tau\) or \(\varepsilon_\min\): one tornado for M55 @ 625 km, \(\rho,\tau,\varepsilon_\min \pm\) a stated range. One page. No new baseline.

---

## Look-back E (whole phase)

1. **Intent.** Is the book still about delivered \(I,D,T\), with applications as the last chapter?
2. **Plan.** Extra campaign? Extra \(I^*\)? Extra altitude? Amend A or delete.
3. **Honesty.** Fluence labeled upper bound. M1km filled-image caveat recorded if needed.
4. **Ready.** F can be written with no new runs.

Checklist:

- [ ] E1–E5 entries complete
- [ ] E5 labeled readout
- [ ] Tables answer \(D(h)\), \(I(A,h)\), \(A_\text{req}\), \(T_\text{useful}\), marker positions
- [ ] No “impractical / useless / will never work” in E
- [ ] No 3D, no cost
- [ ] `carry/E_to_F.md` exists: which binds are even available; fluence caveat; M1km note; E5 is readout only

**No-go examples:** E5 rewritten as the thesis; dropping E4 because “dwell is operational”; inventing 50,000 satellites as a physics result without calling it \(N_\text{overlap}\times N_\text{train}\).

**Go:** boxes true → Phase F. F opens `carry/E_to_F.md` first. Do not open `report.md`.
