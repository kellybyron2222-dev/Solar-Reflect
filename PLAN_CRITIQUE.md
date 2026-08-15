# Critique of the master outline, and recommended modifications

This is a review of `MASTER_OUTLINE.md`. It does not replace that file until you accept a v2.

---

## Verdict

The **intellectual spine is right**: physics first, applications as readout, one kernel, no economics, report last, no AI space-mirror pictures.

The **process is too large for the physics**. The governing model is one intensity equation, a solar-image diameter, and a circular-orbit pass window. The plan around it is sized like a lab: nine phases, a four-pane GUI, a separate image-generation factory, provenance JSON, negative tests, and gates that require documents before anyone is allowed to compute \(D = h\alpha\).

If executed as written, the likely failure mode is not a wrong irradiance. It is **never reaching E** because D (3D workbench + 13 scenes + click-linked formulas) ate the project.

Keep the discipline. Cut the ceremony. Put implementation of the kernel on the critical path. Make 3D and the GUI *optional*, not a gate to analysis.

---

## What is working (do not throw out)

1. **Question split.** Primary = \(I\), spot, dwell, binding law. Secondary = application classes. That is the whole point of the last few revisions.
2. **One physics kernel feeding drawings.** D and IMG must not have private geometry. C7 (kernel identity) is the right fear.
3. **Ideal vs one realistic column.** No third “optimistic” stack.
4. **Peak vs duration kept separate.** F3 is the claim that will otherwise get smuggled.
5. **Report cannot invent scenes.** G picks IDs from a catalog. That prevents last-minute hero images.
6. **No volumetric beam, no product art.** Those drawings would argue a different physics.

---

## Critical problems

### 1. The plan is heavier than the model

E is five tables. B is one equation. D is a product: 2D engine, 3D engine, formula board with click-to-highlight, six concept dual-panels, explorer sliders, snapshot schema, then IMG with two profiles, sidecars, caption YAML, and export tests.

That inversion will dominate calendar time. **Analysis should be allowed to start with `physics.py` + 2D plots.** Schematics and 3D are amplifiers, not prerequisites.

### 2. There is no implementation phase

B is a spec. C is a checklist. D-build is a GUI. `physics.py` appears only as a ghost in gates (“C1–C4 pass on live code”). For a solo project, **spec and kernel should be the same step**: a one-page B plus the functions that C tests. Splitting “write the contract” from “write four functions” produces paperwork, not rigor.

### 3. C conflates “checklist written” with “checks passed”

The master table says the C gate is *checklist written*. Later text says D/E wait until C1–C4 *pass on code*. Both are true but they are two gates. As written, you can stall in C-the-document forever, or you can think C is done when it has not been run.

**Split:** C-plan (written with B) vs C-run (tests on the kernel). C-run is the real gate to E. C-plan is a half-page of expected numbers, not a phase.

### 4. Linear sequence is false, and 13 scenes are frozen too early

Naming S-geo-3d through S-shutter before E1 has been seen is the same mistake as freezing seven report figures. You will want a different concept scene after you look at the 55 m / 625 km number. **Catalog v1 should be four items.** Expand after E2.

Real loop: kernel → D = hα table → one 2D sketch → I(A,h) → then decide which concept scene is actually confusing.

### 5. 3D is the highest-cost, highest-lie, lowest-argument view

G already says the report gets at most one 3D figure. A true-scale 55 m plate on Earth is invisible; enlarging it (even stamped) trains the eye to see a huge mirror lighting a country. **3D should be v2, optional, never a gate to E.** 2D constructions carry étendue. Plots carry scaling.

### 6. D and IMG are one module with two export profiles

Working snapshot vs report freeze is a flag (`profile=working|report`), not a phase that sits after G. Keeping IMG as a *freeze event* after G is good. Keeping IMG as a separately specced engine duplicates D. **Merge: D exports; G lists IDs; freeze is a command, not a department.**

### 7. Hidden physics in the “default snapshot”

\(\gamma = 45^\circ\) is terminator / night-delivery geometry. Daytime fill-in can be better. The plan applies that cosine to **all** campaigns, then reads energy-production applications off it. That is a framing choice, currently buried in B.

**Promote to A:** two geometries, or one stated default (“night-side zenith, \(\gamma=45^\circ\)”) so E5 does not pretend to be geometry-agnostic.

\(\varepsilon\) on the explorer from day one is the same trap: people will quote low-elevation \(I\) as the envelope. **Nadir is the v1 envelope. \(I(\varepsilon)\) is an optional campaign, not a silent slider.**

### 8. Fluence is named and then not computed

A4 insists \(I_\text{peak} \neq\) fluence/pass \(\neq\) time-average. E2 computes \(I\), E4 computes minutes, **nothing multiplies them**. Energy-production readout without J/m² per pass (or Wh/m² per pass) is theater. Add **E2b or fold into E4:** \(F = I_\text{peak} \times T_\text{useful}\) as a first-order upper bound (envelope, not a light curve).

### 9. Case matrix is lumpy

- 18 m and 55 m are architecture-shaped (motivating class), not a physics grid. Fine as **named markers**, not as the definition of A.
- 200 m is in A3 and never used again. Drop or use it.
- Farm area for S-farm is never in A. Hidden \(A_\text{farm}\) will show up in a drawing. Put it in A2 as a scenario constant (e.g. 1 or 2 km²) or cut S-farm from v1.
- C2’s GEO reconstruction fights “GEO is a callout.” Make GEO a one-line \(D = h\alpha\) check, not a literature campaign.

### 10. Application thresholds mix hard SI with soft duration

\(I^*\) is numeric; duration is “hours” / “tens of minutes.” F3 cannot bind dwell without \(T^*\) as numbers. **Lock duration demands in A5** (e.g. moonlight: 1 pass; weak PV: 20 min; energy: 3 h) or admit duration is qualitative and do not pretend F1 has three comparable axes.

0.003 W/m² for moonlight is a photometry conversion. Mark it **derived/estimated** in the constants register, not as if it were CODATA.

### 11. “Two methods / two people” in C3

You are not a lab. **Calculator vs code** is the check. Do not wait for a second reviewer.

### 12. Banned vocabulary is slightly too precious

Banning “beam” in drawings is right. Banning “impractical” inside F makes the assessment mute. F should say **which requirement is not met** (\(A\) too small, \(h\) too high, \(T\) too short, target \(< A_\text{image}\)). That is the grown-up form of impractical.

### 13. Click-linked formula symbols and sidecar JSON are not gating items

They are polish. If they threaten E, they go. Provenance can be a figure filename and a constants hash in a text file, not a JSON spec phase.

---

## Missing pieces the plan should add

| Gap | Why it matters |
|---|---|
| **Kernel implementation as a named step** | Otherwise nothing is testable |
| **Fluence / pass energy envelope** | Connects I and dwell to “energy” |
| **\(\gamma = 45^\circ\) as an A decision** | Night geometry is not universal |
| **Sensitivity mini-campaign** | C5 lists knobs; E never turns them. One tornado: \(\rho, \tau, \varepsilon_\min\) |
| **MVP / v1 vs v2** | Without this, 3D GUI is v1 by accident |
| **Timebox or “enough” rule for D** | e.g. E1 may start when S-geo-2d + S-spot-h exist |
| **\(A_\text{farm}\) if S-farm stays** | Otherwise the intercept fraction is invented in a picture |

Not missing: spectral MODTRAN, J2, constellation optimizer. Those were correctly deferred.

---

## Recommended modifications (v2)

### Compress the spine

| Step | Name | What it actually is |
|---|---|---|
| **A** | Framing | Short note. Keep A1–A6. Add: default geometry = night zenith \(\gamma=45^\circ\); duration numbers in A5; \(A_\text{farm}\) if needed; 18/55 m are markers not the grid. |
| **B+K** | Spec + kernel | One-page spec **and** `physics.py` in the same step. Four functions. No separate “B accepted, still no code.” |
| **C** | Tests | C-plan is a table of expected values in the spec. C-run is pytest. Gate to analysis: tests pass. |
| **D-v1** | Visuals (MVP) | 2D schematic + formula as annotated SVG/math + campaign plots. Explorer can be a script/CLI or a tiny notebook, not a four-pane product. **3D is D-v2, optional, not a gate.** |
| **E** | Campaigns | E1–E5 as written, **plus fluence envelope** (I × T_useful) next to E4. Optional E-sens: \(\eta\) and \(\varepsilon_\min\). |
| **F** | Assessment | Unchanged intent. Allow requirement language. |
| **G** | Scope | Unchanged. Pick scene IDs from the **v1 catalog** (small). |
| **Export** | Freeze | One exporter, two profiles. Freeze after G. Not a separate IMG department. |
| **H** | Draft | Unchanged. |

### Cut from v1 (move to v2 or drop)

- 3D engine, orbit-around camera, click-to-highlight symbols
- Four-pane GUI
- Scenes: S-geo-3d, S-balloon, S-shutter as *required* gates (keep as optional concepts)
- IMG as its own phase (keep freeze event)
- Sidecar JSON schema, IMG8 negative-test framework as a phase
- 200 m aperture unless you have a reason
- GEO as a C2 campaign (keep \(D_\text{GEO} \approx 330\) km as a one-liner)
- \(\varepsilon\) slider in v1 explorer (nadir only until an optional I(ε) campaign)

### Keep in v1 scene catalog (six, not thirteen)

1. S-geo-2d — the mechanism  
2. S-spot-h — D vs h  
3. S-I-A — I vs A by h  
4. S-A-req — required A (after E2)  
5. S-dwell — pass window  
6. S-focus **or** S-disk — one étendue concept (not both required)

S-watts, S-farm, S-cases, S-balloon, 3D: add when E says they are needed.

### Fix A5 durations (proposal)

| Class | I* (W/m²) | T* (lock this) |
|---|---|---|
| Moonlight-class | 0.003 (estimated radiometric equivalent) | 1 useful pass |
| Street / work lighting | 0.1 | 20 min |
| Weak PV | 50 | 20 min |
| Energy production | 200 | 3 h |
| Daylight-equivalent | 1000 | n/a if I* unreachable |

### Fix the D → E gate

**Old:** explorer + 3D + S-disk + S-focus + kernel identity on all of that.  
**New:** tests pass; S-geo-2d and S-spot-h exist; E1 may start. Other scenes are earned by campaigns, not prepaid.

### Fluence (add to E)

First-order: \(F_\text{pass} \approx I_\text{peak} \times T_\text{useful}\). State that a real pass is a light curve, so this is an **upper bound**. Without it, “energy production” is only a brightness number.

---

## What I would not change

- Physics first, applications last  
- No economics in A–F  
- No AI-generated mirrors  
- No thin beam  
- Report cannot invent figures  
- Ideal fail vs realistic fail (F2)  
- Single realistic factor \(\rho\tau \approx 0.68\), not a weather model  

---

## Suggested decision

Accept **v2 compression** (kernel on the critical path, 3D optional, IMG merged into export, fluence added, six-scene v1 catalog, \(\gamma=45^\circ\) declared in A). Keep `MASTER_OUTLINE.md` as the verbose reference until you say to rewrite it to v2.

If you agree, next action is still A, but A is a **one-to-two page framing note**, not a new process document.
