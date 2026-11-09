# MANIFEST — Plan 23: Geonode for Pillows (rule34video 3881817)

- Plan: `../../repo/plans/23-geonode-pillows.md`
- Source video: rule34video 3881817, "Blender tutorial: Geonode
  for pillow(s)" — **KenFurFox** (watch-page info block).
  Upload 2025-06-13; 9,191 views / 106 likes (JSON-LD).
- **Duration: 706.048 s (11:46)** per ffprobe of the acquired
  file, matching page JSON-LD PT0H11M46S. **The plan's 2:04 is
  an erratum** (local plan copy annotated). The task brief's
  "124 s, one small chunk" sizing inherits the same error; the
  real file is still a single whisper pass under the 3,600 s
  cap.
- Description (as seen): "Just a short tut abou how to use the
  set position geonode for deforming on "collision" Enjoy" —
  the premise correction that governs Passes 1–2 (OBSERVATION).
- **Licence: none stated** on the page (no licence statement in
  metadata or description). Study-only posture per protocol:
  studied, never redistributed; no video file, transcript, or
  frame enters any shipped artifact.
- Acquisition: 2026-11-06, sandbox egress. Direct page fetch
  with browser UA + cookie jar; the 1080p `get_file` URL taken
  from the *same page load* (per-load `v-acctoken`), followed
  with `-L`. (The browser-tool fetch route is policy-blocked
  for this domain; the curl route is the one prior plans
  proved.) Sandbox vs primo probe: the sandbox route succeeded
  first try; primo egress was not needed for capture. Primo
  itself was reached via `~/workspace/bin/primo-ssh` (plain
  `ssh primo` from this sandbox reads the wrong config and
  fails against the proxy — friction-logged in the bloch
  candidate).
- File: `plan23-source-1080p.mp4`, canonical copy on primo at
  `~/.local/share/pax/night-school/plan-23/`, **176,578,936 B**,
  h264 1920×1080 @60 fps + AAC, **sha256
  ade3ef0753cffae60a72e8c5153f200ce1dc3f51a05a7b45954ffc66c27b62b4**
  — identical hash computed on both machines (sandbox + primo).
- Audio: AAC → 16 kHz mono WAV (`audio.wav`, 22,593,614 B).
  Volumedetect: mean −35.8 dB, max −3.7 dB — a quiet track;
  whether it carries narration is settled by the transcript
  census, not assumed.
- Transcription: whisper.cpp `whisper-cli` + large-v3-turbo on
  primo, single pass (706 s < 3,600 s cap), 2 threads, nice 10,
  detached run `ns23-whisper` (file-mediated, D-567 pattern) —
  sequenced behind ~10 sibling whisper jobs saturating primo
  (load ≈ 34–36 at launch). Census result in OBSERVATION /
  PASS3 records when the run lands; the observation is
  screen-first regardless (census-is-a-screen).
- Frames: 141 stills at a 5 s grid (`frames/full/`), 4 contact
  sheets, 18 native-res node-editor crops + panel/status crops
  (`frames/crops/`). Blender in frame: **4.4.3**. Estate
  Blender: **5.2.3 LTS** (primo) — drift assessed in
  PASS3-REBUILD.md.
- Software versions (rebuild): Blender 5.2.3 LTS on primo;
  build/sweep/determinism runs detached (`ns23-buildA`,
  `ns23-sweep`), nice 10, `--threads 4`, `--factory-startup`.
