#!/usr/bin/env python3
# Flowline mở rộng: radar, radar dẫn sóng (GWR), áp suất thủy tĩnh, bộ điều khiển/hiển thị.
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
def tank(x,y,w,h,fill=0.45,liquid="#bcd6f5"):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='4' fill='#eef3fb' stroke='{WIRE}' stroke-width='2'/>"
    lh=int(h*fill); s+=f"<rect x='{x+2}' y='{y+h-lh}' width='{w-4}' height='{lh-2}' rx='2' fill='{liquid}'/>"
    return s

W,H=720,270

# ---- radar (non-contact) representative: horn antenna on tank ----
save("rep-radar",W,H,
  tank(300,95,120,110,0.4)
  +f"<rect x='340' y='52' width='40' height='26' rx='5' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +f"<path d='M345 78 L335 108 L385 108 L375 78 Z' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"  # horn
  +''.join(f"<path d='M{338-4*k} {112+14*k} q22 12 44 0' fill='none' stroke='{AMBER}' stroke-width='2' opacity='{0.9-0.2*k}'/>" for k in range(3))
  +arr(380,64,540,64,GREEN)+T(500,56,'4–20mA',10.5,GREEN,'middle','700')
  +T(360,230,'Cảm biến radar đo mức (EchoWave)',13,INK,'middle','700'),"Hình đại diện")

# ---- guided-wave radar representative: probe rod into liquid ----
save("rep-gwr",W,H,
  tank(300,95,140,110,0.45)
  +f"<rect x='348' y='55' width='44' height='28' rx='5' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +f"<line x1='370' y1='83' x2='370' y2='198' stroke='{STEEL}' stroke-width='4'/>"  # probe
  +''.join(f"<circle cx='370' cy='{100+18*k}' r='6' fill='none' stroke='{AMBER}' stroke-width='1.6' opacity='0.7'/>" for k in range(5))
  +T(470,120,'sóng chạy dọc',11,MUT,'start')+T(470,138,'thanh dò',11,MUT,'start')
  +T(360,230,'Radar dẫn sóng (EchoPulse – GWR)',13,INK,'middle','700'),"Hình đại diện")

# ---- radar principle ----
save("prin-radar",W,H,
  f"<rect x='170' y='70' width='60' height='34' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"+T(200,92,'radar',11,INK,'middle','700')
  +f"<line x1='200' y1='180' x2='620' y2='180' stroke='{BLUE}' stroke-width='3'/>"+T(410,198,'mặt chất lỏng',11,MUT,'middle')
  +arr(190,106,190,175,AMBER)+T(150,150,'phát',10.5,AMBER,'start','700')
  +arr(230,175,230,106,GREEN)+T(250,150,'phản xạ',10.5,GREEN,'start','700')
  +T(410,84,'sóng vô tuyến — không bị ảnh hưởng hơi, bụi, nhiệt',12,INK,'middle','700')
  +T(410,108,'mức = chiều cao bồn − khoảng cách đo',11.5,MUT,'middle')
  ,"Nguyên lý radar: đo thời gian sóng vô tuyến phản xạ")

# ---- hydrostatic / submersible representative ----
save("rep-submersible",W,H,
  tank(280,70,180,150,0.62)
  +f"<line x1='370' y1='60' x2='370' y2='188' stroke='{WIRE}' stroke-width='2.5'/>"  # cable
  +f"<rect x='356' y='188' width='28' height='30' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"  # probe at bottom
  +T(500,110,'thả chìm đáy bồn',11,MUT,'start')
  +arr(370,60,520,60,GREEN)+T(490,52,'4–20mA',10.5,GREEN,'middle','700')
  +T(360,245,'Cảm biến áp suất thủy tĩnh (DeltaSpan)',13,INK,'middle','700'),"Hình đại diện")

# ---- hydrostatic principle: P = rho*g*h ----
save("prin-hydrostatic",W,H,
  tank(120,70,150,160,0.7)
  +f"<line x1='195' y1='95' x2='195' y2='205' stroke='{RED}' stroke-width='2' stroke-dasharray='5 4'/>"
  +f"<rect x='182' y='205' width='26' height='22' rx='5' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +T(300,120,'áp suất tại đáy tỉ lệ với chiều cao cột chất lỏng',12,INK,'start','700')
  +T(300,150,'P = ρ · g · h   →   suy ra mức h',13,BLUE,'start','700')
  +T(300,178,'ρ: khối lượng riêng · g: trọng lực · h: chiều cao',11,MUT,'start')
  +arr(300,205,470,205,GREEN)+T(385,197,'4–20mA',10.5,GREEN,'middle','700')
  ,"Nguyên lý thủy tĩnh: đo áp đáy → tính mức")

# ---- controller / display representative ----
save("rep-controller",W,H,
  f"<rect x='250' y='70' width='220' height='130' rx='10' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +f"<rect x='272' y='90' width='176' height='46' rx='6' fill='#0f1720'/>"+T(360,124,'75.0 %',24,'#7ff0c0','middle','700')
  +''.join(f"<circle cx='{300+k*40}' cy='170' r='9' fill='{[GREEN,AMBER,RED,BLUE][k]}'/>" for k in range(4))
  +T(360,235,'Bộ điều khiển / hiển thị mức',13,INK,'middle','700'),"Hình đại diện")

# ---- application: controller drives pumps + alarm ----
save("app-control",W,H,
  tank(70,95,110,115,0.5)
  +f"<rect x='95' y='60' width='60' height='30' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"+T(125,80,'cảm biến',10,INK,'middle','700')
  +arr(180,150,250,150,BLUE)
  +box(250,110,150,80,'Bộ điều khiển','#eef3fb',BLUE,INK,12,'LevelTouch')
  +arr(400,130,470,130,GREEN)+f"<circle cx='515' cy='130' r='26' fill='#fff' stroke='{GREEN}' stroke-width='2.5'/>"+T(515,134,'BƠM',11,INK,'middle','700')
  +arr(400,175,470,175,RED)+f"<rect x='475' y='160' width='90' height='30' rx='6' fill='#fff' stroke='{RED}'/>"+T(520,180,'còi/đèn',10.5,RED,'middle','700')
  +T(300,225,'điều khiển nhiều bơm & cảnh báo theo mức',12,MUT,'middle')
  ,"Ứng dụng: điều khiển bơm & cảnh báo theo mức")

print("flowline+ diagrams saved. total svg:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]))
