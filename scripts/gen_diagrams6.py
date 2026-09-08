#!/usr/bin/env python3
# Renepoly (BESS · microgrid · energy storage) diagrams — 5 vai trò/bài: rep · prin · spec · app · compare
import os
OUT="/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT,exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
GRN="#0f9d58"; BLUE="#1f6feb"; AMB="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"; VIO="#6b4fd8"; TEAL="#0e8f8f"
F="font-family='Segoe UI,Roboto,Arial,sans-serif'"

def frame(w,h,body,title=""):
    t=f"<text x='20' y='30' {F} font-size='16' font-weight='700' fill='{INK}'>{title}</text>" if title else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='100%' height='auto' role='img'>"
            f"<rect x='1' y='1' width='{w-2}' height='{h-2}' rx='14' fill='{BG}' stroke='{BD}'/>{t}{body}</svg>")
def T(x,y,t,s=12,c=INK,a="start",w="400"):
    return f"<text x='{x}' y='{y}' {F} font-size='{s}' font-weight='{w}' fill='{c}' text-anchor='{a}'>{t}</text>"
def box(x,y,w,h,label="",fill="#fff",stroke=BLUE,tc=INK,fs=13,sub=""):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='9' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
    if label and sub: s+=T(x+w/2,y+h/2-3,label,fs,tc,"middle","700")+T(x+w/2,y+h/2+15,sub,11,MUT,"middle")
    elif label: s+=T(x+w/2,y+h/2+5,label,fs,tc,"middle","700")
    return s
def arr(x1,y1,x2,y2,c=WIRE,w=2.5,dash=""):
    d=f"stroke-dasharray='{dash}'" if dash else ""
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}' {d}/>"
            f"<polygon points='{x2},{y2} {x2-9},{y2-5} {x2-9},{y2+5}' fill='{c}'/>")
def line(x1,y1,x2,y2,c=WIRE,w=2.5):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
def save(name,w,h,body,title): open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

# --- building blocks ---
def cabinet(x,y,w=110,h=140,label="BESS",accent=GRN,soc=0.7):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<rect x='{x+10}' y='{y+12}' width='{w-20}' height='16' rx='3' fill='#0f1720'/>"
    s+=T(x+w/2,y+25,"EMS",10,"#7ff0c0","middle","700")
    for k in range(3):
        yy=y+38+k*30
        s+=f"<rect x='{x+12}' y='{yy}' width='{w-24}' height='22' rx='3' fill='#e8f5ee' stroke='{accent}'/>"
        s+=f"<rect x='{x+14}' y='{yy+2}' width='{int((w-28)*soc)}' height='18' rx='2' fill='{accent}' opacity='0.55'/>"
    s+=T(x+w/2,y+h-8,label,12,INK,"middle","700")
    return s
def container(x,y,w=210,h=100,label="Container BESS",accent=TEAL):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='6' fill='#eef6f6' stroke='{accent}' stroke-width='2.5'/>"
    for k in range(7): s+=f"<line x1='{x+14+k*((w-28)/6)}' y1='{y+8}' x2='{x+14+k*((w-28)/6)}' y2='{y+h-22}' stroke='{accent}' stroke-width='1.4' opacity='0.5'/>"
    s+=T(x+w/2,y+h-8,label,12,INK,"middle","700")
    return s
def battery(cx,cy,w=44,h=26,accent=GRN,soc=0.75):
    s=f"<rect x='{cx-w/2}' y='{cy-h/2}' width='{w}' height='{h}' rx='4' fill='#fff' stroke='{accent}' stroke-width='2'/>"
    s+=f"<rect x='{cx+w/2}' y='{cy-5}' width='4' height='10' rx='1.5' fill='{accent}'/>"
    s+=f"<rect x='{cx-w/2+3}' y='{cy-h/2+3}' width='{(w-6)*soc}' height='{h-6}' rx='2' fill='{accent}' opacity='0.6'/>"
    return s
def solar(x,y,w=90,h=54,accent=BLUE):
    s=f"<polygon points='{x},{y+h} {x+16},{y} {x+w+16},{y} {x+w},{y+h}' fill='#e4edfb' stroke='{accent}' stroke-width='2'/>"
    for k in range(3): s+=f"<line x1='{x+6+k*28}' y1='{y+h}' x2='{x+22+k*28}' y2='{y}' stroke='{accent}' stroke-width='1.3'/>"
    return s
def grid_tower(x,y,c=STEEL):
    return (f"<path d='M{x} {y+56} L{x+16} {y} L{x+32} {y+56}' fill='none' stroke='{c}' stroke-width='2.5'/>"
            f"<line x1='{x+6}' y1='{y+20}' x2='{x+26}' y2='{y+20}' stroke='{c}' stroke-width='2'/>"
            f"<line x1='{x+2}' y1='{y+36}' x2='{x+30}' y2='{y+36}' stroke='{c}' stroke-width='2'/>")
def factory(x,y,c=STEEL):
    return (f"<path d='M{x} {y+44} L{x} {y+18} L{x+22} {y+30} L{x+22} {y+18} L{x+44} {y+30} L{x+44} {y+44} Z' "
            f"fill='#e6ecf5' stroke='{c}' stroke-width='2'/>")
def inverter(x,y,w=90,h=70,accent=AMB,label="PCS"):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<path d='M{x+16} {y+40} q10 -20 20 0 q10 20 20 0' fill='none' stroke='{accent}' stroke-width='2.2'/>"
    s+=T(x+w/2,y+h-10,label,12,INK,"middle","700")
    return s

W,H=720,290

# ================= REPRESENTATIVE =================
save("rep-bess-cabinet",W,H, cabinet(305,70,110,150,"Tủ BESS ngoài trời")
  +T(470,120,"IP55 · làm mát",11.5,MUT)+T(470,142,"bằng chất lỏng",11.5,MUT)
  +T(200,120,"100 kW",12,GRN,"end","700")+T(200,142,"215 kWh",12,GRN,"end","700")
  +T(360,250,"Tủ lưu trữ năng lượng tích hợp (All-in-One)",13,INK,"middle","700"),"Hình đại diện")

save("rep-bess-container",W,H, container(250,95,230,110,"Container BESS 20ft")
  +T(360,232,"Container lưu trữ năng lượng tới 5 MWh",13,INK,"middle","700")
  +T(150,140,"BMS · PCS",11.5,MUT,"end")+T(150,162,"PCCC · HVAC",11.5,MUT,"end"),"Hình đại diện")

save("rep-ems-renepoly",W,H,
  box(230,80,140,80,"EMS Controller","#eef4fc",VIO,INK,12,"bộ điều khiển")
  +box(400,80,120,80,"Màn hình HMI","#fff",BLUE,INK,11,"tại chỗ")
  +box(400,175,120,55,"4G Router","#fff",AMB,INK,11,"")
  +arr(370,120,400,120)+line(290,160,290,202)+arr(290,202,400,202)
  +T(360,265,"Bộ EMS: điều khiển · hiển thị · truyền thông",13,INK,"middle","700"),"Hình đại diện")

save("rep-pcs-renepoly",W,H, inverter(300,90,130,110,AMB,"PCS")
  +T(190,130,"DC",13,GRN,"end","700")+arr(200,145,300,145,GRN)
  +arr(430,145,540,145,BLUE)+T(560,140,"AC",13,BLUE,"start","700")
  +T(360,250,"Bộ chuyển đổi công suất hai chiều (PCS)",13,INK,"middle","700"),"Hình đại diện")

save("rep-battery-rack",W,H,
  ''.join(f"<rect x='250' y='{72+k*30}' width='220' height='24' rx='3' fill='#e8f5ee' stroke='{GRN}' stroke-width='1.8'/>"
          +T(360,89+k*30,f"Module pin LFP {k+1}",10.5,MUT,"middle") for k in range(5))
  +f"<rect x='240' y='62' width='240' height='170' rx='7' fill='none' stroke='{GRN}' stroke-width='2.5'/>"
  +T(360,258,"Rack pin LFP (module xếp chồng)",13,INK,"middle","700"),"Hình đại diện")

save("rep-microgrid",W,H, solar(70,90)+grid_tower(300,80)+cabinet(430,80,80,110,"BESS")
  +factory(590,120)+T(612,190,"Tải",11,MUT,"middle")
  +line(120,150,300,150,WIRE,2)+line(332,140,430,140,WIRE,2)+line(510,140,590,140,WIRE,2)
  +T(360,255,"Lưới điện siêu nhỏ (microgrid) tích hợp",13,INK,"middle","700"),"Hình đại diện")

save("rep-lfp-cell",W,H, battery(240,140,80,50,GRN,0.8)+T(240,190,"Cell LFP",11.5,MUT,"middle")
  +arr(300,140,360,140)+battery(420,140,90,56,GRN,0.8)+T(420,190,"Module",11.5,MUT,"middle")
  +arr(480,140,540,140)+cabinet(560,85,90,110,"Hệ thống",GRN,0.8)
  +T(360,258,"Từ cell LFP đến hệ thống lưu trữ",13,INK,"middle","700"),"Hình đại diện")

save("rep-bess-safety",W,H,
  cabinet(180,80,100,140,"BESS",GRN,0.6)
  +box(330,85,150,50,"BMS","#eef4fc",BLUE,INK,12,"giám sát cell")
  +box(330,150,150,50,"PCCC","#fdeede",RED,INK,12,"khí + báo cháy")
  +box(510,85,150,50,"HVAC","#eef6f6",TEAL,INK,12,"kiểm soát nhiệt")
  +box(510,150,150,50,"Cách ly","#fff",AMB,INK,12,"MCCB · cầu chì")
  +T(360,258,"Các lớp an toàn của hệ BESS",13,INK,"middle","700"),"Hình đại diện")

# ================= PRINCIPLE =================
save("prin-bess-charge",W,H,
  T(160,80,"SẠC (giờ thấp điểm / dư PV)",12,GRN,"middle","700")
  +solar(70,100,80,44)+arr(160,125,250,125,GRN)+cabinet(255,85,80,110,"BESS",GRN,0.35)
  +T(560,80,"XẢ (giờ cao điểm)",12,AMB,"middle","700")
  +cabinet(430,85,80,110,"BESS",AMB,0.85)+arr(515,125,600,125,AMB)+factory(610,110)
  +T(360,250,"Nạp khi điện rẻ/dư · xả khi điện đắt hoặc mất điện",12,MUT,"middle")
  ,"Nguyên lý: chu trình sạc – xả của hệ lưu trữ")

save("prin-pcs",W,H,
  battery(130,140,80,50,GRN,0.7)+T(130,192,"Pin (DC)",11.5,MUT,"middle")
  +arr(180,130,290,130,GRN)+T(235,120,"DC →",10.5,GRN,"middle","700")
  +inverter(290,95,120,95,AMB,"PCS 2 chiều")
  +arr(410,165,300,165,BLUE)+T(355,182,"← AC",10.5,BLUE,"middle","700")
  +arr(415,130,540,130,BLUE)+grid_tower(560,105)
  +T(360,255,"PCS đổi DC↔AC hai chiều, hoà lưới hoặc chạy độc lập",12,MUT,"middle")
  ,"Nguyên lý: bộ chuyển đổi công suất hai chiều")

save("prin-microgrid-switch",W,H,
  grid_tower(80,90)+T(96,165,"Lưới",11,MUT,"middle")
  +box(180,105,120,55,"Điểm đấu nối","#fff",WIRE,INK,11,"PCC")
  +f"<line x1='320' y1='132' x2='360' y2='132' stroke='{RED}' stroke-width='3'/>"
  +f"<circle cx='340' cy='132' r='9' fill='#fff' stroke='{RED}' stroke-width='2.5'/>"
  +T(340,168,"CB tách lưới",10.5,RED,"middle","700")
  +box(390,105,130,55,"PCS + EMS","#eef4fc",VIO,INK,11,"chuyển 0 giây")
  +cabinet(560,80,80,110,"BESS",GRN,0.7)
  +T(360,235,"Mất lưới → tách và chuyển sang chạy độc lập gần như tức thì",12,MUT,"middle")
  +T(360,258,"(zero-second switching — giữ điện cho tải quan trọng)",11,MUT,"middle")
  ,"Nguyên lý: chuyển nối lưới ↔ độc lập")

save("prin-bms",W,H,
  ''.join(battery(120+k*54,110,44,26,GRN,0.7) for k in range(4))
  +T(240,148,"chuỗi cell",11,MUT,"middle")
  +arr(340,110,400,110)+box(400,80,150,70,"BMS","#eef4fc",BLUE,INK,13,"đo U · I · T")
  +arr(550,115,620,115,GRN)+T(660,110,"cân bằng",10.5,GRN,"middle","700")
  +T(400,205,"bảo vệ quá áp · thấp áp · quá dòng · quá nhiệt",11.5,MUT,"middle")
  +T(400,232,"báo SOC / SOH về EMS",11.5,MUT,"middle")
  ,"Nguyên lý: hệ quản lý pin (BMS) giám sát từng cell")

save("prin-peakshaving",W,H,
  f"<polyline points='80,210 140,190 200,150 260,105 320,95 380,120 440,170 500,195 560,205 640,200' fill='none' stroke='{RED}' stroke-width='2.5' stroke-dasharray='5 4'/>"
  +f"<line x1='80' y1='130' x2='650' y2='130' stroke='{GRN}' stroke-width='2.5'/>"
  +T(660,126,"ngưỡng",10.5,GRN,"start","700")
  +f"<polyline points='80,210 140,190 200,150 260,130 320,130 380,130 440,170 500,195 560,205 640,200' fill='none' stroke='{BLUE}' stroke-width='3'/>"
  +T(300,88,"phần cắt đỉnh (BESS xả)",11,AMB,"middle","700")
  +T(120,240,"đường đỏ: tải gốc · đường xanh: sau khi có BESS",11.5,MUT)
  ,"Nguyên lý: cắt đỉnh phụ tải (peak shaving)")

save("prin-liquid-cooling",W,H,
  f"<rect x='120' y='90' width='230' height='120' rx='8' fill='#fff' stroke='{GRN}' stroke-width='2.5'/>"
  +''.join(f"<rect x='{136+k*36}' y='105' width='26' height='60' rx='3' fill='#e8f5ee' stroke='{GRN}'/>" for k in range(6))
  +f"<path d='M132 180 h226' stroke='{BLUE}' stroke-width='4'/><path d='M132 195 h226' stroke='{RED}' stroke-width='4'/>"
  +T(235,225,"ống dẫn chất làm mát áp sát module",11,MUT,"middle")
  +arr(360,182,430,182,BLUE)+T(395,174,"lạnh vào",10,BLUE,"middle","700")
  +arr(430,197,360,197,RED)+T(395,214,"nóng ra",10,RED,"middle","700")
  +box(440,150,150,70,"Chiller","#eef6f6",TEAL,INK,12,"tản nhiệt")
  +T(490,110,"chênh lệch nhiệt giữa các cell nhỏ",11.5,MUT,"middle")
  +T(490,132,"→ pin bền hơn, hiệu suất cao hơn",11.5,MUT,"middle")
  ,"Nguyên lý: làm mát bằng chất lỏng (liquid cooling)")

save("prin-solar-bess",W,H,
  solar(70,95,90,54)+T(125,168,"PV",11,MUT,"middle")
  +arr(180,125,250,125,AMB)+inverter(250,95,100,85,AMB,"PCS")
  +arr(300,190,300,230,GRN)+cabinet(255,235,90,40,"BESS",GRN,0.7)
  +arr(355,135,440,135,BLUE)+box(440,105,120,60,"Tủ phân phối","#fff",WIRE,INK,11,"")
  +arr(560,135,610,135,BLUE)+factory(620,115)
  +grid_tower(500,190)+line(500,190,500,168,WIRE,2)
  +T(360,268,"PV nạp pin — thiếu thì lấy lưới — dư thì tích trữ",12,MUT,"middle")
  ,"Nguyên lý: điện mặt trời kết hợp lưu trữ")

# ================= SPEC / CẤU TẠO =================
save("spec-bess-stack",W,H,
  ''.join([battery(100,140,60,36,GRN,0.8), T(100,180,"Cell",11,MUT,"middle"), arr(140,140,185,140),
           f"<rect x='190' y='112' width='80' height='56' rx='5' fill='#e8f5ee' stroke='{GRN}' stroke-width='2'/>",
           T(230,145,"Module",11.5,INK,"middle","700"), arr(275,140,320,140),
           f"<rect x='325' y='90' width='90' height='100' rx='6' fill='#fff' stroke='{GRN}' stroke-width='2'/>",
           T(370,145,"Rack",11.5,INK,"middle","700"), arr(420,140,465,140)])
  +cabinet(470,80,100,130,"Hệ thống",GRN,0.75)
  +T(360,250,"Cell → Module → Rack → Hệ thống (kèm BMS từng cấp)",12.5,INK,"middle","700")
  ,"Cấu tạo: các cấp của hệ lưu trữ")

save("spec-cabinet-layout",W,H,
  f"<rect x='230' y='60' width='260' height='180' rx='10' fill='#fff' stroke='{GRN}' stroke-width='2.5'/>"
  +f"<rect x='245' y='72' width='230' height='30' rx='4' fill='#eef4fc' stroke='{BLUE}'/>"+T(360,92,"EMS + HMI",11.5,INK,"middle","700")
  +f"<rect x='245' y='108' width='110' height='90' rx='4' fill='#e8f5ee' stroke='{GRN}'/>"+T(300,158,"Rack pin",11.5,INK,"middle","700")
  +f"<rect x='363' y='108' width='112' height='42' rx='4' fill='#fdf0e0' stroke='{AMB}'/>"+T(419,134,"PCS",11.5,INK,"middle","700")
  +f"<rect x='363' y='156' width='112' height='42' rx='4' fill='#eef6f6' stroke='{TEAL}'/>"+T(419,182,"Làm mát",11.5,INK,"middle","700")
  +f"<rect x='245' y='204' width='230' height='26' rx='4' fill='#fdeede' stroke='{RED}'/>"+T(360,221,"PCCC + phân phối",11,INK,"middle","700")
  +T(360,265,"Bố trí bên trong tủ BESS tích hợp",12.5,INK,"middle","700")
  ,"Cấu tạo: bên trong tủ BESS")

save("spec-ems-arch",W,H,
  box(50,110,120,70,"Thiết bị hiện trường","#fff",GRN,INK,11,"BMS·PCS·đồng hồ")
  +arr(170,145,225,145)+box(225,105,130,80,"EMS Controller","#eef4fc",VIO,INK,11,"điều khiển tại chỗ")
  +arr(355,145,410,145)+box(410,105,120,80,"Cloud EMS","#fff",BLUE,INK,11,"máy chủ")
  +arr(530,145,585,145)+box(585,110,110,70,"App / Web","#fff",TEAL,INK,11,"giám sát")
  +T(290,215,"Modbus RTU/TCP",10.5,MUT,"middle")+T(470,215,"4G / Internet",10.5,MUT,"middle")
  +T(360,255,"Kiến trúc EMS: hiện trường → điều khiển → đám mây → người dùng",12,INK,"middle","700")
  ,"Cấu tạo: kiến trúc hệ EMS")

save("spec-container-layout",W,H,
  f"<rect x='120' y='80' width='480' height='140' rx='8' fill='#eef6f6' stroke='{TEAL}' stroke-width='2.5'/>"
  +''.join(f"<rect x='{140+k*70}' y='100' width='58' height='100' rx='4' fill='#e8f5ee' stroke='{GRN}'/>"+T(169+k*70,155,"Rack",10.5,INK,"middle","700") for k in range(4))
  +f"<rect x='425' y='100' width='75' height='48' rx='4' fill='#fdf0e0' stroke='{AMB}'/>"+T(462,129,"PCS",11,INK,"middle","700")
  +f"<rect x='425' y='152' width='75' height='48' rx='4' fill='#eef4fc' stroke='{VIO}'/>"+T(462,181,"EMS",11,INK,"middle","700")
  +f"<rect x='508' y='100' width='80' height='100' rx='4' fill='#fdeede' stroke='{RED}'/>"+T(548,145,"PCCC",11,INK,"middle","700")+T(548,165,"+ HVAC",10.5,MUT,"middle")
  +T(360,255,"Bố trí container BESS: rack pin · PCS · EMS · PCCC/HVAC",12,INK,"middle","700")
  ,"Cấu tạo: bên trong container BESS")

save("spec-sizing",W,H,
  box(60,95,150,80,"Công suất (kW)","#fdf0e0",AMB,INK,12,"tải đỉnh cần bù")
  +box(285,95,150,80,"Dung lượng (kWh)","#e8f5ee",GRN,INK,12,"kW × số giờ")
  +box(510,95,150,80,"C-rate","#eef4fc",BLUE,INK,12,"kW ÷ kWh")
  +T(360,215,"Ví dụ: cắt đỉnh 100 kW trong 2 giờ → cần ≈ 200 kWh (0,5C)",12.5,INK,"middle","700")
  +T(360,245,"Chọn dư 10–20% cho tổn hao, DoD và suy giảm dung lượng theo năm",11.5,MUT,"middle")
  ,"Cấu tạo bài toán: công suất · dung lượng · C-rate")

save("spec-safety-layers",W,H,
  ''.join([box(50,100,130,70,"Cell an toàn","#e8f5ee",GRN,INK,11,"LFP bền nhiệt"),
           arr(180,135,215,135), box(215,100,130,70,"BMS","#eef4fc",BLUE,INK,11,"ngắt khi bất thường"),
           arr(345,135,380,135), box(380,100,130,70,"Báo cháy","#fdf0e0",AMB,INK,11,"khói·nhiệt·khí"),
           arr(510,135,545,135), box(545,100,130,70,"Dập cháy","#fdeede",RED,INK,11,"khí + xả áp")])
  +T(360,215,"Phòng ngừa nhiều lớp — hỏng lớp này còn lớp sau",12.5,INK,"middle","700")
  +T(360,245,"kèm thông gió khẩn cấp, giám sát 24/7 và quy trình ứng phó",11.5,MUT,"middle")
  ,"Cấu tạo: các lớp an toàn PCCC cho BESS")

# ================= APPLICATION =================
save("app-factory-bess",W,H, factory(80,130)+T(102,196,"Nhà máy",11,MUT,"middle")
  +cabinet(200,90,90,120,"BESS",GRN,0.7)+inverter(330,110,90,70,AMB,"PCS")
  +box(460,110,110,70,"Tủ MSB","#fff",WIRE,INK,11,"")+grid_tower(620,105)
  +line(124,160,200,160,WIRE,2)+arr(290,145,330,145,GRN)+arr(420,145,460,145,BLUE)+arr(570,145,616,145,BLUE)
  +T(360,250,"Giảm tiền điện giờ cao điểm · dự phòng khi mất lưới",12,MUT,"middle")
  ,"Ứng dụng: BESS cho nhà máy & khu công nghiệp")

save("app-ev-charging",W,H,
  grid_tower(70,105)+T(86,180,"Lưới yếu",10.5,MUT,"middle")
  +arr(120,140,190,140,STEEL)+cabinet(195,85,90,120,"BESS",GRN,0.65)
  +arr(290,140,360,140,GRN)
  +''.join(f"<rect x='{365+k*70}' y='105' width='46' height='80' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
           +T(388+k*70,150,"⚡",16,BLUE,"middle","700")+T(388+k*70,200,"Trụ sạc",10,MUT,"middle") for k in range(3))
  +T(360,250,"BESS gánh công suất đỉnh — không phải nâng cấp trạm biến áp",12,MUT,"middle")
  ,"Ứng dụng: trạm sạc xe điện có đệm pin")

save("app-island-microgrid",W,H,
  solar(60,100,80,48)+f"<circle cx='210' cy='130' r='26' fill='#fff' stroke='{TEAL}' stroke-width='2'/>"+T(210,135,"DG",11,INK,"middle","700")
  +T(210,172,"máy phát",10,MUT,"middle")
  +cabinet(300,85,90,120,"BESS",GRN,0.7)
  +box(430,100,120,70,"EMS","#eef4fc",VIO,INK,12,"điều phối")
  +''.join(f"<rect x='{590}' y='{95+k*42}' width='70' height='32' rx='4' fill='#fff' stroke='{WIRE}'/>"
           +T(625,116+k*42,["Nhà ở","Trường","Y tế"][k],10,INK,"middle","700") for k in range(3))
  +line(140,150,300,150,WIRE,2)+arr(390,145,430,145)+arr(550,145,588,145,GRN)
  +T(360,255,"Cấp điện ổn định cho đảo/vùng sâu, giảm chạy máy phát dầu",12,MUT,"middle")
  ,"Ứng dụng: microgrid cho đảo & vùng xa lưới")

save("app-solar-storage-roof",W,H,
  f"<path d='M120 170 L240 100 L360 170 Z' fill='#e6ecf5' stroke='{STEEL}' stroke-width='2'/>"
  +f"<rect x='120' y='170' width='240' height='60' fill='#eef3fb' stroke='{STEEL}' stroke-width='2'/>"
  +solar(160,110,80,44)
  +arr(365,150,430,150,AMB)+cabinet(435,95,90,120,"BESS",GRN,0.75)
  +arr(530,150,600,150,BLUE)+box(600,120,90,60,"Tải","#fff",WIRE,INK,11,"")
  +T(360,262,"Điện mặt trời áp mái + lưu trữ: tự dùng tối đa, giảm mua điện",12,MUT,"middle")
  ,"Ứng dụng: điện mặt trời áp mái kết hợp lưu trữ")

save("app-ems-dashboard",W,H,
  f"<rect x='180' y='70' width='360' height='170' rx='10' fill='#fff' stroke='{VIO}' stroke-width='2.5'/>"
  +f"<rect x='180' y='70' width='360' height='30' rx='10' fill='#eef4fc'/>"+T(360,90,"EMS · Giám sát thời gian thực",11.5,VIO,"middle","700")
  +f"<rect x='200' y='115' width='150' height='50' rx='5' fill='#e8f5ee' stroke='{GRN}'/>"+T(275,146,"SOC 78%",14,INK,"middle","700")
  +f"<rect x='366' y='115' width='154' height='50' rx='5' fill='#fdf0e0' stroke='{AMB}'/>"+T(443,146,"Xả 85 kW",14,INK,"middle","700")
  +f"<polyline points='205,220 245,205 285,185 325,195 365,175 405,190 445,168 485,180 520,172' fill='none' stroke='{BLUE}' stroke-width='2.5'/>"
  +T(360,262,"Theo dõi SOC, công suất, doanh thu tiết kiệm — tại chỗ & từ xa",12,MUT,"middle")
  ,"Ứng dụng: giám sát & điều phối bằng EMS")

# ================= COMPARE =================
save("compare-lfp-nmc",W,H,
  box(60,80,280,150,"","#e8f5ee",GRN)+T(200,105,"LFP (LiFePO₄)",14,GRN,"middle","700")
  +T(80,135,"• Bền nhiệt, khó cháy hơn",12)+T(80,160,"• Vòng đời dài (4.000–8.000+)",12)
  +T(80,185,"• Rẻ hơn, không cobalt",12)+T(80,210,"→ chuẩn cho BESS tĩnh",11.5,GRN,"start","700")
  +box(380,80,280,150,"","#fdf0e0",AMB)+T(520,105,"NMC",14,AMB,"middle","700")
  +T(400,135,"• Mật độ năng lượng cao hơn",12)+T(400,160,"• Nhẹ, gọn hơn",12)
  +T(400,185,"• Nhạy nhiệt hơn, đắt hơn",12)+T(400,210,"→ hợp xe điện, nơi chật",11.5,AMB,"start","700")
  ,"So sánh: LFP vs NMC cho lưu trữ")

save("compare-cooling",W,H,
  box(60,80,280,150,"","#eef6f6",TEAL)+T(200,105,"Làm mát chất lỏng",14,TEAL,"middle","700")
  +T(80,135,"• Chênh nhiệt cell thấp",12)+T(80,160,"• Hợp mật độ cao, C-rate cao",12)
  +T(80,185,"• Pin bền hơn, ổn định hơn",12)+T(80,210,"→ tủ/container hiện đại",11.5,TEAL,"start","700")
  +box(380,80,280,150,"","#eef3fb",BLUE)+T(520,105,"Làm mát bằng gió",14,BLUE,"middle","700")
  +T(400,135,"• Cấu tạo đơn giản, rẻ hơn",12)+T(400,160,"• Bảo trì dễ",12)
  +T(400,185,"• Chênh nhiệt lớn hơn",12)+T(400,210,"→ hệ nhỏ, tải nhẹ",11.5,BLUE,"start","700")
  ,"So sánh: làm mát chất lỏng vs làm mát gió")

save("compare-ongrid-offgrid",W,H,
  box(60,80,280,150,"","#eef3fb",BLUE)+T(200,105,"Nối lưới (on-grid)",14,BLUE,"middle","700")
  +T(80,135,"• Cắt đỉnh, dịch tải, mua rẻ",12)+T(80,160,"• Vẫn dùng lưới làm dự phòng",12)
  +T(80,185,"• Cần tuân thủ đấu nối",12)+T(80,210,"→ nhà máy, toà nhà",11.5,BLUE,"start","700")
  +box(380,80,280,150,"","#e8f5ee",GRN)+T(520,105,"Độc lập (off-grid)",14,GRN,"middle","700")
  +T(400,135,"• Tự cấp điện hoàn toàn",12)+T(400,160,"• Cần dự phòng lớn hơn",12)
  +T(400,185,"• Thường kèm PV + máy phát",12)+T(400,210,"→ đảo, trạm xa lưới",11.5,GRN,"start","700")
  ,"So sánh: hệ nối lưới vs hệ độc lập")

save("compare-cabinet-container",W,H,
  box(60,80,280,150,"","#e8f5ee",GRN)+T(200,105,"Tủ (cabinet)",14,GRN,"middle","700")
  +T(80,135,"• ~100 kWh – 400 kWh",12)+T(80,160,"• Lắp nhanh, ít mặt bằng",12)
  +T(80,185,"• Mở rộng theo từng tủ",12)+T(80,210,"→ nhà máy vừa, trạm sạc",11.5,GRN,"start","700")
  +box(380,80,280,150,"","#eef6f6",TEAL)+T(520,105,"Container",14,TEAL,"middle","700")
  +T(400,135,"• ~1 MWh – 5 MWh",12)+T(400,160,"• Suất đầu tư/kWh tốt hơn",12)
  +T(400,185,"• Cần mặt bằng & hạ tầng",12)+T(400,210,"→ dự án lớn, trang trại điện",11.5,TEAL,"start","700")
  ,"So sánh: tủ BESS vs container BESS")

save("compare-roi-bess",W,H,
  T(70,80,"Nguồn hoàn vốn của hệ BESS",13,INK,"start","700")
  +''.join([box(60,105,190,55,"Chênh giá giờ",  "#fdf0e0",AMB,INK,11,"cao điểm ↔ thấp điểm"),
            box(265,105,190,55,"Giảm công suất đỉnh","#e8f5ee",GRN,INK,11,"hạ phí công suất"),
            box(470,105,190,55,"Tự dùng điện PV","#eef3fb",BLUE,INK,11,"bớt mua điện lưới"),
            box(60,175,190,55,"Tránh dừng SX","#fdeede",RED,INK,11,"khi mất điện"),
            box(265,175,190,55,"Trì hoãn nâng cấp","#eef6f6",TEAL,INK,11,"máy biến áp/đường dây"),
            box(470,175,190,55,"Chứng chỉ xanh","#eef4fc",VIO,INK,11,"ESG · giảm phát thải")])
  +T(360,262,"Tính hoàn vốn nên cộng đủ các nguồn, không chỉ chênh giá điện",12,MUT,"middle")
  ,"So sánh: các nguồn hoàn vốn khi đầu tư BESS")

save("compare-bess-may-phat",W,H,
  box(60,80,280,150,"","#e8f5ee",GRN)+T(200,105,"BESS",14,GRN,"middle","700")
  +T(80,135,"• Chuyển tải gần như tức thì",12)+T(80,160,"• Không khói, không ồn",12)
  +T(80,185,"• Còn kiếm tiền lúc bình thường",12)+T(80,210,"→ tải nhạy, đô thị",11.5,GRN,"start","700")
  +box(380,80,280,150,"","#fdf0e0",AMB)+T(520,105,"Máy phát diesel",14,AMB,"middle","700")
  +T(400,135,"• Chạy dài ngày nếu đủ dầu",12)+T(400,160,"• Đầu tư ban đầu thấp hơn",12)
  +T(400,185,"• Có trễ khởi động, ồn, khói",12)+T(400,210,"→ dự phòng dài hạn",11.5,AMB,"start","700")
  ,"So sánh: BESS vs máy phát điện dự phòng")

print("renepoly diagrams saved. total svg:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]))
