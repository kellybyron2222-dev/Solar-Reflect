# Phase C — Diligence (detailed outline)

**Depends on:** `spec.md` + `src/physics.py` after Look-back B  
**Produces:** expected-value table (in spec or `tests/expected.md`) + passing `tests/test_physics.py`  
**Do not produce:** figures, assessment language, a second physics

---

## Why this phase exists

Drawings will make wrong numbers look geometric. Tests have to fail first.

---

## Work sequence

### C0. Re-evaluate from B (before the hand sheet)

B’s actual kernel sets C’s tests. Do not test functions that were cut. Do not skip tests for functions that were kept.

1. Open `spec.md` and `carry/B_to_C.md`. If carry is missing, stop.
2. Diff the default tests below against what B actually shipped.
3. Write `carry/C_scoped.md`: the test list for this run (keep / cut / extra only if B added a framed function).
4. Then do the hand sheet and tests **for the scoped list**.

Typical B→C impacts:

| If B concluded… | Then C… |
|---|---|
| Five functions as default | C1–C3 as written |
| Pass-window formula X | One identity test of X; no STK |
| No off-nadir I | Do not test I(ε); only T_useful uses ε_min |
| Fluence is I×T | Test the product identity only |
| M1km may violate A ≪ A_image | Optional note, not a failed energy test |

### C1. Hand sheet (before tests)

On paper or in `tests/hand_625.md`, compute with a calculator:

**Given:** \(h = 625\times 10^3\,\text{m}\), \(\alpha = 0.0093\), \(E_0 = 1361\), \(\gamma=45^\circ\), \(\cos\gamma = 0.7071\).

1. \(D = h\alpha\)
2. \(A_\text{image} = \pi(D/2)^2\)
3. \(A_{18} = 18^2\), \(A_{55} = 55^2\)
4. \(I_\text{ideal} = E_0 A \cos\gamma / A_\text{image}\)
5. \(I_\text{real} = I_\text{ideal} \times 0.675\)

Keep four significant figures. This sheet is the authority. Code must match it, not the reverse.

### C1b. Analytic tests

| Test ID | Statement | Tolerance |
|---|---|---|
| T-D | `solar_image(h).D == h * alpha` | 1e-12 relative (identity) |
| T-energy | `I_ideal * A_image == E0 * A * cos(gamma)` | 1% (trig rounding) |
| T-invert | `required_area(irradiance(A,h,1), h, 1) == A` | 1% |

### C2. One-line limits (tests, not campaigns)

| Test ID | Statement |
|---|---|
| T-GEO | `solar_image(35786e3).D` in 320–340 km |
| T-diffraction | Airy diameter \(1.22\lambda d/D_\text{ap}\) at \(\lambda=550\,\text{nm}\), \(D_\text{ap}=10\,\text{m}\), \(d=625\,\text{km}\) \(\ll\) solar \(D\). Assert ratio \(> 10^4\). Not used in kernel. |

### C3. Worked-example tests

Compare code to the hand sheet for M18 and M55 at 625 km, ideal and realistic. **Relative 1%.**

If they disagree: fix code or fix the hand sheet. Do not average. Do not change \(\alpha\) to make a website claim match.

### C4. Dominance note (prose in spec.md, not a test)

Write four sentences: \(I \propto A\); \(I \propto 1/h^2\); \(I \propto \eta\); clouds do not belong in peak \(I\). C4 is to prevent F from blaming weather for a snapshot.

### C5. Run

```
pytest tests/test_physics.py
```

Gate is **green tests**, not the file existing.

### C6. What not to test yet

Plot pixel regression, 3D cameras, application classification, pass-window vs STK. Pass-window can have a weak test (period at 400 km ~ 90–95 min; \(T_\text{useful} < T_\text{horizon} < T_\text{period}\)). If the exact \(\varepsilon(t)\) formula is new, add one geometric identity from spec.md.

### C7. Carry to D

Write `carry/C_to_D.md`: what numbers are trusted (D, I at 625 km); what is only weakly tested (T_useful); diffraction discarded; stamp fields C6 requires; **do not draw** anything whose number failed a test.

---

## Look-back C (required)

1. **Intent.** Did we start designing visuals because tests were boring? If yes, stop and finish tests.
2. **Plan.** Any test that encodes an \(I^*\) from A5? Delete it. Kernel must not know moonlight.
3. **Honesty.** Hand sheet vs code to 1%. GEO only as D check.
4. **Ready.** You trust \(D\) and \(I\) enough to label a plot axis.

Checklist:

- [x] Hand sheet exists and was done first
- [x] pytest passes
- [x] T-energy and T-D pass
- [x] M18/M55 @ 625 km match hand sheet
- [x] Diffraction discarded, not modeled
- [x] No application logic in tests
- [x] `carry/C_to_D.md` exists (trusted numbers, weak spots, do-not-draw)

**No-go examples:** changing \(\tau\) so that 18 m equals 0.1 lux; skipping the hand sheet; “we’ll check numbers when we plot.”

**Go:** boxes true → Phase D. D opens `carry/C_to_D.md` first. **Passed** (`carry/C_lookback.md`).
