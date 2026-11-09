# NS13 Pass 4 application — the beauty-pass recreation applied to a COPY of the
# Plan 02 template (template-nswfw.blend). Plan 11's AOV variant had not landed
# when this ran, so per the brief's dependency rule the recreation is built on
# the Plan 02 template directly (deviation recorded in PASS3-REBUILD.md /
# PASS4-APPLICATION.md). Plan 02 / Plan 11 files are never modified: the input
# is a byte copy in this run's own dir.
# The loaded scene is reconfigured ONLY in the copy: NS13 pass set enabled,
# render reduced for a gated measurement run (64 samples, 25% of 1080x1920,
# render denoise OFF), compositor = the NS13 recipe + the same graded variant
# (Gloss x1.6, Emission x2.0). Outputs mirror build_recreate.py.
# Test of record: Prima's skin carries Subsurface Weight 0.20 (Plan 02 sheet)
# and the recipe enables NO subsurface passes — whether the recreation still
# matches the renderer beauty measures where the SSS contribution lands.
import faulthandler; faulthandler.enable()
import bpy, json, os, sys

SAMPLES = 64
RES_PCT = 25
GLOSS_BOOST = 1.6
EMIT_BOOST = 2.0

def mix_node(nt, name, op, loc):
    n = nt.nodes.new("ShaderNodeMix")
    n.name = name
    n.label = name
    n.data_type = 'RGBA'
    n.blend_type = op
    n.clamp_factor = True
    n.clamp_result = False
    n.inputs[0].default_value = 1.0
    n.location = loc
    return n

def A(n):
    return n.inputs[6]

def B(n):
    return n.inputs[7]

def OUT(n):
    return n.outputs[2]

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    outdir = os.path.abspath(args.get("--outdir", "."))
    os.makedirs(outdir, exist_ok=True)

    scene = bpy.context.scene
    vl = bpy.context.view_layer
    assert scene.render.engine == 'CYCLES', scene.render.engine

    vl.use_pass_combined = True
    vl.use_pass_diffuse_direct = True
    vl.use_pass_diffuse_indirect = True
    vl.use_pass_diffuse_color = True
    vl.use_pass_glossy_direct = True
    vl.use_pass_glossy_indirect = True
    vl.use_pass_glossy_color = True
    vl.use_pass_transmission_direct = True
    vl.use_pass_transmission_indirect = True
    vl.use_pass_transmission_color = True
    vl.use_pass_emit = True
    vl.use_pass_ambient_occlusion = True
    vl.cycles.use_pass_volume_direct = True
    vl.cycles.use_pass_volume_indirect = True
    vl.cycles.denoising_store_passes = True

    scene.cycles.samples = SAMPLES
    scene.cycles.use_adaptive_sampling = False
    scene.cycles.use_denoising = False
    scene.cycles.device = 'CPU'
    scene.cycles.seed = 0
    scene.cycles.use_animated_seed = False
    scene.render.resolution_percentage = RES_PCT
    scene.render.image_settings.file_format = 'OPEN_EXR'
    scene.render.image_settings.media_type = 'MULTI_LAYER_IMAGE'
    scene.render.image_settings.exr_codec = 'ZIP'
    scene.render.image_settings.color_depth = '32'
    scene.render.filepath = os.path.join(outdir, "passes_multilayer.exr")
    scene.render.use_compositing = True
    vl.update_render_passes()

    nt = bpy.data.node_groups.new("Compositor Nodes", "CompositorNodeTree")
    scene.compositing_node_group = nt
    rl = nt.nodes.new("CompositorNodeRLayers")
    rl.location = (-1200, 0)
    rl_sockets = [s.name for s in rl.outputs]
    print("RL SOCKETS:", rl_sockets)
    have_volume = "Volume Direct" in rl_sockets and "Volume Indirect" in rl_sockets
    gout = nt.nodes.new("NodeGroupOutput")
    gout.location = (950, 200)
    nt.interface.new_socket(name="Image", in_out='OUTPUT', socket_type='NodeSocketColor')

    def S(name):
        return rl.outputs[name]

    def fileout(name, fname, x, y, fmt=None):
        fo = nt.nodes.new("CompositorNodeOutputFile")
        fo.name = name
        fo.location = (x, y)
        fo.directory = outdir
        fo.file_name = ""
        fo.format.media_type = 'IMAGE'
        fo.format.file_format = 'OPEN_EXR'
        fo.format.exr_codec = 'ZIP'
        fo.format.color_depth = '32'
        item = fo.file_output_items.new("RGBA", fname)
        if fmt == 'PNG':
            item.override_node_format = True
            item.format.file_format = 'PNG'
            item.format.color_depth = '8'
        return fo

    fo_beauty = fileout("FO_Beauty", "beauty_image", 500, 760)
    nt.links.new(S("Image"), fo_beauty.inputs[0])

    def component(prefix, direct, indirect, color, x, y, boost=1.0):
        add = mix_node(nt, f"{prefix}_Add", 'ADD', (x, y))
        nt.links.new(S(direct), A(add))
        nt.links.new(S(indirect), B(add))
        mul = mix_node(nt, f"{prefix}_Mul", 'MULTIPLY', (x + 260, y))
        nt.links.new(OUT(add), A(mul))
        nt.links.new(S(color), B(mul))
        out = OUT(mul)
        if boost != 1.0:
            b = mix_node(nt, f"{prefix}_Boost", 'MULTIPLY', (x + 520, y))
            nt.links.new(out, A(b))
            B(b).default_value = (boost, boost, boost, 1.0)
            out = OUT(b)
        return out

    def sum_chain(name, branches, x, y):
        cur = branches[0]
        for i, br in enumerate(branches[1:]):
            a = mix_node(nt, f"{name}_Sum{i+1}", 'ADD', (x + i * 60, y - i * 150))
            nt.links.new(cur, A(a))
            nt.links.new(br, B(a))
            cur = OUT(a)
        return cur

    def rest_chain(x, y, emit_boost=1.0, tag=""):
        first = None
        if have_volume:
            r1 = mix_node(nt, f"Rest{tag}_Add1", 'ADD', (x, y))
            nt.links.new(S("Volume Direct"), A(r1))
            nt.links.new(S("Volume Indirect"), B(r1))
            first = OUT(r1)
        emit_sock = S("Emission")
        if emit_boost != 1.0:
            eb = mix_node(nt, f"Emit{tag}_Boost", 'MULTIPLY', (x, y - 190))
            nt.links.new(emit_sock, A(eb))
            B(eb).default_value = (emit_boost, emit_boost, emit_boost, 1.0)
            emit_sock = OUT(eb)
        if first is None:
            return emit_sock
        r2 = mix_node(nt, f"Rest{tag}_Add2", 'ADD', (x + 260, y))
        nt.links.new(first, A(r2))
        nt.links.new(emit_sock, B(r2))
        return OUT(r2)

    diff = component("Diff", "Diffuse Direct", "Diffuse Indirect", "Diffuse Color", -850, 350)
    gloss = component("Gloss", "Glossy Direct", "Glossy Indirect", "Glossy Color", -850, 60)
    trans = component("Trans", "Transmission Direct", "Transmission Indirect", "Transmission Color", -850, -230)
    rest = rest_chain(-850, -520)
    recreated = sum_chain("Rec", [diff, gloss, trans, rest], -250, 350)
    fo_rec = fileout("FO_Recreated", "recreated", 500, 460)
    nt.links.new(recreated, fo_rec.inputs[0])

    def denoise(name, image_sock, x, y):
        dn = nt.nodes.new("CompositorNodeDenoise")
        dn.name = name
        dn.location = (x, y)
        dn.inputs["HDR"].default_value = True
        nt.links.new(image_sock, dn.inputs["Image"])
        nt.links.new(S("Denoising Albedo"), dn.inputs["Albedo"])
        nt.links.new(S("Denoising Normal"), dn.inputs["Normal"])
        return dn

    dn = denoise("Denoise_Rec", recreated, 250, 250)
    fo_dn = fileout("FO_RecreatedDenoised", "recreated_denoised", 500, 300)
    nt.links.new(dn.outputs[0], fo_dn.inputs[0])
    fo_rec_png = fileout("FO_RecreatedPNG", "recreated_denoised_png", 500, 160, fmt='PNG')
    nt.links.new(dn.outputs[0], fo_rec_png.inputs[0])
    nt.links.new(dn.outputs[0], gout.inputs[0])

    gloss_v = component("GlossV", "Glossy Direct", "Glossy Indirect", "Glossy Color", -850, -850, boost=GLOSS_BOOST)
    rest_v = rest_chain(-850, -1140, emit_boost=EMIT_BOOST, tag="V")
    variant = sum_chain("Var", [diff, gloss_v, trans, rest_v], -250, -850)
    dn_v = denoise("Denoise_Var", variant, 250, -950)
    fo_var = fileout("FO_Variant", "variant", 500, -850)
    nt.links.new(dn_v.outputs[0], fo_var.inputs[0])
    fo_var_png = fileout("FO_VariantPNG", "variant_png", 500, -990, fmt='PNG')
    nt.links.new(dn_v.outputs[0], fo_var_png.inputs[0])

    inv = {"input": "copy of Plan 02 template-nswfw.blend",
           "samples": SAMPLES, "res_pct": RES_PCT,
           "res": [scene.render.resolution_x, scene.render.resolution_y],
           "gloss_boost": GLOSS_BOOST, "emit_boost": EMIT_BOOST,
           "rl_sockets": rl_sockets, "have_volume": have_volume}
    with open(os.path.join(outdir, "node-inventory.json"), "w") as f:
        json.dump(inv, f, indent=1)

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(outdir, "ns13-template-aov.blend"))
    bpy.ops.render.render(write_still=True)
    print("OK ns13_template_apply have_volume=", have_volume)
    print("OUTDIR FILES:", sorted(os.listdir(outdir)))

main()
