# Formulas log

Formulas we may want later. Not a kernel change. Kernel remains `spec.md` / `physics.py`.

Two different angles live in this problem. Mixing them is the usual mistake.

| Symbol | What it is | What it is not |
|---|---|---|
| \(\alpha\) | How wide the Sun looks (full disk, \(0.0093\,\mathrm{rad}\)) | The tilt of the foil |
| \(i=r\) | Incidence and reflection **from the foil’s normal** | \(45^\circ\) to the ground |
| \(\gamma\) | Collector incidence at this snapshot (\(45^\circ\)) | Ground solar zenith |
| \(\varepsilon\) | How the center ray meets the local tangent (\(90^\circ\) nadir) | A knob on \(D\) |
| \(h\) | Orbital altitude | Orbit radius \(a=R_E+h\) |
| \(d\) | Distance along the reflected center ray to the ground | \(d=h\) only at nadir |
| \(D\) | Width of the lit patch (solar image) | A design target you zoom with curvature |

**How to add.** Name, what it computes, the equation, a plain line, a 625 km number if we have one, and what it does not do.

---

## F1 — Law of reflection: aim the patch center

Law of reflection at the shiny face:

\[
i = r
\]

**Plain:** the incoming ray and the outgoing ray make the same angle with the normal.

Turn of the center ray:

\[
\mathrm{turn}=180^\circ-2i
\]

At this snapshot \(i=45^\circ\) from the normal, so the turn is \(90^\circ\): incoming is parallel to the local ground, outgoing is perpendicular to it (\(\varepsilon=90^\circ\)).

The foil’s own tilt is already \(45^\circ\) to the ground. That is why “\(45^\circ\) at the foil” is not “\(45^\circ\) at the ground.”

**Does not:** set the width \(D\). It only aims the *center* of the patch.

---

## F2 — Solar-image width: \(D=h\alpha\) (flat foil)

The Sun is a disk. Two limbs differ by \(\alpha\). A flat foil copies that angle. From height \(h\), with the center ray straight down:

\[
d=h,\qquad D=h\alpha
\]

**Plain:** patch width = height × how wide the Sun looks.

Exact cone (same picture, no small-angle step):

\[
D=2h\tan(\alpha/2)
\]

At \(h=625\,\mathrm{km}\), \(\alpha=0.0093\,\mathrm{rad}\): \(D=5.812\,\mathrm{km}\) (kernel) vs \(5.813\,\mathrm{km}\) (exact). Kernel stays \(D=h\alpha\).

If the center ray were not nadir, replace \(h\) by the slant range \(d=h/\sin\varepsilon\). That case is parked in v1. The fold angles \(i,r\) still do not appear in \(D\).

**Does not:** depend on how big the foil is, while \(A\ll D\). Does not depend on \(i=r\).

---

## F3 — Solar-image width: \(D_{\min}=f\alpha\) (curved foil)

A dish focuses one Sun-point to one ground-point. The disk still has two limbs, still \(\alpha\) apart. At the focal plane the image width is

\[
D_{\min}=f\alpha
\]

**Plain:** the picture of the Sun is still “focal length × how wide the Sun looks.”

Put that picture *on the ground* and the ground is a distance \(h\) along the reflected center ray, so \(f=h\) and

\[
D_{\min}=h\alpha
\]

Same number as the flat foil. Same 5.812 km at 625 km.

If \(f\neq h\), the image is sharp somewhere else. On the ground you get extra smear from the foil’s own size \(A\):

\[
D\approx h\alpha+A\bigl|1-h/f\bigr|
\]

**Does not:** let you choose a curve that makes \(D\) smaller than \(h\alpha\) on the ground. Shorter \(f\) makes a smaller image *above* the ground, then a larger footprint on the ground.

---

## F4 — Optimal curvature: \(f=h\), \(R=2h\)

Wanted: a sharp “sun shadow” (lit patch) on the ground at altitude \(h\).

Sun at infinity (object distance \(s=\infty\)). Mirror equation:

\[
\frac{1}{f}=\frac{1}{s}+\frac{1}{s'}\quad\Rightarrow\quad f=s'
\]

The image distance \(s'\) is the path along the reflected center ray. At this snapshot that path is \(h\):

\[
f_\mathrm{opt}(h)=h
\]

Sphere or parabola, paraxial:

\[
R_\mathrm{opt}(h)=2f_\mathrm{opt}=2h
\]

Sag of an aperture of side \(A\):

\[
\mathrm{sag}=R-\sqrt{R^2-(A/2)^2}\approx\frac{A^2}{8R}=\frac{A^2}{16h}
\]

**Held \(h=625\,\mathrm{km}\):** \(f=625\,\mathrm{km}\), \(R=1250\,\mathrm{km}\). M55 (\(A=55\,\mathrm{m}\)): \(\mathrm{sag}=0.30\,\mathrm{mm}\).

The sunlight and reflection *angles* (\(i=r\)) aim the center. They do not enter \(f_\mathrm{opt}\) at nadir, because the image distance is already \(h\). If we later open a slanted shot, \(f_\mathrm{opt}=d=h/\sin\varepsilon\), and \(D=d\alpha\) grows with the slant. Still no extra shrink from bending harder.

**The interesting constraint.** You cannot pick \(h\), \(\alpha\), *and* a smaller \(D\), then solve for a curve that “focuses the shadow across that \(D\).” Those four quantities are not independent:

\[
D=h\alpha\qquad\text{and}\qquad f_\mathrm{opt}=h\qquad\text{so}\qquad f_\mathrm{opt}=\frac{D}{\alpha}
\]

If you want a given \(D\), you need a given height \(h=D/\alpha\). The optimal dish at that height is \(R=2D/\alpha\). Curvature makes the rim sharp. It does not choose \(D\).

**Does not:** a brightness knob. Centre \(I\) is still collected power over \(\pi(D/2)^2\). Rim-only gain is F5 (Rim brightness gain).

---

## F5 — Rim brightness gain: \(G_{\mathrm{rim}}=2\)

Along a 1D cut, a flat foil smears each Sun-point by the aperture \(A\). Brightness is a trapezoid: full in the middle, ramps of width \(A\) at the sides. At the geometric rim \(r=D/2\):

\[
I_\mathrm{rim,flat}=\tfrac12 I_\mathrm{centre},\qquad I_\mathrm{rim,curve}=I_\mathrm{centre}\quad(f=h)
\]

\[
G_\mathrm{rim}=\frac{I_\mathrm{rim,curve}}{I_\mathrm{rim,flat}}=2
\]

M55 ideal, 625 km: \(I_\mathrm{centre}=0.1097\,\mathrm{W/m^2}\). Rim \(0.0549\to 0.1097\,\mathrm{W/m^2}\). The strip that changes is \(\sim A=55\,\mathrm{m}\) on \(D=5.812\,\mathrm{km}\) (\(A/D=0.95\%\)).

**Does not:** double the whole patch. Does not change `irradiance` in the kernel.
