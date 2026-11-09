# D-1 Stage 1 — §7 Retarget Proof (the §7.4 verification, executed)

- **Date:** 2026-11-06 · **Standard:** `SIX-GIRL-STANDARD.md` §7 (with
  errata E-1…E-5) · **Route:** Blender 5.2.3 LTS headless on primo,
  scripted; clip-space retarget in pure Python (`scripts/retarget.py`).
- **Verdict: §7 is PROVEN** — with two recorded exceptions, both in the
  fluid layer's late window, neither in the retarget itself (§6 below).
  Before this run §7 conformance stood UNVERIFIED fleet-wide ("a
  cross-girl retarget has never been executed", AUDIT §7). It has now
  been executed for **14 clip applications** (7 castings × follower +
  leader parts) covering **all six girls in the follower role and
  three girls (Prima, Yui, Alma) in the leader role**, each proven in
  clip space and in scene space.

## 1. What was retargeted

The layered ingredient clips of record (`runs/plan-39/layer/clips/`,
hash-verified pre/post: prima jiggle clip sha256 `5bff5c4a…`, yui
`98805eee…`) carry the Plan 01 loop (49 body tracks + face tracks,
78 samples @ 60 Hz) plus the Plan 39 `jiggle_beat` section. Per §7.2,
for each casting: bind by name against the target girl's skeleton def
(`anim-arc/<girl>-skeleton.json`, 54 bones) and spec morph list (36);
drop `Fac_Pupil_Heart` for troupe targets; scale Hips translation
keys by `ZS_target / ZS_authoring`; rotations and morph weights
verbatim; jiggle beat re-derived per **role** (follower wave peak 45,
leader wave peak 38 — girl-independent beat values, §7.2.6).
Artifacts: `clips/` (14 retargeted clips) +
`clips/retarget-proof-data.json`.

## 2. Bone-track completeness (§7.4, per application)

Every application: **49/49 body tracks resolve** against the target's
54-bone def; the unkeyed set is exactly the §2.2 practice set
(`Spine2`, both `Shoulder`s, both `Hand`s) — no missing, no extra, no
silently dropped track (the retarget asserts and would have failed
loudly). Face tracks resolve against all 36 morphs on every girl.

| Casting | Part → girl | ZS ratio | Governance |
|---|---|---|---|
| 01 | follower → Prima / leader → Yui | 1.0000 / 1.0000 | — (identity application; output clips byte-identical to the ingredients, §5) |
| 02 | follower → Yui / leader → Prima | 0.909096 / 1.099993 | — |
| 03 | follower → Alma / leader → Prima | 1.103030 / 1.099993 | — |
| 04 | follower → Sloane / leader → Prima | 1.018185 / 1.099993 | **`Fac_Pupil_Heart` dropped** |
| 05 | follower → Lux / leader → Prima | 1.000000 / 1.099993 | **`Fac_Pupil_Heart` dropped** |
| 06 | follower → Piper / leader → Prima | 1.030301 / 1.099993 | **`Fac_Pupil_Heart` dropped** |
| 07 (swap) | follower → Prima / leader → Alma | 1.000000 / 1.213326 | — |

Scene-space confirmation: the builds' exported clips carry the same
governance (build records `face_channels`: troupe followers key
exactly 3 face channels — `Fac_Ebr_Relax`, `Fac_Eye_HalfClose`,
`Fac_Mth_Aa`; trio followers key 4, incl. `Fac_Pupil_Heart`).

## 3. Seam exactness (§7.4)

- **Clip space:** every track of every retargeted clip evaluated at
  frame 0 vs 78 — rotation, Hips translation, face, and beat deltas
  all **0.000000** (`retarget-proof-data.json: seam_clip_space`).
- **Scene space:** per build, evaluated pose deltas frame 0 vs 78
  over all **108 bones** (54 × 2 girls): **max translation 0.000 mm,
  max rotation 0.000°** in all 9 builds (build records `seam`).

## 4. Determinism (§7.4)

- **Clip space:** each retarget run twice from independent loads —
  canonical-JSON sha256 identical for all 14 clips.
- **Scene space:** each casting built **twice in independent Blender
  processes** (runA/runB, `builds/<casting>/run{A,B}/records/
  build_record.json`): scene-data fingerprints equal, exported clip
  sha256 sets equal, and **decoded-pixel hashes equal at gated frames
  0/38/45 (and 60)** for **all 9 builds** (7 castings + 2 Alma
  extremes). One methodological note: an early runB in a reduced
  "light" measurement mode produced different pixels — traced to the
  T-13 cure integrating penetration depths over fewer samples, i.e.
  a different build, not nondeterminism; all reported runBs are
  full-mode builds with identical inputs.
- **Fluid (control casting 01, the §7.4 extension to the layer):**
  two independent bakes (fluidA/fluidB) — particle counts and mesh
  verts identical at every measured frame (33/173/316/410/467;
  156/192/210/214/220 through the gated window), decoded-pixel
  hashes identical at f34/f38/f45/f90. Against Plan 06's own pair,
  my bakes land on its "B" late-slump branch (f60 218, f90 302 verts
  vs mainA2's 214/304) — the documented ~1–2% late divergence class,
  reproduced, not new.

## 5. The control casting closes the loop

Casting 01 (Prima follows, Yui leads — the ingredient casting) built
through the retarget pipeline reproduces the ingredient records
**exactly**: layered clips byte-identical to the Plan 39 artifacts
(prima `5bff5c4a…`, yui `98805eee…`; base clips `bab815bb…` /
`6089cc69…`); layered pixel hashes equal to PASS4-LAYERING's
(f0000 `54066a8e…`, f0038 `090365e8…`, f0045 `ebbeced7…`, f0060
`b750f541…`); keyed drift 0.3933 mm (record 0.393); post-cure
penetration 5.4582 mm (record 5.4582); jiggle 15.203 / 15.025 mm
(record 15.203 / 15.025); fluid f38 pixel hash `3bb28db5…` equal to
Plan 06's gated-window hash. The pipeline that produced the fleet
numbers is therefore the pipeline of record, not a re-implementation
that happens to agree.

## 6. Exceptions (the "with-exceptions" list)

1. **Fluid late-window interior event, casting 02 only** (Yui
   follows, Prima leads): interior count is **0 at every gated frame**
   (34/38/42/45/47/48) and at f60/f78, but **35 of 486 particles read
   inside Prima_Body at f90** — the slumped coating tunnelling into
   the emitting body late, outside the gated window. All other
   castings read 0 at every measured frame including f90. Recorded
   per-girl in DEMONSTRATOR-RECORD §4; the gated gate passes, the
   late window is reported, not averaged away.
2. **Fluid determinism is gated-window-scoped** (inherited from Plan
   06, re-confirmed): mesh-vert counts diverge ~1–2% between
   independent bakes in the late slump (my control pair agreed with
   each other at all measured frames but sits on the alternate
   branch vs Plan 06's mainA2 at f60/f90). Determinism claims for
   the fluid layer are valid for the gated emission phase only —
   exactly the scope Plan 06 recorded.

No exception touches the retarget procedure itself: completeness,
governance, seam, and replay determinism hold for every application.

## 7. Identity invariance (§7.4 static control)

Method (stated honestly, per the brief): the loop pose is never
neutral, so each build renders each girl **solo at rest, canon face,
the build's bust m, in the stack scene** (partner hidden) before any
posing; a reference render of her **pristine conformed blend alone**
is produced by the same set/camera code (`scripts/identity_ref.py`).
Decoded-pixel hashes must match. They do, for **every girl in every
build** (14/14 role instances at canon + Alma at m 0.50/1.50):
e.g. Prima `d05222a3…`, Yui `ff179a5b…`, Alma `1d8c7593…`, Sloane
`44845646…`, Lux `1638e356…`, Piper `0e4591b5…` (in-stack ==
reference; gate-table `identity`). The stack copy of each rig is
pixel-identical to her conformed rig at neutral — no identity drift
was introduced by retargeting, and the fleet files themselves are
hash-identical before/after all work (post-work sweep in
DEMONSTRATOR-RECORD §7).

## 8. Proposed standard note (standard NOT edited)

§7.4's gate list should name the fluid layer's determinism scope
explicitly (gated window) alongside the pixel-hash rule, since the
demonstrator's fluid bakes confirm Plan 06's scoping on a second
scene pair. Proposed as a note for the coordinator; no text changed
by this run.
