# Look-back B

## Four questions

1. **Intent.** Kernel answers \(I\), \(D\), \(T\) (and \(F\), \(A_\text{req}\)). No application classifier, no moonlight vs PV.
2. **Plan.** Cut `n_overlap` from the kernel (E5). Named terminator-nadir instead of “night zenith.” Optional `epsilon_rad` exists but is not the envelope. Legitimate vs A.
3. **Honesty.** \(\rho,\tau\) realistic are `estimated`. Mean \(R_E\) labeled. Fluence docstring says upper bound.
4. **Ready.** 625 km, 55 m, ideal \(I\) is computable from `spec.md` + `constants.yaml` with a calculator.

## Checklist

- [x] constants.yaml complete with classes
- [x] spec.md ≤1–2 pages and matches code
- [x] five functions exist; no plotting
- [x] default call is nadir, \(\gamma=45^\circ\) (terminator-nadir)
- [x] fluence docstring says upper bound
- [x] B7 deferred list written (includes clouds, off-nadir I)
- [x] `carry/B_to_C.md` written

**Go:** Look-back B passes. Phase C may start. C0 opens `carry/B_to_C.md` first.

Post-100 trim: `irradiance`/`required_area` no longer take γ/ε. Envelope is the only I.
