# Bloch candidate — Plan 12 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 12 study run (WaifuFactory
  DevLog #1, rule34video 4313470), 2026-11-06.

## Candidate 1 — A silence census is a screen, not a verdict (speech detection)

**Lesson:** In intake audio triage, a silence/energy census
cannot establish "no speech." Plan 12's audio showed exactly
1 silence event (at −35 dB / 0.5 s) across 94 s and a loud
continuous bed (mean −15.9 dB), which read as "music teaser,
no narration." A bounded whisper transcription (large-v3-
turbo, nice'd, file-mediated) then found a full English
voiceover — 11 segments spanning the whole video, carrying
claims (two plugin names) that the frames alone could not
supply. A quiet voice under a continuous bed produces no
silence gaps, so the census's failure mode is silent and
total: it does not merely miss words, it deletes a whole
provenance class from the claims table.
**Rule:** for any study intake, "no speech" may only be
recorded from a transcription attempt (or a stated reason
one cannot be run), never from silence/energy statistics
alone. Census numbers may scope the transcription (clip
length, model size), not replace it.
**Evidence:** runs/plan-12/MANIFEST.md (census figures),
runs/plan-12/INTAKE.md (audio verdict + the correction),
runs/plan-12/transcript.txt (11 segments),
primo `~/.local/share/pax/night-school/plan-12/whisper.log`.

## Candidate 2 — In editor screen-captures, the inspector is the transcript

**Lesson:** A 94-second "devlog" with no captions yielded a
complete architecture read because the evidence was the
editor UI itself: node-tree names (module taxonomy), file
paths (skins as `.tres` data), and inspector parameter names
with numeric values (shader and physics surfaces) are claims
with numbers attached, readable frame by frame. Where a
source is a screen capture, Pass 1 should budget its dense
frames for inspector/tree legibility first and treat any
voiceover as a second, separate provenance class — the two
classes corroborate (SoupGroup in the tree ↔ "Soup IK" in
the voice) but must never be merged into one claim.
**Evidence:** runs/plan-12/OBSERVATION.md §1–§3,
runs/plan-12/TECHNIQUE.md §1 (V/SP tables kept separate).

## D-1064 friction log (this run)

- **Cost time:** ~10 min — the sandbox file GET answered 302
  then closed early on completion (curl rc=18) with a
  misleading `size_download=0`; integrity had to be proven
  by a Content-Range probe + full decode instead of trusting
  the transfer. Next agent: on this host, always pin a file
  by Content-Range total + decode check, never by curl's
  exit code or byte counters.
- **Forced a guess:** the watch page's own download menu
  labels the 1080p file "51 MB"; the true size is
  53,749,645 B (51.3 MiB). Page size labels on this host are
  rounded MiB — do not use them as a completion check.
- **Silent workaround caught:** the audio silence census
  (above) — a plausible-looking "music only" conclusion that
  transcription refuted. Filed as Candidate 1.
