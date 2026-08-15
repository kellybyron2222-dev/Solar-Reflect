# Observations log

What we saw on the drawings. Not a kernel change, not a campaign result, not a product claim.

Newest entry at the bottom. Snapshot is terminator-nadir, \(h=625\,\mathrm{km}\) held, unless an entry says otherwise. Numbers from `physics.py` / `constants.yaml`.

**How to add.** Date, scene, what we saw, the number, and one line of what it is *not*.

---

## O1 — Fold is at the foil, not at the ground

**Date:** 2026-08-15  
**Scene:** S-geo-2d (flat), locked in `figures/final/`

Incoming sunlight is parallel (Sun at infinity) and horizontal at this snapshot. The foil is a backslash (`\`). The shiny face sees the Sun *and* the ground; the back faces space.

The \(45^\circ\) is the incidence angle **from the foil’s normal**. It is not \(45^\circ\) to the ground. The foil is already tilted \(45^\circ\), so the center ray turns \(90^\circ\) and hits the local tangent straight on: \(\varepsilon=90^\circ\). Local ground is the tangent; the center ray is the Earth radius.

\[
i = r = 45^\circ,\qquad \mathrm{turn}=180^\circ-2i=90^\circ,\qquad d=h
\]

**Not:** a midnight overhead lighting geometry. Not a shiny face aimed at space.

---

## O2 — The lit patch is the Sun’s disk, not a lamp spot

**Date:** 2026-08-15  
**Scene:** S-geo-2d panel 2 (flat)

The Sun is a disk of full angle \(\alpha=0.0093\,\mathrm{rad}=0.53^\circ\). The foil copies that angle. Similar triangles to the ground:

\[
D = h\alpha = 5.812\,\mathrm{km}
\]

Exact cone \(D=2h\tan(\alpha/2)=5.813\,\mathrm{km}\). Kernel stays \(D=h\alpha\).

Earth curvature under that 5.8 km patch is a sagitta of about \(0.7\,\mathrm{m}\) and a rim tilt of about \(0.03^\circ\). Do not draw a curved ground on the width panel.

**Not:** inverse-square from a point lamp. Not a patch you can zoom by tilting the foil.

---

## O3 — A curved foil does not shrink the patch or brighten the centre

**Date:** 2026-08-15  
**Scene:** S-geo-2d-curved; also S-focus

A dish focuses **one point on the Sun** to **one point on the ground**. The Sun is a disk, so the other limb is a different direction and lands a different ground point. With the image on the ground, \(f=h\), so the two limbs are still \(h\alpha\) apart.

At 625 km that is still \(D_{\min}=5.812\,\mathrm{km}\), same as flat. Collected power is still spread over that same circle, so centre brightness is the same: M55 ideal \(I=0.1097\,\mathrm{W/m^2}\) (hand sheet).

A magnifying glass looks small because \(f\) is centimetres. Here \(f\) is the distance to the ground.

If \(f<h\), the two limbs meet *above* the ground, then cross and spread. The footprint gets **bigger** and the middle gets **dimmer**.

**Not:** a city-block spotlight. Not a brightness knob. Curvature is not a \(D\) knob.

---

## O4 — Optimal curvature at fixed range

**Date:** 2026-08-15  
**Scene:** S-geo-2d-curved  
**Held:** \(h=625\,\mathrm{km}\). Sun at infinity.

Put the solar image on the ground:

\[
f_\mathrm{opt}(h)=h,\qquad R_\mathrm{opt}(h)=2f_\mathrm{opt}=2h
\]

At this snapshot: \(f=625\,\mathrm{km}\), \(R=1250\,\mathrm{km}\).

Sag of an aperture of side \(A\) (sphere; parabola is the same paraxially):

\[
\mathrm{sag}=R-\sqrt{R^2-(A/2)^2}\approx\frac{A^2}{8R}
\]

M55 (\(A=55\,\mathrm{m}\)): \(\mathrm{sag}=0.30\,\mathrm{mm}\). The dish is almost flat. Drawings enlarge the curve so you can see it.

**Not:** a flyable 55 m architecture. M55 is a scale marker. Real sag this small is a figure note, not a manufacturing spec.

---

## O5 — What the curve *does* change: the rim, not the middle

**Date:** 2026-08-15  
**Scene:** S-geo-2d-curved

Flat foil: each Sun-point is smeared into a copy of the aperture, width \(A\). The patch is a soft-edged disk. Along a 1D cut, brightness is a trapezoid: full in the middle, linear ramps of width \(A\) at each side.

At the geometric rim (\(r=D/2\)), that ramp is half finished:

\[
I_\mathrm{rim,flat}=\tfrac12 I_\mathrm{centre}
\]

Focused at \(f=h\): each Sun-point is a sharp point. The rim is a step. Just inside the rim:

\[
I_\mathrm{rim,curve}=I_\mathrm{centre}
\]

Rim gain (1D cut, \(A\ll D\)):

\[
G_\mathrm{rim}=\frac{I_\mathrm{rim,curve}}{I_\mathrm{rim,flat}}=2
\]

The zone that changes is only a strip of width \(\sim A\) around the rim. At M55: \(A/D=55/5812=0.95\%\). Centre \(I\) is unchanged. Width \(D\) is unchanged.

M55 ideal, 625 km: \(I_\mathrm{centre}=0.1097\,\mathrm{W/m^2}\). Then \(I_\mathrm{rim,flat}=0.0549\,\mathrm{W/m^2}\), \(I_\mathrm{rim,curve}=0.1097\,\mathrm{W/m^2}\).

**Not:** a factor-of-two on the whole patch. Not a kernel change to `irradiance`. 2D circular smear is the same order when \(A\ll D\) (the limb looks locally straight).

---

## O6 — Patch width \(D\) is set by reflector height

**Date:** 2026-08-15  
**Scene:** S-geo-2d, S-spot-h, S-geo-2d-curved  
**Accurate:** yes, at this snapshot.

The Sun’s angular width \(\alpha\) is a property of the Sun, not of the foil. At nadir the range is the altitude, so

\[
D=h\alpha
\]

Raise the reflector, the lit patch grows in proportion. Lower it, the patch shrinks. Flat or curved does not matter: both give \(D_{\min}=h\alpha\).

On the v1 grid:

| \(h\) | \(D=h\alpha\) |
|---|---|
| 400 km | 3.72 km |
| 625 km | 5.812 km |
| 1000 km | 9.30 km |
| 2000 km | 18.6 km |
| GEO \(\approx 35786\) km | \(\approx 333\) km |

**Not:** set by foil area, fold angle, or curvature. Off-nadir (parked) the range is the slant \(d=h/\sin\varepsilon\), so \(D=d\alpha\) still tracks *range*, which is no longer equal to height.
