# Carry A → B

## Conclusions (what we actually decided)

- Primary: \(I_\text{peak}\), \(D\), \(T\) at **terminator-nadir**. Binders = **energy** (incl. solar-image dilution) and **shutter**. Ω (spot too small) is N/A for v1 classes. The 1-sun line \(I\lesssim E_0\eta\cos\gamma\) is the same energy/image law as \(A\to A_\text{image}\), not a third kernel formula and not a `min()` in `irradiance`.
- **I snapshot:** terminator-nadir, \(\gamma=45^\circ\) = **collector incidence**, \(\varepsilon=90^\circ\), sunlit dusk/dawn footpoint. Not deep-night dark-target zenith. Bias: conservative vs daytime \(\gamma<45^\circ\); optimistic vs deeper-night \(\gamma>45^\circ\) and vs off-nadir dark-site lighting.
- \(\eta=\rho\tau_\text{zenith}\). \(\tau_\text{zenith}=0.75\) is **clear-sky, direct-beam, zenith, estimated** — not all-sky, not GHI, not AM1.5/G173. Ideal 1; estimated \(0.9\times 0.75=0.675\). Do not multiply η and ρτ. Do not stack later \(\tau(\varepsilon)\), MODTRAN, or clouds on 0.75.
- \(h\in\{400,625,1000,2000\}\) km. GEO = C one-liner only, not a plot axis. Do not add 550 km.
- \(A\) continuous; M18, M55, M1km are illustrations, not architectures.
- No \(A_\text{farm}\). No \(I^*\) in the kernel. lux not a kernel output. C-moon/C-light stay estimated into E5.
- \(F_\text{pass}=I_\text{peak}\times T_\text{useful}\) is an upper bound because \(I\) is not constant on the window **and** because \(T_\text{useful}\) is geometric (no umbra cut). Airmass on the \(T\) window is already inside that bound — do not swap AM1.5 into \(\tau\).
- \(\varepsilon_\min=30^\circ\) with **strict** \(\varepsilon>30^\circ\) for \(T\) only. Never inside `irradiance` default.
- \(D_\min=d\alpha\) for flat **and** focusing. \(I\) is power/\(A_\text{image}\), not a lamp \(1/r^2\).
- Filled-image linear \(I(A)\) assumes \(A\ll A_\text{image}\); no formula switch in B; E2 flags M1km at low \(h\).
- \(N_\text{train}\) is a shutter ratio, not \(N_\text{sat}\). Keep it out of `physics.py`.
- Earth albedo, climate forcing, light-pollution ethics do not enter \(I\).

## Keep in B

- `solar_image`, `irradiance`, `required_area`, `pass_window`, `fluence_envelope`.
- Write the governing equation in `spec.md`:
  \[
  I = \frac{E_0\,\rho\,\tau\,A\cos\gamma\sin\varepsilon}{\pi(d\alpha/2)^2}
  \]
  Default call: \(\varepsilon=90^\circ\), \(d=h\), \(\gamma=45^\circ\). Internal units: metres.
- Constants: E0 (AM0), α (full diameter), μ, R_E (mean, not ellipsoid), γ, ρ, τ (class `estimated` for realistic), ε_min, h grid, marker sides.
- Default `irradiance` call: nadir, γ=45°. `pass_window`: circular geometric visibility on a spherical Earth; one ε law; period uses \(a=R_E+h\). Do not imply eclipse. Do not take the time fraction from \(2\arcsin(R_E/a)\).
- Deferred list in spec must name **clouds as peak I** (already in B7 default) so F cannot discover weather.

## Cut or defer in B

- Farm intercept. Application names. Off-nadir \(I(\varepsilon)\) as reported envelope.
- Daytime γ, spectral τ, MODTRAN/SMARTS, clouds-as-I, J2, umbra, BRDF/billow-as-D, 3D, N_train, lux, pointing/GNC, SSO state (i/LTAN/β), Earth rotation / ECEF, STK as T oracle, Van Allen, ATOX, albedo.

## Watch

- Do not code `E0 * eta * rho * tau`.
- Do not report \(I(\varepsilon_\min)\) as the envelope.
- Do not treat γ as sun-nadir angle (that would give 90° and \(\cos\gamma=0\)).
- Do not mix \(d=h\) (nadir range) with \(a=R_E+h\) (orbit radius). Do not code \(T=2\pi\sqrt{h^3/\mu}\).
- Do not zero \(I\) or cut \(T\) because the footpoint is dusk.
- Brightness: required_area(C-day) may hit \(I\lesssim E_0\eta\cos\gamma\); do not invent a new formula; E/F note the cap.
- α is full diameter so \(A_\text{image}=\pi(d\alpha/2)^2\). Convert km→m before area.
- Do not implement a binder classifier. Code \(I\) and \(T\) only.
- `pass_window(h)` takes altitude only — not i/RAAN/LTAN.

## Must not reopen without returning to A

- Terminator-nadir as the I envelope (dusk/dawn footpoint, not midnight).
- Two η columns only; τ = clear-sky direct zenith estimated.
- Parked classes and T*; C-moon/C-light estimated.
- framing.md §6 (including clouds).
