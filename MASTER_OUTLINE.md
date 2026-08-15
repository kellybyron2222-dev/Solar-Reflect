# Master plan — orbital sunlight on Earth

**Detailed phase outlines** are in the `phases` folder (expand it in the left file tree):

- `phases/A_framing.md`
- `phases/B_spec_kernel.md`
- `phases/C_diligence.md`
- `phases/D_visuals.md`
- `phases/E_campaigns.md`
- `phases/F_assessment.md`
- `phases/G_scope.md`
- `phases/X_export.md`
- `phases/H_draft.md`

Index: `PHASE_OUTLINES.md` (this folder’s root) and `phases/README.md`. From **B onward**, each phase starts by re-evaluating its default outline against `carry/` from the prior phase (`phases/CARRY.md`).


Physics-first thought experiment and analysis. Not a 3D rendering project. Not a company review. Not a journal pipeline. The report is a summary of a finished assessment.

This file is the plan spine. **Detailed working outlines for each phase** are in [`phases/`](phases/README.md). Execute in order. At the end of every phase, run that phase’s **look-back loop** before starting the next one.

---

## Frozen intent

**Framed amendment (A freeze).** Default geometry is **terminator-nadir** (dusk/dawn footpoint, sunlit, \(\gamma=45^\circ\) collector incidence), not zenith over a deep-night dark target. Reason: nadir at local midnight is typically umbra (\(I=0\)); lighting a dark city is off-nadir and parked. Binders in v1 are **energy** (including solar-image dilution) or **shutter**; Ω (“spot too small”) is N/A for parked classes. Clouds as peak \(I\) are out (clear-sky envelope).

**Primary.** For a reflector of collecting area \(A\) at altitude \(h\) with optical factor \(\eta\): what peak irradiance \(I\), ground-patch size \(D\), and dwell \(T\) can be delivered to Earth’s surface at that snapshot, and which physical fact binds (energy including solar-image dilution, or orbital shutter)?

**Secondary.** After those quantities exist, sit them against application classes (moonlight, lighting, weak PV, energy production, daylight). Applications do not drive the model.

**Not the work.** Launch cost, markets, policy, spacecraft product design, photoreal rendering, constellation optimization, spectral weather models, clouds as peak \(I\), AI images of space mirrors.

**Default geometry (declared here, not buried later).** Terminator-nadir snapshot: satellite over the terminator, nadir footpoint at dusk/dawn, \(\gamma = 45^\circ\) collector incidence, \(\varepsilon=90^\circ\), filled solar image, sunlit. Conservative vs daytime \(\gamma<45^\circ\); optimistic vs deeper-night \(\gamma>45^\circ\) and vs off-nadir dark-site lighting. Daytime fill-in is not v1.

**Optical columns.** Ideal (\(\rho = \tau = 1\)) and one realistic (\(\rho\tau = 0.9 \times 0.75 = 0.675\)). No third “optimistic” column.

**Visuals exist to see the physics**, not to produce cinema. v1 is 2D schematics, formulas, and plots constructed from the kernel. 3D is optional later and is never a gate.

---

## Spine

| Phase | Name | Output | You may not start the next phase until |
|---|---|---|---|
| **A** | Framing | Framing note (2 pages) | Look-back A passes |
| **B** | Spec + kernel | One-page spec + `physics.py` | Look-back B passes |
| **C** | Diligence | Expected-value table + passing tests | Look-back C passes |
| **D** | Visuals v1 | 2D schematic, formula, six plots/scenes from the kernel | Look-back D passes |
| **E** | Campaigns | Results book (tables + working figures) | Look-back E passes |
| **F** | Assessment | Assessment log (shown / inferred / open) | Look-back F passes |
| **G** | Report scope | Scope memo + figure ID list | Look-back G passes |
| **X** | Export freeze | `figures/report/` from scoped IDs | Look-back X passes |
| **H** | Draft | Thought-piece summary of F | Look-back H passes (project close) |

**Rule.** A later phase may not invent a number, threshold, scene, or loss term that an earlier phase did not specify. If it must, go back and change the earlier phase on purpose, then re-run that phase’s look-back.

**Feed-forward.** From B onward, do not execute the default phase outline blindly. First re-evaluate that outline against the **carry file** from the prior look-back (`carry/`). Prior conclusions may **narrow** this phase. They may not widen into out-of-scope items. See `phases/CARRY.md`.

**Look-back (same four questions every phase).**

1. **Intent.** Does this output still serve the frozen intent above, physics first?
2. **Plan.** What did we add or skip versus this phase’s outline? Legitimate framed change, or drift?
3. **Honesty.** Every number traces to the kernel or is marked estimated. No beam, no cost, no application-led physics.
4. **Ready.** The gate checklist is actually true, not hoped.

If 1–4 fail: do not proceed. Fix, or record a framed amendment at the top of this file.

---

## Phase A — Framing

### Purpose

Write down what the assessment is, so later phases cannot quietly change the question.

### Outline

1. **A1 Question.** Copy the frozen-intent primary and secondary paragraphs. One page max including A2–A6.
2. **A2 Variables.**
   - Independent: \(h\), \(A\), \(\eta\) (ideal / realistic).
   - Dependent: \(D\), \(A_\text{image}\), \(I_\text{peak}\), \(T_\text{horizon}\), \(T_\text{useful}\).
   - Derived: fluence envelope \(F_\text{pass} \approx I_\text{peak} \times T_\text{useful}\), \(N_\text{overlap} = I^*/I_\text{one}\), lux (derived only).
   - Scenario constants: \(\gamma = 45^\circ\), \(\varepsilon = 90^\circ\) (nadir), \(\varepsilon_\min = 30^\circ\) for useful pass, \(A_\text{farm} = 2\,\text{km}^2\) only if we draw intercept (optional, not required for v1).
3. **A3 Grid and markers.**
   - Physics grid altitudes: 400, 625, 1000, 2000 km. GEO is a one-line \(D = h\alpha\) callout, not a campaign.
   - Physics grid areas: use side lengths 18 m, 55 m, 1 km as **named markers** on plots, plus the continuous \(A\) axis. Drop 200 m unless a later framed change needs it.
4. **A4 Vocabulary.** \(I_\text{peak}\) ≠ fluence/pass ≠ time-average. Patch = solar image, not beam. Requirement not met ≠ a vibe. Ban in drawings: volumetric beam, spacecraft product art.
5. **A5 Application classes (parked until E5).**

   | Class | \(I^*\) (W/m²) | \(T^*\) |
   |---|---|---|
   | Moonlight-class | 0.003 (estimated radiometric equivalent of moonlight; not CODATA) | 1 useful pass |
   | Street / work lighting | 0.1 | 20 min |
   | Weak PV | 50 | 20 min |
   | Energy production | 200 | 3 h |
   | Daylight-equivalent | 1000 | n/a if \(I^*\) unreachable |

6. **A6 Out of scope.** Cost, launch, policy, ecology, spectral RT, clouds as peak \(I\), J2, constellation design, company evaluation, 3D as a deliverable, daytime \(\gamma\) other than 45° (v2).

### Deliverable

`framing.md` — A1–A6, ≤2 pages.

### Look-back A

- [x] Primary question is about \(I\), \(D\), \(T\), and binding law — not about a firm or a use case.
- [x] \(\gamma = 45^\circ\) and nadir are explicit.
- [x] \(I^*\) and \(T^*\) are parked, not used to design the kernel.
- [x] 18 m / 55 m are markers, not the definition of \(A\).
- [x] Nothing in A6 leaked into A1.
- [x] Ready for B: a stranger could write the four functions from this note plus a constants list.

**Go / no-go:** framing.md exists and the boxes are true → **GO (v3).** Record: `carry/A_lookback.md`.

---

## Phase B — Spec + kernel

### Purpose

The model is the spec **and** the code in one step. No paperwork-only B.

### Outline

1. **B1 Constants** (in `constants.yaml`, cited): \(E_0 = 1361\,\text{W/m}^2\), \(\alpha = 9.3\,\text{mrad}\), \(\mu\), \(R_E\), \(\gamma\), \(\rho\), \(\tau\), \(\varepsilon_\min\). Moonlight \(I^*\) flagged estimated.
2. **B2 Geometry.** Spherical Earth, circular orbit. Nadir: \(d = h\), \(D = d\alpha\), \(A_\text{image} = \pi(d\alpha/2)^2\). Off-nadir (for \(T_\text{useful}\) only): document \(\varepsilon_\min\); do not use off-nadir \(I\) as the v1 envelope.
3. **B3 Optics.** Filled solar image. Flat and focusing share \(D_\min = d\alpha\). Scalar \(\rho\). No BRDF, no slope-error switch in v1.
4. **B4 Irradiance.**
   \[
   I = \frac{E_0\,\rho\,\tau\,A\cos\gamma\sin\varepsilon}{\pi(d\alpha/2)^2}
   \]
   v1 envelope: \(\varepsilon = 90^\circ\), \(d = h\), \(\gamma = 45^\circ\).
5. **B5 Time window.** Keplerian circular period; horizon-to-horizon; useful window \(\varepsilon > 30^\circ\).
6. **B6 Derived.** \(F_\text{pass} \approx I_\text{peak} \times T_\text{useful}\) (upper bound; not a light curve). \(N_\text{overlap} = I^*/I_\text{one}\).
7. **B7 Deferred.** Spectral atmosphere, J2, eclipse seasons, PSF, 3D, \(I(\varepsilon)\) sweep, constellation trains except as \(N_\text{train} \approx T^*/T_\text{useful}\).
8. **Kernel functions** (same phase): `solar_image`, `irradiance`, `required_area`, `pass_window`, `fluence_envelope`.

### Deliverable

`spec.md` (one page) + `constants.yaml` + `src/physics.py`.

### Look-back B

- [x] Every symbol in the equation lives in constants.yaml or is an input.
- [x] Terminator-nadir default matches A. No daytime geometry snuck in.
- [x] Fluence is an envelope, labeled upper bound.
- [x] Code implements only B2–B6. No plotter, no GUI, no application logic.
- [x] Deferred list B7 is explicit; F cannot later “discover” missing physics as a conclusion.
- [x] Ready for C: you can write expected numbers for 625 km by hand.

**Go / no-go:** spec + kernel exist and boxes true → **GO** pending 100-persona FATAL union. Record: `carry/B_lookback.md`.

---

## Phase C — Diligence

### Purpose

Distrust the kernel before drawing or interpreting. C-plan is a small table of expected values. C-run is tests. **Passing tests** is the gate, not the table existing.

### Outline

1. **C1 Analytic.** Nadir \(D = h\alpha\). Ideal energy: \(I \times A_\text{image} = E_0 A \cos\gamma\).
2. **C2 Limit checks (one-liners).** GEO \(D \approx 330\,\text{km}\). Airy disk \(\ll D\) at visible \(\lambda\) for meter-class \(A\) (discard diffraction).
3. **C3 Worked example, two methods.** 625 km, 18 m square and 55 m square, ideal and realistic \(I\). Calculator vs code, agree to 1%.
4. **C4 Dominance reminder.** Peak \(I\) moves with \(A\), \(h\), \(\eta\). Clouds do not move peak \(I\). Dwell moves with \(h\) and \(\varepsilon_\min\).
5. **Tests.** `tests/test_physics.py` encodes C1–C3. No visual tests yet.

### Deliverable

Expected-value table in `spec.md` + passing tests.

### Look-back C

- [x] Tests were run, not only written.
- [x] 625 km example matches hand arithmetic to 1%.
- [x] Diffraction was shown negligible and is not in the kernel.
- [x] No application \(I^*\) was used to “tune” the code.
- [x] Intent still physics-first; we did not start a GUI to avoid checking the equation.
- [x] Ready for D: numbers are trustworthy enough to draw.

**Go / no-go:** tests pass and boxes true → **GO.** Record: `carry/C_lookback.md`. D opens `carry/C_to_D.md` first.

---

## Phase D — Visuals v1

### Purpose

See the physics while analyzing. 2D constructions, formulas, plots — from the kernel only. **Not a 3D product. Not report art.**

### Outline

**v1 catalog (six). Do not prepaid a larger set.**

| ID | Kind | Question | Needed to start |
|---|---|---|---|
| S-geo-2d | 2D schematic | What are \(\alpha, d, \gamma, \varepsilon\), and the solar image? | E1 |
| S-spot-h | Plot | How does \(D\) scale with \(h\)? | E1 |
| S-I-A | Plot | How does \(I_\text{peak}\) scale with \(A\) and \(h\)? | E2 |
| S-A-req | Plot | What \(A\) does a given \(I^*\) require? | E3 (after E2) |
| S-dwell | Plot | What time window does orbit allow? | E4 |
| S-focus | Concept (2D) | Why does focusing not shrink \(D_\min\)? | E1 |

Optional later (not gates): watt chain, farm intercept, case scatter, balloon vs LEO, 3D terminator view.

**Rules.** Geometric construction from `physics.py`. Stamp: ideal/realistic, \(\gamma\), \(\varepsilon\), equation. No beam, no spacecraft mesh, no Earth-from-space stock. Formula is typeset math with current numbers, not a GUI science project.

**Build.** Python + Matplotlib (and mathtext). Scripts, or a thin notebook that calls the kernel. No four-pane app. No Plotly Earth globe as a requirement.

**Working export.** `figures/working/<scene-id>.*` with constants hash in the filename or a text stamp. Same scripts will later freeze report copies (phase X).

### Deliverable

Scripts that produce the six v1 scenes from the kernel. S-geo-2d and S-spot-h must exist before E1. The others may be built campaign-by-campaign (earned, not prepaid).

### Look-back D

- [x] Every drawn number matches `physics.py` (spot-check 625 km on S-geo-2d and S-spot-h).
- [x] We did not build 3D, a GUI, or extra scenes “because it would look good.”
- [x] S-focus argues étendue, not a pretty mirror.
- [x] Application horizontals are **off** on S-I-A until E5.
- [x] Intent: visuals serve the thought experiment, not the other way around.
- [x] Ready for E1: S-geo-2d and S-spot-h exist; remaining scenes have a named campaign owner.

**Go / no-go:** S-geo-2d + S-spot-h exist, 625 km spot-check holds → E1. Do not wait for S-A-req or optional scenes.

---

## Phase E — Analysis campaigns

### Purpose

Fill a results book. Descriptive observations only. No verdicts (those are F). Use D to see; do not invent physics in a picture.

### Outline

Run in order. After each campaign, a **mini look-back** (same four questions, scoped to that campaign) before the next campaign.

**E1 Geometry.** \(D(h)\), \(A_\text{image}(h)\). Forbidden: target smaller than the solar image. Scenes: S-geo-2d, S-spot-h, S-focus.  
Mini look-back: did we treat \(D\) as a design knob? If yes, stop.

**E2 Energy.** \(I_\text{peak}(A,h)\) ideal and realistic on the A3 markers + curves. Scene: S-I-A.  
Mini look-back: is \(\gamma = 45^\circ\) still labeled? Did application lines sneak on?

**E3 Requirements.** Invert for \(A(I^*,h)\) using parked A5 \(I^*\) only. Scene: S-A-req (build now).  
Mini look-back: any new \(I^*\)? If yes, return to A5.

**E4 Time + fluence.** \(T_\text{horizon}(h)\), \(T_\text{useful}(h)\), \(F_\text{pass} \approx I_\text{peak} \times T_\text{useful}\) as upper bound. Scene: S-dwell.  
Mini look-back: did we imply a single satellite provides \(T^*\)? Duration is a train multiplier \(N_\text{train} \approx T^*/T_\text{useful}\).

**E5 Readout (last).** Place markers on application classes: \(I_\text{peak}\) vs \(I^*\), \(T_\text{useful}\) vs \(T^*\), separately. Optional: \(N_\text{overlap}\), \(N_\text{train}\).  
Mini look-back: did E5 change the kernel? If yes, revert E5.

**Optional E-sens (not a gate).** Tornado on \(\rho,\tau,\varepsilon_\min\) for one marker. Only if E2/E4 left a doubt.

### Deliverable

`results/e1.md` … `results/e5.md` (or one `results_book.md`): question, table, figure IDs, check cited, one descriptive paragraph each.

### Look-back E (whole phase)

- [ ] Five campaigns present; E5 labeled readout.
- [ ] Fluence is in the book and called an upper bound.
- [ ] Tables alone answer \(D(h)\), \(I(A,h)\), \(A_\text{req}(I^*,h)\), \(T_\text{useful}(h)\), and where 18 m / 55 m / 1 km at 625 km sit.
- [ ] No verdict language (“useless,” “impractical”) in E.
- [ ] No new loss terms, altitudes, or \(I^*\) except via framed amendment.
- [ ] Ready for F: you can interpret without computing anything new.

**Go / no-go:** results book complete and boxes true → F.

---

## Phase F — Assessment

### Purpose

The intellectual product. Interpret the results book. Still not the public report.

### Outline

1. **F1 Binding map.** For each A5 class and each named marker: which of energy (\(A/h^2\)), solar-image size (\(D=h\alpha\)), or shutter (\(T\)) binds first.
2. **F2 Ideal vs realistic.** Fail on ideal → physics-limited. Pass ideal, fail realistic → \(\eta\)-sensitive.
3. **F3 Peak vs duration.** Do not promote moonlight-class \(I_\text{peak}\) into energy production via a hypothetical train without writing \(N_\text{train}\).
4. **F4 Cannot say.** Copy B7. Add anything E showed is sensitive but unmodeled (e.g. low \(\varepsilon\)). Open, not conclusions.
5. **F5 Claims.** Numbered. Each points at an E table or scene ID. Allowed language: requirement not met because \(A\), \(h\), or \(T\) fails the parked \(I^*,T^*\). No cost.

### Deliverable

`assessment.md`

### Look-back F

- [ ] Every F5 claim has a pointer into the results book.
- [ ] Applications did not rewrite the physics.
- [ ] 3D or aesthetics did not influence a claim.
- [ ] Open items are listed, not papered over.
- [ ] You would defend this log without an essay.
- [ ] Ready for G: the assessment stands alone.

**Go / no-go:** assessment.md exists and boxes true → G. Do not open a report file.

---

## Phase G — Report scoping

### Purpose

Decide what of F is public. No new math. No new scenes.

### Outline

Answer in a short memo:

1. Audience (technical reader vs yourself).
2. Which F5 claims survive (drop any still tied to an open item).
3. Figure ID list — **subset of v1 catalog only** (plus any optional scene that was actually built in E).
4. At most one schematic that is not a plot; prefer S-geo-2d and S-focus. No 3D unless you later framed D-v2.
5. Applications: table after limits, not the lead.
6. Named 18 m / 55 m markers: illustration of E5, not the subject.
7. Length band chosen from F’s bulk, not guessed now.

### Deliverable

`scope.md` with a bullet figure list of scene IDs.

### Look-back G

- [ ] Every figure ID exists in `figures/working/` from E/D.
- [ ] No “we should draw a satellite over a farm” item.
- [ ] Claims in scope ⊆ F5.
- [ ] Intent: physics first, applications as readout — still true of the proposed essay shape.
- [ ] Ready for X: freeze list is finite and already generated once.

**Go / no-go:** scope.md signed → X.

---

## Phase X — Export freeze

### Purpose

One exporter, two profiles. Working copies already exist. Freeze report copies of **exactly** G’s ID list. This is not a new drawing module.

### Outline

1. Re-run the same scripts with `profile=report` (clean stamp, SVG+PDF, no notebook chrome).
2. Write `figures/report/captions.md`: one-sentence takeaway, assumptions, units, per ID.
3. Record constants hash next to the files (a text file is enough; not a JSON platform).

### Deliverable

`figures/report/` = G’s list, plus captions.

### Look-back X

- [ ] Set of files == G’s list (no extras, no missing).
- [ ] Spot-check: one number on S-spot-h still matches the results book.
- [ ] No new geometry.
- [ ] Ready for H: drafting can only include these paths.

**Go / no-go:** freeze matches G → H.

---

## Phase H — Draft

### Purpose

Summarize F under G with frozen figures. No physics decisions. No drawing decisions.

### Outline

1. Place figures and captions from X.
2. Appendix: 625 km worked example from C3/E2.
3. Body: mechanism → facts → limits (spine) → application readout → close.
4. If a sentence needs a new number → return to E (then F, G, X as needed). If a figure is wrong → return to D/X, not a screenshot editor.

### Deliverable

`report.md` (or equivalent).

### Look-back H (close)

- [ ] Every number is in the results book or C3 example.
- [ ] Every figure is in `figures/report/`.
- [ ] Lead is physics; applications are last.
- [ ] No cost, no firm as subject, no beam.
- [ ] Drift check vs frozen intent: still a thought experiment about limits of delivering reflected sunlight, not a rendering demo and not a business case.
- [ ] Done: framing, spec+kernel, tests, visuals v1, results book, assessment, scope, freeze, draft.

**Stop.** Do not add a v2 3D workbench unless a new framed intent says the assessment is incomplete without it.

---

## v1 vs later (do not mix)

| v1 (this plan) | Later, only after a framed change |
|---|---|
| Kernel, tests, 2D, six scenes, results book, assessment, short report | 3D schematic, GUI explorer, \(I(\varepsilon)\) sweep, slope error, extra concept scenes |
| Night zenith \(\gamma=45^\circ\) | Daytime geometry |
| Fluence as \(I \times T\) upper bound | Integrated light curve |
| Markers 18 m, 55 m, 1 km | Architecture case study of a named system |

---

## Next action

Start **Phase A only.** Use [`phases/A_framing.md`](phases/A_framing.md). Write `framing.md`. Run Look-back A. Do not open `physics.py` until that loop passes.
