#!/usr/bin/env python3
# Generate (1) per-article SEO metadata+tags+image sheet, (2) branded SVG cover per article.
import re, os, html as _h

ROOT = "/home/user/SEO-web/content/vi"
COVERS = "/home/user/SEO-web/assets/covers"
os.makedirs(COVERS, exist_ok=True)

GROUPS = [
    ("Thiết bị đo lường", "#1f6feb", [
        "cam-bien-ap-suat-la-gi-cach-chon.md","cam-bien-nhiet-do.md","cam-bien-chenh-ap.md",
        "dong-ho-do-ap-suat-wika.md","dau-day-cam-bien-ap-suat-4-20ma.md"]),
    ("PLC", "#12a594", ["plc-mitsubishi-fx3u-la-gi.md"]),
    ("Thiết bị khó tìm & hàng ngừng sản xuất", "#d9862a", [
        "thiet-bi-cong-nghiep-kho-tim.md","linh-kien-tu-dong-hoa-ngung-san-xuat.md","tim-cam-bien-transmitter-kho-tim.md","thay-the-plc-module-doi-cu.md"]),
    ("Seneca — Hãng & danh mục", "#e5484d", [
        "seneca/seneca-viet-nam.md","seneca/bo-chuyen-doi-tin-hieu-seneca.md",
        "seneca/remote-io-seneca-z-pc.md","seneca/datalogger-rtu-seneca.md","seneca/gateway-modbus-seneca.md","seneca/dong-ho-do-dien-nang-seneca.md","seneca/bo-hien-thi-seneca.md"]),
    ("Seneca — Sản phẩm", "#e5484d", [
        "seneca/k109s-seneca.md","seneca/k109pt-seneca.md","seneca/k109lv-seneca.md","seneca/k121-seneca.md",
        "seneca/z109reg2-1-seneca.md",
        "seneca/k120-seneca.md","seneca/z109reg2-2-seneca.md","seneca/t121-seneca.md",
        "seneca/z-4rtd2-seneca.md","seneca/z-8ai-seneca.md","seneca/z-4ao-seneca.md","seneca/z-10-d-in-seneca.md",
        "seneca/z-logger3-seneca.md","seneca/z-gprs3-seneca.md","seneca/z-umts-seneca.md","seneca/z-lte-seneca.md",
        "seneca/z-key-seneca.md","seneca/r-key-lt-seneca.md","seneca/z-pass2-seneca.md","seneca/r-pass-seneca.md","seneca/s504-seneca.md","seneca/s604-seneca.md","seneca/s311a-seneca.md"]),
]

def field(name, text):
    m = re.search(name + r"[^:\n]*:\s*(.*)", text)
    return m.group(1).strip() if m else ""

def parse(path):
    raw = open(path, encoding="utf-8").read()
    mc = re.search(r"<!--(.*?)-->", raw, re.S)
    cmt = mc.group(1) if mc else ""
    after = raw[mc.end():] if mc else raw
    slug = field("URL SLUG", cmt).split()[0] if field("URL SLUG", cmt) else ""
    return dict(
        slug=slug, loai=field("LOẠI TRANG", cmt), tukhoa=field("TỪ KHÓA", cmt),
        title=field("TITLE TAG", after), meta=field("META", after), h1=field("H1", after))

def anchor(slug): return slug.strip("/").replace("/", "-") or "art"

def keywords(tukhoa):
    return [k.strip() for k in tukhoa.split("|") if k.strip()]

def focus_kw(kws): return kws[0] if kws else ""

def tags_for(d):
    t = []
    low = (d["tukhoa"] + " " + d["h1"]).lower()
    if "seneca" in low: t.append("Seneca")
    if "wika" in low: t.append("WIKA")
    if "mitsubishi" in low or "fx3u" in low or "fx5u" in low: t.append("Mitsubishi")
    cat = [
        ("cảm biến áp suất", "cam-bien-ap-suat" in d["slug"]),
        ("cảm biến nhiệt độ", "nhiet-do" in d["slug"]),
        ("cảm biến chênh áp", "chenh-ap" in d["slug"]),
        ("đồng hồ áp suất", "do-ap-suat-wika" in d["slug"]),
        ("đồng hồ đo điện năng", "dien-nang" in d["slug"] or d["slug"].strip("/") in ("s504-seneca","s604-seneca")),
        ("bộ hiển thị / panel meter", "hien-thi" in d["slug"] or "s311a" in d["slug"]),
        ("bộ chuyển đổi tín hiệu", "chuyen-doi" in d["slug"] or re.search(r"/(k109|k121|z109)", d["slug"])),
        ("PLC", "plc" in d["slug"]),
        ("remote I/O", "remote-io" in d["slug"]),
        ("datalogger", "datalogger" in d["slug"] or "logger" in d["slug"] or "gprs" in d["slug"]),
        ("gateway Modbus", "gateway" in d["slug"] or "key" in d["slug"]),
        ("thiết bị khó tìm", "kho-tim" in d["slug"]),
        ("hàng ngừng sản xuất", "ngung-san-xuat" in d["slug"] or "kho-tim" in d["slug"]),
        ("obsolete", "ngung-san-xuat" in d["slug"]),
    ]
    for name, cond in cat:
        if cond: t.append(name)
    # a couple model tags
    m = re.search(r"/((?:k1\d\d[a-z]*|z\d+reg[\d-]*|z-[a-z0-9]+|r-[a-z0-9-]+))/", d["slug"])
    if m: t.append(m.group(1).upper())
    t += ["thiết bị tự động hóa", "thiết bị đo lường"]
    # dedupe, keep order
    seen=set(); out=[]
    for x in t:
        if x.lower() not in seen:
            seen.add(x.lower()); out.append(x)
    return out[:8]

def img_brief(d):
    s = d["slug"]
    if any(k in s for k in ["k109","k121","z109","z-logger","z-gprs","z-umts","z-lte","z-key","r-key","z-pass2","r-pass","s504","s604","s311a"]):
        return "Ảnh sản phẩm thật trên nền trắng, thấy rõ mặt trước + tem model, gắn DIN rail. Nếu có, thêm 1 ảnh sơ đồ đấu nối."
    if "seneca-viet-nam" in s: return "Ảnh nhóm thiết bị Seneca (bộ chuyển đổi + module) hoặc logo Seneca + dải sản phẩm."
    if "chuyen-doi" in s: return "Ảnh vài model bộ chuyển đổi K109/Z109 gắn trên DIN rail."
    if "remote-io" in s: return "Ảnh cụm module Z-PC gắn thành hàng trên DIN rail."
    if "datalogger" in s: return "Ảnh datalogger Z-LOGGER3/Z-GPRS3 + ăng-ten (nếu có)."
    if "gateway" in s: return "Ảnh gateway Z-KEY/R-KEY-LT có cổng Ethernet + RS485."
    if "wika" in s: return "Ảnh đồng hồ áp suất WIKA (chân đồng & inox, loại có dầu) trên nền trắng."
    if "cam-bien-ap-suat" in s: return "Ảnh cảm biến áp suất thật + ảnh minh họa lắp trên đường ống."
    if "nhiet-do" in s: return "Ảnh Pt100/can nhiệt (que đo) + bảng phân biệt loại."
    if "chenh-ap" in s: return "Ảnh cảm biến chênh áp + sơ đồ đo lưu lượng/mức bồn kín."
    if "plc" in s: return "Ảnh PLC Mitsubishi FX3U/FX5U + bảng so sánh."
    if "dau-day" in s: return "Sơ đồ đấu dây 4-20mA (2/3/4 dây) rõ ràng, dễ nhìn."
    if "dien-nang" in s: return "Ảnh đồng hồ đo điện năng Seneca (S500/S604) gắn DIN rail."
    if "hien-thi" in s: return "Ảnh bộ hiển thị/panel meter gắn mặt tủ, màn LED."
    if "kho-tim" in s: return "Ảnh kho thiết bị/linh kiện đa dạng hoặc hình ghép nhiều model — gợi ý nguồn hàng sẵn."
    if "ngung-san-xuat" in s: return "Ảnh so sánh model cũ → model kế nhiệm, hoặc nhãn 'obsolete/EOL'."
    return "Ảnh minh họa liên quan chủ đề, nền sạch."

def alt_text(d):
    base = d["h1"].split("–")[0].split("?")[0].strip()
    if "seneca" in d["tukhoa"].lower() or "wika" in d["tukhoa"].lower():
        return f"{base} chính hãng"
    return base

# ---- cover SVG ----
def wrap(text, maxc):
    words = text.split(); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1 <= maxc: cur=(cur+" "+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines[:4]

def cover_svg(d, group, accent):
    title = d["h1"].split("–")[0].split("?")[0].strip()
    lines = wrap(title, 24)
    W,H = 1200,630
    y0 = 300 - (len(lines)-1)*34
    tspans = "".join(
        f'<text x="80" y="{y0+i*70}" font-family="Segoe UI,Roboto,Arial,sans-serif" '
        f'font-size="54" font-weight="700" fill="#f2f5fa">{_h.escape(l)}</text>'
        for i,l in enumerate(lines))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#111925"/><stop offset="1" stop-color="#1d2b3d"/>
 </linearGradient>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.04" stroke-width="1"/>
 </pattern>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect x="0" y="0" width="14" height="{H}" fill="{accent}"/>
<g opacity="0.5">
 <circle cx="1000" cy="315" r="150" fill="none" stroke="{accent}" stroke-width="2"/>
 <circle cx="1000" cy="315" r="110" fill="none" stroke="{accent}" stroke-width="1.5" stroke-opacity="0.6"/>
 <path d="M1000 315 L1000 205" stroke="{accent}" stroke-width="3"/>
 <circle cx="1000" cy="315" r="8" fill="{accent}"/>
 <path d="M820 470 q45 -60 90 0 t90 0 t90 0 t90 0" fill="none" stroke="{accent}" stroke-width="3" stroke-opacity="0.7"/>
</g>
<g font-family="Consolas,Menlo,monospace">
 <rect x="80" y="70" width="18" height="18" fill="{accent}"/>
 <text x="108" y="85" font-size="22" font-weight="700" letter-spacing="3" fill="#f2f5fa">HOANTRANTDH</text>
 <text x="80" y="150" font-size="16" letter-spacing="2" fill="{accent}">{_h.escape(group.upper())}</text>
</g>
{tspans}
<text x="80" y="560" font-family="Consolas,Menlo,monospace" font-size="20" fill="#8b97a6">hoantrantdh.com · thiết bị đo lường – tự động hoá</text>
</svg>'''

# ---- build ----
rows = []
n = 0
for gtitle, accent, files in GROUPS:
    rows.append(("__group__", gtitle, "", "", "", "", ""))
    for f in files:
        d = parse(os.path.join(ROOT, f)); a = anchor(d["slug"]); n += 1
        kws = keywords(d["tukhoa"])
        fname = a + ".jpg"
        # write cover
        open(os.path.join(COVERS, a + ".svg"), "w", encoding="utf-8").write(cover_svg(d, gtitle, accent))
        rows.append((d["slug"], d["h1"], focus_kw(kws), d["meta"],
                     ", ".join(tags_for(d)), fname, alt_text(d), img_brief(d)))

# metadata sheet
md = ["# Gói SEO cho từng bài: Focus keyword · Meta · Thẻ tag · Ảnh\n",
      "> Dùng khi đăng WordPress (Rank Math). Ảnh bìa thương hiệu đã tạo sẵn trong `assets/covers/<slug>.svg` — ",
      "dùng tạm làm **featured image**; trang sản phẩm nên thay bằng **ảnh sản phẩm thật** (theo cột \"Gợi ý ảnh\").",
      "Tên file ảnh & Alt text đã đặt sẵn chứa từ khoá.\n"]
for r in rows:
    if r[0] == "__group__":
        md.append(f"\n## {r[1]}\n")
        continue
    slug,h1,fkw,meta,tags,fname,alt,brief = r
    md.append(f"### {h1}")
    md.append(f"- **URL:** `{slug}`")
    md.append(f"- **Focus keyword:** {fkw}")
    md.append(f"- **Meta description:** {meta}")
    md.append(f"- **Thẻ (tags):** {tags}")
    md.append(f"- **Ảnh bìa có sẵn:** `assets/covers/{anchor(slug)}.svg`")
    md.append(f"- **Tên file ảnh nên đặt:** `{fname}`")
    md.append(f"- **Alt text ảnh:** {alt}")
    md.append(f"- **Gợi ý ảnh thật:** {brief}\n")

open("/home/user/SEO-web/research/seo-metadata-tags-hinh-anh.md", "w", encoding="utf-8").write("\n".join(md))
print("covers:", n, "-> assets/covers/*.svg ; sheet -> research/seo-metadata-tags-hinh-anh.md")
