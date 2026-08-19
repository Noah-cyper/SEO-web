#!/usr/bin/env python3
# Diagrams for Batch 2 PLC cluster (kiến thức / lập trình / ứng dụng).
# Same light-card house style as gen_diagrams2..7.py.
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
def save(name,w,h,body,title):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

W,H=720,270

# ---- PLC structure / cấu tạo ----
st=""
st+=box(300,110,150,70,"CPU","#eef3fb",BLUE,INK,14,"xử lý logic")
st+=box(300,40,150,44,"Bộ nhớ","#fff",BLUE,INK,12)
st+=line(375,84,375,110,WIRE,2)
st+=box(40,70,150,44,"Nguồn 24VDC","#fff",AMBER,INK,12)
st+=arr(190,92,300,120,AMBER)
st+=box(40,150,150,60,"Ngõ vào (I)","#fff",GREEN,INK,12,"cảm biến, nút")
st+=arr(190,175,300,160,GREEN)
st+=box(560,150,120,60,"Ngõ ra (O)","#fff",GREEN,INK,12,"motor, van")
st+=arr(450,160,560,175,GREEN)
st+=box(300,200,150,44,"Truyền thông","#fff",WIRE,INK,12)
st+=line(375,180,375,200,WIRE,2)
st+=T(360,262,"Nguồn · CPU · Bộ nhớ · I/O · Truyền thông",11.5,INK,'middle','700')
save("cautao-plc",720,290,st,"Cấu tạo cơ bản của một PLC")

# ---- 5 IEC languages ----
langs=[("LAD","Ladder — bậc thang",GREEN),("FBD","khối hàm",BLUE),
       ("ST","văn bản có cấu trúc",AMBER),("SFC","tuần tự",RED),("IL","danh sách lệnh",WIRE)]
lg=""
bw=128
for i,(nm,desc,col) in enumerate(langs):
    if i<3: x=30+i*(bw+12); y=70
    else: x=30+ (i-3)*(bw+12) +70; y=160
    lg+=box(x,y,bw,64,nm,"#fff",col,INK,15,desc)
save("ngon-ngu-plc",W,H,lg,"5 ngôn ngữ lập trình PLC (chuẩn IEC 61131-3)")

# ---- ladder rung ----
lr=""
railL,railR=60,660; y1,y2=90,170
lr+=line(railL,60,railL,200,INK,3)+line(railR,60,railR,200,INK,3)
# rung 1: --| |--|/|--( )--
def contact(x,y,label,no=True):
    s=f"<line x1='{x-22}' y1='{y}' x2='{x-8}' y2='{y}' stroke='{INK}' stroke-width='2.5'/>"
    s+=f"<line x1='{x-8}' y1='{y-12}' x2='{x-8}' y2='{y+12}' stroke='{INK}' stroke-width='2.5'/>"
    s+=f"<line x1='{x+8}' y1='{y-12}' x2='{x+8}' y2='{y+12}' stroke='{INK}' stroke-width='2.5'/>"
    if not no: s+=f"<line x1='{x-8}' y1='{y+12}' x2='{x+8}' y2='{y-12}' stroke='{INK}' stroke-width='2'/>"
    s+=f"<line x1='{x+8}' y1='{y}' x2='{x+22}' y2='{y}' stroke='{INK}' stroke-width='2.5'/>"
    s+=T(x,y-20,label,11,BLUE,'middle','700')
    return s
def coil(x,y,label):
    s=f"<path d='M{x-12} {y-13} A 13 13 0 0 0 {x-12} {y+13}' fill='none' stroke='{GREEN}' stroke-width='2.5'/>"
    s+=f"<path d='M{x+12} {y-13} A 13 13 0 0 1 {x+12} {y+13}' fill='none' stroke='{GREEN}' stroke-width='2.5'/>"
    s+=T(x,y-20,label,11,GREEN,'middle','700')
    return s
lr+=line(railL,y1,150,y1,INK,2.5)+contact(172,y1,"X0")+line(194,y1,300,y1,INK,2.5)+contact(322,y1,"X1",no=False)+line(344,y1,560,y1,INK,2.5)+coil(590,y1,"Y0")+line(603,y1,railR,y1,INK,2.5)
lr+=line(railL,y2,300,y2,INK,2.5)+contact(322,y2,"Y0")+line(344,y2,560,y2,INK,2.5)+coil(590,y2,"Y1")+line(603,y2,railR,y2,INK,2.5)
lr+=T(360,235,"Tiếp điểm thường mở/thường đóng → cuộn dây ngõ ra",11.5,INK,'middle','700')
save("ladder-co-ban",W,H,lr,"Ví dụ chương trình Ladder (LAD)")

# ---- timer timing diagram (ON-delay) ----
tm=""
tm+=T(40,80,"Ngõ vào",11,INK,'start','700')
tm+=line(150,95,260,95,WIRE,1)  # low
tm+=line(260,95,260,65,BLUE,3)+line(260,65,520,65,BLUE,3)+line(520,65,520,95,BLUE,3)+line(520,95,660,95,WIRE,1)
tm+=T(40,150,"Ngõ ra",11,INK,'start','700')
tm+=line(150,165,340,165,WIRE,1)
tm+=line(340,165,340,135,GREEN,3)+line(340,135,520,135,GREEN,3)+line(520,135,520,165,GREEN,3)+line(520,165,660,165,WIRE,1)
tm+=line(260,60,260,170,STEEL,1)+line(340,60,340,170,STEEL,1)
tm+=T(300,120,"T (đặt)",10.5,AMBER,'middle','700')
tm+=f"<line x1='262' y1='185' x2='338' y2='185' stroke='{AMBER}' stroke-width='1.5'/>"
tm+=T(360,235,"Timer ON-delay: ngõ ra bật sau thời gian đặt T",11.5,INK,'middle','700')
save("timer-plc",W,H,tm,"Nguyên lý lệnh Timer (bộ định thời)")

# ---- counter concept ----
cn=""
for k in range(5):
    x=90+k*46
    cn+=line(x,150,x,100,BLUE,3)+line(x,100,x+16,100,BLUE,3)+line(x+16,100,x+16,150,BLUE,3)
cn+=T(150,175,"xung đếm vào",11,MUT,'middle')
cn+=arr(340,125,410,125)
cn+=box(410,95,120,60,"Counter","#eef3fb",BLUE,INK,12,"đếm 1,2,3…")
cn+=arr(530,125,600,125,GREEN)
cn+=box(600,100,80,50,"Ngõ ra","#fff",GREEN,INK,11,"= preset")
cn+=T(360,235,"Đếm đủ giá trị đặt (preset) → bật ngõ ra",11.5,INK,'middle','700')
save("counter-plc",W,H,cn,"Nguyên lý lệnh Counter (bộ đếm)")

# ---- PID loop ----
pd=""
pd+=box(40,110,90,50,"Setpoint","#fff",AMBER,INK,11)
pd+=f"<circle cx='185' cy='135' r='20' fill='#fff' stroke='{WIRE}' stroke-width='2'/>"+T(185,140,"∑",16,INK,'middle','700')
pd+=arr(130,135,163,135)
pd+=arr(205,135,250,135)+T(228,126,"sai lệch",9.5,RED,'middle')
pd+=box(250,110,110,50,"Bộ PID","#eef3fb",BLUE,INK,12)
pd+=arr(360,135,410,135)
pd+=box(410,110,140,50,"Đối tượng","#fff",GREEN,INK,12,"van/động cơ")
pd+=arr(550,135,610,135,GREEN)+box(610,110,70,50,"Ra","#fff",GREEN,INK,11)
# feedback
pd+=line(645,160,645,210,WIRE,2)+line(645,210,185,210,WIRE,2)+arr(185,210,185,157,WIRE)
pd+=T(400,205,"phản hồi từ cảm biến",10.5,MUT,'middle')
pd+=T(360,250,"Vòng kín: so setpoint với phản hồi → PID điều chỉnh",11,INK,'middle','700')
save("pid-plc",720,270,pd,"Nguyên lý điều khiển PID bằng PLC")

# ---- motor control ----
mc=""
mc+=box(40,100,140,64,"PLC","#fff",GREEN,INK,13,"logic start/stop")
mc+=arr(180,132,250,132)
mc+=box(250,100,150,64,"Contactor / VFD","#eef3fb",BLUE,INK,12,"đóng cắt / tốc độ")
mc+=arr(400,132,470,132,AMBER)
mc+=f"<circle cx='560' cy='132' r='40' fill='#fff' stroke='{AMBER}' stroke-width='2.5'/>"+T(560,138,"M",20,INK,'middle','700')
mc+=T(560,195,"động cơ",11,MUT,'middle')
mc+=T(360,235,"PLC điều khiển động cơ qua contactor (ON/OFF) hoặc biến tần (tốc độ)",11,INK,'middle','700')
save("dieu-khien-dong-co-plc",W,H,mc,"PLC điều khiển động cơ")

# ---- PLC + IoT cloud ----
iot=""
iot+=box(30,105,130,60,"PLC","#fff",GREEN,INK,13)
iot+=arr(160,135,220,135)
iot+=box(220,105,140,60,"Gateway/RTU","#eef3fb",BLUE,INK,12,"4G / Ethernet")
iot+=arr(360,135,430,135,AMBER)
iot+=f"<path d='M470 120 q-30 0 -30 22 q-24 0 -14 22 h120 q14 -22 -12 -26 q0 -26 -32 -22 q-10 -14 -32 -18 Z' fill='#fff' stroke='{WIRE}' stroke-width='2'/>"
iot+=T(505,150,"Cloud",12,INK,'middle','700')
iot+=arr(560,140,620,140,GREEN)
iot+=box(620,110,60,60,"Dashboard","#fff",GREEN,INK,10)
iot+=T(360,235,"PLC → gateway → cloud: giám sát & điều khiển từ xa",11.5,INK,'middle','700')
save("plc-iot",W,H,iot,"PLC kết nối IoT / giám sát từ xa")

# ---- control panel layout ----
cp=""
cp+=f"<rect x='40' y='50' width='640' height='190' rx='8' fill='#fff' stroke='{WIRE}' stroke-width='2'/>"
cp+=box(60,70,120,50,"MCB / CB","#fff",RED,INK,11,"bảo vệ")
cp+=box(60,140,120,50,"Nguồn 24VDC","#fff",AMBER,INK,11)
cp+=box(210,70,150,120,"PLC","#eef3fb",BLUE,INK,14,"+ module I/O")
cp+=box(390,70,120,50,"Relay trung gian","#fff",GREEN,INK,10.5)
cp+=box(390,140,120,50,"Terminal","#fff",WIRE,INK,11,"đấu dây")
cp+=box(540,70,120,120,"HMI","#fff",BLUE,INK,13,"trên cánh tủ")
cp+=T(360,260,"Bố trí tủ điện PLC: bảo vệ · nguồn · PLC · relay · terminal · HMI",11,INK,'middle','700')
save("tu-dien-plc",720,285,cp,"Bố trí tủ điện điều khiển PLC")

print("wrote batch-2 diagrams: cautao-plc, ngon-ngu-plc, ladder-co-ban, timer-plc, counter-plc, pid-plc, dieu-khien-dong-co-plc, plc-iot, tu-dien-plc")
