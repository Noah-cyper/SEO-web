#!/usr/bin/env python3
# Insert 3 images per article: representative / principle / application. Idempotent.
import os, re, glob
ROOT="/home/user/SEO-web/content/vi"

# Renepoly (BESS · microgrid): 5 ảnh/bài — rep · prin · spec · app · comp
RENEPOLY_IMG = {
 "renepoly":                        ("rep-microgrid","prin-bess-charge","spec-bess-stack","app-factory-bess","compare-cabinet-container"),
 "he-thong-luu-tru-nang-luong-bess-la-gi":("rep-bess-cabinet","prin-bess-charge","spec-bess-stack","app-factory-bess","compare-lfp-nmc"),
 "tu-luu-tru-nang-luong-renepoly":  ("rep-bess-cabinet","prin-bess-charge","spec-cabinet-layout","app-factory-bess","compare-cabinet-container"),
 "container-luu-tru-nang-luong-renepoly":("rep-bess-container","prin-bess-charge","spec-container-layout","app-island-microgrid","compare-cabinet-container"),
 "ems-quan-ly-nang-luong-renepoly": ("rep-ems-renepoly","prin-microgrid-switch","spec-ems-arch","app-ems-dashboard","compare-ongrid-offgrid"),
 "pcs-bo-chuyen-doi-cong-suat-renepoly":("rep-pcs-renepoly","prin-pcs","spec-cabinet-layout","app-factory-bess","compare-ongrid-offgrid"),
 "pin-lfp-battery-rack-renepoly":   ("rep-battery-rack","prin-bms","spec-bess-stack","app-factory-bess","compare-lfp-nmc"),
 "egs215-renepoly":                 ("rep-bess-cabinet","prin-liquid-cooling","spec-cabinet-layout","app-factory-bess","compare-cabinet-container"),
 "es215-renepoly":                  ("rep-bess-cabinet","prin-bess-charge","spec-cabinet-layout","app-factory-bess","compare-cooling"),
 "es232-renepoly":                  ("rep-bess-cabinet","prin-liquid-cooling","spec-cabinet-layout","app-ev-charging","compare-cabinet-container"),
 "microgrid-la-gi":                 ("rep-microgrid","prin-microgrid-switch","spec-ems-arch","app-island-microgrid","compare-ongrid-offgrid"),
 "peak-shaving-cat-dinh-tai":       ("rep-bess-cabinet","prin-peakshaving","spec-sizing","app-factory-bess","compare-roi-bess"),
 "dien-mat-troi-ket-hop-luu-tru":   ("rep-microgrid","prin-solar-bess","spec-bess-stack","app-solar-storage-roof","compare-ongrid-offgrid"),
 "bess-cho-nha-may-khu-cong-nghiep":("rep-bess-cabinet","prin-peakshaving","spec-sizing","app-factory-bess","compare-roi-bess"),
 "bess-cho-tram-sac-xe-dien":       ("rep-bess-cabinet","prin-peakshaving","spec-sizing","app-ev-charging","compare-roi-bess"),
 "pin-lfp-lifepo4-luu-tru-nang-luong":("rep-lfp-cell","prin-bms","spec-bess-stack","app-factory-bess","compare-lfp-nmc"),
 "lam-mat-chat-long-cho-bess":      ("rep-bess-cabinet","prin-liquid-cooling","spec-cabinet-layout","app-factory-bess","compare-cooling"),
 "bms-he-thong-quan-ly-pin":        ("rep-battery-rack","prin-bms","spec-bess-stack","app-ems-dashboard","compare-lfp-nmc"),
 "an-toan-pccc-he-thong-bess":      ("rep-bess-safety","prin-bms","spec-safety-layers","app-factory-bess","compare-bess-may-phat"),
 "tinh-cong-suat-dung-luong-bess":  ("rep-bess-cabinet","prin-peakshaving","spec-sizing","app-factory-bess","compare-roi-bess"),
}

# Biến tần (VFD): 5 ảnh/bài — chuỗi bài 5 tầng (nền tảng → chọn → lắp → cài → lỗi)
VFD_IMG = {
 # Tầng 1 — Nền tảng
 "bien-tan-la-gi":            ("rep-bien-tan","prin-vfd-pwm","spec-vfd-parts","app-vfd-bom","comp-vfd-saobam"),
 "cau-tao-bien-tan":          ("rep-bien-tan","prin-vfd-pwm","spec-vfd-parts","app-vfd-bangtai","comp-vf-vector"),
 "nguyen-ly-hoat-dong-bien-tan":("rep-bien-tan","prin-vfd-pwm","spec-vfd-parts","app-vfd-quat","comp-vf-vector"),
 "phan-loai-bien-tan":        ("rep-bien-tan","prin-vf-ratio","spec-vfd-parts","app-vfd-bom","comp-vfd-tai"),
 "bien-tan-tiet-kiem-dien":   ("rep-bien-tan-bom","prin-affinity","spec-vfd-sizing","app-vfd-tietkiem","comp-vfd-saobam"),
 "bien-tan-va-dong-co-3-pha": ("rep-bien-tan","prin-vf-ratio","spec-vfd-dauday","app-vfd-bangtai","comp-vf-vector"),
 # Tầng 2 — Chọn mua
 "cach-chon-bien-tan":        ("rep-bien-tan","prin-vf-ratio","spec-vfd-sizing","app-vfd-bom","comp-vfd-tai"),
 "chon-cong-suat-bien-tan":   ("rep-bien-tan","prin-affinity","spec-vfd-sizing","app-vfd-bangtai","comp-vfd-tai"),
 "bien-tan-1-pha-ra-3-pha":   ("rep-bien-tan-1p3p","prin-vfd-pwm","spec-vfd-dauday","app-vfd-bom","comp-vfd-saobam"),
 "so-sanh-cac-hang-bien-tan": ("rep-bien-tan","prin-vf-ratio","spec-vfd-sizing","app-vfd-plc","comp-vfd-hang"),
 "phan-biet-bien-tan-that-gia":("rep-bien-tan","prin-vfd-loi","spec-vfd-baotri","app-vfd-suachua","comp-vfd-that-gia"),
 # Tầng 3 — Lắp đặt & đấu nối
 "so-do-dau-day-bien-tan":    ("rep-bien-tan","prin-vfd-pwm","spec-vfd-dauday","app-vfd-bom","comp-vfd-saobam"),
 "dau-dieu-khien-bien-tan":   ("rep-bien-tan","prin-vfd-pwm","spec-vfd-dieukhien","app-vfd-plc","comp-vf-vector"),
 "chon-cap-aptomat-cho-bien-tan":("rep-tu-dien-bien-tan","prin-vfd-pwm","spec-vfd-dauday","app-vfd-bangtai","comp-vfd-tai"),
 "lap-bien-tan-trong-tu-dien":("rep-tu-dien-bien-tan","prin-vfd-nhieu","spec-vfd-emc","app-vfd-plc","comp-vfd-hang"),
 "chong-nhieu-emc-cho-bien-tan":("rep-tu-dien-bien-tan","prin-vfd-nhieu","spec-vfd-emc","app-vfd-plc","comp-vfd-hang"),
 "cuon-khang-loc-nhieu-bien-tan":("rep-tu-dien-bien-tan","prin-vfd-nhieu","spec-vfd-emc","app-vfd-bom","comp-vfd-tai"),
 # Tầng 4 — Cài đặt & điều khiển
 "cai-dat-thong-so-bien-tan": ("rep-bien-tan","prin-vf-ratio","spec-vfd-thongso","app-vfd-bom","comp-vf-vector"),
 "cai-tang-giam-toc-bien-tan":("rep-bien-tan","prin-vf-ratio","spec-vfd-thongso","app-vfd-bangtai","comp-vfd-tai"),
 "che-do-dieu-khien-vf-vector":("rep-bien-tan","prin-vf-ratio","spec-vfd-thongso","app-vfd-bangtai","comp-vf-vector"),
 "dieu-khien-bien-tan-bang-plc":("rep-bien-tan","prin-vfd-pwm","spec-vfd-dieukhien","app-vfd-plc","comp-vfd-hang"),
 "dieu-khien-pid-bang-bien-tan":("rep-bien-tan-bom","prin-vfd-pid","spec-vfd-dieukhien","app-vfd-bom","comp-vfd-tai"),
 "bien-tan-cho-bom-nuoc":     ("rep-bien-tan-bom","prin-vfd-pid","spec-vfd-sizing","app-vfd-bom","comp-vfd-tai"),
 "bien-tan-cho-quat-hut":     ("rep-bien-tan","prin-affinity","spec-vfd-sizing","app-vfd-quat","comp-vfd-tai"),
 # Tầng 5 — Lỗi & bảo trì
 "loi-bien-tan-thuong-gap":   ("rep-bien-tan-loi","prin-vfd-loi","spec-vfd-baotri","app-vfd-suachua","comp-sua-thay"),
 "loi-qua-dong-bien-tan":     ("rep-bien-tan-loi","prin-vfd-loi","spec-vfd-thongso","app-vfd-suachua","comp-vfd-tai"),
 "loi-qua-ap-thap-ap-bien-tan":("rep-bien-tan-loi","prin-vfd-loi","spec-vfd-dauday","app-vfd-suachua","comp-vfd-tai"),
 "loi-qua-nhiet-qua-tai-bien-tan":("rep-bien-tan-loi","prin-vfd-loi","spec-vfd-baotri","app-vfd-suachua","comp-vfd-tai"),
 "bao-tri-bien-tan-dinh-ky":  ("rep-tu-dien-bien-tan","prin-vfd-loi","spec-vfd-baotri","app-vfd-suachua","comp-sua-thay"),
 "sua-hay-thay-bien-tan":     ("rep-bien-tan-loi","prin-vfd-loi","spec-vfd-baotri","app-vfd-suachua","comp-sua-thay"),
}

# Biến tần — mở rộng tầng 6–9 (20 bài): 5 ảnh/bài
VFD2_IMG = {
 "bien-tan-cho-bang-tai":       ("rep-vfd-bangtai","prin-vf-ratio","spec-vfd-sizing","app-vfd-bangtai2","comp-vfd-tai"),
 "bien-tan-cho-may-nen-khi":    ("rep-vfd-nenkhi","prin-vfd-pid","spec-vfd-sizing","app-vfd-nenkhi","comp-vfd-tai"),
 "bien-tan-cho-cau-truc-palang":("rep-vfd-cautruc","prin-vfd-regen","spec-vfd-sto","app-vfd-cautruc","comp-vfd-regen"),
 "bien-tan-cho-may-tron-may-nghien":("rep-vfd-tron","prin-vf-ratio","spec-vfd-thongso","app-vfd-tron","comp-vf-vector"),
 "bien-tan-trong-hvac":         ("rep-vfd-hvac","prin-affinity","spec-vfd-sizing","app-vfd-hvac","comp-vfd-tai"),
 "bien-tan-hoan-nang-luong":    ("rep-vfd-cautruc","prin-vfd-regen","spec-vfd-afe","app-vfd-cautruc","comp-vfd-regen"),
 "dong-bo-nhieu-bien-tan":      ("rep-vfd-bangtai","prin-master-slave","spec-vfd-fieldbus","app-vfd-bangtai2","comp-fieldbus"),
 "bien-tan-cho-dong-co-nam-cham-vinh-cuu":("rep-bien-tan","prin-pmsm","spec-vfd-thongso","app-vfd-tietkiem","comp-motor-im-pm"),
 "safe-torque-off-bien-tan":    ("rep-tu-dien-bien-tan","prin-vfd-sto","spec-vfd-sto","app-vfd-cautruc","comp-loto-sto"),
 "bien-tan-mang-truyen-thong-cong-nghiep":("rep-bien-tan","prin-fieldbus","spec-vfd-fieldbus","app-vfd-plc","comp-fieldbus"),
 "song-hai-thd-bien-tan":       ("rep-tu-dien-bien-tan","prin-song-hai","spec-vfd-emc","app-vfd-plc","comp-loc-song-hai"),
 "he-so-cong-suat-tu-bu-bien-tan":("rep-tu-dien-bien-tan","prin-cosphi","spec-vfd-emc","app-vfd-tietkiem","comp-loc-song-hai"),
 "bien-tan-chay-tren-may-phat-dien":("rep-bien-tan","prin-may-phat","spec-vfd-sizing","app-vfd-nenkhi","comp-vfd-tai"),
 "dong-ro-noi-dat-bien-tan":    ("rep-tu-dien-bien-tan","prin-dong-ro","spec-vfd-emc","app-vfd-suachua","comp-vfd-hang"),
 "bien-tan-va-khoi-dong-mem":   ("rep-bien-tan","prin-vf-ratio","spec-vfd-sizing","app-vfd-bangtai2","comp-vfd-khoidongmem"),
 "lap-bien-tan-cho-may-dang-chay":("rep-vfd-retrofit","prin-affinity","spec-retrofit","app-vfd-retrofit","comp-vfd-roi"),
 "nghiem-thu-chay-thu-bien-tan":("rep-tu-dien-bien-tan","prin-vfd-pwm","spec-nghiem-thu","app-vfd-retrofit","comp-vfd-hang"),
 "an-toan-dien-voi-bien-tan":   ("rep-tu-dien-bien-tan","prin-dong-ro","spec-vfd-sto","app-vfd-suachua","comp-loto-sto"),
 "giam-sat-bien-tan-tu-xa":     ("rep-bien-tan","prin-fieldbus","spec-giam-sat","app-vfd-monitor","comp-fieldbus"),
 "danh-gia-dau-tu-hoan-von-bien-tan":("rep-bien-tan-bom","prin-affinity","spec-vfd-sizing","app-vfd-tietkiem","comp-vfd-roi"),
}

def pick(slug):
    s=slug
    key = slug.strip("/").replace("/","-")
    if key in RENEPOLY_IMG: return RENEPOLY_IMG[key]
    if key in VFD_IMG: return VFD_IMG[key]
    if key in VFD2_IMG: return VFD2_IMG[key]
    # ei3 (IIoT bảo mật) — xử lý trước để không đụng rule chung (gateway, hien-thi…)
    if "ei3" in s or any(k in s for k in ["amphion","zethus","portara","connectedai"]):
        if "amphion" in s or "gateway-ket-noi" in s: return ("rep-gateway-ei3","prin-outbound","app-fleet")
        if "portara" in s: return ("rep-gateway-ei3","prin-outbound","app-remote-service")
        if "zethus" in s: return ("rep-gateway-virtual","prin-outbound","app-fleet")
        if "connectedai" in s or "lifecycle" in s: return ("rep-analytics","prin-ai","app-oee")
        if "remote-service" in s or "zero-trust" in s: return ("rep-security","prin-zerotrust","app-remote-service")
        if "nen-tang-bao-ve-cps" in s: return ("rep-platform","prin-zerotrust","app-fleet")
        if "thu-thap-du-lieu" in s: return ("rep-platform","prin-ai","app-fleet")
        if s.strip("/") == "ei3": return ("rep-platform","prin-outbound","app-fleet")
        return ("rep-app","prin-ai","app-oee")   # monitor/oee/downtime/quality/recipe/sustain/ung-dung
    # Flowline (đo mức) — xử lý trước để không đụng các rule chung (cam-bien-ap-suat, hien-thi…)
    if "flowline" in s:
        if "echotouch" in s: return ("rep-uslevel","prin-ultrasonic","app-hazard")
        if "echospan" in s: return ("rep-loop-level","prin-ultrasonic","app-level")
        if "echopulse" in s: return ("rep-gwr","prin-radar","app-level")
        if "echowave" in s or "radar" in s: return ("rep-radar","prin-radar","app-level")
        if "thuy-tinh" in s or "deltaspan" in s: return ("rep-submersible","prin-hydrostatic","app-level")
        if any(k in s for k in ["dieu-khien-hien-thi","leveltouch","dataloop"]): return ("rep-controller","prin-switch","app-control")
        if "cong-tac" in s: return ("rep-switch","prin-switch","app-switch")
        return ("rep-level","prin-ultrasonic","app-level")  # echopod / hub / cảm biến siêu âm
    if "dau-day" in s: return ("wiring-4-20ma-2wire","wiring-4-20ma-3wire","signal-chain")
    if "do-ap-suat-wika" in s: return ("rep-gauge","prin-bourdon","app-gauge")
    if "chenh-ap" in s: return ("rep-dp","prin-dp","dp-measurement")
    if "nhiet-do" in s: return ("rep-temp","rtd-vs-tc","app-temp")
    if "cam-bien-ap-suat" in s: return ("rep-pressure","prin-pressure","app-pressure")
    if "plc-mitsubishi" in s: return ("rep-plc","prin-plc","app-plc")
    if any(k in s for k in ["k109","k121","k120","z109reg","t121","bo-chuyen-doi"]): return ("rep-converter","signal-converter","signal-chain")
    if any(k in s for k in ["remote-io","z-4rtd2","z-8ai","z-4ao","z-10-d-in"]): return ("rep-remoteio","modbus-remote-io","app-remoteio")
    if any(k in s for k in ["z-pass2","r-pass"]): return ("rep-iot","remote-monitoring","app-iot")
    if any(k in s for k in ["datalogger","z-logger","z-gprs","z-umts","z-lte"]): return ("rep-datalogger","remote-monitoring","app-datalogger")
    if "gateway" in s or "z-key" in s or "r-key" in s: return ("rep-gateway","modbus-gateway","app-gateway")
    if "dien-nang" in s or re.search(r"/s50\d|/s60\d", s): return ("rep-energy","prin-energy","app-energy")
    if "hien-thi" in s or "s311a" in s: return ("rep-panel","prin-panel","app-panel")
    if any(k in s for k in ["kho-tim","ngung-san-xuat","thay-the-plc","tim-cam-bien"]): return ("rep-obsolete","obsolete-replacement","app-obsolete")
    if "seneca-viet-nam" in s: return ("rep-converter","signal-chain","app-remoteio")
    return None

CAP={"rep":"Hình đại diện","prin":"Nguyên lý hoạt động","spec":"Cấu tạo & thông số",
     "app":"Ứng dụng thiết bị","comp":"So sánh & lựa chọn"}

def slug_of(raw):
    mc=re.search(r"<!--(.*?)-->",raw,re.S); cmt=mc.group(1) if mc else ""
    m=re.search(r"URL SLUG[^:\n]*:\s*(\S+)",cmt); return m.group(1) if m else ""

def strip_old(lines):
    out=[]; skip_blanktail=False
    for ln in lines:
        st=ln.strip()
        if st=="<!--DIAGRAM-->" or re.match(r"<!--IMG:\w+-->",st): continue
        if re.match(r"!\[.*\]\(assets/diagrams/.*\)$",st): continue
        out.append(ln)
    # collapse 3+ blank lines to 1
    res=[]; blanks=0
    for ln in out:
        if ln.strip()=="":
            blanks+=1
            if blanks<=1: res.append(ln)
        else:
            blanks=0; res.append(ln)
    return res

def block(role,fname):
    return f"\n<!--IMG:{role}-->\n![{CAP[role]}](assets/diagrams/{fname}.svg)\n"

changed=0
for path in glob.glob(os.path.join(ROOT,"**","*.md"),recursive=True):
    base=os.path.basename(path)
    if base.startswith("_") or "/promo/" in path.replace("\\","/"): continue
    raw=open(path,encoding="utf-8").read()
    slug=slug_of(raw); trio=pick(slug)
    if not trio: continue
    # 3 ảnh (rep·prin·app) hoặc 5 ảnh (rep·prin·spec·app·comp — dùng cho Renepoly)
    five = len(trio)==5
    if five: rep,prin,spec,app,comp = trio
    else:    rep,prin,app = trio; spec=comp=None
    lines=strip_old(raw.split("\n"))
    # anchors
    p_rep=None; p_prin=None; p_app=None; p_spec=None; p_comp=None
    for i,ln in enumerate(lines):
        if p_rep is None and ln.strip().startswith("## "):
            p_rep=i+1
    # first blockquote end
    for i,ln in enumerate(lines):
        if ln.strip().startswith(">"):
            j=i
            while j<len(lines) and lines[j].strip().startswith(">"): j+=1
            p_prin=j; break
    # application heading (bỏ qua heading đầu = vị trí rep; khớp không phân biệt hoa/thường)
    for i,ln in enumerate(lines):
        if p_rep is not None and i < p_rep: continue
        if ln.strip().startswith("## ") and re.search(r"(ứng dụng|dùng để làm gì)",ln,re.I):
            p_app=i+1; break
    if p_app is None:
        for i,ln in enumerate(lines):
            if ln.strip().startswith("## ") and "Câu hỏi thường gặp" in ln:
                p_app=i; break
    if five:
        # spec: heading cấu tạo/thông số/thành phần (trước mục ứng dụng)
        for i,ln in enumerate(lines):
            if p_rep is not None and i < p_rep: continue
            if ln.strip().startswith("## ") and re.search(r"(cấu tạo|thông số|thành phần|cấu hình|kiến trúc)",ln,re.I):
                p_spec=i+1; break
        # comp: heading so sánh/lựa chọn/phân loại
        for i,ln in enumerate(lines):
            if p_rep is not None and i < p_rep: continue
            if ln.strip().startswith("## ") and re.search(r"(so sánh|lựa chọn|chọn |phân loại|khi nào|nên chọn)",ln,re.I):
                p_comp=i+1; break
    if five:
        # fallback: nếu thiếu heading tương ứng, chèn trước mục FAQ để bài luôn đủ 5 ảnh
        faq=next((i for i,ln in enumerate(lines)
                  if ln.strip().startswith("## ") and "Câu hỏi thường gặp" in ln), len(lines))
        if p_spec is None: p_spec=max(0,faq-1)
        if p_comp is None: p_comp=max(0,faq-1)
    # insert from largest index to smallest; tránh 2 ảnh trùng vị trí
    ins=[]
    used=set()
    def add(pos,role,fname):
        if pos is None: return
        while pos in used: pos+=1
        used.add(pos); ins.append((pos,block(role,fname)))
    add(p_rep,"rep",rep); add(p_prin,"prin",prin); add(p_app,"app",app)
    if five: add(p_spec,"spec",spec); add(p_comp,"comp",comp)
    for pos,blk in sorted(ins,key=lambda t:-t[0]):
        lines.insert(min(pos,len(lines)),blk)
    open(path,"w",encoding="utf-8").write("\n".join(lines))
    changed+=1
print("images inserted into",changed,"articles")
