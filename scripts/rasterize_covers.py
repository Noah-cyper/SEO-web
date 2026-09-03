#!/usr/bin/env python3
# Rasterize branded cover SVGs -> optimized JPG 1200x630 for WordPress featured
# images / OG images. A raster format (not SVG) is required by Facebook/Zalo
# crawlers; 1200x630 far exceeds the 200x200 minimum. JPG keeps files tiny
# (~40KB each vs ~170KB PNG) — these covers use gradients, so a quantized PNG
# still lands around 110KB. Renders through headless Chromium directly, so the
# only Python dependency is Pillow.
import os, re, subprocess, tempfile
from PIL import Image

SRC = "/home/user/SEO-web/assets/covers"
BIN = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
QUALITY = 82
PAD = 200          # extra window height so headless Chromium doesn't clip when window==content

def size(svg):
    m = (re.search(r'width="(\d+)"\s+height="(\d+)"', svg)
         or re.search(r"viewBox=['\"]0 0 (\d+) (\d+)", svg))
    return (int(m.group(1)), int(m.group(2))) if m else (1200, 630)

done = total = 0
for f in sorted(os.listdir(SRC)):
    if not f.endswith(".svg"):
        continue
    svg = open(os.path.join(SRC, f), encoding="utf-8").read()
    W, H = size(svg)
    html = (f"<!doctype html><html><head><meta charset='utf-8'></head>"
            f"<body style='margin:0;padding:0'>"
            f"<div style='width:{W}px;height:{H}px'>{svg}</div></body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as t:
        t.write(html); wrap = t.name
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as t:
        shot = t.name
    subprocess.run([BIN, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H+PAD}",
        f"--screenshot={shot}", f"file://{wrap}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    os.unlink(wrap)
    if os.path.getsize(shot) if os.path.exists(shot) else 0:
        jpg = os.path.join(SRC, f[:-4] + ".jpg")
        Image.open(shot).convert("RGB").crop((0, 0, W, H)).save(
            jpg, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        total += os.path.getsize(jpg); done += 1
    if os.path.exists(shot):
        os.unlink(shot)
print(f"covers: {done} -> {SRC}/*.jpg  (JPG q{QUALITY}, avg {total//done//1024 if done else 0}KB)")
