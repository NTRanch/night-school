# Bloch candidate — D-1 Stage 1 retarget lessons

origin_lane: ntranch
content_label: nsfw
evidence: night-school-20261105/runs/d1-demonstrator/RETARGET-PROOF.md
+ DEMONSTRATOR-RECORD.md + records/gate-table.json (this run);
SIX-GIRL-STANDARD.md §7 (the procedure proven).

## Candidate 1 — cross-girl retarget is a bind-scale-filter operation, not a re-authoring
A clip authored on one rig transfers to any rig sharing the bone/morph
name space by exactly three operations: bind by name (assert every
track resolves; fail loudly, never drop silently), scale ONLY the
root (Hips) translation keys by the target/authoring height-scale
ratio, and apply the governance filter for reserved channels
(heart-pupil morph dropped for the troupe girls). Rotations, morph
weights, and timing transfer verbatim — rest-pose and proportion
differences live in each target's own skeleton definition. Proven on
14 applications across a six-girl fleet: seam deltas 0.000 mm / 0.000°
over 108 bones per scene build, replay determinism exact in clip
space and in decoded pixels. The failure mode this prevents is the
unscaled-Hips class (a shorter girl sprawling because the authoring
girl's translation keys were copied raw).

## Candidate 2 — a determinism comparison is only valid between identical builds
An early duplicate build measured with a reduced measurement set
(fewer penetration samples) produced different rendered pixels than
the full build — not nondeterminism: the corrective shape key derived
from those measurements integrated a different sample set, so the two
runs were different builds. When a determinism pair disagrees, diff
the builds' full input sets (including measurement-derived
correctives) before suspecting the renderer or the solver. Rule:
determinism gates compare like-for-like constructions, end to end.

## Candidate 3 — determinism and stability are separate gates, in fluids as in cloth
Independent fluid bakes can agree exactly through the gated emission
window and still diverge ~1–2% in mesh verts in the late slump; one
casting additionally read 35/486 particles inside a body at the final
frame while reading 0 at every gated frame. A fluid layer's
determinism claim and its interior-particle gate must both be scoped
to the gated window, with the late window measured and reported per
casting — never averaged across castings and never extended past the
window the evidence covers. (Companion to the Plan 39 bake lesson:
a hash-identical cache can be a hash-identical failure.)
