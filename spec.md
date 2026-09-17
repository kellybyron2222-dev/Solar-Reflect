# Kernel spec (Phase B)

**Readable formulas:** open the [drafting board](whiteboard/index.html) (`python whiteboard/serve.py`) — or [`notebooks/the_model.html`](notebooks/the_model.html). Each equation below also has a **Plain:** line.

Contract for `src/physics.py`. Defaults from `framing.md` v3. Constants: `constants.yaml`.

**Units in code:** metres, seconds, radians, watts. `pass_window` returns **seconds** (framing tables use minutes for reading). Snapshot numbers \(45^\circ\), \(90^\circ\), \(30^\circ\) are degrees in prose; convert before evaluating \(\cos/\sin/\arccos\).

## Snapshot

**Envelope (`irradiance`).** Terminator-nadir: \(d=h\), \(\gamma=45^\circ\), \(\varepsilon=90^\circ\). Canady special case.

**Value (`irradiance_night`).** Terminator-sunlit satellite, site at solar depression \(\theta\) (default \(6^\circ\), civil night). Closest approach. \(d>h\), \(\varepsilon<90^\circ\), foil incidence \(i\) from the sun/target bisector. Local midnight nadir is not this call.

\(\varepsilon_\min\) is shutter-only. Off-track duration is `pass_window_offtrack`.

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

## Night image and irradiance (value snapshot)

Satellite on the terminator. Site Earth-central angle \(\theta\) toward night (= solar depression). Slant range and elevation:

\[
d=\sqrt{a^2+R_E^2-2a R_E\cos\theta},\qquad \sin\varepsilon=(a\cos\theta-R_E)/d
\]

Ellipse \(A_\text{image}=\pi(d\alpha/2)^2/\sin\varepsilon\). Foil \(\cos i\) from the bisector of sun-direction and look-direction (recovers \(i=45^\circ\) at \(\theta=0\)).

\[
I=\frac{E_0\eta A\cos i}{A_\text{image}}
\]

**Plain:** `night_snapshot(h, theta)` · `I = E0 * eta * A * cos_i / A_image`

Off-track window: \(\psi_\max=\arccos(\cos\theta_\text{lim}/\cos\theta_\text{off})\) when \(\theta_\text{off}<\theta_\text{lim}\), else \(0\). \(T=T_\text{period}\,\psi_\max/\pi\). Recovers overhead at \(\theta_\text{off}=0\).

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
`irradiance(A,h,eta)` → \(I\) (W/m²), terminator-nadir envelope  
`required_area(I,h,eta)` → \(A\) (m²)  
`pass_window(h,ε_min)` → \(T,T_\text{horizon},T_\text{useful}\) (**seconds**), overhead  
`night_snapshot(h,θ)` → \(d,\varepsilon,i,D,A_\text{image}\)  
`irradiance_night(A,h,eta,θ)` → \(I\) (W/m²), civil-night value snapshot  
`required_area_night` → invert of `irradiance_night`  
`pass_window_offtrack(h,θ_off,ε_min)` → off-track window  
`fluence_envelope(I,T_useful)` → \(F\) (J/m²)  
`fleet_count(I*,T*,A,h,η)` → \(N=(T^*/T_u)\max(1,I^*/I)\) (one site; \(+\infty\) if no pass)

No plots. No \(I^*\) table. No \(N_\text{train}\). No \(N_\text{overlap}\). No binder classifier. No full light-curve \(I(t)\).

## Deferred (F must not discover these as findings)

Spectral \(\tau(\varepsilon)\), clouds as peak \(I\), J2, eclipse/umbra along the pass, Earth rotation, PSF/slope error, limb darkening, diffraction, BRDF, 3D, daytime \(\gamma\), light-curve integral, constellation scheduling, albedo, pointing, true midnight / polar exceptions. Civil-night closest-approach \(I\) is in-kernel (`irradiance_night`).

## Dominance (C4)

Peak \(I\) scales linearly with collecting area \(A\). Peak \(I\) scales as \(1/h^2\) because \(A_\text{image}\propto h^2\), not because the reflector is a lamp. Peak \(I\) scales with \(\eta\). Clouds do not belong in peak \(I\) (clear-sky envelope; weather is deferred).

<!-- board-review -->
## Board review

Votes from the drafting board. Not freeze text until an iteration below is accepted.

| Concept | Vote | Comment |
|---|---|---|
| Only one brightness geometry | **agree** |  |
| Patch size | **agree** |  |
| Brightness formula | **agree** |  |
| How long a pass lasts | **agree** |  |
| Energy per pass is an upper bound | **agree** |  |
| Missing physics is not a finding | **agree** |  |

<!-- iteration -->

_No iteration written yet._
<!-- /iteration -->
<!-- /board-review -->
