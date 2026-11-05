# Plan 02 — How to Create NSFW Images in Blender (RamFuTanSFW)

- **Source:** https://rule34video.com/video/3257664/how-to-create-nsfw-images-in-blender-ramfutansfw/
- **Video ID:** 3257664 · **Creator:** RamFutaNSFW (presented by Anime Nyan, who sponsored it) · **Duration:** 1:36:30 · **Views at intake:** 32,892
- **Lane:** NSFW-primary / SFW translation: still-image posing, lighting, and render discipline generally
- **Estate targets:** keeper stills and key art, pose library construction, Strobe/Torogao promotional renders
- **Status:** PLANNED

## Why this video

The estate generates stills through its own image lanes, but posed 3D
renders are the reference class the 2D work is measured against — and
the code-first doctrine's end state is characters emitted as 3D. A
working artist's still-image Blender pipeline (posing, lighting,
camera, render, post) is directly comparable to our keeper-art process.

## SHOULD-BE-SEEN (written before viewing)

A full still pipeline: model preparation, posing method, lighting rig,
camera/lens choices, render engine settings, and whatever post or
compositing finishes the image — with the artist's taste decisions
visible enough to separate craft from tool defaults.

## Timed observation focus

- Pose construction: from-scratch keying vs pose libraries vs physics
  settle; how natural joint limits are respected.
- Lighting: light types, placement, HDRI use, shadow settings; whether
  the look is lit or merely rendered.
- Skin and material handling: shader setup, subsurface values, any
  texture work.
- Camera: focal length, depth of field, framing rules the artist
  states or demonstrates.
- Render: engine (Cycles/Eevee), samples, denoising, resolution,
  colour management — copied numerically.
- Post: compositor nodes or external edit steps, in order.

## Distillation targets

1. **The lighting rig** — reproducible as a named, saveable setup.
   Question: is the look portable to a different character and room,
   or tuned to one shot?
2. **Posing discipline** — how a pose is made to read as a body with
   weight rather than a mannequin. Question: what checks does the
   artist run before rendering?
3. **Render economics** — quality per minute of render time. Question:
   which settings carry the quality and which are ceremony?

## Clean-room rebuild spec

- Recreate the pipeline as a scripted Blender scene template
  (lighting rig + camera + render preset as named collections), then
  produce one still of an estate character from the template alone.
- The template is the deliverable mechanism: versioned, parameterised,
  re-runnable headlessly.

## Application

- **NSFW application:** one keeper-candidate still per the template,
  run through the visual verdict pack process.
- **SFW translation:** the same template renders the SFW key-art class
  unchanged — lighting and posing discipline do not know the rating.

## Gate

Side-by-side at viewing size: template still vs the video's result
class. PASS = same quality drivers identifiable and present; FAIL =
name which driver is missing and return to Pass 2.

## Deliverables

- `results/plan-02-blender-stills/` — technique sheet, scene template,
  rebuild still, gate result.
