import re, subprocess, sys, time, os, hashlib, json
D = os.path.expanduser("~/.local/share/pax/night-school/plan-24/dl")
URL = "https://rule34video.com/video/3666838/tentacle-monster-wip-3/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def curl(url, out, referer=None):
    cmd = ["curl", "-s", "-A", UA, "-b", os.path.join(D, "cookies.txt"),
           "-c", os.path.join(D, "cookies.txt"), "-L", "--max-time", "300",
           "-o", out, "-w", "%{http_code} %{size_download}"]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout.strip()

deadline = time.time() + 21600
attempt = 0
page = None
while time.time() < deadline:
    attempt += 1
    out = curl(URL, os.path.join(D, "watch.html"))
    print(f"[{time.strftime('%H:%M:%S')}] attempt {attempt}: {out}", flush=True)
    p = os.path.join(D, "watch.html")
    if os.path.exists(p) and os.path.getsize(p) > 20000:
        txt = open(p, encoding="utf-8", errors="replace").read()
        if "get_file" in txt or "video_url" in txt:
            page = txt
            break
    time.sleep(60)

if page is None:
    print("CAPTURE-BLOCKED: watch page never served full content", flush=True)
    sys.exit(3)

open(os.path.join(D, "watch-full.html"), "w").write(page)
cands = re.findall(r"video_url\d*\s*:\s*'(https?://[^']+)'", page)
cands += re.findall(r"(https?://[^\"' ]*get_file[^\"' ]*?\.mp4[^\"' ]*)", page)
seen = []
for c in cands:
    c = c.replace("\\/", "/")
    if c not in seen:
        seen.append(c)
print("candidates:", len(seen), flush=True)
for c in seen:
    print("  ", c, flush=True)
if not seen:
    print("CAPTURE-BLOCKED: no video_url in page", flush=True)
    sys.exit(4)

best = None
for pat in ("1080", "720", "480"):
    for c in seen:
        if pat in c:
            best = c
            break
    if best:
        break
best = best or seen[0]
open(os.path.join(D, "video-url.txt"), "w").write(best + "\n")
out = curl(best, os.path.join(D, "plan24-source.mp4"), referer=URL)
print("download:", out, flush=True)
f = os.path.join(D, "plan24-source.mp4")
h = hashlib.sha256()
with open(f, "rb") as fh:
    for chunk in iter(lambda: fh.read(1 << 20), b""):
        h.update(chunk)
info = {"size": os.path.getsize(f), "sha256": h.hexdigest(), "url_used": best}
r = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json",
                    "-show_format", "-show_streams", f],
                   capture_output=True, text=True)
info["ffprobe"] = json.loads(r.stdout) if r.stdout else {}
json.dump(info, open(os.path.join(D, "capture-info.json"), "w"), indent=1)
print(json.dumps({k: info[k] for k in ("size", "sha256")}), flush=True)
print("CAPTURE-OK", flush=True)
