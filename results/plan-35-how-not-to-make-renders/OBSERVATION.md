# Plan 35 — Pass 1 Timed Observation Record

- **Plan:** `repo/plans/35-how-not-to-make-renders.md`
- **Video:** shadowyartsdirty (recorded by; uploaded by
  shadowyartsporn), "How not to make rule 34 renders in Blender" —
  rule34video 3352570, upload 2024-03-24, page-stated licence:
  **none**. Duration 20:29 (page PT0H20M29S = 1,229 s; file
  ffprobe 1228.567 s).
- **Media of record (primo):**
  `~/.local/share/pax/night-school/plan-35/plan35-source-720p.mp4`
  — SHA-256 `a46e3bea3be1d50f660c00ba5d892d276efa415b2c3a49400fa6fc3cd1990c1e`,
  523,120,487 bytes, h264 1282×720 + AAC. Provenance in
  `MANIFEST.md` (this run dir + a copy beside the media on primo).
- **Transcript:** primo `~/.local/share/pax/night-school/plan-35/transcript.txt`
  (+ `.srt`; copy in this run dir). Single pass (1,228.567 s < the
  3,600 s cap), chunked-transcription skill lane, whisper-cli
  (whisper.cpp 1.9.2) + ggml-large-v3-turbo, primo CPU, nice'd at
  4 threads under a tenant training job. Single-transcriber,
  **UNCONFIRMED tier**. Loop census recorded in `MANIFEST.md`.
  The transcript's content is addressed in §2 — it is song lyrics,
  not narration.
- **Frames:** 31 grid stills at 40 s spacing (t = 5…1205 s),
  native 1282×720, primo `~/.local/share/pax/night-school/plan-35/frames/`
  (copies in this run dir's `frames/`, g01–g31). Every frame was
  read for this record; the four contact grids and the targeted
  native frames g27 (t=1045) and g31 (t=1205) were read at full
  resolution.

## 1. HEADLINE: the plan's premise is REFUTED by the screen

The SHOULD-BE-SEEN (adopted verbatim at intake, from the plan)
expects:

> A tour of bad renders with the defects named: lighting sins, anatomy/pose sins, material sins, composition sins — each shown, not just described.

**That video does not exist at this URL.** What the screen shows,
in every one of the 31 grid frames spanning the full 20:29, is a
single continuous **Blender screen-recording of the creator posing
two characters for one scene** — Gwen Tennyson and a shark-like
character (Helen Wheels), per the .blend file's own title bar:
"…\Ben 10\Made using assets\Just Helen Wheels\Helen Wheels and Gwen
Comic one\Helen Wheels and Gwen getting close one.blend" (g31,
t=1205, read at native resolution). This matches the watch page's
own description, recorded at intake: *"Behind the scenes of a
romantic fan fiction comic I am working on featuring Gwen and
Hellen Wheels in romantic situation."* The title "How NOT to make
rule 34 renders" is ironic/clickbait framing over a behind-the-
scenes posing session; no failure catalogue is presented.

**Scores against the SHOULD-BE-SEEN, item by item:**

| SHOULD-BE-SEEN element | Seen? | Evidence |
|---|---|---|
| Tour of bad renders | **NO** | One work-in-progress scene, posed continuously; the only finished render shown is the creator's own current scene (Render Result, t≈1045, g27) |
| Defects named | **NO — zero** | No narration, no captions, no text overlays naming any defect, in any frame |
| Lighting sins shown as examples | **NO** | Lighting is never presented as an example of anything; a World HDRI + Sun setup is visible incidentally (g31) |
| Anatomy/pose sins shown as examples | **NO** | Posing is the activity, not the subject; no pose is held up as wrong |
| Material sins shown as examples | **NO** | No material is discussed or showcased as a failure |
| Composition sins shown as examples | **NO** | One camera framing is set up incidentally (t≈845–925); never critiqued |

## 2. What the audio is

There is **no spoken narration at any point**. The audio track is
music with sung lyrics; the whisper transcript is lyric fragments
(e.g. an insomnia-themed song in the opening minutes) interleaved
with long repetition loops over instrumental stretches — the loop
census in `MANIFEST.md` quantifies the loop share. Nothing in the
audio names, describes, or diagnoses any render defect. Any
"transcript claim" about technique in this video would be a
hallucination; none is recorded.

## 3. Timed record — what actually happens on screen

All times from the grid/targeted frames; the activity is
continuous posing, so the record is by phase, not by technique.

| Span | What the screen shows | Frames |
|---|---|---|
| 0:05–5:25 | Blender (Layout workspace, Pose Mode) — the creator poses the two characters on a dark wedge/roof prop: rotating limbs, moving the shark character's tail, adjusting Gwen's arms/head. Grey-clay and textured viewport states alternate. Outliner shows the Gwen rig/body/clothing collections. | g01–g09 |
| 5:25–8:05 | Close posing work: legs/feet, then faces — Gwen's head tilted toward the shark character's head, eyes/expression adjusted via rig controls (visible face close-up, g10 t=365). | g09–g13 |
| 8:05–11:25 | Wider posing: full-figure adjustments, hand placement on the other character's body, tail wrapped around Gwen; weight/position corrections on the wedge. | g13–g18 |
| 11:25–14:05 | Detail passes: hands/fingers against the shark character's back, torso contact adjustments, hip/leg contact close-ups. | g18–g22 |
| 14:05–15:25 | Background/camera phase: an HDRI landscape backdrop appears in the viewport (mountain dusk scene, g23 t=885); camera framing of the posed pair against it; one grey mesh close-up (weight/vertex-group panel visible, g25 t=965). | g22–g25 |
| 15:25–17:05 | Camera-perspective framing of the pair on the wedge; shape-key panel visible (g26 t=1005). | g25–g27 |
| ≈17:24 | **The video's only finished render**: Blender Render Result (Frame 12, 2.70 s render) — the posed pair on the black wedge against a pale dusk sky (g27, read at native resolution). Recording overlay shows the capture at 00:17:24. | g27 |
| 17:05–18:05 | A second render result / file-save dialog (Blender File View, PNG output settings) — the creator saves the render. | g28 |
| 18:05–20:29 | Back in Pose Mode for further adjustment of the same scene (vertex groups / DEF- bones visible, g29; final frame g31 t=1205: Blender **4.0.2**, Pose Mode, file title as quoted in §1; World nodes show an equirectangular HDRI "…dusk…" texture, Strength 0.500; Sun.001 in the outliner). The video ends mid-work, still posing. | g29–g31 |

**Tools/settings readable on screen (copied, not paraphrased):**
Blender 4.0.2 (g31 status bar); render: Frame 12, Time 00:02.70,
Mem 844.74M (Peak 927.44M) (g27 header); World: HDRI
equirectangular, Strength 0.500 (g31 node editor); objects include
`Sun.001`, `Plane`, `Gwen_Pants`, `Gwen_Shirt`, `Gwen_Shirt_Lifted`,
`Gwen_Shoes`, `Gwen_Kneesocks`, `Gwen_Panties`,
`Gwen_Earrings & Hair Clip` (g31 outliner). The render resolution
shown in early frames is 1401×1139 px at 100% (grid frames,
right-side properties) — portrait framing for a comic panel.

## 4. The plan's three foci — answered plainly

1. **Every defect class named, with its on-screen example:**
   **zero.** No defect class is named anywhere in the video —
   not in narration (there is none), not in captions or overlays
   (there are none), not in on-screen text.
2. **The creator's diagnosis per defect (cause, not symptom):**
   **zero.** No diagnosis of any kind is stated. Cause count: 0.
3. **Defects shown but NOT named (the plan's "interesting ones"):**
   The video shows a work-in-progress scene, not defect examples.
   Observer reads of the one finished render (g27) — the shark
   character's tail/body interpenetrating Gwen's legs, a stiff
   contact read, the untextured black wedge — are **this run's
   reads of an unfinished scene, not defects the creator shows
   as defects**, and are therefore **not** entered into the
   taxonomy as Plan 35 material. Logging them as the video's
   unnamed catalogue would fabricate the very deliverable the
   plan wants. Count of creator-presented unnamed defects: **0**.

## 5. UNREADABLEs and disagreements

- **UNREADABLE count: 3.** (1) The full HDRI filename in the
  World node editor (g31) — only "…dusk…" is legible. (2) The
  middle span of the .blend path in the title bar (g31) —
  partially legible, quoted only where read with confidence.
  (3) The exact glyph string on TG3-Y1's shirt in the Pass 3
  exercise sheet (an estate artifact, not this video) — read as
  a text print; exact letters not asserted (the TG3 report
  records "CALIN"; this run's sheet read could not confirm the
  letters at sheet size).
- **Screen vs narration disagreements: 0** — there is no
  narration to disagree with. **Screen vs plan disagreements: 1,
  total** — the premise itself (§1). **Screen vs page
  description disagreements: 0** — the page description
  ("behind the scenes of a romantic fan fiction comic") describes
  the actual video accurately; the plan's intake premise, not
  the page, was wrong.

## 6. Claims list (Pass 1 → Pass 3 test list)

The video makes **no claims** about any technique. The single
claim under test in this run is the plan's own premise:

- **C-35-1:** "This video is a failure catalogue: bad renders
  shown with defects named (lighting / anatomy-pose / material /
  composition)." — **REFUTED** (§1, §3, §4). Pass 3 proceeds on
  the plan's rebuild spec adapted to this evidence; see
  `TECHNIQUE.md` §1 for the provenance ruling.
