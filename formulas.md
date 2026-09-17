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
| \(A\) | Collecting area of the foil | The ground patch area \(A_\text{image}\) |
| \(P\) | Watts the foil catches | Brightness on the ground |
| \(I\) | Centre / filled-image irradiance (W/m²) | lux; a lamp \(1/r^2\) |

**How to add.** Name, what it computes, the equation, a plain line, a 625 km number if we have one, and what it does not do.

**Catalog**

| ID | What it computes |
|---|---|
| F1 | Law of reflection: aim the patch center. \(i=r\), turn \(=180^\circ-2i\) |
| F2 | Flat solar-image width. \(D=h\alpha\); small means \(w\le 0.01\,h\alpha\) |
| F3 | Curved solar-image floor. \(D_{\min}=f\alpha\); on the ground \(f=h\) |
| F4 | Optimal curvature. \(f=h\), \(R=2h\), sag \(A^2/(16h)\) |
| F5 | Rim brightness gain. \(G_{\mathrm{rim}}=2\) in a strip \(\sim A\) |
| F6 | \(D(f)\) extrema. \(D_{\min}=h\alpha\); hemispherical \(D_{\max}\approx 4h\); rims-touch is dark |
| F7 | Centre irradiance. Same \(I\) for flat and \(f=h\): \(I=P/A_\text{image}\). At fixed \(h\), peak \(I\propto A\) while small (F12) |
| F8 | Flat vs dish: total power and centre \(I\) identical; rim and over-bend differ |
| F9 | Required area. Invert of F7: \(A_\mathrm{req}=I^* A_\text{image}/(E_0\eta\cos\gamma)\) |
| F10 | Foil vs footprint at given \(I\): \(A/A_\text{image}=I/(E_0\eta\cos\gamma)\) |
| F11 | Watts on the foil vs watts on the ground. Ratio \(\eta\) at every \(A\); small-\(A\) formula at \(A=A_\text{image}\) gives \(\eta E_0\cos\gamma\) (not an étendue proof) |
| F12 | Circular flat foil past “small”: \(D=h\alpha+w\), \(A_\text{lit}=(\sqrt{A}+\sqrt{A_\text{image}})^2\); peak vs mean \(I\) |
| F13 | Pass window. \(T=2\pi\sqrt{a^3/\mu}\), \(a=R_E+h\); \(T_\text{useful}=T\,\theta(\varepsilon_\min)/\pi\) |
| F14 | Fluence upper bound. \(F_\mathrm{pass}=I_\text{peak}T_\text{useful}\); \(N_\text{train}\approx T^*/T_\text{useful}\) |
| F15 | Civil-night value snapshot. Terminator-sunlit sat, site \(\theta=6^\circ\); \(I=E_0\eta A\cos i/A_\text{ellipse}\) |
| F16 | Fleet for one site: \(N=N_I N_T\), \(N_I=I^*/I_\text{one}\), \(N_T=T^*/T_\text{useful}\) |
| F17 | Optimal \(N(A,h)=(T^*/T_u)\max(1,I^*/I)\). Fixed \(A\): min \(N\) at max \(I T_u\) (\(\sim 1420\,\mathrm{km}\)) |
| F18 | Train vs square: parked \((I^*,T^*)\) needs \(N\ge N_I N_T\). Equal fluence is not enough. Tight cluster \(\equiv\) larger \(A\) |

Kernel shutter \(T\) is F13 (`pass_window`). lux is derived (framing); not a kernel output; not an F-number until E5 needs a conversion.

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

**Does not:** depend on how big the foil is, **while the foil is small compared with that blur**. Does not depend on \(i=r\).

**Limit of small.** The kernel drops the foil’s own width. The flat-sheet width is \(D\approx h\alpha+w\) with \(w\) the side (F6). Relative error in \(D\) is \(w/(h\alpha)\). Take **small** to mean that error \(\le 1\%\):

\[
w \le 0.01\,h\alpha
\]

At 625 km: \(w\le 58\,\mathrm{m}\). M55 (\(55\,\mathrm{m}\)) sits on that line (\(0.95\%\)). M18 is \(0.31\%\). M1km is \(17\%\) — not small. At 400 km the 1% width is \(37\,\mathrm{m}\); M1km is \(27\%\) of \(D\) and \(A/A_\text{image}=0.092\), which is the E2 approximation flag.

That 1% cut is a working definition, not a `min()` in `irradiance()`. S-a-fill’s \(0.1 / 1 / 10\) panels are all past it.

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

**Does not:** let you choose a curve that makes \(D\) smaller than \(h\alpha\) on the ground. Shorter \(f\) makes a smaller image *above* the ground, then a larger footprint on the ground. Extrema of this formula are F6.

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

---

## F6 — Ground-patch width vs curvature: \(D_{\min}\) and \(D_{\max}\)

Geometric lit width along a 1D cut. Sun at infinity, aperture side \(A\), focal length \(f\). Sphere or parabola, paraxial: \(R=2f\).

\[
D(h,f,A)=h\alpha+A\bigl|1-h/f\bigr|
\]

Same thing in radius of curvature, or in the spherical-cap half-angle \(\psi\) (vertex to rim, from the sphere’s centre), where \(\sin\psi=A/(2R)=A/(4f)\):

\[
D(h,R,A)=h\alpha+A\bigl|1-2h/R\bigr|
\]

\[
D(h,\psi,A)=h\alpha+A\left|1-\frac{4h\sin\psi}{A}\right|
\]

**Minimum.** \(D(f)\) is smallest when the image sits on the ground, \(f=h\) (\(R=2h\), \(\sin\psi=A/(4h)\)):

\[
D_{\min}(h)=h\alpha
\]

That extra term is then zero. You cannot beat \(h\alpha\) on the ground by bending more or less. At \(h=625\,\mathrm{km}\): \(D_{\min}=5.812\,\mathrm{km}\). Flatten (\(f\to\infty\)): \(D\to h\alpha+A\). M55: \(5.867\,\mathrm{km}\). Kernel still quotes \(D=h\alpha\) because \(A\ll D\).

**Maximum.** The paraxial line \(D=h\alpha+A|1-h/f|\) at **fixed opening** \(A\) goes to infinity as \(f\to 0\). That limit is unphysical: a sphere of radius \(R=2f\to 0\) cannot keep a finite opening \(A\).

Hold the **foil length** \(L\) fixed instead (the sheet you are curling). Then the opening is the chord \(A=(L/\psi)\sin\psi\), and \(f=L/(4\psi)\). After \(f=h\), for \(h\gg L\),

\[
D\approx h\alpha+4h\sin\psi
\]

That **does** have a peak, at the hemisphere \(\psi=90^\circ\):

\[
D_{\max}=h\alpha+4h-A\qquad(\psi=90^\circ,\; A=2L/\pi)
\]

M55-length foil at 625 km: \(D_{\max}\approx 2506\,\mathrm{km}\) (\(\approx 4h\)). Not a useful optic, and not drawn to scale.

**When the two ends touch.** Keep curling past the hemisphere. The rims approach; \(A\to 0\); \(\psi\to 180^\circ\) (2D: a closed circle, \(L=2\pi R\)). The shiny face is now the **inside** of the shell; the back faces space. Sunlight hits the back. Nothing useful reflects to the ground. Collected power is zero. There is **no** lit patch — \(D\) is undefined, not infinite, not \(\pi R\).

On the way there, \(D\approx h\alpha+4h\sin\psi\) **falls** from the hemispherical peak back toward \(h\alpha\) as the opening pinches off (a vanishingly dim pinhole of the Sun), then the cavity closes and goes dark.

**Not \(\pi\) in \(D\), not a ground point.** \(\pi\) relates foil length to radius when the circle closes (\(L=2\pi R\)), and it is in the image *area* \(\pi(D/2)^2\). It is not a factor in \(D_{\max}\). The singularity is the **focus** in the air; past that focus the cone opens. The ground patch never pinches to a point.

**Held illustration** (S-focus panel 3, labeled \(D_{\max}\) under the orange bar, M55): \(f=10\,\mathrm{km}\), \(R=20\,\mathrm{km}\), \(\psi\approx 0.079^\circ\).

\[
D_{\max}^\mathrm{(illust)}=h\alpha+A\bigl(h/f-1\bigr)=9.195\,\mathrm{km}
\]

That drawn bar is a readable over-bend, not the 2506 km hemisphere and not the closed shell.

**Does not:** enter `solar_image` / `irradiance`. Kernel stays \(D=h\alpha=D_{\min}\). Does not make a smaller ground patch than \(h\alpha\). Does not put \(\pi\) into \(D\). The \(f\to 0\) infinity is not a physical state.

---

## F7 — Centre irradiance: same formula for flat and \(f=h\)

Collected power at this snapshot (same foil area \(A\), same \(\eta\), same fold):

\[
P=E_0\,\eta\,A\cos\gamma
\]

(\(\sin\varepsilon=1\) at nadir). That \(P\) does not know if the foil is flat or a dish.

The Sun’s image on the ground has area \(A_\text{image}=\pi(D/2)^2\) with \(D=h\alpha\) (F2). For a dish with the image on the ground, \(f=h\), so \(D_{\min}=h\alpha\) as well (F3). Same denominator.

Filled-image centre brightness (Canady; the kernel):

\[
I_\mathrm{centre}=\frac{P}{A_\text{image}}=\frac{E_0\,\eta\,A\cos\gamma}{\pi(h\alpha/2)^2}
\]

**Plain:** watts the foil catches, spread over the Sun’s picture on the ground.

**Flat** (\(f\to\infty\), \(A\ll D\)) and **dish** (\(f=h\)):

\[
I_\mathrm{centre,flat}=I_\mathrm{centre,dish}=I_\mathrm{centre}
\]

M55 ideal, 625 km: \(P=2.911\,\mathrm{MW}\), \(A_\text{image}=2.653\times 10^7\,\mathrm{m}^2\), \(I_\mathrm{centre}=0.1097\,\mathrm{W/m^2}\) (C3 / E2). Realistic: \(\times 0.675\).

**Linear in \(A\) at fixed \(h\).** \(A_\text{image}\) does not depend on foil size (while \(A\ll A_\text{image}\)), so

\[
\frac{I_2}{I_1}=\frac{A_2}{A_1}
\]

S-i-two (flat foils, 625 km): \(I_{55}/I_{18}=A_{55}/A_{18}=9.34\). M18: \(0.01175\,\mathrm{W/m^2}\). That is not a log law. S-I-A is log–log only so the markers fit; a slope-1 line there *is* \(I\propto A\).

**Does not:** depend on \(R\) or sag when \(f=h\). Does not double if you curve the foil. Does not mean \(I\) grows as \(\log A\). lux is not this formula.

---

## F8 — Flat vs dish: where the energy *does* differ

Total power on the ground is \(P\) (F7) either way: reflection does not create watts. Centre \(I\) is the same when \(f=h\) and \(A\ll D\). The difference is *where* those watts sit.

**Rim (F5).** Flat: each Sun-point is smeared by \(A\), so a 1D cut is a trapezoid and \(I_\mathrm{rim,flat}=I_\mathrm{centre}/2\). Dish \(f=h\): step edge, \(I_\mathrm{rim,dish}=I_\mathrm{centre}\). Gain \(G_\mathrm{rim}=2\), only in a strip of width \(\sim A\). At M55 / 625 km that strip is \(A/D=0.95\%\) of the diameter. Order of power in the soft edge: \(\sim 2A/D\approx 1.9\%\) of \(P\). Not a factor-of-two on the patch.

**Over-bent** (\(f<h\)). Same \(P\), larger footprint \(D(f)=h\alpha+A|1-h/f|\) (F6). If that power is spread over \(\pi(D(f)/2)^2\):

\[
I_\mathrm{centre}(f)\approx\frac{P}{\pi\bigl(D(f)/2\bigr)^2}=I_\mathrm{centre}\left(\frac{D_{\min}}{D(f)}\right)^2
\]

Held illustration, M55, \(f=10\,\mathrm{km}\): \(D=9.195\,\mathrm{km}\), area \(\times 2.50\), \(I_\mathrm{centre}\approx 0.0438\,\mathrm{W/m^2}\) (about \(40\%\) of \(0.1097\)). The middle gets dimmer. This is not in the kernel; kernel \(I\) stays \(P/A_\text{image}\) at \(D_{\min}\).

**Ratio at \(f=h\):**

\[
\frac{I_\mathrm{centre,dish}}{I_\mathrm{centre,flat}}=1,\qquad \frac{P_\mathrm{dish}}{P_\mathrm{flat}}=1
\]

**Does not:** a brightness knob at the useful curve. Does not change `irradiance`. Does not put the over-bent drop into E2’s table.

---

## F9 — Required collecting area: invert of F7

Same snapshot, same filled image. Solve F7 for \(A\) at a parked target \(I^*\):

\[
A_\mathrm{req}(I^*,h,\eta)=\frac{I^*\,A_\text{image}(h)}{E_0\eta\cos\gamma}=\frac{I^*}{I(A=1)}
\]

**Plain:** how large a foil you need so the sun-shadow’s centre hits \(I^*\).

At fixed \(I^*\), \(A_\mathrm{req}\propto h^2\). The fill fraction does not depend on height:

\[
\frac{A_\mathrm{req}}{A_\text{image}}=\frac{I^*}{E_0\eta\cos\gamma}
\]

Linear even if \(I^*>E_0\eta\cos\gamma\) (then \(A_\mathrm{req}>A_\text{image}\)). No clip in the kernel.

Check: \(I^*=0.1097\,\mathrm{W/m^2}\) at 625 km, \(\eta=1\) returns \(A=3025\,\mathrm{m}^2\) (M55). C-day \(I^*=1000\): fill \(1.039\) even at \(\eta=1\).

**Does not:** buy hours (\(T^*\) is E4). Does not add a new \(I^*\). Does not switch formulas when \(A\) approaches \(A_\text{image}\).

---

## F10 — Foil size vs footprint size at a given \(I\)

Collecting area \(A\) (mirror/foil in orbit). Footprint \(A_\text{image}=\pi(D/2)^2\) (sun-shadow on the ground). From F7, at a chosen brightness \(I\):

\[
\frac{A}{A_\text{image}}=\frac{I}{E_0\eta\cos\gamma}
\]

**Plain:** to make the patch as bright as \(I\), the foil must cover that fraction of the solar image. The ratio does **not** depend on height. Both \(A\) and \(A_\text{image}\) grow as \(h^2\); their quotient is fixed by \(I\) versus how bright sunlight is on the collector.

Call the collector-face irradiance \(E_c=E_0\cos\gamma\) (\(\approx 962\,\mathrm{W/m^2}\) at this snapshot, \(\eta=1\)). Then

\[
\frac{A}{A_\text{image}}=\frac{I}{\eta E_c}
\]

**Daylight-class \(I=1000\,\mathrm{W/m^2}\), \(\eta=1\):** \(A/A_\text{image}=1000/962=1.039\). The foil is **about the same area as the footprint**, 3.9% larger. At 625 km: footprint \(26.53\,\mathrm{km}^2\), foil \(27.57\,\mathrm{km}^2\). At 400 km both shrink; at 2000 km both grow; the **1.039 stays**. Realistic \(\eta=0.675\): ratio \(1.54\).

M55 at 625 km (\(I=0.1097\,\mathrm{W/m^2}\)): \(A/A_\text{image}=3025/(2.653\times 10^7)=1.14\times 10^{-4}\). Tiny foil, huge patch, dim \(I\).

Drawn: `figures/working/s-a-fill.svg` — circular foils sized \(0.1\), \(1\), \(10\) of the solar image. Lit patch is F12. Kernel still \(D=h\alpha\).

**Does not:** depend on curvature when \(f=h\). Does not shrink the footprint if you enlarge the foil. Does not include \(T\).

---

## F11 — Watts in space vs watts on the ground

Sunlight intercepted by the foil (before optical factor):

\[
P_\mathrm{in}=E_0 A\cos\gamma
\]

Power that reaches the ground (after \(\eta=\rho\tau\)):

\[
P_\mathrm{ground}=\eta P_\mathrm{in}=E_0\eta A\cos\gamma
\]

That same power is the integral of brightness over the sun-shadow:

\[
P_\mathrm{ground}=I\,A_\text{image}
\]

Those two expressions are the same identity (F7). **Watts are conserved** through the bounce, except for the factor \(\eta\) (reflection and the one clear-sky \(\tau\)). They are not lost to inverse-square from a lamp. They are **spread**: the same \(P_\mathrm{ground}\) over \(A_\text{image}\) instead of over \(A\).

Dilution of brightness (W/m²), not of watts:

\[
\frac{I}{E_0\cos\gamma}=\eta\frac{A}{A_\text{image}}
\]

**Plain:** the ground is dimmer than the sunlight on the foil by (optical efficiency) × (foil area / patch area). For daylight \(I=1000\) you need \(A\) slightly *larger* than \(A_\text{image}\) because \(1000>E_0\cos\gamma\). For M55, \(I/(E_0\cos\gamma)=0.1097/962\approx 1.14\times 10^{-4}\), the same number as \(A/A_\text{image}\).

Held, M55, 625 km, ideal: \(P_\mathrm{in}=P_\mathrm{ground}=2.911\,\mathrm{MW}\) into \(26.53\,\mathrm{km}^2\).

**Ceiling.** The *watts* ratio is already \(\eta\) at every size:

\[
\frac{P_\mathrm{ground}}{P_\mathrm{in}}=\eta
\]

Enlarging the foil does **not** improve that. You catch more watts and you deliver more watts; the fraction kept is still \(\eta\).

The *brightness* ratio \(I/(E_0\cos\gamma)\) does rise with \(A\), but it does not go to 1 at infinite \(A\). The filled-image picture stops being the right story when the foil is as large as the sun-shadow:

\[
A\to A_\text{image}\qquad\Rightarrow\qquad I\to \eta E_0\cos\gamma
\]

At this snapshot \(\eta=1\): the **small-\(A\) formula** at \(A=A_\text{image}\) gives \(I\to 962\,\mathrm{W/m^2}\), not AM0 \(1361\) (the fold still has \(\cos\gamma=1/\sqrt{2}\)). Realistic: \(650\,\mathrm{W/m^2}\). That 962 is **not** an étendue / radiance ceiling — a ground point that sees a full solar disk would sit near \(\eta E_0\), and C-day \(I^*=1000\) sits between 962 and 1361. Do not read “unreachable by étendue.” An infinitely large foil is not a physical state in this model; \(A\gg A_\text{image}\) is outside the small-collector assumption. The kernel still inverts linearly (no clip); that is bookkeeping, not a bigger-than-the-Sun spotlight. The circular-foil geometry that replaces a fixed 5.8 km hole is F12.

**Does not:** a \(1/h^2\) lamp. \(I\propto 1/h^2\) only because \(A_\text{image}\propto h^2\). Does not put extra loss in the kernel beyond \(\eta\). Does not count umbra or clouds. Does not make \(P_\mathrm{ground}/P_\mathrm{in}\) depend on \(A\). Does not add a \(\min()\) clip in `irradiance()`.

---

## F12 — Circular flat foil: lit patch and two irradiances

Review of the large-foil illustration. Not a kernel change. `solar_image` / `irradiance` stay \(D=h\alpha\) and \(I=P/A_\text{image}\).

A **circular** flat foil of area \(A\) has diameter

\[
w=2\sqrt{A/\pi}
\]

The Sun is a disk. Each point on the foil copies that disk onto the ground (diameter \(h\alpha\)). The outer lit region is the Minkowski sum of two disks: foil plus solar blur.

\[
D_\text{lit}=h\alpha+w
\]

\[
A_\text{lit}=\pi\bigl((h\alpha+w)/2\bigr)^2=\bigl(\sqrt{A}+\sqrt{A_\text{image}}\bigr)^2
\]

A circular mirror makes a **circular** sun-shadow. The square on the old S-a-fill was the M18/M55 marker shape, not the optic.

Watts still scale with the foil (F11): \(P=E_0\eta A\cos\gamma=E_c A\) with \(E_c=E_0\eta\cos\gamma\).

Two different W/m²:

**Peak (centre).** From the ground, the foil subtends \(w/h\) and the Sun subtends \(\alpha\). The centre sees a partial Sun until the foil fills the disk, then only more sky.

\[
I_\text{peak}=E_c\min\bigl(1,\,A/A_\text{image}\bigr)=E_c\min\bigl(1,\,(w/h\alpha)^2\bigr)
\]

This **is** the kernel \(I=P/A_\text{image}\) while \(A\le A_\text{image}\). It is linear in \(A\) at fixed \(h\) up to the 1-sun line, then flat. S-I-A’s plotted range (\(A\le 3\times 10^6\,\mathrm{m}^2\)) never reaches \(A_\text{image}\) on the v1 grid, so those lines stay linear as peak \(I\).

**Mean over the outer disk.** The patch is not uniform: a brighter middle and a penumbra of width \(\sim h\alpha\). The area average is

\[
I_\text{mean}=P/A_\text{lit}=E_c\frac{A}{(\sqrt{A}+\sqrt{A_\text{image}})^2}
\]

This is **not** linear in \(A\). Growing \(A_\text{lit}\) offsets part of the extra watts. As \(A\to 0\), \(I_\text{mean}\to I_\text{peak}\). As \(A\to\infty\), both \(I_\text{peak}\) and \(I_\text{mean}\) go to \(E_c\) (one folded sun), and \(A_\text{lit}\sim A\).

Held, 625 km, \(\eta=1\), \(E_c=962\,\mathrm{W/m^2}\), \(A_\text{image}=26.53\,\mathrm{km}^2\). Circular foils sized as \(0.1\), \(1\), \(10\) of that solar image:

| \(A/A_\text{image}\) | \(w\) | \(D_\text{lit}\) | \(A_\text{lit}\) | \(I_\text{peak}\) | \(I_\text{mean}\) | Kernel \(I\) (fixed \(D\)) |
|---|---|---|---|---|---|---|
| \(0.1\) | \(1.84\,\mathrm{km}\) | \(7.65\,\mathrm{km}\) | \(46.0\,\mathrm{km}^2\) | \(96.2\,\mathrm{W/m^2}\) | \(55.6\,\mathrm{W/m^2}\) | \(96.2\) |
| \(1\) | \(5.81\,\mathrm{km}\) | \(11.6\,\mathrm{km}\) | \(106\,\mathrm{km}^2\) | \(962\,\mathrm{W/m^2}\) | \(241\,\mathrm{W/m^2}\) | \(962\) |
| \(10\) | \(18.4\,\mathrm{km}\) | \(24.2\,\mathrm{km}\) | \(459\,\mathrm{km}^2\) | \(962\,\mathrm{W/m^2}\) | \(556\,\mathrm{W/m^2}\) | \(9624\) |

The 9624 number is the kernel with the patch held fixed. It is not a physical centre or a physical average.

**Logic that passed this review**

1. Sun-shadow scales with **height** while the foil is small (\(w\le 0.01\,h\alpha\), F2). Markers M18/M55 are there. Kernel \(D=h\alpha\) is the right \(D\).
2. Past that cut, the same law is \(D=h\alpha+w\). Height still sets the blur; the foil adds its own silhouette. Both statements in the earlier argument are this one law in two regimes.
3. Peak W/m² **does** scale linearly with \(A\) until \(A=A_\text{image}\), then it saturates. Mean W/m² does **not** stay linear: \(A_\text{lit}\) grows and offsets part of the gain.
4. Watts \(P\) always scale linearly with \(A\). The offset is in W/m², not in the watts ratio \(\eta\).
5. A circular foil → circular outer patch. No clip in `irradiance()`.

**Does not:** enter the kernel. Does not apply a square foil (that was F6’s 1D side \(A\)). Does not make a dish at \(f=h\) grow \(D\) (there \(|1-h/f|=0\)). Does not put \(I_\text{mean}\) into S-I-A as the campaign \(I\).

---

## F13 — Pass window (time only)

Circular Kepler, spherical Earth. Period uses orbit radius \(a=R_E+h\), not altitude \(h\):

\[
T=2\pi\sqrt{a^3/\mu}
\]

Earth-central angle from nadir to the elevation contour \(\varepsilon\):

\[
\theta(\varepsilon)=\arccos\bigl((R_E/a)\cos\varepsilon\bigr)-\varepsilon
\]

Full overhead (zenith-track) windows — satellite traverses \(2\theta\):

\[
T_\text{horizon}=T\,\theta(0)/\pi,\qquad T_\text{useful}=T\,\theta(\varepsilon_\min)/\pi
\]

\(\varepsilon_\min=30^\circ\) is shutter only. It does not change snapshot \(I\).

**Plain:** how long the satellite stays above the horizon, and how long it stays above \(30^\circ\), on a pass that goes straight overhead. Off-track is shorter. No umbra, no Earth rotation.

At 625 km: \(T=97.06\,\mathrm{min}\), \(T_\text{horizon}=13.16\,\mathrm{min}\), \(T_\text{useful}=4.281\,\mathrm{min}\). At 400 km, \(T=92.41\,\mathrm{min}\) (C band 90–95). At 1000 km, \(T_\text{horizon}=17.61\,\mathrm{min}\) is Çelik & McInnes (2022) \(T_\text{pass}\) (horizon-to-horizon). Their “pass” is not our \(\varepsilon>30^\circ\) useful window.

Literature “\(\sim 20\,\mathrm{min}\) at 1000 km” is that horizon number rounded (Viale/Çelik). \(T_\text{useful}=6.727\,\mathrm{min}\) is the \(30^\circ\) shutter. Horizon at 2000 km (\(28.54\,\mathrm{min}\)) would pass a \(20\,\mathrm{min}\) test; useful (\(13.25\,\mathrm{min}\)) does not.

**Does not:** buy hours with more foil area. Does not subtract eclipse. Does not put \(i\)/LTAN into the kernel. Does not use \(T=2\pi\sqrt{h^3/\mu}\). Does not equal the flash of an unsteered spot (\(D/v_\text{ground}\sim 0.5\)–\(3.5\,\mathrm{s}\) on this grid; \(T_\text{useful}\) assumes the image is held on the site).

---

## F14 — Fluence upper bound and train multiplier

Product of E2 peak brightness and E4 useful dwell:

\[
F_\mathrm{pass}=I_\text{peak}\,T_\text{useful}
\]

SI is J/m². Wh/m² \(=F/3600\). **Upper bound:** \(I\) is held at the nadir peak for the whole window; \(T_\text{useful}\) is geometric and has no umbra cut.

M55, 625 km, ideal: \(I=0.1097\,\mathrm{W/m^2}\), \(T_\text{useful}=256.9\,\mathrm{s}\), \(F=28.18\,\mathrm{J/m^2}=7.828\times 10^{-3}\,\mathrm{Wh/m^2}\).

Parked duration \(T^*\) that is not n/a, as a multiplier, not a constellation:

\[
N_\text{train}(T^*)\approx T^*/T_\text{useful}
\]

One useful pass \(\Rightarrow N=1\). \(20\,\mathrm{min}\) at 625 km \(\Rightarrow N=4.672\). \(3\,\mathrm{h}\) \(\Rightarrow N=42.04\). C-day \(T^*\) is n/a.

**Does not:** a light curve. Does not say one satellite provides 3 hours. Does not enter `physics.py` as \(N_\text{train}\). Does not mix \(T^*\) into \(A_\mathrm{req}\).

---

## F15 — Civil-night value snapshot

Satellite on the terminator (sunlit, incoming horizontal). Site a night-side Earth angle \(\theta\) equal to the solar depression. Default \(\theta=6^\circ\) (civil night). Closest approach.

\[
d=\sqrt{a^2+R_E^2-2a R_E\cos\theta},\qquad
\sin\varepsilon=(a\cos\theta-R_E)/d,\qquad
A_\text{image}=\pi(d\alpha/2)^2/\sin\varepsilon
\]

Foil incidence \(i\) from the bisector of the sun direction and the look direction. At \(\theta=0\) this is \(i=45^\circ\), \(d=h\).

\[
I=\frac{E_0\eta A\cos i}{A_\text{image}}
\]

Off-track useful time: \(T=T\,\psi_\max/\pi\) with \(\psi_\max=\arccos(\cos\theta(\varepsilon_\min)/\cos\theta)\) if \(\theta<\theta(\varepsilon_\min)\), else \(0\).

**Plain:** the valuable case is early night, not dusk overhead and not 2 a.m. The patch is an ellipse; the foil is steeper; the pass is off the terminator track.

Held, 625 km, \(\theta=6^\circ\), \(\eta=1\): \(d=937.5\,\mathrm{km}\), \(\varepsilon=38.74^\circ\), \(i=67.63^\circ\), \(D_\text{minor}=8.719\,\mathrm{km}\), \(A_\text{image}=95.41\,\mathrm{km}^2\), M55 \(I=0.01642\,\mathrm{W/m^2}\) (\(0.150\times\) nadir), \(T_\text{useful}=2.809\,\mathrm{min}\).

**Does not:** light local midnight. Does not put umbra in the kernel. Does not retune \(\tau\) for low \(\varepsilon\). Does not replace `irradiance()`.

---

## F16 — Vehicles for one dark site

To hit both parked thresholds at the civil-night snapshot:

\[
N_I=\frac{I^*}{I_\text{one}},\qquad N_T=\frac{T^*}{T_\text{useful}},\qquad N=N_I N_T
\]

If the foil is already \(A_\mathrm{req}\), \(N_I=1\) and \(N=N_T\). C-moon uses \(N_T=1\). C-day has no \(T^*\).

**Plain:** brightness is how many aim at the same patch; duration is how many follow each other. The product is one site, one night — not a planet. A square of all \(N\) is not a substitute (F18).

Held, 625 km, \(\eta=1\), civil night: C-light M18 \(N=404.8\); M55 \(N=43.36\); sized foil \(N=7.120\). C-weak M1km \(N=65.58\).

**Does not:** cover the Earth. Does not stack past one sun. Does not enter `physics.py` as a new kernel symbol.

---

## F17 — Optimal \(N\) for given \(I^*\), \(T^*\), orbit

\[
N(A,h)=\frac{T^*}{T_\text{useful}(h)}\max\!\left(1,\frac{I^*}{I(A,h)}\right)
\]

`fleet_count` in `physics.py`. \(I\) and \(T_\text{useful}\) are the civil-night functions (F15).

- \(A^*=A_\mathrm{req}\) if unconstrained; then \(N^*=T^*/T_\text{useful}\) (higher \(h\) always smaller \(N\)).
- If \(A\) is capped, maximize fluence per sat \(F=I(A,h)\,T_\text{useful}(h)\). On this snapshot that peaks near \(h=1420\,\mathrm{km}\).

**Plain:** grow the mirror until it is bright enough, then only a train remains. If you cannot grow it, pick the height where (watts × minutes) per craft is largest — about 1400–1500 km, not 625.

Held, C-light, \(\eta=1\): M18 \(N(625)=405\), \(N(1500)=196\). Sized foil: \(N(625)=7.12\), \(N(3000)\approx 1\).

**Does not:** a cost function. Does not cover the globe. Does not put GEO in the night snapshot.

---

## F18 — Train vs square for one site

Parked tests are indicators, not fluence. A site is served only if there exists a time set of duration at least \(T^*\) on which \(I(t)\ge I^*\). One resolved sun is the brightness cap (F10–F12):

\[
I\le I_\text{fill}=E_0\eta\cos i
\]

Write \(n_\parallel\) for co-aimed copies in **one orbital slot** (a tight square / matrix about the boresight) and \(n_\rightarrow\) for **sequential** slots along the same track (a train). Linear stacking while \(n_\parallel A\le A_\text{image}\):

\[
I = n_\parallel\,I_\text{one},\qquad
T_\text{on}=n_\rightarrow\,T_\text{useful}
\]

if the slots abut and do not overlap in time. Area and \(n_\parallel\) do not change \(T_\text{useful}\) (F13, O19).

**Necessity.** \(I\ge I^*\) needs \(n_\parallel\ge N_I=\max(1,I^*/I_\text{one})\) at those instants (impossible if \(I^*>I_\text{fill}\)). Duration \(\ge T^*\) needs \(n_\rightarrow\ge N_T=T^*/T_\text{useful}\). Vehicles multiply:

\[
N\ge n_\parallel\,n_\rightarrow\ge N_I N_T
\]

**Sufficiency (linear, under fill).** \(N_T\) abutting clusters of \(N_I\) co-aimed copies hit both tests. That is F16. A co-aimed cluster of \(k\) is the same map as one foil of area \(kA\) (F7, F17): grow to \(A_\mathrm{req}\), then only the train remains.

**Equal fluence is not the test.** All \(N=N_I N_T\) in one slot:

\[
I_\square=\min(N I_\text{one},\,I_\text{fill}),\qquad T_\square=T_\text{useful},\qquad
F_\square=I_\square T_\text{useful}
\]

In the linear regime \(F_\square=I^*T^*=F^*\), but \(T_\square<T^*\) whenever \(N_T>1\), so the square **fails \(T^*\)**. A single-file train of the same \(N\) has \(I=I_\text{one}\) for duration \(N T_\text{useful}\); it **fails \(I^*\)** whenever \(N_I>1\).

**Sparse square is worse for one site.** If the matrix is opened until ground patches do not overlap, \(I\) at the intended point stays \(I_\text{one}\) and the extra foils light neighboring ground. The night image is already an ellipse of size \(D_\text{minor}=d\alpha\) (F15). Offsets of order \(D\) smear, they do not brighten.

Along-track spacing that *abuts* windows, not a visual pack:

\[
\Delta\psi=2\pi\,\frac{T_\text{useful}}{T},\qquad \Delta s=a\,\Delta\psi
\]

**Plain:** watts are copies on the same patch (or a bigger sheet). Minutes are replacements along the track. A square around the focal point is the watts job; it cannot buy the minutes job. Matching \(I\times t\) in joules does not pass a parked \((I^*,T^*)\).

Held, civil night, 625 km, \(\eta=1\): \(T_\text{useful}=2.809\,\mathrm{min}\), \(I_\text{fill}=518\,\mathrm{W/m^2}\), \(\Delta s=1272\,\mathrm{km}\). C-light M18: \(N_I=56.85\), \(N_T=7.12\), \(N=405\). Square of 405: \(I=0.712\,\mathrm{W/m^2}\) for \(2.809\,\mathrm{min}\), \(F=120\,\mathrm{J/m^2}=F^*\), fails 20 min. Filled-sun pulse \(F_\text{fill}=87.3\,\mathrm{kJ/m^2}\) vs C-energy \(F^*=2.16\,\mathrm{MJ/m^2}\) — a square cannot substitute 64 passes.

**Does not:** enter `physics.py`. Does not stack past one sun. Does not schedule a 2D constellation or prove station-keeping. Cross-track of a square leaves the terminator; that is geometry, not a kernel run. Does not cover the Earth.
