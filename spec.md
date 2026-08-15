# Kernel spec (Phase B)

**Readable formulas:** open the [drafting board](whiteboard/index.html) (`python whiteboard/serve.py`) — or [`notebooks/the_model.html`](notebooks/the_model.html). Each equation below also has a **Plain:** line.

Contract for `src/physics.py`. Defaults from `framing.md` v3. Constants: `constants.yaml`.

**Units in code:** metres, seconds, radians, watts. `pass_window` returns **seconds** (framing tables use minutes for reading). Snapshot numbers \(45^\circ\), \(90^\circ\), \(30^\circ\) are degrees in prose; convert before evaluating \(\cos/\sin/\arccos\).

## Snapshot (`irradiance` call — the only \(I\) in this kernel)

Terminator-nadir: \(d=h\), \(\gamma=45^\circ\) collector incidence, \(\varepsilon=90^\circ\). Not deep-night zenith. **No \(I(\varepsilon)\) argument.** \(\varepsilon_\min\) is shutter-only.

## Image

\[
d=h,\qquad D=d\alpha,\qquad A_\text{image}=\pi(D/2)^2
\]

**Plain:** `d = h` · `D = d * alpha` · `A_image = pi * (D/2)**2` (metres)

\(\alpha\) is the **full** solar angular diameter. Compute in metres. \(D_\min=d\alpha\) for flat and focusing.

## Irradiance (Canady filled image)

\[
I=\frac{E_0\,\eta\,A\cos\gamma\sin\varepsilon}{\pi(d\alpha/2)^2}
\]

**Plain:** `I = E0 * eta * A * cos(gamma) * sin(epsilon) / A_image`

At the envelope, \(\sin\varepsilon=1\), \(\cos\gamma=1/\sqrt{2}\). \(\eta=\rho\tau\) is passed as one factor. Do not code \(E_0\cdot\eta\cdot\rho\cdot\tau\). Ideal \(\eta=1\); estimated clear-sky \(\eta=0.9\times 0.75=0.675\).

Linear in \(A\) while \(A\ll A_\text{image}\). No formula switch; no \(I\lesssim E_0\eta\cos\gamma\) clip in code. That sanity line is \(I(A=A_\text{image})\), not AM0 \(E_0\) and not G173 \(1000\).

## Pass window (time only)

Circular two-body, spherical Earth, no refraction, no Earth rotation, no umbra. \(a=R_E+h\). **Not** \(T=2\pi\sqrt{h^3/\mu}\).

\[
T=2\pi\sqrt{a^3/\mu}
\]

**Plain:** `a = R_earth + h` · `T_period = 2 * pi * sqrt(a**3 / mu)`

Earth-central angle **from nadir to the \(\varepsilon\) contour** (one-sided). Law of sines in triangle Earth-center / ground / satellite; angle at ground \(=90^\circ+\varepsilon\):

\[
\theta(\varepsilon)=\arccos\!\big((R_E/a)\cos\varepsilon\big)-\varepsilon
\]

**Plain:** `theta(eps) = arccos((R_earth / a) * cos(eps)) - eps` (radians)

(angles in radians). Horizon identity: \(\theta(0)=\arccos(R_E/a)\). Full overhead (zenith-track) window — satellite traverses \(2\theta\):

\[
T_\text{horizon}=T\,\theta(0)/\pi,\qquad T_\text{useful}=T\,\theta(\varepsilon_\min)/\pi
\]

**Plain:** `T_horizon = T_period * theta(0) / pi` · `T_useful = T_period * theta(30°) / pi` (seconds)

This is **max-duration** geometric access (ground track through the site). Off-track passes are shorter. Coded duration is \(\varepsilon\ge\varepsilon_\min\); framed \(\varepsilon>30^\circ\) differs by a set of measure zero. One \(\varepsilon\) law for horizon and useful cut. Do not use \(2\arcsin(R_E/a)\). `pass_window` takes altitude (and optional \(\varepsilon_\min\)); **no** \(i\)/LTAN/RAAN.

## Derived

- `required_area`: invert irradiance at the terminator-nadir snapshot. Linear even if the target exceeds \(E_0\eta\cos\gamma\).
- `fluence_envelope`: \(F=I_\text{peak}T_\text{useful}\), SI (J/m²), **upper bound** (\(I\) is not constant on the window; \(T\) is geometric overhead duration, no umbra).

## Functions

`solar_image(h)` → \(d,D,A_\text{image}\) (m, m, m²)  
`irradiance(A,h,eta)` → \(I\) (W/m²), terminator-nadir only  
`required_area(I,h,eta)` → \(A\) (m²)  
`pass_window(h,ε_min)` → \(T,T_\text{horizon},T_\text{useful}\) (**seconds**)  
`fluence_envelope(I,T_useful)` → \(F\) (J/m²)

No plots. No \(I^*\) table. No \(N_\text{train}\). No \(N_\text{overlap}\). No binder classifier. No \(I(\varepsilon)\).

## Deferred (F must not discover these as findings)

Spectral \(\tau(\varepsilon)\), clouds as peak \(I\), J2, eclipse/umbra, Earth rotation, PSF/slope error, limb darkening, diffraction, BRDF, 3D, daytime \(\gamma\), light-curve integral, constellation scheduling, albedo, pointing, off-nadir \(I(\varepsilon)\).

## Dominance (C4)

Peak \(I\) scales linearly with collecting area \(A\). Peak \(I\) scales as \(1/h^2\) because \(A_\text{image}\propto h^2\), not because the reflector is a lamp. Peak \(I\) scales with \(\eta\). Clouds do not belong in peak \(I\) (clear-sky envelope; weather is deferred).
