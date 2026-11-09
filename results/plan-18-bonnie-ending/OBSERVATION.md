# Plan 18 — Pass 1 Timed Observation

Artefact as captured (INTAKE.md): a 1020.07 s Source
Filmmaker session recording (30,602 frames @ 30 fps) in which
the creator finishes one 20.000 s shot — the ending of the
Bonnie series scene. All frame ranges below are recording
frames @ 30 fps unless marked "shot-time" (the SFM timeline's
own seconds). Every number traces to `records/` in this run
dir or to a named frame.

## §0 Safety-clause verdict (taken before Pass 1)

Depicted figures are the SFM elements `bonnie_male1` and
`bonnie1`: adult-proportioned FNAF animatronic robots in all 34
grid frames. **Clause not triggered** (full record in
INTAKE.md).

## §1 Beat map of the recording (what the artefact is, by frame ranges)

| # | Recording frames | Time | Phase | Evidence |
|---|---|---|---|---|
| 1 | f0–f750 | 0.00–25.0 s (2.5%) | **Intro + survey.** Post-edit overlays (HSTUDIOS logo animation, editor credit, music credit "Animal Crossing Theme LoFi") over the SFM session; Motion Editor open, whole-shot time selection (≈ shot-time 0–20 s), `rig_hand_L` of `bonnie_male1` selected | intro sheet (2 fps); frames i003/i013 on primo |
| 2 | f750–f29460 | 25.0–982 s (93.8%) | **The finishing pass.** Lighting build (element list grows: `light3` by ~360 s, `light5`/`light6` by ~870 s), volumetric work, work-camera surveys, scrub-review fragments, small motion-editor work — all with the playhead parked (see §3) | 30 s grid g02–g33; cluster table §3 |
| 3 | f29460–f30150 | 982–1005 s (2.3%) | **Parked frame.** Viewport motion energy mean **0.0047** over 661 consecutive frame pairs (max 0.24, a cursor-class blip) — a true freeze, not an animated hold | `records/viewport-energy.csv`, window 960–1020 |
| 4 | f30150–f30602 | 1005–1020.07 s (1.5%) | **Credit cards** over the blurred frozen scene: "THANKS FOR WATCHING!" ≈1005–1010 s → "EDITED WITH THE HELP OF @OpacityNSFW" ≈1010–1014 s → Patreon/Twitter/allmylinks card ≈1014–1020.07 s | outro sheet (1 fps); full-frame energy transitions at 1005 / 1010 / 1014 / 1019 s |

Sub-events inside phase 2 worth naming (all measured, all
visually resolved — none is a playback):

- **480–512 s cluster:** the recording's largest sustained
  viewport motion (per-second viewport means to 9.7; full-frame
  per-second peak 18.46 at 500 s). Resolved on the 2 fps
  viewport sheet: **work-camera flight** — the camera flies
  through the hallway, overhead, and into light blowouts while
  lights are placed. Camera work, not scene motion.
- **579.33 s:** one of only three scene-cut-detector firings in
  the whole file (60.07, 61.43, 579.33 at threshold 0.4) — a
  **volumetric light blowout** filling the viewport for ~3 s
  (frames c566–c594 on primo), i.e. a lighting state change,
  not an edit cut.
- **630–645, 720–740, 840–910 s clusters:** repeated short
  viewport bursts (single-second spikes 5–12 with near-zero
  between) — **scrub fragments and light/camera adjustments**,
  resolved on the late/cut sheets.

## §2 Beat map of the shot (the ending itself)

What the artefact states about the ending shot, exactly:

- **One clip, one take.** The Clip Editor (crop of the t≈990 s
  frame, `frames/crop-g34-timeline.png`) shows a single clip,
  `shot1`: "scale 1.00 offset 0.000 **duration 20.000**",
  spanning session time 0–20 s on a seconds ruler. There is no
  second shot and no internal cut in the ending.
- **The creator treats it as one unit:** in the Motion Editor
  the time selection (light-green span) covers ≈ the whole
  0–20 s shot in frame after frame (g01, i013).
- **The parked tableau (shot-time 0, the only shot pose the
  recording ever shows):** leader standing behind, hands at
  the follower's back/hips; follower on all fours, head up and
  turned; both are blue animatronic rabbits with glowing eyes;
  the follower's face carries purple lip and eye makeup. This
  pose is identical in the secondary (camera2) viewport at
  t≈0 s, 900 s, and 990 s — the playhead never leaves it.

### UNREADABLE register (the plan's core questions, honestly bounded)

| ID | Item | Why it cannot be read from this artefact |
|---|---|---|
| U-1 | Build / peak / settle boundaries inside the 20 s shot | The creator never plays the shot through (§3); no frame range of the recording contains the shot's motion |
| U-2 | Reaction animation at the peak (expression/posture change vs before) | Only the shot-time-0 tableau is ever displayed; a single parked pose carries no change |
| U-3 | The shot's final hold (length; breath/micro-motion in it) | The shot's last seconds are never displayed at all |

## §3 The no-playback finding (measured)

Three independent lines of evidence say the shot is never
played through in this recording:

1. **Playhead readouts:** both SFM viewport time readouts read
   **0.000** in all 34 grid frames and in every full-res frame
   inspected across the session (0 s, 360 s, 870 s, 990 s
   sampled by name).
2. **Cluster resolution:** every sustained-motion cluster in
   the per-frame motion-energy record (file-wide mean 0.235,
   median 0.015) was visually resolved: 0–80 s = intro overlays
   + work-camera survey; 230–255 s = scrub bursts; 480–512 s =
   camera flight; 566–595 s = volumetric blowout; 630–645,
   720–740, 840–910 s = scrub fragments / adjustments. None is
   body-motion playback.
3. **No qualifying window exists:** no ≥15 s window in either
   energy record shows the sustained, moderate, body-only
   motion a 20 s shot playback would produce; the longest
   near-zero stretch (982–1004 s, mean 0.0047) is the parked
   frame of §1 phase 3.

The creator's review method in this session is **scrubbing +
parked-frame inspection**, not playback. That is itself the
session's craft fact — and it caps what a beat study of the
shot can claim.

## §4 SHOULD-BE-SEEN scored

Plan's expectation: *"The final beat of the series scene: how
motion, reaction, and timing close the loop."*

| Item | Verdict | Evidence |
|---|---|---|
| Motion closing the loop | **NOT SEEN** | §3: the shot's motion is never displayed |
| Reaction at the close | **NOT SEEN** | U-2: only a static frame-0 tableau exists in the artefact |
| Timing of the close | **PARTIALLY SEEN** | At artefact level only: the close is one 20.000 s terminal take (no cut, no loop — §2), finished by a dedicated lighting/camera pass and closed at publishing level by a frozen frame + three credit cards (§1 phases 3–4) |
| Surprise (recorded per protocol) | The premise itself: duration (28×), medium (SFM, not a finished clip / not Blender), and type (finishing session, not the clip) all differ from the plan | INTAKE.md |

## §5 Claims list (for Pass 2/3 disposition)

- **C-1** [SCREEN] The ending is a single SFM shot clip,
  duration 20.000 s, session time 0–20 s, no internal cut.
- **C-2** [SPEECH 0:57–1:22, partial transcript] The creator
  disclaims formal lighting theory: "I just do what looks
  good for me personally" — three-point lighting is named as
  hearsay he works around, by eye.
- **C-3** [SPEECH 1:10–1:26] Rim light defined operationally
  ("a light [that] lights up the rim"); his first rim attempt
  is self-flagged as bad ("That is a very bad rim light. It's
  not on a good angle.") — a failure shown and then worked,
  in the session's first two minutes.
- **C-4** [SPEECH 1:26–1:43] The radius slider "can diffuse
  lighting"; demonstrated with a volumetric light.
- **C-5** [SCREEN] The finishing pass is performed on a parked
  playhead: lights, volumetrics, and camera are authored
  against a frozen tableau and reviewed by scrubbing, never
  by through-playback.
- **C-6** [SCREEN] The publishing-level ending: frozen final
  frame held under three sequential credit cards (~5 s /
  ~4 s / ~6 s), i.e. the recording's terminal hold is a
  still, not an animated hold.
