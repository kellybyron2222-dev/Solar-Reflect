# Phase B — build loop log

## Scope

`carry/B_scoped.md`: five functions, terminator-nadir defaults, no I*/n_train/plots.

## Build

- `constants.yaml`, `spec.md`, `src/physics.py`, `requirements.txt` (PyYAML)
- Smoke: energy identity exact; GEO \(D\approx 333\) km; μ YAML `e+14` → `e+14` fix

## Peer review (parallel)

| Reviewer | Verdict | Action |
|---|---|---|
| Compliance | Hold (process): kernel OK; look-back/B_to_C missing at review time | Closed after this log |
| Hostile physics | Approve with nits | Off-nadir ε footgun documented; no FATAL |
| Optics | Approve with nits | Same; 1-sun = I(A=A_image) |
| Orbit | Approve with nits | Overhead max-duration named; θ one-sided |

## Iterate

spec.md + docstrings: radians, overhead pass, do not report I(ε), θ one-sided.

## 100-persona pass

See `carry/B_reviews_100.md` (next).

## Gate

Look-back B written. C must not start until 100-persona FATAL union is empty.
