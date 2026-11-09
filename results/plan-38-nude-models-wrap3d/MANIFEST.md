# Plan 38 — Capture Manifest

Plan: `repo/plans/38-nude-models-wrap3d.md`
Item: "How to Make Nude Models in Blender through Wrap3D",
rule34video video 3213869, uploaded by **Anime Nyan**
(page info block, as seen), upload date 2023-12-23 (JSON-LD).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-38/plan38-source-1080p.mp4`
- Bytes: **5,020,677,997** (CDN Content-Range total, probed
  before download; assembled file size exact).
- SHA-256: **d04a49d90757929dfa736e1f769d662720b137e7e5846dcce9e1ff6fef3896a1**
  (primo assembly; see "Two assemblies" below).
- Streams (ffprobe, primo): video h264 1920×1080 @ 60 fps;
  audio AAC. Format duration **12054.175 s (3:20:54)**.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens for 360p/480p/720p/1080p).

## Duration verdict — plan CORRECT

The plan states 3:20:54. The watch page's JSON-LD states
PT3H20M54S and the probed file is 12054.175 s. **The plan's
duration is correct** (second correct duration in the corpus
after Plan 37). No erratum.

## Two assemblies — the sandbox copy is CORRUPT, primo's governs

Both egresses fetched the watch page at HTTP 200 with
byte-identical size (220,032 B; sandbox sha 6d6b3df6…,
primo copy in the primo plan dir) and the control video
(Plan 22's 3881849) at 200 / 223,476 B on both — both
routes healthy. First sandbox page tries returned a 15 B
"Access denied." and a 93 B DB-fatal 503 (the site's known
transient DB body); retries succeeded — recorded, not a
target-absence signal.

- **Sandbox assembly (REJECTED):** 16 ranged segments;
  11 closed early (curl rc=18) and were tail-repaired by
  ranged append; 1 (s10) hung pre-data, was killed and
  refetched whole. Every segment reached its exact expected
  size and the concatenation hashed
  c9dda0e079ae557aa560777a9e63da8f4966f2757f16a24ffdf577e4fbccd5db
  — **but full decode FAILS (ffmpeg rc=234) at 264.36 s**
  (frame 15862). Byte arbitration against two independent
  fresh fetches: segment 0 is byte-identical to fresh bytes
  for 0–113,138,560 and diverges at **byte 113,138,561**
  (~99.6% of bytes differ thereafter in the compared
  windows). Per-segment sha256 vs the primo set: **only
  segments 2 and 12 match — exactly the two sandbox
  segments that completed rc=0 without repair.** Every
  rc=18/repaired/refetched sandbox segment differs.
  Conclusion: sandbox ranged transfers through this
  proxy splice/corrupt silently at exact final sizes —
  size verification alone does NOT verify a segment
  (see BLOCH-CANDIDATE).
- **Primo assembly (CANONICAL):** 16 ranged segments, all
  rc=0, exact sizes, no repairs. Assembled size exact,
  sha256 above. Full-decode + packet-span verification
  (`verify.log` on primo): **decode rc=0, zero error
  bytes**; first video packet pts 0.000000, last
  12054.116667 — the rendition spans its full duration
  (no Plan 05-style truncation). The pinned capture is
  the primo assembly.

## Licence (as seen)

- The watch page states **no licence** for the video
  (the only "license" string is a player-internal
  `license_code`). Posture per protocol: study only,
  never redistribute; no video file, transcript, or frame
  enters any shipped artifact. The rebuild is clean-room
  from distilled technique onto estate models.

## Audio

- An AAC stream EXISTS. Transcription follows the chunked
  lane / slice-ladder discipline (see OBSERVATION.md §5);
  single-transcriber = UNCONFIRMED tier; the screen
  governs over narration.
