"""Build the PillowSquish asset .blend + demo measures + demo render.
Usage: blender -b -noaudio --threads 4 -Y --python build_pillow.py -- TAG OUTDIR
TAG distinguishes determinism runs (A/B); scene content is identical.
"""
import bpy
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pillow_core import DEMO, build_scene, measure, setup_render

argv = sys.argv[sys.argv.index('--') + 1:]
tag, outdir = argv[0], argv[1]
os.makedirs(outdir, exist_ok=True)

p = dict(DEMO)
cushion, collider, ng = build_scene(p)
cushion.color = (0.78, 0.74, 0.68, 1.0)
collider.color = (0.42, 0.48, 0.60, 1.0)

m = measure(cushion, collider, p)
m['tag'] = tag
m['blender'] = bpy.app.version_string
m['params'] = p
with open(os.path.join(outdir, 'measures_demo_%s.json' % tag), 'w') as f:
    json.dump(m, f, indent=1, sort_keys=True)

scene = bpy.context.scene
render_path = os.path.join(outdir, 'demo_%s.png' % tag)
setup_render(scene, render_path)
bpy.ops.render.render(write_still=True)

if tag == 'A':
    blend_path = os.path.join(outdir, 'pillow_asset.blend')
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print('NS23-BUILD-DONE tag=%s dent=%s hash=%s' % (tag, m['dent_depth'], m['vert_hash'][:16]))
