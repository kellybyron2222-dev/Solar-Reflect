# Assessment

**Phase F**, with a framed night-value amendment (E6). Every number points at E. Fluence is an upper bound.

**Value snapshot (what the original question meant):** satellite still on the terminator (sunlit), site in **civil night** (Sun \(6^\circ\) below the horizon), closest approach. Default height \(625\,\mathrm{km}\).

**Envelope snapshot (E1–E5):** terminator-nadir twilight. Brighter and longer. Not a dark site. Kept as the Canady special case, not as the application score.

Local midnight overhead is usually umbra (\(I=0\)). That is not a harder lighting case; it is lights-out.

---

## F1. Binding map — civil night, 625 km (E6)

Each cell is **E** (peak \(I<I^*\)), **T** (peak passes, useful dwell \(<T^*\)), **pass** (both), or **n/a**. Ω is N/A.

**Ideal \(\eta=1\).** \(I\): M18 \(0.001759\), M55 \(0.01642\), M1km \(5.429\). \(T_\text{useful}=2.809\,\mathrm{min}\).

| Class | \(I^*\), \(T^*\) | M18 | M55 | M1km |
|---|---|---|---|---|
| C-moon | \(0.003\), 1 pass | E | pass | pass |
| C-light | \(0.1\), \(20\,\mathrm{min}\) | E | E | T (\(N_\text{train}=7.12\)) |
| C-weak | \(50\), \(20\,\mathrm{min}\) | E | E | E |
| C-energy | \(200\), \(3\,\mathrm{h}\) | E | E | E |
| C-day | \(1000\), n/a | E | E | E |

**Realistic \(\eta=0.675\).** Same T. M18 \(0.001187\), M55 \(0.01108\), M1km \(3.664\). Same letters as ideal (M55 C-moon still clears \(0.003\)).

Never mark pass on \(T^*=3\,\mathrm{h}\) for a single pass. No civil-night cell has \(T_\text{useful}\ge 20\,\mathrm{min}\).

**400 km.** Civil night sits at \(\varepsilon_\max=27.2^\circ\), below the \(30^\circ\) shutter: \(T_\text{useful}=0\). No useful night pass on that grid point.

**Nadir envelope (E5), for contrast.** M18/M55/M1km all pass C-moon on \(I\). M55 ideal vs C-light is **T** not E (\(I=0.1097>0.1\), \(T=4.281\,\mathrm{min}\)). That map is twilight, not night.

---

## F2. Ideal vs realistic

On the **night** map, M55 vs C-light is not η-sensitive: both columns fail on \(I\) (\(0.016\) and \(0.011\) vs \(0.1\)). The η-sensitive cell was a twilight artifact. C-weak / C-energy / C-day still fail at \(\eta=1\).

---

## F3. Peak vs duration

Night \(I\) is \(0.150\times\) the nadir envelope at 625 km (longer path, ellipse \(1/\sin\varepsilon\), foil \(i=67.6^\circ\) not \(45^\circ\)). Useful dwell is shorter too (\(2.809\) vs \(4.281\,\mathrm{min}\)) because the site is off the terminator track.

M55 at night meets moonlight-class **brightness** for one pass and misses street-class on **energy**. M1km meets street-class \(I\) and misses \(20\,\mathrm{min}\) (\(N_\text{train}=7.12\)). C-energy still needs both \(A_\mathrm{req}=3.684\times 10^7\,\mathrm{m}^2\) (E6) and \(N_\text{train}=64.1\). Those multipliers do not substitute.

---

## F4. Cannot say (open, not conclusions)

Light curve vs fluence envelope; \(\tau(\varepsilon)\) (realistic \(\eta\) is still zenith); true midnight / polar-summer exceptions; umbra along the pass; packing many reflectors beyond \(N_\text{overlap}\times N_\text{train}\); cost. Off-nadir **civil night** is no longer in this list (E6).

---

## F5. Numbered claims

F5.1  At nadir, \(D=h\alpha\). Focusing at \(f=h\) does not reduce \(D_\min\).  (pointer: E1; S-spot-h; S-focus)

F5.2  Peak \(I\propto A/h^2\) at terminator-nadir because \(A_\text{image}\propto h^2\), not because the foil is a lamp.  (pointer: E2)

F5.3  At 625 km **nadir**, M18 ideal \(I=0.01175\,\mathrm{W/m^2}\) is above C-moon and below C-light. M55 ideal \(0.1097\) is above C-light and far below C-weak.  (pointer: E2; E5 §3.1)

F5.4  Meeting C-weak \(I^*=50\) at 625 km nadir, \(\eta=1\), needs \(A_\mathrm{req}=1.379\times 10^6\,\mathrm{m}^2\). C-day inverts past \(A_\text{image}\) (fill \(1.039\)).  (pointer: E3)

F5.5  Hours are a shutter ratio: nadir \(N_\text{train}(20\,\mathrm{min})=4.67\), \(N(3\,\mathrm{h})=42.0\) at 625 km.  (pointer: E4)

F5.6  \(F_\mathrm{pass}=I_\text{peak}T_\text{useful}\) is an upper bound. M55 @ 625 km nadir ideal is \(28.18\,\mathrm{J/m^2}\).  (pointer: E4)

F5.7  Nadir \((I^*,T^*)=(0.1,\,20\,\mathrm{min})\) is not met by a single M55 pass: ideal brightness passes, duration does not.  (pointer: E5)

F5.8  Civil-night value snapshot at 625 km: \(d=937.5\,\mathrm{km}\), \(\varepsilon=38.74^\circ\), \(i=67.63^\circ\), \(D_\text{minor}=8.719\,\mathrm{km}\), \(A_\text{image}=9.541\times 10^7\,\mathrm{m}^2\), \(T_\text{useful}=2.809\,\mathrm{min}\). \(I=0.150\times\) nadir.  (pointer: E6)

F5.9  At that night snapshot, M18 ideal \(I=0.001759\,\mathrm{W/m^2}\) **fails** C-moon \(0.003\). M55 ideal \(0.01642\) passes C-moon and fails C-light \(0.1\).  (pointer: E6 §4)

F5.10  Street-class \((0.1,\,20\,\mathrm{min})\) at night is **E** for M55 (not the twilight T). M1km is **T** (\(N_\text{train}=7.12\)).  (pointer: E6)

F5.11  400 km cannot serve civil night above \(\varepsilon=30^\circ\) (\(T_\text{useful}=0\)). Nautical night (\(-12^\circ\)) is below the shutter at 625 and 1000 km.  (pointer: E6 §5)

---

## Literature stamp (not a new run)

Canady TP-2065 nadir special case is the **envelope** \(I\) and \(D\). His general eq. 9 is the night snapshot (\(d\), \(\sin\varepsilon\), \(\cos\gamma\)). Çelik \(T_\text{pass}=17.6\,\mathrm{min}\) at 1000 km is still our **overhead** horizon window, not the off-track night \(T_\text{useful}\). Reflect Orbital’s Eärendil-1 (18 m, 625 km, ~5 min, moonlight) is this night case, not our dusk envelope.

---

## F6. Fleet for one site (E7)

\(N=N_I N_T\) at civil night, \(\eta=1\). One site, one window. 400 km: no pass.

| Class | M18 @ 625 km | M55 @ 625 km | M1km @ 625 km | If already \(A_\mathrm{req}\) |
|---|---|---|---|---|
| C-moon | 1.706 | 0.183 (one) | one | 1 |
| C-light | 405 | 43.4 | 0.131 (one + train if smaller) | 7.12 |
| C-weak | \(2.02\times 10^5\) | \(2.17\times 10^4\) | 65.6 | 7.12 |
| C-energy | \(7.29\times 10^6\) | \(7.80\times 10^5\) | 2361† | 64.1 |
| C-day | \(N_I\) only; fill \(>1\) | same | 184† | n/a |

† \(N_I\) past fill ~1 is bookkeeping, not stacked suns.

Raising \(h\) from 625 to 1000 km cuts C-light / C-weak \(N\) by about half (longer \(T_\text{useful}\) wins over a dimmer \(I\)). Pointer: `results/e7.md`.

---

## F7. Optimal count (E8)

\[
N=(T^*/T_\text{useful})\max(1,I^*/I)
\]

Grow \(A\) to \(A_\mathrm{req}\), then \(N=N_T\) only. Fixed 18 m / 55 m: minimum \(N\) near **1500 km** (street-class M18 \(405\to 196\)). Unconstrained 20 min: one sat near 3000 km. Analysis close-out: `results/e8.md`.
