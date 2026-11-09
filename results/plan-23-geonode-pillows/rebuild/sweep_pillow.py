"""Parameter sweep for PillowSquish. Each step rebuilds the group
from the parameter vector alone, evaluates, measures, classifies.
Renders: first + last step of each axis, plus every CLIFF step.
Usage: blender -b -noaudio --threads 4 -Y --python sweep_pillow.py -- OUTDIR
"""
import bpy
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pillow_core import DEMO, build_scene, measure, setup_render, classify

outdir = sys.argv[sys.argv.index('--') + 1]
rdir = os.path.join(outdir, 'sweep_renders')
os.makedirs(rdir, exist_ok=True)

AXES = [
    ('A_from_min', 'from_min', [-4.0, -3.0, -2.1, -1.6, -1.0, -0.5, 0.0, 0.5]),
    ('B_from_max', 'from_max', [0.2, 0.5, 1.0, 2.0, 4.0]),
    ('C_to_window', None, [(0.5, 0.9), (0.0, 1.0), (0.8, 0.9), (0.0, 0.3), (1.2, 1.6)]),
    ('D_ramp_start', 'ramp_start', [0.0, 0.3, 0.714, 0.9, 0.99]),
    ('E_press', 'press', [-0.10, 0.0, 0.06, 0.15, 0.30]),
    ('F_seg', 'seg', [4, 8, 16, 32]),
    ('G_thick', 'thick', [0.05, 0.15, 0.25, 0.50]),
    # H: inversion hunt — steepen BOTH windows together (the
    # through-thickness lift gradient is their product). Added
    # after round 1 found no inversion anywhere on axes A-G:
    # C(0,1) reached thick_ratio 0.13 without crossing.
    ('H_inversion_hunt', 'FULL', [
        dict(from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0),
        dict(from_min=-0.5, from_max=0.5, to_min=0.0, to_max=1.0),
        dict(from_min=-0.2, from_max=0.2, to_min=0.0, to_max=1.0),
    ]),
]

rows = []
base_faces = None
for axis_name, key, values in AXES:
    for idx, val in enumerate(values):
        p = dict(DEMO)
        label = str(val)
        if key is None:  # C: (to_min, to_max) pair
            p['to_min'], p['to_max'] = val
            label = '%.2f-%.2f' % val
        elif key == 'FULL':  # H: full parameter override dict
            p.update(val)
            label = 'w%.1f_to0-1' % (val['from_max'] - val['from_min'])
        else:
            p[key] = val
        cushion, collider, ng = build_scene(p)
        cushion.color = (0.78, 0.74, 0.68, 1.0)
        collider.color = (0.42, 0.48, 0.60, 1.0)
        m = measure(cushion, collider, p)
        if base_faces is None:
            base_faces = m['faces']
        cls = classify(m, m['faces'])
        render = (idx == 0 or idx == len(values) - 1 or cls == 'CLIFF')
        rname = ''
        if render:
            rname = 'sweep_%s_%d_%s.png' % (axis_name, idx, label.replace('.', 'p').replace('-', 'm').replace(',', '_'))
            setup_render(bpy.context.scene, os.path.join(rdir, rname))
            bpy.ops.render.render(write_still=True)
        row = dict(axis=axis_name, step=idx, value=label, params=p,
                   measures=m, verdict=cls, render=rname)
        rows.append(row)
        print('NS23-SWEEP %s[%d]=%s -> %s dent=%s inv=%s nan=%s pen=%s' % (
            axis_name, idx, label, cls, m['dent_depth'], m['inversion'],
            m['nan'], m['penetration_verts']), flush=True)

with open(os.path.join(outdir, 'sweep.json'), 'w') as f:
    json.dump(rows, f, indent=1, sort_keys=True)
print('NS23-SWEEP-DONE rows=%d' % len(rows))
