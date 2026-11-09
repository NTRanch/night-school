# Plan 06 — Pass 4 Application Record

- **Application target:** the fluid layer of Pass 3 over the
  Plan 39 layered stack (Plan 01 loop + §5.2 jiggle beat) in
  the D-1 scene — Prima = Follower, Yui = Leader, Contact at
  sample 38, 60 fps. Evidence frames are renders of the
  layered-with-fluid scene (`rebuild/scene/mainA2_baked.blend`)
  at the scene's own camera (NSCam, EEVEE 960×540), plus 3×
  crops of the pelvis interface: `rebuild/mainA2/renders/`,
  `rebuild/frames/`.
- **Reads below are the agent's reads** against the benchmark,
  per the visual-evaluation doctrine; items that need the
  Owner's eye are queued in §3, not decided here.

## 1. Benchmark — what the layered scene should read as

Written as the standard the evidence frames are judged
against:

- **B1 — Aim reads.** At the emission peak the fluid visibly
  travels from the emitting body's pelvis anchor toward the
  receiving body — a stream whose direction a viewer can
  trace to the aim anchor.
- **B2 — Beat reads.** Emission starts and stops on the
  authored beat: nothing before the gate opens at Contact−4,
  nothing new after it closes at Contact+10; the envelope
  follows the jiggle beat (Contact 38, follower peak 45).
- **B3 — Settle reads.** After cutoff the fluid stays on the
  bodies, slides/coats under gravity, and comes to rest on
  the bodies or the cushion/ground — no floating, no
  vanishing, no tunnelling.
- **B4 — No interior artifacts.** At the gated frames
  (Contact 38 and the emission peaks) no fluid is visible
  inside either body, and the measured interior count is 0.
- **B5 — Presence at viewing size.** At the scene camera and
  full-frame viewing size, the fluid's presence at peak and
  at settle is discernible without zooming — the layer reads
  as part of the shot, not as a measurement-only artefact.

## 2. Per-item reads (agent)

| Item | Verdict | Evidence |
|---|---|---|
| B1 Aim reads | **FAIL** | No stream exists to trace. In this geometry the emission is pressure-projected to a creep inside the 26–30 mm inter-body corridor (Pass 3 §5, 14-variant discrimination): what forms is a contact-interface **extrusion** at the pelvis interface, not an aimed jet. The fluid does arrive at the receiving body's surface and coats it — the destination is right; the travelling read the benchmark asks for is not there. |
| B2 Beat reads | **PASS** | Measured, not eyeballed: first sourced frame 34 = gate-on (offset **0 samples**), last increase 47, count frozen at 467 from frame 48 = gate-off; retime variant follows a +10 beat shift exactly (+10/+10) with zero hand edits (`mainA2/measurements.json`, `retime/measurements.json`). |
| B3 Settle reads | **PARTIAL** | The fluid coats the interface and slumps down the receiving body's front (mesh z-min descends to 0.5062 by f90; bbox in `mainA2/measurements.json`), with no floating or vanishing — but at the end of the 90-frame record it is **still a descending coating**, not yet pooled on the cushion (top z 0.4). Settle is in progress, not complete, inside this record's window. |
| B4 No interior artifacts | **PASS** | Measured interior count **0 at every frame 1–90**, gated frames 38/42/45 included, by ray parity against the real body meshes; nothing interior is visible in the f38/f45 crops either (`rebuild/frames/`). |
| B5 Presence at viewing size | **FAIL at peak / PARTIAL at settle** | At f45 (follower peak) the fluid is essentially **not discernible** at full-frame viewing size — the interface is occluded from NSCam and the extrusion is small. At f90 a small pale blue-grey patch is visible at the pelvis interface in the 3× crop (`rebuild/frames/mainA2_frame_0090_crop3x.png`); at full frame it remains marginal. |

**Summary of reads:** the layer is mechanically exact
(timing, gating, interior, round trip — Pass 3 §6) and
visually weak: it does the right things at the interface,
but the two reads a viewer would judge it by — a travelling
stream (B1) and presence at the scene camera (B5) — do not
land in this geometry at this camera.

## 3. Eye items queued for the Owner

1. **Jet vs extrusion (decides B1's future).** Is a gated
   contact-interface extrusion — fluid emerging at the
   interface, coating, and slumping — an acceptable D-1
   read for this shot class, or is a visible travelling
   stream required? A stream is not achievable in-pocket
   with Mantaflow FLIP inflow at these settings (measured,
   Pass 3 §5); getting one means a different shot geometry
   (larger separation at emission) or a different emission
   mechanism, which is a programme decision, not a tuning
   pass.
2. **Material / visibility.** The shipped fluid material
   (pale blue-grey 0.82/0.87/0.92, roughness 0.15) barely
   reads against skin at the scene camera. Colour, roughness,
   and thickness are an eye call; no proxy metric is offered
   as a substitute.
3. **Settle endpoint.** The 90-frame record ends mid-slump
   (z-min 0.5062, cushion top 0.4). Whether the
   demonstrator's shot should run long enough to pool — and
   whether pooling on the cushion is the wanted end state —
   is an eye/scope call on the f90 frame and crop.

## 4. D-1 readiness statement

The fluid ingredient is **ready as a layer**: gated,
beat-relative, interior-clean (0 at every frame), exactly
round-tripped through the estate's two-tier cache contract,
and additive over the loop + jiggle stack without altering
their measured state. What the demonstrator still needs on
top of it: **(i)** per-girl retarget of the whole stack
(loop, jiggle beat, fluid layer) beyond the Prima/Yui pair;
**(ii)** the lactation module built on this same layer at
the `Anchor_Fluid_Nipple.L/.R` emitters (SIX-GIRL-STANDARD
§6.3); **(iii)** casting per the D-1 record; and the three
Owner decisions in §3 — most load-bearing, the jet-vs-
extrusion call, because it decides whether this layer's
emission form is the demonstrator's form or a placeholder
for a re-staged shot.

