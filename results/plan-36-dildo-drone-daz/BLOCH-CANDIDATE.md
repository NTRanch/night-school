# Plan 36 — Bloch candidate (D-1064 friction + attribution)

- origin_lane: ntranch
- content_label: nsfw
- Artefact: this run — `~/workspace/night-school-20261105/runs/plan-36/`
  (IN­TAKE/MANIFEST/OBSERVATION/TECHNIQUE/PASS4 + `rebuild/`),
  results copy at `repo/results/plan-36-dildo-drone-daz/`.
  Build script revision: `rebuild/build_prop.py` sha256
  prefix `dfe6599e…`; measurements of record:
  `rebuild/build_record.json` (primo detach logs
  `ns36-dl`, `ns36-media`, `ns36-build`).

## Friction log (including silent workarounds in
successful runs)

1. **Background-exec handoff text contradicted the
   on-disk log (D-567 specimen, live).** The sandbox probe
   script's background completion handoff showed "target
   try 1: 404, 384 B, sha fd562038…" — a result the script
   never produced. The on-disk `records/route-log-sandbox.txt`
   (written by the script itself) shows the true sequence:
   503 / **200 (222,295 B, correct title)** / 503, with the
   control at 200 / 259,287 B. Acting on the handoff text
   would have closed a live source as SOURCE-NOT-FOUND.
   Lesson, restated for the estate: the file-mediated rule
   is not hygiene, it is the only thing standing between a
   run and a fabricated negative. Candidates: any worker
   brief that still tolerates handoff-text evidence should
   name the .log/.done FILE as the sole completion record.
2. **Blender exits 0 when a --python script dies.** Three
   successive build attempts (§ attribution) exited rc=0
   with partial or no output. The run caught each only by
   checking for the record file + grepping the log for the
   script's own sentinel ("BUILD DONE"). Silent-workaround
   risk: a pipeline that trusts rc would have shipped
   attempt 1's empty run as a completed rebuild. Estate
   form: headless-Blender wrappers should require a
   sentinel line or an output artifact, never rc.
3. **mathutils API drift (5.2):** `Quaternion.angle_difference`
   does not exist (use 2·acos(|dot|)); layered-action
   fcurves require `strip.channelbag(slot)` with the slot
   argument (Plan 01 found this; this run re-hit the
   no-argument form and re-derived it — the lesson had not
   travelled). Candidate for the Blender skill: a 5.2 API
   gotcha list in one place (channelbag(slot),
   BLENDER_EEVEE vs _NEXT, angle_difference absence,
   per-object wm.append duplication).
4. **mixamorig bone-space ≠ world axes for anchor
   offsets.** A constant bone-space offset placed the prop
   behind the torso; the cure is computing the anchor from
   a world-space target through the evaluated bone matrix.
   Any estate code placing register points by bone-space
   constants on the fleet rigs carries this bug silently
   (it measures fine — the prop tracks the bone perfectly,
   just in the wrong place; only the render shows it).
5. **Workspace write quota is transient and silent.**
   Mid-run, writes to `~/workspace` began failing with
   "Disk quota exceeded" while `df` showed 36 G free and
   /tmp accepted writes; the quota cleared on its own
   ~15 min later. Workaround used: stage in /tmp + primo,
   copy in when writes recovered. No artefact was lost,
   but a worker that treated the first failure as fatal
   would have stranded the run. (btrfs apparent size:
   `du` reports 177 G for the workspace on a 150 G fs —
   apparent-size numbers from this fs should never be
   quoted as usage.)
6. **A `find /` fallback in a primo probe** (my own
   command) ran for ~2 min under load before returning.
   Bounded probes should name the directories they search;
   the estate's primo layout makes `/` searches never
   necessary (fleet staging lives under
   `~/.local/share/pax/` and the sandbox workspace is NOT
   mirrored on primo — staging a fleet file means scp from
   the sandbox + hash verify, which this run did).
7. **Benchmark-file deviation (self-reported):** Pass 3's
   expected-vs-seen targets were fixed in the build
   script's design rather than filed as a separate
   BENCHMARK.md before renders (Plans 15/34 file one).
   The table in PASS3-REBUILD §6 is labelled accordingly.
   The gate did its work anyway — three attempts failed
   the visual item honestly — but the pre-filed artifact
   is the discipline and it was skipped under time
   pressure. Recorded, not smoothed.
8. **Primo tenancy:** load sat at 10–16 on 16 threads for
   most of the run (programme-wide sibling work). A 266 s
   whisper single pass took ~7 min wall. All of this run's
   heavy stages were serialized under one detach prefix
   and niced; nothing queued behind another of my jobs.

## Per-edit attribution (build; full table in
PASS3-REBUILD §5 — summary rows here)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Window selection | `angle_difference` → 2·acos(\|dot\|) | Script progressed past selection to Form A | fix confirmed |
| Imports | + `Matrix` | Form A setup executes | fix confirmed |
| Form B fcurves | `channelbag` → `channelbag(slot)` | Form B completes; LINEAR readback applied | fix confirmed |
| Anchor | bone-space constant → world-target computation | Root moved from behind torso to sternum (probe positions) | fix confirmed |
| Chain curls | +X → −X (bow forward) | Strand tip moved from inside torso (Y −0.085) to clear of it (Y −0.225) | fix confirmed; changed with camera in the same edit — **confounded** for the visual delta alone, unconfounded via probe positions |
| Anchor distance | −0.095 m → −0.16 m (worn over garment) + Principled base colour for beads | Strand visible on the garment in all evidence frames; drift rose slightly with the longer lever (B max 0.0054→0.0073 mm across attempts 3→6 — expected, and the comparison across attempts is **confounded** by the anchor change) | PASS (final) |

## Lesson candidates for promotion (propose-only)

- **L-36-1 (egress evidence):** a SOURCE-NOT-FOUND close
  requires the slugged target URL to fail on BOTH
  egresses with the control passing on both; slug-less
  variants 404 on this origin even for live videos
  (this run: `/video/3352555/` = 404 shell while the
  slugged page = 200). A probe that tests only the
  slug-less form will false-close live sources.
- **L-36-2 (prop census):** "does the estate have a prop
  for X" is answered by censusing the fleet files, not by
  the character spec — Sloane's spec says `mala: true`
  while her fleet file contains no Mala object at all;
  the spec describes the build recipe, the file is the
  shipped truth.
- **L-36-3 (registration band):** keyed-registration
  error is a band (0.007–0.39 mm measured), not a
  constant; quote it with key density, trajectory, and
  lever, or do not quote it.
