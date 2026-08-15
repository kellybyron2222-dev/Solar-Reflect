# Carry C → D

## Conclusions (what we actually found)

- pytest: 14 passed. Hand sheet `tests/hand_625.md` is the authority; code matches to ~0.01% (gate 1%).
- **Trusted:** \(D=h\alpha\); \(A_\text{image}\); terminator-nadir \(I\) at 625 km for M18 and M55, \(\eta=1\) and \(0.675\).
  - \(D(625\,\mathrm{km})=5.812\,\mathrm{km}\)
  - \(I_{55}\) ideal \(=0.1097\,\mathrm{W/m}^2\); real \(=0.07406\,\mathrm{W/m}^2\)
  - \(I_{18}\) ideal \(=0.01175\,\mathrm{W/m}^2\); real \(=0.007932\,\mathrm{W/m}^2\)
- **GEO:** \(D\approx 333\,\mathrm{km}\) (band 320–340). Not a plot axis.
- **Diffraction discarded:** Airy/solar \(D > 10^4\) at the C2 case. Do not draw Airy rings.
- **Weak:** \(T_\text{useful}\) (horizon identity + ordering + 400 km period 90–95 min only). Not a D-axis number.
- Energy identity holds: \(I\times A_\text{image}=E_0\eta A\cos\gamma\) at the snapshot. \(I\propto 1/h^2\) is image-area, not a lamp.

## Keep in D

- S-geo-2d and S-spot-h **before E1** (D gate).
- Stamp: terminator-nadir, \(\gamma=45^\circ\) collector incidence, ideal/realistic, equation.
- Spot-check 625 km \(D\) on those two scenes against the hand sheet.

## Cut or defer in D

- S-dwell is **not** a D gate (wait E4; stamp “formula as in spec”).
- S-I-A application horizontals **off** until E5.
- S-A-req after E2.
- 3D, GUI, extra scenes, beams, spacecraft mesh, “night lighting,” lamp \(1/r^2\) captions.

## Watch

- Draw \(D=h\alpha\), not a searchlight cone.
- Do not caption terminator-nadir as midnight / dark-sky lighting.
- Do not treat missing clouds or diffraction as a visual finding.
- M1km vs \(A_\text{image}\) is an E2 flag, not a C fail and not a D scene.

## Must not reopen without returning to C (or B)

- Trusted 625 km \(D\) and \(I\) numbers.
- Diffraction out of the kernel.
- No \(I^*\) in drawings until E5.
