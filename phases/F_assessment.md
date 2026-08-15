# Phase F — Assessment (detailed outline)

**Depends on:** complete results book (Look-back E)  
**Produces:** `assessment.md`  
**Do not produce:** the public essay, new tables, new figures, cost language

---

## Why this phase exists

This is the thought experiment’s answer. It must stand if the report is never written.

---

## Work sequence

### F0. Re-evaluate from E (before the binding map)

E’s results book sets which claims F is allowed to make. F does not get a second analysis.

1. Open `results_book.md` (or `results/e*.md`) and `carry/E_to_F.md`. If carry is missing, stop.
2. Re-read frozen intent and `framing.md` A1.
3. Diff the default F1–F5 outline against E: if E never computed N_train, F cannot quote a train size; if E labeled fluence an upper bound, F cannot treat it as delivered energy; if a marker failed A ≪ A_image, F must carry that caveat.
4. Write `carry/F_scoped.md`: which matrix cells you will fill; which F5 claim *templates* are in play; which you will not write because E has no pointer.
5. If F wants a number that is not in the book, return to E (then look-back E), not “estimate in F.”

Typical E→F impacts:

| If E concluded… | Then F… |
|---|---|
| M18/M55 I is illumination-class | F5 may say that with a pointer; not “useless” |
| C-energy fails on I at those markers | Energy bind; quote A_req or N_overlap from E3/E5 |
| T_useful ≪ 3 h | T bind; quote N_train from E4 |
| F_pass is an upper bound | Do not call it farm output |
| No small-spot requirement in A5 | Ω cells mostly N/A |

### F1. Binding map

Build a matrix: rows = A5 classes; columns = markers {M18, M55, M1km} at a stated \(h\) (default 625 km; you may repeat 400 and 1000 if the book has them).

Each cell: **E** (energy / \(A\) too small for \(I^*\)), **Ω** (étendue / target would need \(D < h\alpha\) — usually N/A unless the class assumed a small spot), **T** (shutter / \(T_\text{useful} < T^*\)), or **pass** (both \(I\) and \(T\) tests pass on that column).

Rules:

- If \(I_\text{peak} < I^*\) → E binds for that snapshot (or \(N_\text{overlap}\) required; write the number, still an energy bind).
- If the class implicitly wants a farm-sized patch \(\ll A_\text{image}\) → Ω binds (only if we claimed that; v1 classes do not require a small spot unless we say so — default: classes accept the solar image).
- If \(I\) test passes but \(T_\text{useful} < T^*\) → T binds; record \(N_\text{train}\).
- Never mark “pass” on \(T^*\) = 3 h for a single pass.

### F2. Ideal vs realistic

For cells that pass ideal and fail realistic: tag **η-sensitive**, not “impossible.”  
For cells that fail ideal: tag **physics-limited at this \(A,h\)**.

### F3. Peak vs duration paragraph

One explicit paragraph: a moonlight-class \(I_\text{peak}\) plus a train is still not energy production unless \(I^*\) and \(T^*\) are both met. Quote E4/E5 numbers.

### F4. Cannot say

Copy B7. Add: light curve vs fluence envelope; low-\(\varepsilon\) atmosphere; daytime \(\gamma\); packing many reflectors (operations, not v1 physics beyond \(N_\text{overlap}\)).

Each open item: “not a conclusion.”

### F5. Numbered claims

Format:

`F5.n  [claim]  (pointer: E# table / scene ID)`

Claims should be of the forms:

- \(D = h\alpha\) at nadir; focusing does not reduce \(D_\min\).
- \(I_\text{peak} \propto A/h^2\) at the default snapshot.
- At 625 km, M18 and M55 lie in illumination-class \(I\) (cite numbers).
- Meeting C-weak or C-energy at 625 km requires \(A\) or \(N_\text{overlap}\) of [number from E3/E5].
- Hours require \(N_\text{train}\) of [number], independent of \(\rho\).

No claim without a pointer. No cost. Allowed negative: “requirement \((I^*,T^*)\) is not met at marker X because …”

### F6. Write `assessment.md`

Headings: Binding map; Ideal vs realistic; Peak vs duration; Cannot say; Claims.

### F7. Carry to G

Write `carry/F_to_G.md`: surviving-claim *candidates* (all F5, with which are solid vs open-tied); figures that actually support them; what the report must not say; whether markers are illustrations.

---

## Look-back F (required)

1. **Intent.** Could this log be the whole project? If it only makes sense as a takedown of a firm, rewrite.
2. **Plan.** Any claim not in E? Delete or go back to E.
3. **Honesty.** Open items listed. Fluence still an upper bound if used.
4. **Ready.** G can pick a subset of claims without computing.

Checklist:

- [ ] Matrix + numbered claims
- [ ] Every claim has a pointer
- [ ] Applications did not change B
- [ ] No 3D-driven claim
- [ ] No report.md yet
- [ ] `carry/F_to_G.md` exists

**No-go examples:** “therefore the company is fraudulent”; dropping T-binds because trains “are just engineering”; using 0.1 lux as a kernel output.

**Go:** boxes true → Phase G. G opens `carry/F_to_G.md` first.
