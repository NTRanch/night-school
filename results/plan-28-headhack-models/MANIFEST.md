# MANIFEST — Plan 28: How to Headhack Models (rule34video 3644780; plan ID 3655211 = 404)

- Plan: `../../repo/plans/28-headhack-models.md`
- Source video: rule34video **3644780**, "How to Make 3D Porn -
  How to Headhack Models in Blender - Anime Nyan" — **Anime Nyan**
  (watch-page info block). Upload 2025-01-03; 36,702 views /
  124 likes (JSON-LD). The plan's ID **3655211** returns the
  site's 404 from both egress routes and is absent from the
  site's search results; 3644780 is the title-exact match and
  its description reproduces the estate headhack skill's asset
  inventory item for item (INTAKE.md). Substitution flagged
  there and in the local plan copy.
- **Duration: 6169.23 s (1:42:49)** per ffprobe of the acquired
  file, matching page JSON-LD PT1H42M49S. **The plan's 1:58 is
  an erratum** (local plan copy annotated). This corpus's
  durations have been wrong repeatedly; this one is wrong by ~52×.
- Description (as seen): tutorial-pack and Discord links, then
  the tool links (Victoria 8 blend, Diffeomorphic import_daz,
  MHX, PSK/PSA importer, UEShaderScript, Fuse-Skeletons,
  "Finished Blender File (with Fixed Face, jaw and eye bones)").
- **Licence: none stated** on the page (no licence statement in
  metadata or description). Study-only posture per protocol:
  studied, never redistributed; no video file, transcript, or
  frame enters any shipped artifact.
- Acquisition: 2026-11-06, **terminal egress only** (browser
  route is policy-blocked for this domain and was not used).
  Sandbox curl hit the site's own 503 (database) error page;
  the working route was primo via `~/workspace/bin/primo-ssh`:
  watch page fetched with browser UA + cookie jar; the 1080p
  `get_file` URL taken from the *same page load* (per-load
  `v-acctoken`), followed with `-L`. Canonical copy on primo at
  `~/.local/share/pax/night-school/plan-28/` (dl/ + audio.wav +
  slices/).
- File: `plan28-source-1080p.mp4`, **2,303,508,423 B**, h264
  1920×1080 @60 fps + AAC, **sha256
  0bad3efa4c10e82ef29fbda08c633b97076306105c7e4bdd908f04693e2e076a**
  (primo). Observation frames were extracted by HTTP range-seek
  against the same load's 720p URL (the 1080p download, 2.3 GB,
  completed in parallel and is the pinned canonical copy).
- Audio: AAC → 16 kHz mono WAV (`audio.wav`, 189 MB).
  Volumedetect: mean −28.3 dB, max −9.1 dB — a quiet track;
  narration presence settled by transcription, not assumed.
- Transcription: whisper.cpp `whisper-cli` + **base.en** on
  primo, two bounded windows (join 1800–3300 s; weights/fusion
  5400–6169 s), 2 threads, nice 15, detached run `ns28-whisper`
  (file-mediated, D-567 pattern) behind ~10 sibling whisper
  jobs. Both windows landed in-run: `transcript-join-slice.txt`
  (219 lines), `transcript-tail-slice.txt` (111 lines).
  Census: narration exists throughout the sampled windows and
  agrees with the screen; the join window's narration *changed*
  the Pass 2 distillation (OBSERVATION/PASS3 corrections).
- Frames: 102 stills at a 60 s grid (`frames/coarse/`), 225
  dense stills at 10–15 s across the four working segments
  (`frames/dense/`), 9 native-resolution key frames read
  individually. Blender in frame: **3.0.0**. Estate Blender:
  **5.2.3 LTS** (primo) — drift assessed in PASS3-REBUILD.md.
- Software versions (rebuild): Blender 5.2.3 LTS on primo;
  build/bend/determinism runs detached (`ns28-build1`,
  `ns28-bend1`, `ns28-det`), nice 10, `--factory-startup`, `-Y`.
- Resource note: primo ran at load ≈ 29–35 (sibling whisper
  saturation) for the whole run; all plan-28 work was niced and
  small (fleet blends ≈ 0.5 MB; renders 640² Workbench).
