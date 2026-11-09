# Plan 02 — Pass 4 Application Gate

## SHOULD-BE-SEEN (from the plan)

"A still image produced from the template alone exhibits the
same lighting character (key/rim/fill balance), skin read, and
camera language as the tutorial's final render, judged
side-by-side; the template's parameters are recorded so another
artist could rebuild the setup without the video."

Evidence: `frames/pass4-side-by-side.jpg` — left: the video's
delivered still (crop of OBSERVATION frame t5700, his
Photoshop window; signature visible); centre: template NSFW
still (Prima, `rebuild/render-nswfw.png`); right: template
SFW still (`rebuild/render-sfw.png`). Viewing-size crops:
`frames/pass4-nswfw-facehand.png`.

## Per-driver gate — NSFW still (agent read; Owner eye queued)

| # | Driver (from Pass 2) | Verdict | Evidence / trace |
|---|---|---|---|
| 1 | Lighting character: key models the form, magenta rim from behind-side, fill opens shadows, points sparkle | PASS (structure) | Side-by-side: directional key modelling + cast floor shadow, rim-side edge light present, shadow side open not crushed. Rim reads as brightness separation more than hue because the rim colour IS the backdrop colour — which is the video's own mechanism (C-02-6). |
| 2 | Silhouette punched out of a glowing emissive ground; world contributes nothing | PASS | Figure separates cleanly against the neon gradient at viewing size; backdrop is the only environment light |
| 3 | Skin read: SSS warmth + slight wet sheen, skin tone separated from ground | PARTIAL / weak PASS | Separation is strong (bright figure, dark ground) and sheen is present, but the skin reads pale-cream rather than warm: Prima's Skin albedo is a near-white peach in linear values (0.896, 0.694, 0.564) with NO texture map — the video's read comes from a textured DAZ skin. Traced to Pass 2 Target 1 Adapt line: the SHEET carried the dials, but the estate character has no textured skin for them to act on. **Route-limited, not a sheet error.** |
| 4 | Camera language: portrait 1080×1920, 35 mm, three-quarter, figure fills frame | PASS | As built; figure ≈72% of frame height. His DELIVERED still is tighter still — it is a post-crop of his render (≈85%+, chest-up emphasis); the template reproduces the RENDER framing, and the crop belongs to the external post step (C-02-9) |
| 5 | Pose discipline: standing three-quarter promo, gross→fine, no mannequin stiffness | PASS (agent read) | Contrapposto weight shift, head counter-turned to camera, left arm bent with hand raised at shoulder height, fingers articulated by the rig's rest hand shape. Weaker than the video's bespoke pose (his includes a held prop + extreme hip rotation) — the discipline is present, the virtuosity is the artist's, as Pass 2 predicted |
| 6 | Post character: deep-focus render + synthesised DoF + signature | NOT APPLIED — external step | C-02-9 UNTESTABLE-IN-ROUTE (Pass 3). The still ships deep-focus, ready for that post; no fake blur or signature was added |

FAIL drivers: none outright. Weakest = skin read (#3),
route-limited as traced. Every driver was in the Pass 2 sheet;
no driver was missing from the sheet, and none was
mistranslated — the two estate-filled values (fill power,
backdrop emission) behaved as designed across the v1→final
probe sweep.

## SFW translation record

Same template, same script, one parameter changed
(`variant=sfw` → Prima_Outfit visible, Prima_OutfitEnd hidden;
scene-of-use differs by exactly that in the fingerprint:
acc3f09d… vs ca585ca4…). Pose, lights, camera, backdrop,
render preset untouched. Driver re-check on
`rebuild/render-sfw.png`: #1 PASS (same key/rim/fill read,
outfit shading models under the key), #2 PASS, #3 PASS
(skin areas read identically at face/hands/legs), #4 PASS,
#5 PASS (same promo pose reads as key-art stance in the
clothed variant), #6 n/a. The template does not change
between lanes — the SFW key-art still is the same neon
portrait language with the clothed outfit variant.

## Note for the record — Plan 35 GAP 1

Plan 35 found the 3D/Blender render lane has no artifact-side
gate checklist. This run produced, as a by-product, exactly
the shape of one: a fixed driver list (lighting character /
silhouette-into-ground / skin read / camera language / pose
discipline / post state) scored per artifact against a
SHOULD-BE-SEEN, with FAILs traced to the distillation sheet
or to a named route limit, plus two machine-checkable
pre-gates this template already enforces (model-never-moved
assertion, Simplify-OFF assertion, scene fingerprint +
decoded-pixel determinism). **Candidate seed for GAP 1: YES,
as a note for the Owner — not an adoption.** The checklist
above is this template's; generalising it to the lane is an
Owner call.

## Eye items queued for the Owner (no Owner PASS declared)

1. NSFW template still (`rebuild/render-nswfw.png`) —
   keeper-candidate judgement; skin paleness is the known
   weak driver (Prima's untextured albedo).
2. SFW still (`rebuild/render-sfw.png`) — key-art candidate
   judgement.
3. The GAP-1 candidate-seed note above.
4. C-02-9's post step (Lightroom blur + signature) remains
   external/proprietary — Owner call whether an estate
   equivalent (e.g. a compositor DoF pass) is worth a future
   plan; this run deliberately did not fake it.
