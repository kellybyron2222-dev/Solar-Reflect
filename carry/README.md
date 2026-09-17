# Carry files

Written at the **end** of each phase look-back. Read at the **start** of the next phase (B onward).

Template and rules: `phases/CARRY.md`

| After phase | File | Read by |
|---|---|---|
| A | `carry/A_to_B.md` | B0 |
| A | `carry/B_scoped.md` | B (this phase) |
| B | `carry/B_to_C.md` | C0 |
| C | `carry/C_to_D.md` | D0 |
| D | `carry/D_to_E.md` | E0 |
| E | `carry/E_scoped.md` | E (this phase) |
| E1 | `carry/E1_to_E2.md` | E2 |
| E2 | `carry/E2_to_E3.md` | E3 |
| E3 | `carry/E3_to_E4.md` | E4 |
| E | `carry/E_to_F.md` | F0 |
| F | `carry/F_to_G.md` | G0 |
| G | `carry/G_to_X.md` | X0 |
| X | `carry/X_to_H.md` | H0 |

Each receiving phase also writes `carry/<phase>_scoped.md` before doing the work.
