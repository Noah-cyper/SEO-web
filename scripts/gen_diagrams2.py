#!/usr/bin/env python3
# Extra diagrams so every article has 3 images: representative / principle / application.
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

# device with dark screen
def device(x,y,w,h,label,accent=BLUE,screen=True,sval="8.8"):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='10' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    if screen:
        s+=f"<rect x='{x+12}' y='{y+12}' width='{w-24}' height='34' rx='5' fill='#0f1720'/>"
        s+=T(x+w/2,y+37,sval,20,"#7ff0c0","middle","700")
    for k in range(4):
        s+=f"<circle cx='{x+16+k*((w-32)/3)}' cy='{y+h-10}' r='3.5' fill='{accent}'/>"
    s+=T(x+w/2,y+h-24,label,13,INK,"middle","700")
    return s
def pipe(x1,y,x2,c=STEEL): return f"<line x1='{x1}' y1='{y}' x2='{x2}' y2='{y}' stroke='{c}' stroke-width='10'/>"
def tank(x,y,w,h,fill=0.5):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='#eef3fb' stroke='{WIRE}'/>"
    lh=int(h*fill); s+=f"<rect x='{x}' y='{y+h-lh}' width='{w}' height='{lh}' fill='#bcd6f5'/>"
    return s
def gauge(cx,cy,r=30,accent=BLUE):
    return (f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
            f"<line x1='{cx}' y1='{cy}' x2='{cx+r*0.5}' y2='{cy-r*0.6}' stroke='{RED}' stroke-width='3'/>"
            f"<circle cx='{cx}' cy='{cy}' r='3.5' fill='{INK}'/>")
def antenna(cx,cy,c=AMBER):
    return (f"<polygon points='{cx-22},{cy} {cx},{cy-55} {cx+22},{cy}' fill='none' stroke='{c}' stroke-width='2.5'/>"
            f"<path d='M{cx-8} {cy-45} q8 -10 16 0' fill='none' stroke='{c}' stroke-width='2'/>")
def factory(x,y,c=STEEL):
    return (f"<path d='M{x} {y+50} L{x} {y+20} L{x+25} {y+35} L{x+25} {y+20} L{x+50} {y+35} L{x+50} {y+50} Z' "
            f"fill='#e6ecf5' stroke='{c}' stroke-width='2'/>")

W,H=720,270
# ---------- REPRESENTATIVE (device look) ----------
save("rep-pressure",W,H,
  f"<rect x='300' y='150' width='120' height='16' fill='{STEEL}'/>"  # process connection
  f"<rect x='330' y='60' width='60' height='95' rx='8' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  f"<circle cx='360' cy='95' r='22' fill='#0f1720'/>"+T(360,100,'bar',12,'#7ff0c0','middle','700')
  +T(360,205,'Cảm biến / transmitter áp suất',13,INK,'middle','700'),"Hình đại diện")
save("rep-gauge",W,H, gauge(360,110,58)+f"<rect x='348' y='168' width='24' height='40' fill='{STEEL}'/>"
  +T(360,230,'Đồng hồ đo áp suất',13,INK,'middle','700'),"Hình đại diện")
save("rep-temp",W,H,
  f"<rect x='300' y='95' width='150' height='14' rx='7' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
  f"<rect x='300' y='95' width='40' height='14' rx='7' fill='{BLUE}'/>"
  f"<line x1='450' y1='102' x2='520' y2='102' stroke='{WIRE}' stroke-width='3'/>"
  +T(360,150,'Que đo Pt100 / can nhiệt',12,MUT,'middle')
  +T(360,205,'Cảm biến nhiệt độ',13,INK,'middle','700'),"Hình đại diện")
save("rep-dp",W,H, device(300,70,140,110,'DP transmitter',BLUE,True,'ΔP')
  +f"<line x1='320' y1='185' x2='320' y2='210' stroke='{WIRE}' stroke-width='3'/><line x1='420' y1='185' x2='420' y2='210' stroke='{WIRE}' stroke-width='3'/>"
  +T(320,225,'+',13,GREEN,'middle','700')+T(420,225,'—',13,RED,'middle','700')
  +T(500,130,'2 cổng áp',12,MUT,'start'),"Hình đại diện")
save("rep-plc",W,H, device(280,60,180,130,'PLC',GREEN,True,'RUN')
  +T(360,225,'Bộ điều khiển lập trình (PLC)',13,INK,'middle','700'),"Hình đại diện")
save("rep-converter",W,H,
  f"<rect x='330' y='55' width='55' height='150' rx='8' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  f"<rect x='340' y='70' width='35' height='16' rx='3' fill='#dbe6f7'/>"
  +''.join(f"<circle cx='{345+k*12}' cy='{195}' r='3.5' fill='{BLUE}'/>" for k in range(3))
  +T(500,120,'DIN rail — nhỏ gọn',12,MUT,'start')
  +T(360,235,'Bộ chuyển đổi tín hiệu',13,INK,'middle','700'),"Hình đại diện")
save("rep-remoteio",W,H,''.join(
  f"<rect x='{250+i*70}' y='70' width='55' height='120' rx='7' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
  +''.join(f"<circle cx='{258+i*70+k*18}' cy='180' r='3' fill='{BLUE}'/>" for k in range(3)) for i in range(3))
  +T(360,225,'Cụm module remote I/O (Z-PC)',13,INK,'middle','700'),"Hình đại diện")
save("rep-datalogger",W,H, device(280,75,150,110,'Datalogger',BLUE,True,'LOG')+antenna(470,150)
  +T(360,225,'RTU / Datalogger',13,INK,'middle','700'),"Hình đại diện")
save("rep-gateway",W,H, device(290,80,160,100,'Gateway',BLUE,False)
  +f"<rect x='305' y='150' width='30' height='12' rx='2' fill='{GREEN}'/><rect x='405' y='150' width='30' height='12' rx='2' fill='{AMBER}'/>"
  +T(320,205,'Ethernet',10.5,GREEN,'middle')+T(420,205,'RS485',10.5,AMBER,'middle')
  +T(360,240,'Gateway Modbus',13,INK,'middle','700'),"Hình đại diện")
save("rep-iot",W,H, device(280,80,160,100,'IIoT GW',BLUE,False)+antenna(480,155)
  +f"<rect x='300' y='150' width='26' height='12' rx='2' fill='{GREEN}'/><rect x='394' y='150' width='26' height='12' rx='2' fill='{AMBER}'/>"
  +T(360,235,'IIoT gateway / router (VPN, 4G)',13,INK,'middle','700'),"Hình đại diện")
save("rep-energy",W,H, device(290,60,150,140,'kWh',AMBER,True,'kWh')
  +T(360,235,'Đồng hồ đo điện năng',13,INK,'middle','700'),"Hình đại diện")
save("rep-panel",W,H,
  f"<rect x='285' y='70' width='170' height='110' rx='8' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  f"<rect x='305' y='92' width='130' height='50' rx='5' fill='#0f1720'/>"+T(370,130,'123.4',26,'#7ff0c0','middle','700')
  +T(360,225,'Bộ hiển thị (panel meter)',13,INK,'middle','700'),"Hình đại diện")
save("rep-obsolete",W,H, box(250,90,110,80,'Mã cũ','#fff',RED,INK,13,'obsolete')
  +arr(360,130,470,130,BLUE)+box(470,90,120,80,'Thay thế','#fff',GREEN,INK,13,'tương đương')
  +T(360,215,'Tìm hàng thay thế cho thiết bị ngừng SX',12.5,INK,'middle','700'),"Hình đại diện")

# ---------- PRINCIPLE ----------
save("prin-pressure",W,H,
  f"<path d='M300 150 q30 -40 60 0' fill='none' stroke='{BLUE}' stroke-width='3'/>"  # diaphragm
  +T(330,175,'màng cảm biến',11,MUT,'middle')+arr(120,110,300,110,AMBER)+T(210,100,'áp suất',11,AMBER,'middle','700')
  +box(400,85,150,60,'Mạch điện tử','#eef3fb',BLUE)+arr(550,115,650,115,GREEN)+T(600,105,'4–20mA',10.5,GREEN,'middle','700')
  ,"Nguyên lý: áp → biến dạng màng → tín hiệu điện")
save("prin-bourdon",W,H,
  f"<path d='M330 170 C300 120 380 90 400 130' fill='none' stroke='{BLUE}' stroke-width='6'/>"
  +T(360,195,'ống Bourdon',11,MUT,'middle')+arr(180,150,300,160,AMBER)+T(230,142,'áp suất',11,AMBER,'middle','700')
  +f"<line x1='400' y1='130' x2='470' y2='95' stroke='{RED}' stroke-width='3'/>"+T(500,110,'kim quay',11,MUT,'start')
  ,"Nguyên lý: áp làm ống Bourdon giãn → kim quay")
save("prin-dp",W,H, tank(250,80,60,110,0.4)+T(280,205,'buồng +',11,GREEN,'middle')
  +tank(410,80,60,110,0.4)+T(440,205,'buồng —',11,RED,'middle')
  +f"<path d='M340 135 q20 -25 40 0' fill='none' stroke='{BLUE}' stroke-width='3'/>"+T(360,165,'màng',11,MUT,'middle')
  +arr(500,135,620,135,BLUE)+T(560,125,'ΔP → tín hiệu',10.5,BLUE,'middle','700')
  ,"Nguyên lý: chênh áp 2 buồng làm lệch màng")
save("prin-plc",W,H, box(230,90,110,70,'Ngõ vào','#fff',BLUE,INK,12,'cảm biến')
  +arr(340,125,400,125)+box(400,90,110,70,'CPU','#eef3fb',BLUE,INK,12,'chạy logic')
  +arr(510,125,570,125)+box(570,90,120,70,'Ngõ ra','#fff',GREEN,INK,12,'motor/van')
  ,"Nguyên lý: đọc vào → xử lý logic → điều khiển ra")
save("prin-energy",W,H, T(250,120,'Tải 3 pha',12,INK,'start','700')
  +f"<circle cx='330' cy='150' r='24' fill='#fff' stroke='{WIRE}' stroke-width='2'/>"+T(330,155,'CT',12,INK,'middle','700')
  +arr(360,150,430,150)+box(430,120,160,60,'Đồng hồ đo','#eef3fb',AMBER)
  +T(510,205,'U • I • P • kWh',11,MUT,'middle')
  ,"Nguyên lý: CT lấy dòng → đồng hồ tính công suất/điện năng")
save("prin-panel",W,H, box(230,105,120,55,'Tín hiệu vào','#fff',BLUE,INK,12,'4-20mA/Pt100')
  +arr(350,132,410,132)+f"<rect x='410' y='100' width='130' height='64' rx='6' fill='#0f1720'/>"+T(475,140,'123.4',20,'#7ff0c0','middle','700')
  +arr(540,132,610,132,RED)+T(650,127,'relay',10.5,RED,'middle','700')
  ,"Nguyên lý: nhận tín hiệu → hiển thị số → cảnh báo")

# ---------- APPLICATION ----------
save("app-pressure",W,H, pipe(180,150,470)+device(300,70,60,70,'',BLUE,False)
  +f"<rect x='322' y='140' width='16' height='14' fill='{STEEL}'/>"+arr(470,150,560,150,GREEN)
  +box(560,120,120,60,'PLC/SCADA','#fff',GREEN)+T(330,205,'đo áp đường ống, bồn, lò hơi',12,MUT,'middle')
  ,"Ứng dụng: giám sát áp trong nhà máy")
save("app-gauge",W,H, pipe(200,160,430)+gauge(320,110,34)+f"<rect x='312' y='142' width='16' height='20' fill='{STEEL}'/>"
  +T(360,210,'lắp tại chỗ trên đường ống / máy nén / lò hơi',12,MUT,'middle')
  ,"Ứng dụng: đọc áp trực tiếp tại hiện trường")
save("app-temp",W,H, factory(230,90)+f"<rect x='330' y='120' width='120' height='40' rx='6' fill='#fde8d6' stroke='{AMBER}'/>"
  +T(390,145,'LÒ / ĐƯỜNG ỐNG',11,AMBER,'middle','700')+f"<rect x='450' y='133' width='60' height='12' rx='6' fill='{BLUE}'/>"
  +arr(515,139,600,139,GREEN)+T(560,130,'°C',11,GREEN,'middle','700')
  +T(360,210,'đo nhiệt lò hơi, lò nung, đường ống',12,MUT,'middle')
  ,"Ứng dụng: giám sát nhiệt độ quá trình")
save("app-remoteio",W,H, factory(210,80)
  +''.join(f"<rect x='{300+i*40}' y='120' width='30' height='40' rx='4' fill='#fff' stroke='{BLUE}'/>" for i in range(3))
  +f"<line x1='300' y1='175' x2='560' y2='175' stroke='{BLUE}' stroke-width='3'/>"+T(430,168,'RS485',10.5,BLUE,'middle','700')
  +box(560,120,120,55,'SCADA','#fff',GREEN)+f"<line x1='620' y1='160' x2='620' y2='175' stroke='{WIRE}'/>"
  ,"Ứng dụng: gom tín hiệu phân tán về trung tâm")
save("app-datalogger",W,H, factory(210,95)+box(300,110,120,55,'Trạm bơm','#fff',BLUE,INK,12,'ở xa')
  +antenna(470,150)+arr(430,135,455,120,AMBER)+arr(500,120,560,120,AMBER)
  +box(560,95,120,55,'Trung tâm','#fff',GREEN,INK,12,'/ đám mây')
  +T(360,205,'giám sát & cảnh báo qua 3G/4G',12,MUT,'middle')
  ,"Ứng dụng: giám sát trạm ở xa")
save("app-gateway",W,H,
  ''.join(f"<rect x='{230+i*35}' y='120' width='26' height='36' rx='4' fill='#fff' stroke='{AMBER}'/>" for i in range(3))
  +f"<line x1='230' y1='175' x2='360' y2='175' stroke='{AMBER}' stroke-width='3'/>"+T(300,168,'RTU',10.5,AMBER,'middle','700')
  +box(370,115,110,55,'Gateway','#eef3fb',BLUE)+arr(480,142,560,142,GREEN)
  +box(560,115,120,55,'SCADA/PC','#fff',GREEN,INK,12,'TCP')
  ,"Ứng dụng: đưa thiết bị RS485 lên mạng Ethernet")
save("app-iot",W,H, box(220,115,120,60,'Máy / tủ','#fff',BLUE,INK,12,'ở xa')+antenna(400,150)
  +arr(340,140,385,130,AMBER)+arr(420,130,500,130,AMBER)+T(430,120,'VPN',10.5,GREEN,'middle','700')
  +f"<rect x='500' y='105' width='150' height='80' rx='6' fill='#fff' stroke='{GREEN}'/>"+T(575,150,'Kỹ sư / PC',12,INK,'middle','700')
  ,"Ứng dụng: truy cập & bảo trì máy từ xa an toàn")
save("app-energy",W,H,
  f"<rect x='230' y='80' width='150' height='120' rx='8' fill='#eef3fb' stroke='{WIRE}'/>"+T(305,72,'Tủ điện',12,INK,'middle','700')
  +device(255,110,100,70,'kWh',AMBER,True,'kWh')+arr(380,140,470,140,BLUE)+T(425,132,'Modbus',10.5,BLUE,'middle','700')
  +box(470,110,120,60,'EMS','#fff',GREEN,INK,12,'quản lý NL')
  ,"Ứng dụng: giám sát điện năng nhà máy")
save("app-panel",W,H,
  f"<rect x='250' y='75' width='220' height='130' rx='8' fill='#eef3fb' stroke='{WIRE}'/>"+T(360,68,'Mặt tủ điều khiển',12,INK,'middle','700')
  +f"<rect x='285' y='105' width='150' height='55' rx='6' fill='#0f1720'/>"+T(360,143,'123.4',24,'#7ff0c0','middle','700')
  +f"<circle cx='320' cy='180' r='7' fill='{GREEN}'/><circle cx='400' cy='180' r='7' fill='{RED}'/>"
  ,"Ứng dụng: hiển thị & cảnh báo tại tủ")
save("app-obsolete",W,H, factory(220,95)+box(310,110,110,60,'Máy đang chạy','#fff',BLUE,INK,11,'PLC/cảm biến cũ')
  +arr(420,140,500,140,GREEN)+box(500,110,130,60,'Dự phòng / thay thế','#fff',GREEN,INK,11,'chính hãng')
  +T(360,205,'duy trì máy chạy, tránh dừng dây chuyền',12,MUT,'middle')
  ,"Ứng dụng: giữ dây chuyền hoạt động")

print("extra diagrams:", len([f for f in os.listdir(OUT)]))
