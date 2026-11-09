# Bloch candidate — Plan 24 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 24 study run (Tentacle Monster WIP 3,
  rule34video 3666838), 2026-11-06. Run outcome: CAPTURE-BLOCKED
  (see runs/plan-24/MANIFEST.md).

## Candidate 1 — KVS origin DB-flap: video pages die, static pages live; existence of one video is undecidable from outside

**Lesson:** On a Kernel Video Sharing host whose database backend
is flapping, watch pages alternate HTTP 503 with the verbatim body
`[FATAL]: can't connect to database defined in
/admin/include/setup_db.php: Connection refused` (93 B) and HTTP
404 (384 B shell), while the homepage and listing pages serve 200
from cache. The discriminating control set is: homepage (proves
host alive) + a *known-live* video page from the site's own
latest-updates listing + a *previously captured* video page. On
2026-11-06 all three controls flapped too (the previously captured
page returned 200 exactly once in ~3 h), proving origin-wide
distress. But note the limit: a specific video whose page never
once succeeds cannot be pronounced deleted — "origin down" and
"this video gone" produce identical evidence. Record
CAPTURE-BLOCKED, never "video removed".
**Evidence:** runs/plan-24/MANIFEST.md (attempt table + control
probes), runs/plan-24/dl/capture.log (67 attempts: 51×404, 16×503),
runs/plan-24/dl/capture2.log (284 attempts: 199×404, 85×503),
primo `~/.local/share/pax/night-school/plan-24/dl/home.html`
(200, 206,871 B) and `p23.html` (200, 219,300 B, the single control
success, 20:34 PST).

## Candidate 2 — Long retry loops live on primo, never in the sandbox

**Lesson:** Detached capture/retry loops launched from the sandbox
(detach-run) were reaped twice in one evening — after 29 attempts
and after 3 attempts, both ending "lost" with no done file — and
sandbox /tmp content vanished once mid-run. The same loop on primo
(setsid nohup, file-mediated .log/.done) ran 5+ h across service
restarts without loss. Rule: any unattended loop that must survive
>10 min runs on primo; the sandbox is for foreground work only.
Verify liveness from the loop's own log file, never from the
launcher's exit.
**Evidence:** `~/workspace/detach-runs/ns24-sbx.log` (29 attempts,
then lost), `ns24-sbx2.log` (3 attempts, then lost); primo
`capture.log` / `capture2.log` / `capture3.log` continuity in
runs/plan-24/dl/ and MANIFEST.md.

## D-1064 friction log (this run)

- **Cost time:** ~3 h — the origin's video pages were down for the
  whole capture window; two full primo retry loops (351 attempts)
  exhausted before CAPTURE-BLOCKED was declared and an overnight
  loop (60 s cadence, 6 h) was left running. Next agent: run the
  control-probe set FIRST (homepage + known-live page + a
  previously captured page, ~1 min) — if all flap, start the long
  loop immediately and write the blocked-state scaffolding in
  parallel instead of hand-probing for the first hour.
- **Cost time:** ~20 min — two sandbox retry loops died silently
  (Candidate 2) before the primo-only rule was applied; a third
  loss was the primo-ssh relaunch call hanging ~2 min on a
  congested ControlMaster tunnel under sibling-wave load.
- **Forced a guess:** none. The run's deliverable discipline held:
  with zero frames, no motion numbers, grammar layers, or
  confidences were invented; Passes 1–4 are recorded as not
  performed / deferred, and the reference-only Pass-3 branch was
  explicitly NOT claimed (it is a verdict about a viewed clip).
- **Silent workaround caught:** the sandbox `scp` needs
  `-F /home/hatch/.ssh/config` (same trap as Plan 22's candidate);
  without it the transfer fails "Connection closed".

## Per-edit attribution (capture script, dl/capture.py)

| Component / change | Observed difference | Verdict |
|---|---|---|
| Loop 1 → loop 2: cadence 45 s → 25 s, budget 50 min → 2 h | Attempts 67 → 284; success count unchanged (0) | confounded — origin distress, not cadence, was the binding constraint |
| Fresh cookie jar + homepage warm-up (manual probes) | No change: 404/503 pattern identical | no effect (rules out session poisoning) |
| Embed / search / ID-only URL forms | 404/403/404 — no alternate route to the file | rejected as routes |
| Sandbox loops added in parallel | Both reaped by the sandbox (29 + 3 attempts) | fix rejected — primo-only (Candidate 2) |
| Loop 3: cadence 60 s, budget 6 h, left running overnight | Running at report time (attempt 1: 404) | adopted as the standing retry |

## Artefact pointers

- Blocked-state record of record: `runs/plan-24/MANIFEST.md`
  (this run, 2026-11-06).
- Capture script: `runs/plan-24/dl/capture.py` sha256
  `0214fa026920bb9d542cf9383c2199d54a56c41f61c2f23ab46032c7d1777ba4`.
- Attempt logs: `runs/plan-24/dl/capture.log` sha256
  `2b5a9ba91402ad195662ae08e29a6340b29bbcbe32b322fc4713d8a1036dd5f8`,
  `capture2.log` sha256
  `7edbd95c34d4060fde27542055518fa17da668342b208135e76f4daadb257de0`.
- Standing retry: primo
  `~/.local/share/pax/night-school/plan-24/dl/capture3.log`.
