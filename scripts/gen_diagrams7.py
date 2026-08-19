#!/usr/bin/env python3
# Diagrams for the 20-article PLC cluster (brand heroes + symptom/guide/connect diagrams).
# Same light-card house style as gen_diagrams2..6.py.
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
def line(x1,y1,x2,y2,c=WIRE,w=2.5,dash=""):
    d=f"stroke-dasharray='{dash}'" if dash else ""
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}' {d}/>"
def led(cx,cy,color,lit=True,r=7):
    glow=f"<circle cx='{cx}' cy='{cy}' r='{r+4}' fill='{color}' opacity='0.22'/>" if lit else ""
    fill=color if lit else "#e4e9f1"; stroke=color if lit else "#c3ccdb"
    return glow+f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
def batt(x,y,c=AMBER):
    return (f"<rect x='{x}' y='{y}' width='34' height='20' rx='3' fill='#fff' stroke='{c}' stroke-width='2'/>"
            f"<rect x='{x+34}' y='{y+6}' width='4' height='8' fill='{c}'/>"+T(x+17,y+14,"+",11,c,'middle','700'))
def cross(cx,cy,c=RED,r=9):
    return (f"<line x1='{cx-r}' y1='{cy-r}' x2='{cx+r}' y2='{cy+r}' stroke='{c}' stroke-width='3'/>"
            f"<line x1='{cx-r}' y1='{cy+r}' x2='{cx+r}' y2='{cy-r}' stroke='{c}' stroke-width='3'/>")
def check(cx,cy,c=GREEN,r=9):
    return f"<path d='M{cx-r} {cy} l{r*0.7} {r*0.8} l{r*1.3} -{r*1.6}' fill='none' stroke='{c}' stroke-width='3'/>"
def save(name,w,h,body,title):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

W,H=720,270

# ---------- brand LED-panel hero (shared) ----------
def brand_hero(name, model, leds, caption):
    b = f"<rect x='140' y='64' width='210' height='150' rx='12' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
    b += f"<rect x='158' y='80' width='174' height='42' rx='6' fill='#0f1720'/>" + T(245,108,model,20,'#7ff0c0','middle','700')
    b += "".join(f"<circle cx='{170+k*40}' cy='200' r='4' fill='{BLUE}'/>" for k in range(5))
    b += T(245,152,name,15,INK,'middle','700')
    lx=430; y0=90
    for i,(lab,col,lit) in enumerate(leds):
        cy=y0+i*32
        b += led(lx,cy,col,lit) + T(lx+16,cy+4,lab,12,INK,'start','700')
    b += T(245,238,caption,12,INK,'middle','700')
    save("rep-loi-"+name.lower().split()[0], W, H, b, f"Đèn báo lỗi trên PLC {name}")

brand_hero("LS","XGB / XGT",
    [("PWR — nguồn OK",GREEN,True),("RUN — không chạy",GREEN,False),
     ("STOP — đang dừng",AMBER,True),("ERR — lỗi",RED,True)],
    "PWR · RUN · STOP · ERR — công cụ XG5000")
brand_hero("Schneider","Modicon",
    [("RUN — không chạy",GREEN,False),("ERR — lỗi",RED,True),
     ("I/O — lỗi vào/ra",AMBER,True),("MB/NS — mạng",AMBER,False)],
    "M221/M241/M340 — EcoStruxure")
brand_hero("Panasonic","FP",
    [("RUN — không chạy",GREEN,False),("PROG — chế độ lập trình",AMBER,True),
     ("ERROR/ALARM — lỗi",RED,True),("—",STEEL,False)],
    "FP0/FP-X/FPΣ — công cụ FPWIN")
brand_hero("Allen-Bradley","Logix",
    [("OK — đỏ nhấp nháy",RED,True),("RUN — không chạy",GREEN,False),
     ("FORCE — ép I/O",AMBER,False),("I/O — lỗi module",RED,True)],
    "Micro/Compact/ControlLogix — Studio 5000")
brand_hero("Fatek","FBs / FB",
    [("POWER — nguồn OK",GREEN,True),("RUN — không chạy",GREEN,False),
     ("ERR — lỗi",RED,True),("—",STEEL,False)],
    "FBs/FB — công cụ WinProladder")

# ---------- power chain ----------
pw=""
pw+=box(24,96,150,58,"Nguồn 220VAC","#fff",AMBER,INK,12.5,"lưới điện")
pw+=arr(174,125,214,125)
pw+=box(214,96,140,58,"Cầu chì / CB","#fff",WIRE,INK,12.5,"bảo vệ")
pw+=arr(354,125,394,125)
pw+=box(394,96,150,58,"Bộ nguồn 24VDC","#eef3fb",BLUE,INK,12.5,"cấp điều khiển")
pw+=arr(544,125,584,125)
pw+=box(584,96,112,58,"PLC","#fff",GREEN,INK,13)
pw+=T(360,196,"Mất nguồn · đứt cầu chì · sụt áp 24V do quá tải · đấu ngược cực",11.5,INK,'middle','700')
pw+=cross(284,80,RED,8)+cross(469,80,RED,8)
save("power-plc",W,H,pw,"Chuỗi cấp nguồn cho PLC & điểm hay lỗi")

# ---------- battery / memory ----------
bm=""
bm+=f"<rect x='60' y='80' width='250' height='120' rx='12' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
bm+=box(80,100,120,50,"Bộ nhớ RAM","#eef3fb",BLUE,INK,12,"chứa chương trình")
bm+=batt(120,168,AMBER)+T(200,182,"pin nuôi RAM",11,MUT,'start')
bm+=T(185,96,"PLC",12,INK,'middle','700')
bm+=arr(310,140,380,140,RED)
bm+=box(380,105,300,70,"Pin yếu + mất điện","#fff",RED,INK,12.5,"→ MẤT chương trình")
bm+=T(360,215,"Khắc phục: BACKUP + thay pin khi PLC còn điện · dùng dòng Flash/EEPROM",11,INK,'middle','700')
save("pin-nho-plc",W,H,bm,"Vì sao PLC mất chương trình khi pin yếu")

# ---------- PC <-> PLC connect ----------
pc=""
pc+=f"<rect x='60' y='90' width='150' height='90' rx='8' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
pc+=f"<rect x='72' y='102' width='126' height='55' rx='4' fill='#0f1720'/>"+T(135,135,"GX / TIA…",13,'#7ff0c0','middle','700')
pc+=T(135,196,"Máy tính (phần mềm)",12,INK,'middle','700')
pc+=box(510,95,150,80,"PLC","#fff",GREEN,INK,13)
pc+=line(210,135,510,135,WIRE,3)
pc+=T(360,120,"USB / RS232 / Ethernet",11.5,BLUE,'middle','700')
pc+=T(360,152,"cần đúng cổng · driver · chọn đúng model",11,MUT,'middle')
save("ket-noi-pc-plc",W,H,pc,"Kết nối máy tính ↔ PLC để nạp chương trình")

# ---------- sink/source I/O ----------
io=""
# NPN (sink)
io+=T(180,62,"Cảm biến NPN (sink)",12.5,INK,'middle','700')
io+=box(60,80,110,60,"Cảm biến","#fff",BLUE)
io+=box(250,80,120,60,"Ngõ vào PLC","#eef3fb",GREEN,INK,11)
io+=line(170,100,250,100,WIRE,2.5)+T(210,92,"OUT",10,MUT,'middle')
io+=line(170,125,250,125,AMBER,2.5)+T(210,138,"COM = +V",10,AMBER,'middle','700')
# PNP (source)
io+=T(540,62,"Cảm biến PNP (source)",12.5,INK,'middle','700')
io+=box(420,80,110,60,"Cảm biến","#fff",BLUE)
io+=box(610,80,90,60,"Ngõ vào","#eef3fb",GREEN,INK,11)
io+=line(530,100,610,100,WIRE,2.5)+T(570,92,"OUT",10,MUT,'middle')
io+=line(530,125,610,125,WIRE,2.5)+T(570,138,"COM = 0V",10,WIRE,'middle','700')
io+=T(360,190,"Sai kiểu Sink/Source (NPN/PNP) → ngõ vào không tác động",11.5,RED,'middle','700')
io+=T(360,215,"Kiểm tra: đèn Input, điện áp tại terminal, đúng chân COM",11,MUT,'middle')
save("io-sink-source",W,H,io,"Đấu ngõ vào PLC: NPN (sink) và PNP (source)")

# ---------- noise / grounding ----------
ns=""
ns+=box(40,90,140,64,"Biến tần / VFD","#fff",RED,INK,12,"nguồn nhiễu")
ns+=''.join(f"<path d='M{190+k*10} {100+k*6} q10 -8 0 -16' fill='none' stroke='{RED}' stroke-width='2' opacity='{0.9-0.2*k}'/>" for k in range(3))
ns+=box(300,70,150,50,"Dây động lực","#fdeede",AMBER,INK,11)
ns+=box(300,140,150,50,"Dây tín hiệu","#eef3fb",BLUE,INK,11)
ns+=T(455,95,"đi tách máng",10.5,MUT,'start')+T(455,165,"cáp xoắn có màn",10.5,MUT,'start')
ns+=box(560,105,120,54,"PLC","#fff",GREEN,INK,13)
ns+=line(620,159,620,195,STEEL,2.5)
ns+=line(605,195,635,195,STEEL,2.5)+line(610,200,630,200,STEEL,2.5)+line(615,205,625,205,STEEL,2.5)
ns+=T(620,222,"nối đất",10,MUT,'middle')
ns+=T(300,222,"Tách dây · cáp shielded · nối đất tốt · lọc nhiễu VFD",11.5,INK,'middle','700')
save("chong-nhieu-plc",W,H,ns,"Chống nhiễu & nối đất cho PLC")

# ---------- backup / restore ----------
br=""
br+=box(60,95,150,80,"PLC","#fff",GREEN,INK,13,"chương trình đang chạy")
br+=box(510,95,150,80,"Máy tính","#eef3fb",BLUE,INK,13,"file .gxw/.ap…")
br+=arr(210,120,510,120,BLUE)+T(360,110,"Upload = đọc về PC (BACKUP)",11,BLUE,'middle','700')
br+=arr(510,155,210,155,AMBER)+T(360,175,"Download = nạp xuống (RESTORE)",11,AMBER,'middle','700')
br+=T(360,215,"Luôn backup trước khi sửa · lưu kèm ghi chú phiên bản",11.5,INK,'middle','700')
save("backup-restore-plc",W,H,br,"Backup & Restore chương trình PLC")

# ---------- PLC <-> VFD (Modbus) ----------
vf=""
vf+=box(40,95,150,70,"PLC (Master)","#fff",GREEN,INK,12.5,"Modbus RTU")
vf+=arr(190,130,300,130,BLUE)+T(245,118,"RS485",10.5,BLUE,'middle','700')
vf+=box(300,95,150,70,"Biến tần","#eef3fb",BLUE,INK,12.5,"điều khiển tốc độ")
vf+=arr(450,130,540,130,AMBER)
vf+=f"<circle cx='600' cy='130' r='34' fill='#fff' stroke='{AMBER}' stroke-width='2.5'/>"+T(600,135,"M",16,INK,'middle','700')
vf+=T(600,180,"động cơ",11,MUT,'middle')
vf+=T(360,210,"Đặt tốc độ, chạy/dừng, đọc dòng–tần số qua Modbus",11.5,INK,'middle','700')
save("plc-bien-tan",W,H,vf,"Kết nối PLC ↔ biến tần qua Modbus RS485")

# ---------- expand I/O ----------
ex=""
ex+=box(40,90,120,80,"PLC CPU","#fff",GREEN,INK,12.5)
# local expansion modules
for i in range(3):
    ex+=f"<rect x='{175+i*55}' y='90' width='48' height='80' rx='6' fill='#eef3fb' stroke='{BLUE}' stroke-width='2'/>"
ex+=T(230,182,"module mở rộng gắn cạnh",10.5,MUT,'middle')
ex+=arr(345,130,430,130,AMBER)+T(388,118,"Modbus",10,AMBER,'middle','700')
# remote I/O
for i in range(3):
    ex+=f"<rect x='{450+i*55}' y='90' width='48' height='80' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
ex+=T(505,182,"remote I/O (Z-PC) từ xa",10.5,MUT,'middle')
ex+=T(360,215,"Hết chân I/O → gắn module mở rộng hoặc remote I/O qua Modbus",11.5,INK,'middle','700')
save("mo-rong-io-plc",W,H,ex,"Mở rộng I/O cho PLC: module & remote I/O")

# ---------- genuine vs fake ----------
gf=""
gf+=box(40,74,300,120,"","#eef7f0",GREEN)
gf+=T(190,98,"Hàng chính hãng",13.5,GREEN,'middle','700')
gf+=check(66,128)+T(86,132,"Tem/nhãn, mã model chuẩn",11.5,INK,'start')
gf+=check(66,162)+T(86,166,"CO/CQ, hóa đơn VAT",11.5,INK,'start')
gf+=box(380,74,300,120,"","#fdeede",RED)
gf+=T(530,98,"Hàng giả / trôi nổi",13.5,RED,'middle','700')
gf+=cross(406,128)+T(426,132,"Không tem, mã mờ/sai",11.5,INK,'start')
gf+=cross(406,162)+T(426,166,"Không CO/CQ, lỗi vặt sớm",11.5,INK,'start')
gf+=T(360,224,"FX3U và nhiều PLC bị làm giả — mua nguồn có kiểm tra, CO/CQ",11.5,INK,'middle','700')
save("plc-that-gia",W,H,gf,"Phân biệt PLC chính hãng và hàng giả")

print("wrote 5 brand heroes + power/pin/pc/io/noise/backup/vfd/expand/fake diagrams")
