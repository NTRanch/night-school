# BLOCH CANDIDATE — Plan 28: headhack seam practice, audited against its own source

- **origin_lane:** ntranch
- **content_label:** nsfw
- **evidence:** `runs/plan-28/` (this run): INTAKE.md (ID-404 +
  title-exact substitution evidence), OBSERVATION.md (102-frame
  grid + 225 dense frames + 2 transcript windows), TECHNIQUE.md,
  PASS3-REBUILD.md, `rebuild/measures.json`,
  `rebuild/build_record.json`, `rebuild/headhack_both.blend`.
- **artefact:** `runs/plan-28/rebuild/headhack_both.blend`
  (also copied to `repo/results/plan-28-headhack-models/rebuild/`)
  — both joins on Alma→Prima, Blender 5.2.3, built by
  `rebuild/build_headhack.py` (sha256 `c85cf6ff…`) + bend-tested
  by `rebuild/bend_test.py` (`71638ffe…`); primo detach runs
  `ns28-build1` / `ns28-bend1` / `ns28-det`, logs in
  `~/.local/share/pax/detach/`. Revision: this run, 2026-11-06;
  no prior revision exists.

## Lesson 1 (technique): a headhack weld has two independent choices — price them separately

The seam everyone argues about ("merge / bridge / shrinkwrap")
is not one choice but two: **(a) correspondence** — how ring
points are made to coincide (global scale of the donor vs
per-point snapping), and **(b) weight provenance** — whose field
the seam deforms under (the body's template field vs the
donor's own field, renamed). The source tutorial (Anime Nyan,
3644780) welds exactly like the estate does (Ctrl+J + Merge by
Distance); its measured deficit at 45° neck flexion — weld-edge
strain 0.613 mm max vs the estate's 0.007, kink concentrated
*above* the weld, shading normal-step excursion 36–39° vs
8–11° — comes from (a)+(b), not from the weld. And its win is
equally specific: per-point snapping preserves the donor head's
proportions exactly where global scaling quietly resized the
head −8.6%/−8.9%. **Rule: for any graft, name both choices and
their prices in the record; never let "welded" read as "equal".**

## Lesson 2 (failure class): stray donor bones after armature fusion

The source tutorial's final defect was not in the mesh at all:
one leftover donor bone (`joint_torso_C_01`, plus donor
clavicles) inside the manually fused rig made the neck deform
"all screwed up" until deleted. Any fusion route (add-on or
manual Ctrl+J + reparent) needs a **post-fusion stray-bone
sweep**: enumerate donor-named bones that drive no graft
vertices and delete or quarantine them before the first pose
check. (Proposal filed as an amendment in PASS4; the skill is
not edited by this run.)

## Lesson 3 (measurement): screen-first has a floor — sub-grid operations need the transcript before distillation

This run's frame-only first read classified the join as
"overlap + Ctrl+J, unwelded" — wrong. The two operations that
define the method (per-point Snap-to-Active; Merge by Distance
after the join) happen *between* 60 s grid frames and are
invisible in them; the narration names both. A first build of
the wrong method was completed and discarded. **Rule adopted:
when an operation class is load-bearing for Pass 2 and the
grid cannot show it, the transcript window covering it is a
Pass 1 dependency, not a Pass 3 correction.** (Census-is-a-screen
stands — the screen governs what is *shown*; narration governs
what was *done* between frames.)

## Friction log (D-1064 clause — incl. silent workarounds in successful runs)

1. **Plan ID 404.** The commissioned source ID (3655211) does
   not exist on the site (both egress routes, site search
   parsed). The title-exact substitute (3644780) was adopted on
   documented evidence (description = the estate skill's asset
   inventory). Cost: ~15 min of route-checking. The silent-
   workaround risk was proceeding without flagging; it is
   flagged in INTAKE, MANIFEST, the plan copy, and the report.
2. **Site 503s from the sandbox route.** rule34video returned
   its own database-error 503 to sandbox curl while primo curl
   succeeded — route-dependent site health, not a block. The
   primo route is the standing one; the sandbox failure cost
   two retries before switching.
3. **`find /` on primo.** A model-file search ran ~13 min
   under load and held an SSH session; the answer was in
   `/usr/share/whisper.cpp-model-*` all along. Use targeted
   paths; never `find /` on a saturated box.
4. **Boundary-loop trap (fleet geometry).** The fleet Body
   mesh's neck weld is a true merge — it has *no* boundary
   loop (and an inner folded rim), so a boundary-based split
   silently harvested wrist/hand boundaries (212 verts) and
   produced a garbage first build (ring radius 216 mm,
   scale 4.84). Caught because the numbers were absurd, not by
   any check. The containment split (faces fully on one side)
   + a z-gated loop fixed it. Sweep harnesses should sanity-
   gate derived quantities (ring radius vs spec) before use.
5. **Render contamination.** The first bend renders included
   the un-deleted source bodies (Prima_Body upright + Alma
   head swinging as a "blob") and briefly read as a weight
   catastrophe in Method A. It was a scene-hygiene bug in my
   own build (sources not removed before save). Silent-
   workaround risk: "explaining" the blob instead of hunting
   it. Rule: rebuild scenes ship with ONLY the artefacts under
   gate + their rig.
6. **Whisper throughput.** Even base.en took ~2× the naive
   estimate behind ~10 sibling large-v3-turbo jobs (load
   ≈ 30). Bounded windows (join + weights/fusion = 2,269 s of
   6,169 s) were chosen *because* of the queue; the untranscribed
   windows are named in PASS4 residuals rather than silently
   skipped.
7. **In-flight byte counts.** The 1080p download's partial
   sizes (57 MB → 686 MB → 2.2 GB) were never recorded as
   facts; the pin waited for the `.done` file + sha256 +
   Content-Length agreement (2,303,508,423 B on both).

## Per-edit attribution (fix reports)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| `build_headhack.split_by_face_z` | face-centroid split → containment split (faces fully one side; band faces drop from both) | boundary loop at the neck exists (24 verts, r 48.02 mm); prior run's loop was wrist verts (r 216 mm) | clean (sole change between the failed and sane builds) |
| `build_headhack.boundary_loop` | added z-gate (±20 mm of cut) after the 212-vert harvest | loop = the weld ring only, both parts | clean |
| Method A construction (whole) | overlap + unwelded + profile-repaint → snap-to-active + Ctrl+J + Merge-by-Distance + donor weights kept + 3× smooth | A became the transcript-verified method; measures changed class (weld strain became defined; kink moved above the weld) | **confounded** (geometry, weld, and weight provenance changed together — unavoidable: the first A was a different method, not a variant; the correction is recorded in PASS3, and no A-v1 numbers are reported) |
| `bend_test` measures | seam-pair distance (both rings Neck-bound: change ≈ 0) → corridor ladder (kink / radius step / normal step) + weld-edge strain | posed-vs-rest discrimination appears (A kink 7.207 vs B 5.041 mm at flexion); pair distance retained as a secondary line | clean |
| build scene hygiene | source bodies deleted before save | renders show only the join under gate; the "blob" artefact disappears | clean |
| `build_headhack` DEFORM scope | constant re-added at module level after the A-section rewrite dropped it | build completes (NameError at Method B weights) | clean |
