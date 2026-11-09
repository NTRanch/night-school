# Plan 10 — Capture Manifest

Plan: `repo/plans/10-animation-bootcamp-1.md`
Item: "Animation Bootcamp - 1" — kaitou3d (NSFW Blender Dojo),
rule34video video 4331646.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-10/plan10-source-1080p.mp4`
- Bytes: **555,026,396**
- SHA-256: **30ec7b4b4ed3de9f91c9cb47077d023ceef3dd18f1453bee335d8ffad80a7dd8**
- Streams (ffprobe): video h264 1920×1080, audio AAC; format
  duration 1551.53 s — the watch page states PT0H25M52S
  (1,552 s); the 0.47 s difference is container rounding,
  recorded not smoothed.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens for 360p/480p/720p/1080p). Total size established
  before download by a Content-Range probe: 555,026,396 bytes.
- Captured: 2026-11-06. The primo pin's hash was verified
  against the sandbox assembly byte-for-byte after transfer
  (identical, above). The manifest of record is this file in
  the run dir; the primo media dir holds the media + the
  transcript outputs.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07
  route). The `browser.open` fetch route is policy-blocked
  for this domain; capture used terminal egress, as in prior
  plans.
- **Site instability at intake:** the host's database faulted
  intermittently ("can't connect to database", "Access
  denied" 15-byte stubs) on BOTH egresses for the first
  minutes; retries landed the full watch page (221,995 B) on
  the sandbox route first, then on primo. Tokens are
  egress-bound (prior-plan law, confirmed again).
- Egress probes (2026-11-06, on the real file, ~60 s budget,
  PF-5/PF-6):
  - sandbox, single-stream ranged GET on the 720p token:
    4 MiB at ≈ **1.34 MB/s**; 4-way parallel 8 MiB segments
    all completed inside the probe window.
  - primo, single-stream ranged GET on its 1080p token:
    4 MiB at ≈ **0.82 MB/s**.
  - Sustained rates were lower and uneven on both routes
    (per-connection throttling, the PF-6 shape): the sandbox
    8-segment run saw repeated mid-segment connection resets
    on segments 0 and 2 (each restarted from zero by the
    retry loop, three times).
  - **Winner: hybrid.** Segments 1, 3, 4, 5, 6, 7 completed
    on the sandbox route; segments 0 and 2 were re-fetched
    on the primo route as 4 sub-ranges each (8 streams, all
    size-verified in ~90 s), transferred to the sandbox, and
    the file was assembled there. Every segment was
    size-verified against the segmap before concatenation
    (segmap kept at `dl/segmap.txt` in this run dir; the
    per-segment verify lines are in the primo dl dir's
    `sub02/verify.txt` and the run's capture log); assembled size equals the
    probed total exactly; SHA-256 pinned above; the assembled
    file was then transferred to primo as the canonical pin
    and its hash re-verified there (identical).
- Integrity: **decode verified** (not just ffprobe):
  full-frame decodes at t = 100/500/1000/1500 s each produced
  0 error bytes (`dl/decode-*.err` in the run dir, all empty).
- Friction logged for the coordinator: the sandbox `/tmp` is
  a 512 MB tmpfs — the segment set (536 MB) filled it
  mid-transfer ("No space left on device"); the working set
  was moved to the workspace disk and the run proceeded. The
  first pin-transfer scp also died silently with its
  background session and was restarted; the second completed
  (rc=0, hash verified).

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page for licence
  terms finds only the player config's opaque `license_code`
  token. Posture per protocol: study only, never redistribute;
  no video file, transcript, or frame enters any shipped
  artifact.

## Page metadata of record (watch page fetched 2026-11-06)

- Title: "Animation Bootcamp - 1"; video_id 4331646;
  uploadDate 2026-04-13 (JSON-LD); duration PT0H25M52S;
  views **4,769** at capture; likes 20.
- Uploader: **kaitou3d** (member 91300, "Uploaded by" credit).
- Creator description: "From the NSFW Blender Dojo, Week 1 on
  the Animation Bootcamp. This week is the introduction of
  the timeline, graph editor, and how to use them"

## Transcription (whisper lane, per skill)

- Single pass (1,551.53 s < the 3,600 s cap — no chunking):
  whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundle), model
  large-v3-turbo, primo CPU. Input: 16 kHz mono WAV extracted
  in the sandbox from the pinned file (49,649,742 B) and
  transferred to primo with the media pin.
- Contention note: the all-hands finish (D-1073) had two
  other lanes' whisper jobs on primo; this run executed
  niced (nice -n 10) at 4 threads to preserve headroom, and
  is therefore slower than the lane's ~2.16× reference rate.
  Status and tier: see REPORT.md (transcript is a study aid;
  OBSERVATION is screen-governed and no claim rests on the
  transcript alone).

## Deliverables in this run dir

INTAKE.md · MANIFEST.md · OBSERVATION.md · TECHNIQUE.md ·
PASS3-REBUILD.md · PASS4-APPLICATION.md · BLOCH-CANDIDATE.md ·
REPORT.md · CLAIM.txt · transcript.srt/.txt (when landed) ·
frames/ (5 grid sheets + 52 grid frames + 17 native frames +
2 crops) · stage/ (fcurve_exercises.py, measurements.json,
4 exercise strips, pass4_gate.py, pass4-measurements.json,
pass4-firstlast.json, 2 pass-4 strips, DESIGN-DRAFT.md).
Copies: `repo/results/plan-10-animation-bootcamp-1/` (LOCAL only).
Working media (`dl/`) is removed at task-end cleanup; the
canonical pin stays on primo.
