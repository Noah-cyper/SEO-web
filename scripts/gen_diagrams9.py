#!/usr/bin/env python3
# Diagrams for the Rhize cluster (Manufacturing Data Hub).
# Same light-card house style as gen_diagrams2..8.py.
import os
OUT = "/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT, exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#1f6feb"; GREEN="#12a06a"; AMBER="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"
VIO="#6E56CF"                      # accent thương hiệu Rhize
F="font-family='Segoe UI,Roboto,Arial,sans-serif'"

def frame(w,h,body,title=""):
    t=f"<text x='20' y='30' {F} font-size='16' font-weight='700' fill='{INK}'>{title}</text>" if title else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='100%' height='auto' role='img'>"
            f"<rect x='1' y='1' width='{w-2}' height='{h-2}' rx='14' fill='{BG}' stroke='{BD}'/>{t}{body}</svg>")
def T(x,y,t,s=12,c=INK,a="start",w="400"):
    return f"<text x='{x}' y='{y}' {F} font-size='{s}' font-weight='{w}' fill='{c}' text-anchor='{a}'>{t}</text>"
def box(x,y,w,h,label="",fill="#fff",stroke=VIO,tc=INK,fs=13,sub=""):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='9' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
    if label and sub:
        s+=T(x+w/2,y+h/2-3,label,fs,tc,"middle","700")+T(x+w/2,y+h/2+16,sub,11,MUT,"middle")
    elif label:
        s+=T(x+w/2,y+h/2+5,label,fs,tc,"middle","700")
    return s
def arr(x1,y1,x2,y2,c=WIRE,w=2.5):
    dx=9 if x2>x1 else -9
    if abs(y2-y1)>abs(x2-x1):
        dy=9 if y2>y1 else -9
        head=f"{x2},{y2} {x2-5},{y2-dy} {x2+5},{y2-dy}"
    else:
        head=f"{x2},{y2} {x2-dx},{y2-5} {x2-dx},{y2+5}"
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
            f"<polygon points='{head}' fill='{c}'/>")
def line(x1,y1,x2,y2,c=WIRE,w=2.5,dash=""):
    d=f" stroke-dasharray='{dash}'" if dash else ""
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'{d}/>"
def node(cx,cy,r,label,fill="#fff",stroke=VIO,fs=11):
    return (f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
            + T(cx,cy+4,label,fs,INK,"middle","700"))
def save(name,body,title,w=720,h=270):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

W,H=720,270

# 1. rep-mdh — Manufacturing Data Hub ngồi giữa OT và IT
s =box(30,90,130,60,"OT / Nhà xưởng","#eef3fb",BLUE,INK,12,"PLC · SCADA")
s+=box(30,175,130,55,"Thiết bị đo","#eef3fb",BLUE,INK,12,"cảm biến")
s+=box(275,80,180,150,"MANUFACTURING","#f2effc",VIO,INK,13,"DATA HUB")
s+=T(365,190,"ISA-95 · GraphQL · BPMN",11,MUT,"middle")
s+=box(560,90,130,60,"IT / Doanh nghiệp","#eef3fb",GREEN,INK,12,"ERP · BI")
s+=box(560,175,130,55,"Ứng dụng","#eef3fb",GREEN,INK,12,"dashboard · AI")
s+=arr(160,120,275,130,BLUE)+arr(160,200,275,180,BLUE)
s+=arr(455,130,560,120,GREEN)+arr(455,180,560,200,GREEN)
save("rep-mdh",s,"Manufacturing Data Hub: lớp dữ liệu có ngữ cảnh giữa OT và IT")

# 2. rep-isa95 — mô hình ISA-95
s =box(40,70,150,44,"Enterprise","#f2effc",VIO,INK,12)
s+=box(40,120,150,44,"Site / Nhà máy","#f7f5fd",VIO,INK,12)
s+=box(40,170,150,44,"Area / Khu vực","#fff",VIO,INK,12)
s+=box(40,220,150,40,"Work center / unit","#fff",VIO,INK,11)
for y in (114,164,214): s+=line(115,y,115,y+6,STEEL,2)
s+=T(300,66,"4 mô hình tài nguyên ISA-95",13,INK,"start","700")
s+=box(300,80,180,44,"Equipment · Thiết bị","#fff",BLUE,INK,12)
s+=box(300,132,180,44,"Material · Vật tư","#fff",GREEN,INK,12)
s+=box(500,80,180,44,"Personnel · Nhân sự","#fff",AMBER,INK,12)
s+=box(500,132,180,44,"Physical asset","#fff",STEEL,INK,12)
s+=box(300,192,380,44,"Models of work: definition → schedule → response","#f2effc",VIO,INK,12)
save("rep-isa95",s,"ISA-95: phân cấp thiết bị và bốn mô hình tài nguyên")

# 3. rep-graphql — một endpoint cho mọi ứng dụng
apps=["Dashboard","Báo cáo OEE","ERP","AI / ML"]
s=""
for i,a in enumerate(apps):
    s+=box(30,60+i*50,140,40,a,"#fff",GREEN,INK,11)
    s+=arr(170,80+i*50,290,150,GREEN,2)
s+=box(290,120,150,60,"GraphQL","#f2effc",VIO,INK,14,"một endpoint")
s+=arr(440,150,540,150,VIO)
s+=box(540,110,150,80,"Rhize DB","#fff",VIO,INK,13,"đồ thị ISA-95")
save("rep-graphql","".join(s),"GraphQL: một điểm truy cập duy nhất cho mọi ứng dụng")

# 4. rep-graphdb — graph database
s =node(140,132,34,"Lô TP","#f2effc")
s+=node(58,220,28,"NL 1")+node(145,232,28,"NL 2")+node(232,214,28,"NL 3")
s+=line(120,160,76,194,STEEL,2)+line(143,166,145,204,STEEL,2)+line(165,158,215,192,STEEL,2)
s+=node(300,108,28,"Máy")+node(252,66,24,"Ca B")
s+=line(173,124,272,112,STEEL,2)+line(283,88,265,84,STEEL,2)
s+=T(360,90,"Mỗi lô, thiết bị, người là một nút.",12,INK)
s+=T(360,112,"Mỗi quan hệ là một cạnh.",12,INK)
s+=T(360,145,"Truy xuất nguồn gốc = duyệt cạnh,",12,MUT)
s+=T(360,167,"không phải join nhiều bảng.",12,MUT)
s+=box(360,190,320,50,"Rhize DB (libreBaas)","#f2effc",VIO,INK,13,"graph + time-series")
save("rep-graphdb",s,"Rhize DB: đồ thị tri thức của toàn bộ vận hành")

# 5. rep-core — rules engine
s =box(30,110,140,60,"Tag thô","#fff",STEEL,INK,12,"Line3 = 4820")
s+=arr(170,140,250,140,STEEL)
s+=box(250,80,190,120,"Rhize Core","#f2effc",VIO,INK,14,"xử lý luật")
s+=T(345,175,"đối chiếu model ISA-95",11,MUT,"middle")
s+=arr(440,140,520,140,VIO)
s+=box(520,80,170,120,"Sự kiện","#fff",GREEN,INK,13,"có ngữ cảnh")
s+=T(605,150,"máy · lô · ca",11,MUT,"middle")
s+=T(605,170,"lệnh sản xuất",11,MUT,"middle")
s+=T(605,190,"so kế hoạch",11,MUT,"middle")
s+=T(30,230,"Historian lưu con số. Rhize Core lưu ý nghĩa của con số đó.",12,MUT)
save("rep-core",s,"Rhize Core: biến giá trị tag thành sự kiện có nghĩa")

# 6. rep-workflow — BPMN
s =node(60,140,20,"","#fff",GREEN)+T(60,185,"Sự kiện",11,MUT,"middle")
s+=arr(82,140,130,140,STEEL,2)
s+=box(130,115,110,50,"Kiểm tra","#fff",VIO,INK,12)
s+=arr(240,140,285,140,STEEL,2)
s+=(f"<polygon points='315,110 345,140 315,170 285,140' fill='#fff' stroke='{AMBER}' stroke-width='2'/>")
s+=T(315,105,"Điều kiện?",11,AMBER,"middle","700")
s+=arr(345,140,395,140,STEEL,2)
s+=box(395,115,120,50,"Gọi ERP","#fff",VIO,INK,12)
s+=arr(515,140,560,140,STEEL,2)
s+=box(560,115,110,50,"Ghi kết quả","#fff",VIO,INK,12)
s+=line(315,170,315,215,STEEL,2)+arr(315,215,395,215,STEEL,2)
s+=box(395,195,120,42,"Cảnh báo QC","#fff",RED,INK,11)
save("rep-workflow",s,"BPMN: quy trình vẽ ra là chạy được, không cần viết lại")

# 7. rep-agent — kết nối thiết bị
s =box(30,70,140,50,"PLC / DCS","#eef3fb",BLUE,INK,12)
s+=box(30,135,140,50,"SCADA","#eef3fb",BLUE,INK,12)
s+=box(30,200,140,45,"Gateway Modbus","#eef3fb",BLUE,INK,11)
s+=arr(170,95,290,130,BLUE,2)+arr(170,160,290,155,BLUE,2)+arr(170,222,290,180,BLUE,2)
s+=box(290,110,160,90,"Libre Agent","#f2effc",VIO,INK,13,"subscribe tag")
s+=arr(450,140,540,110,VIO)+T(495,100,"đọc",10,MUT,"middle")
s+=arr(540,180,450,180,GREEN)+T(495,205,"ghi (qua BPMN)",10,MUT,"middle")
s+=box(540,90,150,110,"NATS + Core","#fff",VIO,INK,12,"nền tảng Rhize")
s+=T(30,262,"OPC UA · MQTT · Modbus qua gateway",11,MUT)
save("rep-agent",s,"Libre Agent: cầu nối hai chiều giữa lớp OT và Data Hub")

# 8. rep-nats — bus sự kiện
s =box(60,60,130,44,"Libre Agent","#fff",BLUE,INK,11)
s+=arr(125,104,125,135,BLUE,2)
s+=(f"<rect x='60' y='135' width='600' height='46' rx='23' fill='#f2effc' stroke='{VIO}' stroke-width='2'/>")
s+=T(360,164,"NATS · bus sự kiện thời gian thực",14,VIO,"middle","700")
for i,(x,lab) in enumerate([(230,"Libre Core"),(390,"BPMN engine"),(540,"Dịch vụ mới")]):
    s+=arr(x+65,181,x+65,210,VIO,2)
    st = VIO if i<2 else STEEL
    s+=box(x,210,130,44,lab,"#fff",st,INK,11)
s+=T(60,116,"publish khi tag đổi giá trị",11,MUT)
s+=T(660,254,"",11,MUT,"end")
save("rep-nats",s,"NATS: bên phát không cần biết ai sẽ dùng dữ liệu")

# 9. prin-event-driven — luồng dữ liệu
steps=[("PLC","tag đổi",BLUE),("Agent","publish",BLUE),("NATS","định tuyến",VIO),
       ("Core","gắn ngữ cảnh",VIO),("Rhize DB","ghi đồ thị",VIO),("GraphQL","ứng dụng đọc",GREEN)]
s=""
x=25
for i,(lab,sub,c) in enumerate(steps):
    s+=box(x,110,100,64,lab,"#fff",c,INK,12,sub)
    s+=T(x+50,100,str(i+1),11,MUT,"middle","700")
    if i<len(steps)-1: s+=arr(x+100,142,x+115,142,STEEL,2)
    x+=115
s+=T(25,215,"Ngữ cảnh được gắn NGAY khi sự kiện xảy ra — không phải dựng lại lúc làm báo cáo.",12,MUT)
s+=T(25,240,"Đó là khác biệt giữa historian và Manufacturing Data Hub.",12,MUT)
save("prin-event-driven",s,"Luồng dữ liệu hướng sự kiện trong Rhize")

# 10. prin-isa95 — definition vs actual
s =T(190,66,"ĐỊNH NGHĨA (definition)",12,MUT,"middle","700")
s+=T(530,66,"THỰC TẾ (actual)",12,MUT,"middle","700")
rows=[("Loại thiết bị","Máy chiết số 2",BLUE),("Bột mì loại A","Lô NL-2026-118",GREEN),
      ("Vai trò: vận hành","Ca B · tổ trưởng",AMBER)]
y=82
for d,a,c in rows:
    s+=box(60,y,260,48,d,"#fff",c,INK,12)
    s+=arr(320,y+24,400,y+24,STEEL,2)
    s+=box(400,y,260,48,a,"#f7f5fd",c,INK,12)
    y+=58
s+=T(60,250,"Truy xuất nguồn gốc chỉ chạy được khi hệ thống ghi đúng phần THỰC TẾ.",12,MUT)
save("prin-isa95",s,"ISA-95 tách đôi: cái được phép và cái đã thực sự xảy ra")

# 11. prin-graph — graph vs bảng
s =T(180,62,"BẢNG QUAN HỆ",12,MUT,"middle","700")
s+=T(540,62,"ĐỒ THỊ (Rhize DB)",12,VIO,"middle","700")
for i in range(3):
    s+=(f"<rect x='70' y='{80+i*46}' width='220' height='36' rx='5' fill='#fff' stroke='{STEEL}' stroke-width='1.5'/>")
    s+=T(180,103+i*46,["bảng lô","bảng nguyên liệu","bảng thiết bị"][i],11,MUT,"middle")
s+=T(180,240,"join lồng nhau, truy vấn đệ quy",11,RED,"middle")
s+=node(540,105,26,"Lô","#f2effc")
s+=node(460,180,24,"NL")+node(545,195,24,"Máy")+node(630,170,24,"Ca")
s+=line(522,127,478,158,VIO,2)+line(542,131,545,171,VIO,2)+line(562,124,614,152,VIO,2)
s+=T(540,240,"duyệt cạnh, một bước",11,GREEN,"middle")
s+=line(360,70,360,250,BD,2,"5 5")
save("prin-graph",s,"Truy xuất nguồn gốc là bài toán duyệt đồ thị")

# 12. prin-bpmn — phần tử BPMN
els=[("Start event","sự kiện kích hoạt",GREEN),("Service task","gọi API, ghi dữ liệu",VIO),
     ("Gateway","rẽ nhánh điều kiện",AMBER),("User task","người xác nhận",BLUE),
     ("End event","kết thúc, ghi vết",RED)]
s=""
x=25
for lab,sub,c in els:
    s+=box(x,105,128,74,lab,"#fff",c,INK,12,sub)
    x+=138
s+=T(25,215,"Lưu đồ có thể chạy được: người vận hành đọc hiểu, kỹ sư sửa trên giao diện,",12,MUT)
s+=T(25,240,"không phải dừng dây chuyền để sửa logic trong PLC.",12,MUT)
save("prin-bpmn",s,"Các phần tử BPMN dùng trong workflow sản xuất")

# 13. app-graph — ứng dụng trong nhà máy
s =box(25,70,150,58,"Truy xuất lô","#fff",GREEN,INK,12,"phút thay vì ngày")
s+=box(25,145,150,58,"OEE thật","#fff",GREEN,INK,12,"bắt cả dừng ngắn")
s+=box(545,70,150,58,"Hồ sơ lô điện tử","#fff",BLUE,INK,12,"review by exception")
s+=box(545,145,150,58,"Nền dữ liệu AI","#fff",BLUE,INK,12,"có nhãn sẵn")
s+=box(255,95,210,110,"Một mô hình","#f2effc",VIO,INK,14,"dữ liệu ISA-95")
s+=T(360,178,"dùng chung cho mọi bài toán",11,MUT,"middle")
s+=arr(255,110,175,99,VIO,2)+arr(255,180,175,174,VIO,2)
s+=arr(465,110,545,99,VIO,2)+arr(465,180,545,174,VIO,2)
s+=T(25,245,"Thêm bài toán mới không phải lắp thêm hệ thống — chỉ thêm truy vấn và workflow.",12,MUT)
save("app-graph",s,"Một nền dữ liệu, nhiều bài toán nhà máy")

print("Đã tạo", len([f for f in os.listdir(OUT) if f.startswith(('rep-mdh','rep-isa95','rep-graphql','rep-graphdb','rep-core','rep-workflow','rep-agent','rep-nats','prin-event','prin-isa95','prin-graph','prin-bpmn','app-graph'))]), "sơ đồ Rhize")
