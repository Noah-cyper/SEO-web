#!/usr/bin/env python3
# Flowline (đo mức) diagrams: representative / principle / application for level sensors & switches.
import os
OUT="/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT,exist_ok=True)
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
        s+=T(x+w/2,y+h/2-3,label,fs,tc,"middle","700")+T(x+w/2,y+h/2+15,sub,11,MUT,"middle")
    elif label:
        s+=T(x+w/2,y+h/2+5,label,fs,tc,"middle","700")
    return s
def arr(x1,y1,x2,y2,c=WIRE,w=2.5):
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
            f"<polygon points='{x2},{y2} {x2-9},{y2-5} {x2-9},{y2+5}' fill='{c}'/>")
def save(name,w,h,body,title): open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

# a tank with liquid + ultrasonic sensor on top
def tank(x,y,w,h,fill=0.45,liquid="#bcd6f5"):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='4' fill='#eef3fb' stroke='{WIRE}' stroke-width='2'/>"
    lh=int(h*fill); s+=f"<rect x='{x+2}' y='{y+h-lh}' width='{w-4}' height='{lh-2}' rx='2' fill='{liquid}'/>"
    return s
def sensor(cx,y,w=54,h=40,accent=BLUE,label=""):
    s=f"<rect x='{cx-w/2}' y='{y}' width='{w}' height='{h}' rx='7' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<rect x='{cx-10}' y='{y+h}' width='20' height='10' fill='{STEEL}'/>"  # process fitting
    if label: s+=T(cx,y-8,label,11.5,INK,"middle","700")
    return s
def waves(cx,y1,y2,c=BLUE):
    # 3 downward sonar arcs between sensor bottom and liquid
    s=""
    for k,yy in enumerate([y1+ (y2-y1)*f for f in (0.25,0.5,0.75)]):
        s+=f"<path d='M{cx-26} {yy} q26 22 52 0' fill='none' stroke='{c}' stroke-width='2' opacity='{0.9-0.2*k}'/>"
    return s

W,H=720,270

# ---------- REPRESENTATIVE ----------
# EchoPod / EchoTouch style: transmitter on top of a chemical tank
save("rep-level",W,H,
  tank(300,95,120,110,0.4)
  +sensor(360,55,60,42,BLUE,"EchoPod")
  +f"<rect x='348' y='97' width='24' height='12' fill='{STEEL}'/>"
  +waves(360,110,150+15)
  +arr(422,76,540,76,GREEN)+T(500,68,'4–20mA',10.5,GREEN,'middle','700')
  +T(360,230,'Cảm biến siêu âm đo mức (Flowline)',13,INK,'middle','700'),"Hình đại diện")

# EchoTouch intrinsically safe (hazardous area badge)
save("rep-uslevel",W,H,
  tank(300,95,120,110,0.4,"#f6ddc4")
  +sensor(360,55,60,42,AMBER,"EchoTouch")
  +f"<rect x='348' y='97' width='24' height='12' fill='{STEEL}'/>"
  +waves(360,110,150+15,AMBER)
  +f"<rect x='470' y='95' width='150' height='40' rx='8' fill='#fff' stroke='{RED}' stroke-width='2'/>"
  +T(545,120,'Ex — an toàn tia lửa',11.5,RED,'middle','700')
  +T(360,230,'Cảm biến siêu âm phòng nổ (EchoTouch)',13,INK,'middle','700'),"Hình đại diện")

# EchoSpan loop-powered (2-wire) transmitter
save("rep-loop-level",W,H,
  tank(300,95,120,110,0.45)
  +sensor(360,55,58,40,BLUE,"EchoSpan")
  +f"<rect x='348' y='95' width='24' height='12' fill='{STEEL}'/>"
  +waves(360,108,150+15)
  +T(500,70,'2 dây (loop)',12,MUT,'start')
  +arr(419,90,560,90,BLUE)+T(505,82,'4–20mA',10.5,BLUE,'middle','700')
  +T(360,230,'Transmitter siêu âm 2 dây (loop-powered)',13,INK,'middle','700'),"Hình đại diện")

# point-level switch (float / ultrasonic gap)
save("rep-switch",W,H,
  tank(300,95,120,110,0.55)
  +f"<circle cx='360' cy='60' r='16' fill='#fff' stroke='{GREEN}' stroke-width='2.5'/>"
  +f"<rect x='352' y='75' width='16' height='60' fill='{STEEL}'/>"
  +f"<ellipse cx='360' cy='150' rx='26' ry='14' fill='#cfe0f7' stroke='{BLUE}' stroke-width='2'/>"
  +T(470,120,'ON / OFF',12,GREEN,'start','700')
  +T(470,142,'khi chạm ngưỡng',11,MUT,'start')
  +T(360,230,'Công tắc báo mức (Switch-Tek)',13,INK,'middle','700'),"Hình đại diện")

# ---------- PRINCIPLE ----------
# time-of-flight ultrasonic
save("prin-ultrasonic",W,H,
  sensor(200,70,64,44,BLUE,"đầu phát/thu")
  +f"<line x1='200' y1='180' x2='620' y2='180' stroke='{BLUE}' stroke-width='3'/>"
  +T(410,198,'mặt chất lỏng',11,MUT,'middle')
  +arr(200,116,200,175,AMBER)+T(150,150,'phát',10.5,AMBER,'start','700')
  +arr(240,175,240,116,GREEN)+T(258,150,'phản xạ về',10.5,GREEN,'start','700')
  +T(410,80,'khoảng cách = tốc độ âm × thời gian ÷ 2',12,INK,'middle','700')
  +T(410,105,'mức = chiều cao bồn − khoảng cách đo được',11.5,MUT,'middle')
  ,"Nguyên lý siêu âm: đo thời gian sóng dội (time-of-flight)")

# switch principle (setpoint relay)
save("prin-switch",W,H,
  box(230,95,140,60,'Cảm biến điểm','#fff',BLUE,INK,12,'phao/siêu âm')
  +arr(370,125,430,125)
  +box(430,95,120,60,'So ngưỡng','#eef3fb',BLUE,INK,12,'setpoint')
  +arr(550,125,610,125,RED)+T(650,120,'relay',10.5,RED,'middle','700')
  +T(410,185,'chạm mức cao/thấp → đóng/mở tiếp điểm điều khiển bơm/van',11,MUT,'middle')
  ,"Nguyên lý: phát hiện mức điểm → đóng/ngắt relay")

# ---------- APPLICATION ----------
# multiple chemical tanks monitored
save("app-level",W,H,
  ''.join(tank(70+i*130,100,90,100,f) + sensor(115+i*130,68,44,32,BLUE)
          for i,f in enumerate([0.6,0.35,0.75]))
  +arr(470,150,520,150,GREEN)+T(475,142,'4–20mA',10.5,GREEN,'middle','700')
  +box(520,120,150,60,'PLC / SCADA','#fff',GREEN,INK,12,'giám sát mức')
  +T(240,225,'kiểm soát mức bồn hoá chất / nước / dầu',12,MUT,'middle')
  ,"Ứng dụng: giám sát mức nhiều bồn chứa")

# hazardous-area application
save("app-hazard",W,H,
  f"<rect x='40' y='70' width='300' height='150' rx='8' fill='#fdeede' stroke='{RED}' stroke-width='2'/>"
  +T(190,92,'Khu vực nguy hiểm (Ex)',12,RED,'middle','700')
  +tank(120,110,100,95,0.45,"#f6ddc4")+sensor(170,78,44,30,AMBER)
  +f"<rect x='340' y='130' width='80' height='40' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
  +T(380,155,'barrier',11,BLUE,'middle','700')
  +arr(224,150,340,150,AMBER)+arr(420,150,520,150,GREEN)
  +box(520,120,150,60,'Phòng điều khiển','#fff',GREEN,INK,12,'an toàn')
  +T(380,110,'rào cách ly an toàn tia lửa',10.5,MUT,'middle')
  ,"Ứng dụng: đo mức trong môi trường dễ cháy nổ")

# switch application: pump control
save("app-switch",W,H,
  tank(90,95,130,120,0.35)
  +f"<circle cx='155' cy='70' r='14' fill='#fff' stroke='{GREEN}' stroke-width='2.5'/>"
  +f"<rect x='148' y='84' width='14' height='40' fill='{STEEL}'/>"
  +T(155,150,'mức thấp',10.5,RED,'middle','700')
  +arr(230,150,320,150,BLUE)
  +box(320,120,120,60,'Bộ điều khiển','#eef3fb',BLUE,INK,12,'/ relay')
  +arr(440,150,520,150,GREEN)
  +f"<circle cx='575' cy='150' r='34' fill='#fff' stroke='{GREEN}' stroke-width='2.5'/>"+T(575,155,'BƠM',12,INK,'middle','700')
  +T(360,225,'tự bật/tắt bơm theo mức — chống tràn & chạy khô',12,MUT,'middle')
  ,"Ứng dụng: điều khiển bơm chống tràn / chạy khô")

print("flowline diagrams saved. total:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]))
