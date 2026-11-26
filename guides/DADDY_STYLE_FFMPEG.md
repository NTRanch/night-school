# Daddy Style FFmpeg — full guide

> This is the Ranch's house style guide for FFmpeg, adapted for adult game
> production — mosaic and censor passes, held-media study pipelines, loop
> finishing, and voice-track finishing for explicit scenes — and published
> as part of Night School.
> Every rule, gate, and number below is the rule the Ranch actually runs:
> the framing is adult production, the engineering is unchanged.

Version basis: **FFmpeg 8.1.2**: binary `ffmpeg` / `ffprobe` on the
hatch host, version string read by run on 2026-11-26 (`ffmpeg -version`
exited 0, first line `ffmpeg version 8.1.2`). Filter and muxer behaviour
cited below is the 8.x series behaviour; a filter whose exact semantics
no run in this programme has exercised is marked **U** at its point of
use and never carries load in a pipeline without a probe first.

This guide holds the NSFW-unique substance of Ranch media finishing. The
general converter discipline — named deterministic converters, no silent
re-encodes, exit-code honesty, golden tests — is the Tiger Style FFmpeg
guide's (`local-tiger-style-ffmpeg`), and this guide cross-references it
rather than restating it. Where the two disagree, the fence sections of
this guide win for adult work, because the fences are law, not style.

## Evidence legend

The same legend is used in every file of this package. The order below
carries meaning (strongest evidence first), so it is not alphabetical.

- **B**: exercised by run in the Ranch's own study and finishing
  pipelines, with the run's artefacts (hashes, frame counts, diff
  curves) recorded in the owning workdir. The point of use names the
  pipeline class, not a marketing claim.
- **S**: statically verified by reading a file, manifest, or record in
  the estate (a held-reference manifest, an INTAKE record, a scene
  spec). Nothing was executed. The file is named at each use.
- **D**: stated in the official FFmpeg documentation (ffmpeg-filters,
  ffmpeg-utils, the loudnorm filter documentation). Not confirmed by
  **B** or **S**.
- **U**: UNVERIFIED. No source settles it. A **U** claim never carries
  load in a pipeline without a probe run first.

## The fences (read first; they outrank every technique below)

ELI5: adult media work at the Ranch runs inside four fences that no
converter, however convenient, may cross. The fences are stated once
here and cited by name everywhere else in this guide.

- **Bloch lane law.** Sharing is governed by CONTENT label, not origin.
  NSFW-pure material — held references, study extractions, finished
  adult media, and any lesson learned from them — never reaches
  qompassai repos, callers, or datasets. SFW lessons may flow the other
  way. A converter script, preset, or profile written for adult work
  carries its content label in its name or header from birth; an
  unlabelled adult-work artefact is a defect, fixed before it moves.
- **Tier A.** Held media is measurement and reference only. It lives in
  held-reference trees, it never leaves those trees, and nothing derived
  from it ships: no frame, no clip, no loop, no audio snippet from held
  media appears in a Ranch product, dataset, README, or message. What
  ships is estate-original work informed by the measurements — frozen,
  hashed scene specs and the numbers in extraction records. Section
  "Held-media handling" operationalises this for the ffmpeg pipeline.
- **Audio silence.** No audio testing is audible on primo unless the
  Owner presses play himself or authorises specific playback. All QC in
  this guide is silent: waveforms, spectra, loudness numbers, and
  frame-level evidence stand in for listening, everywhere, without
  exception. Finished audio travels as files only, never autoplay.
- **Adults only.** Every character in any media this guide touches is
  an adult, verified at intake before any processing (the intake screen
  is fail-closed: an unresolved cast member stops the pipeline, it does
  not get processed "pending" anything). A converter never runs on
  unscreened media.

## Agent use

ELI5: FFmpeg has no remote control the Ranch trusts. Agents drive it the
way a shell script would: they build a command line from a named
converter, run it headless, and verify what came out — hashes, frame
counts, probe output — before anything is called finished. On the Ranch
that means a mosaic pass over a release cut, or the frame extraction for
a study census, is a command line and a verified file, never an
interactive session in a GUI editor.

### Broker and connector reality

- **No FFmpeg connector or MCP server exists.** The pipeline is the
  installed `ffmpeg` / `ffprobe` binaries, driven by named converter
  scripts checked into the owning workdir. A converter that exists only
  as a command in someone's shell history does not exist.
- **Primo vs hatch.** Study extraction runs where the media is: held
  media is processed on primo, inside its tree (see Tier A); estate-
  original finishing may run on either host, but the converter records
  which host and which binary version produced the output.

## Named converters (the spine, applied)

The Tiger Style rule stands unchanged: every transformation is a named,
deterministic converter — a script or a recorded command line with a
name, an input contract, an output contract, and a version. This guide
adds the adult-work consequences:

- A converter's name carries its content class: `censor-*`, `study-*`,
  `finish-*`, `loop-*`. A name that hides what the converter does to
  explicit material is renamed before it runs twice.
- No silent re-encodes. A pass that changes codec, colour space, frame
  rate, or sample rate says so in its contract and its output filename
  or sidecar record. "Just running it through ffmpeg" is not a
  converter.
- Every converter is bounded: named input size and duration limits,
  named frame-count ceilings for extraction, and a scratch directory it
  owns and cleans (see "Scratch discipline").
- Exit 0 is not success. Success is the output passing its verification:
  probe the result, count its frames, hash it. A zero exit with a
  missing sentinel or a short frame count is a failure.

## Mosaic and censor passes

Mosaic work at the Ranch runs in exactly two directions, and the guide
keeps them in separate sections because confusing them is the one
unforgivable error in this area: **applying** mosaic to estate-original
material for a release profile, and **studying** mosaic already present
in held material. There is no third direction.

### Applying mosaic — named converters only

A mosaic pass is a named converter (class `censor-*`) whose contract
states, before it runs:

- **Region.** The censored region as explicit geometry: either a fixed
  rectangle per shot, or a tracked region given as a keyframed rectangle
  series (frame range → x, y, w, h) recorded in the converter's input
  file. "Roughly over the middle" is not a region. Region tracking is
  authored data — a human or a gated tracker produces the keyframes, the
  converter consumes them; the converter never invents motion.
- **Cell size.** The mosaic cell size in output pixels, stated as a
  number in the profile (see below), not as a "strength" slider. Cell
  size is the compliance-relevant parameter, so it is the one the
  contract pins.
- **Chain.** The canonical chain is crop → scale down → scale up
  (nearest) → overlay: `crop` isolates the region, the downscale to the
  cell grid destroys the detail, the nearest-neighbour upscale restores
  the region's size without inventing any, and `overlay` composites it
  back at the stated coordinates. Any other chain (blur, pixelize
  filters, generative fill) is a different converter with its own name
  and its own review — blur in particular is not mosaic and never
  substitutes for it in a release profile.
- **Coverage verification.** The pass is verified, not eyeballed: sample
  frames at the region's keyframe extremes and at every shot cut inside
  the range, and confirm the region covers the target at each. A tracked
  region that lags its target at a fast-motion extreme is a failed pass,
  re-keyframed — never "close enough" on a release cut.

### Per-target profiles

Cell size, region policy, and output encoding are bundled per target in
a named profile, and the profile name travels with the output (see
Provenance):

- **`jp-release`** — the strict profile: the largest cell size the Ranch
  ships, applied to every region the target market's rules name, full
  coverage verification at every cut. This is the only profile whose
  output may leave the Ranch as a release.
- **`internal`** — the working profile for estate-original material in
  production: mosaic present where a scene's staging calls for it as a
  deliberate device, cell size stated per project. Internal-profile
  output never ships externally; re-profiling to `jp-release` is a new
  converter run, not a rename.
- **No profile means no pass.** A mosaic applied without a named profile
  is an unrecorded edit; the file is treated as unfinished until the
  pass is re-run under one.

### The reverse study case — mosaic in held material

Held material sometimes arrives already mosaic'd. The rule is short and
absolute:

- **Mosaic in held media is observable data.** It is measured like any
  other observable: presence, region, cell size in source pixels, the
  frames and beats it covers, how the staging composes around it. The
  extraction record states it plainly.
- **It is never "removed."** No de-censoring, de-mosaicing,
  reconstruction, inpainting, or generative guessing at what a mosaic
  covers is performed on held media, by any tool, at any fidelity. That
  work is out of scope for the Ranch's study pipelines, and this guide
  states so rather than leaving the gap ambiguous: the mosaic is part of
  the artefact as authored, and the census takes the artefact as it is.
- A scene whose grammar is partly under mosaic is extracted at the level
  the artefact supports (staging, beats, timing, the observable face and
  body channels) and the record names the occlusion honestly instead of
  papering over it.

## Held-media handling in the pipeline

Tier A, operationalised for media work. Every held item moves through
the same five steps; a step skipped is a pipeline defect.

1. **Intake hashing.** On arrival, before any processing: byte size and
   SHA-256 of the file as received, recorded in the item's INTAKE
   record alongside its source and screening outcome. Every later hash
   in the pipeline is checked against this one; a mismatch stops work —
   the file in hand is not the file that was screened.
2. **Held original vs study copy.** The original stays in the
   held-reference tree, untouched, forever. Processing runs on a study
   copy inside the item's workdir (or, on primo, inside the held tree's
   study area). Converters never write into the original's path, and no
   converter takes the original as an output target.
3. **Frame extraction bounds.** Extraction is bounded work: a named
   frame budget per item (a sampling interval and a total ceiling),
   stated in the extraction brief before the run. Full-density
   extraction is the exception and names its reason (loop closure
   measurement is the standing example — see below). Thumbnails are
   study-resolution (the Ranch standard is 1280 px on the long edge for
   cited frames); a frame cited in a record is kept at that resolution,
   not as a recompressed thumbnail of a thumbnail.
4. **Contact-sheet discipline.** Contact sheets are the screening and
   census instrument: a regular grid over the item's duration, built by
   a named converter, read by the screener, and kept with the study
   artefacts. A contact sheet is Tier A material — it lives and dies
   inside the workdir, and is never attached, uploaded, or shown outside
   it. Adult presentation is confirmed from the contact sheet before any
   extraction is commissioned; the sheet's verdict is recorded in the
   INTAKE.
5. **Scratch discipline.** Decodes, per-frame dumps, diff curves, and
   analysis scripts are scratch: they live in a scratch directory the
   job owns, and they are deleted at task end. What survives is the
   record (INTAKE, EXTRACTION, the frozen scene spec) and the cited
   frames the record names. Raw full-density frame dumps never survive
   "just in case" — they are re-derivable from the held original by the
   named converter, which is the whole point of naming it.

## Loop finishing for adult loops

Loops are the Ranch's signature deliverable shape — companion idles,
scene loops, preview loops — and adult loops get the same measurement
discipline as any other, plus a surface gate the SFW pipeline does not
need.

### Seamless micro-loop verification

A loop is called seamless only when the claim is measured:

- **Closure measurement.** Decode the loop at full density and compute
  the frame-difference curve (consecutive-frame mean absolute difference
  over a fixed luma proxy is the Ranch's standard instrument). A
  construction-seamless loop closes: the last frame's difference to the
  first is at the loop's own noise floor, and the recurrence of the
  start configuration is demonstrated at the stated lag, not asserted.
- **Cycle length in frames.** The loop's period is reported in frames
  (and seconds at the stated frame rate), derived from the diff curve's
  recurrence peaks. A loop with no single period is not forced into one
  — see envelope loops.
- **Per-performer phase.** In multi-body loops, each performer's region
  is measured against the shared cycle clock; phase offsets are reported
  in frames. Secondary motion (hair, soft-body) is expected to be
  period-locked without being phase-locked, and the record says which
  was observed.

### Envelope loops

Not every honest loop is construction-closed. An **envelope loop**
ramps its tempo or intensity (period breathing across the file) and
closes by phase placement — both ends parked at a velocity dead point,
so the near-closure reads clean. The finishing rules:

- Classify before finishing: seamless (measured closure) or envelope
  (measured near-closure + dead-point parking). The class is recorded
  in the asset's provenance; calling an envelope loop "seamless" is a
  false claim and is corrected in the record that carried it.
- An envelope loop is finished as authored — its tempo envelope is a
  keyed curve in the scene spec, not flattened to a constant period to
  make the loop tidier. Flattening is a re-authoring decision, not a
  finishing pass.

### GIF / APNG export discipline and surface gating

- **Export is a named converter** (`loop-export-*`): stated frame rate
  (a loop exported below its authored rate says so and why), stated
  palette discipline for GIF (generated palette, dithering named),
  stated dimensions. APNG is preferred where the surface supports it;
  GIF is the compatibility fallback, never the master.
- **The master is never the GIF.** The loop's master is the scene spec
  plus the full-rate render; GIF/APNG are preview derivatives.
- **Surface gating is a recorded decision, per asset.** Where an adult
  loop may be shown at all — which README, which dataset, which store
  page, which message — is a surface decision made and recorded per
  asset before export, not a default. The default for an adult loop is
  *shown nowhere* until a surface is named. SFW preview surfaces (public
  READMEs, public datasets) take only loops whose content passes those
  surfaces' own rules, and the gating record names the surface it
  cleared. A loop exported "for the README" without a gating record is
  unfinished.

## Audio in NSFW finishing

Adult work leans on voice — dialogue-driven scenes, VN-format pieces,
performed tracks — and its audio finishing runs under the audio silence
fence: **no stage of this section is verified by listening on primo.**
Verification is waveform, spectrum, loudness numbers, and timing
artefacts, all of which travel as files.

### Loudness normalisation for voice and dialogue

- Voice and dialogue tracks are normalised with the `loudnorm` filter
  as a **two-pass, measured** converter: first pass measures (integrated
  loudness, true peak, LRA) and prints its JSON; second pass applies
  with the measured values pinned in the command line. A single-pass
  loudnorm is a different, weaker converter and is named as such.
- The target is stated per deliverable class in the converter contract
  (integrated LUFS and true-peak ceiling as numbers), not left to the
  filter's defaults. Dialogue sits over any bed or music by the mix's
  own stated offset, measured from the stems — never by ear on primo.
- Music-only and effects-only tracks are not voice-normalised; each stem
  class has its own converter, and a mixed track is separated or the
  record says it was normalised as a mix and why.

### Silence-rule compliance in QC

- QC evidence for an audio pass is: the loudnorm measurement JSON, a
  waveform or spectrum render kept as an image artefact, and the
  `astats` / silence-detection numbers where the pass claims them.
  `silencedetect` output is the evidence for claimed pauses and gaps —
  cited by timestamp in the record.
- A pass whose only evidence is "sounded fine" has no evidence. It is
  re-run with instruments or it does not ship.
- Transcription for study and subtitle work runs on the audio file with
  the estate's transcription tooling, silently, and its output is
  checked against the burned-in text or script where one exists (see
  below) — a transcript that disagrees with the artefact's own text is
  flagged, and ASR hallucination over non-speech beds is a known failure
  mode the record must actively rule out, not a surprise.

### Subtitle and dialogue timing passes (VN-format pieces)

Visual-novel-format pieces — dialogue boxes, nameplates, burned-in
subtitles, player choice points — get a dedicated timing pass:

- **Dialogue extraction reconciles three sources**: the audio transcript,
  the burned-in subtitle/bubble text read from frames, and any script
  the artefact carries. Where they disagree, the record keeps all three
  readings and marks which governs; silent overwriting of one source by
  another is a defect.
- **Timing is frame-cited.** Each line's appearance and clearance is
  recorded against frame numbers at the piece's native frame rate, so
  the scene spec's dialogue track can be compiled deterministically.
  Choice points are first-class entries: the options shown, the dwell
  before selection, and which option the piece takes.
- **Re-timing for Ranch production** (dubbing, re-voicing, subtitle
  replacement on estate-original VN work) is a named converter whose
  contract states the timing source it follows — the original line
  timings, a new script's timings, or a stated hybrid — and whose output
  is verified by re-extracting the finished file's subtitle timings and
  diffing them against the contract.

## Provenance

Every finished file — release cut, loop, preview derivative, audio
track — carries its provenance, in a sidecar record or a manifest entry
that travels with it:

- **Source hash**: the SHA-256 of the exact input the finishing chain
  started from (for held-media study outputs, the intake hash; for
  estate-original work, the master render's hash).
- **Converter chain**: the named converters, in order, with their
  versions — enough to re-derive the output byte-for-byte or to prove
  why it cannot be re-derived.
- **Profile**: the named profile each pass ran under (`jp-release`,
  `internal`, the loop's surface-gating record, the loudness target).
- **Content label**: the bloch content label, from birth.

**Backup.** Finished NSFW media backs up under the generated-media rule:
uploaded to the Ranch's gated Hugging Face dataset immediately on
completion, labelled candidate, before any verdict; if upload is blocked
(agent locked, tooling down), the file is staged with a manifest and an
UPLOAD-PENDING flag and swept after the block clears. Held media and
anything derived from held media are **never** part of this backup — the
backup rule covers estate-original finished media only, and confusing
the two sets is a Tier A breach. Third-party study renders stay local,
always.

## Tests

Every converter in this guide is gated half validation / half
adversarial, in the family pattern:

- **Validation**: the golden cases — a known input through the named
  converter produces the recorded output hash, frame count, loudness
  numbers, or closure measurement.
- **Adversarial**: the cases built to break the contract — a mosaic
  region keyframed too loosely for a fast-motion extreme (must fail
  coverage verification, not pass quietly); a "loop" whose closure is
  97% there (must classify as envelope, not seamless); a held-media path
  offered as an output target (must refuse); a single-pass loudnorm
  presented under the two-pass converter's name (must fail the
  provenance check); an unscreened input (must stop at the fence).

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well,
with its reason.

- `loudnorm` linear-mode availability on arbitrary voice material.
  **U** with reason: the filter falls back to dynamic mode when the
  measured material cannot be normalised linearly (**D**, official
  documentation); which Ranch voice material triggers the fallback has
  not been settled by run, so a finishing contract that requires linear
  mode must probe its own material first.
- Palette-optimal GIF export settings for skin-tone-dominant loops.
  **U** with reason: palette generation and dithering choices are named
  in the export converter's contract, but no Ranch run has yet measured
  banding across the candidate settings on adult loop material; the
  first loop-export converter settles it by run and amends this guide.
- Tracked-region authoring tooling. **U** with reason: this guide
  requires keyframed region series as converter input and names them
  authored data; which tool authors them to Ranch standard (manual
  keyframing vs a gated tracker) is a project decision not yet taken,
  and no converter may assume one exists.
