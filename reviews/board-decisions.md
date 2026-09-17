# Board decisions

Written into this repo when you Agree or Disagree on the drafting board (`python whiteboard/serve.py`). This file is what the next review pass reads.

## Open disagrees

- **tests/hand_625.md** — Checked example (625 km, 55 m): can we do a second calc at a more reasonable size, 9square meter

## MASTER_OUTLINE.md

- **agree** Master plan — orbital sunlight on Earth
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:52
- **agree** Frozen intent
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:53
- **agree** Spine
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:53
- **agree** Purpose
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:53
- **agree** Outline
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back A
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back B
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back C
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Deliverable
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back D
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back E (whole phase)
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back F
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back G
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back X
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Look-back H (close)
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** v1 vs later (do not mix)
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54
- **agree** Next action
  - Recommended: Keep this section as written.
  - Updated: 2026-08-14 23:54

## constants.yaml

- **agree** Constants
  - Recommended: Keep these constants as written.
  - Updated: 2026-08-14 22:03

## framing.md

- **agree** Dusk/dawn snapshot, not midnight
  - Recommended: Keep terminator-nadir (sunlit dusk/dawn footpoint) as the brightness envelope, because a mirror overhead at local midnight is usually in Earth’s shadow and has nothing to bounce. Dark-city lighting is a different, parked geometry. Treat 18 m / 55 m / 1 km as scale markers, not architectures. Keep the 400–2000 km grid; GEO is a size check only.
  - Comment: Accepted iteration: keep terminator-nadir. Midnight overhead is usually umbra; dark-site lighting is off-nadir and parked.
  - Updated: 2026-08-14 19:54
- **agree** The question
  - Recommended: Freeze the question as: how bright, how big, and how long is the ground patch at dusk/dawn looking straight down? Then: does energy or the orbital shutter bind first. Lighting/PV wait until those numbers exist.
  - Updated: 2026-08-14 21:25
- **agree** What we vary vs what we freeze
  - Recommended: Vary only altitude, area, and optical factor. Keep fold 45° and nadir 90° as a frozen snapshot. Do not let lighting or PV thresholds choose the model.
  - Updated: 2026-08-14 20:56
- **agree** The Sun is a disk, not a lamp
  - Recommended: Treat the ground patch as the Sun’s image. Focusing cannot shrink it. Binders are energy (including that dilution) or shutter — not cost, not “spot too small.”
  - Updated: 2026-08-14 20:59
- **agree** How we will score uses later
  - Recommended: Keep moonlight / lighting / weak PV / energy / daylight as parked estimated bins for a later readout. They must not choose area, altitude, or efficiency.
  - Updated: 2026-08-14 20:59
- **agree** What we are not modeling
  - Recommended: Keep cost, clouds-as-peak-I, eclipse on the pass, 3D, daytime geometry, and company evaluation out of this version. Peak I stays a clear-sky envelope.
  - Updated: 2026-08-14 21:00

## spec.md

- **agree** Only one brightness geometry
  - Recommended: Keep kernel I at terminator-nadir only. The 30° elevation cut is for timing, not for dimming the quoted peak.
  - Updated: 2026-08-14 21:29
- **agree** Patch size
  - Recommended: Keep D = h × α with α the full solar angular diameter, the same for flat and focusing, computed in metres.
  - Updated: 2026-08-14 21:30
- **agree** Brightness formula
  - Recommended: Keep I as collected sunlight spread over the solar image (not a lamp 1/r²). Pass η as one factor (1 or 0.675); do not stack ρ and τ on top.
  - Updated: 2026-08-14 21:33
- **agree** How long a pass lasts
  - Recommended: Keep period on a = R_Earth + h. Useful time is geometric visibility above 30° on an overhead pass, with no umbra cut — an upper bound on duration.
  - Updated: 2026-08-14 21:36
- **agree** Energy per pass is an upper bound
  - Recommended: Keep fluence as I × T_useful, labeled upper bound. Keep required_area as a linear invert with no 1-sun clip in the kernel.
  - Updated: 2026-08-14 21:39
- **agree** Missing physics is not a finding
  - Recommended: Do not treat missing clouds, spectral atmosphere, umbra, wrinkles, or daytime fold as later results. They were left out on purpose.
  - Updated: 2026-08-14 21:39

## tests/hand_625.md

- **disagree** Checked example (625 km, 55 m)
  - Recommended: Accept 0.11 W/m² ideal (0.074 estimated) into a 5.8 km patch as the calibration point. If that scale feels wrong, stop before we draw or sweep the grid.
  - Comment: can we do a second calc at a more reasonable size, 9square meter
  - Updated: 2026-08-14 22:03

<!-- iteration -->

### Iteration — twilight vs darkest night

**Keep terminator-nadir.** Do not switch the kernel to local midnight looking straight down.

At the darkest part of the night, a satellite *overhead* is usually behind the Earth. The mirror is in shadow, so there is no sunlight to reflect. That snapshot is not “the hard lighting case”; it is lights-out unless we also model eclipse (out of v1).

The night-lighting picture people mean is: satellite still in sunlight, beam steered *sideways* toward a dark city. That is off-nadir, longer path, bigger/dimmer solar image, and it needs umbra geometry. Parked. Terminator-nadir \(I\) is optimistic versus that case.

So twilight is not a claim that dusk is the application. It is the only nadir geometry where the mirror is guaranteed sunlit without an eclipse model. Later scoring must not treat this \(I\) as midnight street lighting. C-moon / C-light stay magnitude bins, not a dark-sky scene.

Accept this iteration to freeze the snapshot; reopen it only if v1 should add off-nadir dark-site lighting (new kernel, not a caption change).

<!-- /iteration -->
