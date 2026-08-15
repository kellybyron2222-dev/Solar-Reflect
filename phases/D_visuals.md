# Phase D — Visuals v1 (detailed outline)

**Depends on:** passing tests (Look-back C)  
**Produces:** figure scripts + `figures/working/` for v1 scenes (S-geo-2d and S-spot-h required before E1; others earned by campaign)  
**Do not produce:** 3D globe, GUI product, report-styled “hero” art, application horizontals on S-I-A yet

---

## Why this phase exists

You need to *see* \(\alpha\) and \(h^2\). You do not need a renderer. If a drawing cannot be built from `physics.py`, it is not in v1.

---

## Work sequence

### D0. Re-evaluate from C (before drawing)

C decides what is safe to put on an axis. Untrusted quantities do not get a scene.

1. Open `carry/C_to_D.md`. If missing, stop.
2. Diff the default six-scene catalog against C: if T_useful is weakly tested, S-dwell can wait until E4 and must be labeled accordingly; if D and I passed, S-geo-2d and S-spot-h proceed.
3. Write `carry/D_scoped.md`: which scenes this phase will actually build **now** vs campaign-owned; anything C forbids drawing.
4. Then pin the rules and build the scoped set.

Typical C→D impacts:

| If C concluded… | Then D… |
|---|---|
| D and I at 625 km trusted | S-geo-2d and S-spot-h are in |
| T_useful only weakly tested | Do not treat S-dwell as a D gate; stamp “formula as in spec” |
| Diffraction discarded | Do not draw Airy rings |
| Energy identity passed | S-I-A may be built in E2 |
| A test failed | No figure that uses that quantity until C is re-run |

### D1. Rules (pin above the keyboard)

- Matplotlib (or equivalent) 2D only.
- Numbers from kernel calls, never typed into the artist layer.
- Stamp on every figure: geometry (nadir, \(\gamma=45^\circ\)), \(\eta\) column, equation ID, constants hash or date+git.
- No beam, no satellite mesh, no Earth photo.
- Catalog is six IDs. Building a seventh is a framed change or it waits.

### D1b. Scene specs (draw from these, not from memory)

**S-geo-2d — mechanism**

- Show: Sun as a *disk* of angle \(\alpha\), mirror as a short segment, slant \(d\), \(\gamma\), ground, solar-image diameter \(D\).
- Nadir case. Label symbols to match spec.md.
- Optional second small panel: same geometry with \(\varepsilon < 90^\circ\) showing an elongated ellipse — only if it does not become the envelope.
- Question on the figure: “The Sun is extended; the patch is \(d\alpha\).”

**S-spot-h — scaling of patch**

- x: \(h\) (km), 300–2000 at least; GEO as a text callout, not a compressed axis.
- y: \(D\) (km).
- One line: \(D = h\alpha\).
- Markers: none required. Optional vertical lines at 400, 625, 1000, 2000.

**S-focus — étendue concept (2D)**

- Dual panel: (left) flat mirror, cone of angle \(\alpha\), patch \(D\); (right) concave with \(f=d\), image of the solar disk still \(D\); caption that \(f<d\) focuses early then diverges.
- No ray-tracing theater. Three rays from two solar-limb points are enough.

**S-I-A — energy scaling** (may wait until E2)

- log \(A\) vs log \(I_\text{peak}\), one line per \(h\) in the grid, two frames or two styles for ideal vs realistic.
- **No \(I^*\) horizontals in D / E2.** Those turn on in E5 only.

**S-A-req** (wait for E3)

- \(h\) vs required \(A\) (log), one line per parked \(I^*\).

**S-dwell** (wait for E4)

- \(h\) vs \(T_\text{horizon}\) and \(T_\text{useful}\) (minutes).

### D2. Script layout (suggested)

```
figures/s_geo_2d.py
figures/s_spot_h.py
figures/s_focus.py
figures/s_I_A.py      # E2
figures/s_A_req.py    # E3
figures/s_dwell.py    # E4
figures/working/
```

Each script: import physics + constants, compute, plot, save svg+png, print the hash/stamp.

Shared helper allowed: `figures/_style.py` for fonts, line weights, stamp function. No second physics module.

### D3. Minimum to leave D and start E1

Must exist and match kernel at 625 km:

- [ ] S-geo-2d
- [ ] S-spot-h
- [ ] S-focus (strongly preferred with E1; if time-split, E1 mini look-back must still include the focusing argument in prose)

S-I-A, S-A-req, S-dwell are **campaign-owned**. Do not block E1 on them.

### D4. Explicitly out of D-v1

3D Earth, orbit camera, clickable symbols, Plotly dash, watt-Sankey, farm overlay, balloon comparison, GUI sliders. If you want them, framed v2 after F.

---

## Look-back D (required)

1. **Intent.** Did visuals become the project? Count hours: kernel+tests should not be smaller than D. If D is a product, cut it back to two scripts.
2. **Plan.** Seventh scene? 3D? Application lines on S-I-A? Undo.
3. **Honesty.** Read \(D\) off S-spot-h at 625 km; compare to C hand sheet.
4. **Ready.** E1 can be written from S-geo-2d + S-spot-h + tables.

Checklist:

- [ ] Stamp on every saved figure
- [ ] 625 km \(D\) matches tests
- [ ] No beam
- [ ] S-I-A, if it exists already, has no \(I^*\) lines
- [ ] Remaining catalog IDs assigned to E2–E4
- [ ] `carry/D_to_E.md` exists: which scenes exist, which E campaigns may start, what E must not treat as trusted

**No-go examples:** Blender; a render of a mylar satellite; delaying E because the 3D terminator “would help.”

**Go:** S-geo-2d + S-spot-h exist and spot-check holds → E (`phases/E_campaigns.md`). E opens `carry/D_to_E.md` first.
