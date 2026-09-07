#!/usr/bin/env python3
# Rasterize branded cover SVGs -> PNG 1200x630, song song với bản JPG.
#
# JPG (rasterize_covers.py) là bản mặc định cho featured/OG image vì nhẹ hơn ~3,5 lần.
# PNG ở đây dành cho nơi cần ảnh không mất dữ liệu: in ấn, sàn/CMS chỉ nhận PNG,
# hoặc khi cần chỉnh sửa lại ảnh mà không muốn tích luỹ nhiễu nén.
#
# Ảnh bìa dùng dải gradient nên KHÔNG quantize: 256 màu chỉ nhẹ hơn ~17% mà lại
# gây banding trên nền chuyển màu. Giữ PNG đủ màu.
#
# Render qua headless Chromium, phụ thuộc Python duy nhất là Pillow.
import os, re, subprocess, tempfile
from PIL import Image

SRC = "/home/user/SEO-web/assets/covers"
BIN = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PAD = 200          # thêm chiều cao cửa sổ để Chromium headless không cắt ảnh

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
    if os.path.exists(shot) and os.path.getsize(shot):
        png = os.path.join(SRC, f[:-4] + ".png")
        Image.open(shot).convert("RGB").crop((0, 0, W, H)).save(png, "PNG", optimize=True)
        total += os.path.getsize(png); done += 1
    if os.path.exists(shot):
        os.unlink(shot)
print(f"covers: {done} -> {SRC}/*.png  (PNG 1200x630, trung bình {total//done//1024 if done else 0}KB, "
      f"tổng {total//1024//1024}MB)")
