# Bloch candidate — Night School Plan 17

origin_lane: ntranch
content_label: nsfw

## Candidate 1 — a creator's specialist tutorial is not evidence of their production practice; triangulate against their integrated workflow before adopting

- Evidence: Plan 17 (this run) vs Plans 11/13. Divinity
  Studio's specialist videos teach light-group relighting
  ("a powerful mechanism that every serious blender user
  should utilize", Plan 11 page description) and faithful
  beauty-pass decomposition (Plan 13). The same creator's
  integrated finishing workflow (Part 2, a real delivery)
  uses **neither**: no Combined_<group> passes exist in
  the scene, the beauty is never decomposed, lighting is
  baked interactively and comp is a global grade
  (OBSERVATION §6/§8; TECHNIQUE headline).
- Lesson: when a curriculum contains both a creator's
  technique deep-dives and their start-to-finish
  workflow, the workflow is the adoption evidence and
  the deep-dive is a capability catalogue. Weight them
  in that order, or the estate adopts tools their own
  author shelves in production.
- Pointers: runs/plan-17/TECHNIQUE.md (headline +
  C-11-A/C-13-B), runs/plan-17/OBSERVATION.md §6,
  runs/plan-11/TECHNIQUE.md, runs/plan-13/OBSERVATION.md.

## Candidate 2 — a sampling pair found in a file is a template default, not a production setting; record the retune step

- Evidence: Plan 17's scene opens at the 0.0100/4096
  adaptive pair (OBS §2, t0030) and the delivered render
  runs at 0.0300/512 after an on-camera retune (OBS §7,
  t2910). Plan 13's production render independently
  reads 0.0300/512 (its OBSERVATION, 7:40). Plans 01/02
  record only the 0.0100/4096 pair.
- Lesson: render-setting extraction must timestamp
  *which* state of the file a value comes from (inherited
  template vs production retune). A technique sheet that
  records one pair without the retune teaches ceremony
  as quality. Estate form: pairs are defaults + a named
  retune step in the order of operations (F-17-11).
- Pointers: runs/plan-17/OBSERVATION.md §2/§7,
  runs/plan-17/TECHNIQUE.md row C-02-D.

## Candidate 3 — passes can be used as effects (deliberate double-count), not only as reconstruction ingredients

- Evidence: Plan 17 comp adds Volume Direct + Emission
  at Factor 0.492 **on top of** a Combined that already
  contains both (OBS §8.2, t3150) — more fog and glow by
  algebraic double-count. Plan 13 adds the same Emission
  pass at unity because its reconstruction is *missing*
  it (C-13-5). Identical nodes, opposite intent.
- Lesson: when distilling a compositor tree, classify
  every pass-sum as reconstruction (target: identity
  with Combined) or effect (target: a measured delta
  from Combined). The classification — not the wiring —
  is what a rebuild must reproduce; an effect-sum built
  as reconstruction (or vice versa) silently changes
  the image.
- Pointers: runs/plan-17/OBSERVATION.md §8.2,
  runs/plan-17/PASS3-REBUILD.md ST-17-4.

## Friction log (D-1064 — what cost time, forced a guess, or forced a workaround)

1. **Plan metadata was wrong in two fields** (duration
   1:19:12 vs actual 1:01:10; Part 1's plan is wrong by
   ~2.7× per Plan 16's landed intake). Cost: the task
   brief's chunk arithmetic (~4,752 s) had to be
   re-derived from the page before capture. Workaround:
   page JSON-LD + Content-Range probe before any
   download arithmetic — already the lane's habit;
   this run adds: never size chunks from the plan file.
2. **Primo heavy-slot contention.** Three other
   whispers (Plans 11/15 + a third) held primo at load
   ~21–25 throughout this run. Workaround (silent in a
   successful run, recorded here per D-1064): the
   observation pass was executed **screen-first** —
   full frame grid + 62 natives + crops before any
   transcription — so the run's claims never queued
   behind the transcript. Transcription was chunked
   and WAV-staged early (light ffmpeg work) so it can
   start the moment a slot frees.
3. **Primo extraction-regex break.** The first primo
   page-parse truncated the token URL (shell quoting),
   returning HTTP 404 on the probe. Fix: base64-carried
   Python extractor (the sandbox extractor's code),
   after which primo probes matched the sandbox values
   byte-for-byte (916,337,092). Cost: one probe cycle.
4. **Crop coordinates missed twice** (the RL-node crop
   landed on viewer pixels at 720p layout fractions).
   Fix: crop from the native frame with coordinates
   re-derived from the actual pane boundary, third
   attempt read clean (crops/crop-t3030-rloutputs.png).
   Lesson folded into Candidate-adjacent practice:
   at 720p, pane boundaries sit at non-obvious
   fractions; verify a crop by reading it before
   citing values from it — done here for all 5 crops.
5. **pkill -f self-match killed the relaunch.** Restarting
   the transcription at higher thread count, the
   `pkill -f "plan-17/transcribe.sh"` pattern matched the
   primo-ssh caller's own remote command line (which
   contained the same string) and killed the launching
   shell before its sed/nohup ran — the follow-up exec
   returned empty with exit 0, and only a later ps/file
   inspection showed nothing had relaunched (the Primo
   waiter-loop trap family: a pattern in your own command
   line matches yourself). Recovery: kill by exact PID,
   write a fresh script file instead of sed-ing the old
   one, verify the new process exists by PID + args.
   Cost: ~10 min plus one discarded 5-minute partial run.
6. **Decode .done file wrote a literal `$?`** (shell
   escaping in the detached launcher). The verification
   did not depend on it: the decode error log (0 bytes),
   five spot decodes (0 error bytes each) and the
   packet-span probe carry the verdict in MANIFEST.md.
   Recorded so the next run writes the rc with a
   single-quoted heredoc launcher instead.

## Per-edit attribution (artefacts produced by this run)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| INTAKE.md | Created with duration errata + comparison-input state | Plan-vs-page duration conflict (4,752 s vs 3,670 s) surfaced before viewing | landed |
| MANIFEST.md | Capture pinned (916,337,092 B, sha256 65015280…), decode+packet-span verified | Packet span 282,120 packets covering −0.021…3669.824 s; 0 decode errors | landed |
| OBSERVATION.md | 18-step finishing order (F-17-01…18) + 8 claims + 6 UNREADABLEs from 93 frames | Premise reclassified: still-finishing course, no animation content | landed |
| TECHNIQUE.md | 22 comparison rows vs 02/11/13 | Sharpest difference isolated: bake-and-grade (17) vs decompose-and-re-decide (11/13) | landed |
| PASS3-REBUILD.md | 8 unmatched dispositioned (5 scoped tests / 3 rejects) + 10 confirmations | Every unmatched technique has a runnable proposal or an evidence reason | landed |
| PASS4-APPLICATION.md | Gate scored PASS with PROVISIONAL flags named | Hand-off to 11/13 programme stated explicitly | landed |
| Transcription (MANIFEST §Transcription) | Chunked whisper RUNNING detached (ns17-tr2, -t 8); stitch+census staged as primo `finish.sh` | Flushed narration (≈2:48 at delivery) already refined the retune chronology (OBSERVATION preliminary addendum) | confounded — primo oversubscribed by the parallel wave (5 whispers + Blender, swap exhausted); harvest = run `finish.sh` when `ns17-tr2.done` lands |

Artefact location/revision pointers: all artefacts at
`~/workspace/night-school-20261105/runs/plan-17/`
(LOCAL night-school tree, uncommitted working files at
run time 2026-11-06); canonical media + frames + chunks
at primo `~/.local/share/pax/night-school/plan-17/`
(media SHA-256 6501528046641b23f9b1593c000e2203c434515a0b8d6a871d5b16bc7422da72).
Results copies at
`repo/results/plan-17-porn-in-blender-part-2/` (LOCAL only).
