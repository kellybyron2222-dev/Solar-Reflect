# Framing note (Phase A)

Status: v3 — freeze after peer review and 100-persona pass. No results.

**Readable formulas:** [drafting board](whiteboard/index.html) (`python whiteboard/serve.py`) or [`notebooks/the_model.html`](notebooks/the_model.html). This file is the question freeze, not the typeset notebook.

---

## 1. Question

**Primary.** For a specular orbital reflector of collecting area \(A\) at altitude \(h\) with optical factor \(\eta\), what peak irradiance \(I_\text{peak}\), solar-image diameter \(D\), and dwell \(T\) can be delivered to Earth’s surface at a stated **terminator-nadir snapshot**, and which fact binds first: **energy** (including solar-image dilution from the Sun as an extended source) or the **orbital shutter**? A separate Ω fail (“spot too small”) is N/A for v1 classes unless a class required \(A_\text{target}<A_\text{image}\).

**Secondary.** After those quantities exist, compare them to parked application classes \((I^*, T^*)\). Classes do not choose \(A\), \(h\), or \(\eta\), and they do not alter the kernel.

---

## 2. Variable map

| Symbol | Role | Unit | v1 rule |
|---|---|---|---|
| \(h\) | independent | km | Grid: 400, 625, 1000, 2000 |
| \(A\) | independent | m² | Continuous; markers M18, M55, M1km |
| \(\eta\) | independent | — | \(\eta=\rho\tau_\text{zenith}\). Ideal \(=1\); estimated clear-sky \(=0.9\times 0.75=0.675\). Never stack a second \(\tau\) |
| \(E_0\) | source | W/m² | AM0 solar constant (number in B). Collected power \(P=E_0 A\cos\gamma\,\eta\) at \(\sin\varepsilon=1\) |
| \(\gamma\) | scenario | deg | **45 = collector incidence** at terminator-nadir. Not swept. Not ground solar zenith |
| \(\varepsilon\) | scenario for \(I\) | deg | **90 (nadir) always** for the \(I\) envelope. \(\sin\varepsilon\) is not evaluated at \(\varepsilon_\min\) |
| \(\varepsilon_\min\) | scenario for \(T\) | deg | 30; **shutter only**; strict \(\varepsilon>30^\circ\) |
| \(d\) | calculated | km | \(d=h\) at nadir |
| \(\alpha\) | source | rad | \(9.3\times 10^{-3}\), **mean full solar angular diameter** |
| \(D\) | dependent | km | \(D=d\alpha\) |
| \(A_\text{image}\) | dependent | m² | \(\pi(D/2)^2\) at nadir; convert \(D\) to metres before squaring |
| \(I_\text{peak}\) | dependent | W/m² | \(P/A_\text{image}\) on the filled solar image (Canady). **Not** inverse-square from a lamp |
| \(T_\text{horizon}\) | dependent | min | Circular Kepler, horizon to horizon. Period uses \(a=R_E+h\), not \(h\) |
| \(T_\text{useful}\) | dependent | min | Geometric time with \(\varepsilon>30^\circ\). Not “sunlit and dark” time |
| \(F_\text{pass}\) | derived | J/m² | \(I_\text{peak}\times T_\text{useful}\); **upper bound** (I is not constant on the window) |
| \(N_\text{overlap}\) | derived | — | \(I^*/I_\text{one}\); E5 only |
| \(N_\text{train}\) | derived | — | \(T^*/T_\text{useful}\); **shutter ratio**, not satellite count |
| lux | derived | lx | Never primary; not a kernel output |
| \(I^*\), \(T^*\) | parked | W/m², min | §5; unused until E5 |

No \(A_\text{farm}\) in v1.

---

## 3. Grid, snapshot, markers

**Altitudes:** 400, 625, 1000, 2000 km. GEO = Phase C one-line \(D\) check (\(\approx 333\) km), not a campaign, not a plot axis.

**Area:** continuous \(A\) (log). Markers (scale illustrations, not the subject):

| Marker | Side | \(A\) |
|---|---|---|
| M18 | 18 m | 324 m² |
| M55 | 55 m | 3025 m² |
| M1km | 1 km | \(1.00\times 10^6\) m² |

**Default \(I\) snapshot:** terminator-nadir. Satellite over the terminator, nadir footpoint at dusk/dawn, collector incidence \(\gamma=45^\circ\), \(\varepsilon=90^\circ\), sunlit. This is **not** zenith over a deep-night dark target (that state is off-nadir or eclipsed). Envelope bias: **conservative vs daytime** (\(\gamma<45^\circ\), larger \(\cos\gamma\)); **optimistic vs deeper-night still-sunlit nadir** (\(\gamma>45^\circ\), smaller \(\cos\gamma\)) and vs lighting a dark site from a dawn-dusk orbit (off-nadir).

**Why twilight, not the darkest night.** A specular mirror can only bounce sunlight that is actually hitting it. At local midnight with the satellite overhead, low Earth orbit is usually in Earth’s shadow (umbra): the ground is dark *and* the mirror sees no Sun, so \(I=0\). The geometry that *can* light a dark city is different: satellite still sunlit, beam aimed off-nadir into the night. That case has longer range, a larger solar image, worse incidence, and needs an eclipse model. It is parked, not substituted. Terminator-nadir is the sunlit-overhead envelope, not a night-lighting claim. Do not read \(I\) here as “brightness at 2 a.m.”

Filled-image \(I\propto A/A_\text{image}\) assumes \(A\ll A_\text{image}\). Do not switch formulas in B; flag M1km at low \(h\) in E2. The linear law approaches a flat 1-sun sanity line \(I\lesssim E_0\eta\cos\gamma\) as \(A\to A_\text{image}\). That is the same energy/image formula, not a second kernel, not an étendue \(\min()\) in `irradiance`, and not a radiance quantity.

---

## 4. Glossary

- **Solar image / patch** — ground region set by the Sun as an **extended source**. Diameter \(D_\min=d\alpha\) for **flat and focusing**; focusing is not a \(D\) knob. Not a collimated searchlight.
- **Étendue** — the Sun’s finite solid angle already sets \(D_\min\) and the dilution inside \(I\). Not a third v1 binder.
- **Peak irradiance \(I_\text{peak}\)** — snapshot W/m² = collected power / filled solar-image area, terminator-nadir only.
- **Fluence envelope \(F_\text{pass}\)** — \(I_\text{peak}\times T_\text{useful}\). Upper bound, not a light curve and not night-delivery energy.
- **Dwell / useful pass** — geometric time above \(\varepsilon_\min\). Eclipse/umbra not subtracted.
- **Binding fact** — energy (including solar-image dilution), or shutter. Ω (“spot too small”) is N/A for v1 classes.
- **Requirement not met** — allowed negative in F. Not “impractical.” Not a cost or market judgment.

**Drawing bans (A–E):** volumetric beam, spacecraft product shot, “sunlight on demand.” Do not caption this snapshot as “night lighting.”

---

## 5. Parked application classes (E5 / F only)

Magnitude bins for readout, not standards, not kernel inputs. C-moon / C-light \(I^*\) are **estimated** photometric conversions (lux never a kernel output). Terminator-nadir is twilight; C-moon is not a dark-sky scene. PV classes are broadband W/m², not G173.

| ID | Class | \(I^*\) (W/m²) | \(T^*\) | Note |
|---|---|---|---|---|
| C-moon | Moonlight-class | 0.003 | 1 useful pass | **Estimated** radiometric equivalent |
| C-light | Street / work lighting | 0.1 | 20 min | Lighting, not power; **estimated**; not a lighting code |
| C-weak | Weak PV | 50 | 20 min | First PV-band threshold |
| C-energy | Energy production | 200 | 3 h | Dawn/dusk-class I and hours |
| C-day | Daylight-equivalent | 1000 | n/a if \(I^*\) unreachable | Envelope test; may exceed \(E_0\cos\gamma\,\eta\) |

---

## 6. Out of scope (v1)

Cost, launch, policy, ecology, light-pollution ethics, spectral RT / MODTRAN, **clouds as peak \(I\)** (clear-sky envelope only), J2, drag, Earth rotation during the pass, eclipse seasons **and umbra-on-pass**, BRDF / wrinkles as a model, slope-error switch, constellation optimization, company evaluation, photoreal or 3D as a deliverable, daytime \(\gamma \neq 45^\circ\), AI-generated images.

<!-- board-review -->
## Board review

Votes from the drafting board. Not freeze text until an iteration below is accepted.

| Concept | Vote | Comment |
|---|---|---|
| Dusk/dawn snapshot, not midnight | **Agree** | Accepted iteration: keep twilight; midnight nadir is usually shadow. |

<!-- iteration -->
### Iteration — twilight vs darkest night

**Keep terminator-nadir.** Do not switch the kernel to local midnight looking straight down.

At the darkest part of the night, a satellite *overhead* is usually behind the Earth. The mirror is in shadow, so there is no sunlight to reflect. That snapshot is not “the hard lighting case”; it is lights-out unless we also model eclipse (out of v1).

The night-lighting picture people mean is: satellite still in sunlight, beam steered *sideways* toward a dark city. That is off-nadir, longer path, bigger/dimmer solar image, and it needs umbra geometry. Parked. Terminator-nadir \(I\) is optimistic versus that case.

So twilight is not a claim that dusk is the application. It is the only nadir geometry where the mirror is guaranteed sunlit without an eclipse model. Later scoring must not treat this \(I\) as midnight street lighting. C-moon / C-light stay magnitude bins, not a dark-sky scene.

Accept this iteration to freeze the snapshot; reopen it only if v1 should add off-nadir dark-site lighting (new kernel, not a caption change).
<!-- /iteration -->
<!-- /board-review -->

