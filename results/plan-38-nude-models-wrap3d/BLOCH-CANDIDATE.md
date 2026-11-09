# Bloch Candidate — Plan 38 (Wrap3D template-wrap conforming)

origin_lane: ntranch
content_label: nsfw
evidence: ~/workspace/night-school-20261105/runs/plan-38/
  (MANIFEST.md, OBSERVATION.md, TECHNIQUE.md,
  PASS3-REBUILD.md, PASS4-APPLICATION.md; build artifacts
  on primo ~/.local/share/pax/night-school/plan-38/build/,
  metrics-*.json + logs as cited per claim)

## Lessons proposed

L-1 **Size-verified ≠ verified.** A ranged download whose
every segment reaches its exact expected size can still
be corrupt mid-segment (sandbox copy: decode died at
264.36 s; bytes diverge from byte 113,138,561; only the
two never-truncated segments matched the clean egress
hash-for-hash). Capture gates need full decode +
cross-egress hash arbitration; size is a necessary
condition that lies like a sufficient one.
Artefact: runs/plan-38/MANIFEST.md ("Two assemblies").

L-2 **Correspondence is geometry-bound.** A point set
authored against other geometry must be refused, not
reused (the source video's 127 stale points +
"Points does not match geometry" warning). The rebuild's
stale-source analog (E4) shows the failure is silent:
global mean 0.46 mm while landmarks sit 15–18 mm off —
only the correspondence gate catches it. Any stored
anchor/landmark set should carry the hash of its source
geometry. Artefact: PASS3-REBUILD.md §3 (W-5).

L-3 **A wrap precondition checklist must be falsifiable,
and two of ten items failed falsification.** W-4
(exclusion subsets) and W-7 (multi-resolution solve)
did not reproduce their predicted failures on a gentle
estate morph and were struck as universals, re-issued
as conditionals. Checklists kept on faith are how
pipelines accrete ceremony; the strike is a feature.
Artefact: PASS3-REBUILD.md §3 (W-4, W-7, E2, E7).

L-4 **Never blanket-smooth a convex feature.** One
group-limited Smooth pass (0.25 ×2) cost +1.94 mm bust
mean, +5.3 mm at the nipple anchor (Laplacian shrinkage
on the mound), isolated by decomposition before removal.
Cleanup verbs are zone-specific: re-seat features,
smooth seams. Artefact: build/polish-decomp.json.

L-5 **Fleet bodies are non-manifold; manifold-presuming
tools refuse them.** Prima's body carries 36 edges with
>2 faces (576 non-manifold edges), so Surface Deform
cannot bind to any target derived from it (three refused
binds, incl. sparse). Any estate pipeline step that
presumes manifold input needs a stated fallback.
Artefact: build/diag3.log, build/gb-run1.log.

L-6 **Voxel remesh is not a safe "scan stand-in" for
sparse open meshes.** It deleted Prima's z 0.4–0.6 leg
slab outright (0 verts in band; floor p95 189 mm).
Decimation preserves a faithful surface with
independent topology and is the correct stand-in.
Artefact: build/diag2.log,
build/metrics-v1voxel-stage1.json.

L-7 **Pose mismatch is ignored, not corrected.** A wrap
whose target was bent 40° at the forearm returned the
source pose untouched (hand-region centroid shift
0 mm). Pre-alignment (W-2) is a hard precondition
precisely because the failure is invisible in the
output. Artefact: PASS3-REBUILD.md §3 (E6/E6B).

## Friction log (incl. silent workarounds in successful runs)

F-1 Sandbox ranged transfers through the proxy splice
silently at exact sizes (see L-1); the working route was
primo's uninterrupted per-segment fetches. The first
capture plan (sandbox primary) was abandoned mid-task —
the abandonment is recorded in MANIFEST, not hidden.
F-2 A `nohup`-inside-ssh launch on primo died with the
session; `setsid` + .done/.log files (file-mediated
pattern) worked every time after. Two self-inflicted
`pkill -f` matches killed my own shell (pattern matched
the caller's own command line) — bracket-pattern or PID
waits only, afterwards.
F-3 Sandbox disk quota blocked assembling the 5 GB file
locally; verification moved to hash-streaming and the
primo-side assembly. No error surfaced — the write just
stalled; detected by progress inspection, not by a tool
failure.
F-4 The fleet tool place_anchors.py self-executes
main() on import (no __main__ guard); the primo working
copy was patched (call removed) to import it. The estate
original was NOT edited (out of scope); candidate fix
for the fleet tool: guard main() under __main__.
F-5 Surface Deform bind failure reports only a console
warning; is_bound must be asserted programmatically —
the first GUI run "succeeded" (rc=0, file saved) with an
unbound modifier. Caught by asserting is_bound into a
JSON artifact.
F-6 Whisper under wave contention crawls (~9 min of
audio per ~50 min wall on slice A): the slice ladder +
micro-slices at decisive spans replaced full
transcription; coverage is stated in OBSERVATION §6
rather than implied.
F-7 Primo ssh probes intermittently stalled under
sibling-plan load (one 130 s probe); tolerated with
timeouts, no retries stormed.

## Per-edit attribution rows (rebuild-level)

See PASS3-REBUILD.md §5 (five rows: scan construction,
refine stage substitution, Smooth removal, correction
zone narrowing, E6 instrument swap) — verdicts:
curative ×5, confounded ×0 (the one confounded
candidate, the combined polish, was decomposed into
sw_only/smooth_only before attribution).

## Artefact pointers

- Run record: ~/workspace/night-school-20261105/runs/plan-38/
  @ local tree, 2026-11-06 (no push, per brief).
- Build scripts + metrics + logs: primo
  ~/.local/share/pax/night-school/plan-38/build/
  (ns38_build.py as of the stage2 run1 run;
  metrics-*.json enumerated in PASS3 §2–3).
- Canonical media: primo
  ~/.local/share/pax/night-school/plan-38/plan38-source-1080p.mp4
  sha256 d04a49d90757929dfa736e1f769d662720b137e7e5846dcce9e1ff6fef3896a1.
