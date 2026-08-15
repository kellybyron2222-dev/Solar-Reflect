# Carry B → C

## Conclusions (what we actually implemented)

- Five functions in `src/physics.py`; contract in `spec.md`; numbers in `constants.yaml`.
- `irradiance(A,h,eta)` is **terminator-nadir only** (no γ/ε arguments). \(I=E_0\eta A\cos\gamma\sin\varepsilon/A_\text{image}\) with one \(\eta\); \(\gamma=45^\circ\), \(\varepsilon=90^\circ\), \(d=h\).
- Pass window: \(a=R_E+h\), \(\theta(\varepsilon)=\arccos((R_E/a)\cos\varepsilon)-\varepsilon\) (radians; \(\theta\) one-sided). Overhead zenith-track full window \(T\,\theta/\pi\). Returns **seconds**. No umbra, no i/LTAN.
- `required_area` is linear inversion at that snapshot, no 1-sun clip.
- `fluence_envelope` is \(I\times T_\text{useful}\), labeled upper bound.
- \(\mu\) is `3.986004418e+14` (YAML 1.2 needs the `+`).

## Keep in C

- Hand reconstruction at **625 km** vs code, **1%** (Phase C gate). Independents: \(h=625\) km, M55 (\(A=3025\,\text{m}^2\)), \(\eta=1\) and \(0.675\).
- Identities: \(D=h\alpha\); \(I\times A_\text{image}=E_0\eta A\cos\gamma\) at the snapshot; \(\theta(0)=\arccos(R_E/a)\); \(T_\text{useful}<T_\text{horizon}<T_\text{period}\).
- GEO one-liner: \(D\approx h\alpha\) at \(h=35786\) km \(\approx 333\) km. Not a campaign.
- Diffraction one-liner then drop (C2).
- Flag, do not recode: M1km vs \(A_\text{image}\) at 400 km (E2 owns the flag).

## Cut or defer in C

- Plots, GUI, I* table, STK as T oracle, \(I(\varepsilon)\), n_train, n_overlap, binder classifier, spectral τ, clouds, umbra, J2.
- Do not add 550 km or extra markers.

## Watch

- SI: `h_m` in metres; `pass_window` returns **seconds** (divide by 60 for minutes in tables). Snapshot degrees in prose; code converts. `h=400` is 400 m.
- Do not code `E0 * eta * rho * tau`.
- Do not invent \(I(\varepsilon)\) tests. Kernel has no such argument.
- Do not treat I as deep-night zenith.
- Do not fail tests because linear I exceeds \(E_0\eta\cos\gamma\) (no clip in B).
- τ is clear-sky direct zenith estimated; “realistic” is not all-sky.
- T_useful is max-duration overhead pass, not a typical off-track pass.

## Must not reopen without returning to B (or A)

- Terminator-nadir envelope; no \(I(\varepsilon)\).
- One ε law; a vs d split.
- Five functions only.
- B7 / spec deferred list (including clouds).
