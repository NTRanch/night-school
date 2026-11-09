# Plan 36 — Pass 3 Clean-Room Rebuild Record

- **Date:** 2026-11-06 · **Route:** Blender **5.2.3 LTS**
  headless on primo (`/usr/bin/blender`, `-Y` discipline),
  scripted, deterministic. **Only source used:** the gated
  `TECHNIQUE.md` in this run dir (video/transcript closed
  throughout the build).
- **Host rig:** a COPY of Prima's conformed fleet rig —
  sandbox fleet file `torogao-models-20261104/prima/prima.blend`
  SHA-256 `50dfd83c9d5c409a…`, staged to primo as
  `rebuild/prima-fleet-copy.blend` and re-hashed there
  (identical). The fleet original was never opened for
  writing; the staged copy's hash is unchanged after all
  runs (`ns36-build.log`). Sloane's fleet file was staged
  read-only for the census (SHA-256 `b86e5e8f36d2…`,
  unchanged).
- **Build host discipline:** primo, serialized detached
  runs (`~/.local/share/pax/detach/`, prefix `ns36-`),
  completion and results read from `.done`/`.log` FILES
  and from the build's own JSON record — Blender's exit
  code is 0 even when a script dies (§5), so exit codes
  were never used as evidence. Nothing audible.
- **Deliverables:** `rebuild/build_prop.py` (the one build
  script, sha256 prefix `dfe6599e…`), `rebuild/census.py`
  + `census-prima.json` / `census-sloane.json` (the
  Pass 2 comparison instrument), `rebuild/build_record.json`
  (run1 ≡ run2 except run name + frame paths),
  `rebuild/formA_{start,mid,end}.png`, `formB_mid.png`,
  `prop-only.png` (diagnostic), scene on primo at
  `plan-36/rebuild/run1/scene.blend` (sha256 prefix
  `a5ed7595…`).

## 1. The build

One bpy script: census-verified rig intake (54 bones,
`mixamorig:` colon names; clip bone map resolved with
zero missing), a minimal **Mala-class articulated prop**
built in-scene, registration in the video's translated
method, a 2-second estate animation, per-frame drift
measurement in two forms, and evidence renders.

- **The prop** (estate form of TECHNIQUE §1c Adapt): a
  `MalaPropRoot` empty; a 4-bone prop armature (`root`,
  `seg1`, `seg2`, `seg3`; 45 mm segments) parented under
  the root — **hierarchy parenting, the video's internal
  mechanism (C-02)**; 12 bead spheres bone-parented along
  the chain (3 per bone) + a pendant cone at the tip; a
  `RegisterTip` empty bone-parented to `seg3` as the
  register point. Bead material = Sloane's own `Mala`
  palette colour (0.3, 0.19, 0.1) from her spec — the
  estate prop's look comes from the fleet palette, as the
  DAZ prop's look comes from its preset library.
  **Prop control surface: 21 animator channels** (root
  transforms 9 + 4 bones × rotation 3; beads/pendant 0 —
  they ride their bones, as the DAZ fans' geometry rides
  its nodes). Static chain pose: forward bow (−6°/−9°/−12°)
  so the strand hangs clear of the leaning torso (§5).
- **Animation:** the estate's own `prima-arc` clip
  (torogao-motion-clip/1, skeleton prima-rig/1 sha
  `1c6087af…` — the def of record from Plan 01), window
  chosen deterministically in-script: the 120-frame
  window of maximum Spine1 angular travel = **clip
  frames 255–375** (travel 0.966 rad), sampled per frame
  (slerp/lerp between the clip's 15-frame keys), 60 fps.
  121 samples measured per form.
- **Registration (the video's method, translated):**
  - *Internal:* parts parented under the prop root and
    the prop armature parented under the root — plain
    parenting throughout, as in the video.
  - *Body-side (the step the video does not show):* the
    prop root is registered to Prima's chest bone
    **`mixamorig:Spine2`** at a sternum anchor computed
    from a world-space target (bone head + (0, −0.16,
    +0.03) m at frame 255; the Mala is worn OVER the
    garment — §5) and measured in the two estate forms:
    **Form A** — Child Of constraint, Influence **1.000**,
    inverse set manually to the frame-255 bone world
    matrix inverted; post-constraint root displacement
    (the set-inverse delta as this build measures it)
    **0.000075 mm**. **Form B** — the shipped/keyed form:
    constraint removed, root world transforms baked to
    keys at the clip format's own **15-frame density**
    (keys at 255…375, LINEAR interpolation), the form a
    torogao-motion-clip would carry.
  - *Error definition (Plan 01 frozen-offset form):* the
    RegisterTip's offset in the Spine2 bone frame is
    frozen at frame 255; per frame, error = |evaluated
    tip − bone-frame × frozen offset| in mm. Internal
    error likewise against the tip's frozen offset in
    prop-root space.

## 2. Gate measurements (all from `build_record.json`
of the final pair; run1 ≡ run2)

| Form | Register-point (tip) error, n=121 | Internal (parenting) error |
|---|---|---|
| **A — Child Of live** | **max 0.0002 mm, mean 0.0001 mm** | max 0.0001 mm, mean 0.0001 mm |
| **B — keyed @15 f, LINEAR** | **max 0.0073 mm, mean 0.0031 mm** (worst at window index 8) | max 0.0001 mm, mean 0.0000 mm |

**Against the method's own claim:** the video's method
claims nothing numerically — it claims parenting *holds*
(C-02). Measured: parenting holds to float precision
(internal ≤0.0001 mm across 121 frames of body motion);
the constraint form holds at the Plan 01 class
(≤0.0002 mm vs Plan 01's ≤0.0001 mm contact lock — the
same class, a different contact set).

**Against the Plan 01 keyed-lock reference class:** Plan
01's shipped keyed lock measured max **0.393 mm** /
mean 0.087 mm. This build's keyed form measures max
**0.0073 mm** / mean 0.0031 mm — ~54× tighter, and the
difference is explained, not hidden: Plan 01 keyed a
*solved pelvis channel* whose rotation about a ~0.10 m
lever re-expresses as translation error between 8 sparse
solve keys; this build bakes the prop root's *own world
transform* at 15-frame density over a gentler chest
trajectory (Spine1 travel 0.966 rad over 2 s). The keyed
class is therefore **motion- and lever-dependent**; the
honest estate statement is: keyed registration error
lives in the 0.007–0.39 mm band across the two measured
cases, set by key density, trajectory curvature, and
lever length — not a single constant.

## 3. Claims (the 12 from OBSERVATION §8)

**Tallies: REPRODUCED 6 · ADAPTED 2 · NOT BUILT 2 ·
UNTESTABLE-IN-ROUTE 1 · n/a (not a technique) 1.**

| Claim | Score | Evidence |
|---|---|---|
| C-01 premise (tutorial, prop only) | REPRODUCED (Pass 1 finding; the rebuild's scope rests on it) | OBSERVATION §0/§2 |
| C-02 registration = parenting | REPRODUCED (translated) | Prop parts + prop armature parented under the root; internal error ≤0.0001 mm over 121 frames |
| C-03 transforms-only control surface | REPRODUCED as an inventory; estate contrast measured | Pass 1 inventory; census: estate Mala = 0 channels, rebuild prop = 21 (TECHNIQUE §1) |
| C-04 single geometry, ≥9 surfaces | ADAPTED in miniature | Rebuild prop is one assembly whose look is palette-driven (Sloane `Mala` colour); surface-group authoring was not rebuilt — not the study's mechanism |
| C-05 library-first surface | ADAPTED | Estate form stated in TECHNIQUE §1c (presets as proposal, Pass 4); the rebuild prop itself ships as one scripted asset with a spec-style palette entry |
| C-06 animated spin preset | not built — distillation stands | Out of the brief's rebuild scope (registration); the estate form (keyed bone rotation on the phase table) is specified in TECHNIQUE §3 |
| C-07 hover = keyframed root bob | not built — distillation stands | As C-06; the recipe's numbers are recorded exactly (rise/lower 20 f @30 fps; tilt read X −5.00°/Z 8.50°) for the Pass 4 proposal |
| C-08 no shadow/camera/physics device | REPRODUCED (observational) | OBSERVATION §6; rebuild evidence renders likewise use no grounding device |
| C-09 device hidden for YouTube | n/a — creator hygiene, not a technique | — |
| C-10 asset ships broken references | REPRODUCED as a negative | The estate build loads and runs with **zero** missing-file errors for its assets (build logs; the only file complaints are a primo user addon's own settings files, unrelated) — the clean-load gate their asset fails is stated as an estate requirement in TECHNIQUE §1c |
| C-11 appendage can be lengthened | UNTESTABLE-IN-ROUTE | The lengthening channel is UNREADABLE in the source (OBSERVATION §7.5) — there is no mechanism to reproduce. Nearest equivalent, deviation stated: this build's prop length is set by its bone chain (segment lengths / bone scale are directly keyable in the estate form), which is our design, not a reproduction of theirs |
| C-12 registration precedes animation | REPRODUCED | Build order is script-enforced: assemble → parent → register → animate; no re-registration occurs after keying in either form |

## 4. Determinism

Full build run **twice in separate Blender processes**
(run1/run2, identical script sha256 `dfe6599e…`), primo
detach log `ns36-build.log`:

- **Measurements identical** — the two `build_record.json`
  files diff only in the run name and frame paths.
- **Decoded-pixel hashes identical** (ffmpeg rawvideo
  decode of the PNGs, never PNG bytes): Form A start
  `cc5cf88a…`, mid `637a77c4…`, end `0fdbfcd4…`; Form B
  start `cc5cf88a…`, mid `0fe38d79…`, end `0fdbfcd4…` —
  in both runs.
- Form A ≡ Form B at start and end (both are key frames,
  where the keyed form reproduces the constraint form
  exactly). The Form B **mid** frame's hash differs from
  Form A's while the two are visually identical at
  viewing size (both in this dir): the mid frame is also
  a key frame, so the difference is a sub-visible
  evaluation-order residue in a few pixels, recorded
  here rather than smoothed; the verdict rides on the
  per-frame measurements, not on this pair.

## 5. Per-edit attribution (attempts; D-1064)

| Attempt | Change vs previous | Observed difference | Verdict |
|---|---|---|---|
| 1 | First build | Died in window selection: `Quaternion.angle_difference` does not exist in the 5.2 mathutils API; Blender still exited 0 and the run produced nothing — caught only because outputs were checked, not exit codes | FAIL — API slip, fixed by 2·acos(\|dot\|) |
| 2 | Angle fix | Died at Form A setup: `Matrix` never imported (import line carried only Vector/Quaternion) | FAIL — one-line slip, same catch mechanism |
| 3 | Matrix import; channelbag(slot) fix for the Form B fcurve access (Plan 01's 5.2 finding) | **Full build completes; drift measured** (A 0.0002/0.0001; B 0.0054/0.0023 at the first anchor). BUT the evidence render shows no prop on the body: a constant bone-space anchor offset (0,−0.055,0.10) landed the root behind the torso (mixamorig bone axes ≠ world axes) | PASS on numbers, FAIL on the visual gate — anchor rework |
| 4 | Anchor computed from a world-space sternum target (−0.095 m front); curls as first built (+X) | Numbers hold (A 0.0002/0.0001; B 0.0061/0.0026); prop still invisible in the full render. Positional probe (`probe_pos.py`): the strand's lower half sat **inside** the leaning torso — the +X curls bowed it backward (+Y) into the garment | FAIL on visual gate — curl sign + probe evidence |
| 5 | Curls reversed to bow forward (−6°/−9°/−12°); camera pulled back | Numbers hold; prop-only vs full render pair (`probe_render.py`) isolates the last occluder: the loose **Outfit mesh billows forward of the strand** in the arc pose — the strand hangs at the skin sternum, inside the garment's silhouette | FAIL on visual gate — worn-over placement required |
| 6 (final) | Anchor moved out to −0.16 m (worn OVER the garment, as a Mala is worn); bead material given a real Principled base colour (attempts 1–5 set only the legacy diffuse colour, rendering the beads near-white) | **Strand visible on the body in all evidence frames** (brown beads + pendant over the garment, `formA_mid.png`); drift: A max 0.0002 / mean 0.0001 mm; B max 0.0073 / mean 0.0031 mm; determinism pair identical | **PASS** |

Confounded note: attempts 4→5 changed curl sign and camera
together; attempts 5→6 changed anchor distance and material
together. In both pairs the *occlusion* attribution rests on
the probe renders (prop-only vs full), not on the A/B frame
difference alone — recorded as partially confounded for the
visual sub-steps, unconfounded for every number.

## 6. Expected-vs-seen (design targets fixed in the build
script before the successful run; no separate BENCHMARK.md
was filed for this plan — deviation recorded in
BLOCH-CANDIDATE.md)

| # | Item | Read |
|---|---|---|
| 1 | Prop registered to the chest and carried through 2 s of arc motion, no visible detachment | **PASS** — strand + pendant ride the torso in start/mid/end frames; drift ≤0.0002 mm (Form A) |
| 2 | Keyed (shipped) form stays in the sub-mm class | **PASS** — max 0.0073 mm at 15-frame key density |
| 3 | Prop reads as a worn Mala-class item (beads + pendant over the garment) | **PASS (agent read)** — `formA_mid.png`; Owner's eye queued in Pass 4 |
| 4 | Internal parenting is exact | **PASS** — ≤0.0001 mm, float-precision class |
| 5 | Fleet untouched | **PASS** — fleet-copy + Sloane hashes identical before/after all runs; builds wrote only inside `plan-36/rebuild/` |
