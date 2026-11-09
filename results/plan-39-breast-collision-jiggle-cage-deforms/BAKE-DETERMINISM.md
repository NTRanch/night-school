# Plan 39 (A) — True-Stack Bake-Determinism Experiment

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on primo,
  scripted, deterministic discipline (one heavy job at a time; only
  other tenant ComfyUI :8191; file-mediated detached runs, primo
  `~/.local/share/pax/detach/`, prefix `ns39-`). Nothing audible.
- **Question (the pilot's open follow-up, TECHNIQUE.md):** the video's
  true stack — cloth on the cage driving the body via Surface Deform —
  is baked for determinism. **Do two identical bakes produce identical
  caches?**
- **Answer, plainly:** **YES — the bake is bit-deterministic.** Five
  independent bakes of a byte-identical scene produced **96/96
  bit-identical cache files** (combined sha256
  `fb6720ca40ff9d4a…` every time). **But the baked motion is a
  diverged simulation:** under the video's verbatim parameters the
  cage solver explodes by frame 3–4, so the deterministic artifact is
  **not usable jiggle**. Determinism gate: **PASS**. Viability gate:
  **FAIL** (see §3). A §5.3 status change is proposed, not made (§5).

## 1. What was built (the video's stack, TECHNIQUE.md / Standard §5.3)

Scene `bake/scene/cloth_scene.blend` (sha256 `732ba3ea…`), built by
`work/cloth_build.py` from Prima's **conformed** fleet blend
(sandbox sha256 `50dfd83c…`, hash-verified again on primo) in a
private scene copy — the fleet file was never modified. Record:
`bake/scene/build_record.json`.

- Per side (`.L` / `.R`, standard convention +X = `.L`): cage
  `PrimaCage.L/R` (56 verts, the conformed cages) gains a **Pin**
  vertex group = the flat chest-wall face (cage-local max-Y plane,
  **16 verts/side**); empty bone groups for all 54 bones; object
  parent = Armature (world transform preserved, drift < 1e-6 m);
  a **Data Transfer** modifier copies the body's vertex-group
  weights onto the cage and is **applied** from the top of the
  stack (transferred bone weights sum to 1.0 per vertex; the
  +1.0 on 16 verts is the body's own `Cage.L/R` mask group riding
  along, inert under the Armature modifier); **Armature**
  modifier; **Cloth** modifier; **Collision** modifier.
- Cloth settings (video's numbers, TECHNIQUE §4; 5.2.3 RNA mapping
  in ADDENDA.md): mass **3.0** (video range 2–4), **Pressure Scale
  (`pressure_factor`) 10,000**, pin group `Pin`, **pin stiffness
  0**, **gravity effector weight 0.5**, quality steps **5**
  (OPEN in the source; Blender default, stated here), pressure on
  with uniform pressure force 0 (no constant-inflation value is
  given by the source — OPEN). Collision on (quality 2). Point
  caches set to disk cache, frames 1–48.
- Body: the keyed route's Mesh Deform pair is removed **in this
  scene copy only**; **Surface Deform** per side
  (`CageSurface.L/R`, target = cage, mask = `Cage.L/R`) — **both
  binds `is_bound = true`**, strength 1.0, falloff 4.0 (defaults;
  the source gives no value — OPEN). Collision modifier on the
  body (estate form of the video's collision shell: the full body
  surface carries Collision; recorded as an adaptation).
- Drive (so results compare to the pilot): a skeletal beat on
  `Spine` / `Spine1` rotation X keyed on the pilot's timing grid
  at 24 fps — f1 rest, f4 wind (−5°/−3°), **f7 peak (+7°/+4°)**,
  f10 release, f13 settle (+2.5°/+1.5°), f19 rest, hold to f48;
  all keys LINEAR. The pilot keyed the cage; here the skeleton
  moves and the cloth must answer — that lag is the technique.
- Measurement band (pilot convention): body verts with z in
  [zmin + 0.66Δz, zmin + 0.84Δz] of the rest body = **236 verts**,
  z 1.10302–1.39581 m — the pilot's band exactly.

## 2. Determinism evidence (the cache is the object of the question)

Bake procedure per run: fresh Blender process opens a byte-identical
copy of the scene (copies sha256-verified, `bake/copies.sha256` on
primo), `ptcache.bake_all`, cache written to the `blendcache_*`
directory beside each copy. Cache-file hashes are used **because the
cache itself is the question**; frame comparisons use decoded-pixel
hashes as always.

| Evidence | Result | Artifact |
|---|---|---|
| Cache files per bake | 96 (2 cages × 48 frames) | `bake/runB/blendcache_cloth_scene/` (pulled copy, re-hashed in the sandbox: per-file and combined hashes match the primo record exactly) |
| Combined cache sha256, bake pair 1 (runA/runB) | `fb6720ca40ff9d4a…` = `fb6720ca40ff9d4a…`; **per-file diffs: none (96/96)** | `bake/runA/records/bake_record.json`, `bake/runB/records/bake_record.json` |
| Combined cache sha256, bake pair 2 (re-bake after the measurement-script revision) | `fb6720ca40ff9d4a…` again, both runs | primo detach `ns39-abake` second run; records overwritten in place, values read at the time |
| Fifth bake (runA2, for replay sampling) | `fb6720ca40ff9d4a…` again | `bake/runA2/bake.log` (primo), `bake/runA/replay_runA2.json` |
| Decoded-pixel hashes at f01 / f07 (drive peak) / f19 / f48, bake pair | identical per frame across runs: f01 `373aa3cc…`, f07 `1a2d020c…`, f19 `373aa3cc…`, f48 `373aa3cc…` | `bake/run{A,B}/records/bake_record.json` (`pixel_hashes`) |
| Replay determinism (two baked copies replayed in fresh processes, sequential stepping, toggle-free) | body-band + cage positions: **max positional diff 0.0 m** at every finite cell, all 48 frames; replayed per-frame totals reproduce the bake processes' own totals at all 48 frames (0 mismatches > 0.01 mm) | `bake/runB/records/replay.json`, `bake/runA/replay_runA2.json`, `bake/ref/replay.json` |
| Stabilised variant (pressure scale 1, §4) bake pair | also bit-identical: 96/96, combined `ebd1b4908ba0…`; pixel hashes identical; replay A-vs-B max diff 0.0 m, zero non-finite cells | `bake/varA/bake_record.json` (`bake/varA/` pull), `bake/var/build_record.json` |

**Verdict: the cloth route is deterministic when baked** — under
the conditions that held in every run here: same Blender build
(5.2.3 LTS), byte-identical scene file, bake executed in a fresh
process, and replay performed sequentially without touching the
cage modifiers (§6, finding R-2 — a workflow condition, not a
solver condition). The result is stronger than the minimum claim:
the solver reproduced bit-identically **even in a divergent
regime** (§3), where chaotic sensitivity would be expected to
amplify any nondeterminism.

## 3. Viability: the verbatim stack diverges on the estate cage

The cage does not jiggle under the video's parameters — it
**explodes**, live and baked alike:

- Live (unbaked) probe of the built scene (`work/live_probe.py`):
  cage L centroid is sane at f1–f2, displaced to (0.52, 0.41, 1.18)
  at **f3**, and **NaN from f4** onward. The reference scene (same
  build, no Cloth) follows the armature cleanly at every frame.
- Baked replay vs the skeletal-follow reference scene
  (`bake/ref/`, same build minus Cloth — the isolation method of
  §6): cage deviation from skeletal follow, max over verts —
  f2: **189.7 mm (L) / 757.8 mm (R)**; f3: **5,583.7 mm (L) /
  ~2.3×10¹⁵ mm (R)**; f4 onward: NaN / 10²⁰–10²² mm class.
  Non-finite coordinate cells per cloth replay: **5,400** (ref: 0).
- What the **body** receives through Surface Deform is only the
  pre-divergence residue: cloth-attributable band displacement
  (baked replay vs reference replay, same sample, same pose)
  peaks at **f7: max 3.212 mm / mean 0.283 mm, 0 of 236 band
  verts over 5 mm** — and returns to 0.001 mm whenever the drive
  rests (the modifier falls back to skeletal follow once its
  target is invalid; the body mesh itself never goes non-finite
  in the band). Total band motion at f7 is max 72.007 mm /
  mean 49.177 mm, but that is the skeletal drive itself, not
  secondary motion (the reference scene shows the same totals).

**Route comparison on the same beat, same band** (secondary
motion only — the pilot's keyed numbers are pure secondary by
construction, since its rig had no skeletal motion):

| Route | Max | Mean | Verts > 5 mm | State |
|---|---|---|---|---|
| Keyed cage + Mesh Deform (pilot, PILOT-REPORT §3) | 15.6 mm | 5.4 mm | 102 / 236 | deterministic, usable |
| Keyed cage, conformed canon beat (FIX-REPORT §3) | 15.2 mm | 5.3 mm | 100 / 236 | deterministic, usable |
| **Cloth (verbatim video parameters)** | **3.212 mm** | **0.283 mm** | **0 / 236** | **deterministic bake; sim diverged f3–f4** |

The failure implicates the parameter set on this cage, not the
mechanism: a 56-vert closed cage at quality 5 with Pressure Scale
10,000 is violently over-pressured (the source itself warns the
sim can glitch and names lowering the density as the cure), and
pin stiffness 0 gives the pinned face no anchoring stiffness in
5.2.3's solver. §4 tests the source's own fallback direction.

## 4. The source's fallback, tested (pressure scale 10,000 → 1)

One controlled variant — identical build except
`pressure_factor = 1` (the video's "lower it to 1 if other
settings glitch", applied to the pressure scale; ADDENDA.md):
scene `bake/var/cloth_scene_p1.blend`, record
`bake/var/build_record.json`; bakes `bake/varA`, `bake/varB`.

- **No explosion** (0 non-finite cells) and the bakes are again
  **bit-identical** (table in §2) — determinism survives the
  parameter change.
- But the cage now **drifts unanchored**: deviation from skeletal
  follow grows monotonically — 42.7 mm (L) at f2, ~198–207 mm at
  f8, **471.9 mm (L) / 382.5 mm (R) max by f46** — the cage
  leaves the breast entirely (pin stiffness 0 does not hold it;
  collision with the body does not retain it). The body's
  cloth-attributable response is the same residue curve as §3
  (peak max 3.212 mm / mean 0.283 mm at f7) — still no beat.

So neither the verbatim parameters nor the source's own fallback
produces usable jiggle on the estate cage. The knobs a tuning
pass must move are named by the evidence: **pin stiffness**
(0 anchors nothing in 5.2.3), **pressure scale** (10,000
diverges; 1 under-pressures), and **quality steps** (OPEN in the
source). That pass is a coordinator decision (§5), not this
experiment's scope.

## 5. What the determinism result unlocks (proposal — standard NOT edited)

§5.3 currently reserves the baked-cloth route "until the
bake-determinism experiment passes". **The determinism
precondition is now met** — with two honest qualifications the
coordinator should carry into any status change:

1. The route may be promoted only to **"determinism-proven,
   tuning-pending"**: a baked cloth cache is an admissible
   *form* of estate artifact (bit-reproducible, replay-verified),
   but no cloth *content* is admissible until a tuned parameter
   set stays finite, stays anchored, and produces a measured
   secondary beat on the estate cage.
2. The tuning pass should be gated like the keyed route's was:
   finite at every frame (0 non-finite cells), cage deviation
   bounded to the jiggle register (not metres, not drift), body
   secondary in the pilot's register class (≈15 mm max / ≈5 mm
   mean over the band), and a fresh bake pair bit-identical
   before any content use.

The keyed route (§5.2) remains the route of record for directed
beats regardless — this experiment changes nothing there, and
PASS4-LAYERING.md layers it over the Plan 01 loop.

## 6. Route findings / measurement honesty (read before citing §3)

- **R-1 — the first isolation measurement was invalid and is
  superseded.** The bake script's first revision isolated
  secondary motion by toggling the Cloth modifiers off inside
  the bake process; it read exactly 0.0 mm at every frame.
  Toggling a cloth modifier **frees the bake** in-process, so
  both passes evaluated skeletal-follow only. The §3/§4 numbers
  come from the corrected method: **separate scenes** (cloth vs
  no-cloth builds), **separate fresh processes**, sequential
  replay, no toggles. The invalid values remain visible in
  `bake/runB/records/bake_record.json` (`secondary_*` fields) —
  kept, labelled by this section, not silently replaced.
- **R-2 — replay discipline for baked caches.** A diagnostic
  pass that toggled cloth visibility in a fresh process deleted
  86 of runA's 96 cache files on disk (the bake frees itself)
  and its cold re-simulation produced the 32 m / NaN readings
  first seen there. Those readings are a harness artifact and
  are **not** cited as bake evidence anywhere in this record;
  the divergence in §3 is established independently by the live
  probe and the toggle-free replay. Rule: replay a baked scene
  sequentially, in a fresh process, and never touch its
  modifiers; measure against a separately built reference scene.
- **R-3 — Surface Deform masks cage failure at the body.** With
  its target NaN, the modifier's contribution collapses and the
  body reads as clean skeletal follow (pixel hashes at rest
  frames equal the rest pose exactly). A body-level render gate
  alone would have called this scene healthy; the cage-level
  measurement is what caught the divergence. Any future cloth
  gate must measure the cage, not only the body.

## 7. Eye items

- **None for the cloth route** — there are no usable cloth
  frames to judge (the cage diverged; body frames show only the
  skeletal drive, `bake/runB/frames/`). The Owner's eye is not
  asked to rule on a failed sim.
- The pilot frames eye item from PILOT-REPORT §6 (keyed-route
  amplitude register) is **still unruled** and is re-queued in
  PASS4-LAYERING.md with this run's layered-loop frames.

## 8. Artifacts

`bake/scene/` (built cloth scene + build record) · `bake/runA/`,
`bake/runB/` (bake records; runB also carries the full pulled
`blendcache_cloth_scene/` — 96 files, sandbox-rehashed to the
recorded combined hash) · `bake/ref/` (reference build record +
replay) · `bake/var/`, `bake/varA/` (fallback variant) ·
`work/cloth_build.py`, `work/cloth_bake.py`,
`work/replay_measure.py`, `work/live_probe.py` · primo detach
logs `ns39-abuild`, `ns39-abake`, `ns39-areplay`, `ns39-var`,
`ns39-ref` (primo `~/.local/share/pax/detach/`).
