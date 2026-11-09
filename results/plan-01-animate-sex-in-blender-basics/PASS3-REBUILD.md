# Plan 01 — Pass 3 Clean-Room Rebuild Record

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on primo,
  scripted, deterministic. **Only source used:** the gated
  `TECHNIQUE.md` in this run dir (video/transcript closed throughout).
  Sheet gaps found are in `ADDENDA.md` (dated tuning values).
- **Casting (coordinator):** Prima = Follower, Yui = Leader — timing /
  contact roles, not characters. Rigs are the CONFORMED fleet blends
  (`torogao-models-20261104/{prima,yui}`; staged to primo by hash:
  prima.blend md5 `2dc75c2f…`, yui.blend md5 `45ecd804…`). Fleet files
  were never modified; both rigs were appended into a new scene.
- **Build host discipline:** primo, one heavy job at a time (only other
  tenant: ComfyUI :8191; ≥33 GiB RAM free throughout), file-mediated
  detached runs (`~/.local/share/pax/detach/`, prefix `ns01r-`),
  completion read from `.done` files. Nothing audible.
- **Deliverables:** `rebuild/build_loop.py` (the one build script,
  sha256 `4caf4889…`), `rebuild/scene/scene.blend` (`0bcd3bcd…`),
  `rebuild/clips/` (two `torogao-motion-clip/1` artifacts + skeleton
  defs), `rebuild/frames/` (evidence frames + bonus clip),
  `rebuild/records/` (`build_record.json`, `measurements.json`,
  show JSONs), benchmark at `rebuild/BENCHMARK.md` (written before
  final renders).

## 1. The build

One bpy script produces everything: scene assembly (T-01 estate form:
Prima's blend opened, Yui appended in one `libraries.load` pass —
per-object `wm.append` re-appends dependency armatures/cages on 5.2,
probed), placement solved onto the Hips channel only (T-03; placement
residuals ≤0.003 mm), the source's own arrangement (observation §2:
Follower seated on a cushion on a low platform, legs raised; Leader
kneeling on the platform behind her, leaning over her back), the
contact empty + solve, hand solves, keying (all fcurves LINEAR,
306 CYCLES modifiers read back), measurements, the T-13 cure,
evidence renders, and clip export through the fleet's own
`build/gen_clip.py`.

- **Loop:** 78 samples @ 60 Hz, Contact at sample 38, markers
  "Contact" (38) / "End of Loop" (78); scene range 0–234 = 3 cycles
  (ruling 1; T-04/T-21 estate forms). All key times are the source's
  ×78/31: Leader 0/15/31 → 0/38/78, breakdown 6 → 15; Follower
  ≈6/12/17/20/26/31 → 15/30/43/50/65/78 family (realised as the
  amplitude table in §3); feet 15/23 → 38/58.
- **Contact (T-10, ruling 2):** scene-side empty `ContactEmpty`
  carries a Child Of constraint → Prima's armature, bone
  `mixamorig:Hips`, all axes, Influence read back **1.000**. Set
  Inverse on 5.2 was probed: the manual inverse matrix
  (`(arm.matrix_world @ bone.matrix)⁻¹`) reproduces Set Inverse with
  a post-constraint empty displacement of **0.000004 mm**
  (`build_record.json: childof_setinverse_delta_mm`). The Leader's
  Hips location keys are then *solved* against the frozen frame-0
  registration offset in Prima's Hips frame (the keyed expression of
  the lock; clips carry no constraints, §7.2). Solve residuals at the
  8 location keyframes ≤0.0004 mm. Her location channel carries extra
  solve keys at 26/45/65 so the keyed form interpolates tightly;
  rotation keys stay on the sheet's grammar frames.
- **Hands (T-11, ruling 4):** solved as keys, never constraints.
  Damped least-squares on Arm/ForeArm rotations against frozen
  offsets in the target UpLeg bone frame (Prima's hands → her own
  thigh tops, frac 0.10; Yui's hands → Prima's thigh roots/buttocks
  from behind, frac 0.10). Frame-0 solve residuals: Prima L/R
  0.448/0.462 mm, Yui L/R 0.393/0.392 mm.
- **No opening mechanism** (T-12, ruling 3): nothing invented, no
  channel added. **Jiggle layer not built** (Plan 39's layer): both
  girls' cage `Bounce` values measured **0.0 at every sample**
  (`bounce_max_abs`), the beat window left intact — see §5.

## 2. Gate measurements (all from `records/measurements.json` /
`build_record.json` of the final run)

- **Drift — the Child Of class claim is "no drift"; measured:**
  contact empty vs Prima's `mixamorig:Hips` head across all 79
  evaluated samples (0–78): **max 0.0001 mm, mean 0.0000 mm**. The
  shipped (keyed) form of the same lock — Yui's Hips registration
  error against the frozen offset: **max 0.393 mm, mean 0.087 mm**
  (pure interpolation residual between solve keys).
- **Interpenetration** (contact set = pelvis-box verts of both Body
  meshes; test = two-axis ray parity + nearest-surface depth ≤15 mm,
  see the artifact note in §7): pre-cure **max 5.97 mm** (all
  penetrating verts Prima-in-Yui; Yui-in-Prima: none at any sample).
  T-13 cure applied — scene-side shape key `ContactFix` on the scene
  copy of Prima's Body only (named key, value 1.0, never Basis;
  8 verts, max delta 6.97 mm, capped at sculpt class): post-cure
  **max 5.46 mm, mean-of-sample-maxima 3.76 mm**, worst samples
  61–67 (recovery half). **What remains is a real residual**: two
  rigid pelvis meshes in sustained registered contact graze a few
  millimetres where their curved surfaces meet under rotation; a
  single static corrective key cannot chase a moving overlap the
  way the source's per-pose interactive sculpting did. Reported,
  not hidden.
- **Seam:** per-bone evaluated pose deltas, frame 0 vs 78, all
  108 bones (54 × 2 girls): **max translation 0.000 mm, max rotation
  0.000°** — exact, after the seam-law construction (endpoint keys
  are copies of frame 0, not independent re-solves; a re-solve
  landed within solver tolerance but 0.0019 quat off on the arm
  chain, visible at silhouette edges — §7). Pixel verdict below.
- **80/20 (T-05 test form, channel-energy over the full cycle):**
  rotation 62.83 mm at the 0.10 m contact lever vs translation
  14.30 mm → **rotation share 0.8146**. Torso counter-rotation is in
  the channels (Spine −10°, Spine1 −7° against Hips +18°); measured
  world swings: Hips 18.0°, Spine1 1.0°, **Head 6.0°** (head
  stabilised to a third of the hip swing).
- **Oval (T-06):** the Leader's pelvic contact point
  (`Anchor_Fluid_Pelvis` world path; the Hips head is the rotation
  centre and is lock-held, so it cannot trace the arc): closed
  (closure 0.000 mm), PCA extents PC1 37.85 mm × PC2 8.79 mm,
  **PC2/PC1 = 0.232** — a true oval, not a line.
- **Follower grammar (T-07/T-08):** Prima Spine RX evaluated:
  11.8° (s0) → 10.8° (s15) → 10.0° (s30) → **10.0° at Contact (s38)**
  → **14.0° peak (s45)** → 13.2° (s52) → 11.8° (s78). Hold-until-
  Contact holds (no reaction motion 30→38); peak lands 7 samples
  after Contact; endpoints are the same mid-recovery pose.

## 3. Key tables (samples @ 60 Hz; source frames ×78/31)

- Leader phase p: {0: 0, 15: 0.12, 38: 1.0, 53: 0.38, 78: 0} —
  entry pause 0–15, thrust 15–38, long recovery 38–78.
- Follower amplitude a: {0: 0.45, 15: 0.20, 30: 0, 38: 0, 45: 1.0,
  52: 0.80, 63: 0.52, 73: 0.44, 78: 0.45} — mid-recovery at both
  endpoints (T-08 construction), peak centre pulled −5 samples
  (the −2 source-frame pull; ADDENDA #3).
- Feet (T-15): LeftFoot bump +6° peaking s45; RightFoot offsets
  {0: +4°, 38: +4°, 58: +7°, 78: +4°} (the s38 value copied to s78).
- Faces: Prima's governed channels ride the follower phase
  (HalfClose peak 0.55 @45, Aa 0.38 @45, Pupil_Heart 0.80 @45 —
  Prima is a trio girl, §3.3); Yui steady (Smile 0.35,
  HalfClose 0.15).

## 4. Claims (the 29 in the sheet's coverage table; C-30 was judged
not-a-technique at the Pass 2 gate and is excluded)

**Tallies: REPRODUCED 18 · REFUTED 0 · UNTESTABLE-IN-ROUTE 4 ·
not built — rejection stands 7.**

| Claim | Score | Evidence |
|---|---|---|
| C-01 cycle + markers + authoring range | REPRODUCED (estate form, ruling 1) | 78 samples, markers Contact 38 / End 78 read back; scene range 0–234 |
| C-02 thrust keys + cyclic over full span | REPRODUCED (estate form) | Keys 0/38/78 + breakdown 15; 306 CYCLES modifiers; every channel spans 0–78 |
| C-03 80/20, counter-rotation, head | REPRODUCED | Share 0.8146; world swings Hips 18.0° / Spine1 1.0° / Head 6.0° |
| C-04 oval arc path | REPRODUCED | Anchor path PCA 37.85 × 8.79 mm, PC2/PC1 0.232, closure 0 |
| C-05 follower offset/denser, hold, peak after, −2 pull | REPRODUCED | §2 follower grammar line; key tables §3 |
| C-06 follower mid-recovery at both endpoints | REPRODUCED | a(0) = a(78) = 0.45; Spine RX 11.8° at both, measured |
| C-07 Child Of pelvic lock, Influence 1.000, Set Inverse | REPRODUCED (translated to fleet names, finding 1) | Empty → Prima `mixamorig:Hips`; influence readback 1.000; Set Inverse Δ 0.000004 mm; drift max 0.0001 mm |
| C-08 second genital lock (speech-only) | UNTESTABLE-IN-ROUTE | No second lock point exists on the 54-bone fleet; the sheet itself needs only one (T-10 flag) |
| C-09 constraints after posing, auto-key OFF, right stack | REPRODUCED (scripted form) | Build order pose → constrain → set-inverse; constraint lives on the constrained item (T-10 estate note); headless build has no auto-key |
| C-10 Limit Scale guard | not built — rejection stands (T-12) | No fleet channel exists (§3.1 census: 36 `Fac_` only); ruling 3 |
| C-11 VaginaOpen range raise, values >1.0 | not built — rejection stands (T-12) | As C-10; the read-backs remain source-side evidence |
| C-12 opening bone keyed Loc+Rot+Scale | not built — rejection stands (T-12) | As C-10; key magnitude UNREADABLE item 2 besides |
| C-13 correctives in sculpted keys at 1.0, never Basis | REPRODUCED | `ContactFix` scene-side key, value 1.0; penetration 5.97 → 5.46 mm max |
| C-14 her hands locked to closest thigh bone | REPRODUCED (ruling-4 form: solved keys) | Frame-0 residual ≤0.46 mm; across-loop dev max 0.49 mm |
| C-15 his hands likewise (speech-only) | REPRODUCED (ruling-4 form) | Frame-0 residual ≤0.39 mm; across-loop dev max 4.94 mm (interpolation between her 5 hand keyframes) |
| C-16 `<Contact>` IK pose variants | not built — rejection stands (T-14) | Contact pose of record = the clip's sample-38 keys; variant values are source-rig spaces, non-transferable |
| C-17 feet last/subtlest, one bump, 15/23 + copy | REPRODUCED | §3 feet line (38/58, 38 copied to 78) |
| C-18 seam law: identical endpoints, variation mid-cycle | REPRODUCED | Bone deltas 0.000 mm / 0.000° over 108 bones; pixel-identical seam frames (§5) |
| C-19 breast follow-through, peak ≈Contact, no add-on | UNTESTABLE-IN-ROUTE (this build) | The jiggle layer is Plan 39's, excluded by the brief; `Bounce` = 0.0 at every sample and the beat window is left intact (§5 phase map) |
| C-20 hair curve cascade +2 offsets | not built — rejection stands (T-17) | Fleet Hair is an unboned mesh (§2.1); no chain exists |
| C-21 Mask-modifier limb hiding, off for render | UNTESTABLE-IN-ROUTE | Scripted route has no interactive posing to occlude; no mask was needed or faked |
| C-22 append by collection, widgets quarantined, rig_ui | REPRODUCED (estate form) | One-pass scripted append, object census in build record; cages/anchors render-quarantined; fleet rigs carry no `rig_ui` (sub-clause has no analogue) |
| C-23 scale the armature object, never the root bone | REPRODUCED | No scale channel exists in either clip (gen_clip emits none, clips inspected); no bone was ever scaled in the build |
| C-24 realistic stature for lighting | REPRODUCED | Fleet spec heights Prima 1.65 m / Yui 1.50 m (§8.1), scene lit at metre scale |
| C-25 sofa Light Path material | not built — rejection stands (T-22) | Scene/lighting craft, outside this sheet's target |
| C-26 Volume Scatter wrap | not built — rejection stands (T-22) | As C-25; anisotropy value UNCONFIRMED besides |
| C-27 source render settings | UNTESTABLE-IN-ROUTE | T-21: settings are not the estate contract; estate evidence renders are EEVEE 960×540 from the fleet-style rig (two suns) |
| C-28 render range = whole cycles, repetition baked in | REPRODUCED (principle) | Scene renders 3 cycles (0–234); repetition frames pixel-identical (§5) |
| C-29 timing judged at true rate, never raw viewport | REPRODUCED (estate form) | No interactive playback exists in the route; all timing verdicts are from rendered frames + rate-exact clip data |

## 5. Determinism + seam pixels + the Plan 39 phase map

Full build run **twice in separate Blender processes** (runA/runB,
identical script sha256 `4caf4889…`), primo detach logs
`ns01r-buildAB.log`:

- **Clip artifacts bit-identical:** Prima clip sha256
  `bab815bbe20078502154afbf756b02595dfa27a6397f988043db737ff54f2566`,
  Yui clip sha256
  `6089cc6902ca6f6869aeecdf20050976ebd05dda34c508f789e7d4578aefa541`
  in both runs. (Prima's skeleton def sha `1c6087af…` equals the def
  of record from her solo-arc clip — the retarget binding is the
  fleet's own.)
- **Decoded-pixel hashes identical** (via `rebuild/pixelhash.py`;
  never PNG file bytes): f_0019 `5d4cd82b…`, f_0038 `570ee7fa…`,
  f_0045 `16b09e7c…` in both runs.
- **Seam:** f_0000 and f_0078 pixel hash both `779cc562…` —
  identical. **Repetition:** f_0116 and f_0194 both equal f_0038
  (`570ee7fa…`) — the loop holds over 3 cycles (T-21/C-28).
- **Phase map for the Plan 39 jiggle layer (T-16):** no `Bounce`
  keys were authored and both girls' cages sit at 0.0 throughout, so
  the §5.2 beat of record drops onto this loop without collision:
  beat peak at the Contact sample **38**, settle (0.30·amp) at
  **53**, rest at **83 ≡ sample 5** of the next cycle; the
  follower's spine reaction peak (s45) sits inside the beat window,
  7 samples after the beat peak — the cage lag reads off the same
  impulse the sheet's T-16 describes (peak at Contact, body pulled
  early). D-1 stacks the beat on these samples unchanged.

## 6. Expected-vs-seen (benchmark: `rebuild/BENCHMARK.md`, written
before final renders; frames are bodies-only renders so the contact
set is visible — outfits occlude it entirely, record in
`build_record.json`)

| # | Item | Read |
|---|---|---|
| 1 | Contact held, no visible gap/breakthrough | **PASS** — no air gap at the hip line at 19/38/45; interface partly occluded by Prima's torso from the ¾ view, measurement carries it (gap 3.0 mm at frame 0, drift ≤0.39 mm) |
| 2 | Follower phase lag visible | **PASS** — Yui's advance/head lowest at 38; Prima's torso pitch + face peak at 45 (Spine RX 10.0° → 14.0°) |
| 3 | Leader reads as rotation, not sliding | **PASS** — advance reads as a lean-over pivot; head swing 6.0° vs hips 18.0° |
| 4 | No visible penetration at the contact set | **PASS at viewing size** — none visible in any evidence frame; the measured subsurface residual (max 5.46 mm) is reported in §2, not hidden behind this read |
| 5 | Seam invisible, follower mid-recovery | **PASS** — f0/f78 pixel-identical; Prima at the seam is mid-recovery (Spine 11.8°, a = 0.45), not parked |
| 6 | Hands stay planted | **PASS** — Prima's hands on her own thighs, Yui's at Prima's hips in all three phase frames; deviations measured in §2/C-14/C-15 |
| 7 | Faces alive, follower-phased | **PASS** — Prima's mouth/expression visibly opens at 45 vs 19/38; Yui steady. Face size in frame is small — quality verdict is the Owner's (eye item E-2) |

**Eye items queued for the Owner** (frames in `rebuild/frames/`,
bonus clip `frames/contact-loop-x2.mp4`, 2 cycles at 60 fps,
sha256 `7b3405c0…`):
- E-1: the loop as motion — does the contact read as held and
  weighted over repetition, or as two mannequins in proximity?
- E-2: Prima's expression at the follower peak (f_0045) — face is
  small at this framing; is the governed-expression read strong
  enough, or does D-1 need a closer evidence camera?
- E-3: small dark specks visible on the cushion between Prima's
  legs in some frames (f_0019) — read as Yui's toe tips seen
  through the leg gap; Owner to confirm they don't read as
  artifacts.
- E-4: the residual penetration (§2) is subsurface at this
  camera; if D-1's camera goes closer, the 5.46 mm recovery-half
  residual becomes the first thing to re-cure (per-pose keys, not
  one static key).

## 7. Route findings / gaps (video stayed closed)

1. **Blender 5.2 API drift (probe-first, all readback-verified):**
   `Action.fcurves` is gone for layered actions — fcurves live on
   `strip.channelbag(slot)` (slot argument required);
   `BLENDER_EEVEE_NEXT` did not take, `BLENDER_EEVEE` did (read
   back); per-object `wm.append` re-appends dependency objects
   (duplicate armatures/cages) — one-pass `libraries.load` is the
   clean route; Child Of Set Inverse is exactly reproduced by the
   manual inverse matrix (Δ 0.000004 mm).
2. **First-attempt pose geometry was refuted by the gate, as
   designed:** posing the Leader facing the Follower drove her
   raised knees through the Leader's torso (66 mm penetration at
   every sample). The source's own arrangement (Leader kneeling
   behind, observation §2) is the fix — ADDENDA #5.
3. **Penetration-test artifact class:** single-axis ray parity
   miscounts hip-side verts beside the partner's gripping fingers
   (small closed blobs read as "inside", depths to 47 mm). The
   shipped test requires two-axis parity agreement + ≤15 mm
   nearest-surface depth; 1 such reading was rejected and counted
   (`penetration_detail.rejected_far_count`).
4. **Seam exactness is a construction, not a tolerance:** endpoint
   keys must be *copies* (of frame-0 keys / solves), because
   independent re-solves land within tolerance but not on the same
   pose, and 0.7 mm at a fingertip is 1.1% of pixels at an edge.
5. No TECHNIQUE.md content gap required an addendum beyond tuning
   values (ADDENDA.md, 2026-11-06): thrust amplitudes, foot-bump
   amplitude, follower peak placement, hand-solve tolerance, pose
   arrangement.

## 8. What ships for D-1

`rebuild/clips/prima-contactloop.clip.json` (Follower part) and
`yui-contactloop.clip.json` (Leader part): `torogao-motion-clip/1`,
49 body tracks + face tracks (Prima 4, Yui 2), 60 Hz, `loop: true`,
frames 78, binding by bone name to `prima-rig/1` / `yui-rig/1` —
ready for the §7 retarget procedure. The scene file
(`rebuild/scene/scene.blend`) holds the authoring state (contact
empty + Child Of, `ContactFix` key, markers); the clips themselves
carry no constraints and no cage state, per §7.2.
