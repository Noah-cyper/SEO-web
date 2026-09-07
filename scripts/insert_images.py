#!/usr/bin/env python3
# Insert 3 images per article: representative / principle / application. Idempotent.
import os, re, glob
ROOT="/home/user/SEO-web/content/vi"

def pick(slug):
    s=slug
    # Rhize (Manufacturing Data Hub) — bảng tra theo slug, giữ đúng sơ đồ đã chèn
    _RHIZE = {
        "kien-truc-nen-tang-rhize": ("rep-mdh","prin-event-driven","app-graph"),
        "manufacturing-data-hub-la-gi": ("rep-mdh","prin-event-driven","app-graph"),
        "rhize-admin-ui": ("rep-app","prin-isa95","app-graph"),
        "rhize-agent-ket-noi": ("rep-agent","prin-event-driven","app-graph"),
        "rhize-ai-ml-du-lieu-san-xuat": ("rep-analytics","prin-ai","app-graph"),
        "rhize-b2mml": ("rep-isa95","prin-isa95","app-graph"),
        "rhize-batch-record-dien-tu": ("rep-app","prin-event-driven","app-graph"),
        "rhize-bpmn-workflow": ("rep-workflow","prin-bpmn","app-graph"),
        "rhize-core": ("rep-core","prin-event-driven","app-graph"),
        "rhize-db-graph-database": ("rep-graphdb","prin-graph","app-graph"),
        "rhize-grafana-tempo": ("rep-analytics","prin-event-driven","app-graph"),
        "rhize-graphql-api": ("rep-graphql","prin-event-driven","app-graph"),
        "rhize-isa-95": ("rep-isa95","prin-isa95","app-graph"),
        "rhize-keycloak-phan-quyen": ("rep-security","prin-zerotrust","app-graph"),
        "rhize-mqtt-uns": ("rep-nats","prin-event-driven","app-graph"),
        "rhize-nats-event-streaming": ("rep-nats","prin-event-driven","app-graph"),
        "rhize-nganh-duoc-pham": ("rep-platform","prin-isa95","app-graph"),
        "rhize-san-xuat-roi-rac-serial": ("rep-platform","prin-graph","app-graph"),
        "rhize-nganh-thuc-pham-do-uong": ("rep-platform","prin-event-driven","app-graph"),
        "rhize-oee": ("rep-analytics","prin-event-driven","app-oee"),
        "rhize-opc-ua": ("rep-agent","prin-event-driven","app-graph"),
        "rhize-quan-ly-chat-luong": ("rep-app","prin-event-driven","app-graph"),
        "rhize-quan-ly-kho-vat-tu": ("rep-app","prin-event-driven","app-graph"),
        "rhize-scheduling-lap-ke-hoach": ("rep-app","prin-event-driven","app-graph"),
        "rhize-tich-hop-erp": ("rep-app","prin-event-driven","app-graph"),
        "rhize-tich-hop-scada-historian": ("rep-platform","prin-event-driven","app-graph"),
        "rhize-truy-xuat-nguon-goc": ("rep-graphdb","prin-graph","app-graph"),
        "rhize-trien-khai-kubernetes": ("rep-platform","prin-event-driven","app-graph"),
        "rhize": ("rep-mdh","prin-event-driven","app-graph"),
        "rhize-vs-mes-historian-data-lake": ("rep-mdh","prin-event-driven","app-graph"),
    }
    if s.strip("/") in _RHIZE: return _RHIZE[s.strip("/")]
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

_RHIZE_ALT = {
    "kien-truc-nen-tang-rhize": "Kiến Trúc Rhize - Các Thành Phần Nền Tảng",
    "manufacturing-data-hub-la-gi": "Manufacturing Data Hub Là Gì Trong Nhà Máy Số?",
    "rhize-admin-ui": "Rhize Admin UI - Giao Diện Quản Trị Data Hub",
    "rhize-agent-ket-noi": "Rhize Agent - Kết Nối Thiết Bị Vào Data Hub",
    "rhize-ai-ml-du-lieu-san-xuat": "dữ liệu sản xuất - Rhize AI - Nền Dữ Liệu Cho AI Trong Nhà Máy",
    "rhize-b2mml": "Rhize B2MML - Chuẩn Trao Đổi Dữ Liệu ISA-95",
    "rhize-batch-record-dien-tu": "Batch Record Điện Tử Với Rhize - Hồ Sơ Lô Realtime",
    "rhize-bpmn-workflow": "Rhize BPMN - Workflow Low-Code Cho Nhà Máy",
    "rhize-core": "Rhize Core - Rules Engine Xử Lý Sự Kiện Sản Xuất",
    "rhize-db-graph-database": "Rhize DB - Graph Database Chuẩn ISA-95",
    "rhize-grafana-tempo": "Rhize Grafana & Tempo - Giám Sát Và Truy Vết",
    "rhize-graphql-api": "Rhize GraphQL API - Một Endpoint Cho Mọi Ứng Dụng",
    "rhize-isa-95": "Rhize ISA-95 - Mô Hình Dữ Liệu Chuẩn Nhà Máy",
    "rhize-keycloak-phan-quyen": "Rhize Keycloak - Xác Thực Và Phân Quyền Dữ Liệu",
    "rhize-mqtt-uns": "Rhize MQTT & UNS - Bổ Sung Ngữ Cảnh Cho Namespace",
    "rhize-nats-event-streaming": "Rhize NATS - Bus Sự Kiện Thời Gian Thực",
    "rhize-nganh-duoc-pham": "Rhize Ngành Dược - Data Hub Cho Nhà Máy GMP",
    "rhize-san-xuat-roi-rac-serial": "Rhize Sản Xuất Rời Rạc - Truy Xuất Theo Serial",
    "rhize-nganh-thuc-pham-do-uong": "Rhize Ngành Thực Phẩm - Truy Xuất Và OEE",
    "rhize-oee": "Rhize OEE - Hiệu Suất Thiết Bị Từ Dữ Liệu Thật",
    "rhize-opc-ua": "Rhize OPC UA - Kết Nối PLC Vào Data Hub",
    "rhize-quan-ly-chat-luong": "Rhize Quản Lý Chất Lượng Ngay Trong Quá Trình",
    "rhize-quan-ly-kho-vat-tu": "Rhize Quản Lý Kho Và Vật Tư Tại Xưởng",
    "rhize-scheduling-lap-ke-hoach": "Rhize Scheduling - Điều Độ Theo Dữ Liệu Thật",
    "rhize-tich-hop-erp": "Rhize Tích Hợp ERP - Nối Văn Phòng Với Nhà Xưởng",
    "rhize-tich-hop-scada-historian": "Rhize Tích Hợp SCADA & Historian Sẵn Có",
    "rhize-truy-xuat-nguon-goc": "Rhize Track & Trace - Truy Xuất Nguồn Gốc Nhanh",
    "rhize-trien-khai-kubernetes": "Triển Khai Rhize Trên Kubernetes - Hạ Tầng",
    "rhize": "Rhize - Manufacturing Data Hub Chuẩn ISA-95",
    "rhize-vs-mes-historian-data-lake": "Rhize vs MES, Historian, Data Lake - Chọn Cái Nào?",
}
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

def block(role,fname,slug=""):
    cap = _RHIZE_ALT.get(slug.strip("/"), CAP[role]) if role=="rep" else CAP[role]
    return f"\n<!--IMG:{role}-->\n![{cap}](assets/diagrams/{fname}.svg)\n"

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
    # application heading (bỏ qua heading đầu = vị trí rep; khớp không phân biệt hoa/thường)
    for i,ln in enumerate(lines):
        if p_rep is not None and i < p_rep: continue
        if ln.strip().startswith("## ") and re.search(r"(ứng dụng|dùng để làm gì)",ln,re.I):
            p_app=i+1; break
    if p_app is None:
        for i,ln in enumerate(lines):
            if ln.strip().startswith("## ") and "Câu hỏi thường gặp" in ln:
                p_app=i; break
    # insert from largest index to smallest
    ins=[]
    if p_rep is not None: ins.append((p_rep,block("rep", rep, slug)))
    if p_prin is not None: ins.append((p_prin,block("prin",prin)))
    if p_app is not None: ins.append((p_app,block("app",app)))
    for pos,blk in sorted(ins,key=lambda t:-t[0]):
        lines.insert(pos,blk)
    open(path,"w",encoding="utf-8").write("\n".join(lines))
    changed+=1
print("3 images inserted into",changed,"articles")
