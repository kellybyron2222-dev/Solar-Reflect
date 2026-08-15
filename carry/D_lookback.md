# Look-back D

Re-read frozen intent. Artifacts: `figures/s_geo_2d.py`, `figures/s_spot_h.py`, `figures/s_focus.py`, `figures/working/`.

1. **Intent.** Three 2D scripts. No GUI, no 3D, no extra catalog ID. Kernel+tests remain larger than D.
2. **Plan.** No seventh scene. No \(I^*\) lines. S-I-A / S-A-req / S-dwell not built.
3. **Honesty.** \(D(625\,\mathrm{km})=5.812\,\mathrm{km}\) on S-geo-2d and S-spot-h (rel \(0.0086\%\) vs hand sheet). GEO callout \(333\,\mathrm{km}\). Angle \(\alpha\) on S-geo-2d is enlarged and labeled.
4. **Ready.** E1 can be written from S-geo-2d + S-spot-h + S-focus + C tables.

## Checklist

- [x] Stamp on every saved figure
- [x] 625 km \(D\) matches tests
- [x] No beam
- [x] S-I-A does not exist (no \(I^*\) lines)
- [x] Remaining IDs assigned: S-I-A → E2, S-A-req → E3, S-dwell → E4
- [x] `carry/D_to_E.md` exists

**Go.** E opens `carry/D_to_E.md` first (`phases/E_campaigns.md`).
