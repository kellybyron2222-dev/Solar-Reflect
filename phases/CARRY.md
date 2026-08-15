# Carry-forward (how phases talk to each other)

The outlines in this folder are the **default** plan. They are not a script that ignores what just happened.

**From B onward, the first step of every phase is a re-evaluation:** read the prior phase’s carry file, compare it to this phase’s default outline, then write a **scoped plan for this phase** before doing the work. Conclusions upstream change what is in scope downstream.

Frozen intent in `MASTER_OUTLINE.md` still wins. A carry file may **narrow** a later phase. It may **not widen** into A6 / B7 out-of-scope items without going back and amending the earlier phase.

---

## Carry file

Write to `carry/<from>_to_<to>.md` at the end of each look-back.

```
# Carry <from> → <to>

## Conclusions (what we actually decided or found)
-

## Keep in <to> (still needed)
-

## Cut or defer in <to> (no longer worth the default outline)
-

## Watch (assumptions that <to> must not contradict)
-

## Must not reopen without returning to <from>
-
```

---

## Re-evaluation block (paste as step 0 of B–H)

1. Open the carry file from the previous phase. If it is missing, **stop** — the prior look-back did not finish.
2. Re-read frozen intent (one minute).
3. Diff the default outline for *this* phase against the carry file.
4. Write `carry/<this>_scoped.md` (short): what this phase will actually do; what it will skip and why.
5. Only then start the numbered work items, using the scoped plan as the real checklist.

If the scoped plan adds something the default outline never had: that is a **framed amendment** — update the prior phase (or A/B7), re-run that look-back, then continue. Do not smuggle scope in step 4.
