# The Night School Study Protocol

Every video in the curriculum is run through the same five passes. A plan is
not done when the video has been watched — it is done when its techniques
exist in the estate as named, tested, clean-room capability.

## Pass 0 — Intake (before watching)

- Record the source: URL, video ID, title, creator, duration, upload date.
- State the SHOULD-BE-SEEN: what the title promises, written down *before*
  the first viewing, so the viewing is checked against an expectation
  instead of absorbed uncritically.
- Note the licence posture: a tutorial is studied, never redistributed.
  No video file, transcript, or frame enters any shipped artifact. What
  ships is the distilled technique, re-derived.

## Pass 1 — Timed observation

- Watch at 1x with a timestamp log open. Every technique gets a row:
  timestamp, what the hands did, what the screen showed, what the result
  was. Settings are copied numerically (values, node names, modifier
  stacks), not paraphrased.
- Mark surprises: anything that contradicts the SHOULD-BE-SEEN, anything
  the creator does that they do not explain, anything that fails on
  screen and gets fixed — the fixes are usually the real lesson.
- End with a claims list: each claim the video makes about its own
  technique, numbered, so Pass 3 can verify them one by one.

## Pass 2 — Distillation

- Rewrite the timestamp log as a technique sheet: inputs, steps,
  invariants, failure modes, and the *mechanism* — why it works, in terms
  of the underlying system (rig, solver, sampler, compositor), not the
  creator's UI clicks.
- Split every technique three ways:
  - **Adopt** — the mechanism is sound and estate-shaped as-is.
  - **Adapt** — the mechanism is sound; the estate's version differs
    (different DCC, deterministic instead of interactive, scripted
    instead of clicked).
  - **Reject** — recorded with the reason. A rejection with evidence is
    a deliverable, not a failure.

## Pass 3 — Clean-room rebuild

- Rebuild each Adopt/Adapt technique from the technique sheet alone,
  in the estate's own toolchain, without the video open. If the rebuild
  needs the video, the sheet was incomplete — fix the sheet, then
  rebuild.
- Claims from Pass 1 are the test list: each claim either reproduces or
  is marked REFUTED with the measured difference.
- The rebuild is deterministic where the estate is: seeded, scripted,
  re-runnable headlessly, with the run recorded (command, versions,
  hashes of outputs).

## Pass 4 — Application and gate

- Apply the rebuilt technique to one real estate target named in the
  plan (a Torogao scene, a Strobe build item, a keeper-art round, a jam
  game) and one SFW translation target where the plan names one.
- Gate it the estate way: expected-vs-seen benchmark written first,
  frames from the final artifact at viewing size, per-item PASS/FAIL.
  Numbers support the verdict; they never carry it alone.
- File the lesson: technique sheet + rebuild record + gate result land
  in this repo under `results/`, and a summary goes to the estate
  lesson store with its origin and content labels attached.

## Standing rules

- **Reference only.** Studied material informs; it is never copied into
  shipped work — no meshes, textures, motion data, prompts, or text
  lifted from a source video or its subject files.
- **Mechanism over mimicry.** If a step cannot be explained, it is not
  distilled yet.
- **Adult material stays in its lane.** NSFW findings land in NTRanch
  surfaces; only genuinely SFW translations cross to SFW work, and the
  crossing is named in the plan, never assumed.
- **One plan, one owner run.** Each plan is executed as a single study
  run with its own report; partial runs are recorded as partial.
