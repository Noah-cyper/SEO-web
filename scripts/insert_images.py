#!/usr/bin/env python3
# Insert 3 images per article: representative / principle / application. Idempotent.
import os, re, glob
ROOT="/home/user/SEO-web/content/vi"

def pick(slug):
    s=slug
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

CAP={"rep":"Hình đại diện","prin":"Nguyên lý hoạt động","app":"Ứng dụng thiết bị"}

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
    rep,prin,app=trio
    lines=strip_old(raw.split("\n"))
    # anchors
    p_rep=None; p_prin=None; p_app=None
    for i,ln in enumerate(lines):
        if p_rep is None and ln.strip().startswith("## "):
            p_rep=i+1
    # first blockquote end
    for i,ln in enumerate(lines):
        if ln.strip().startswith(">"):
            j=i
            while j<len(lines) and lines[j].strip().startswith(">"): j+=1
            p_prin=j; break
    # application heading
    for i,ln in enumerate(lines):
        if ln.strip().startswith("## ") and re.search(r"(Ứng dụng|dùng để làm gì)",ln):
            p_app=i+1; break
    if p_app is None:
        for i,ln in enumerate(lines):
            if ln.strip().startswith("## ") and "Câu hỏi thường gặp" in ln:
                p_app=i; break
    # insert from largest index to smallest
    ins=[]
    if p_rep is not None: ins.append((p_rep,block("rep",rep)))
    if p_prin is not None: ins.append((p_prin,block("prin",prin)))
    if p_app is not None: ins.append((p_app,block("app",app)))
    for pos,blk in sorted(ins,key=lambda t:-t[0]):
        lines.insert(pos,blk)
    open(path,"w",encoding="utf-8").write("\n".join(lines))
    changed+=1
print("3 images inserted into",changed,"articles")
