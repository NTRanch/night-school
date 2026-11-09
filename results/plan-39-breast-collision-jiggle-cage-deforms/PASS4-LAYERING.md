# Plan 39 — Pass 4: Application Record (jiggle layer over the Plan 01 loop)

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on
  primo, scripted (one heavy job at a time; file-mediated detached
  runs, prefix `ns39-`). Nothing audible.
- **Pass 4 statement of the plan:** apply the distilled technique
  (TECHNIQUE.md) to real estate work and gate it expected-vs-seen.
  Two applications are of record:
  1. **The TF-game pilot application** (executed under D-1044,
     PILOT-REPORT §3): the §5.2 keyed cage + Mesh Deform beat on
     Prima's rig as the directed-beat mechanism for the TF entry's
     stage moments (composure → crack → surrender). Gate read
     there: determinism PASS, motion PASS numerically, agent read
     PARTIAL in stills; the outfit-deform gap it named was cured
     fleet-wide by the conforming-fix step (Standard §5.2 outfit
     pairs landed ×6). Its follow-up — the true-stack bake
     question — is closed by BAKE-DETERMINISM.md (companion to
     this record): bake bit-deterministic, verbatim stack
     divergent, keyed route confirmed as the route of record.
  2. **The D-1 layering application (this record):** the same
     §5.2 beat layered over the Plan 01 two-body contact loop
     (Prima = Follower, Yui = Leader), producing the D-1 stack's
     two-body + jiggle state. Gates below are **agent reads**;
     the Owner's eye verdicts are queued in §5.

## 1. The build (script `work/layer_loop.py`)

Base: the Plan 01 Pass 3 scene (`runs/plan-01/rebuild/scene/
scene.blend`, sha256 `0bcd3bcd…`, hash-verified on primo) — opened,
layered, saved as a new scene; the base file and the fleet files
were never modified. Both girls' conformed cages were already in
the scene; all **12 Mesh Deform binds read back `is_bound =
true`** (Body + Outfit + OutfitEnd × 2 girls × 2 sides,
`layer/runA/records/layer_record.json: mesh_deform_binds`).

**Beat (§5.2 of record):** `Bounce` shape key per cage, peak
**L 1.0 / R 0.85**, settle **0.30 × amp**, rest 0 — keyed as a
period-78 key set spanning samples 0–78 with equal endpoints
(the wrapped tail value), LINEAR interpolation, CYCLES fcurve
modifiers — the fleet's loop form, repeating over the scene's
0–234 range. Bust at canon **m = 1.0** (no `Body_Bust_Size`
change).

**Phasing (Plan 01 sheet T-16, per PASS3-REBUILD §5 + the
coordinator's follower-phasing ruling):** the beat fires off the
Contact cycle, phased per girl —

| Girl | Role | Beat peak | Settle (0.30×) | Rest | Key set (frame, normalised) |
|---|---|---|---|---|---|
| Yui | Leader — beats off her own motion | **38** (Contact) | 53 | 83 ≡ sample 5 | (0, 0.05) (5, 0) (23, 0) (38, 1) (53, 0.30) (78, 0.05) |
| Prima | Follower — beats off her reaction phase | **45** (her reaction peak) | 60 | 90 ≡ sample 12 | (0, 0.12) (12, 0) (30, 0) (45, 1) (60, 0.30) (78, 0.12) |

Sampled readback (layer record `bounce_sampled`, both runs):
Prima L = 0.5333 at 38 (mid-rise), **1.0 at 45**, 0.30 at 60,
0.12 at the wrap; Yui L = **1.0 at 38**, 0.6733 at 45 (decay),
0.30 at 53, 0.05 at the wrap; R sides peak at 0.85 exactly
(`bounce_max`: L 1.0 / R 0.85, both girls). The §5.2 window the
Plan 01 build left intact (`Bounce` = 0.0 at every sample there)
is now filled, on the phase map PASS3 recorded for it.

## 2. Gate measurements (all from `layer/runA/records/layer_record.json`)

**Displacement** — layered vs Bounce = 0 reference at the same
sample and pose, over each girl's §5.1.3 chest band (Prima 236
verts, z 1.10302–1.39581; Yui 224 verts, z 1.01185–1.28050),
canon bust m = 1.0:

| Girl @ sample | Max | Mean | Verts > 5 mm |
|---|---|---|---|
| **Prima @ 45 (her peak)** | **15.203 mm** | **5.343 mm** | 100 / 236 |
| **Yui @ 38 (her peak)** | **15.025 mm** | **5.429 mm** | 97 / 224 |
| Prima @ 38 (mid-rise, cross-check) | 8.108 mm | 2.850 mm | 26 / 236 |
| Yui @ 45 (decay, cross-check) | 10.117 mm | 3.656 mm | 58 / 224 |

The own-peak numbers land on the conformed canon beat's register
measured by the conforming-fix gate on the solo rigs (Prima
15.2 / 5.3, 100/236; Yui 15.0 / 5.4, 97/224 — FIX-REPORT §3):
the beat survives transplantation into the posed two-body loop
at full amplitude, and the cross-phase samples show the phasing
in the numbers (Prima at half amplitude while Yui peaks; Yui
decayed while Prima peaks).

**Determinism** — two independent builds (separate Blender
processes, identical base scene, identical script):

- `layer_record.json` **byte-identical** across runs (sha256
  `56b0af25…`); canonical scene-data fingerprint
  `de4a627b2b454a9c…` equal.
- **Decoded-pixel hashes identical** at all four evidence
  frames: f0000 `54066a8e…`, **f0038 `090365e8…`** (Yui peak),
  **f0045 `ebbeced7…`** (Prima peak), f0060 `b750f541…`.
- The saved `.blend` files' bytes differ between runs
  (`8c754671…` vs `29be80ac…`) — the same volatility class as
  the pilot's PNG finding (save-session data in the container);
  the determinism objects of record are the scene-data
  fingerprint and the pixel hashes above, not container bytes.

**Contact set** — re-measured on the layered build with the
Plan 01 build's own test (pelvis-box verts, two-axis ray parity,
nearest-surface depth ≤ 15 mm) at its recorded worst samples:

| Sample | Layered max | Plan 01 record | Delta |
|---|---|---|---|
| 61 | 5.391 mm | 5.391 mm | 0.000 |
| 62 | 5.4172 mm | 5.4172 mm | 0.000 |
| 63 | 5.4424 mm | 5.4424 mm | 0.000 |
| **64** | **5.4582 mm** | **5.4582 mm** | **0.000** |
| 65 | 5.4218 mm | 5.4218 mm | 0.000 |
| 66 | 4.0174 mm | 4.0174 mm | 0.000 |
| 67 | 5.3812 mm | 5.3812 mm | 0.000 |

**Delta vs the 5.46 mm record: 0.000 mm.** The jiggle layer
introduces no new interpenetration — expected (the Mesh Deform
masks cover only the chest band) and now proven per-sample, not
assumed. (Samples 38 / 45 also match the record exactly:
1.0434 / 3.1743 mm.) The Plan 01 residual itself is unchanged
and remains as PASS3-REBUILD §2 reported it — a subsurface
graze in the recovery half, with its E-4 caveat for closer
cameras.

## 3. What ships (the D-1 two-body + jiggle state)

- `layer/runA/scene/scene.blend` — the layered authoring scene
  (Plan 01 scene + Bounce beats; runB's record is identical).
- `layer/clips/prima-contactloop-jiggle.clip.json` (sha256
  `5bff5c4a…`) and `yui-contactloop-jiggle.clip.json` (`98805eee…`)
  — the Plan 01 `torogao-motion-clip/1` artifacts plus a
  `jiggle_beat` section carrying each girl's period-78 Bounce
  tracks (per §7.2.6, cage keys are authored in girl-independent
  beat values). Original clip content verified unchanged:
  deep-equality against the Plan 01 clips with the added
  section removed, asserted at build time; skeleton defs and
  channel lists carried over byte-identical alongside.
- `layer/runA/frames/` — evidence frames f0000 / f0038 / f0045 /
  f0060 (EEVEE 960×540, the Plan 01 evidence camera, bodies-only
  as in Pass 3 so the contact set stays visible).

## 4. Expected-vs-seen (benchmark written from the Pass 3 record's terms)

SHOULD be seen: the loop unchanged except chest-band secondary
motion; each girl's beat peaking on her own phase (Yui at
Contact 38, Prima at her reaction peak 45); no new contact-set
penetration; two builds indistinguishable.

| # | Item | Agent read |
|---|---|---|
| 1 | Beat present at full register in loop context | **PASS** — own-peak displacement 15.2 / 15.0 mm max, matching the solo canon-beat gate (§2) |
| 2 | Follower phasing respected (Prima peaks at 45, not 38) | **PASS** — sampled Bounce curves + cross-phase displacement (§1, §2) |
| 3 | Determinism of the layered build | **PASS** — records byte-identical; pixel hashes identical at 0/38/45/60 (§2) |
| 4 | No new interpenetration | **PASS** — delta 0.000 mm at every re-measured sample (§2) |
| 5 | Beat reads visually at loop framing | **QUEUED FOR THE OWNER'S EYE** — frames f0038/f0045 in `layer/runA/frames/`; at 960×540 full-scene framing the chest band is small and the pilot's own read of this amplitude class was "subtle in stills" — the register verdict is the Owner's (eye item L-1) |

## 5. Eye items queued for the Owner

- **L-1 (new):** the layered loop's beat peaks — `layer/runA/
  frames/f_0038.png` (Yui peak) and `f_0045.png` (Prima peak),
  against their Plan 01 counterparts in
  `runs/plan-01/rebuild/frames/`. Does the §5.2 amplitude
  register read at two-body framing, or should the D-1
  demonstrator push it (the pilot's open amplitude question,
  now in loop context)?
- **L-2 (re-queued, still unruled):** the Plan 39 pilot frames
  eye item from PILOT-REPORT §6 — front/side rest-vs-peak
  stills in `jam-entries-20261104/validation/plan-39-pilot/`:
  is the keyed-cage beat's amplitude the right register for
  directed beats, or push further? (The cloth alternative this
  item waited on is now closed by BAKE-DETERMINISM.md: the
  baked-cloth route is deterministic but divergent as
  parameterized — it is not a register option until tuned.)
- Plan 01's own eye items E-1…E-4 (PASS3-REBUILD §6) remain
  queued and are unaffected by this layer; E-4's warning
  stands: a closer D-1 camera re-opens the 5.4582 mm
  recovery-half residual, which this layer neither worsened
  nor cured (delta 0.000 mm).

## 6. Artifacts

`layer/runA/` (scene, frames, records) · `layer/runB/records/`
(identical record) · `layer/clips/` (layered clips + carried
defs) · `work/layer_loop.py` · primo detach log `ns39-layer`.
Companion record: `BAKE-DETERMINISM.md` (experiment A).
