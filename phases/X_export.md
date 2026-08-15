# Phase X — Export freeze (detailed outline)

**Depends on:** `scope.md` after Look-back G  
**Produces:** `figures/report/` + `figures/report/captions.md`  
**Do not produce:** new scenes, a second drawing stack, GUI screenshots

---

## Why this phase exists

H may only include files that were generated from the kernel and named in G. Freeze is a repeatable export, not Photoshop.

---

## Work sequence

### X0. Re-evaluate from G (before re-running scripts)

G’s manifest is the scope. X does not choose favorites.

1. Open `scope.md` and `carry/G_to_X.md`. If carry is missing, stop.
2. If G cut a figure, do not export it “because we already had a nice working copy.”
3. Write `carry/X_scoped.md`: exact ID list to freeze.
4. Then export that list only.

### X1. List

Copy G’s figure ID list. This is the manifest. `ls figures/report` must equal this list (plus captions and a hash file).

### X2. Re-run

Same scripts as D/E with a `report` flag or output directory:

- SVG (and PDF if easy)
- PNG preview
- No notebook UI, no slider chrome, no “working draft” watermark that implies unreliability; keep the physics stamp (\(\gamma\), \(\eta\), equation)

### X3. Captions (`figures/report/captions.md`)

Per ID, four lines:

- Takeaway (one sentence; must not exceed the F5 claim it supports)
- What is plotted (axes/units or schematic contents)
- Assumptions (nadir, \(\gamma=45^\circ\), ideal vs realistic)
- Pointer (E table / F5.n)

Do not write captions that introduce farms, firms, or cost.

### X4. Hash note

`figures/report/PROVENANCE.txt`: git commit if any, date, constants.yaml identity (copy E0, alpha, rho, tau). Enough to regenerate. Not a platform.

### X5. Spot-check

Pick S-spot-h: \(D\) at 625 km equals results book and C hand sheet.

### X6. Carry to H

Write `carry/X_to_H.md`: frozen paths, caption file, provenance file. H may include only these.

---

## Look-back X (required)

1. **Intent.** Any decorative extra file? Delete it.
2. **Plan.** Files == G list.
3. **Honesty.** Spot-check passed.
4. **Ready.** H can include graphics without opening Matplotlib.

Checklist:

- [ ] Manifest match
- [ ] Captions exist for every ID
- [ ] Provenance.txt exists
- [ ] One numeric spot-check passed
- [ ] No 3D, no new geometry
- [ ] `carry/X_to_H.md` exists (paths + caption file)

**Go:** boxes true → Phase H. H opens `carry/X_to_H.md` first.
