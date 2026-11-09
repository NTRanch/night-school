# Plan 14 — Structural Observation (sparse sampling, triage scope)

This is **not** a Pass 1 timed observation. Per the triage
brief, the observation base is sparse structural sampling
sufficient to classify production format and structure:
25 stills at 30 s spacing over the full runtime, 36 further
stills around the episode boundary, Episode 2's opening, and
the tail (61 stills total), plus a whole-file hard-cut scan
(ffmpeg scene threshold 0.4; `records/scene-cuts-clean.txt`,
37 cuts) and the stream facts in MANIFEST.md. What follows
describes **structure and format only** — no scene content is
written up, by design.

## 1. Format

- One file, 716.480 s, 1920×1080 at 60 fps, h264 + AAC stereo
  (48 kHz, `eng`). A 3D-animated narrative item (page
  categories 3D / Hentai / iwara / Tutorials).
- A corner watermark ("NTRgasm") is present in effectively
  every sampled frame of both episodes — a maker/series mark
  burned into the published file.
- All dialogue text sampled is burned-in in-story text
  (speech bubbles and caption lines), not subtitles-as-track
  (the file has no subtitle stream; ffprobe shows exactly two
  streams) and not instruction. A black frame at t = 90 s
  carries dialogue text alone — a dialogue-on-black beat
  inside Episode 1, not a title or lesson card.

## 2. Structure — two episodes, split at ~355 s

| Segment | Span (s) | Length | Structural evidence |
|---|---|---|---|
| Episode 1 ("Futa Tutor") | 0 – ~355 | ~355 s (~5:55) | One cast and one domestic setting throughout the grid samples t = 0…330 s; the plot set-up is in the opening dialogue (a hired tutor). Hard cuts are frequent (30 of the 37 scan cuts fall at or before this span's end, several at exact 10 s joins — 240/250/260/270/280/290/300/310 — suggesting assembly from short rendered clips). |
| Episode 1 end cards | ~356 – ~364 | ~9 s | Full-frame maker logo card (sampled at t = 356/358/360 s), then a "Thanks for watching / To be contnued………………" [sic] card (t = 362 s), then black (t = 364 s). The scan's cut at **355.3 s** is the episode boundary. |
| Episode 2 ("Futa Black Date") | ~365 – ~686 | ~321 s (~5:21) | A different cast and settings (café, club, bathroom in the samples). Its opening (~365–~454 s) is fade-linked: the scan finds **no hard cut between 355.3 s and 444 s**, while the stills change scene repeatedly through black/dark frames (t = 368 s black; t = 408–440 s very dark) — dissolves/fades, not cuts. A cut cluster at 444/446.8/450.1/454.3 s opens a long segment with **no hard cut at all from 454.3 s to 686.1 s** (231.8 s) — one continuous-feeling closing scene. |
| Closing segment + end card | ~686 – 716.48 | ~30 s | Cuts at 686.1 and 696.1 s; a bedroom scene whose cast differs from Episode 2's closing scene (preview-like; sparse sampling cannot prove intent, and none is claimed). "THANKS FOR WATCHING…" overlay at t = 710 s, SubscribeStar overlay at t = 714 s, cut at **715.35 s** to a full-frame SubscribeStar end card that runs to the end of the file. |

So the title's "Ep-1,2" is literal and the split is
discernible from structure alone: **Episode 1 ≈ 355 s,
Episode 2 ≈ 352 s including its closing segment and end
card** — a roughly half-and-half bundle of two separately
finished episodes, each with its own end furniture (Episode 1
kept its own "thanks / to be continued" card inside the
bundle, which is the clearest sign the two were published or
produced as separate instalments and later concatenated).

## 3. Tutorial-marker checklist (the classification test)

Checked across all 61 sampled stills:

| Marker | Found? |
|---|---|
| Software / engine UI on screen | **No** — no UI of any kind in any sample |
| Instruction or step text addressed to a viewer | **No** — all text is in-story dialogue, logo cards, end cards, or promotion |
| Narration / presenter addressing the audience | **No** — dialogue sampled is character-to-character; the only audience-addressed text is the end-card thanks and the SubscribeStar promotion |
| Demonstration of a process (hands, tools, settings, before/after) | **No** |
| Series/brand marks of a *content* serial | **Yes** — corner watermark throughout, logo card between episodes, "to be continued" card, subscription end card |

0 of 4 tutorial markers; 4 of 4 sampled text classes are
content furniture. Together with the page record (INTAKE.md
evidence table), this is the basis for the CONTENT
classification.

## 4. What was deliberately not done

- No full viewing, no timed content log, no transcription —
  the plan's gate does not ask for them and the triage brief
  forbids inflating the run into one.
- No claim about animation technique, rig, or engine: the
  stream handler strings ("Mainconcept … Media Handler") are
  recorded as seen in MANIFEST.md, and no engine attribution
  is built on them. A production-format *finding* worth
  distilling did not emerge — only the bundle structure in
  §2, which is a release-format note, not a technique.
