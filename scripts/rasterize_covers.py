#!/usr/bin/env python3
# Rasterize branded cover SVGs -> optimized JPG 1200x630 for social featured
# images. JPG (not SVG) is required by Facebook/Zalo/social crawlers; 1200x630
# far exceeds the 200x200 minimum. Progressive + optimized keeps files tiny
# (~35-40KB each vs ~230KB PNG).
import glob, io, os
from PIL import Image
from playwright.sync_api import sync_playwright

COVERS = "/home/user/SEO-web/assets/covers"
W, H = 1200, 630
QUALITY = 82
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

svgs = sorted(glob.glob(os.path.join(COVERS, "*.svg")))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    for svg in svgs:
        page.goto("file://" + svg)
        raw = page.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H})
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        jpg = svg[:-4] + ".jpg"
        im.save(jpg, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        print("->", os.path.basename(jpg), f"{os.path.getsize(jpg)//1024}KB")
    browser.close()
print("done:", len(svgs), "covers ->", W, "x", H, "JPG q%d" % QUALITY)
