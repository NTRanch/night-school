# Plan 37 — Observation (Pass 1) — Full-Span Accounting

Observation base (MANIFEST.md): 36 stills at 2 fps
(`frames/f_*.jpg`) + 18 per-second stills (`frames/sec/s_*.jpg`),
all native 1920×1080, spanning the whole file; hard-cut scans
at scene thresholds 0.4 and 0.12 (`records/scene-cuts*.txt`);
one whisper pass over the audio (`transcript.*`). Container
duration 18.181 s (video stream 18.117 s, 1,087 frames @ 60 fps).

Segment boundaries are ±0.3 s: most transitions in this item
are animated redraws or mostly-white card changes that fall
below scene-scan thresholds. The three anchored hard cuts
(threshold 0.12) are **2.617 s** (title → Step 1 card),
**13.417 s** (cat front → cat profile), and **15.167 s**
(cat → punchline card; the only cut at threshold 0.4).

## Second-by-second log (every second classified)

| Sec | Span (s) | What the screen shows | Class |
|---|---|---|---|
| 0 | 0.0–1.0 | Ornate hand-drawn title card assembling/holding: "How to draw the SEXY" in a decorative frame (`s_00`) | Joke setup (tutorial-parody framing) |
| 1 | 1.0–2.0 | Title card hold; ornament completes (`contact-sheet-1s.jpg` tile 2; `s_02` at the boundary) | Joke setup |
| 2 | 2.0–3.0 | Title card until the anchored cut at **2.617 s**, then the "(Step 1)" card (`s_02`, `f_006`) | Joke setup → step card |
| 3 | 3.0–4.0 | "(Step 1)" card hold (`s_03`) | Step card |
| 4 | 4.0–5.0 | Near-blank page; the first sphere's arc appears faintly at top — drawing begins (`s_04`) | Drawing demonstration |
| 5 | 5.0–6.0 | Two overlapping spheres with cross-contour guidelines, drawn/refined on screen (`s_05`, `s_06` at the boundary) | Drawing demonstration |
| 6 | 6.0–7.0 | "(Step 2)" card (`f_013`, `f_014`) | Step card |
| 7 | 7.0–8.0 | The spheres are extended into a full construction figure: torso cylinders above, thigh forms below (`f_015` → `f_016`) | Drawing demonstration |
| 8 | 8.0–9.0 | Construction figure refined (`s_08`); by ~8.5 s the construction is replaced by clean line art, a cartoon cat's ears entering at the bottom of frame (`f_017` → `f_018`) — the intermediate work is elided | Drawing demonstration → finished-piece transition |
| 9 | 9.0–10.0 | Finished clean line art, rear view from below: buttocks in underwear under a short skirt, the cartoon cat's head censoring the crotch; slow zoom in (`s_09`, `f_019`) | Finished-piece showcase |
| 10 | 10.0–11.0 | Zoom continues (`s_10`); "(Step 3)" card begins ≈10.3 s (`f_021`) | Showcase → step card |
| 11 | 11.0–12.0 | "(Step 3)" card hold (`s_11`, `f_022`); the cat-front view resumes late in the second (`f_024`, t≈11.5) | Step card → joke |
| 12 | 12.0–13.0 | The cartoon cat, front-facing, held in front of the drawing (`s_12`) — no drawing occurs | Joke (mascot beat) |
| 13 | 13.0–14.0 | Cat front until the anchored cut at **13.417 s**, then the cat in profile (`s_13` front at 13.0; cut record) | Joke |
| 14 | 14.0–15.0 | Cat in profile, tongue out, licking its raised paw (`s_14`, `f_030` at ≈14.5) | Joke |
| 15 | 15.0–16.0 | Cat front again at 15.0 (`s_15`); anchored cut at **15.167 s** to the punchline card: a drawn woman in profile glancing back over her shoulder, handwritten text **"you learned nothing ~"** + heart (`s_16`) | Joke punchline |
| 16 | 16.0–17.0 | Punchline card hold (`s_16`) | Joke punchline |
| 17 | 17.0–18.181 | Punchline card hold; the white background fades to grey by ≈17.5 s (fade-out; `s_17` white at 17.0, `f_036` grey at ≈17.5); file ends at 18.181 s | Joke punchline / fade-out |

**Accounting check: 18 of 18 seconds classified, plus the
0.181 s container tail (inside second 17's row). No second
is unaccounted.**

Class tally (by second, a second split between classes is
counted under its first class): joke setup / step cards /
mascot / punchline **11 s** (0, 1, 2, 3, 6, 10, 11, 13, 14,
15, 16, 17 — 12 rows, of which seconds 2/10/11 are shared
with transitions); drawing demonstration **4 s** (4, 5, 7, 8);
finished-piece showcase **1 s** (9) plus the shared second
10. Drawing content of any kind occupies ≈5 of 18 seconds,
and none of it is explained: there is no narration (audio =
music only, below), no caption, no annotation — the step
cards carry numbers and nothing else.

## What the three "steps" actually contain

- **Step 1 (≈3.4–6.0 s):** draw two overlapping spheres with
  cross-contour guidelines. This is the only self-contained
  drawing act in the item, and it is a genuine construction
  shorthand (spheres as buttock volumes).
- **Step 2 (≈6.9–10.3 s):** the spheres are extended into a
  construction figure (torso/thigh forms), then — with all
  intermediate work elided — clean finished line art appears,
  censored by the creator's cartoon cat. The gap between
  construction and finish is the joke's mechanism: the
  "draw the rest of the owl" elision, performed straight.
- **Step 3 (≈11.4–15.167 s):** no drawing at all. The cat
  mascot animates (front hold → profile paw-lick → front)
  in front of the finished piece. A step in name only.

## Audio

One AAC stereo stream, 48 kHz, continuous: silencedetect
(−35 dB / 0.5 s) finds zero silence events; volumedetect
mean −17.4 dB, max −1.2 dB. Single whisper pass
(`transcript.txt`): one segment, 0.00–18.08 s, text
"*outro music*" — **music only; no speech, no lyrics, no
narration**. The page tag "background music" agrees. The
screen therefore governs entirely (protocol), and the screen
contains no instruction beyond the step numbers.

## Claims list (for Pass 2)

- **C-01 (the title's implied claim):** that following the
  three steps teaches how to draw "the sexy". **Refuted by
  the item itself**: its final card states "you learned
  nothing", its page description states "Haha u learnt
  nothing", Step 3 contains no drawing, and Step 2 elides
  the work that would constitute the teaching.
- **C-02 (Step 1's implicit construction claim):** that two
  overlapping cross-contoured spheres serve as the volume
  construction for the buttocks in the finished view.
  Shown on screen (the spheres persist as the buttock
  volumes through the Step 2 construction), but **never
  asserted as a sufficiency claim** — no before/after is
  offered, and the item's own punchline disowns the
  tutorial framing wholesale. Recorded in TECHNIQUE.md as
  an observed construction fragment, not a claim under test.
