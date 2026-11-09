# Plan 11 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). The video's mechanism is
Cycles **Light Groups** (the title's "Light AOVs" is a
misnomer — OBSERVATION Surprise 1). Estate context: Blender
5.2.3 (source video: Blender 5.0.1 — version drift recorded
at Target 1), the Plan 02 NS02 template (four light roles:
Key Area / Rim Spot / Fill Area / 4 Accent Points, plus an
emissive procedural backdrop; Cycles, CPU, seed 0).

## Target 1 — The pass contract

**What the artist actually consumes** (OBSERVATION §"Compositor
tree" — every pass below is seen wired into his tree; passes
merely *enabled* but never consumed are listed separately):

| Pass (Render Layers output) | Role in the contract |
|---|---|
| `Combined_<group>` × N groups | One per lamp. The relightable energy, split by *which lamp produced it* (direct + indirect + glossy + transmission of that lamp, pre-summed by Cycles into the group's Combined) |
| `Emission` | Ungrouped emissive surfaces seen by camera (his photo backdrop plane). **Not optional when emissives exist**: group passes contain no backdrop (OBS. 10:00–11:00, figure on black) |
| `Volume Direct` | Ungrouped volumetric scattering (his fogbox). Same status as Emission: outside every group |
| `Denoising Normal`, `Denoising Albedo` | Guides for the terminal comp Denoise (C-11-4). Not image energy; quality inputs |
| `Combined` | The renderer's own sum — the verification reference, not an input to the relight sum |

Enabled-but-never-consumed on screen: Ambient Occlusion,
Noisy Image, Denoising Depth (present as RL outputs, no
wire is ever isolated), and the full Light component set
(Diffuse/Glossy/Transmission × Direct/Indirect/Color —
enabled in the panel, absent from the consumed list).
Data utility passes (Depth/Normal/Position/Vector/UV) are
OFF in his setup.

**The minimal set that still relights convincingly —
answered from this evidence:** the per-group Combined
passes **plus the ungrouped-energy passes your scene
actually produces** (Emission when emissive geometry is
visible; Volume Direct/Indirect when volumes exist) **plus
the two denoising guides** if the sum will be denoised in
comp. Nothing else in his tree earns its storage. A
group-pure set is *provably* incomplete in any scene with
an emissive backdrop or fog — his own rebuild shows the
hole (figure on black) before he closes it. Conversely the
component passes (DiffDir etc.) are ceremony for this
workflow: Cycles has already folded them into each group's
Combined, which is the granularity relighting acts on.

**Precision / file format — the video states neither**
(UNREADABLE 2: the workflow is session-resident, nothing
is saved on screen). Estate contract, recorded as an
estate choice filling that gap, not as video evidence:

- **Multilayer OpenEXR, 32-bit full float, ZIP (lossless).**
  Rationale: relight algebra multiplies passes by gains
  ≥2 and adds them in linear space; 16-bit half float
  (≈3 decimal digits) bands visibly in the dark fill /
  backdrop gradients this pipeline exists to adjust, and
  lossy EXR codecs (DWAA/DWAB) spend their error exactly
  in those gradients. ZIP is lossless and the files are
  stills, not sequences — size is not the constraint.
- **Colour pipeline:** passes are scene-linear by
  construction; the view transform (AgX in both 5.0.1 and
  5.2.3 defaults) applies once, at display/output, never
  to stored passes. His exposure/grade lives in comp nodes
  (HSV/Color Balance/Add factors), i.e. *after* the sum —
  the estate variant keeps the template's view settings
  untouched and does all relight math in linear space.

- **Adopt:** the consumed-pass list above as the contract's
  core; per-lamp groups named for the lamp's role; Combined
  retained in the same file as the verification reference.
- **Adapt:** (a) persistence — the estate writes the
  contract to a multilayer EXR (above); his session-only
  form is rejected as a deliverable (below). (b) His
  backdrop is ungrouped and rides the Emission pass; the
  estate variant *additionally* assigns the backdrop to
  its own group (`Backdrop`), so the largest ungrouped
  term becomes gainable/tintable like any lamp — the
  Emission/Volume remainder is still carried in the sum
  (measured in Pass 3) so nothing is silently dropped.
  (c) Renderer denoise OFF for pass renders (his C-11-4
  posture: denoise the sum in comp); the Plan 02 template's
  renderer-denoise-ON default is overridden *in the
  variant only*, and recorded there.
- **Reject:** session-resident passes as a workflow (the
  relight dies with the session; no verdict pack can be
  built from it later); the component-pass sprawl
  (Diff/Gloss/Trans Direct/Indirect/Color) as part of the
  contract — enabled in his panel, consumed nowhere.

## Target 2 — Comp grammar (node operations that replace render iterations)

The tree (OBSERVATION, full order) reduces to five
operations — this is the grammar the estate implements:

1. **ADD is the identity.** Beauty = Σ (treated group
   passes) + Emission + Volume Direct. An unmodified sum
   must reproduce the renderer's Combined (Pass 3 measures
   this; it is the grammar's correctness gate).
2. **Gain per group** — his form: Hue/Saturation/Value
   with Saturation 1, Hue 0.5, **Value = the gain** (rim
   at 2.000). Estate form: a per-group multiply (RGB gain
   node), which is the same linear operation without the
   HSV round-trip; HSV stays available where a *hue*
   move is the intent.
3. **Retint per group** — HSV Hue (0.216667 typed live;
   0.467 on the rim branch) rotates a group's colour
   after the fact. A lamp's *colour* is a comp decision;
   only its position/type are render decisions.
4. **Per-branch treatment before the sum** — Glare
   (Bloom) on the rim branch ahead of its gain; Color
   Balance on one branch; branch Add factors (0.858 /
   0.500) as fades between sub-sums. Order matters:
   treatments act on *separated* light, which is the
   entire point — the same nodes on the Combined could
   not isolate one lamp's bloom.
5. **Terminal Denoise on the sum** — Denoise node (HDR ✓,
   Accurate, Follow Scene) guided by Denoising Albedo /
   Normal. Denoising is a comp stage in this grammar, so
   a relight never re-noises and never re-renders to
   change its mind about denoise strength.

**What still forces a re-render (the grammar's boundary,**
**from C-11-5):** lamp position, lamp type, lamp power /
temperature / radius *as baked into the pass* (a gain can
rescale a pass, but it cannot change the falloff shape a
different radius would have produced, nor move a
shadow), backdrop image, geometry, materials. Gains are
also not free at extremes: multiplying a pass multiplies
its noise and its quantisation — the practical relight
envelope is roughly 0.1×–2.5× per group before the
substitute shows (his own demonstrated maximum is 2.000×).

- **Adopt:** operations 1–5 as the estate comp grammar,
  in this order (treat → gain/tint → add → denoise).
- **Adapt:** HSV-Value gain → linear RGB multiply in the
  scripted estate tree (same math, no colour-space
  round-trip, values directly comparable across relights);
  his interactive Add-factor fades become named recipe
  parameters in the relight record.
- **Reject:** nothing in the grammar. Judged
  not-a-technique: the Google-Images backdrop sourcing
  (a licensing hazard the estate must not copy — Plan 02's
  procedural backdrop already routes around it) and the
  solo-pass viewer checks as a *gate* (they are inspection,
  not verification; Pass 3's pixel stats replace them).

## The named estate form — NS11 "Light Groups" variant

Plan 02 NS02 template + : one light group per lamp
(Key / Rim / Fill / Accent_1…4) + Backdrop group for the
emissive cyclorama; compositor tree implementing the
grammar (per-group RGB gain/tint → Add chain → terminal
guided Denoise → Composite/Viewer/File Output); render
contract = multilayer EXR 32-bit ZIP with Combined +
group passes + Emission + Volume + Denoising Data;
renderer denoise OFF. Relight = pass algebra on the EXR
(gains/tints per group, remainder at 1.0), measured per
group. Pass 3 builds it.

## Claim-by-claim disposition

| Claim | Disposition | Note |
|---|---|---|
| C-11-1 one group per lamp, role-named | Adopt | Estate names = Plan 02 roles; accents split per lamp, following his fill_01/fill_02 precedent |
| C-11-2 beauty = Σ groups + Emission + Volume | Adopt (as the contract's core identity) | Pass 3 measures both the groups-only gap and the full-sum match on estate geometry |
| C-11-3 per-group gain/tint in comp, no re-render | Adopt | Gain via linear multiply (Adapt of his HSV form); envelope ~0.1–2.5× noted |
| C-11-4 denoise after the sum, in comp, guided | Adopt | Variant: renderer denoise OFF; tree carries the guided Denoise as terminal node |
| C-11-5 lamp geometry still forces re-render | Adopt (as the named boundary) | Pass 4 gate FAIL drivers are read against exactly this list |
| C-11-6 "instantaneously change lighting without re-render" | Adopt as scoped | True inside the grammar's envelope; the unscoped version is marketing, recorded as such |
