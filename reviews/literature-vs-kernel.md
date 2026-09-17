# Literature vs this kernel

Not a kernel change. Published-work comparison (Canady, Ehricke/SOLARES, Znamya, Çelik–McInnes–Viale–Fraas). Living professionals were **not** interviewed; positions are reconstructed from papers.

## Sources

| Work | What we used it for |
|---|---|
| Canady & Allen, NASA TP-2065 (1982) | Filled-image \(I\), \(D=0.0093d\), GEO \(333\,\mathrm{km}\), \(\gamma=45^\circ\) nadir special case |
| Oberth (1929); Buckingham & Watson (1967–68); Ehricke Lunetta/Powersoletta (1970s); Billman SOLARES | Historical scope: lighting vs energy vs climate; we do not cost or constellation-optimize |
| Znamya 2 (1993), 20 m | Flight: solar-disk image on cloud tops; failed 2.5 is operations, not a formula |
| Çelik & McInnes, ASR 69 (2022) | Analytical energy to a ground target; \(\alpha=0.0093\); finite-reflector term; \(T_\text{pass}\) |
| Viale et al., ASR (2023) reference architecture | 1000 km spot \(\sim 10\,\mathrm{km}\); pass “order of 20 min” |
| Fraas (2012+) polar SPF illumination | Same image-size limit; Çelik flags Fraas as optimistic (slant-range / atmosphere) |

## Matches (formula-level)

1. **Canady (15):** \(D_s=0.0093d\) at nadir. Ours: \(D=h\alpha\) with \(\alpha=0.0093\). GEO callout \(333\,\mathrm{km}\) is Canady’s number.
2. **Canady (12):** \(I=0.707\,I_0 A_m/A_s\) at \(\varepsilon=90^\circ\), \(\gamma=45^\circ\). Ours: \(I=E_0\eta A\cos\gamma/A_\text{image}\) with \(\cos 45^\circ=0.707\). Same snapshot.
3. **Canady (14):** \(D_s=2d\tan(\alpha/2)+D_m\cos\gamma\), last term dropped when \(d\gg D_m\). Ours: kernel drops \(+w\); F12 restores \(D=h\alpha+w\) past the 1% cut. Same two-regime story.
4. **Canady prose:** spot \(\approx 1\%\) of altitude; intensity \(\propto\) reflector area; size independent of reflector while small. E1/E2.
5. **Çelik (2022):** 1000 km period \(T=105\,\mathrm{min}\). Ours \(104.97\,\mathrm{min}\). Their \(T_\text{pass}=17.6\,\mathrm{min}\) **is our \(T_\text{horizon}=17.61\,\mathrm{min}\)**, not \(T_\text{useful}\). Zenith \(A_\text{image}=67.93\,\mathrm{km}^2\) is our E1 number exactly.
6. **Viale (2023):** 1000 km solar-image diameter “on the order of \(10\,\mathrm{km}\)”. Ours \(D=h\alpha=9.30\,\mathrm{km}\). Fraas uses \(\alpha=10\,\mathrm{mrad}\) \(\to 10\,\mathrm{km}\) (7.5% high).
7. **Çelik:** finite reflector “may not be negligible … especially when the reflector is large and/or at lower altitudes.” E2 M1km@400 km flag + F12. At 1 km foil / 1000 km they quote \(67.93\to 68.33\,\mathrm{km}^2\) (+0.5%).
8. **Znamya 2:** 20 m foil \(\approx\) M18. Nadir \(D(400\,\mathrm{km})=3.72\,\mathrm{km}\); reported 5–8 km is an untracked, off-nadir sweep, not a kernel fail.

## Not errors — scoped out of v1 (literature is richer)

| Literature has | Our v1 |
|---|---|
| \(I(\varepsilon)\), elongated ellipse at rise/set | Terminator-nadir envelope only |
| Atmosphere vs elevation; clouds as a factor (Canady \(\tau\), cloud coefficient) | One zenith \(\tau\) inside \(\eta\); clouds out of peak \(I\) |
| Light curve / energy integral over a pass | \(F=I_\text{peak}T_\text{useful}\) **upper bound** |
| Umbra / Earth rotation / SSO dawn-dusk pointing | Geometric overhead; no umbra |
| GEO constellations, solar sailing, hoop-column spacecraft | Not a product study |
| Lunar/Mars cases (Çelik) | Earth only |
| Cost, 8 lux GEO product claim | lux derived; cost out |

Çelik vs Fraas: zenith \(I\times T_\text{pass}\) overstates farm energy by \(\sim 4.6\times\) vs a model with \(\tau(t)\) and image/farm overlap (Çelik 2022). That is the size of misreading our \(F_\mathrm{pass}\) if the upper-bound label is dropped.

**Estimate bias (not algebra):** Hottel zenith \(\tau\approx 0.64\) (Canady/Çelik). Ours \(0.75\) is \(\sim 17\%\) high at nadir; realistic \(\eta=0.675\) is still optimistic vs Canady’s mission stack \(\xi\rho\tau\sim 0.56\). Do not silently retune `constants.yaml`. Optional E-sens later.

**Naming:** M1km is a **1 km square** (\(10^6\,\mathrm{m}^2\)). Canady/Hedgepeth “1 km” is a **disk** (\(7.85\times 10^5\,\mathrm{m}^2\)). Area ratio \(1.27\). Do not equate the marker to their spacecraft.

## Numerical envelope check (Canady 8 lux GEO)

Canady: sixteen 1 km-**diameter** reflectors, GEO, \(\sim 8\,\mathrm{lx}\) over a \(333\,\mathrm{km}\) disk — a **constellation**, not one foil.  
One 1 km disk \(A=\pi/4\times 10^6\,\mathrm{m}^2\). Our kernel at GEO, \(\eta=1\), \(\gamma=45^\circ\): \(I\approx 0.0087\,\mathrm{W/m^2}\) \(\approx 0.87\,\mathrm{lx}\) using Canady’s own \(1361\,\mathrm{W/m^2}/136\,700\,\mathrm{lx}\). His Fig. 15 (0.62 lx) is that number times \(\xi\rho\) and sea-level \(I_0\). Sixteen craft after off-nadir geometry is why he quotes 8 lx. Our M1km square at GEO is \(1.27\times\) the disk (\(\approx 1.1\,\mathrm{lx}\) ideal nadir). Same law; different area and stack. Not a lux kernel.

## Reconstructed expert flags (not interviews)

- **Canady:** would accept eqs. 10–13 as our snapshot; would want eq. 9 for other angles; \(\xi\approx 0.91\) and a cloud policy for design numbers; M1km \(\neq\) his 1 km disk; 8 lux is 16 craft at GEO.
- **Çelik / McInnes:** would accept \(D=h\alpha\) and Kepler \(T_\text{pass}=T_\text{horizon}\); would insist farm **energy** is an integral — \(F_\mathrm{pass}\) must stay a bound (\(\sim 4\)–\(6\times\) over if read as delivered); \(\tau=0.75\) high vs Hottel 0.64; M1km @ 400 km needs the finite-foil term (E2 already flags).
- **Fraas:** 1000 km SSO so the spot is farm-sized; 1-sun needs \(A\sim A_\text{image}\) (our E3 C-day); his extra lamp \(1/R^2\) is the literature’s actual formula error — we do not have it.
- **Hedgepeth / Ehricke:** structure, CMG, 12 g/m², Lunetta vs Powersoletta scale — out of kernel.

## Verdict

The v1 kernel is **sound as a terminator-nadir envelope**: Canady’s zenith special case plus Çelik’s Kepler window, losses collapsed to one \(\eta\). No formula error in \(D\) or \(I\). Soft spots are an optimistic \(\tau\), M1km square vs disk naming, and misreading \(F_\mathrm{pass}\) as a light curve.
