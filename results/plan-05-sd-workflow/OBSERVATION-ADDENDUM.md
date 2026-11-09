
## Addendum A — chunk-2 narration mapping (completes §7, corrects §10)

Added when the 360p-audio transcript landed (stitched:
1,694 segments incl. seam marker; census: 10.6% loop share,
recoverable 89.4% — `loop-census.txt`). Items below are
[SPOKEN] unless noted; where narration and an earlier
frame read conflict, the narration + native crop govern.

- **img2img prompt source (new):** the img2img demo's
  prompt is written by the **DeepBooru interrogator** from
  the source image ("one boy, one girl… bed sheets, black
  hair, blush… it knows what that is… this button can write
  a prompt for you"). Not hand-typed, not the txt2img
  prompt.
- **The img2img pass is a denoise series, one image, one
  seed:** denoise guidance stated as a rule — "you'll want
  to keep it within a range from 20 percent just to do an
  upscaling and to 50 percent" — then demonstrated at
  **0.35** (shading/eyes shift toward 2.5D, pose and
  contents held) and at **0.75** ("completely reimagined…
  got rid of him, got rid of the penis… completely changed
  the face and the hairstyle"), plus at least one further
  blend attempt. The 4 browsed files (0000–0003,
  `…-1854461071.png`) are this series + the original,
  compared side by side in the browser. **Correction to
  §7:** the 0.75 pass is img2img-family (the panel sampled
  at t3480 is the inpaint-sketch sub-tab of that surface),
  not a separate "winner refinement" step; claim C10 is
  reworded in the tally below. Sampler for the series:
  he changes it *to* DPM++ 2S a Karras from Euler a
  ("some of these samplers are much more advanced") —
  [SCREEN] crop3480 confirms DPM++ 2S a Karras, 20 steps.
- **Anime inpaint target = the FACE** (resolves §10
  UNREADABLE 3): "let's say I just wanted to add some more
  details to the eyes… the whole face… I'll just paint
  over face here and we can inpaint the face." Masked
  content guidance: **original** is the default "because
  if not, your face will end up not really fitting into
  the picture"; fill / latent noise / latent nothing
  explained and dismissed. **Only-masked mechanism, in his
  words:** it "draws a square around your mask… kind of
  like zooming in and increasing the resolution" and
  generates that square at the Resize-to size — he sets
  **1024×1024** for the face.
- **Inpaint prompt is a variable, and the first run fails
  instructively:** with the inherited scene prompt, the
  pass "tried to put all of this in that little box". He
  replaces the prompt with a local one ("face", "high
  quality" tags) and re-runs at denoise **0.5**, then
  "try one at 35% — it's always good to try a couple".
  Anime face inpaint events: ≥3 generations (inherited
  prompt → local prompt @0.5 → @0.35).
- **His GPU is an RTX 4090** [SPOKEN, theAllysMix batch]:
  "my computer is running through it real fast… the 4090".
  Per-image times in §10 stand (1.5–2.5 s at 512–768²).
- **theAllysMix batch:** settings sent from an AAM image
  to txt2img did **not** switch the checkpoint ("it didn't
  switch the model… there's a way you can set it up to
  where whenever you send something over it'll switch the
  model") — the batch of 12 at 768×768 then ran on
  theAllysMix as intended. Curation in words: "this model
  is pretty unruly, so you do have to run batches really
  to pick one that's really good… this looks like the best
  one out of the whole bunch."
- **Repair order (new, explicit): upscale BEFORE inpaint.**
  He first tries to fold a 1.5× resize into the inpaint
  (1190²/1536² musings), reverses himself — "I should
  upscale it before I do the inpaint" — runs an img2img
  resize-by-1.5 pass ("small improvements… did increase
  the resolution, took a little bit of color out"), and
  only then inpaints the face at **1152×1152**
  (denoise 0.35 per crop4565). Verdict on the result:
  "definitely a higher detail face, a lot less little
  errors… **this one's ready to post right there**" — the
  tutorial's only explicit keeper declaration, and it is
  the product of batch → pick → upscale → inpaint, in
  that order.
- **Second-half event tally** (same counting rule as §6):
  interrogate-prompt ×1; img2img generations ×≥3 (denoise
  0.35, 0.75, blend retry) + sampler change ×1 (Euler a →
  DPM++ 2S a Karras); inpaint generations ×≥3 (anime face)
  + ×1 (photoreal face); prompt-for-region changes ×1;
  batch runs ×1 (12, theAllysMix); seed changes ×0 (the
  1854461071 lock holds across txt2img → img2img →
  inpaint → and is even left in the seed field for the
  photoreal inpaint); checkpoint changes ×1 (AAM →
  theAllysMix, via send-to-txt2img + manual switch).
  **Full-video totals:** seed re-rolls ≥6 + 2 batch runs
  (24 rolls); prompt changes ≥6; LoRA weight ×1; negative
  assembly ×3; resolution ×≥5; checkpoint ×2; seed locks
  ×3 contexts; transplants ×1 (+1 send-to-txt2img);
  fix-up generations ×≥7. Fix-ups are ~15% of all
  generation events; batches are ~55% of all rolls.
- **Claims amended:** C9 strengthened (his own words:
  batches are *required* to pick a good one on an unruly
  model). C10 reworded: a denoise *series* on one image at
  its locked seed explores the blend between two
  checkpoints' styles (0.35 = shading pass, 0.75 =
  recomposition) — the variation is a style dial, not a
  refinement. New claim C13: repair order is upscale →
  inpaint, and the inpaint prompt must describe the
  *region*, not the scene (the inherited-prompt failure).
  New claim C14: only-masked inpaint is a resolution
  device as much as a repair device (the masked square is
  regenerated at the Resize-to resolution).
- **Keep-rate, restated with the keeper declaration:** the
  one image he calls "ready to post" emerges from
  12 batch rolls → 1 pick → 1 upscale pass → 1 inpaint
  pass. Across the tutorial's generation demos, declared
  keepers = 1 (the photoreal portrait) from ~45+ rolls —
  but §8's limit stands: this counts *declared* keepers
  on camera, not his archive's true keeper rate.
