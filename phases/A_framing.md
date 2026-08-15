# Phase A — Framing (detailed outline)

**Depends on:** frozen intent in `MASTER_OUTLINE.md`  
**Produces:** `framing.md` (≤2 pages)  
**Do not produce:** code, plots, `spec.md`, application conclusions

---

## Why this phase exists

Later phases will try to change the question (usually toward a use case or a drawing). A exists so that change has to be explicit.

---

## Work sequence

### A0. Re-read intent (15 min)

Read the **Frozen intent** section of the master outline. Write nothing yet. Confirm you still agree that:

- Primary object is \(I\), \(D\), \(T\), and the binding law.
- Applications are a readout.
- Default geometry is **terminator-nadir** (dusk/dawn footpoint, sunlit), \(\gamma = 45^\circ\) collector incidence, nadir \(I\). Not zenith over a deep-night dark target.
- This is not a 3D or company project.

If you disagree, amend the master outline first. Do not hide the disagreement in `framing.md`.

### A1. Question freeze

Write two paragraphs only.

**Paragraph 1 (primary).** For collecting area \(A\), altitude \(h\), and optical factor \(\eta\), what peak irradiance, solar-image size, and dwell can be delivered to the surface, and which fact binds: conservation of energy, the Sun’s angular size, or the orbital shutter?

**Paragraph 2 (secondary).** After those quantities exist, compare them to parked application classes. Classes do not set the model.

Forbidden in A1: firm names, “useful,” “impractical,” “beam,” markets, lighting-as-the-point.

### A2. Variable map

Fill this table in `framing.md`. Do not add rows without a reason.

| Symbol | Role | Unit | v1 rule |
|---|---|---|---|
| \(h\) | independent | km | Grid: 400, 625, 1000, 2000 |
| \(A\) | independent | m² | Continuous; markers at 18², 55², 1000² m² |
| \(\eta\) | independent | — | Two values: 1 and 0.675 |
| \(\gamma\) | scenario constant | deg | 45 (night zenith). Not swept in v1 |
| \(\varepsilon\) | scenario constant for \(I\) | deg | 90 (nadir) for the \(I\) envelope |
| \(\varepsilon_\min\) | scenario constant for \(T\) | deg | 30, used only for \(T_\text{useful}\) |
| \(d\) | calculated | km | \(d = h\) at nadir |
| \(\alpha\) | source constant | rad | 9.3e-3 |
| \(D\) | dependent | km | \(D = d\alpha\) |
| \(A_\text{image}\) | dependent | m² | \(\pi(D/2)^2\) at nadir |
| \(I_\text{peak}\) | dependent | W/m² | Canady envelope |
| \(T_\text{horizon}\) | dependent | min | Circular Kepler |
| \(T_\text{useful}\) | dependent | min | \(\varepsilon > 30^\circ\) |
| \(F_\text{pass}\) | derived | J/m² or Wh/m² | \(I_\text{peak}\times T_\text{useful}\), upper bound |
| \(N_\text{overlap}\) | derived | — | \(I^*/I_\text{one}\), E5 only |
| \(N_\text{train}\) | derived | — | \(T^*/T_\text{useful}\), E5 only |
| lux | derived | lx | Optional; never primary |
| \(I^*\), \(T^*\) | parked scenario | W/m², min | A5; unused until E5 |

Do not add \(A_\text{farm}\) unless you later frame S-farm. v1 does not need it.

### A3. Grid and markers

**Altitude grid (physics):** 400, 625, 1000, 2000 km.

**GEO:** one-line check \(D \approx 35786 \times 0.0093 \approx 333\) km in C. Not a campaign. Not a plot axis unless a framed change.

**Area:** plots vs continuous \(A\) (log). Overlay three markers only:

| Marker | Side | \(A\) |
|---|---|---|
| M18 | 18 m | 324 m² |
| M55 | 55 m | 3025 m² |
| M1km | 1 km | 1.00×10⁶ m² |

These markers illustrate scale. They are not “the architectures under test” as the subject of the piece.

### A4. Vocabulary (must appear as a short glossary)

Define, in one line each:

- **Solar image / patch** — ground region of diameter \(\sim d\alpha\). Not a beam.
- **Peak irradiance \(I_\text{peak}\)** — snapshot W/m² on the filled solar image at the default geometry.
- **Fluence envelope \(F_\text{pass}\)** — \(I_\text{peak}\times T_\text{useful}\). Upper bound, not a light curve.
- **Dwell / useful pass** — time above \(\varepsilon_\min\).
- **Binding fact** — energy, solar-image size, or shutter, whichever first makes a parked \((I^*,T^*)\) fail.
- **Requirement not met** — the allowed negative verdict in F. Not “impractical.”

**Banned in v1 drawings and in A–E prose:** volumetric beam, spacecraft product shot, “sunlight on demand” as a claim.

### A5. Application classes (parked)

Copy this table unchanged into `framing.md`. Do not use it to choose \(h\) or \(A\).

| ID | Class | \(I^*\) (W/m²) | \(T^*\) | Note |
|---|---|---|---|---|
| C-moon | Moonlight-class | 0.003 | 1 useful pass | \(I^*\) is estimated radiometric equivalent |
| C-light | Street / work lighting | 0.1 | 20 min | Still lighting, not power |
| C-weak | Weak PV | 50 | 20 min | First PV-band threshold |
| C-energy | Energy production | 200 | 3 h | Dawn/dusk-class I and hours |
| C-day | Daylight-equivalent | 1000 | n/a if I unreachable | Envelope test |

If you want different \(I^*\) or \(T^*\), this is the only place to change them, and you must re-run Look-back A.

### A6. Out of scope (copy into framing.md)

Cost, launch, policy, ecology, light-pollution ethics, spectral RT / MODTRAN, J2, drag, eclipse seasons, BRDF / wrinkles as a model, slope-error switch, constellation optimization, company evaluation, photoreal or 3D as a deliverable, daytime \(\gamma \neq 45^\circ\), AI-generated images.

### A7. Draft `framing.md`

Suggested headings only:

1. Question  
2. Variable map (the table)  
3. Grid and markers  
4. Glossary  
5. Parked application classes  
6. Out of scope  

Hard cap: ~800 words / 2 pages. If it is longer, you are writing spec (B) or assessment (F).

### A8. Carry to B (required before leaving A)

Write `carry/A_to_B.md` using the template in `phases/CARRY.md`. It must say, in concrete terms:

- Which defaults B must copy (γ, nadir, η columns, h grid, markers).
- What B must **not** implement (A6 list, parked I* as kernel inputs).
- Any framing choice that shrinks B (e.g. “no A_farm → no intercept function”).
- What B is still expected to deliver (the five functions).

If A concluded that daytime geometry is out, B’s default snapshot is night zenith only — say that explicitly so B does not “helpfully” add ε as an envelope.

---

## Look-back A (required)

Re-read frozen intent. Then:

1. **Intent.** Is paragraph 1 still about \(I,D,T\) and binding law, not a use case?
2. **Plan.** Did any extra altitude, marker, \(I^*\), or geometry appear? If yes: framed amendment or delete.
3. **Honesty.** Is moonlight \(I^*\) marked estimated? Is \(\gamma=45^\circ\) explicit?
4. **Ready.** Could someone write `solar_image` and `irradiance` from this note plus constants, without guessing the question?

Checklist:

- [x] `framing.md` exists and is ≤2 pages
- [x] Primary question has no firm and no application as subject
- [x] \(\gamma = 45^\circ\), nadir \(I\) envelope, \(\varepsilon_\min = 30^\circ\) for \(T\) only
- [x] Markers ≠ definition of \(A\)
- [x] A5 parked (not used to design B)
- [x] A6 list present; none of it appears in A1
- [x] `carry/A_to_B.md` exists and names keep / cut / watch for B

**No-go examples:** “the question is whether solar farms can run at night”; adding 600 km because a website said so without amending A3; adding a 200 m marker “for completeness.”

**Go:** all boxes true → Phase B (`phases/B_spec_kernel.md`). B must open the carry file first. **Passed** (`carry/A_lookback.md`, `framing.md` v3).
