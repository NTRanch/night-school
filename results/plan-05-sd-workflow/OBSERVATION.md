# Plan 05 — Pass 1 Observation

Plan: `repo/plans/05-stable-diffusion-nsfw-art-harry-heck.md`
Intake: `runs/plan-05/INTAKE.md` (Pass 0; SHOULD-BE-SEEN adopted
verbatim from the plan, written before viewing).
Capture: `runs/plan-05/MANIFEST.md`; canonical media on primo at
`~/.local/share/pax/night-school/plan-05/` (720p complete +
360p complete; 1080p rendition defective past 2,679 s — see
MANIFEST).

## Media and transcript of record

- Media: h264 1920×1080 @60fps capture (720p rendition
  1280×720, full span; 1080p frames used 0–2,679 s), duration
  4,730.78 s (1:18:50.8) — page states 4,731 s.
- Frames in `runs/plan-05/frames/` (50 files): 12 grid frames
  every 240 s from the 1080p file (g0005…g2645), 8 grid frames
  from the 360p file (h2885…h4565), 9 targeted 1080p frames
  (t120…t2620), 9 targeted 360p frames (u2760…u4680), 10
  native 720p frames (m2760…m4565), 3 native 1080p frames
  (n485, n2165, n2405, n2620) and 7 native-resolution crops of
  parameter panels (crop485-info, crop2165-prompt,
  crop2405-info, crop2620-hires, crop2885-hires,
  crop3480-img2img, crop3845-inpaint, crop4565-inpaint).
  Every numeric value below names its frame.
- Transcript: chunked lane from the **360p file's audio**
  (2 chunks @3,300 s; map in `chunk-map.txt`). Stitch +
  loop census in MANIFEST close-out / `loop-census.txt`.
  Tier: single-transcriber, **UNCONFIRMED**. The screen
  governs: settings are tagged [SCREEN] (read off a named
  frame), [SPOKEN] (narration only), [BOTH].

## 1. What this video actually is — premise check

The plan's premise **HOLDS, with a scope note**. This is a
genuine end-to-end generation workflow tutorial in
**AUTOMATIC1111 WebUI v1.5.1** [SCREEN, footer in every
frame: version v1.5.1, python 3.10.6, torch 2.0.1+cu118,
xformers 0.0.20, gradio 3.32.0, Cozy Nest theme v2.4.3],
taught unscripted by Harry Heck ("my first ever tutorial
collab with Anime Neon [Nyan]" [SPOKEN 0:00]). Scope note:
WebUI *installation* is explicitly NOT covered — he points
to a pinned install post in a Discord AI channel [SPOKEN
~3:40]. What is covered, in order: txt2img from the stock
checkpoint → settings literacy → Civitai as the model
source → extension installs → in-app model/embedding
downloads → character LoRA use with weight tuning →
negative-embedding stack → seed locking for controlled
comparisons → Civitai generation-data transplant (prompt +
full settings + seed) with hires. fix → batch-of-12
curation → img2img / inpaint-sketch passes on the batch
winner → inpaint repair on two images (anime hero,
photoreal portrait) → close on the Civitai model page.

It is an **SD 1.5** workflow throughout (2023-era stack).
No ControlNet ("that's one to a dozen videos by itself;
I'm not going to get into it" [SPOKEN ~21:00]), no
checkpoint merging, no training — all three named and
deliberately excluded.

Section map (global timestamps):
- 0:00–3:30 — cold open: the joke prompt on stock SD 1.5.
- 3:30–13:00 — UI tour + settings literacy (steps, CFG,
  resolution discipline, seed) with defect demos.
- 13:00–20:00 — Civitai: categories, filters, the Makima
  character LoRA as the worked example of what a LoRA is.
- 20:00–27:00 — extensions: Infinite Image Browsing, Cozy
  Nest, Civitai Helper, Booru tag autocomplete; restart.
- 27:00–35:00 — Civitai Helper downloads in-app: AAM
  checkpoint; negative embeddings (bad-hands-5, bad-artist,
  EasyNegative); scan/previews.
- 35:00–43:00 — character LoRA at work: Elinalise on AAM;
  weight 0.50 → 0.80; negative-embedding stack assembled;
  same-seed A/B of the embeddings' effect; TI-hash check.
- 43:00–52:00 — generation-data transplant from a Civitai
  sample (prompt, negative, sampler, hires, ENSD, seed);
  SwinIR upscaler error and fix; near-identical
  reproduction; then the batch-of-12 run and its grid.
- 52:00–68:00 — img2img / inpaint-sketch on the batch
  winner at its locked seed; output browsing (4 files).
- 68:00–78:00 — second checkpoint (theAllysMix, realistic):
  batch of 12 from the same joke prompt + LoRA; face
  inpaint at denoise 0.35.
- 78:00–78:51 — close on the AAM Civitai page.

## 2. The cold open (0:00–3:30) — the control-sample baseline

- Checkpoint: **v1-5-pruned-emaonly.safetensors [6ce0161689]**
  [SCREEN g0005] — the stock SD 1.5 checkpoint. Sampler
  **Euler a**, **20 steps**, seed **-1** (random), empty
  negative [SCREEN g0005/g0725]. Prompt typed live:
  "I want to see some boobies" [SCREEN t120/g0725].
- Results are bad and he says so: deformed anatomy, a
  "finger penis thing sitting on her shoulder" [SPOKEN
  ~1:50], an eyeless face on the re-roll [SPOKEN ~2:20].
  Defect-spotting is taught as a skill in the first three
  minutes: "It's kind of like a game of Where's Waldo. You
  got to look around, see what's wrong with the image."
  [SPOKEN ~2:10]
- He generates **at least 3 times** in the cold open on the
  untouched defaults (frames t120, g0245, t600 show three
  distinct outputs) — roll-the-seed iteration before any
  teaching starts. Event class: seed-roll ×3, nothing else
  changed.

## 3. Settings literacy (3:30–13:00)

- **Filename pattern set to include the seed** in Settings →
  Saving images/grids [SCREEN t300] — provenance by
  filename from minute ~5 (later output files are literally
  named `00001-3909785413.png`, `0000-1854461071.png`).
  "Always save all generated images" is on: every roll is
  kept on disk, curation happens in the browser, not by
  deletion at generation time.
- First recorded generation info [SCREEN n485/crop485-info]:
  "boobies / Euler a, CFG scale: 7, Seed: 3909785413, Size:
  512x512, Model hash: 6ce0161689, Model: v1-5-pruned-emaonly,
  Clip skip: 2, Version: v1.5.1" — so his standing txt2img
  defaults are **Euler a / 20 steps / CFG 7 / 512×512 /
  clip skip 2** even on the stock checkpoint.
- Steps: "how many times [the model] makes a pass to refine
  this picture; more steps, longer it takes" [SPOKEN];
  CFG: "how much to pay attention to your prompt… at the
  higher end it really starts breaking apart" [SPOKEN].
- **Resolution discipline (a claim with a mechanism):** the
  base model "was trained at 512 by 512; take it above 768
  it kind of tries to put two pictures together… it made
  her into a Siamese woman" [SPOKEN ~9:30; SCREEN t600 —
  the two-headed output]. Demonstrated again at 1024×1024
  on the SD 1.5 anime checkpoint (~40:00 [SPOKEN]): extra
  monster figure composited in. His working resolutions
  stay at the model's trained size (512, 768) and scale is
  delegated to hires. fix / upscalers, never to the base
  latent.
- Seed: "the random noise that it starts with… -1 just
  means random" [SPOKEN]. The X/Y/Z plot script is named
  as the systematic way to sweep a setting [SPOKEN + SCREEN
  g0725 script menu] but never run in the tutorial.

## 4. Checkpoint and LoRA stack (13:00–35:00)

- **Source discipline:** "where do you get your models
  from? There's pretty much only one place right now and
  that's CivitAI" [SPOKEN]. Categories toured: checkpoints
  are "the full models… 2.5 to 8 gigabytes… based off 1.5
  or SDXL 1.0" [SPOKEN]; LoRAs "insert layers into the
  models to guide it towards a character or style"
  [SPOKEN].
- Worked LoRA example: **Makima (Chainsaw Man) LoRA**
  [SCREEN g0965]: SD 1.5 LoRA, trigger words "MAKIMA
  (CHAINSAW MAN)", two preview styles (anime vs 2.5D) from
  one LoRA. Not downloaded on camera; the character LoRA
  actually used is Elinalise (below).
- Extensions installed [SPOKEN + SCREEN g1205/g1445]:
  **Infinite Image Browsing**, **Cozy Nest** (theme; moves
  the extra-networks tray), **Civitai Helper**, **Booru tag
  autocomplete**. Apply + restart.
- Downloads via Civitai Helper (in-app, by pasted Civitai
  URL, with scan + preview fetch):
  1. **AAM — AnyLoRA Anime Mix** checkpoint ("Anime
     Screencap Style Model", by Lykon; SD 1.5; the page at
     g2645/u4680 shows 15,386 downloads, hash AUTOV2
     354B8C571D; in-WebUI hash **354b8c571d**) [SCREEN
     g2645, crop2405-info]. "3 or 4 gigabytes" [SPOKEN].
  2. **Negative embeddings** [SCREEN g1685/t1800]: from the
     embedding shelf — **bad-hands-5**, **bad-artist**
     (Civitai model 5224), **EasyNegative** (model 7808,
     version "EasyNegative_9200" in the helper's download
     field [SCREEN g1685]). "These negative embeddings are
     very important" [SPOKEN].
  3. A second checkpoint later: **theAllysMix**
     (checkpoint hash in footers from ~56:00:
     [9d7d8f…] partial — see UNREADABLEs) for the realistic
     closing demo [SCREEN m3365/m4085 range].

## 5. Prompt grammar (35:00–43:00)

His own generations use a three-slot grammar, consistent
across every demo:

1. **Subject slot, plain language or trigger:** "you want
   to see some boobies" (the running test prompt, sic —
   first typed as "I want to see some boobies", later
   retyped without "I" [SCREEN t120 vs g2165]), or the
   character form "Elinalise, nude" [SCREEN crop2405-info].
2. **LoRA slot, inline in the prompt:**
   `<lora:ElinaliseV6 - NAI-000010:0.80>` [SCREEN
   crop2165-prompt/crop2405-info]. The extra-networks card
   inserts it at weight 1.0 by default [SPOKEN: "it comes
   with a weight; the weight of 1 is the training weight…
   think of it like a percentage"]. He runs it at **0.50**
   first [SCREEN t2100], judges "that does not look very
   much like her at all", and raises it to **0.80**
   [SPOKEN + SCREEN crop2405-info] — a named-variable
   change with the reason stated (identity strength).
3. **Negative slot = embedding names only:** the finished
   negative reads, in full, **"bad-hands-5, bad-artist,
   EasyNegative"** [SCREEN g2405, u3240, u4085]. No quality
   words, no anatomy lists, no boilerplate: three textual
   inversions carry the whole negative. Assembly is shown:
   clicking bad-hands-5 drops it in the POSITIVE prompt by
   default; he cuts and pastes it into the negative
   [SPOKEN].

Contrast (recorded, not conflated): the **Civitai sample
prompt** he transplants at 43:00 is a different grammar —
"masterpiece, best quality, 1girl, 1boy, spread legs, sex,
nude, large breasts, penis, vaginal, open mouth, brown
eyes, long hair, raw, black hair, on bed, pov" with
negative "(worst quality, low quality:1.5),
(FastNegativeEmbedding:0.9)" [SCREEN g2645 sample card] —
 Danbooru-tag style with quality boilerplate and a weighted
negative. That grammar is the *sample author's*, shown as
data on the model page; his own prompts (§5.1–5.3) never
use it. The distinction matters for Pass 2: two prompt
grammars appear in this video, and only one is his.

**Trigger-word discipline:** with the LoRA at 0.80 the
first attempts omit the character's name and the hair/eye
colours come out wrong ("she really doesn't have red hair
or blue eyes… it's got the hair shape down"); adding the
name — "we'll go ahead and call up her name" — fixes the
eye colour toward canon [SPOKEN]. Identity = LoRA +
trigger word together, neither alone.

**TI-hash verification:** the generation-info block lists
"TI hashes" for the embeddings actually fired; when a name
is mistyped the hash line drops to two and he catches it:
"you have to put in the exact file name to call it up
correctly" [SPOKEN]. A provenance self-check built into
his loop.

## 6. Iteration behaviour — event counts (Pass 1 tally)

Counting rule: one event = one visible Generate press or
one deliberate change of exactly one variable class,
counted from frames + narration jointly; where the two
disagree the screen governs. Full-video tally in the
close-out addendum; the first-half tally (0–2,679 s):

| Event class | Count (0–2,679 s) | Notes |
|---|---|---|
| Seed re-roll, nothing else changed (seed -1) | ≥6 | cold open ×3; steps/CFG demos; 768² test |
| Prompt text change | 4 | joke prompt typed; shortened; "Elinalise, nude" ×2 forms |
| LoRA weight change | 1 | 0.50 → 0.80 (identity judged too weak) |
| Negative change | 3 | bad-hands-5 added; bad-artist added; EasyNegative added (one assembly sequence) |
| Resolution change | 4 | 512→768; 768→512 (reset); →1024 test; →512×768 (transplant) |
| Checkpoint change | 1 | stock 1.5 → AAM |
| Seed lock (recycle a known seed) | 2 | embedding A/B; LoRA-with/without comparison |
| Settings transplant (copied gen data) | 1 | Civitai sample → full settings incl. seed + ENSD |
| Batch change | 0 in first half | batch stays 1×1 until the 43:00+ runs |

The pattern the counts show: **one variable at a time,
with the seed locked when a variable's effect is the
question** — his embedding demo is a controlled A/B
(generate at locked seed with the stack; strip the stack;
regenerate; compare [SPOKEN]) — and **the seed rolled
freely when exploration is the point**. That is the same
discipline the estate's rounds run, arrived at
independently; the difference is bookkeeping (his is
filenames + the info block; ours is stamped run records).

## 7. Fix-up passes and curation (43:00–78:51)

(Second-half detail completed from chunk-2 transcript +
720p frames; the settings below are [SCREEN]-verified from
the named crops, the narration mapping is in the addendum.)

- **Hires. fix** [SCREEN crop2620-hires / crop2885-hires]:
  base **512×768, 25 steps, Euler a, CFG 7** → upscaler
  **SwinIR_4x**, **hires steps 15**, **denoising 0.4**,
  **upscale by 1.8** → 921×1382. Two runs use it: (a) the
  transplant run — batch 1×1, seed fixed at the sample's
  **3020654048**, ENSD override 31337 carried from the
  copied data; first attempt **errored on the upscaler**
  (SwinIR not yet loaded) and he switches the upscaler
  selection and re-runs [SPOKEN]; the result is "really
  similar… almost identical" to the Civitai sample
  [SPOKEN]; (b) the curation run — same hires settings,
  **batch count 12, seed -1**.
- **Batch-of-12 curation** [SCREEN m3000/u3000]: the
  12-up grid of the black-haired subject; he works from
  the grid into the image browser and takes one forward
  (the on-bed POV image, seed **1854461071** — the seed
  A1111 assigns the batch's first slot). Visible keep
  rate for the batch: **1 of 12 carried forward** (see §8
  for what "kept" can and cannot mean here).
- **img2img / inpaint sketch on the winner** [SCREEN
  m3365/u3240, crop3480-img2img]: the winner is sent to
  img2img; the pass that produces the browsed outputs is
  the **inpaint sketch** sub-tab at **DPM++ 2S a Karras,
  20 steps, CFG 7, denoising 0.75, seed locked at
  1854461071**, resize-by scale 1 (920×1376). Output
  browser [SCREEN h3605/u3960]: **4 files**, all named
  `…-1854461071.png` (0000–0003) in `outputs/img2img-images`
  — four passes at one locked seed, browsed side by side;
  one is viewed full-screen [SCREEN u3720] (the finished
  POV image). Whether the four differ by mask, denoise or
  prompt is a chunk-2 narration question (addendum).
- **Inpaint (anime hero)** [SCREEN crop3845-inpaint]:
  **Only masked, padding 32 px, mask blur 4, masked
  content = original, resize-to 1024×1024, DPM++ 2S a
  Karras, 20 steps, CFG 7, denoising 0.5**, batch 1×1.
  The masked region on the hero image is small (the
  preview inset sits at the lower centre of the frame —
  target read in the addendum; at 720p the mask itself is
  not separately visible in the sampled frames).
- **Inpaint (photoreal portrait)** [SCREEN
  crop4565-inpaint]: same inpaint settings family on the
  theAllysMix redhead batch winner; the mask is the
  **face** [SCREEN u4440/h4325: black mask painted over
  the face in the inpaint canvas]; **resize-to 1152×1152,
  denoising 0.35**, seed field shows 1854461071 (recycled
  hero seed, carried across checkpoints — the seed is his
  bookmark, not a per-image variable).
- **Restore faces is never enabled** in any sampled frame
  (checkbox off in txt2img, img2img and inpaint panels
  alike). Face repair, where done, is manual inpaint —
  there is no ADetailer/CodeFormer step in this workflow.

## 8. Curation and keep rate, as observed

- Stated criteria [SPOKEN]: none as a list. The working
  criteria visible across the video are: (1) deformity
  veto — the Where's-Waldo scan (§2); (2) identity match
  for LoRA subjects (hair/eye colour vs canon, §5);
  (3) "not very refined" as a publishability bar — base-
  model output "you'd probably be laughed off [the art
  server]" [SPOKEN ~4:00].
- Visible numbers: cold open 3 rolls → 0 kept (all
  rejected on deformity); Elinalise sequence ~6 generations
  → 1 carried into the nude demo line; transplant 1 → 1
  (reproduction goal, kept by construction); batch of 12
  → 1 carried forward; img2img family 4 → 1 viewed as the
  finish; redhead batch of 12 → 1 taken to inpaint.
  **Observed carry-forward rate ≈ 1 per generation batch,
  ~8–15% of rolls** — with the caveat that "carried
  forward" (taken to the next pass) is the only keep event
  the video makes visible; final publish/discard decisions
  happen off camera, so a true keeper rate is NOT
  observable from this source (recorded as a limit, §10).
- Nothing is deleted on camera. "Always save all" +
  seed-in-filename + the image browser is the whole
  curation apparatus: generation and judgement are
  separate passes over a complete archive.

## 9. Claims list (numbered for Pass 3)

- C1. Base SD 1.5 at its trained size with a plain-language
  prompt produces NSFW images but with frequent anatomy
  deformities; above ~768 px it duplicates subjects.
  [BOTH, §2–3]
- C2. Steps trade time for refinement; excessive CFG
  "breaks apart" the image. [SPOKEN, §3]
- C3. A community checkpoint (AAM) at 768², Euler a 20 /
  CFG 7 / clip skip 2, out-resolves the stock checkpoint
  for anime NSFW. [BOTH, §4–5]
- C4. A character LoRA needs its trigger word AND a tuned
  weight (0.80 ≫ 0.50 for Elinalise) to hold identity.
  [BOTH, §5]
- C5. The three-embedding negative stack (bad-hands-5,
  bad-artist, EasyNegative) visibly improves quality at a
  locked seed vs no negative. [BOTH, §5–6]
- C6. Seed locking + the recycle button makes any single
  variable's effect directly comparable. [BOTH, §6]
- C7. Copied Civitai generation data (prompt + settings +
  seed + ENSD) reproduces the sample image near-identically
  on the same checkpoint. [BOTH, §7]
- C8. Hires. fix (SwinIR_4x, ×1.8, denoise 0.4, 15 steps)
  scales a 512×768 base to 921×1382 without the
  duplication failure of a large base latent. [SCREEN, §7]
- C9. A batch of 12 at a locked prompt yields ~1 image
  worth carrying forward. [SCREEN, §7–8]
- C10. Whole-image variation (inpaint sketch, denoise
  0.75) at the winner's own seed refines composition
  while holding identity. [SCREEN, §7]
- C11. Masked inpaint at denoise 0.5 (1024²) / 0.35
  (1152²) repairs a local region (face) without
  re-rolling the image. [SCREEN, §7]
- C12. Filename-embedded seeds + save-all + an image
  browser are sufficient curation infrastructure.
  [BOTH, §3/§8]

## 10. UNREADABLEs, disagreements, limits

- UNREADABLE (5): (1) theAllysMix checkpoint hash — footer
  shows [9d7d8f…] truncated in every sampled frame;
  (2) the exact upscaler error text in the transplant
  failure (console window too small; the fix — selecting
  SwinIR_4x — is visible, the message is not);
  (3) the inpaint mask target on the anime hero (§7) at
  the sampled timestamps; (4) the prompt text in the
  redhead batch (the field shows the joke prompt + a LoRA
  line whose weight digit is ambiguous at 720p: 0.99 vs
  0.80); (5) per-image generation times beyond the two
  shown (2.5 s Elinalise 768²; 1.5 s boobies 512²).
- Disagreements (2): (1) at t3480 the panel is the
  *inpaint sketch* sub-tab, not plain img2img — an early
  grid read (§7 first pass) called the 0.75 pass
  "img2img"; the native crop corrects it and the record
  follows the crop. (2) The batch-12 grid (m3000) shows
  the subject in ~12 distinct compositions while the
  hires panel (crop2885) shows seed -1: A1111 batch-count
  semantics (consecutive seeds from a random base) are
  inferred from the UI + filename evidence, not stated by
  the creator — marked as inference wherever used.
- Limits: single-transcriber UNCONFIRMED narration;
  keeper decisions off camera (§8); the creator's machine
  (GPU, per-image times) mostly unstated, so keepers/hour
  in Pass 2 is computed from batch structure + the two
  visible timings, not from a wall-clock log.
