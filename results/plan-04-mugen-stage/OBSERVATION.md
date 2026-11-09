# Plan 04 — Timed Observation (Pass 1)

Source: rule34video 3417736, "MUGEN Factory: Streaming the Creation
of a Stage" (Fapmaster/Viket), 4,127 s. Screen governs over
narration throughout: the audio lane produced only whisper loop
hallucinations in the processed span ("Thank you." / "Bye." /
"Fight!" at 30 s spacing — the no-speech signature over music and
game audio; see MANIFEST.md), so every claim below is anchored to a
frame, not to the transcript. Single-transcriber tier: UNCONFIRMED.

Method: 30 s grid (138 frames, 5 contact sheets) + 29 native-res
frames at parameter-bearing moments, read directly. Frame files:
`frames/sheet1–5.jpg`, `frames/native/t<sec>.png` in this run dir
(copies; originals on primo beside the media).

## What the video is

Exactly what the title promises: one full streamed stage build,
start to finish, in a Discord-streamed session (server "Fighter
Furry Fac…", streamer Viket/Fapmaster, live chat participating).
The stage built is **"Glitter Cookie's Trial"** — a night-waterfront
stage themed on Cookie Run's Shining Glitter Cookie trial stage,
whose OST becomes the stage music and whose artwork is the visual
reference. The build runs: template copy → sourced plate →
Photoshop slicing/keying → Fighter Factory .sff/.def wiring →
repeated in-engine test fights → foreground character layers →
select.def registration → final fights on the finished stage.

## Timed log (t in seconds from media start)

- **0–150** — Explorer over his `stages/` taxonomy (folders:
  `#1Training Rooms`, `#2Hentai`, `#3Pokemon`, `#4Sonic`,
  `#5beat em up`, `#6Nightclubs`, `#7Forests`, `#8Spooky`,
  `#9Miscs sfw`, `#10specific char stages`, `#11Comissions`).
  The new stage starts as a copy of his template pair
  **Creation1.def (10.0 KB) + Creation1.sff**.
- **~150–330** — His written stage guide open (the template .def's
  own comment text): [LOCATION] section explains stage paths;
  `[Music] bgmusic`, `bgvolume = 255` guidance.
- **~360–660** — Photoshop work on the city plate; the template
  sprite in Fighter Factory (pink measured grid, numbered columns,
  floor band) — group 0 index 0, 1035×775 px, axis (518, 598);
  palette (.act) handling.
- **~660–840** — Art sourcing: Google image search ("city streets
  night anime"); a painted anime night-skyline waterfront image is
  chosen (artist watermark legible on a lamppost in the FF sprite
  view). A Cookie Run OST YouTube video is open alongside — the
  composition reference (purple city, palms, railing, pink car).
- **840** — `cookie base.psd` (~16 layers): the sky is cut out of
  the plate with the magic wand (tolerance 22); the template grid
  shows through behind, hand-marked "0.8".
- **900–960** — FF sprite editor: the plate (group 0, index 1) is
  **1035×775 px, 8-bit**, axis (518, 598); he then **mirror-widens
  it to 1396×775** (axis 698, 598) — the in-engine frames later
  show the mirror seam symmetry in the skyline.
- **990** — Discord: viewer Powi Pinku shares the star-sky image —
  "use dis oke / u have to loop it tho". Chat tips recorded
  verbatim: "TIP / PUT TUMBLR ON IT / FOR SOME REASON WHEN U LOOK
  UP WITH TUMBLR PRETTY IMAGES SHOW UP LOL"; a viewer asks how to
  set up chars to test stages in Fighter Factory.
- **1020** — FF Options: engine profile "mugen 1.1". The template
  .def on screen (the SquidCity tab uses the same template):
  `[BG BACKGROUND] type=normal, spriteno=0,1, start=0,620,
  delta=1,1, mask=1, velocity=0.00,0.00, tile=1,0, tilespacing=0,0,
  scalestart=1,1`, with `;trans = addalpha` / `;alpha = 100, 120`
  present but commented out. Status bar: "Syntax error count: 8".
- **1080** — **In-engine test #1**: city plate + floor render;
  the sky is **solid black** — no back layer wired yet (his own
  comment predicts exactly this failure: see claim C4).
- **~1200–1500** — The star sky is built in Photoshop (purple
  gradient + star specks, the Discord-shared image); a YouTube
  downloader fetches the stage music (Cookie Run OST,
  "Shining Glitter Cookie's Trial Theme"); test fight #2.
- **1815** — .def state A (230 lines): `[BG stars] type=anim,
  actionno=1, start=0,620, delta=1,1, mask=1, tile=0,0,
  tilespacing=000,000, scalestart=1.00,1.00, trans=none,
  alpha=255,0`; `[BG BACKGROUND] spriteno=0,1, start=0,620,
  delta=1,1, tile=1,0`.
- **2040** — Test fight #3 ("FIGHT"): mirror symmetry of the
  widened plate plainly visible; sky still black at top.
- **~2250–2580** — Photoshop: green-key compositing (the bright
  green is the mask colour for `mask = 1`); star gradient refined.
- **2580** — .def state B (234 lines): the stars were reworked —
  `[BG stars] type=anim, actionno=1, start=100,1300, delta=1,1,
  mask=1, tile=0,0, scalestart=6,3`; `[BG BACKGROUND]
  spriteno=1,1, start=0,620, delta=1,1, mask=1, velocity=0,0,
  tile=1,0, tilespacing=0,0, scalestart=1,1` (trans/alpha still
  commented); then a **duplicate** `[BG stars] type=normal,
  actionno=1, start=100,1300, delta=1,1, mask=1, tile=0,0,
  scalestart=6,3` — a normal-type BG carrying actionno is inert
  in MUGEN (normal reads spriteno); a copy-paste slip, resident
  among the 8–9 syntax errors FF reports. `[Begin Action 1]`
  begins at line 217.
- **~2640–2880** — Browser: a "Complete Stage Creation" guide tab
  (MFG) is open next to "Fighter Factory 3 problem" and the
  SquidCity download tab (MUGEN Archive) — the template's origin
  trail. The Cookie Run OST video is paused on the reference art.
- **3030** — .def lines 110–160 (see "Values copied exactly"):
  [Music], [BGdef], [Reflection], [Shadow], and the template's
  BG-sprites teaching comments.
- **~3030–3330** — `cookie base.psd`: a billboard element is
  composited into the plate (Shining Glitter Cookie stage image,
  centre, over the waterfront); tabs `asset_1_000009.png` …
  `asset_1_000014.png` and `bulbs.psd` are open — a frame sequence
  and a light-bulb sheet pass through Photoshop.
- **3360–3630** — FF sprite editor: the .sff now holds **20
  sprites**; group 3 holds character sprites. Photoshop: the
  foreground character ("cookie bitch.png") composited on green.
- **3840** — Sprite editor: group 3 index 2 (189×189 blue grid
  sprite visible in list position 16/20); palette 5/5.
- **3870** — .def state C (271 lines): line 79 `screenright = 30`
  (tail of [Bound]); [Scaling] and [StageInfo] as below; the
  Definitions tree now shows **7 BG sections**.
- **3930** — .def tail (283 lines): the floor + foreground stack
  (below) and the full `[Begin Action 1]`: frames
  `0,1 / 0,2 / 0,3 / 0,4 / 0,5 / 0,6` at **10 ticks** each,
  `0,7` at **50 ticks**, `0,8` at **10 ticks** — 8 frames,
  120-tick loop (2.0 s at 60 ticks/s).
- **~3900–4127** — select.def edited in Notepad to register the
  stage; character-select screen; **final fights on the finished
  stage**: purple star sky, mirrored city, waterfront floor with
  reflections, billboard, and the foreground witch figure sitting
  at bottom-right, in front of the fighters.

## Values copied exactly (screen-read; frame refs)

Stage identity / file wiring (t3030, t3870):
- `[Music] bgmusic = stages/cookie bitch.mp3`, `bgvolume = 255`
- `[BGdef] spr = Creation1.sff`, `debugbg = 0`
- `[Reflection] intensity = 50` — under his own section banner
  ";[THE I HAVE NO FUCKING CLUE WHAT DOES THIS PART DOES SECTION]"
- `[Shadow] intensity = 64`, `color = 0,0,0`, `yscale = -.1`
  (being edited at capture), `fade.range = -400,-100`
- `[Scaling] topz = 0`, `botz = 50`, `topscale = 1`,
  `botscale = 1.2` — under ";[Settings 2 SECTION] … DO NOT MODIFY
  THESE VALUES … DO NOT TOUCH GO TO STAGE INFO"
- `[StageInfo] zoffset = 310`, `autoturn = 1`, `resetBG = 0`,
  `xscale = .3.5`, `yscale = .3.5` (as written — a malformed
  float; see UNREADABLEs), `localcoord = 534,400` (first digit
  least certain)
- `[Bound]` — only `screenright = 30` read (line 79, t3870).

Final layer stack, in file order = draw order (t2580 + t3930):
1. `[BG stars]` anim, actionno 1, start 100,1300, delta 1,1,
   mask 1, tile 0,0, scalestart 6,3
2. `[BG BACKGROUND]` normal, spriteno 1,1 (0,1 in state A),
   start 0,620, delta 1,1, mask 1, velocity 0,0, tile 1,0,
   tilespacing 0,0, scalestart 1,1
3. `[BG stars]` normal (duplicate, inert actionno), as (1)
4. `[BG …]` normal, spriteno 2,2, start 0,620, delta 1,1,
   mask 1, tile 1,0, scalestart 1,1 (header above frame cut;
   the tiled floor/front strip)
5. `[BG Cookitch]` normal, spriteno 3,1, start 0,620, delta 1,1,
   mask 1, tile 0,0, scalestart 1.5,1.5
6. `[BG Cookwitch solid]` normal, spriteno 3,2, start 0,620,
   layerno 0, delta 1,1, mask 1, tile 0,0, scalestart 2,4
   (mid-edit at capture)
7. `[BG Cookwitch trans]` normal, spriteno 3,2, start 0,620,
   **layerno 1**, delta 1,1, mask 1, tile 0,0,
   scalestart 2.5,2.5, **trans = addalpha, alpha = 100, 120**

Every element anchors at start y = 620 (x = 0 except the stars
at x = 100). **Every delta in the stage is 1,1.**

## The template's doctrine, in his own comments (t3030, t2580, t1815, t3870)

- ";delta allows you to create depth in the stage, by making the
  elements move one between the others, as some elements our
  closer to the fight while other are very far. **For the floor,
  the delta should ALWAYS be 1,1 for low-res stages, and 2,2 for
  high-res stages. If you fail to comply with this, the characters
  will appear to slide on the floor**, which is not suitable at
  all. **The further the element is in the background, the lower
  its delta must be**, in order for it to look natural and
  realistic."
- "; UPPER BG ELEMENTS ARE BEHIND DOWN BG ELEMENTS ARE UPPER
  like if bg floor is at the bottom then the floor is gonna be
  above every bg element, but if bg floor is at the top then bg
  floor is gonna be on the background" — file order is draw order.
- ";start is the location where the sprite starts, i dont
  recommend change 620 is exactly where the sprite is moving
  around the sprites section; of course this change when you
  modify the scalestart"
- ";mask 1 REMOVES BACKGROUND 0 ENABLES BACKGROUND, IF YOU DONT
  HAVE A BACKGROUND IT WILL BE JUST A BLACK SCREEN, SERIOUSLY
  WHY WOULD YOU WANT TO TURN OFF THIS?"
- ";velocity ALLOW MAKES A BG ELEMENT TO MOVE AROUND TO THE
  STAGE WITHOUT NEED TO ANIMATED IT … tile WITH VELOCITY ALLOWS
  BG ELEMENT TO COME BACK, WITHOUT VELOCITY Multiplies the same
  sprite over all the stage"
- "; layerno = 1 … will make the bg element above all the sprites
  INCLUDING THE CHARS FIGHTING"
- ";alpha … DEFAULT IS 255,255 MY RECOMMENDATION ON TRANSPARENCY
  IS 100, 120" / "; ANIM TRANS PROPS ARE MUGEN 1.1 ONLY!"
- ";tip for low res and medium res sprites … medium res sprite be
  equal to low res use 0.5 … low res sprite be same as a medium
  res you gotta use 2 … low res is half the size of medium"
- ";zoffset is the position where the players stand at, it
  defines the ground level. + is down - is up, i dont recommend
  modify the zoffset for nsfw stages"
- ";the first bg contains the trans and alpha codes for make them
  work you must delete ";" text when you use … is just for make
  a comment is useful for turn off a code"

## Art sourcing and cleanup per source

- **City plate**: one painted anime background found via Google
  Images (Tumblr recommended in chat for exactly this). Cleanup:
  sky cut out (magic wand, tolerance 22), palette-reduced to
  8-bit in the .sff, **mirror-widened 1035→1396 px** when the
  stage outgrew the art.
- **Star sky**: an image shared in Discord chat ("u have to loop
  it tho") + Photoshop gradient/star work; wired as an 8-frame
  anim scaled 6×/3× so a small sheet covers the sky.
- **Billboard**: the Cookie Run trial-stage artwork composited
  into the plate in Photoshop (cookie base.psd, ~16 layers,
  green key).
- **Foreground character**: fan-art-style character image
  composited on green in Photoshop, green = mask colour; wired
  three times (two scales behind, one ghost in front).
- **Music**: the Cookie Run OST YouTube video, downloaded and
  dropped in as `cookie bitch.mp3`, bgvolume 255 (default max;
  his guide links a separate tutorial for lowering stage music).

## In-engine judgement — what playing checked that files don't

At least four test fights are visible (t≈1080, ≈1320, 2040,
≈2760 sheet frames, plus the finals). They catch, in order:
(1) the **black sky** — no back layer yet; (2) **floor contact
and reflection** — fighters stand on the promenade with the
[Reflection] 50 sheen reading under them; (3) the **mirror
seam** — the widened plate's symmetry is only visible in motion
framing; (4) the **foreground ghost** — whether the layerno=1
addalpha copy reads as atmosphere or as a smear over the fight.
None of these is decidable from the .def text.

## Claims list (for Pass 3 verification)

- **C1** File order of [BG] sections = draw order; later = in front.
- **C2** Floor delta is always 1,1 (low-res) / 2,2 (high-res);
  any other floor delta makes characters slide.
- **C3** Depth = delta rank: the further the element, the lower
  its delta.
- **C4** mask=1 keys the sprite's background colour; with no
  back element the screen is black.
- **C5** All elements share the floor anchor (start y=620 here);
  start must move when scalestart changes.
- **C6** layerno=1 draws above the fighters; layerno=0 behind.
- **C7** addalpha at alpha=100,120 is the recommended foreground
  transparency recipe.
- **C8** Rescale rule across resolutions: ×2 up, ×0.5 down.
- **C9** tile without velocity multiplies the sprite across the
  stage; tile+velocity wraps a scrolling element.
- **C10** zoffset is the ground line; + is down, − is up.
- **C11** (observed practice) A stage can ship with every delta
  at 1,1 when depth is carried by compositing, file order,
  scale, and layerno instead.
- **C12** (observed practice) The iteration loop is in-engine:
  wire → fight → fix; file inspection alone misses black-sky,
  seam, contact, and ghost defects.

## Disagreements (screen vs stated / plan)

- **DG1** — Doctrine (C3) says differentiate delta by depth;
  practice sets **every delta to 1,1** because the depth is
  baked into one composited plate. The plan's SHOULD-BE-SEEN
  expected per-layer parallax factors; the build has none.
- **DG2** — His comment says "i dont recommend change" the 620
  start; he then moves the stars to start=100,1300 — under his
  own stated exception (scalestart changed 1,1 → 6,3). Logged
  as consistent-under-exception, not a contradiction.
- **DG3** — Plan intake tagged the video "pixel art"; the plate
  is a painted background, palette-reduced to 8-bit on import.
- **DG4** — BACKGROUND spriteno reads 0,1 (t1815) then 1,1
  (t2580): the .sff was repacked between reads (2 → 20 sprites),
  renumbering groups. Not resolvable further from frames.

## UNREADABLEs (counted, never guessed) — 8

1. [Info] name/author lines — never on screen in sampled frames.
2. [Camera] section (startx/y, boundleft/right/high/low,
   tension, verticalfollow, floortension) — never shown.
3. [PlayerInfo] start positions/facings — never shown.
4. [Bound] boundleft/boundright/boundhigh/boundlow/screenleft —
   only screenright=30 read.
5. Action 1's 8 frames: star-twinkle variants vs billboard
   frames — the group-0 sprite contents were not opened at
   native res beyond indices 0–1; the [BG stars] name is the
   only evidence, and the bulbs/asset tabs cut the other way.
6. `xscale/yscale = .3.5` — malformed as written; intended value
   (3.5? .35?) unreadable.
7. `localcoord = 534,400` — first digit read as 5 at crop zoom;
   low certainty (could be 8).
8. `[BG Cookwitch solid] scalestart = 2,4` — captured mid-edit;
   the shipped value may differ.

Narration: no recoverable narration in the transcribed span
(loop census in MANIFEST.md); any spoken reasoning is
UNCONFIRMED-absent, and nothing above rests on it.
