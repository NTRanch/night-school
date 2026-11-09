# Bloch candidate — Night School Plan 15 (Bonnie POV tutorial)

- origin_lane: ntranch
- content_label: nsfw
- evidence: `~/workspace/night-school-20261105/runs/plan-15/`
  (INTAKE.md, OBSERVATION.md, TECHNIQUE.md,
  rebuild/PASS3-REBUILD.md, PASS4-APPLICATION.md,
  rebuild/runC-measurements.json, rebuild/runC-record.json)
- Date: 2026-11-06

## Lesson candidates (propose-only)

1. **POV is a blocking discipline before it is a camera
   discipline.** A head-locked camera transplanted onto a
   fixed-camera blocking fails measurably: on the Plan 01
   seated blocking, the eye→contact ray's first surface was
   the partner's back at 0.046–0.158 m at EVERY phase
   (contact at 0.47–0.49 m). Any embodied-camera scene must
   be blocked for the sightline at every phase, or the
   occlusion named as a deliberate beat. Evidence:
   PASS3-REBUILD.md occlusion record; PASS4 gate.
2. **A moving camera amplifies the subject's reaction, not
   the action.** Follower spine screen travel: 1.92 px
   (fixed) → 100.7 px (head-locked POV), ~52×; the thrust
   point's travel barely changed (9.17 → 10.91 px). Budget
   head-motion envelopes against the PARTNER's motion.
3. **World-space registration is camera-invariant; only
   visibility degrades.** Hand/contact errors reproduced
   Plan 01's record to ~0.0001 mm under a moving camera.
   Registration-under-motion problems are staging/frustum/
   occlusion problems — measure them by projection, never
   by re-measuring the world and blaming the rig.
4. **Presence can be geometrically in-frame and visually
   absent.** Hands projected at the grips with ≤1.14 px
   screen error were not visible in the render because both
   characters shared one pale evidence material and the
   partner's silhouette covered the arm lines. Presence
   gates need a visibility read (render), not only a
   projection read (numbers) — and vice versa.
5. **Eye offsets for head-locked cameras must be authored
   in head-bone space.** A world-axis offset landed the
   camera inside the character's hair mesh (all frames
   blank). Bone-space offset (0, +0.10, +0.09) placed the
   eye at the face plane, clear of the hair bbox.

## Friction log (D-1064 — including silent workarounds in successful runs)

| # | Friction | Cost / workaround | Class |
|---|---|---|---|
| F1 | Sandbox egress 403 (15 B) vs primo egress 200 for the same watch page | Probed both, captured via primo | per-host egress variance; probe-both rule already estate practice |
| F2 | **Scripts written via heredoc through `primo-ssh` had their `$VARS` expanded by the wrong shell** — first download script (`$DL`→empty, arithmetic errors) and the first slices script (`$BASE`→empty, outputs aimed at `/slices`, and the script still printed a success marker) | Two failed launches, ~15 min; durable fix: author scripts locally with the file tool, scp them, never heredoc through primo-ssh | silent workaround risk — the false SLICES_OK is the dangerous part: success markers must be gated on output existence |
| F3 | run-slices2.sh first launch: `whisper-cli` not on PATH in the nohup context AND a guessed model path; every slice rc=127 while the script still printed SLICES2_OK | One full ladder pass wasted (~10 min of queue); fixed with absolute binary/model paths + rc aggregation (now prints SLICES2_FAIL) | same class as F2: unguarded success markers |
| F4 | `pkill -f <pattern>` matched the caller's own ssh command line and killed the calling shell (exit 255) | One round-trip; switched to PID-explicit kills | self-match trap |
| F5 | Grid frame script's `while read` skipped the last timestamp (no trailing newline in the timestamp file) | g42 (t=4925) missing from the grid; recovered manually | classic shell trap |
| F6 | extract-frames.sh scene scan failed on first run because primo `records/` didn't exist | One rerun after mkdir | setup ordering |
| F7 | whisper-cli stdout is block-buffered when redirected — log tails lag true progress by minutes and segment timestamps in the log are NOT a rate | Repeatedly misread as stalls; CPU-time (`ps -o time`) is the reliable progress signal | observability |
| F8 | Programme-wide transcription contention: 8–10 concurrent whisper jobs (plans 11/13/15/16/17/19 + tenants), load ≈ 40 on 16 threads | My jobs reniced (chunk 19→5, slices 19→8/12) and re-scoped to a slice ladder; full 4,991 s transcription still in flight at close-out (detach `ns15-whisper`) — OBSERVATION §1 records exact coverage | resource discipline: the one-heavy-job rule was collectively unenforceable from a single lane; flagged for the coordinator |
| F9 | Blender 5.2 API: f-curves live on `strip.channelbag(slot)`; `Scene.evaluated_depsgraph_get` doesn't exist (it's on the context) | RunA `bob_fcurves: 0`; one v2 build crash before renders | version-API drift; probe, don't assume |
| F10 | The saved scene's active camera was the FIXED camera (build script set it before save) — first isolation diagnostics were fixed-camera views misread as POV | One diagnostic round redone with the camera forced | save-state hygiene: set the evidence camera before save (fixed in v2) |
| F11 | Blender exits 0 even when the --python script throws | runC/runD first pass "rc=0" with no POV_BUILD_OK and no frames; gate on the OK marker + output existence, never rc | known Blender trap, re-confirmed |

## Artefact locations / revisions

- Run dir: `~/workspace/night-school-20261105/runs/plan-15/`
  (this file's siblings; frames under `frames/`, rebuild
  under `rebuild/`).
- Primo canonical: `~/.local/share/pax/night-school/plan-15/`
  — `plan15-source-720p.mp4` sha256
  `9c7124c81444a4d77b6750b21ec873976d9695e30ead88f30115c87ab196c039`
  (1,223,491,951 B); scene copy sha256
  `0bcd3bcd9149b0972769a83fce6a0313c894890ebb1d9e890a37432faf97d6ab`;
  built scenes `rebuild/runC/scene/pov_scene.blend` (+ runD).
- Build script revision: `rebuild/build_pov.py` as used for
  runC/runD (lens 21 mm; depsgraph fix; occlusion record;
  POVCam saved active). RunA/runB records retained in
  `rebuild/` (`runB-record.json`, run logs on primo).
- Results copy: `repo/results/plan-15-bonnie-pov-tutorial/`
  (LOCAL only, this delivery).
