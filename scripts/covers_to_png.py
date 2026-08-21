#!/usr/bin/env python3
# Rasterize cover SVGs (1200x630 OG/featured images) -> PNG for WordPress featured/OG images.
import re, os, subprocess, tempfile
from PIL import Image

SRC = "/home/user/SEO-web/assets/covers"
OUT = "/home/user/SEO-web/assets/png/covers"; os.makedirs(OUT, exist_ok=True)
BIN = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SCALE = 1          # 1200x630 is the standard OG/featured size
PAD = 200          # extra window height so headless Chromium doesn't clip when window==content

def size(svg):
    m = (re.search(r'width="(\d+)"\s+height="(\d+)"', svg)
         or re.search(r"viewBox=['\"]0 0 (\d+) (\d+)", svg))
    return (int(m.group(1)), int(m.group(2))) if m else (1200, 630)

done = 0
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
    out = os.path.join(OUT, f[:-4] + ".png")
    subprocess.run([BIN, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        f"--force-device-scale-factor={SCALE}", f"--window-size={W},{H+PAD}",
        f"--screenshot={out}", f"file://{wrap}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    os.unlink(wrap)
    if os.path.exists(out):
        Image.open(out).convert("RGB").crop((0, 0, W*SCALE, H*SCALE)).save(out, optimize=True)
        done += 1
print("converted", done, "cover PNGs ->", OUT)
