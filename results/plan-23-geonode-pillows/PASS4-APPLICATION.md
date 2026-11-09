# PASS 4 — Application and gate: Plan 23 (Geonode Pillows)

## Expected-vs-seen benchmark (written from the plan's gate)

SHOULD-BE-SEEN at the gate: (1) the node group rebuilt as a
reusable asset; (2) a parameter sweep across and beyond the
plausible ranges with renders at the corners; (3) safe ranges
documented; (4) the group must work beyond its demo settings
— a group that only works at demo settings FAILs.

## Gate items (agent reads; the Owner's eye is the verdict of record)

| # | Item | Agent read | Evidence |
|---|------|-----------|----------|
| 1 | Group rebuilt as a named, reusable asset | **PASS** | `rebuild/out/pillow_asset.blend`: group `PillowSquish`, Collider + Map Range window exposed as inputs, video values as defaults |
| 2 | Pillow form at demo settings | **PASS** (agent eye) | `out/demo_A.png`: plump saddle cushion, smooth central pocket cradling the sitter; measures in PASS3 (dent 0.2089 m, zero inverted/NaN/flipped) |
| 3 | Sweep across + beyond ranges, corners rendered | **PASS** | 39 steps / 8 axes (`out/sweep.json`); 17 corner+CLIFF renders (`out/sweep_renders/`) |
| 4 | Safe ranges documented | **PASS** | PASS3 "Safe ranges" + the gradient rule (To width / From width ≤ ~0.13) |
| 5 | Works beyond demo settings (the plan's FAIL condition) | **PASS** | Demo configuration is SAFE, and so are 19 other steps across every axis; failure modes are mapped, not hypothetical |
| 6 | Determinism (estate doctrine) | **PASS** | Two processes: vertex-hash and render pixel-hash identical (`out/determinism.json`) |
| 7 | Cliff located, not just predicted | **PASS** | Inversion cliff at combined steep windows (H2/H3: 182 / 159 inverted columns); render shows the torn form |

**Gate read: PASS** — group rebuilt + sweep recorded + safe
ranges written, and the sweep itself proves the group is not
a demo-settings-only artefact. This is an agent gate read;
Owner eye items are queued below and do not block the read.

## Application

- **NSFW application (per plan):** Torogao interior dressing —
  seat cushions, futons, and bedding that dent under a posed
  character with no simulation and full determinism. Filed as
  an estate asset candidate: `rebuild/out/pillow_asset.blend`
  + TECHNIQUE.md spec + PASS3 safe ranges. The collider input
  takes any evaluated mesh, so a posed Torogao rig drives it
  exactly as the video's Gummigoo rig drives the original.
- **SFW translation (per plan): identical** — props are props.
  The technique is lane-neutral: nothing in the group, the
  demo scene, or this record is NSFW. The same .blend serves
  SFW scene work unchanged; the crossing is named here per
  protocol (the *study source* sits in the NSFW lane; the
  *technique* is SFW-clean, and the bloch candidate carries
  the matching labels).

## Eye items queued for the Owner (from the corner renders)

- **Q-1 (demo form).** `out/demo_A.png` — free-standing, the
  demo settings give a pronounced hammock/saddle (edges lift
  ~0.42 m). In the video the chair hides the sides; for
  Torogao dressing the cushion will usually sit in a frame —
  confirm the saddle reads as "soft cushion" or whether the
  asset should ship with a milder default window.
- **Q-2 (over-inflation corner).** `sweep_D_ramp_start_0_0p0.png`
  — ramp start 0 lifts the cushion clean off the sitter.
  Agent read: DEGRADED (balloon, not pillow). 
- **Q-3 (density corner).** `sweep_F_seg_0_4.png` — dent
  depth is intact at 4 segments/edge but the pocket is a
  coarse faceted dip. Agent read: form reads, strained;
  the ≥16/edge guideline in PASS3 is an eye call, not a
  numeric one.
- **Q-4 (hover corner).** `sweep_E_press_0_m0p1.png` — dent
  forms under a *hovering* collider (proximity needs no
  contact). Agent read: numerically SAFE (dent 0.189), but a
  dimple under a floating sitter may read as a mistake in
  scene work.
- **Q-5 (the cliff).** `sweep_H_inversion_hunt_1_w1p0_to0m1.png`
  — the inversion break, for the record: torn V, flipped
  walls. No decision needed; it bounds the safe envelope.

## Residuals / in-flight

- **Transcript census:** narration exists (English). The
  primo whisper run (`ns23-whisper`, nice 10, 2 threads) is
  still in flight behind ~10 sibling jobs (load ≈ 43 at last
  check; 7 segments / 68 s recovered in ~28 min — it is
  crawling, not stuck). Recovered segments are in
  `transcript-partial.txt`; they agree with the screen
  ("we don't need some kind of soft body or collision, some
  fake kind of collision"). The full transcript lands in the
  primo plan-23 dir as `transcript.{txt,srt,json}` when the
  detached run finishes; no claim in this run waits on it
  (screen-first observation, U-6). If a later segment states
  a value the screen contradicted, OBSERVATION's screen
  values govern.
- U-2 (a Subdivision modifier after the GN modifier on the
  video's pillow) remains unreadable at video resolution;
  the rebuild needs none (density is in the base mesh), so
  the gap does not reach the asset.
