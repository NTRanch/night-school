# Plan 34 — Pass 3 Clean-Room Rebuild (Controlled Comparison)

Rebuilt from `TECHNIQUE.md` alone (video closed). Estate
toolchain: Blender 5.2.3 (Arch build `/usr/bin/blender` —
scripted posing + Workbench renders; not the IK/Rigify
class), primo headless, canonical argv (`-b -Y
--factory-startup --offline-mode -noaudio -t 4
--python-exit-code 1`), one heavy job at a time, niced.

## Design of the comparison

- **Pose set (4 poses for Prima, on a COPY of her conformed
  rig; fleet untouched):** the brief's set — (1) standing
  alert, (2) seated (bench), (3) reaching, (4)
  contrapposto rest. Stated analogues to the video's set:
  pose 2 ↔ the broom-sit (support-chain pose), pose 3's
  left hand and pose 4's left hand carry the video's
  hand-contact element (hand→thigh / hand→hip; Prima holds
  no prop), pose 1 is the neutral control.
- **Rig copy:** `rebuild/prima-copy.blend` on primo,
  SHA-256 50dfd83c9d5c409af9e1d5e2046f1a9b49d3384ea942ecf059f783cd137d3f92
  — byte-identical to the fleet file as recorded in Plan
  02's PASS3; copied, never modified at source.
- **One shared target table** (`rebuild/build_pose.py`,
  SHA-256 f32ecbf8faf689b0bdd034fefbe10536609754e1de808ba52fc082cc21dfcddf):
  identical final bone values for both runs, including a
  shared contact delta and a shared secondary micro-settle.
  The ONLY differences between the runs are (a) the ORDER
  in which chains are set, (b) where the read falls, (c)
  where the contact delta is applied (T: terminal contact
  phase; E: inside the hands phase), (d) corrections each
  run's own read produced.
- **Run T (their order, strict):** context → legs → pelvis
  → spine → head → feet → arms → **mid-build distance read
  (2 Workbench previews, front + side, 360×640)** → hands →
  contact → secondary-settle → final render. Two stages:
  stage 1 ends at the read; the agent read the previews and
  wrote per-pose corrections; stage 2 applied them.
- **Run E (estate order, strict):** pelvis → legs+feet →
  spine → head → arms → hands(+contact delta) →
  secondary-settle → ambient-expression → final render →
  **verify read at end**; stage 2 applied its corrections.
- Same camera for every render (Plan 02 template position
  (0.8, −2.1, 1.42) → target (0, 0, 1.02), 35 mm), same
  Workbench studio shading, 540×960 finals. A bench box
  (0.95×0.50×0.45 m) is scene setup in both runs for pose 2.
- All 16 stage runs rc=0 with the `OK ns34_*` sentinel
  (detach logs `ns34-build1` / `ns34-build2` on primo,
  .done reads 0). Per-step logs: `out/run{T,E}-pose{1..4}-s{1,2}-log.json`
  (copies in `rebuild/`).

## The reads and the corrections they produced (agent reads)

Mid-build read of T previews (front+side per pose) and
end-state verify of E finals, same criteria (silhouette
clarity, weight read, hand registration):

| Pose | T read (mid-build) | E read (end-state) |
|---|---|---|
| 1 alert | PASS — stance, head turn, raised arm read both angles; no correction | PASS; no correction |
| 2 seated | Side preview: figure perched at the bench's front edge, feet dangling, skirt clipping the bench front → **correction: hips settle −0.04 m**, applied in stage 2 BEFORE hands/contact | The SAME defect, found at end-state verify → **same −0.04 m correction, applied AFTER hands + ambient were already finished** |
| 3 reaching | PASS — reach reads from the side; front framing crops the raised hand (shared fixed camera; noted, not a pose defect); no correction | PASS; no correction |
| 4 contrapposto | Side preview: left hand floats forward of the hip line → **correction: LeftForeArm +8° X during the contact phase** | PASS as built — the hands-phase contact delta had already landed the hand acceptably; no correction |

## Comparison numbers (all traced to the run logs)

Steps = executed phases (ordered step lists are in the
per-pose logs; sequences below). Revision count =
**unified re-touch instances**: bones set in more than one
phase across the full build (stage logs concatenated in
execution order; computed from the logs, not estimated).
Posing wall = sum of the logs' per-phase posing timers
(render time excluded). Hand registration = script probe:
world distance, LeftHand head → Hips head, metres (lower =
hand closer to the hip body mass; a registration proxy,
labelled as such).

| Measure | Run T (their order) | Run E (estate order) |
|---|---|---|
| Phase sequence | context, legs, pelvis, spine, head, feet, arms, [READ], hands, contact, settle | pelvis, legs+feet, spine, head, arms, hands(+contact), settle, ambient, [VERIFY] |
| Steps (phases, 4 poses) | **40** | **35** |
| Re-touch instances (unified) | **14** (2/4/3/5 per pose) | **13** (2/4/3/4) |
| Read-driven corrections | **2** (pose 2 seat settle — before hands; pose 4 forearm — during contact) | **1** (pose 2 seat settle — after the pose was fully built) |
| Posing-phase wall (4 poses) | 0.002 s | 0.001 s |
| Render wall (4 poses, incl. reads) | 5.92 s (8 finals + 8 previews) | 4.50 s (8 finals) |
| Hand→hip distance, pose 4 | **0.3740 m** | 0.3944 m |
| Hand→hip distance, poses 1/2/3 | 0.3169 / 0.4201 / 0.2914 m | identical (same targets/correction) |

Reading the numbers honestly:

- **Wall time does not discriminate.** Scripted posing is
  sub-millisecond per phase in both orders; the human-time
  cost of an order lives in interactive work this rebuild
  cannot measure. Reported because the brief asks; weighted
  at zero in the gate.
- **Re-touch totals are at parity (14 vs 13)** — by
  construction both runs apply the same deltas. The
  difference is WHEN re-touches land: in T every re-touch
  is a planned phase (contact, settle, read-correction)
  executed before the pose is declared done; in E the one
  substantive correction is post-verify rework on a
  finished pose (its hands and ambient already final when
  the pelvis moved −0.04 m under them).
- **Steps: T spends +5** — the context step (×4) and feet
  as their own pass, partly offset by E's ambient step
  (×4). T also spends +1.42 s of renders on its mid-build
  reads. That is the entire measured cost of their order.
- **Quality: one measurable edge.** Pose 4's hand
  registration is 2.0 cm closer under T (0.3740 vs
  0.3944 m) — the only pose where the runs' reads diverged,
  and it diverged because T's read happened while the
  contact phase was still open to absorb the fix. All
  other final pairs are visually identical (same targets).

## Final paired reads (agent reads, from `final-pairs-sheet.jpg`)

| Pose | Silhouette | Weight read | Hand registration | Pair verdict |
|---|---|---|---|---|
| 1 alert | Clear in both | Lean + head turn read in both | Natural in both | TIE |
| 2 seated | Clear in both | Seated mass on bench reads in both (post-correction); feet still dangle in both — bench height vs shin length, shared table property | Hands rest at thighs in both | TIE |
| 3 reaching | Strong diagonal in both | Counter-lean reads in both | Left hand flat on skirt/thigh in both | TIE |
| 4 contrapposto | Subtle under the long skirt in both | Hip tilt subtle in both | **T: hand lies flatter on the hip/skirt; E: hand hovers slightly forward** (matches the 2.0 cm probe) | **T edge** |

Note (both runs): Prima's conformed outfit is a long
skirt — leg work in standing poses is largely hidden,
which caps what any order can show in poses 1/3/4 and is
recorded as a rig property, not a run difference.

## Claims scored as tests

| Claim | Score | Evidence |
|---|---|---|
| C-34-1 order exists, legs-early/hands-late | REPRODUCED (as a buildable sequence) | Run T executed T1–T10 strictly for 4 poses, all rc=0 |
| C-34-2 revisions follow nameable checks | REPRODUCED | Both runs' only corrections came from reads (distance/contact), none from taste; the video's trigger table (TECHNIQUE §2) predicted the rebuild's behaviour |
| C-34-3 mid-build read before hands | REPRODUCED, with measured effect | T's read caught pose 2's seat defect before hands and pose 4's floating hand while contact was open; E's end verify caught pose 2's defect only post-build |
| C-34-4 chain-scoped partial presets | NOT TESTED in this rebuild | The comparison isolates ORDER (the plan's gate); partial-preset capture is a library mechanism, verified observationally in Pass 1 (save/load dialogs + re-application) but not rebuilt — recorded as the rebuild's scope limit, not a refutation |
| C-34-5 contact is the terminal check | REPRODUCED | T's contact phase + read-correction produced the set's best hand registration (pose 4 probe) |
