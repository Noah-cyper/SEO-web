#!/usr/bin/env python3
# Rasterize diagram SVGs -> PNG (via prebuilt Chromium) for uploading to WordPress Media.
import re, os, subprocess, tempfile
from PIL import Image

SCALE = 2
PAD = 160   # extra window height; headless Chromium clips when window==content height
SRC = "/home/user/SEO-web/assets/diagrams"
OUT = "/home/user/SEO-web/assets/png/diagrams"; os.makedirs(OUT, exist_ok=True)
BIN = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def size(svg):
    m = re.search(r"viewBox='0 0 ([\d.]+) ([\d.]+)'", svg) or re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    return int(float(m.group(1))), int(float(m.group(2)))

done = 0
for f in sorted(os.listdir(SRC)):
    if not f.endswith(".svg"):
        continue
    svg = open(os.path.join(SRC, f), encoding="utf-8").read()
    W, H = size(svg)
    # force explicit pixel size so headless Chromium doesn't collapse height:auto
    svg = svg.replace("width='100%' height='auto'", f"width='{W}' height='{H}'", 1)
    svg = svg.replace('width="100%" height="auto"', f'width="{W}" height="{H}"', 1)
    html = (f"<!doctype html><html><head><meta charset='utf-8'></head>"
            f"<body style='margin:0;padding:0'>"
            f"<div style='width:{W}px;height:{H}px'>{svg}</div></body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as t:
        t.write(html); wrap = t.name
    out = os.path.join(OUT, f[:-4] + ".png")
    subprocess.run([BIN, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        f"--force-device-scale-factor={SCALE}", f"--window-size={W},{H+PAD}",
        f"--screenshot={out}", f"file://{wrap}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=40)
    os.unlink(wrap)
    if os.path.exists(out):
        im = Image.open(out).convert("RGB")
        im.crop((0, 0, W*SCALE, H*SCALE)).save(out, optimize=True)  # trim the PAD headroom
        done += 1
print("converted", done, "PNGs ->", OUT)
