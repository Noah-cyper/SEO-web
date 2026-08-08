#!/usr/bin/env python3
# Insert the relevant technical diagram(s) into each article body (idempotent).
import os, re, glob

ROOT = "/home/user/SEO-web/content/vi"
MARK = "<!--DIAGRAM-->"

CAP = {
 "wiring-4-20ma-2wire":"Sơ đồ đấu dây 2 dây (loop-powered) 4–20mA",
 "wiring-4-20ma-3wire":"Sơ đồ đấu dây 3 dây 4–20mA",
 "pressure-types":"Ba loại áp suất: tương đối, tuyệt đối, chênh áp",
 "dp-measurement":"Ứng dụng cảm biến chênh áp: đo lưu lượng & mức bồn kín",
 "rtd-vs-tc":"So sánh Pt100 (RTD) và can nhiệt (thermocouple)",
 "signal-converter":"Chuyển đổi & cách ly tín hiệu (vd 4–20mA → 0–10V)",
 "signal-chain":"Chuỗi tín hiệu: cảm biến → bộ chuyển đổi → PLC/SCADA",
 "modbus-remote-io":"Thu thập tín hiệu từ xa qua Modbus RTU (remote I/O Z-PC)",
 "modbus-gateway":"Gateway chuyển đổi Modbus TCP ↔ RTU",
 "remote-monitoring":"Giám sát & cảnh báo từ xa qua RTU/datalogger (3G/4G)",
 "energy-monitoring":"Giám sát điện năng: tải → CT → đồng hồ đo → Modbus → EMS",
 "panel-indicator":"Bộ hiển thị: cảm biến → hiển thị LED → relay & ngõ ra analog",
 "obsolete-replacement":"Quy trình tìm hàng thay thế cho thiết bị ngừng sản xuất",
}

def diagrams_for(slug):
    s = slug
    if "dau-day" in s: return ["wiring-4-20ma-2wire","wiring-4-20ma-3wire"]
    if "chenh-ap" in s: return ["dp-measurement"]
    if "nhiet-do" in s: return ["rtd-vs-tc"]
    if "cam-bien-ap-suat" in s or "do-ap-suat-wika" in s: return ["pressure-types"]
    if any(k in s for k in ["k109","k121","k120","z109reg","t121","bo-chuyen-doi"]): return ["signal-converter"]
    if any(k in s for k in ["remote-io","z-4rtd2","z-8ai","z-4ao","z-10-d-in"]): return ["modbus-remote-io"]
    if any(k in s for k in ["datalogger","z-logger","z-gprs","z-umts","z-lte"]): return ["remote-monitoring"]
    if any(k in s for k in ["z-pass2","r-pass"]): return ["remote-monitoring"]
    if "gateway" in s or "z-key" in s or "r-key" in s: return ["modbus-gateway"]
    if "dien-nang" in s or re.search(r"/s60\d|/s50\d", s): return ["energy-monitoring"]
    if "hien-thi" in s or "s311a" in s: return ["panel-indicator"]
    if any(k in s for k in ["kho-tim","ngung-san-xuat","thay-the-plc","tim-cam-bien"]): return ["obsolete-replacement"]
    if "seneca-viet-nam" in s: return ["signal-chain"]
    if "plc-mitsubishi" in s: return ["signal-chain"]
    return []

def slug_of(raw):
    mc = re.search(r"<!--(.*?)-->", raw, re.S)
    cmt = mc.group(1) if mc else ""
    m = re.search(r"URL SLUG[^:\n]*:\s*(\S+)", cmt)
    return m.group(1) if m else ""

changed = 0
for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    base = os.path.basename(path)
    if base.startswith("_") or "/promo/" in path.replace("\\","/"):
        continue
    raw = open(path, encoding="utf-8").read()
    if MARK in raw:
        continue
    slug = slug_of(raw)
    dgs = diagrams_for(slug)
    if not dgs:
        continue
    block = MARK + "\n" + "\n".join(f"![{CAP[d]}](assets/diagrams/{d}.svg)" for d in dgs) + "\n"
    lines = raw.split("\n")
    # find end of first blockquote
    ins = None
    for i, ln in enumerate(lines):
        if ln.strip().startswith(">"):
            j = i
            while j < len(lines) and lines[j].strip().startswith(">"):
                j += 1
            ins = j
            break
    if ins is None:
        # fallback: after first paragraph following first '## '
        for i, ln in enumerate(lines):
            if ln.strip().startswith("## "):
                j = i + 1
                while j < len(lines) and lines[j].strip():
                    j += 1
                ins = j
                break
    if ins is None:
        continue
    lines.insert(ins, "\n" + block)
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    changed += 1

print("inserted diagrams into", changed, "articles")
