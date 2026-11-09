# Plan 06 — Pass 3 Rebuild Record (clean-room, sheet only)

- **Date:** 2026-11-06. **Route:** Blender 5.2.3 LTS, Mantaflow
  FLIP, scripted and headless on primo. **Video closed
  throughout** — the only technique source is the gated sheet
  `TECHNIQUE.md` (Adopt 3 · Adapt 18 · Reject 4) under its four
  coordinator rulings.
- **What was built:** the fluid layer over the Plan 39 layered
  two-body stack (Plan 01 loop + §5.2 jiggle beat), on the
  LOCKED Plan 07 physical preset. This completes the D-1
  ingredient set. Layer data of record:
  `rebuild/fluid-layer-record.json`.
- **Headline result, stated plainly:** the layer is gated,
  beat-relative, interior-clean, and round-trips exactly —
  but in this shot's geometry the aimed emission does **not**
  fly as a free jet. It extrudes into the contact interface,
  coats, and slumps. The free-jet form of the aim claim
  (C-17) is REFUTED in-pocket and REPRODUCED in open
  geometry; the mechanism hunt behind that verdict is §5.

---

## 1. Build summary

| Item | Value (artifact) |
|---|---|
| Input scene | `runs/plan-39/layer/runA/scene/scene.blend`, sha256 `8c7546710515de696343c870636911006d3194a9c6845ef0b63a30d9c31a0ff7`, verified identical before and after all work (§6c) |
| Pairing (ruling 1) | Emitter = Yui `Anchor_Fluid_Pelvis.001` (Leader, emitting body); aim = Prima `Anchor_Fluid_Pelvis` (receiving body) |
| Preset (ruling 2) | Plan 07 preset unchanged; readback `viscosity_value` 0.05632, `surface_tension` 10.0, FLIP ratio 0.97, particle radius 1.43, mesh particle radius 2.933 (`mainA2/run_record.json`) |
| Domain | dims (0.80, 0.95, 0.74) m, centre (0, 0.025, 0.65); resolution_max 50 → cell 0.019 m; anchor min margin 0.3181 m |
| Emitter | UV sphere r = 0.024 m at anchor + aim×0.012 m, parented to the anchor empty (data-API parent; `parent_set` operator silently failed headless — first-run defect, caught by readback, fixed) |
| Gate (T-19) | `use_inflow` ON exactly while `flow` > 0.1; on frame 34, off 48 (Contact 38) |
| Bake | main variant 62.18 s, 90 frames (`mainA2/run_record.json`) |
| Tier 2 handoff | `rebuild/mainA2/ns06_mainA2_fluidmesh.abc`, 2,217,813 B, sha256 `614a6f7097beda5ebd8667daebc4e193470d3b757005a06e60bfcbdb5643dde7` |
| Layered-with-fluid scene | `rebuild/scene/mainA2_baked.blend`, 1,049,142 B |

Build scripts: `rebuild/scripts/ns06_sim.py` (layer build +
bake), `ns06_measure.py` (per-frame particle/interior/mesh
measurement), `ns06_render.py`, `ns06_abc.py` (Tier 2 export),
`ns06_abc_probe.py` (round-trip probe), `ns06_pixelhash.py`
(decoded-pixel hashes, Plan 07's tool), `ns06_velprobe*.py`
(route probes, §5).

## 2. Translation table (sheet → estate build)

| Entry | Estate form as built | Status |
|---|---|---|
| T-01 Adapt | Collider/proxy work on the evaluated rest/frame-0 configuration; all fluid timing authored beat-relative to Contact 38 (no shifted absolutes) | Built |
| T-02 Adapt | Scripted census: only body meshes + Platform/Cushion/Floor enter the sim; outfits/hair/cages `hide_render`, never effectors; collider-source assertion in the build | Built |
| T-03 Adapt | Direction reversed per the sheet: Alembic is the Tier 2 **output** (mesh-only, frames 1–90, scale 1.000); the sim consumes evaluated geometry from the depsgraph in-scene | Built |
| T-04 Adapt | Emitter at the named anchor empty, parented so it rides the animation; collision exclusion as an estate clause: emitting-side effector proxy with a 0.055 m patch (13 faces) around the anchor; receiving body unpatched | Built |
| T-05 Adapt | Aim = two named evaluated points (emitter anchor, aim anchor), differenced in the build script; no marker furniture, no point indices | Built |
| T-06 Adapt | Separation by name throughout; the layer's emitter tracks are their own record section (`fluid-layer-record.json`), cheaply re-authorable without touching body data | Built |
| T-07 Adapt | `v = normalize(p1 − p0) × flow` written as the flow object's `velocity_coord`. **Estate deviation, measured:** Mantaflow samples inflow velocity **once at bake start**, so per-frame re-evaluation is a silent no-op in-route; the shipped form evaluates aim at the Contact beat and holds it static — (0, −1.99853, 0.07656) at peak. Aim direction spread across the window ≤ ~5.2°, so the static hold costs little direction fidelity. The jet dynamics themselves: see §5 | Built, with deviation |
| T-08 Adapt | One named scalar channel `flow` per emitter in the layer data; keys, gate and solver read it and nothing else does. Session values 0.68/4.05 not carried; estate peak authored 2.0 m/s | Built |
| T-09 Adapt | Closure as a **precondition check**, per the sheet's estate clause. **Measured deviation:** evaluated fleet bodies are not strictly closed — 3084 verts / 4302 polys, **576 edges** not used exactly twice, per girl (identical counts; `mainA2/run_record.json` closure block). No fill was applied (the taught Fill Mode is UNREADABLE 1); the build proceeded on surface-based effectors, and the interior gate (§6a) measured against the real meshes came back 0 | Built as check; deviation recorded |
| T-10 Adapt | Proxy built from the evaluated frame-0 configuration (patch selection on evaluated centres — the pose lives in the Armature modifier, so local-coord selection removes 0 faces; first attempt caught by readback). **Hand cut not taken:** shot decision, recorded — the fleet carries `Anchor_Fluid_Hand.L/.R` attach points and the D-1 shot keeps full bodies as effectors; density choice = the fleet's own evaluated mesh (no separate remesh; Max Size is UNREADABLE 6, so no taught value exists to transcribe) | Built; cut declined with reason |
| T-11 Adapt | Contract carried, machinery dropped per the sheet: the collider the solver sees is per-frame evaluated geometry of the animated meshes (Mantaflow animated effectors), produced in the run-scoped Tier 1 cache before any experiment; frame range 1–90 stated in the run record | Built |
| T-12 Adapt | Effectors deform with the animation; `surface_distance` 0.0 read back on all five effectors (Collision Radius 0 analogue); body effector subframes 2 | Built |
| T-13 Adapt | Bounds assertion: every named effector/flow object inside the domain (anchor min margin 0.3181 m); Platform/Cushion/Floor are in-domain effectors, so the "floor outside the solved world" failure class is closed by construction | Built |
| T-14 Adapt | Numerals stay behind as evidence (another solver's shot coordinates); the discipline is carried: domain extents and centre are numbers in every run record | Carried as discipline |
| T-15 Adapt | Start bound relationally: the layer starts at the named Contact beat, not a typed numeral (proven by the retime variant, §6d). Resolution: preset's resolution_max 50 at this domain gives cell 0.019 m — finer than Part 2's 0.033 working separation, per this entry's own rule (resolution chosen against the smallest surface the fluid must read: a 26–30 mm inter-body interface). This is an integration-layer choice on the sheet's rule, not a preset change; its sensitivity consequence is measured in §7. Friction 0.563 recorded as the source-side value, **not transcribed** (cross-solver, per the sheet) | Built |
| T-16 Adapt | Mantaflow INFLOW flow object at the emitter anchor sourcing continuously while gated on — the constant stream. Finding 2's narrowing carried: no Source-Smoke analogue exists or is needed in-route. Seed 7 (estate preset of record), not the source's 0 | Built |
| T-17 Adopt | Force audit: the shipped layer contains gravity + solver internals only — no force fields. (A wind-force probe was run as a route experiment, §5 V21; it is not in the layer.) | Built |
| T-18 Adapt | Flow keys beat-relative: offsets (−5, 0), (−4, 0.8), (−2, 1.6), (0, 2.0 peak), (+7, 2.0), (+9, 0.4), (+10, 0) from Contact 38. Retime gate: §6d | Built |
| T-19 Adopt | Threshold gate with dead band, implemented as keyed inflow state; proven in §6d — magnitude-0 flow with the gate held open does **not** stop sourcing | Built, proven |
| T-20 Reject | **Not built — rejection stands.** "Thousands" / "57 or so" never seeded anywhere; physical magnitudes are Plan 07's locked preset, read back in the run record | Rejection stands |
| T-21 Adapt | Ratio lineage already in the locked preset (particle radius 1.43). The particle-death defect **never occurred in-route** (particle count monotonic non-decreasing across all 90 frames; interior 0), so the fix itself is untested here; the diagnostic order (ratios before resolution) is recorded as the standing cure order, and the interior-gate cure class was held on standby, never invoked | Standing; defect absent |
| T-22 Reject (tolerance) | **The tolerance is not inherited.** The estate gate is ruling 4, measured in §6a: 0 interior at gated frames, 0 loop-wide. The chain result itself stands as outcome evidence via §6/Pass 4 | Rejection stands; gate enforced |
| T-23 Adopt | Meshing scale read from the baked domain by reference (preset mesh particle radius 2.933 against resolution 50, stated in the run record); no balloon at any frame — mesh bbox stays body-scale (max span 0.153 m, f90) | Built |
| T-24 Reject (as video technique) | **Not built from the video — rejection stands.** The return trip is estate design per ruling 3 (§3) | Rejection stands; estate design built |
| T-25 Reject | **Not built — rejection stands.** No soft-body fluid coupling, no point-force stickiness; the T-17 force audit confirms none is present | Rejection stands |

## 3. Return trip (ruling 3 — estate design, not video technique)

Two-tier, per Plan 07's `CACHE-CONTRACT.md`:

- **Tier 1 working cache:** primo `runs/mainA2/cache`, 7.1 MB —
  `fluid_mesh_*.bobj.gz` ×90 + `fluid_data_*.vdb` ×90
  (`mainA2/artifact_sizes.txt`).
- **Tier 2 Alembic mesh:** `rebuild/mainA2/ns06_mainA2_fluidmesh.abc`,
  2,217,813 B, frames 1–90, sha256
  `614a6f7097beda5ebd8667daebc4e193470d3b757005a06e60bfcbdb5643dde7`
  (`mainA2/abc.sha256`).
- **Round-trip verification in metres** (re-import probe,
  `mainA2/abc_probe.log`, vs sim-side `mainA2/measurements.json`):
  verts and bounding boxes **identical** at every probed frame —
  f38: 192 verts, bbox y [0.1409, 0.1935], z [0.5983, 0.6656];
  f45: 214 verts, bbox y [0.1445, 0.1974], z [0.6017, 0.6798];
  f90: 304 verts, bbox y [0.1214, 0.1729], z [0.5062, 0.6334].
  Scale identity in metres is verified, not assumed.

## 4. Claims scores (C-01…C-34; mechanisms scored, Houdini syntax untestable)

| Claim | Score | Evidence |
|---|---|---|
| C-01 handoff contract / no return taught | REPRODUCED (mechanism) | Evaluated-geometry-only consumption in-route; return built as estate design (§3), never attributed to the video |
| C-02 scene census (versions, 0–250, 18 poses) | UNTESTABLE-IN-ROUTE | Provenance numerals of another scene/toolchain; nothing to rebuild |
| C-03 rest-frame construction + re-based timing | REPRODUCED (mechanism, estate form) | Frame-0 proxy work; beat-relative timing (§6d retime) |
| C-04 Alembic export discipline | REPRODUCED (in reverse) | Tier 2 output ABC: explicit range, unit scale, round-trip exact (§3) |
| C-05 exclusion set | REPRODUCED | Scripted census; effector list in `mainA2/run_record.json` |
| C-06 emitter rides the emitting body; interior placement legal under exclusion | REPRODUCED | Anchor-parented emitter (parent verified by readback); emitting-side patch exclusion (13 faces) |
| C-07 two-point aim rig | REPRODUCED (mechanism) | Two named evaluated anchor points; furniture not carried, per sheet |
| C-08 util channel separate and tiny | REPRODUCED (mechanism) | Separation by name; layer data is its own record, re-authorable alone |
| C-09 versions/project path | NOT-A-TECHNIQUE | Provenance only (sheet's judgement, carried) |
| C-10 close the body first | REPRODUCED as precondition check, with measured deviation | Closure census ran; fleet bodies measure non-closed (576 non-manifold edges/girl); interior gate still 0 (§6a) |
| C-11 freeze at frame 0 for proxy construction | REPRODUCED | Patch selection on evaluated frame-0 mesh |
| C-12 hand cut | NOT BUILT — shot decision | Hands retained (fleet hand anchors; full-body effectors); reason in §2/T-10 |
| C-13 remesh density values | REPRODUCED (mechanism) | Density is a recorded choice (fleet evaluated mesh; no transcription — Max Size UNREADABLE) |
| C-14 point-deform re-animation | REPRODUCED (mechanism) | Collider follows the animation per frame (animated effectors); lattice machinery not needed in one scene |
| C-15 bake the animated collider first | REPRODUCED | Tier 1 per-variant cache precedes all experiments; range 1–90 recorded |
| C-16 split by path identity | REPRODUCED (mechanism) | Parts recovered by name everywhere; nothing was ever merged |
| C-17 aim VEX: normalized difference × flow as initial velocity | **REFUTED in this shot's geometry; REPRODUCED in open geometry** | §5: 14-variant discrimination. In-pocket, the jet is pressure-projected to a creep; in open space the same source flies at authored velocity (V1/V10) |
| C-18 normalization = absolute speed; distance-gain rejected | REPRODUCED | Estate aim normalizes; anchor distance varies 0.2136–0.2267 m while authored speed stays exactly the flow value (aim table, `fluid-layer-record.json`) |
| C-19 one `cumflow` control | REPRODUCED | Single `flow` channel read by keys, gate, solver |
| C-20 named source output | REPRODUCED (form) | NS06_* naming contract throughout |
| C-21 solver-world completeness (ground inside limits) | REPRODUCED (mechanism) | Bounds assertion, anchor margin 0.3181 m; node graph itself is Houdini furniture |
| C-22 deforming surface collider, radius 0 | REPRODUCED | Animated body-mesh effectors, `surface_distance` 0.0 read back ×5 |
| C-23 solver numerals (box 3/2/3, smoothing 0.1) | UNTESTABLE-IN-ROUTE | Another solver's shot coordinates; discipline (explicit domain numbers) carried |
| C-24 creation bound relationally to scene start | REPRODUCED (mechanism, estate form) | Beat-bound start; retime +10/+10 with zero hand edits (§6d) |
| C-25 separation 0.033 / friction 0.563 pane | REPRODUCED (resolution mechanism) | Cell 0.019 m chosen against the smallest surface per the entry's rule; sensitivity in §7. Friction 0.563 **not transcribed** (cross-solver; sheet's instruction) |
| C-26 constant stream via standing source | REPRODUCED | Counts grow every gated frame (33→467, f34–47); nogate keeps growing (§6d) |
| C-27 initial push only, no continuous force | REPRODUCED as layer rule | Force audit: gravity + solver internals only. (The push's in-pocket fate is C-17's verdict, not a force added later) |
| C-28 flow keyframed, hard stop | REPRODUCED (estate form) | Beat-relative keys; measured stop exactly on the keys (§6d) |
| C-29 gate: 0 flow ≠ stop; threshold activation | REPRODUCED, proven in-route | nogate variant: 1,194 particles at f60 and still increasing vs main frozen at 467 from f48 |
| C-30 tuning magnitudes "thousands"/"57" | NOT BUILT — rejection stands (T-20) | Never seeded; locked preset readback is the evidence |
| C-31 particle-death ratio fix | UNTESTABLE-IN-ROUTE | Defect absent in-route (counts monotonic, interior 0); ratios inherited from the locked preset, fix held as standing cure order |
| C-32 accepted result, strays tolerated | NOT-A-TECHNIQUE | Outcome evidence; its tolerance is rejected (T-22) and replaced by ruling 4's measured gate |
| C-33 surfacing must read the real separation | REPRODUCED | Meshing scale by reference from the baked domain; no balloon (max mesh span 0.153 m) |
| C-34 (aim part) distance-as-gain | REPRODUCED as a rejection | Estate normalizes (see C-18); the alternative was never built |
| C-34 (extensions) soft-body push, point-force stickiness | NOT BUILT — rejection stands (T-25) | Named, never taught; none present in the layer (force audit) |

**Tallies (35 scored lines; C-34 split):** REPRODUCED **26** ·
REFUTED **1** (C-17, in-shot form; reproduced in open
geometry) · UNTESTABLE-IN-ROUTE **3** (C-02, C-23, C-31) ·
NOT BUILT — rejection stands **2** (C-30, C-34 extensions) ·
NOT BUILT — shot decision **1** (C-12) · NOT-A-TECHNIQUE **2**
(C-09, C-32).

## 5. Route findings — the velocity investigation

The build's central problem: with aim authored at 2.0 m/s,
particles in the shot were born at ≈0.05 m/s and crept, while
the gate, timing, and collision all behaved exactly as
designed. Fourteen controlled variants (probe logs on primo,
`~/.local/share/pax/ns06r/probe/`; probe scripts in
`rebuild/scripts/ns06_velprobe*.py`) discriminate the cause:

- **Open space works.** Factory probes with the same preset
  and static `velocity_coord` fly at authored velocity (V1:
  centroid travels −0.31 m; V10 at scene scale — cell 0.019 m,
  r 0.024 m source, no effectors — flies). Adaptive timesteps
  innocent (V6); low viscosity flies (V12); GEOMETRY source
  behaviour seeds nothing (V3, corroborating Plan 07 §7.3);
  coarse cell + small source seeds ≈nothing (V11).
- **Emitting-side overlap kills velocity; receiving-side
  doesn't.** V5 (both bodies as effectors) stalls; V7
  (emitting side only) stalls; V8 (receiving side only)
  **flies**. This is T-04's mechanism proven in-route and is
  why the shipped build carries the patched emitting-side
  proxy.
- **But the patch is not sufficient in-pocket.** With the
  patch, the full build still stalls; removing body effectors
  entirely flies (noPrima variant, mean velocity −0.84 m/s);
  effector subframes 0 and velocity_factor 0 change nothing
  (identical stall). Pocket probes at res 50, res 110, and
  with a 60 mm corridor and no overlaps all stall; a corridor
  wind force (V21) moves the centroid negligibly (0.229 vs
  0.237 m).
- **Small sources have a floor.** A r = 0.010 m sphere
  mid-gap seeds **zero** particles; a Ø36×6 mm disc seeds zero
  even in the factory scene. Sources under ~1.5 cells do not
  seed at all.
- **Settled conclusion:** in Mantaflow FLIP at these
  settings, an inflow jet inside a body-scale pocket —
  effector walls within ~2 cells on 3+ sides; here a
  26–30 mm inter-body corridor — is pressure-projected to a
  creep regardless of patch, subframes, velocity factor, or
  resolution. The shipped layer is therefore a gated,
  anchor-attached **contact-interface extrusion**: fluid
  extrudes into the interface during the gate window, coats
  and spreads over the receiving body, and slumps down its
  front. That is a real, gated, measurable layer — it is not
  the free jet the source video shows in its open staging.

Two further API findings, both readback-proven:
`velocity_coord` is sampled **once at bake start** (keyframing
it is a silent no-op — hence the static-at-Contact shipped
form), and headless `parent_set` can silently leave a parent
unset (hence data-API parenting + readback).

## 6. Gates

**(a) Interior-particle gate (ruling 4) — PASS, no cure
needed.** Measured per frame from sim data by two-axis ray
parity against the **real** Prima_Body / Yui_Body meshes
(`ns06_measure.py`; `mainA2/measurements.json`, all 90
frames): interior count **0 at every frame 1–90**, including
gated frames 38 / 42 / 45 (0 / 0 / 0). Loop-wide transience
is vacuous: no interior events exist, so no consecutive-pair
violation is possible. Also 0 in mainB2, sens32, retime, and
nogate measured frames. The particle-death cure class was
never invoked; pre-cure and post-cure numbers are the same
because there was nothing to cure.

**(b) Determinism — HOLDS in the gated window, BREAKS in the
late slump.** Two full builds in separate processes (mainA2 /
mainB2): particle counts identical at every measured frame;
mesh vertex counts identical through f48 (156/192/210/214/220);
decoded-pixel hashes **match at f34/f38/f45** (f38
`3bb28db5…`, both files) and **differ at f60/f78/f90**
(`mainA2/pixelhash.txt`, `mainB2/pixelhash.txt`); mesh cache
bytes identical at f38 only (sha256 `613c5a72…`,
`mainA2/cachehash_ab2.txt`); mesh verts diverge ~1–2% late
(f60 214 vs 218; f78 246 vs 250; f90 304 vs 302). Data `.vdb`
hashes differ at all frames — expected, and per Plan 07's
contract cache bytes are not the gate surface. Verdict:
determinism claims for this layer are valid for the gated
emission phase and must not be extended over the slump.

**(c) Contact-set non-interference — PASS.** The fluid layer
is additive: every input artifact's hash is unchanged after
the work (layered scene `8c754671…` re-verified at this
record's writing; Plan 39 clips and Plan 01 clips/scene
verified in the pre/post sweep). In-scene, the anchor
fingerprint recorded in `mainA2/run_record.json` matches the
pristine-input probe to <0.1 mm at frames 0/38/45/78 — the
underlying loop's measured state is untouched.

**(d) Emission timing — offset 0 samples.** Expected first
sourced frame 34, measured **34** (33 particles); expected
last increase 47, measured **47** (467 total, frozen from
f48). Counts: 33@34, 68@35, 173@38, 316@42, 410@45
(`mainA2/measurements.json`). **Gate proof (C-29):** the
nogate variant — flow magnitude 0 everywhere, gate held open
— reaches 731@40, 980@48, 1,114@55, 1,194@60 and is still
increasing where main is frozen at 467: zero magnitude does
not stop sourcing; the gate channel does. **Retime gate —
PASS:** the retime variant (Contact 38→48, zero hand edits)
sources first at **44** and last increases at **57** —
exactly +10/+10.

## 7. Resolution sensitivity (measured, per the tasking's rule)

The preset's resolution was **not** down-res'd silently; the
integration-layer choice and its consequence are both on
record. At resolution 32 (cell 0.0297 m) the same build seeds
only **20 particles total** vs **467** at resolution 50 — the
0.024 m emitter spans ~1.6 cells at res 32 and emission rate
collapses (`sens32/measurements.json`). Resolution 50 is the
floor for this emitter scale. (The coarser run also spreads
wider once meshed — f90 bbox y-span 0.153 m from 20 particles;
cited as the T-23 scale-coupling from the other side.)

## 8. Deviations and residuals (all carried, none softened)

1. C-17 free-jet form refuted in-pocket (§5) — the layer
   ships as an extrusion; whether that serves D-1 is an
   Owner/Pass-4 question, not a build claim.
2. Determinism breaks in the late slump (§6b).
3. Fleet body meshes are not strictly closed (§2/T-09) —
   measured deviation from the sheet's precondition; the
   interior gate nonetheless measures 0.
4. `velocity_coord` is bake-start-static in-route (§5) —
   per-frame aim re-evaluation is not available in this
   Mantaflow form; aim spread over the window is ≤ ~5.2°,
   so the cost is bounded and recorded.
5. Friction 0.563 not transcribed (cross-solver; C-25).

