# B scoped (from A)

Look-back A passed (`carry/A_lookback.md`, `framing.md` v3). Frozen intent: terminator-nadir, not deep-night zenith.

## Diff vs default `phases/B_spec_kernel.md`

| Default | Decision |
|---|---|
| Five functions + fluence | **Keep** |
| B4 equation | **Keep** — write it in `spec.md`; default ε=90°, d=h, γ=45° |
| constants.yaml | **Keep** — τ_real class `estimated`, label clear-sky direct zenith |
| Night zenith default | **Narrow** — terminator-nadir (same numbers; do not name it deep night) |
| I* / n_overlap in kernel | **Cut** — `n_overlap` lives in E5; do not import application names |
| A_farm / intercept | **Cut** |
| Off-nadir I as envelope | **Cut** — ε may exist as an argument but default envelope is nadir |
| B7 deferred | **Keep and name clouds as peak I** (A6) |
| Markers as kernel inputs | **Cut** — constants may list sides; functions take continuous A |
| N_train | **Cut** from physics.py |

## Actual B checklist

1. `constants.yaml` with value / unit / source / class.
2. `spec.md` ≤2 pages: B4 equation, pass-window formula actually coded, defaults, deferred list, pointer to constants.
3. `src/physics.py`: `solar_image`, `irradiance`, `required_area`, `pass_window`, `fluence_envelope`. Stdlib + PyYAML. No matplotlib, no I* table, no binder classifier.
4. Internal SI (metres, seconds, radians). Period uses \(a=R_E+h\). Image uses \(d=h\).
5. Linear inversion even if \(I^*\) exceeds the 1-sun line; do not `min()`.

## Will not code

Daytime γ, spectral τ, MODTRAN, clouds, J2, umbra, BRDF, 3D, lux, pointing, SSO state, Earth rotation, STK, albedo, n_train, n_overlap, farm intercept.

## Pass-window formula (chosen here, coded in B)

Earth-central angle at elevation ε (spherical Earth, circular orbit, no refraction):

\[
\theta(\varepsilon)=\arccos\!\big((R_E/a)\cos\varepsilon\big)-\varepsilon
\]

\(T_\text{horizon}=T\,\theta(0)/\pi\), \(T_\text{useful}=T\,\theta(\varepsilon_\min)/\pi\), \(T=2\pi\sqrt{a^3/\mu}\), \(a=R_E+h\). Duration of \(\varepsilon\ge\varepsilon_\min\) equals the framed \(\varepsilon>30^\circ\) (boundary has measure zero).
