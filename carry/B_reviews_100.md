# Phase B — 100-persona review (synthesis)

Simulated on spec+kernel before the post-review API trim, then MAJOR closed.

## Tally (as reviewed)

| Block | Approve | Nits | Reject |
|---|---|---|---|
| 1–25 kernel / optics | 12 | 11 | 2 |
| 26–50 orbit / T | 16 | 9 | 0 |
| 51–75 process | 9 | 11 | 5 |
| 76–100 readers | 12 | 10 | 3 |
| **Total** | **49** | **41** | **10** |

Rejects were: no 1-sun clip (A/E policy), C-day 1000 past fill line (parked I*), B incomplete without tests (that is C), GUI/3D/classifier/daytime (A6), constellation N_train, daytime γ, optional I(ε) footgun.

## Union FATAL

**None.**

## Union MAJOR → disposition

| Issue | Disposition |
|---|---|
| Optional `epsilon_rad` on `irradiance` with \(d=h\) | **Removed.** `irradiance(A,h,eta)` is terminator-nadir only. |
| T units (seconds vs framing minutes) | spec.md + B_to_C state **seconds** |
| Degree snapshot vs radian equations | spec.md units banner |

Nits not reopened: no clip; Earth rotation/J2 scoped out; STK not oracle.

## Freeze

**Yes.** Look-back B + `carry/B_to_C.md`. C0 opens that file first.
