# Hand sheet — 625 km (authority)

Computed with a calculator from `spec.md` + `constants.yaml` **before** comparing to `physics.py`. Four significant figures. Code must match this sheet to **1%**, not the reverse.

**Given:** \(h = 6.250\times 10^5\,\mathrm{m}\), \(\alpha = 0.0093\), \(E_0 = 1361\,\mathrm{W/m^2}\), \(\gamma=45^\circ\), \(\cos\gamma = 1/\sqrt{2} = 0.7071\).

| Quantity | Formula | Value |
|---|---|---|
| \(D\) | \(h\alpha\) | \(5.812\times 10^3\,\mathrm{m}\) (5.812 km) |
| \(A_\text{image}\) | \(\pi(D/2)^2\) | \(2.653\times 10^7\,\mathrm{m}^2\) |
| \(A_{18}\) | \(18^2\) | \(324\,\mathrm{m}^2\) |
| \(A_{55}\) | \(55^2\) | \(3025\,\mathrm{m}^2\) |
| \(I_{18}\) ideal | \(E_0 A\cos\gamma/A_\text{image}\) | \(0.01175\,\mathrm{W/m}^2\) |
| \(I_{18}\) real | \(\times 0.675\) | \(0.007932\,\mathrm{W/m}^2\) |
| \(I_{55}\) ideal | \(E_0 A\cos\gamma/A_\text{image}\) | \(0.1097\,\mathrm{W/m}^2\) |
| \(I_{55}\) real | \(\times 0.675\) | \(0.07406\,\mathrm{W/m}^2\) |

GEO one-liner (C2, not a campaign): \(D = 35786\,\mathrm{km}\times 0.0093 = 333\,\mathrm{km}\) (320–340 km band).

Diffraction (C2, then drop): Airy diameter \(1.22\lambda d/D_\text{ap}\) at \(\lambda=550\,\mathrm{nm}\), \(D_\text{ap}=10\,\mathrm{m}\), \(d=625\,\mathrm{km}\) is \(0.042\,\mathrm{m}\). Solar \(D/\)Airy \(\sim 1.4\times 10^5 > 10^4\). Not in the kernel.
