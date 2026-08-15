# Phase B — Spec + kernel (detailed outline)

**Depends on:** `framing.md` after Look-back A  
**Produces:** `spec.md`, `constants.yaml`, `src/physics.py`  
**Do not produce:** tests-as-a-substitute-for-spec (that is C), plots, GUI, application functions

---

## Why this phase exists

The model is the contract and the code together. If they split, the drawings will grow a private physics.

---

## Work sequence

### B0. Re-evaluate from A (do this before any constants or code)

A’s conclusions set B’s scope. The rest of this file is the **default** kernel. It is not automatically the work.

1. Confirm Look-back A passed.
2. Open `framing.md` and `carry/A_to_B.md`. If the carry file is missing, stop.
3. Re-read frozen intent (one minute).
4. Diff this default outline against the carry file:
   - **Keep** — still required for I, D, T.
   - **Cut / defer** — A made it unnecessary (example: no A_farm → no intercept helper).
   - **Watch** — defaults A froze (γ = 45°, nadir envelope, two η columns, markers not architectures).
   - **Must not reopen** — A6 out of scope (no daytime γ, no spectral τ, no application classifier).
5. Write `carry/B_scoped.md`: the actual B checklist (which functions, which constants, what you will not code). If you want something this default outline does not have, that is a framed amendment to A — go back. Do not add it here.
6. Execute B1–B8 **as modified by** `carry/B_scoped.md`, not as a cargo-cult of every bullet below.

Typical A→B impacts:

| If A concluded… | Then B… |
|---|---|
| Night zenith only | Default irradiance call is γ = 45°, ε = 90°; ε is not an envelope input |
| I* parked until E5 | Kernel does not import application names or thresholds |
| Markers are illustrations | Kernel takes continuous A; markers are just example A values |
| No farm intercept in v1 | No A_farm, no intercept fraction function |
| Fluence is in the question | `fluence_envelope` stays in the kernel |

### B1. `constants.yaml`

Include, each with `value`, `unit`, `source`, `class` (`source` | `scenario` | `estimated`):

| Key | Proposed v1 value | Class | Source to cite |
|---|---|---|---|
| E0 | 1361 | source | Kopp & Lean / IAU solar constant order |
| alpha_rad | 0.0093 | source | Mean solar angular diameter (Canady uses 9.3 mrad) |
| mu_earth | 3.986004418e14 | source | IAU / WGS84 GM, m³/s² |
| R_earth | 6371e3 | source | Mean radius, m (state “mean, not WGS84 ellipsoid”) |
| gamma_deg | 45 | scenario | Night zenith from A |
| epsilon_nadir_deg | 90 | scenario | A |
| epsilon_min_deg | 30 | scenario | A |
| rho_ideal | 1.0 | scenario | Envelope |
| tau_ideal | 1.0 | scenario | Envelope |
| rho_real | 0.9 | estimated | Typical aluminized film order |
| tau_real | 0.75 | estimated | Clear-sky broadband zenith order |
| h_grid_km | [400, 625, 1000, 2000] | scenario | A3 |
| marker_sides_m | [18, 55, 1000] | scenario | A3 |

`eta_real = rho_real * tau_real` is calculated in code, not a third independent guess.

Do not put \(I^*\) in the kernel. They live in framing / a small `applications.yaml` read **only** by E5 scripts.

### B2. Geometry (write in spec.md, then code)

Nadir (v1 envelope):

- \(d = h\)
- \(D = d \cdot \alpha\)
- \(A_\text{image} = \pi (D/2)^2\)

Useful pass (time only, not for \(I_\text{peak}\) in v1):

- Circular orbit \(a = R_E + h\)
- Period \(T = 2\pi\sqrt{a^3/\mu}\)
- Horizon half-angle \(\beta = \arccos(R_E / a)\)
- \(T_\text{horizon} = T \cdot (2\beta) / (2\pi)\)
- \(T_\text{useful}\): time with elevation \(\varepsilon \ge \varepsilon_\min\). Spec must state the exact trigonometric cut (central angle from the law of sines / spherical geometry on a circular orbit). Implement one formula and cite it in spec.md. Do not mix two different \(\varepsilon(t)\) models.

**Not in v1 geometry:** Earth rotation during the pass, J2, eclipse, oblateness, refraction.

### B3. Optics

- Filled solar image: the patch is the solar disk, not the projected mirror, for \(A \ll A_\text{image}\) (true for M18 and M55; check M1km at 400 km in E2 and note if the assumption thins).
- \(D_\min\) identical for flat and focusing conjugating the Sun at distance \(d\).
- Scalar \(\rho\) only.

### B4. Irradiance

\[
I = \frac{E_0\,\rho\,\tau\,A\cos\gamma\sin\varepsilon}{\pi(d\alpha/2)^2}
\]

v1 call for envelope: \(\varepsilon=90^\circ\), \(d=h\), \(\gamma=45^\circ\).

Two wrappers: `irradiance_ideal(...)` and `irradiance_realistic(...)` or one function with `eta`.

Units: \(h\) in meters internally; never mix km in the formula.

### B5. Time window

Implement `pass_window(h)` → `T_period, T_horizon, T_useful`.

Document \(\varepsilon_\min = 30^\circ\) as a scenario, not a physical constant.

### B6. Derived (kernel, still no applications)

- `required_area(I_star, h, eta)` — invert B4 at default geometry.
- `fluence_envelope(I_peak, T_useful)` — product, SI, labeled upper bound in the docstring.
- `n_overlap(I_star, I_one)` — trivial divide; may live in E5 instead. If in the kernel, it must not import application names.

### B7. Deferred list (paste into spec.md)

Spectral \(\tau(\varepsilon)\), clouds as peak I, J2, eclipse, Earth rotation, PSF / slope error, limb darkening, diffraction (C will show then drop), 3D, daytime \(\gamma\), light-curve integral, constellation scheduling.

### B8. `src/physics.py` shape (suggested)

```
solar_image(h) -> D, A_image, d
irradiance(A, h, eta, gamma=..., epsilon=...) -> I
required_area(I_star, h, eta, ...) -> A
pass_window(h, epsilon_min=...) -> T_period, T_horizon, T_useful
fluence_envelope(I, T_useful) -> F
```

No matplotlib. No argparse GUI. No reading of \(I^*\) tables.

### B9. `spec.md` (one page)

Must contain: the equation, default snapshot, the pass-window formula you actually coded, deferred list, pointer to constants.yaml. Not a tutorial.

### B10. Carry to C

Write `carry/B_to_C.md`: which functions exist; the exact pass-window formula; 625 km as the reconstruction case; what not to test (plots, I*, STK); any B finding that shrinks C (e.g. “we did not implement off-nadir I → C must not test I(ε)”).

---

## Look-back B (required)

1. **Intent.** Does the code only answer \(I,D,T\) (and derived F, A_req)? If it classifies moonlight vs PV, delete that.
2. **Plan.** Any extra argument (e.g. `epsilon` used to report envelope \(I\))? If yes, either it is only for T_useful or you drifted.
3. **Honesty.** Estimated \(\rho,\tau\) labeled. Mean Earth radius labeled.
4. **Ready.** You can compute 625 km, 55 m, ideal \(I\) with a calculator from spec.md alone.

Checklist:

- [x] constants.yaml complete with classes
- [x] spec.md ≤1–2 pages and matches code
- [x] five functions exist; no plotting
- [x] default call is nadir, \(\gamma=45^\circ\)
- [x] fluence docstring says upper bound
- [x] B7 deferred list written
- [x] `carry/B_to_C.md` written (what was actually implemented; which formula for T_useful; what C should not bother testing)

**No-go examples:** a function `is_useful_for_solar_farm`; using \(\varepsilon=30^\circ\) inside `irradiance` by default; adding aerosol optical depth.

**Go:** boxes true → Phase C. C opens `carry/B_to_C.md` first. **Passed** (`carry/B_lookback.md`, `carry/B_reviews_100.md`).
