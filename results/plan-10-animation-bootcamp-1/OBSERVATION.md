# Plan 10 — Pass 1 Timed Observation

Source: pinned capture (MANIFEST.md), 1,551.53 s, Blender **4.5.7**
(bottom-right of frame, native read at 22:00). Screen-governed:
grid sheets at 30 s steps (52 frames) + native frames at 90, 480,
615, 630, 645, 720–770 bracket, 900, 1140, 1230, 1320, 1410,
1470, 1500 s. The recording carries a screencast-keys overlay, so
most operations are labelled on screen by the creator's own tool.

**Transcript status at first writing:** the whisper lane on primo
is held by two parallel all-hands jobs (Plans 05/09); this log is
written from the screen and is tagged [SCREEN] throughout.
Speech-dependent items (verbal definitions, any set exercise /
homework wording) are marked PENDING-TRANSCRIPT and are never
rested on until the transcript lands; screen beats speech on any
disagreement when it does.

## The subject

A pre-rigged two-figure NSFW loop scene in Blender Pose Mode:
a red female figure ("Shani" — rig name **Shani_IK_Rig**, action
**Shani_IK_RigAction**) riding a grey male figure. The animated
bone throughout is **torso**; its channel set (native reads at
22:00 and 24:30): X/Y/Z Location, W/X/Y/Z Quaternion Rotation,
X/Y/Z Scale. Scene frame range **Start 1, End 14** — the whole
episode builds one 14-frame loop.

## Timed log

| Time | What happens [SCREEN] |
|---|---|
| 0:00–2:00 | Scene open in the Animation workspace; viewport navigation (Wheel, Shift+Middle Mouse per overlay); output/format settings in view (1920×1080 in the Format panel) |
| 2:00–5:00 | Pose-mode selection work on the rig controls; keyframed fields appear (green transform fields); "(De)select All ('pose.select_all')" |
| 5:00–7:30 | A control is grabbed (G, 'view3d.select'); the Dope Sheet appears with the first keyframe columns (~7:00) |
| 7:30–10:30 | Dope Sheet channel rows multiply as channels are keyed; playback; then "Select Keyframes ('graph.clickselect')" — the Graph Editor opens on a single smooth cyclic curve (~9:30) |
| 10:30–12:30 | Graph Editor close work: the curve and its handles; Dope Sheet summary rows; torso Transform read at 10:30: Loc X 0 m, Y 0.12502 m, Z −0.54967 m, quaternion W 1.000 |
| **12:44** | **Full-screen theory insert: the MOTION EDITORS slide** (transcribed below) |
| 13:00–16:00 | Back in Blender: 'action.select_all' in the Dope Sheet, the 1–14 key columns selected as a block; orbiting views of the loop playing at several phases |
| 16:00–18:00 | Timeline at the bottom with sparse keys; scrubbing/playback |
| 18:00–20:00 | **Motion Paths** shown in the viewport: the white elliptical trajectory around the pelvis with numbered keyframe markers; panel settings read at 22:00 (below) |
| 20:00–22:30 | Graph Editor on **Z Location (torso)**: the curve is switched to a sharp **V** via Set Keyframe Handle Type (V), then returned to a smooth valley; keys moved with 'transform.translate' |
| 22:00 | Native read: curve runs ≈ −0.49 → trough ≈ −0.657 at frame ~7 → back to ≈ −0.49 at 14; playhead at 7; torso Z at that frame −0.65698 m (matches the trough — cross-check PASS); Motion Paths panel: Type **In Range**, Calculation **Scene Frame Range**, Start 1 / End 14 / Step 1, **Thickness 6**, Keyframes ✓, Keyframe Numbers ✓, Before = red, After = green |
| 22:30–24:00 | The smooth curve is shown with a **dip below the trough line** — the overshoot case — then the Dope Sheet returns |
| 24:30 | Native read: Dope Sheet, torso channels, key columns at frames **5, 7, 9** in view; the **Set Keyframe Handle Type menu open: Free / Aligned / Vector / Automatic / Auto Clamped** |
| 24:30–25:52 | Keyframe-type menu in the Dope Sheet; a final flatter Graph Editor curve; end |

## The theory slide (12:44, native read — creator's reference card)

"MOTION EDITORS — Timeline · Dopesheet · Graph Editor — A
Technical Comparison" ("// BLENDER 3D — ANIMATION SYSTEM"):

- **Timeline** (01/03): "The master clock of your scene…
  Best for high-level temporal control — setting in/out points,
  scrubbing through time, and previewing playback." Bullets:
  frame range & playback controls (FPS, looping); scene-wide
  keyframe overview; set render start/end & preview range;
  markers; jump between keyframes with ↑/↓.
- **Dopesheet** (02/03, Shift+F12): "Keyframe management hub…
  Critical for timing edits across multiple objects and channels
  simultaneously — without touching interpolation curves."
  Bullets: per-channel key list; select/move/scale keys with
  G/S; multi-object editing; Action Editor mode for NLA-ready
  clips; interpolation type (T) without curve detail.
- **Graph Editor** (03/03, Shift+F6): "The precision layer.
  Visualizes animation as F-Curves — mathematical splines where
  handles control interpolation between keyframes. Essential for
  polishing easing, eliminating floaty movement, fixing
  overshoots, and crafting professional-quality animation feel."
  Bullets: Bezier handle manipulation; overlay multiple
  F-Curves; modifiers (cycles, noise, envelope, limits);
  extrapolation control; channel filtering, colour by axis.
- **Feature matrix** (capability × editor): playback control
  Primary/Basic/Basic; frame range & markers Full/Markers
  only/No; keyframe timing edit Limited/Full/Full; interpolation
  curves No/No/Primary; handle manipulation No/No/Bezier+Auto;
  multi-channel view No/All channels/Overlaid; F-curve modifiers
  No/No/Cycles, Noise…; action clip editing No/Action
  Editor/Read-only ref; complexity Low/Medium/High.
- **TIP:** "Professional animators keep all three editors open
  simultaneously in a split layout: Timeline at the bottom for
  global playback, Dopesheet in the middle for blocking passes,
  and Graph Editor at the top for polishing. Use T in the
  Dopesheet to bulk-set interpolation, then switch to the Graph
  Editor to refine individual handles."
- **Use-when lists** include, for the Graph Editor: "Fixing
  foot sliding or floaty movement", "Crafting custom ease-in /
  ease-out feels", "Removing unwanted overshoots on a key",
  "Adding procedural noise or oscillation", "Looping an
  animation with Cycles modifier".

## Claims list (Pass 3 test list)

- **C-10-1** The three motion editors divide labour: Timeline =
  range/playback/markers; Dope Sheet = keyframe timing across
  channels; Graph Editor = interpolation and handles. [slide]
- **C-10-2** Working layout: all three open; bulk-set
  interpolation in the Dope Sheet (T), refine individual handles
  in the Graph Editor. [slide TIP]
- **C-10-3** Handle type changes the motion **without moving
  keys**: Vector = straight segments; Automatic / Auto Clamped
  = smooth eased segments. Menu of record: Free / Aligned /
  Vector / Automatic / Auto Clamped. [demo 20:00–24:30]
- **C-10-4** A 14-frame loop is one sparse channel keyed at a
  handful of frames (columns at 5, 7, 9 seen; range 1–14) with
  matched end values; the Z curve troughs at the mid key
  (≈ −0.657 at f7 against ≈ −0.49 at the ends). [screen]
- **C-10-5** Motion Paths (In Range, keyframe numbers on,
  thickness 6) expose trajectory + key placement in the
  viewport so spacing can be judged in space, not just in the
  editors. [demo 18:00–22:00]
- **C-10-6** Smooth (auto) interpolation can leave an unwanted
  overshoot at a key; removing it is Graph Editor work.
  [slide bullet + curve-dip demo ~22:30]
- **C-10-7** Dope Sheet timing edits (select/move/scale, G/S)
  retime every channel at once without touching interpolation.
  [slide + demo 13:00–16:00]
- **C-10-8** RESOLVED from the harvested narration (below):
  the episode's exercise IS set verbally — the classic
  **bouncing-ball tutorial, converted** ("I'm really kind of
  taking away like the bouncing ball tutorial and just
  converting it into a sex tutorial", ~1:03). No separate
  homework is set in the harvested span (0:00–8:33); the
  remaining narration was still transcribing at report time
  (REPORT.md addendum carries the harvest state).

## Narration addendum (whisper log harvest, 0:00–8:33 of 25:52)

Single-transcriber, tier UNCONFIRMED; screen governs on any
conflict. Loop census on the harvested span (rule
normalized-segment-v1): 87 segments, **0 loop segments,
recoverable share 100%** — continuous real narration (the
instructor teaches a live class; students are present and
ask questions). Points the narration adds to the screen log:

1. **The subject is the bouncing ball.** The cowgirl loop is
   the bouncing-ball exercise re-skinned — the vertical torso
   bob is the ball's bounce. (This retroactively sharpens
   C-10-4: the Z curve's hold-dip-return shape is a bounce
   cycle, and it converges with Pass 3's independently-chosen
   ball subject — the estate exercise and the episode's
   exercise are the same atom.)
2. **Pose-to-pose** is the named working method ("we're going
   to be doing it pose to pose instead of straight ahead") —
   a vocabulary item the estate grammar uses but had not
   sourced.
3. **The trio per the narration** is Dope Sheet + **Motion
   Path** + Graph Editor: "all three of those things lead you
   to the same information… either a debug into what's going
   on with your animation or more fine-grain controls." The
   slide's trio (Timeline/Dopesheet/Graph Editor) and the
   narration's trio differ by one member — recorded as-is;
   the estate model in TECHNIQUE keeps all four surfaces.
4. **Loop closure construction:** the first keyframe is
   duplicated (Shift+D) **to frame 15** — the wrap key sits
   one past the 1–14 playback range, the standard cyclic
   form. (Screen showed range End 14; the key at 15 is the
   closure the range implies.)
5. **Keying practice:** K opens the keyframe menu (the
   instructor notes Blender changed it from I); he keys
   **Location + Rotation + Scale, all channels** ("usually
   you want to do all channels") — matching the 10-channel
   set read off the screen.
6. **The lesson's before-state:** the freshly-keyed loop has
   **no interpolation** — "this is a particularly boring
   animation at the moment… mine doesn't have any
   interpolation between the keyframes" (~7:33). The
   interpolation work that fills the rest of the episode is
   the fix; C-10-3's before/after is the episode's own arc.
7. **Tension, recorded:** the narration's session-start
   setup mentions 30 fps and a frame end of 30 (whisper
   wording is garbled here — UNCONFIRMED). The built file's
   UI of record shows range 1–14 with the wrap key at 15.
   Screen governs; the 30s are read as the scratch setup
   before the prepared file, not the loop's dimensions.

### Continuation — full-transcript harvest (2026-11-06, coordinator harvest item closed)

The primo whisper job (detach `ns10-whisper`) finished
(`ns10-whisper.done` on primo, exit 0). The full transcript
is now in this run dir and in
`repo/results/plan-10-animation-bootcamp-1/`, byte-identical
in both places and to the primo originals (verified by
SHA-256 after transfer): `transcript.srt` 29,252 B,
SHA-256 8646359f383cacbb44b1abd5faeb310ced47e53e365064845896170036f40550;
`transcript.txt` 18,596 B, SHA-256
9d3d1a6fd1d1e4c4b2ba8bb56a6e85070332424c8738a68aef869c1f68f60274.
Single-transcriber tier remains UNCONFIRMED; the screen
still governs on any conflict.

**Coverage, measured:** 299 segments; the last cue runs
25:46.840–25:47.840 ("Thank you."). The media duration of
record is 1,551.53 s (25:51.53, ffprobe; the page states
25:52). The transcript's last cue therefore ends **3.7 s
short of the ffprobe end** (4.2 s short of the page
figure): the closing seconds carry no cues. Coverage is
recorded as reaching 25:47.840 of 25:51.53 — near-complete,
not cue-to-the-final-frame.

**Full-file loop census** (rule normalized-segment-v1,
threshold >8; `loop-census.txt` in this run dir): 299
segments, **12 loop segments, loop share 4.0%,
recoverable 287 segments / 96.0%**, 1 loop phrase. The
single loop phrase is the instructor's rhetorical check
"right?" (×12, at 8:38–22:51) — a speech habit crossing
the threshold, not a silence hallucination; the
recoverable share is read with that in mind. The
harvested-span census stands as labelled above (87
segments, 0.0% loop / 100% recoverable over 0:00–8:33);
this whole-file number supersedes it as the file-level
figure only.

Points the 8:33–25:52 narration adds to the screen log:

8. **Bezier is introduced as the unseen interpolation**
   (8:35): Constant holds until a key is hit; Bezier
   "doesn't really show you anything immediately" — its
   effect (an S-curve slope on the Z channel) is visible
   only in the Graph Editor, channels isolated, Home to
   frame all. This is the narration-side setup for
   C-10-3's before/after.
9. **Splining discipline, stated as method** (11:37–
   12:21): reset everything to Constant in the Dope Sheet
   first, because an interpolation key tells Blender to
   "figure out the animation for me… it's just going to
   guess"; put more information in as keys, *then* spline
   (T → Bezier). The estate's two-level authoring
   discipline (C-10-2) gains its stated rationale: family
   interpolation is applied only after the key set
   carries the intent.
10. **A deliberate, keyed overshoot** (12:22–14:09): the
    trough key is duplicated to frame 8 and a deeper key
    is posed and keyed one frame out — "tap down,
    overshoot, come back up, back to formal pose". This
    is overshoot as an *intentional performance key*, a
    different animal from C-10-6's interpolation-
    manufactured defect; C-10-6's verdict is unchanged,
    and the distinction is now on the record from the
    episode's own narration.
11. **Dope Sheet timing tools, corroborated in
    narration:** T opens the interpolation menu; S scales
    selected keyframes **away from the playhead as pivot**
    (15:07–15:27); box-select + move retimes the down/up
    split (16:44–17:07: five frames down, two deeper, two
    back up, longer rise). C-10-7's slide claim is now
    also demo-narrated, not slide-only.
12. **Motion Paths, narrated in detail** (17:42–19:05):
    reached from the armature's Object Data properties
    in Pose Mode (Shift+H first to isolate the control);
    Calculate draws the path for the selected bones; the
    colour code is **blue = where the animation is,
    red = where it has been, green = where it is going**
    — matching the screen-read panel (Before = red,
    After = green, 22:00). The judgement the tool serves
    is the **spacing between the numbered dots** ("frame
    nine is in the exact same place as five"), and the
    spacing fault he finds there is what sends him to the
    Graph Editor. C-10-5 is corroborated end-to-end.
13. **Handle-type work — the episode's practical core**
    (19:22–25:27): V opens Set Keyframe Handle Type.
    Free = handles move independently; Aligned = the
    other handle moves opposite and proportional; Vector
    = the handle points at the neighbouring key (the
    straight segment he wants on the fall). Vector on
    both sides of a key breaks the smoothing, so the
    worked fix is **Vector on one side, Free on the
    other, handles pointed at each other** — smoothness
    retained, "a very sharp drop" at the bottom kept.
    The Dope Sheet cannot show any of this ("there's no
    way for me to understand what's going on here"),
    which is the narration's own statement of C-10-1's
    division of labour. New vocabulary detail the screen
    log did not carry: **the keyframe symbol changes
    with handle type** (24:17–24:57) — Aligned = diamond,
    Automatic = circle with a dot, Auto Clamped = empty
    circle, Vector = square — so handle type is legible
    from a Dope Sheet overview before entering the Graph
    Editor. C-10-3 is corroborated and extended.
14. **No student Q&A materialises in this span.** The
    introduction (0:30) promises students "asking me
    questions throughout", and the harvested span holds
    the one student-shaped line ("How did the legs
    cross?", 6:14); the 8:33–25:52 span is instructor
    monologue throughout, its only question forms the
    rhetorical "Right?" checks counted in the census.
    The coordinator note's expected Q&A content for this
    span does not occur.
15. **Close and C-10-8, full-file scope** (25:27–
    25:47): the session ends on a next-time preview —
    take the initial pose into the next rotation and
    "make sure that an animation is cycling perfectly
    between each rotation". **No homework or separate
    exercise is set anywhere in 8:33–25:52.** C-10-8's
    resolution therefore stands unchanged, with its
    "no separate homework" clause now covering the full
    25:52, not only the harvested span.
16. **Tension, recorded (axis labels):** at 10:18–10:52
    the narration names the Graph Editor's **x-axis as
    "a value" and the y-axis as "time… measured in
    frames"** — swapped against the editor as read on
    screen throughout this log (time runs horizontally,
    value vertically; the Z curve's trough at frame ~7
    is a horizontal position). The instructor's own use
    in the same breath ("it takes us seven frames to get
    to the bottom") follows the screen's geometry, not
    his labels. Screen governs; the labels are recorded
    as a narration error, not adopted.
17. **Tension, recorded (working numbers):** the
    narration's mid-build numbers — seven frames down
    and "another nine" up, the halfway correction
    16 → 15 (10:52–11:16), the 5/2/2 split (point 11) —
    describe the evolving in-progress key set, not the
    finished file's UI of record (range 1–14, columns at
    5/7/9 read at 24:30). Same family as point 7's
    tension; screen governs, and no claim in this run
    rests on the narration's frame numbers.

**Claim impact of the full span, stated plainly:** no
verdict changes. C-10-8 stands resolved (scope extended,
point 15); C-10-3, C-10-5, C-10-7 gain narration
corroboration; C-10-6 gains the deliberate-vs-manufactured
distinction (point 10); C-10-4's screen basis is untouched
by the narration's working numbers (point 17). Two new
narration/screen tensions are recorded (points 16–17) in
the same form as point 7.

## Surprises vs the SHOULD-BE-SEEN

1. The plan expected a principles lecture (anticipation,
   overshoot, arcs as named principles with exercises). The
   episode is instead **tooling-first**: the principles appear
   only as *consequences of curve shape* (easing, overshoot
   removal, float) inside a Timeline/Dope Sheet/Graph Editor
   lesson, taught on a real two-body loop from the first minute.
   The overshoot principle IS present — as a curve defect to
   fix (C-10-6), not as a performance principle.
2. No bouncing-ball or abstract demo subject: the demo subject
   is the production-style loop itself (14 frames, one channel
   carried end-to-end).
3. The theory content is a designed reference card (12:44),
   not slides of principles — the episode's vocabulary gift to
   the estate is the **editor division of labour** and the
   **handle-type menu**, not new principle names.
