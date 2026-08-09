#!/usr/bin/env python3
# Rasterize branded cover SVGs -> PNG 1200x630 so Facebook & social crawlers
# accept them as featured images (SVG is not supported; min 200x200 required).
import glob, os
from playwright.sync_api import sync_playwright

COVERS = "/home/user/SEO-web/assets/covers"
W, H = 1200, 630
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

svgs = sorted(glob.glob(os.path.join(COVERS, "*.svg")))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    for svg in svgs:
        png = svg[:-4] + ".png"
        page.goto("file://" + svg)
        page.screenshot(path=png, clip={"x": 0, "y": 0, "width": W, "height": H})
        print("->", os.path.basename(png))
    browser.close()
print("done:", len(svgs), "covers ->", W, "x", H, "PNG")
