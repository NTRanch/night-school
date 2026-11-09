# NS13 beauty-pass recreation — scripted Blender scene + compositor (Night School Plan 13, Pass 3)
# Clean-room rebuild from TECHNIQUE.md alone. Blender 5.2.3, headless, deterministic.
# API notes (probed on primo, Blender 5.2.3, /tmp/probe2..7.py, 2026-11-06):
#   compositor tree = scene.compositing_node_group (a CompositorNodeTree data-block);
#   Mix node = ShaderNodeMix (data_type RGBA: Factor=in[0], A=in[6], B=in[7], Result=out[2]);
#   Denoise node defaults ARE the video's settings (HDR True, Prefilter Accurate,
#   Quality Follow Scene); Switch node in[0]=Switch bool, in[1]=Off, in[2]=On;
#   File Output = CompositorNodeOutputFile with .directory + file_output_items.new("RGBA", name);
#   Composite = NodeGroupOutput behind an interface socket named "Image".
# Usage:
#   blender -b -Y --factory-startup --offline-mode -noaudio -t 2 --python-exit-code 1 \
#     --python build_recreate.py -- --outdir <dir> --render-denoise off|on
# Scene: synthetic multi-component still — diffuse ground/cube, glossy metal sphere,
# transmission sphere, emissive panel + emissive backplate (the background enters via
# the Emission pass, exactly as in the source scene), a volume fog cube.
# Recipe (TECHNIQUE.md):
#   Diff  = (DiffDir + DiffInd) * DiffCol
#   Gloss = (GlossDir + GlossInd) * GlossCol
#   Trans = (TransDir + TransInd) * TransCol
#   Rest  = VolDir + VolInd + Emission        (dropped to Emission-only if the
#                                              Volume sockets are unavailable; recorded)
#   Recreated = Diff + Gloss + Trans + Rest
#   Denoised  = Denoise(Recreated, Albedo=Denoising Albedo, Normal=Denoising Normal)
#   Variant   = same recipe with Gloss x1.6 and Emission x2.0, then the same Denoise
import faulthandler; faulthandler.enable()
import bpy, json, math, os, sys
from mathutils import Vector

SAMPLES = 64
RES_X, RES_Y = 384, 288
GLOSS_BOOST = 1.6
EMIT_BOOST = 2.0

def look_at(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def mat_principled(name, **kw):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    for k, v in kw.items():
        bsdf.inputs[k].default_value = v
    return m

def add_obj(name, mtype, loc, mat=None, scale=(1, 1, 1), rot=(0, 0, 0)):
    if mtype == 'CUBE':
        bpy.ops.mesh.primitive_cube_add(location=loc)
    elif mtype == 'SPHERE':
        bpy.ops.mesh.primitive_uv_sphere_add(location=loc, radius=1.0, segments=48, ring_count=24)
    elif mtype == 'PLANE':
        bpy.ops.mesh.primitive_plane_add(location=loc)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = scale
    ob.rotation_euler = rot
    if mat:
        ob.data.materials.append(mat)
    return ob

def mix_node(nt, name, op, loc):
    n = nt.nodes.new("ShaderNodeMix")
    n.name = name
    n.label = name
    n.data_type = 'RGBA'
    n.blend_type = op            # 'ADD' or 'MULTIPLY'
    n.clamp_factor = True        # the video's nodes: Clamp Factor on, Factor 1.000
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
    render_denoise = args.get("--render-denoise", "off") == "on"
    os.makedirs(outdir, exist_ok=True)

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    vl = bpy.context.view_layer

    # ------------------------------------------------------------ scene
    world = bpy.data.worlds.new("NS13World")
    scene.world = world
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.0, 0.0, 0.0, 1.0)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.0

    m_diff_red = mat_principled("DiffRed", **{"Base Color": (0.55, 0.10, 0.07, 1.0), "Roughness": 0.9})
    m_diff_teal = mat_principled("DiffTeal", **{"Base Color": (0.05, 0.35, 0.40, 1.0), "Roughness": 0.85})
    m_gloss = mat_principled("GlossMetal", **{"Base Color": (0.90, 0.86, 0.80, 1.0),
                                              "Metallic": 0.9, "Roughness": 0.15})
    m_trans = mat_principled("TransGlass", **{"Base Color": (0.95, 0.97, 1.0, 1.0),
                                              "Roughness": 0.06, "Transmission Weight": 1.0})
    m_emit = mat_principled("EmitWarm", **{"Base Color": (0.0, 0.0, 0.0, 1.0),
                                           "Emission Color": (1.0, 0.55, 0.20, 1.0),
                                           "Emission Strength": 6.0})
    m_back = mat_principled("Backplate", **{"Base Color": (0.0, 0.0, 0.0, 1.0),
                                            "Emission Color": (0.25, 0.45, 0.65, 1.0),
                                            "Emission Strength": 2.5})
    m_vol = bpy.data.materials.new("FogVolume")
    m_vol.use_nodes = True
    ntv = m_vol.node_tree
    for n in list(ntv.nodes):
        ntv.nodes.remove(n)
    outv = ntv.nodes.new("ShaderNodeOutputMaterial")
    vol = ntv.nodes.new("ShaderNodeVolumePrincipled")
    vol.inputs["Density"].default_value = 0.25
    vol.inputs["Color"].default_value = (0.7, 0.8, 0.9, 1.0)
    ntv.links.new(vol.outputs["Volume"], outv.inputs["Volume"])

    add_obj("Ground", 'PLANE', (0, 0, 0), m_diff_red, scale=(6, 6, 1))
    add_obj("TealCube", 'CUBE', (-1.3, 0.3, 0.55), m_diff_teal, scale=(0.55, 0.55, 0.55), rot=(0, 0, 0.5))
    add_obj("GlossSphere", 'SPHERE', (0.15, -0.2, 0.75), m_gloss, scale=(0.75, 0.75, 0.75))
    add_obj("TransSphere", 'SPHERE', (1.35, 0.45, 0.5), m_trans, scale=(0.5, 0.5, 0.5))
    add_obj("EmitPanel", 'PLANE', (-0.4, -1.6, 1.15), m_emit, scale=(0.7, 0.45, 1), rot=(math.radians(90), 0, 0))
    add_obj("Backplate", 'PLANE', (0.4, 2.6, 1.5), m_back, scale=(7, 3.5, 1), rot=(math.radians(90), 0, 0))
    add_obj("FogCube", 'CUBE', (0.9, -0.9, 0.8), m_vol, scale=(0.85, 0.85, 0.85))

    def add_light(name, ltype, energy, color, loc, target=(0, 0, 0.6), **kw):
        data = bpy.data.lights.new(name, ltype)
        data.energy = energy
        data.color = color
        for k, v in kw.items():
            setattr(data, k, v)
        ob = bpy.data.objects.new(name, data)
        ob.location = loc
        scene.collection.objects.link(ob)
        look_at(ob, target)
        return ob

    add_light("Key", 'AREA', 900.0, (1.0, 0.95, 0.9), (-2.5, -3.0, 3.2), shape='RECTANGLE', size=1.2, size_y=1.8)
    add_light("Fill", 'POINT', 60.0, (0.8, 0.9, 1.0), (2.6, -2.2, 1.6), shadow_soft_size=0.4)
    add_light("Rim", 'SPOT', 1200.0, (1.0, 0.6, 0.85), (1.8, 2.2, 2.6),
              spot_size=math.radians(50.0), spot_blend=0.3)

    cam_data = bpy.data.cameras.new("Cam")
    cam_data.lens = 42.0
    cam = bpy.data.objects.new("Cam", cam_data)
    cam.location = (0.3, -5.2, 1.7)
    scene.collection.objects.link(cam)
    look_at(cam, (0.1, 0.2, 0.65))
    scene.camera = cam

    # ------------------------------------------------------------ passes (source video's set)
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
    vl.use_pass_ambient_occlusion = True   # socket present in the source tree, unwired there
    vl.cycles.use_pass_volume_direct = True
    vl.cycles.use_pass_volume_indirect = True
    vl.cycles.denoising_store_passes = True   # Denoising Normal / Albedo / Depth
    vl.update_render_passes()   # required in 5.2: materialises the Noisy Image /
    # Denoising / Volume sockets on the Render Layers node (probed, probe13)
    # NOTE: no subsurface passes, no environment pass — the source tree has neither
    # socket; SSS folds into the diffuse passes and the background is emissive geometry.

    # ------------------------------------------------------------ render settings
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = SAMPLES
    scene.cycles.use_adaptive_sampling = False
    scene.cycles.use_denoising = render_denoise
    if render_denoise:
        scene.cycles.denoiser = 'OPENIMAGEDENOISE'
    scene.cycles.device = 'CPU'
    scene.cycles.seed = 0
    scene.cycles.use_animated_seed = False
    scene.render.resolution_x = RES_X
    scene.render.resolution_y = RES_Y
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.render.image_settings.file_format = 'OPEN_EXR'
    scene.render.image_settings.media_type = 'MULTI_LAYER_IMAGE'  # 5.2: replaces the old OPEN_EXR_MULTILAYER format enum (probed)
    scene.render.image_settings.exr_codec = 'ZIP'
    scene.render.image_settings.color_depth = '32'
    scene.render.filepath = os.path.join(outdir, "passes_multilayer.exr")
    scene.render.use_compositing = True

    # ------------------------------------------------------------ compositor
    vl.update_render_passes()   # again, now that the engine is CYCLES (the first
    # call ran under the factory Eevee engine and did not materialise Cycles sockets)
    nt = bpy.data.node_groups.new("Compositor Nodes", "CompositorNodeTree")
    scene.compositing_node_group = nt
    rl = nt.nodes.new("CompositorNodeRLayers")
    rl.location = (-1200, 0)
    rl_sockets = [s.name for s in rl.outputs]
    print("RL SOCKETS:", rl_sockets)
    print("RL LAYER:", getattr(rl, "layer", None), "scene vl:", vl.name)
    have_volume = "Volume Direct" in rl_sockets and "Volume Indirect" in rl_sockets

    gout = nt.nodes.new("NodeGroupOutput")
    gout.location = (950, 200)
    nt.interface.new_socket(name="Image", in_out='OUTPUT', socket_type='NodeSocketColor')
    viewer = nt.nodes.new("CompositorNodeViewer")
    viewer.location = (950, 40)

    def S(name):
        return rl.outputs[name]

    def fileout(name, fname, x, y, fmt=None):
        fo = nt.nodes.new("CompositorNodeOutputFile")
        fo.name = name
        fo.location = (x, y)
        fo.directory = outdir
        fo.file_name = ""
        fo.format.media_type = 'IMAGE'   # 5.2: node format defaults to MULTI_LAYER_IMAGE (probed)
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
    if "Noisy Image" in rl_sockets:
        # socket exists only when render denoising is enabled (probed: it is the
        # render denoiser's input image); a reference output, not part of the recipe
        fo_noisy = fileout("FO_Noisy", "noisy_image", 500, 620)
        nt.links.new(S("Noisy Image"), fo_noisy.inputs[0])

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
        if have_volume:
            r1 = mix_node(nt, f"Rest{tag}_Add1", 'ADD', (x, y))
            nt.links.new(S("Volume Direct"), A(r1))
            nt.links.new(S("Volume Indirect"), B(r1))
            first = OUT(r1)
        else:
            first = None
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

    # --- matched recreation
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
        # defaults probed = the video's settings: HDR True, Prefilter Accurate, Quality Follow Scene
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

    # Switch A/B exactly as the source: Off = renderer Image, On = denoised recreation
    sw = nt.nodes.new("CompositorNodeSwitch")
    sw.name = "AB_Switch"
    sw.location = (620, 200)
    sw.inputs[0].default_value = True
    nt.links.new(S("Image"), sw.inputs[1])
    nt.links.new(dn.outputs[0], sw.inputs[2])
    nt.links.new(sw.outputs[0], gout.inputs[0])
    nt.links.new(sw.outputs[0], viewer.inputs[0])

    # --- graded variant: Gloss x1.6, Emission x2.0 — impossible from this render
    #     without the passes (the renderer alone cannot re-weight components)
    gloss_v = component("GlossV", "Glossy Direct", "Glossy Indirect", "Glossy Color", -850, -850, boost=GLOSS_BOOST)
    rest_v = rest_chain(-850, -1140, emit_boost=EMIT_BOOST, tag="V")
    variant = sum_chain("Var", [diff, gloss_v, trans, rest_v], -250, -850)
    dn_v = denoise("Denoise_Var", variant, 250, -950)
    fo_var = fileout("FO_Variant", "variant", 500, -850)
    nt.links.new(dn_v.outputs[0], fo_var.inputs[0])
    fo_var_png = fileout("FO_VariantPNG", "variant_png", 500, -990, fmt='PNG')
    nt.links.new(dn_v.outputs[0], fo_var_png.inputs[0])

    inv = {"render_denoise": render_denoise, "samples": SAMPLES,
           "res": [RES_X, RES_Y], "gloss_boost": GLOSS_BOOST,
           "emit_boost": EMIT_BOOST, "rl_sockets": rl_sockets,
           "have_volume": have_volume,
           "nodes": [{"name": n.name, "type": n.bl_idname,
                      "blend_type": getattr(n, "blend_type", None)} for n in nt.nodes]}
    with open(os.path.join(outdir, "node-inventory.json"), "w") as f:
        json.dump(inv, f, indent=1)

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(outdir, "ns13-beauty.blend"))
    bpy.ops.render.render(write_still=True)
    print("OK ns13_recreate render_denoise=", render_denoise, "have_volume=", have_volume)
    print("OUTDIR FILES:", sorted(os.listdir(outdir)))

main()
