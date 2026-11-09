# Plan 40 — Pass 0 Intake Record

- **Plan:** `repo/plans/40-porn-in-blender-lighting-color.md`
- **Run dir:** `runs/plan-40/` · **Passes executed:** 0–4 (full run,
  under wave contention — see MANIFEST/BLOCH for the slice-ladder
  posture where it applies)
- **Intake completed:** 2026-11-06, before any viewing of the video.
  The only page contact before this record was watch-page metadata /
  `flashvars` fetching to obtain capture URLs — no frame of the
  video itself was viewed before the SHOULD-BE-SEEN and the
  pre-registered questions below were adopted. (First fetches on
  both egresses returned transient origin errors — sandbox 403,
  primo 503 DB-fatal — the known flaky-origin pattern documented
  in Plan 29's manifest; metadata below is completed from the
  successful fetch and recorded in MANIFEST.md.)

## Source record

- **URL:** https://rule34video.com/video/3213694/how-to-make-porn-in-blender-basics-lighting-and-color-grading/
- **Video ID:** 3213694
- **Title (plan):** "How to Make Porn in Blender: Basics — Lighting
  and Color Grading"
- **Creator / presenter (AS SEEN, watch page fetched 2026-11-06
  on both egresses, saved as `dl/page-sandbox.html` locally and
  `dl/page.html` on primo):**
  - "Uploaded by" pill: **Anime Nyan** (member 807029); page
    `video_models` field: **'Anime Nyan'**.
  - The JSON-LD description is written first-person by the
    tutorial's maker ("I create those tutorials, because when I
    first started Blender I struggled…") and names NO separate
    presenter — unlike Plan 02 (RamFutaNSFW presented, Anime
    Nyan sponsoring/uploading), this page presents the uploader
    himself as the teaching voice. Recorded as seen: **creator /
    uploader Anime Nyan**; the "Basics" series voice.
  - Description credits (as seen): Polyfjord's EXR tutorial;
    Waqas Qazi's "Teal and Orange" DaVinci Resolve grading
    tutorial; chapters credited to vadimbanshee405. The
    description links a Google Drive folder with "the finished
    Blender file for thumbnail, power grades and this youtube
    video in 1080p" (link recorded, not followed — study-only).
  - Description chapter list (as seen — the video's own map,
    used in Pass 1 as a cross-check, never as a substitute for
    the screen): … 39:50 Camera · 46:20 Light Start · 59:27
    Light Again · 1:16:39 Interior Light Fix · 1:24:50 Render
    Settings · 1:27:00 Davinci Resolve Start · 1:32:19 Color
    Tutorial for DaVinci Resolve. The grading half is therefore
    expected in **DaVinci Resolve (external tool)** — Q40-G1's
    pre-registered falsifier is already narrowed by the page's
    own text; the screen still governs what the chain IS.
- **Duration:** plan states **1:54:44 (6,884 s)**. The watch page
  JSON-LD states `PT1H54M44S` = **6,884 s — the plan and the page
  agree exactly.** The acquired file's ffprobe governs and is
  recorded in `MANIFEST.md`; if it also reads 6,884 s this plan
  joins 34/37 as a duration exception.
- **Upload date:** 2023-12-23 (page JSON-LD). **Views:** 56,894
  and likes 213 at capture load (JSON-LD). **Categories:**
  "Bleach, Tutorials, Blender"; tags empty.
- **Page-stated licence (verified firsthand):** the JSON-LD
  description states, verbatim: **"This video is under the
  creative commons zero license."** — i.e. **CC0, AS SEEN** in
  the creator's own description text. This differs from Plans
  02/11/13/17 (no licence stated). Recorded exactly as seen;
  the protocol's study-only posture is nevertheless kept for
  the run's artifacts (no frames/transcript ship), and the CC0
  statement is noted for the coordinator as a lane fact.
- **Licence posture (protocol, pre-viewing):** a tutorial is
  studied, never redistributed. No video file, transcript, or
  frame enters any shipped artifact. What ships is the distilled
  technique, re-derived. The page-stated licence (if any) is
  verified firsthand at capture and recorded in `MANIFEST.md`
  exactly as seen.

## SHOULD-BE-SEEN (Pass 0 record)

The plan already carried a SHOULD-BE-SEEN, written 2026-11-05
before any viewing by this run. It is adopted **verbatim**:

> A basics course treatment: light types and placement for bodies,
> exposure discipline, then colour grading in render/compositor —
> with the reasoning shown on examples.

Plan observation foci carried into Pass 1 (from the plan,
pre-viewing): lighting setups per example (fixtures, values,
distances); exposure and colour-management settings (view
transform, look) — numerically; grading chain (where it happens:
render settings / compositor / external tool) node by node;
comparison rows vs Plans 02/11/13 kept in the running
triangulation table.

## Pre-registered claims to test (written before viewing)

- **Q40-L1 (light types/placement for bodies):** the video names
  specific fixture types (Area / Spot / Point / Sun) with
  placement rules for bodies (key/fill/rim roles, distances,
  angles), stated as a *basics* discipline rather than one
  artist's per-shot assembly. Falsifier: fixtures appear only
  as one finished scene's tour, or values are never shown.
- **Q40-L2 (exposure discipline):** an explicit exposure rule
  exists — a numeric exposure / strength discipline (e.g. a
  stated exposure value, a "don't clip" check, or a
  light-strength ratio rule) the student can apply without the
  creator's eye. Falsifier: exposure is tuned silently by eye
  with no stated rule.
- **Q40-C1 (colour management):** the video states its colour-
  management settings numerically — view transform (Standard /
  AgX / Filmic), look, exposure, gamma — as part of the basics.
  Falsifier: the Colour Management panel never appears or is
  never read.
- **Q40-G1 (grading-chain location):** the grade lives in ONE
  named place — render settings, the Blender compositor, or an
  external tool — with a node-by-node chain that can be copied.
  Falsifier: grading is scattered, unnamed, or done in an
  unnamed external app with no chain shown.
- **Q40-G2 (grading contract):** a minimal chain survives across
  the video's examples (the same nodes in the same order on
  more than one scene). Falsifier: each example is graded
  ad hoc with no repeated chain.

## Pre-registered triangulation questions (vs 02/11/13/17)

- **TQ-1 (philosophy — bake vs fix-in-comp):** Does this third
  voice side with **Plan 17's bake-in-render** (relight
  interactively, render once cheap, grade the Combined) or with
  **Plans 11/13's fix-in-comp** (decompose into light-group /
  component passes so comp can re-decide)? Pre-registered read
  rule: if the video teaches per-light or per-component pass
  decomposition as its grading method → 11/13 side; if it
  teaches tuning lamps against the live render and grading the
  combined image → 17 side; if it teaches neither (grade in
  render settings only) → recorded as a third position, not
  forced into either camp.
- **TQ-2 (the dead rim):** Plan 11 measured that Plan 02's
  Rim_Spot has **never lit a pixel** — `Combined_Rim`
  identically zero; the spot at (1.6, 1.5, 2.1) sits behind its
  own backdrop wall (wall at y = +1.3). Does this voice's
  rim/back-light practice **explain** that geometry (e.g. it
  places rim lights where a backdrop would occlude them, or
  never checks the rim's solo contribution), **avoid** it
  (rim placed in front of / clear of the backdrop, or solo-
  checked), or is it **silent** on rim placement geometry?
  The rebuild (Pass 3) additionally measures whether THIS
  run's variant rim contributes nonzero energy.
- **TQ-3 (backdrop/world):** Plan 02: emissive backdrop +
  World 0.000, no HDRI. Plan 17: emissive dome + authored
  gradient world. Where does this voice land — HDRI, emissive
  geometry, world-only, or a mix?
- **TQ-4 (render economics):** Plan 02's pair (NT 0.0100 / max
  4096) vs Plan 17/13's production pair (0.0300 / 512). What
  pair, if any, does this voice teach, and does it present the
  pair as prescription or as a retunable default?
- **TQ-5 (rim colour):** Plan 02 samples rim colour from the
  backdrop's neon; Plan 17's rims are neutral (6500 K family).
  Does this voice tint the rim from the scene, keep it neutral,
  or not address rim colour?

## Comparison inputs (state at intake)

- **Plan 02** (`runs/plan-02/`): LANDED, gated. NS02 "Neon
  Backdrop" template of record: Key Area ~1000 W (0.6×1 m),
  Rim Spot 55°/blend 0.150 ~1000 W magenta-from-backdrop,
  oversized weak Fill, 4× 5 W Point accents, World 0.000,
  Cycles NT 0.0100 / max 4096, 35 mm, 1080×1920. Template files
  are READ-ONLY for this run — the Pass 3 variant is a named
  variant built from a copy, never an overwrite.
- **Plan 11** (`runs/plan-11/`): LANDED. Light Groups pass
  contract + remainder rule (beauty = Σ groups + ungrouped
  remainder); **dead-rim finding** (above, TQ-2) — the template
  fix is a queued Owner/Plan-02 decision, NOT this run's to land.
- **Plan 13** (`runs/plan-13/`): LANDED. Beauty decomposition;
  raw recreation matches at float precision, the denoised
  endpoint is a measured approximation.
- **Plan 17** (`runs/plan-17/`): LANDED. Bake-in-render
  philosophy vs 11/13's fix-in-comp — DIFFERENT-PHILOSOPHY rows
  already recorded; codec conflict DWAA vs ZIP resolved for ZIP.
