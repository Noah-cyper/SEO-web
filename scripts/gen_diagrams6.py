#!/usr/bin/env python3
# Diagrams for the PLC per-brand error articles + PLC–HMI/Modbus comms article.
# Same light-card house style as gen_diagrams2..5.py.
import os
OUT = "/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT, exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#1f6feb"; GREEN="#12a06a"; AMBER="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"
F="font-family='Segoe UI,Roboto,Arial,sans-serif'"

def frame(w,h,body,title=""):
    t=f"<text x='20' y='30' {F} font-size='16' font-weight='700' fill='{INK}'>{title}</text>" if title else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='100%' height='auto' role='img'>"
            f"<rect x='1' y='1' width='{w-2}' height='{h-2}' rx='14' fill='{BG}' stroke='{BD}'/>{t}{body}</svg>")
def T(x,y,t,s=12,c=INK,a="start",w="400"):
    return f"<text x='{x}' y='{y}' {F} font-size='{s}' font-weight='{w}' fill='{c}' text-anchor='{a}'>{t}</text>"
def box(x,y,w,h,label="",fill="#fff",stroke=BLUE,tc=INK,fs=13,sub=""):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='9' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
    if label and sub:
        s+=T(x+w/2,y+h/2-3,label,fs,tc,"middle","700")+T(x+w/2,y+h/2+16,sub,11,MUT,"middle")
    elif label:
        s+=T(x+w/2,y+h/2+5,label,fs,tc,"middle","700")
    return s
def arr(x1,y1,x2,y2,c=WIRE,w=2.5):
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
            f"<polygon points='{x2},{y2} {x2-9 if x2>x1 else x2+9},{y2-5} {x2-9 if x2>x1 else x2+9},{y2+5}' fill='{c}'/>")
def line(x1,y1,x2,y2,c=WIRE,w=2.5):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
def led(cx,cy,color,lit=True,r=7):
    glow=f"<circle cx='{cx}' cy='{cy}' r='{r+4}' fill='{color}' opacity='0.22'/>" if lit else ""
    fill=color if lit else "#e4e9f1"; stroke=color if lit else "#c3ccdb"
    return glow+f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
def save(name,w,h,body,title):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

W,H=720,270

# ---------- brand LED-panel hero ----------
def brand_hero(name, model, leds, caption):
    # PLC device on the left, brand LED legend on the right (one fault LED lit).
    b = f"<rect x='140' y='64' width='210' height='150' rx='12' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
    b += f"<rect x='158' y='80' width='174' height='42' rx='6' fill='#0f1720'/>" + T(245,108,model,20,'#7ff0c0','middle','700')
    b += "".join(f"<circle cx='{170+k*40}' cy='200' r='4' fill='{BLUE}'/>" for k in range(5))
    b += T(245,152,name,15,INK,'middle','700')
    lx=430; n=len(leds); y0=90
    for i,(lab,col,lit) in enumerate(leds):
        cy=y0+i*32
        b += led(lx,cy,col,lit) + T(lx+16,cy+4,lab,12,INK,'start','700')
    b += T(245,238,caption,12,INK,'middle','700')
    save("rep-loi-"+name.lower().split()[0], W, H, b, f"Đèn báo lỗi trên PLC {name}")

brand_hero("Mitsubishi","FX / Q",
    [("POWER — nguồn OK",GREEN,True),("RUN — không chạy",GREEN,False),
     ("ERROR — lỗi hệ thống",RED,True),("BATT — pin yếu",AMBER,True)],
    "Đọc POWER · RUN · ERROR · BATT để khoanh vùng")
brand_hero("Siemens","S7",
    [("RUN — không sáng",GREEN,False),("STOP — đang STOP",AMBER,True),
     ("ERROR / SF — lỗi",RED,True),("BF — lỗi bus",RED,False)],
    "S7-1200/1500: ERROR · S7-300: SF / BF")
brand_hero("Omron","CJ / CP",
    [("POWER — nguồn OK",GREEN,True),("RUN — không chạy",GREEN,False),
     ("ERR/ALM — lỗi/cảnh báo",RED,True),("COMM — truyền thông",AMBER,False)],
    "POWER · RUN · ERR/ALM · COMM")
brand_hero("Delta","DVP / AS",
    [("POWER — nguồn OK",GREEN,True),("RUN — không chạy",GREEN,False),
     ("ERROR — nhấp nháy",RED,True),("BAT.LOW — pin yếu",AMBER,True)],
    "POWER · RUN · ERROR · BAT.LOW")

# ---------- RS485 Modbus bus wiring ----------
def dev(x,label,sub,accent=BLUE):
    b=box(x,70,120,54,label,"#fff",accent,INK,12.5,sub)
    return b
bus=""
bus+=dev(30,"PLC / Master","Modbus RTU",GREEN)
bus+=dev(300,"Slave 1","biến tần / đồng hồ",BLUE)
bus+=dev(570,"Slave 2","cảm biến / I/O",BLUE)
# two bus lines A/B
ay,by=150,168
bus+=line(60,ay,660,ay,BLUE,2.5)+T(24,ay+4,"A(+)",10.5,BLUE,'start','700')
bus+=line(60,by,660,by,RED,2.5)+T(24,by+4,"B(–)",10.5,RED,'start','700')
# drops from each device to the bus
for x in (90,360,630):
    bus+=line(x,124,x,ay,BLUE,2)
    bus+=line(x+16,124,x+16,by,RED,2)
# terminators 120Ω at both ends
bus+=f"<rect x='40' y='146' width='16' height='26' rx='3' fill='#fff' stroke='{WIRE}'/>"+T(48,140,"120Ω",9.5,MUT,'middle','700')
bus+=f"<rect x='664' y='146' width='16' height='26' rx='3' fill='#fff' stroke='{WIRE}'/>"+T(672,140,"120Ω",9.5,MUT,'middle','700')
# shield to ground
bus+=line(360,by,360,205,STEEL,2)
bus+=line(345,205,375,205,STEEL,2)+line(350,210,370,210,STEEL,2)+line(355,215,365,215,STEEL,2)
bus+=T(390,212,"màn chống nhiễu nối đất 1 đầu",10.5,MUT,'start')
bus+=T(360,238,"Cùng baud · parity · mỗi thiết bị 1 địa chỉ (ID) duy nhất",11,INK,'middle','700')
save("bus-rs485-modbus",W,H,bus,"Đấu bus RS485 Modbus đúng chuẩn")

# ---------- PLC – HMI – SCADA topology ----------
topo=""
topo+=box(40,95,150,70,"PLC","#fff",GREEN,INK,13,"bộ điều khiển")
topo+=box(285,95,150,70,"HMI","#eef3fb",BLUE,INK,13,"màn hình vận hành")
topo+=box(530,95,150,70,"SCADA / PC","#fff",AMBER,INK,13,"giám sát")
topo+=arr(190,130,285,130,BLUE)+T(237,118,"RS485 /",10.5,BLUE,'middle','700')+T(237,150,"Modbus RTU",10.5,MUT,'middle')
topo+=arr(435,130,530,130,AMBER)+T(482,118,"Ethernet /",10.5,AMBER,'middle','700')+T(482,150,"Modbus TCP",10.5,MUT,'middle')
topo+=T(360,205,"Sai baud/ID, sai IP, đứt A/B hay thiếu 120Ω → mất kết nối",11.5,INK,'middle','700')
save("topo-plc-hmi-scada",W,H,topo,"Kết nối PLC – HMI – SCADA")

print("wrote brand heroes (mitsubishi/siemens/omron/delta) + bus-rs485-modbus + topo-plc-hmi-scada")
