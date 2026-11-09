# Plan 11 — Pass 0 Intake Record

- **Plan:** `repo/plans/11-porn-in-blender-light-aovs.md`
- **Run dir:** `runs/plan-11/` · **Passes executed:** 0–4 (full run)
- **Intake completed:** 2026-11-06 (before any viewing of the video;
  the only page contact before this record was the watch page's
  metadata / `flashvars` block, fetched to obtain the capture URLs —
  no frame of the video itself was viewed before the SHOULD-BE-SEEN
  below was adopted).

## Source record

- **URL:** https://rule34video.com/video/4316378/how-to-make-porn-in-blender-light-aovs/
- **Video ID:** 4316378
- **Title (page):** "How to make Porn in Blender - Light AOVs"
- **Creator / uploader (AS SEEN on the watch page, fetched
  2026-11-06, saved as `dl/page-sandbox.html` in this run dir and
  `page.html` on primo):**
  - "Uploaded by" pill: **divinitystudiox** (member 4570966).
  - Description links the creator's Patreon / SubscribeStar as
    "divinitystudio" / "divinity-studio" — recorded as seen:
    creator **divinitystudiox (Divinity Studio)**. The plan's
    creator field ("category listing shows none") is corrected
    by this intake: the watch page names the uploader.
  - `video_models` field: empty.
- **Duration:** 0:19:15 — page JSON-LD `duration: PT0H19M15S` =
  1,155 s, matching the plan's stated 19:15 exactly. The acquired
  file's ffprobe / packet-span duration is recorded in
  `MANIFEST.md` and governs if it differs.
- **Upload date:** 2026-04-03 (page JSON-LD `uploadDate`).
- **Views:** 15,937 on the capture page load (2026-11-06, JSON-LD
  `userInteractionCount`); likes 88.
- **Categories / tags (page `flashvars`):** categories "3D,
  Tutorials, Final Fantasy vii, Blender"; tags "big breasts,
  sound".
- **Description (creator's own words, AS SEEN):** "In this video
  I will reveal a powerful mechanism that every serious blender
  user should utilized. And that's 'Light Groups'. You ability
  to instantaneously change lighting properties without the need
  to re-render is a crucial tool…" — plus a YouTube mirror link
  and Patreon/SubscribeStar links. **Intake premise note:** the
  title says "Light AOVs"; the creator's own description names
  the mechanism **Light Groups** (Cycles' per-light-group passes,
  exposed to the compositor — in current Blender these surface
  alongside the AOV outputs). Pass 1 scores the title's framing
  against what is actually configured on screen.
- **Available renditions (page `flashvars`):** 360p, 480p, 720p
  only — **no 1080p rendition is offered** (720p is flagged HD).
  Capture is the 720p rendition (the highest offered); total size
  established by Content-Range probe before download:
  310,708,360 bytes. See `MANIFEST.md`.
- **Page-stated licence (verified by this run, not inherited):**
  **none stated.** A full-text search of the watch page for
  "license" / "licence" / "creative commons" / "CC0" finds no
  licence statement for this video (the only hit is the player
  config's opaque `license_code` token, which is not a licence).
  Recorded exactly as seen: no licence. Protocol posture
  therefore governs in full: the video is studied, never
  redistributed — no video file, transcript, or frame enters
  any shipped artifact; what ships is the distilled technique,
  re-derived. Study-only.

## SHOULD-BE-SEEN (Pass 0 record)

The plan already carried a SHOULD-BE-SEEN, written 2026-11-05
before any viewing by this run. It is adopted **verbatim** as
this run's Pass 0 record:

> A focused technique video: AOV setup in Cycles, per-light group
> passes, and the compositor build that relights the beauty from
> passes.

Plan observation foci carried into Pass 1 (from the plan,
pre-viewing): AOV/light-group configuration exactly as set;
compositor node tree in full order; what the artist adjusts in
comp vs what still forces a re-render; file format and colour
pipeline for the passes (EXR settings).

## Input artifact (Pass 3)

The Plan 02 scene template (`runs/plan-02/rebuild/`:
`build_template.py` + `template-nswfw.blend` /
`template-sfw.blend` + `render-nswfw.png` / `render-sfw.png`;
rig per its TECHNIQUE.md / PASS3-REBUILD.md: Key_Area /
Rim_Spot / Fill_Area / Accent_Point_1…4 roles, 35 mm portrait
camera 1080×1920, Cycles adaptive 0.0100 / 4096, CPU, seed 0).
This run's variant extends a **copy** — Plan 02's files are
never modified.
