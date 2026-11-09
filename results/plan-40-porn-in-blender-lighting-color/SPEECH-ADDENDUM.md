# Plan 40 — speech addendum (harvest closed 2026-11-08, night lane)

Generated 2026-11-08. Tier UNCONFIRMED (single transcriber).
This is the artefact `finish.sh` (primo plan dir) was staged to
produce once `ns40-chain.done` landed (it landed 2026-11-07
04:39); the finisher was never run on primo — its census path
(`~/workspace/custom-skills/...` on primo) does not exist there
(the estate copy of loop_census.py lives in plan-17's primo dir).
The stitch + census below were executed sandbox-side with the
canonical skill script over hash-verified copies of the primo
files (slice/chunk .srt hashes match primo originals).

## Slice censuses (normalized-segment-v1, threshold >8)

- slice E: segments=163 loop_segments=22 loop_share=13.5%
  (reproduces OBSERVATION §8 exactly — pipeline cross-check)
- slice A: segments=190 loop_segments=0 loop_share=0.0%
- slice B: segments=316 loop_segments=11 loop_share=3.5%
- slice C: segments=207 loop_segments=0 loop_share=0.0%
- slice D: segments=147 loop_segments=0 loop_share=0.0%

Slice spans (MANIFEST): E 0–480 s · A 2340–3540 · B 3540–4740 ·
C 4740–5940 · D 5940–6884 — 5,264 s of 6,884 s ladder coverage.

## Full transcript (chunked lane)

Chunk map: chunk1 0–3300 s · chunk2 3300–6900 s (media
6,884.033 s). Stitch: chunk2 offset +3300 s, `[SEAM]` marker —
**1,080 + 544 = 1,624 segments; last segment ends 6,883.58 s
≤ 6,884.033 s duration — stitch_verify PASS, no overshoot.**
`transcript-full.txt` in this run dir.

- loop_census_chunk1: segments=1080 loop_segments=132 loop_share=12.2%
- loop_census_chunk2: segments=544 loop_segments=0 loop_share=0.0%
- loop_census_transcript-full: segments=1624 loop_segments=132
  loop_share=8.1% recoverable_share=91.9%

Files: slices A–D (.srt/.txt) installed in `slices/` beside
slice E (A.srt sha256 8e3a85c7…, B.srt 8b470e47…, C.srt
c5c946e3…, D.srt ef9442a8…); chunk .srt originals remain on
primo (`plan-40/chunks/`). OBSERVATION §8's "slices A–D still
in flight" is superseded by this addendum. No claim in
OBSERVATION §§2–7 rests on speech; no verdict changes.
