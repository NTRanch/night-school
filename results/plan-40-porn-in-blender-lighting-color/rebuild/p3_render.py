# NS40 Pass 3 — render driver. One blend in, one PNG out (+ the blend's
# compositor EXR pass contract fires when compositing is on).
# Modes: probe = 540x960 @128 samples (measurement + determinism);
#        beauty = 1080x1920 @384 samples (the judged pair; a matched middle
#        pair for BOTH sides, documented in PASS3-REBUILD.md — the control
#        template's own pair is 0.0100/4096 and the variant's is 0.0100/128;
#        the beauty pair holds threshold + cap constant so light+grade are
#        the only variables, exactly as Plan 17's retune precedent).
# --raw disables compositing (the variant's ungraded plate).
# CPU + seed 0 (Plan 02 deterministic route).
import faulthandler; faulthandler.enable()
import bpy, sys

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    mode = args["--mode"]; outname = args["--outname"]
    raw = "--raw" in argv
    scene = bpy.context.scene
    assert scene.render.engine == "CYCLES"
    scene.cycles.device = 'CPU'
    scene.cycles.seed = 0
    scene.cycles.use_animated_seed = False
    scene.cycles.use_adaptive_sampling = True
    scene.cycles.adaptive_threshold = 0.0100
    scene.cycles.use_denoising = True
    if mode == "probe":
        scene.cycles.samples = 128
        scene.render.resolution_x = 540
        scene.render.resolution_y = 960
    elif mode == "beauty":
        scene.cycles.samples = 384
        scene.render.resolution_x = 1080
        scene.render.resolution_y = 1920
    else:
        raise SystemExit(f"bad mode {mode}")
    scene.render.resolution_percentage = 100
    scene.render.use_compositing = not raw
    import os
    scene.render.filepath = os.path.join(args["--outdir"], outname)
    scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still=True)
    print(f"OK render {mode} {outname} raw={raw}")

main()
