# Plan 38 — Pass 0 Intake (written BEFORE viewing, from the plan file alone)

- **Source:** https://rule34video.com/video/3213869/how-to-make-nude-models-in-blender-through-wrap3ds/
- **Video ID:** 3213869
- **Title (plan):** "How to Make Nude Models in Blender through Wrap3D"
- **Creator:** plan category listing shows none — to be recorded at intake from the watch page.
- **Plan-stated duration:** 3:20:54 (12,054 s) — TO BE VERIFIED from capture; corpus durations are wrong more often than right.
- **Lane:** NSFW-primary in subject / SFW translation: wrapping/retopology is the core of all model conversion.
- **Estate targets:** sprite-to-3D factory conversion, headhack practice (Plan 28), body-variant production.
- **Licence posture:** to be recorded AS SEEN on the watch page; study-only per protocol, never redistribute. No video/transcript/frame enters any shipped artifact.

## SHOULD-BE-SEEN (plan file, verbatim intent)

"A full Wrap3D workflow: source and target preparation, point/correspondence placement, the wrap itself, projection cleanup, and Blender finishing — at working length, with the failures left in."

## Pre-viewing claims to test (a)–(e)

### (a) Preparation contract
Expect BOTH meshes to be required to satisfy, before any wrap:
- clean manifold topology, no open edges except declared openings (neck/wrists/ankles), no non-manifold / degenerate faces;
- matched scale (same units, same height within tolerance) and matched pose (T/A-pose alignment, limbs separated);
- source = clean-topology template body; target = scan/high-poly donor; UVs irrelevant to the wrap itself but required for the Blender transfer that follows.
Prediction to test: the video will show at least one explicit scale/pose alignment step and at least one topology repair (fill holes / delete stray shells) before the first wrap. If it wraps onto an unprepared target, that absence is itself the finding.

### (b) Correspondence strategy
Expect an ordered landmark set: sparse control points placed on anatomically stable features (joint centres, nipples, navel, facial features), placed in a fixed order (head → trunk → limbs, or centre-out), with count in the tens (not hundreds — Wrap3D interpolates between points). Expect the creator to add points reactively where the first wrap fails (hands/face), i.e. count grows across re-wraps.
Prediction to test: first-pass point count vs final count will differ; placement order will be repeatable enough to state as a grammar.

### (c) Wrap parameters
Expect Wrap3D's own parameters (smoothing / control-point weight / subdivision or equivalent) to be shown numerically at least once, and each re-wrap to change ONE variable. Expect defaults to fail visibly at least once (hands or face) before a tuned value succeeds.
Prediction to test: if no numeric parameter is ever readable on screen, the parameter set is UNREADABLE and the rebuild marks those values UNTESTABLE-IN-ROUTE rather than inventing them.

### (d) Cleanup lie-zone map
Expect the wrap to lie predictably at: hands/fingers (thin, self-occluding), face (eyes/mouth concavities), joints (armpit, crotch, elbow/knee creases), and any place where source and target proportions differ most (bust/hips). Expect cleanup in Blender after export: sculpt/proportional-edit fixes, in an order (worst zone first or head-to-toe).
Prediction to test: each lie-zone is either pre-emptable by preparation (more/better-placed correspondence points, pose matching) or inherent to projection (concavities, thin parts) — the map must say which, with evidence.

### (e) Blender finishing pass
Expect, after the wrap: import back into Blender, Data Transfer (normals and/or UVs and/or vertex groups/weights for the armature), material/texture assignment from the target, and a final visual check in pose. Expect the armature/weight transfer to be the step where the wrapped body becomes animatable.
Prediction to test: if the video ends at the raw wrapped mesh with no weight/UV transfer, the finishing pass is ABSENT and the estate must supply it from Plan 22 / fleet practice — recorded as a gap, not filled by invention.

## Closest estate machinery (read before viewing)

Plan 22's preset `NS22-RESPONSIVE-SLEEVE-FIT` (Shrinkwrap Project → Surface Deform → Solidify, collider-proxy architecture) is the estate's existing wrap-adjacent stack. This plan's rebuild must build on or compare against it, never silently duplicate it: Plan 22 wraps a *shell onto a body it must keep following*; Plan 38 wraps a *whole body onto a target it must become*. Shared primitive = projection; different contract = permanence (bake the wrap) vs responsiveness (re-evaluate every frame).

## Rebuild pair (pre-registered, per brief)

Prima's canonical body (m 1.00, amp_canon 0.030 m) wrapped onto her m 1.50 bust-variant geometry (amp 0.045 m; SIX-GIRL-STANDARD §4: sigma 0.050, z 1.235, ZS 0.98214). Ground truth is exact: the target is derived from the standard's own parameter by the builder's analytic gaussian, so fidelity (silhouette + landmark deltas) has a closed-form reference. Correspondence points = the fleet's derived anchors (§6: nipple/mouth/chest/pelvis/hand anchors) plus joint landmarks from the 54-bone skeleton.

## As-seen source facts (added at capture, 2026-11-06)

- Creator/uploader: **Anime Nyan** (same creator as
  Plan 28's headhack video; this video is a session in
  the same Feng project). Upload date (JSON-LD):
  **2023-12-23**. Categories "Tutorials, Blender"; tag
  "feng min (dead by daylight)".
- Duration: page JSON-LD PT3H20M54S; captured file
  12054.175 s. **The plan's stated 3:20:54 is CORRECT**
  (no erratum — see MANIFEST.md).
- Scorecard against the pre-viewing predictions above:
  (a) preparation contract — CONFIRMED and sharper than
  predicted (full OBJ export contract on screen);
  (b) correspondence — CONFIRMED in kind, REFUTED in
  scale of effort: ~69 pairs, not "tens growing across
  re-wraps"; there are NO re-wraps (one compute);
  (c) wrap parameters — READ on screen (Subdiv 3 /
  ICP 5 / Opt 20 / Sampling 5→0.2), not UNREADABLE;
  (d) lie zones — face/neck CONFIRMED (ears, sockets,
  mouth interior, neck seam); hands/joints REFUTED as
  lie zones for this wrap (the body was the template's
  own, never re-targeted);
  (e) finishing pass — CONFIRMED and larger than
  predicted (Correction shape key, shape-key host
  integration, separate Wrap texture-transfer graph);
  the predicted Data Transfer step appears in the
  REBUILD's estate stack, not in the video.
