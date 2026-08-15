# Carry D → E

## What exists

| Scene | File | 625 km check |
|---|---|---|
| S-geo-2d | `figures/final/s-geo-2d.svg` (locked) | \(D=5.812\,\mathrm{km}\) |
| S-geo-2d-curved | `figures/working/s-geo-2d-curved.svg` | same \(D_{\min}\); \(f=h\), \(R=2f\) |
| S-spot-h | `figures/working/s-spot-h.svg` | \(D=5.812\,\mathrm{km}\) (rel \(0.0086\%\)) |
| S-focus | `figures/working/s-focus.svg` | same \(D_{\min}\) |

Scripts call `solar_image`. Stamp: terminator-nadir, \(\gamma=45^\circ\), \(\varepsilon=90^\circ\), \(D=d\alpha\), constants hash.

## E may start

- **E1** now — \(D(h)\), \(A_\text{image}(h)\). Use S-geo-2d, S-spot-h, S-focus. Do not treat \(D\) as a design knob.
- **E2–E5** after each prior mini look-back. Build S-I-A in E2, S-A-req in E3, S-dwell in E4.

## E must not treat as trusted from D

- \(T_\text{useful}\) — still only weakly tested (C). S-dwell is not drawn.
- \(I(A,h)\) curves — not drawn; use the kernel + C hand sheet until E2.
- Application classes / \(I^*\) — off until E5.

## Must not reopen without returning to D (or C)

- 625 km \(D=5.812\,\mathrm{km}\).
- No Airy rings, no lamp \(1/r^2\), no midnight caption, no 3D as a deliverable.
