# Plan 16 — Pass 2 Distillation: Comparison Table + Convergence Map

Source: `OBSERVATION.md` (Pass 1; claims C-16-01…C-16-20).
Comparison inputs, read before viewing: Plan 01 TECHNIQUE.md
(gated sheet, T-01…T-22, Anime Nyan — animation) and Plan 02
TECHNIQUE.md (Targets 1–3, RamFutaNSFW — stills). Plan 16's
creator: **Divinity Studio** (single-character still posing,
Part 1 of 2). Per the plan, this sheet IS the deliverable:
no scene build; the rebuild record is PASS3-REBUILD.md.

**How to read the classes.** AGREE = 2+ independent creators
share the technique. SINGLE = one creator only. CONFLICT =
creators differ; the difference is stated as the deliberate
choice it is. PART-2-PENDING = Part 1 contains no evidence;
the creator's own close assigns the subject to Part 2
(Plan 17, not yet run), so the row is held open rather than
scored from absence.

## 1. Comparison table (26 rows)

| # | Technique | 01 · Anime Nyan | 02 · RamFutaNSFW | 16 · Divinity Studio | Class |
|---|---|---|---|---|---|
| R1 | Model sourcing: SmutBase download, model + separate textures as one unit | Sombra + Male Ultimate; Textures_Sombra.rar MUST be downloaded or the model renders pink | Poison "on SmutBase" | Domina; "you need the textures and the latest version… You need both of them" | **AGREE (3)** |
| R2 | Rig arrives via the DAZ-importer family (Diffeomorphic) with an MHX/CloudRig-class control rig | No — native .blend rigs with their own rig_ui | Yes — DAZ Importer 1.7.0.1540, MHX rig, Genesis 8 | Yes — Diffeomorphic 5.0.0, CloudRig (self-corrected from MHX on record) | **AGREE (02+16)**; 01's rigs were pre-converted upstream — different route, not a disagreement |
| R3 | A rig UI panel drives outfit/visibility configuration | rig_ui panel (restored by script) | Custom Body panel (skin/outfit dials + toggles) | CloudRig panel: outfit/accessory toggles, IK/FK layer switches | **AGREE (3)** |
| R4 | The rig's UI is a Python script that must be run/allowed before the rig works | Open imported `rig_ui` text, Run Script with armature selected | Not addressed (panel simply present) | "You should allow execution. It's just a Python script that allows the rig to work" | **AGREE (01+16)** on the mechanism |
| R5 | Save hygiene before iterating: preserve the file you started from | Not stated | Incremental saves Fixed → Fixed1…Fixed6 through the session | "Typically when I download models, I'll save a copy. In case I make changes that messes up the file" | **AGREE (02+16)** |
| R6 | Never move the model as an object; all work is bone work with the object at identity | Placement concentrated on the root bone; object untouched | Explicit rule, demonstrated the hard way: moving the model BROKE the rig on screen — "Don't move the model" | Armature object at Loc 0 / Rot 0 / Scale 1.000 in every frame; 100% Pose Mode work | **AGREE (3)** |
| R7 | Posing order is gross → fine, torso/spine first | Torso-led build; limbs after | Hip/spine/arms → head/gaze → expression → fingers | "We want to move the torso first. Then the limbs" — stated doctrine | **AGREE (3)** |
| R8 | Where the head sits in the order | Head stabilised as part of the thrust keying (mid-process) | Head/gaze SECOND, before fingers | Head tilt AFTER hands and fingers ("I'm going to try to tilt the head now", ~25:00) | **CONFLICT** (see §3) |
| R9 | Fingers: late, manual, conformed bone-by-bone; contact/surface fit is the check | Fingers conformed individually (Local orientation) before the hand locks | Fingers LAST, bone by bone; "barely grabbing it" is the named failure; contact on the prop is the check | Fingers manual BY CHOICE over rig tooling; conformed on the thigh; standard = "looks convincing" | **AGREE (3)** |
| R10 | Pose against a reference | Live-action reference clip as an in-scene plane | Found image drives camera angle AND pose | A reference is recreated (seated, head tilted); its medium was never captured (UNREADABLE 1) | **AGREE (3)** on reference-first; medium varies |
| R11 | Mirror / symmetry discipline | X-Mirror for the rough pose, then OFF — "humans don't pose completely symmetrical" is a stated RULE | Not addressed | X-Mirror toggled per subtask: on (paired hands) → off (legs) → on (hands) → on (robot wrists, final detail) | **CONFLICT** (see §3) |
| R12 | IK controls + pole targets aim the limbs | Leg IK with pole targets aiming the knees | IK legs layer enabled for posing | IK Controls panel; POLE-UpperArm.L placed on screen; "the legs have pole targets… the hands have pole targets as well" | **AGREE (3)** |
| R13 | When the camera enters the process | Camera added early; framed before animation | Camera FIRST — format + lens set before any posing | Camera added AFTER the gross pose (~2/3 through Part 1), then posing continues in the camera view | **CONFLICT** (see §3) |
| R14 | Camera to View | Turned OFF once framed, so the camera can't be lost by navigation | Not addressed (camera is moved deliberately, model never) | Turned ON as the working mode: navigation moves the camera while posing | **CONFLICT** (see §3) — a direct opposite |
| R15 | Standing focal length | No stated default (1920×1080 landscape scene camera) | 35 mm, stated standing default | 50 mm read off the Camera panel (not stated as a default) | **CONFLICT** (see §3) — values differ; shot classes differ too |
| R16 | Camera-occlusion tolerance: what the camera can't see doesn't get effort | Verbatim doctrine for floor clipping: "if the camera doesn't see it, it literally does not matter" | Not stated (his economy is removal of what fails, R23) | Of the camera-invisible hand: "it doesn't really matter what we do" | **AGREE (01+16)** |
| R17 | Viewport performance mode while posing | Simplify ON, subdivision Levels Viewport 0 | Simplify ON for all interactive work | The rig's own "UI disabled for posing performance" mode | **AGREE (3)** on intent; three different mechanisms |
| R18 | Beginner shortcut primer inside the tutorial | Navigation/transform primer segment | None | G/R/S + numpad-view primer, twice | AGREE (01+16) — pedagogy, not technique; recorded, not distilled |
| R19 | Loop construction, cycle timing, seam law | The video's core: 31 f cycle, Contact 15, Make Cyclic, seam law | n/a (still) | Absent — no keyframe is set in Part 1 | **PART-2-PENDING** |
| R20 | Contact keeping (constraints/locks) | Child Of locks, Set Inverse, Influence 1.000 | n/a beyond finger contact check | Absent — single character in Part 1 | **PART-2-PENDING** |
| R21 | Lighting build method | From black, World 0, rim first, shadows "most important" | Emissive backdrop + World 0.000, role rig built one lamp at a time | Absent — Rim1 + Sun ship inside the model file; nothing built or tuned | **PART-2-PENDING** (creator: "Part two will set up the lighting") |
| R22 | Render preset | Cycles, Noise Threshold 0.0100 / Max 4096, Denoise ON | Cycles GPU, Noise Threshold 0.0100 / Max 4096 | Absent — no render in Part 1 | **PART-2-PENDING** (01+02 already AGREE on the pair; 16/17 would make or break a 3-creator convergence) |
| R23 | Post chain | Resolve image-sequence preview (no grade taught) | Lightroom Lens Blur + Photoshop signature only | Absent — "a little post processing" promised for Part 2 | **PART-2-PENDING** |
| R24 | Outfit problems are solved by visibility, not refitting | Unused clothing collections deleted | Ill-fitting clothing HIDDEN, accessories kept | Outfit configured by panel toggles from the start (no failure shown) | **AGREE (3)** in outcome; 16's is configuration, 01/02's is failure response |
| R25 | Character-sourcing doctrine: an explicit ranked route map for beginners | Sourcing shown, no ranking | Sourcing shown, no ranking | Explicit: download ready-made first (recommended), creator software second, scratch last (defer until skilled) | **SINGLE (16)** |
| R26 | Ecosystem survey as step 0 (Houdini, Maya, ZBrush, Character Creator, MetaHuman, tablets) | No | No | Yes — ≈9.5 min of the 27:48 | **SINGLE (16)** |

**Tallies: AGREE 15 · CONFLICT 5 · SINGLE 2 ·
PART-2-PENDING 4 — 26 rows.** (R18 is counted in AGREE as
logged agreement, flagged pedagogy.)

## 2. Convergence map — AGREE rows × estate practice

For each AGREE row: does an estate practice contradict the
convergent technique? Contradictions are named explicitly
with the evidence's direction — agent read, labelled.

| Row | Convergent technique | Estate contradiction? |
|---|---|---|
| R1 | SmutBase sourcing; model + textures as one download unit | **None at mechanism level.** Estate intake treats the textures as a post-hoc repair (Plan 01 T-01: Find Missing Files is "source-file hygiene… does not transfer"). The convergence says completeness is an INTake property, not a repair — this gap is P3 contribution P3-1, not a contradiction. |
| R2 | DAZ-imported rigs are the field's working rigs | **Asset-strategy tension, not a mechanism contradiction.** Estate: the conformed 54-bone standard (SIX-GIRL-STANDARD §2.1); Plan 01 Binding finding 1 rejects skeleton additions. Both DAZ creators DOWNLOAD rigs rather than design them — the convergence evidences sourcing reality, not a rig-design verdict. Evidence favours the estate for its interchangeability goal. No change. |
| R3 | Rig UI panel as the configuration surface | **None.** Estate rigs carry their own UI equivalents (CloudRig-class panels on the source side; the standard's governed channels on the estate side). |
| R4 | Rig UI = Python script; allow/run it or the rig is dead | **YES — the sharpest contradiction in this map.** 16's instruction is "you should allow execution. It's just a Python script." Estate discipline is the opposite posture for downloaded files: Blender work runs with script auto-execution OFF (-Y always, -y never; the tiger-style-blender autoexec rule), and scripts that run are estate-authored and invoked explicitly (Plan 01's form — open the text, Run Script — is the estate-shaped half of this row). The MECHANISM (a rig UI must be executed to live) is real and convergent; the TRUST POSTURE (allow a stranger's .blend to auto-execute) is what the estate refuses. Evidence favours the estate: the mechanism transfers, the posture must not. Recorded as decision item D-16-1 in PASS4. |
| R5 | Preserve the starting file (copy / incremental versions) | **None.** Estate template practice already versions build outputs (Plan 02); 16's pristine-copy-before-first-edit half is the missing piece — P3 contribution P3-2. |
| R6 | Object stays at identity; pose bones only | **None — already an estate gate.** Plan 02's template asserts armature object location == (0,0,0); Plan 01 T-03 concentrates placement on `mixamorig:Hips`. Three-creator convergence CONFIRMS an existing estate rule. |
| R7 | Gross → fine, torso first | **None.** Matches Plan 02's distilled discipline verbatim in structure. |
| R9 | Fingers last, manual, surface-fit is the check | **None.** Plan 02 Target 2 item 4 is the same rule; the fleet's finger bases (§2.1) are where it lands. 16 adds the explicit rejection of rig finger tooling ("I'd rather just do it manually") — a preference two of three share in practice. |
| R10 | Reference-first posing | **Partial tension on exactness, none on method.** All three pose against a reference. 16's standard is approximate ("won't be exact… as long as it looks convincing" is his finger standard, and the pose standard alike); the estate's keeper discipline gates by eye against a SHOULD-BE-SEEN. Different deliverable classes (tutorial vs production asset) — recorded as a scope difference, not a contradiction. |
| R11 | — (CONFLICT row; §3) | — |
| R12 | IK + pole targets aim limbs | **Adaptation, not contradiction.** The fleet is FK (54 bones, no IK targets, §2.1); Plan 01 T-03 already translates pole-aiming into FK rotation judged by walk-back. 16 extends the pole evidence from legs (01) to arms and hands — P3 contribution P3-3 generalises the authoring note. |
| R16 | Camera-occlusion tolerance | **YES — a standing estate refusal, kept.** Plan 01's sheet rules this tolerance does NOT transfer: the estate gate "measures interpenetration on the contact set, camera or no camera" (Binding finding 3). Two creators now state the tolerance (01's floor clipping; 16's invisible hand), and its honest scope is visible in both uses: EFFORT ALLOCATION in posing/stills, never a correctness criterion. Evidence favours the estate for contact/drift; favours the creators for still-posing effort. Recommendation (PASS4 D-16-2): keep the refusal for contact; admit the tolerance explicitly as a stills effort heuristic so the estate stops pretending it doesn't use it. |
| R17 | A named performance mode while posing | **None.** Estate form is Simplify discipline (Plan 02's scripted assertion); 16's rig-baked UI-off mode is the same intent inside the asset. |
| R24 | Solve outfit failure by visibility | **None.** Estate form is outfit-variant selection at build time (Plan 02 Target 2 item 5, Adapt). |
| R26/R25 | — (SINGLE rows; §4) | — |

## 3. CONFLICT rows — the difference as a deliberate choice, + estate position

| Row | The choice | Estate position |
|---|---|---|
| R8 Head timing | 02: head/gaze early (second) so the pose's intent reads while the body is roughed in. 16: head last-but-prop, tilted once the body and hands are settled, aimed at the camera. 01: head is a stabilised channel of the animation, neither early nor late. | **NO-POSITION** in the rebuild set for stills (Plan 02's sheet adopts 02's order for its template discipline; nothing in the set has tested 16's order). The difference is real but low-stakes: both orders end at the same place; 02's catches a wrong gaze early, 16's avoids re-tilting after hand work. Coordinator's call if the template is ever revised. |
| R11 Symmetry | 01: mirror is a ROUGH-IN tool with an expiry — finished poses are asymmetric BY RULE ("humans don't pose completely symmetrical"). 16: mirror is a per-control CONVENIENCE, toggled whenever pairing helps, including final detail (robot wrists). | Estate position is **01's, already adopted**: Plan 01 T-03 carries the asymmetry rule into the demonstrator ("no finished pose is symmetric by construction"). 16's wrists case is the legitimate exception that tests the rule — the robot arms are symmetric PROPS, not anatomy. Recommendation (PASS4 D-16-3): keep the rule for anatomy; name the prop exception explicitly rather than letting practice drift. |
| R13 Camera timing | 02: camera FIRST — the frame exists before the pose, so every posing decision is made inside the deliverable's geometry. 16: camera AFTER the gross pose — pose freely in open space first, then frame, then finish under supervision. 01 sits between (camera early). | Estate position is **02's, already built**: Plan 02's template opens with camera + format ("still framed before posing in build order", PASS3 claim C-02-1 REPRODUCED). 16's order is the natural one for a pose that must first exist as a body; 02's is the disciplined one for a deliverable that is a frame. No change proposed; the conflict is recorded so the choice stays deliberate. |
| R14 Camera to View | 01: OFF after framing — the camera is an asset; navigation must not be able to lose it. 16: ON while working — the camera is a viewpoint; navigation SHOULD move it, and a second pane supervises. | **NO-POSITION.** The estate's scripted route has no interactive navigation to protect or exploit; both postures are answers to interactive-session risks the estate doesn't run. Recorded so a future interactive authoring step chooses deliberately instead of inheriting a default. |
| R15 Focal length | 02: 35 mm standing default (portrait still, figure-filling). 16: 50 mm on the panel (seated full-body frame). 01: no default stated. | Estate position is **02's values as template parameters** (Plan 02 PASS3: lens 35.0 mm built). The values serve different shot classes — this is the weakest conflict in the table (a default vs an instance), recorded because the plan asks for disagreements logged, not because either is wrong. PART-2-PENDING in part: whether 16 states a general preference when he reaches lighting/render in Part 2. |

## 4. SINGLE rows — one creator only

| Row | Technique | Disposition |
|---|---|---|
| R25 | Ranked sourcing doctrine (download → creator software → scratch, in skill order) | 16-only, and it is the row with the clearest estate value per word: it is the beginner on-ramp the estate's own intake implicitly follows (SmutBase first for study material) without ever stating. Not convergent, so not a P3 contribution by the plan's rule — filed in PASS4 as a documentation candidate for the coordinator, labelled SINGLE. |
| R26 | Ecosystem survey preamble (paid tools surveyed and set aside for a free route) | 16-only. Its transferable content is the DECISION RECORD (why not Houdini/Maya/CC for this work: cost + learning curve vs free + sufficient), not the survey itself. No estate action; recorded. |

## 5. PART-2-PENDING rows — what Plan 17 must answer

- **R19/R20 (animation + contact):** does Divinity Studio keyframe
  the pose into motion in Part 2, and if two characters ever
  meet, what holds contact? (Plan 17's stated focus is
  finishing; animation may be out of the course's scope
  entirely — in which case these rows close as NOT-TAUGHT
  rather than pending forever.)
- **R21 (lighting):** his announced Part 2 opens here. The
  triangulation question is pre-registered: does he build
  from black / World 0 like BOTH predecessors, and does he
  use a role rig or the file's bundled Rim1 + Sun?
- **R22 (render pair):** 01 and 02 already converge on
  Noise Threshold 0.0100 / Max Samples 4096. If Part 2 lands
  on the same pair, that is a three-creator convergence on
  a preset the estate has already adopted twice — the
  single most valuable confirmation Plan 17 can deliver.
- **R23 (post):** "a little post processing" vs 02's
  Lightroom/Photoshop chain and 01's Resolve preview.

## 6. Counts

- Comparison rows: **26** (AGREE 15 · CONFLICT 5 · SINGLE 2 ·
  PART-2-PENDING 4).
- AGREE rows with a named estate contradiction: **2**
  (R4 trust posture; R16 occlusion tolerance) + 1
  asset-strategy tension (R2, no mechanism contradiction).
- Sharpest contradiction: **R4** — a creator's explicit
  instruction to allow a downloaded .blend's Python to
  execute, against the estate's autoexec-off discipline.
  The mechanism is convergent; the posture is refused.
