# Bloch candidate — Night School Plan 10

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 10 study run, 2026-11-06
  (`~/workspace/night-school-20261105/runs/plan-10/`)
- artefact of record: `stage/fcurve_exercises.py` +
  `stage/measurements.json` in the run dir above (copies in
  `repo/results/plan-10-animation-bootcamp-1/`); revision =
  the run's files as of 2026-11-06, uncommitted per brief.

## Candidate 1 — Interpolation manufactures overshoot nobody keyed

**Lesson:** Smooth (Automatic/Auto-Clamped-family) interpolation
crosses a key's value after a settle key when the preceding
segment is still moving: in the estate-form evaluator, a
12-frame gesture whose keys never exceed rest (0) still
produced a **+0.002222 excursion past rest at frame 10**,
decaying by frame 12 — an overshoot with no author. Any baked
loop gated only on its keys can therefore ship motion nobody
keyed.

**Mechanism / evidence:** the auto tangent at a flat key is
computed from its neighbours; after a moving segment the
tangent is non-zero, so the curve leaves the key still moving
and comes back. Measured in `stage/fcurve_exercises.py`
exercise 2 (auto-only run: settle_overshoot_past_rest
0.002222; keys and drop identical in both runs, so the
excursion is attributable to the interpolation alone —
attribution row: component = auto tangent at the settle key /
change = none (control run) / observed difference = +0.002222
past rest / verdict = reproduced).

**Transferable rule:** loop gates audit the *evaluated curve*
at settle keys, not just key values: excursion past a settle
key is a defect class with a metric (absolute excursion, and
its ratio to the preceding segment's travel), whether or not
any key crosses. Feature-overshoot stays deliberate and
keyed, never an interpolation side-effect.

## Candidate 2 — A plan's premise is a claim (Plan 10 instance)

**Lesson:** Plan 10 was written (from title + category
listing) as a principles-of-animation lecture with set
exercises. The video is a Blender *tooling* lesson (Timeline /
Dope Sheet / Graph Editor) taught on a production loop; the
principles exist only as curve-shape consequences. The
creator's own page description stated the real content and was
only read against the premise at intake.

**Mechanism / evidence:** INTAKE.md records the disagreement
before viewing; OBSERVATION.md scores it. Same shape as the
Plan 35 candidate — filed as a second instance, not a
duplicate: the pattern is now 2-for-2 on plans whose intake
trusted the shelf listing, so the rule "read the page
description against the plan premise at intake" has earned
promotion candidacy.

## Friction answer (D-1064)

Yes — three items the next agent would also hit:
1. The sandbox `/tmp` is a 512 MB tmpfs; a 555 MB capture's
   segment set fills it mid-transfer (observed: "No space
   left on device" during scp). Night School capture work
   should stage in the workspace from the start.
2. Backgrounded scp transfers die silently with their exec
   session and restart from zero; the primo pin needed two
   attempts. Large transfers want the file-mediated detach
   pattern with size checks per chunk (the segment route is
   the reliable form — primo sub-ranges landed in ~90 s).
3. Mid-segment connection resets on this host restart the
   whole segment under a plain retry loop (segments 0/2 reset
   three times); ranged resume (`curl -C -`) or smaller
   segments (≤ 20 MB) are the fix — the 17 MB sub-range run
   had zero resets.
