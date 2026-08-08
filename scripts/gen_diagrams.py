#!/usr/bin/env python3
# Generate reusable in-article technical diagrams as SVG (light card style, readable on any surface).
import os
OUT = "/home/user/SEO-web/assets/diagrams"
os.makedirs(OUT, exist_ok=True)

# palette
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#1f6feb"; GREEN="#12a06a"; AMBER="#d9862a"; RED="#e5484d"; WIRE="#48607a"
FONT="font-family='Segoe UI,Roboto,Arial,sans-serif'"

def frame(w,h,body,title=""):
    t=f"<text x='20' y='30' {FONT} font-size='16' font-weight='700' fill='{INK}'>{title}</text>" if title else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='100%' height='auto' role='img'>"
            f"<rect x='1' y='1' width='{w-2}' height='{h-2}' rx='14' fill='{BG}' stroke='{BD}'/>"
            f"{t}{body}</svg>")

def box(x,y,w,h,label,fill="#ffffff",stroke=BLUE,tc=INK,sub="",fs=14):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='9' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
    if sub:
        s+=f"<text x='{x+w/2}' y='{y+h/2-4}' {FONT} font-size='{fs}' font-weight='700' fill='{tc}' text-anchor='middle'>{label}</text>"
        s+=f"<text x='{x+w/2}' y='{y+h/2+15}' {FONT} font-size='11.5' fill='{MUT}' text-anchor='middle'>{sub}</text>"
    else:
        s+=f"<text x='{x+w/2}' y='{y+h/2+5}' {FONT} font-size='{fs}' font-weight='700' fill='{tc}' text-anchor='middle'>{label}</text>"
    return s

def txt(x,y,t,size=12,color=INK,anchor="start",weight="400"):
    return f"<text x='{x}' y='{y}' {FONT} font-size='{size}' font-weight='{weight}' fill='{color}' text-anchor='{anchor}'>{t}</text>"

def arrow(x1,y1,x2,y2,color=WIRE,w=2.5,dash=""):
    d=f"stroke-dasharray='{dash}'" if dash else ""
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{w}' {d}/>"
            f"<polygon points='{x2},{y2} {x2-9},{y2-5} {x2-9},{y2+5}' fill='{color}'/>")

def line(x1,y1,x2,y2,color=WIRE,w=2.5):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{w}'/>"

def save(name,svg):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(svg)

# 1. 2-wire 4-20mA loop
def d_2wire():
    b=""
    b+=box(30,70,150,80,"Nguồn 24VDC",sub="+   —",stroke=AMBER)
    b+=box(300,70,150,80,"Cảm biến",sub="2 dây (loop)",stroke=BLUE)
    b+=box(560,70,150,80,"PLC / AI",sub="AI+   AI—",stroke=GREEN)
    b+=arrow(180,95,300,95); b+=txt(240,88,"+24V",11,AMBER,"middle","700")
    b+=arrow(450,95,560,95); b+=txt(505,88,"4–20mA",11,BLUE,"middle","700")
    # return path
    b+=line(635,150,635,185); b+=line(635,185,105,185); b+=line(105,185,105,150)
    b+=txt(370,178,"vòng dòng (—) khép kín về nguồn",11,MUT,"middle")
    return frame(740,215,b,"Đấu dây 2 dây (loop-powered) 4–20mA")
save("wiring-4-20ma-2wire",d_2wire())

# 2. 3-wire
def d_3wire():
    b=""
    b+=box(30,60,150,120,"Cảm biến","#ffffff",BLUE,INK,"3 dây")
    b+=box(560,60,150,120,"PLC","#ffffff",GREEN)
    b+=arrow(180,85,560,85,AMBER); b+=txt(370,78,"+24V (nguồn)",11,AMBER,"middle","700")
    b+=arrow(180,120,560,120,WIRE); b+=txt(370,113,"0V (GND chung)",11,MUT,"middle","700")
    b+=arrow(180,155,560,155,BLUE); b+=txt(370,148,"OUT 4–20mA → AI",11,BLUE,"middle","700")
    return frame(740,210,b,"Đấu dây 3 dây 4–20mA")
save("wiring-4-20ma-3wire",d_3wire())

# 3. pressure types
def gauge(cx,cy,label):
    s=f"<circle cx='{cx}' cy='{cy}' r='34' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
    s+=f"<line x1='{cx}' y1='{cy}' x2='{cx+18}' y2='{cy-22}' stroke='{RED}' stroke-width='3'/>"
    s+=f"<circle cx='{cx}' cy='{cy}' r='4' fill='{INK}'/>"
    s+=txt(cx,cy+58,label,12.5,INK,"middle","700")
    return s
def d_ptypes():
    b=gauge(130,90,"Tương đối")+txt(130,175,"so với khí quyển",11,MUT,"middle")
    b+=gauge(370,90,"Tuyệt đối")+txt(370,175,"so với chân không",11,MUT,"middle")
    b+=gauge(610,90,"Chênh áp")+txt(610,175,"hiệu áp 2 điểm",11,MUT,"middle")
    return frame(740,205,b,"3 loại áp suất")
save("pressure-types",d_ptypes())

# 4. differential pressure measurement
def d_dp():
    b=txt(30,60,"Đo lưu lượng (qua orifice)",13,INK,"start","700")
    b+=line(40,110,300,110,WIRE,8)  # pipe
    b+=f"<rect x='165' y='92' width='8' height='36' fill='{RED}'/>"  # orifice
    b+=box(120,150,110,40,"DP","#fff",BLUE,INK,"+   —",12)
    b+=line(150,110,150,150,WIRE); b+=line(200,110,200,150,WIRE)
    b+=arrow(40,110,120,110,GREEN); b+=txt(70,102,"dòng",10,GREEN,"middle","700")
    b+=txt(430,60,"Đo mức bồn kín",13,INK,"start","700")
    b+=f"<rect x='470' y='80' width='150' height='110' fill='#eef3fb' stroke='{WIRE}'/>"
    b+=f"<rect x='470' y='135' width='150' height='55' fill='#cfe0f7' stroke='none'/>"
    b+=box(630,150,80,40,"DP","#fff",BLUE)
    b+=line(620,175,630,175,WIRE); b+=line(620,90,690,90,WIRE); b+=line(690,90,690,150,WIRE)
    b+=txt(545,205,"chênh áp đáy–đỉnh → mức",11,MUT,"middle")
    return frame(740,230,b,"Ứng dụng cảm biến chênh áp")
save("dp-measurement",d_dp())

# 5. RTD vs thermocouple
def d_rtdtc():
    b=box(40,60,300,150,"Pt100 (RTD)","#fff",BLUE)
    b+=txt(60,100,"• Chính xác, ổn định",12,INK); b+=txt(60,125,"• Dải ~ -200…600°C",12,INK)
    b+=txt(60,150,"• Đấu 2 / 3 / 4 dây",12,INK); b+=txt(60,175,"→ cần độ chính xác cao",11.5,GREEN,"start","700")
    b+=box(400,60,300,150,"Can nhiệt (TC)","#fff",AMBER)
    b+=txt(420,100,"• Chịu nhiệt rất cao",12,INK); b+=txt(420,125,"• Tới ~1200°C+ (K,S)",12,INK)
    b+=txt(420,150,"• Bền, giá tốt",12,INK); b+=txt(420,175,"→ cần nhiệt độ cực cao",11.5,AMBER,"start","700")
    return frame(740,235,b,"Pt100 vs Can nhiệt")
save("rtd-vs-tc",d_rtdtc())

# 6. signal converter with isolation
def d_conv():
    b=box(40,70,180,80,"4–20mA","#fff",BLUE,INK,"tín hiệu vào")
    b+=box(300,60,150,100,"Bộ chuyển đổi","#eef3fb",BLUE,INK,"CÁCH LY")
    b+=f"<line x1='375' y1='70' x2='375' y2='150' stroke='{RED}' stroke-width='2' stroke-dasharray='4 4'/>"
    b+=box(530,70,170,80,"0–10V","#fff",GREEN,INK,"tín hiệu ra")
    b+=arrow(220,110,300,110); b+=arrow(450,110,530,110)
    b+=txt(375,178,"galvanic isolation — chống nhiễu",11,MUT,"middle")
    return frame(740,205,b,"Chuyển đổi & cách ly tín hiệu")
save("signal-converter",d_conv())

# 7. signal chain
def d_chain():
    b=box(30,75,170,80,"Cảm biến","#fff",BLUE)
    b+=box(285,75,170,80,"Bộ chuyển đổi","#eef3fb",BLUE,INK,"/ cách ly")
    b+=box(560,75,170,80,"PLC / SCADA","#fff",GREEN)
    b+=arrow(200,115,285,115); b+=txt(242,108,"4–20mA",10.5,BLUE,"middle","700")
    b+=arrow(455,115,560,115); b+=txt(507,108,"chuẩn hoá",10.5,MUT,"middle","700")
    return frame(760,205,b,"Chuỗi tín hiệu đo lường")
save("signal-chain",d_chain())

# 8. modbus remote I/O
def d_remoteio():
    b=""
    for i,(lbl) in enumerate(["Z-4RTD2","Z-8AI","Z-4AO"]):
        x=40+i*150
        b+=box(x,60,120,60,lbl,"#fff",BLUE,INK,"",12.5)
        b+=line(x+60,120,x+60,175,WIRE)
    b+=line(70,175,650,175,BLUE,3); b+=txt(360,170,"RS485 — Modbus RTU",11,BLUE,"middle","700")
    b+=box(560,60,150,60,"PLC / SCADA","#fff",GREEN)
    b+=line(635,120,635,175,WIRE)
    return frame(760,205,b,"Remote I/O (Z-PC) qua Modbus RTU")
save("modbus-remote-io",d_remoteio())

# 9. modbus gateway
def d_gateway():
    b=box(30,70,180,90,"Thiết bị RS485","#fff",BLUE,INK,"Modbus RTU")
    b+=box(300,70,150,90,"Gateway","#eef3fb",BLUE,INK,"Z-KEY")
    b+=box(540,70,190,90,"SCADA / PC","#fff",GREEN,INK,"Modbus TCP")
    b+=arrow(210,115,300,115); b+=txt(255,108,"RS485",10.5,MUT,"middle","700")
    b+=arrow(450,115,540,115); b+=txt(495,108,"Ethernet",10.5,GREEN,"middle","700")
    return frame(760,205,b,"Gateway Modbus TCP ↔ RTU")
save("modbus-gateway",d_gateway())

# 10. remote monitoring (RTU/datalogger + 3G/4G)
def d_remote():
    b=box(30,80,150,80,"Cảm biến / I/O","#fff",BLUE)
    b+=box(255,75,160,90,"RTU / Datalogger","#eef3fb",BLUE,INK,"UPS")
    b+=f"<polygon points='520,150 545,80 570,150' fill='none' stroke='{AMBER}' stroke-width='2.5'/>"
    b+=f"<path d='M535 80 q10 -14 20 0' fill='none' stroke='{AMBER}' stroke-width='2'/>"
    b+=txt(545,168,"3G / 4G",11,AMBER,"middle","700")
    b+=box(620,80,110,80,"Cloud / SCADA","#fff",GREEN,INK,"",12)
    b+=arrow(180,120,255,120); b+=arrow(415,120,505,120)
    b+=arrow(575,120,620,120)
    b+=txt(335,185,"cảnh báo SMS/Email khi vượt ngưỡng",11,MUT,"middle")
    return frame(760,215,b,"Giám sát từ xa (RTU/Datalogger)")
save("remote-monitoring",d_remote())

# 11. energy monitoring
def d_energy():
    b=box(30,80,140,80,"Tải 3 pha","#fff",AMBER)
    b+=f"<circle cx='230' cy='120' r='24' fill='#fff' stroke='{WIRE}' stroke-width='2'/>"+txt(230,124,"CT",12,INK,"middle","700")
    b+=box(320,75,170,90,"Đồng hồ đo điện","#eef3fb",BLUE,INK,"S500 / S604")
    b+=box(580,80,150,80,"EMS / SCADA","#fff",GREEN)
    b+=arrow(170,120,206,120); b+=arrow(254,120,320,120)
    b+=arrow(490,120,580,120); b+=txt(535,113,"Modbus",10.5,BLUE,"middle","700")
    return frame(760,205,b,"Giám sát điện năng qua Modbus")
save("energy-monitoring",d_energy())

# 12. panel indicator
def d_panel():
    b=box(30,80,150,80,"Cảm biến","#fff",BLUE,INK,"4–20mA / Pt100")
    b+=box(290,65,180,110,"Bộ hiển thị","#0f1720",BLUE,"#7ff0c0","8.88",22)
    b+=box(560,60,170,44,"Relay cảnh báo","#fff",RED,INK,"",12)
    b+=box(560,120,170,44,"Ngõ ra analog","#fff",GREEN,INK,"",12)
    b+=arrow(180,120,290,120)
    b+=arrow(470,90,560,85); b+=arrow(470,140,560,142)
    return frame(760,205,b,"Bộ hiển thị (panel meter)")
save("panel-indicator",d_panel())

# 13. obsolete -> replacement
def d_obsolete():
    b=box(40,75,190,90,"Mã cũ","#fff",RED,INK,"obsolete / EOL")
    b+=box(300,70,180,100,"Đối chiếu","#eef3fb",BLUE,INK,"cross-reference")
    b+=box(545,75,185,90,"Mã thay thế","#fff",GREEN,INK,"kế nhiệm / tương đương")
    b+=arrow(230,120,300,120); b+=arrow(480,120,545,120)
    b+=txt(390,190,"đối chiếu dải đo • tín hiệu • chứng nhận • kết nối",11,MUT,"middle")
    return frame(760,215,b,"Tìm hàng thay thế cho thiết bị ngừng sản xuất")
save("obsolete-replacement",d_obsolete())

print("diagrams:", len(os.listdir(OUT)))
