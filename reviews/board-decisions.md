# Board decisions

Written into this repo when you Agree or Disagree on the drafting board (`python whiteboard/serve.py`). This file is what the next review pass reads.

## Open disagrees

None. Reviewer accepted all framework cards, including the twilight iteration.

## framing.md

- **agree** Dusk/dawn snapshot, not midnight
  - Recommended: Keep terminator-nadir (sunlit dusk/dawn footpoint) as the brightness envelope, because a mirror overhead at local midnight is usually in Earth’s shadow and has nothing to bounce. Dark-city lighting is a different, parked geometry. Treat 18 m / 55 m / 1 km as scale markers, not architectures. Keep the 400–2000 km grid; GEO is a size check only.
  - Comment: Accepted iteration: keep terminator-nadir. Midnight overhead is usually umbra; dark-site lighting is off-nadir and parked.
  - Updated: 2026-08-14 19:54

<!-- iteration -->
### Iteration — twilight vs darkest night

**Keep terminator-nadir.** Do not switch the kernel to local midnight looking straight down.

At the darkest part of the night, a satellite *overhead* is usually behind the Earth. The mirror is in shadow, so there is no sunlight to reflect. That snapshot is not “the hard lighting case”; it is lights-out unless we also model eclipse (out of v1).

The night-lighting picture people mean is: satellite still in sunlight, beam steered *sideways* toward a dark city. That is off-nadir, longer path, bigger/dimmer solar image, and it needs umbra geometry. Parked. Terminator-nadir \(I\) is optimistic versus that case.

So twilight is not a claim that dusk is the application. It is the only nadir geometry where the mirror is guaranteed sunlit without an eclipse model. Later scoring must not treat this \(I\) as midnight street lighting. C-moon / C-light stay magnitude bins, not a dark-sky scene.

Accept this iteration to freeze the snapshot; reopen it only if v1 should add off-nadir dark-site lighting (new kernel, not a caption change).
<!-- /iteration -->
