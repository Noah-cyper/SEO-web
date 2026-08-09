#!/usr/bin/env python3
# Rasterize all diagram SVGs to PNG (via prebuilt Chromium) for WordPress-safe embedding.
import re, os, subprocess, tempfile
SRC="/home/user/SEO-web/assets/diagrams"
OUT="/home/user/SEO-web/assets/png/diagrams"; os.makedirs(OUT,exist_ok=True)
BIN="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def size(svg):
    m=re.search(r"viewBox='0 0 ([\d.]+) ([\d.]+)'",svg) or re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',svg)
    return int(float(m.group(1))),int(float(m.group(2)))

done=0
for f in sorted(os.listdir(SRC)):
    if not f.endswith(".svg"): continue
    svg=open(os.path.join(SRC,f),encoding="utf-8").read()
    W,H=size(svg)
    html=f"<!doctype html><html><body style='margin:0;padding:0'><div style='width:{W}px'>{svg}</div></body></html>"
    with tempfile.NamedTemporaryFile("w",suffix=".html",delete=False,encoding="utf-8") as t:
        t.write(html); wrap=t.name
    out=os.path.join(OUT,f[:-4]+".png")
    subprocess.run([BIN,"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars",
        "--force-device-scale-factor=2",f"--window-size={W},{H}",f"--screenshot={out}",f"file://{wrap}"],
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=40)
    os.unlink(wrap)
    if os.path.exists(out): done+=1
print("converted",done,"PNGs ->",OUT)
