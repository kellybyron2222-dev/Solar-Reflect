# Copilot briefing — Solar Reflect report

Use this file as grounding when rewriting `report.docx`.
The report is a **physics thought experiment**: can an orbital **specular mirror** deliver useful sunlight to a **dark site**?

Reader: technically literate, not a specialist. Voice: conversational, short sentences, no lab jargon in the opening. Prefer **mirror** / **sheet**. Do not lead with **foil**. Do not say **binds**, **vehicles**, **readout**.

---

## How to help

- Improve language, grammar, flow, and argument. Do **not** invent numbers, thresholds, figures, or physics.
- User notes and suggested wording are a **guide**. If they clash with this briefing, **this briefing wins**.
- Do not turn the piece into a company review, a product pitch, or a launch-cost study.
- Do not conclude from things we did not model (clouds as peak I, light-curve integral, umbra along the pass, pointing error, diffraction, true midnight / polar summer, cost).
- Civil night is the **score**. Terminator-nadir (looking straight down at dusk) is the **brighter envelope**, not the dark-city case. Do not mix them.

---

## The question (frozen)

A mirror of some size, at some height, with an optical factor for reflection and air. How bright is the ground patch? How wide? How long does it last at a site that is already dark (Sun 6° below the horizon)? Then: is that light useful compared with moonlight, street lighting, and sunlight for electricity? Those comparisons **judge scale**. They do **not** choose the physics.

---

## Master metaphor

**Sun projector, not a spotlight.** The mirror copies the Sun’s disk onto the ground. It does not make a tight lamp beam. Curving the mirror does not shrink that disk. Diffraction is negligible (Airy disk ~4 cm vs a ~6 km solar image at 625 km) and is **not** in the model.

**55-metre square** means 55 m on a side (area 3025 m²), building-sized. It is **not** 55 m².

---

## Two facts that cannot be engineered away

1. The Sun is a disk about half a degree wide (α = 0.0093 rad). Patch width at nadir: D = h α. At 625 km, D = 5.812 km, image area 26.53 km².
2. Low Earth orbit does not hover. Period at 625 km is 97.06 min. Useful window (elevation ≥ 30°) is 4.281 min overhead at dusk; 2.809 min at the civil-night snapshot. Unsteered flash across the site is 0.85 s. Area does not buy hours.

Brightness and duration are **two currencies**. A larger mirror buys brightness, not minutes. A longer pass (higher orbit) buys minutes and spends brightness. N = N_I × N_T for one site.

---

## Numbers you must not change (625 km)

**Nadir envelope (twilight, looking down):**
- D = 5.812 km
- M18 ideal I = 0.01175 W/m²; M55 ideal I = 0.1097 W/m²
- T_useful = 4.281 min; horizon pass = 13.16 min
- Fluence upper bound M55: ~28 J/m²

**Civil night (the value case): sat still sunlit on the terminator, site Sun 6° down:**
- Path d = 937.5 km; elevation ε = 38.74°; bounce at mirror i = 67.63°
- Ellipse ~8.7 × 14 km (D_minor = 8.719 km); A_image = 95.41 km²
- I is 0.150 × the nadir envelope
- M18 ideal I = 0.001759 W/m² (fails moonlight 0.003)
- M55 ideal I = 0.01642 W/m² (moonlight pass; fails street 0.1)
- 1 km sheet: 5.429 W/m² (street-bright; fails 20 min — needs ~7.1 sequential passes)
- T_useful = 2.809 min
- 400 km: no useful night pass (max elevation 27.2° < 30°)

**Optical factor:** η = 1 is ideal; 0.675 is one estimated clear-sky factor. Do not stack extra atmospheres.

**Parked bins (scoring only):** moonlight 0.003 W/m²; street-class 0.1 W/m² and 20 min; weak PV 50 W/m²; energy 200 W/m² and 3 h; daylight 1000 W/m².

**Fleet, one site, η = 1, night:** moonlight from M18 is N ≈ 1.7 (two mirrors). Street-class 20 min is N = 405 of 18 m, or ~43 of 55 m. If the mirror stays small, fewest street-class satellites on this scan are near 1500 km (M18: 405 → 196), not at 625 km.

GEO D ≈ 333 km — a size check, not an operating point.

---

## Figures in the report (do not add new ones)

| Figure | Takeaway |
|---|---|
| S-geo-2d | The 45° bounce is at the mirror, not the ground. The patch is the Sun’s image. |
| S-focus | A dish focused at the ground does not shrink the solar image. Extra curve opens D. |
| S-spot-h | Width is height times how wide the Sun looks. 625 km → 5.812 km. |
| S-I-A | Peak I scales with collecting area over the solar image, not like a lamp 1/r². |
| S-dwell | Useful light is minutes. Area does not buy the window. Literature “~20 min at 1000 km” is the horizon pass (17.61 min), not useful time (6.727 min). |

---

## Argument shape

Scene → flashlight picture → two facts → five corrections people reach for (spotlight / curve / bigger / hover / midnight) → two currencies → what the physics actually says → appendix numbers.

Midnight overhead in LEO is usually Earth’s shadow: nothing to bounce. You get **early night from a still-sunlit terminator**, at a penalty, or you get zero.

---

## Out of the report

Launch cost, firms, products, 3D explorer, lux as a kernel output, stacked suns past one filled image, one satellite for three hours, “streetlights from space” as the title subject.
