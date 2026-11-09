#!/bin/bash
# run_main.sh - D-1 Stage 2 lactation: clips (twin builds), sensitivity
# strip, all-six applicability. Sequential, nice'd, thread-capped.
# Status: ~/.local/share/pax/nslac/out/status.log (append-only).
export OMP_NUM_THREADS=8
cd ~/.local/share/pax/nslac
mkdir -p out/clips
ST=out/status.log
SIM="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_sim.py --"
MEAS="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_measure.py --"
REND="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_render.py --"
ABC="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_abc.py --"
ABCP="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_abc_probe.py --"
HASH="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_pixelhash.py --"
MF="4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,36"
OFF=30
MRAD=1.2
DEL=1
RES=110

emitter_json() {  # $1 = run_record.json
  python3 -c "
import json,sys
r=json.load(open('$1'))
e=r['emitters']
print(json.dumps({'L':e['L']['centre'],'R':e['R']['centre'],'vel':r['velocity_coord']}))
"
}

clip() {  # $1 girl $2 m $3 mode $4 clipid $5 gated_csv $6 render_csv $7 frames
  local girl=$1 m=$2 mode=$3 id=$4 gated=$5 rf=$6 FR=$7
  echo "CLIP $id START $(date +%H:%M:%S)" >> $ST
  for t in A B; do
    local out=out/clips/${id}_${t}
    $SIM $girl $m $mode ${id}_${t} $out $FR 1.0 $OFF $MRAD $DEL $RES > $out.log 2>&1
    echo "CLIP $id sim$t rc=$? $(date +%H:%M:%S)" >> $ST
    local ej=$(emitter_json $out/run_record.json)
    local body=$(python3 -c "import json;print(json.load(open('$out/run_record.json'))['body_name'])")
    $MEAS $out/${id}_${t}_baked.blend $body $out/measurements.json $MF "$ej" > $out.measure.log 2>&1
    echo "CLIP $id meas$t rc=$?" >> $ST
  done
  $REND out/clips/${id}_A/${id}_A_baked.blend out/clips/${id}_A/renders $rf > out/clips/${id}_A.render.log 2>&1
  $REND out/clips/${id}_B/${id}_B_baked.blend out/clips/${id}_B/renders $gated > out/clips/${id}_B.render.log 2>&1
  echo "CLIP $id renders rc=$?" >> $ST
  (cd out/clips/${id}_A/renders && ls full_frame_*.png bust_frame_*.png) > /dev/null 2>&1
  $HASH $(for f in ${gated//,/ }; do printf "out/clips/${id}_A/renders/full_frame_%04d.png " $f; done) > out/clips/${id}_A/pixelhash.txt 2>&1
  $HASH $(for f in ${gated//,/ }; do printf "out/clips/${id}_B/renders/full_frame_%04d.png " $f; done) > out/clips/${id}_B/pixelhash.txt 2>&1
  local gf=$(echo $gated | cut -d, -f1)
  printf "A " >> out/clips/${id}_A/meshhash.txt
  sha256sum $(printf "out/clips/${id}_A/cache/mesh/fluid_mesh_%04d.bobj.gz" $gf) >> out/clips/${id}_A/meshhash.txt 2>&1
  printf "B " >> out/clips/${id}_B/meshhash.txt
  sha256sum $(printf "out/clips/${id}_B/cache/mesh/fluid_mesh_%04d.bobj.gz" $gf) >> out/clips/${id}_B/meshhash.txt 2>&1
  $ABC out/clips/${id}_A/${id}_A_baked.blend out/clips/${id}_A/${id}_fluidmesh.abc $FR > out/clips/${id}_A.abc.log 2>&1
  sha256sum out/clips/${id}_A/${id}_fluidmesh.abc > out/clips/${id}_A/abc.sha256 2>&1
  $ABCP out/clips/${id}_A/${id}_fluidmesh.abc $gated > out/clips/${id}_A/abc_probe.log 2>&1
  echo "CLIP $id DONE $(date +%H:%M:%S)" >> $ST
}

clip alma  1.0 drip   alma_m100_drip   12,24,36 8,14,20,26,32,38 40
clip alma  1.0 stream alma_m100_stream 14,20,28 8,14,20,26,32,36 36
clip alma  1.0 spray  alma_m100_spray  14,20,28 8,14,20,26,32,36 36
clip alma  1.5 stream alma_m150_stream 14,20,28 8,14,20,26,32,36 36
clip prima 1.0 stream prima_m100_stream 14,20,28 8,14,20,26,32,36 36
clip prima 1.0 drip   prima_m100_drip  12,24,36 8,14,20,26,32,38 40
clip prima 1.5 stream prima_m150_stream 14,20,28 8,14,20,26,32,36 36

# Sensitivity strip: Alma stream canon, viscosity x0.1 / x10 (single builds)
for vm in 0.1 10; do
  tag=$( [ $vm = 0.1 ] && echo lo || echo hi )
  out=out/sens_${tag}
  echo "SENS $tag START $(date +%H:%M:%S)" >> $ST
  nice -n 10 blender -b -Y -noaudio --python scripts/nslac_sim.py -- alma 1.0 stream sens_${tag} $out 28 $vm $OFF $MRAD $DEL $RES > $out.log 2>&1
  ej=$(emitter_json $out/run_record.json)
  body=$(python3 -c "import json;print(json.load(open('$out/run_record.json'))['body_name'])")
  $MEAS $out/sens_${tag}_baked.blend $body $out/measurements.json "8,14,22,28" "$ej" > $out.measure.log 2>&1
  $REND $out/sens_${tag}_baked.blend $out/renders "22" > $out.render.log 2>&1
  echo "SENS $tag DONE $(date +%H:%M:%S)" >> $ST
done

# Applicability: stream at canon, short bake, four remaining girls
for girl in yui sloane lux piper; do
  out=out/appl_${girl}
  echo "APPL $girl START $(date +%H:%M:%S)" >> $ST
  $SIM $girl 1.0 stream appl_${girl} $out 28 1.0 $OFF $MRAD $DEL $RES > $out.log 2>&1
  ej=$(emitter_json $out/run_record.json)
  body=$(python3 -c "import json;print(json.load(open('$out/run_record.json'))['body_name'])")
  $MEAS $out/appl_${girl}_baked.blend $body $out/measurements.json "4,6,8,10,12,14,16,18,20,22,24,26,28" "$ej" > $out.measure.log 2>&1
  $REND $out/appl_${girl}_baked.blend $out/renders "14,22" > $out.render.log 2>&1
  echo "APPL $girl DONE $(date +%H:%M:%S)" >> $ST
done
echo "ALL DONE $(date +%H:%M:%S)" >> $ST
