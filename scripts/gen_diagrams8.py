#!/usr/bin/env python3
# Biến tần (VFD) — bộ sơ đồ mở rộng cho 20 bài tầng 6–9
import os
OUT="/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT,exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#1f6feb"; GRN="#12a06a"; AMB="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"; VIO="#6b4fd8"; TEAL="#0e8f8f"
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
def arrL(x1,y1,x2,y2,c=WIRE,w=2.5):
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
            f"<polygon points='{x2},{y2} {x2+9},{y2-5} {x2+9},{y2+5}' fill='{c}'/>")
def line(x1,y1,x2,y2,c=WIRE,w=2.5): return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
def save(name,w,h,body,title): open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

def vfd(x,y,w=120,h=150,label="Biến tần",accent=BLUE):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='9' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<rect x='{x+14}' y='{y+14}' width='{w-28}' height='30' rx='4' fill='#0f1720'/>"
    s+=T(x+w/2,y+35,"50.0 Hz",13,"#7ff0c0","middle","700")
    for k in range(4): s+=f"<circle cx='{x+22+k*((w-44)/3)}' cy='{y+62}' r='5' fill='none' stroke='{accent}' stroke-width='1.6'/>"
    s+=f"<rect x='{x+16}' y='{y+78}' width='{w-32}' height='{h-100}' rx='4' fill='#eef3fb'/>"
    for k in range(5): s+=line(x+22,y+88+k*9,x+w-22,y+88+k*9,STEEL,1.4)
    s+=T(x+w/2,y+h-8,label,12,INK,"middle","700")
    return s
def motor(cx,cy,r=32,accent=GRN,label="Động cơ"):
    s=f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=T(cx,cy+6,"M",20,INK,"middle","700")
    if label: s+=T(cx,cy+r+20,label,12,INK,"middle","700")
    return s
def grid3(x,y,label="Lưới 3 pha"):
    s=""
    for k in range(3): s+=line(x,y+k*14,x+52,y+k*14,AMB,3)
    s+=T(x+26,y+58,label,11.5,INK,"middle","700")
    return s
def axes(x,y,w,h,xl="",yl=""):
    s=line(x,y,x,y+h,STEEL,2)+line(x,y+h,x+w,y+h,STEEL,2)
    if xl: s+=T(x+w,y+h+18,xl,11,MUT,"end")
    if yl: s+=T(x-4,y-6,yl,11,MUT,"end")
    return s

W,H=720,290

# ================= REP (đại diện) =================
b=grid3(60,110)+arr(118,124,180,124,AMB,3)+vfd(180,60,110,150)
b+=arr(296,135,360,135,BLUE,3)+T(328,124,"f thay đổi",10.5,BLUE,"middle","700")
b+=motor(400,135,30,GRN,"")
b+=line(432,135,470,135,STEEL,4)
b+=f"<rect x='470' y='108' width='190' height='16' rx='4' fill='{STEEL}'/>"
for k in range(5): b+=f"<circle cx='{490+k*42}' cy='{150}' r='11' fill='none' stroke='{WIRE}' stroke-width='2'/>"
b+=f"<rect x='500' y='84' width='34' height='24' rx='3' fill='#fff' stroke='{AMB}' stroke-width='2'/>"
b+=f"<rect x='566' y='84' width='34' height='24' rx='3' fill='#fff' stroke='{AMB}' stroke-width='2'/>"
b+=T(565,196,"băng tải — tốc độ đặt theo nhịp dây chuyền",11.5,MUT,"middle")
save("rep-vfd-bangtai",W,H,b,"Biến tần điều khiển băng tải")

b=grid3(60,110)+arr(118,124,180,124,AMB,3)+vfd(180,60,110,150)
b+=arr(296,135,352,135,BLUE,3)+motor(392,135,30,GRN,"")
b+=f"<rect x='440' y='96' width='120' height='80' rx='12' fill='#fff' stroke='{TEAL}' stroke-width='2.5'/>"
b+=T(500,132,"Đầu nén",13,INK,"middle","700")+T(500,152,"trục vít",11,MUT,"middle")
b+=line(424,136,440,136,STEEL,5)
b+=arr(560,136,626,136,TEAL,3)
b+=f"<rect x='612' y='150' width='40' height='56' rx='8' fill='#eef6f6' stroke='{TEAL}' stroke-width='2'/>"
b+=T(632,240,"bình chứa",11,MUT,"middle")+T(596,126,"khí nén",10.5,TEAL,"middle","700")
b+=T(300,240,"giữ áp khí ổn định thay vì tải/không tải",11.5,MUT,"middle")
save("rep-vfd-nenkhi",W,H,b,"Biến tần cho máy nén khí")

b=f"<rect x='90' y='62' width='560' height='14' rx='4' fill='{STEEL}'/>"
b+=f"<rect x='300' y='76' width='130' height='60' rx='8' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
b+=T(365,112,"Palăng + biến tần",12,INK,"middle","700")
b+=line(365,136,365,196,WIRE,3)
b+=f"<path d='M348 196 l17 -14 l17 14 z' fill='{AMB}'/>"
b+=f"<rect x='330' y='196' width='70' height='48' rx='6' fill='#fff' stroke='{AMB}' stroke-width='2.5'/>"
b+=T(365,226,"Tải",13,INK,"middle","700")
b+=arr(452,150,452,210,RED,2.5)+T(516,186,"khi hạ: tải kéo động cơ",11,RED,"middle","700")
b+=arrL(452,120,452,90,GRN,2.5)+T(516,104,"khi nâng: động cơ kéo tải",11,GRN,"middle","700")
b+=T(180,120,"cần mô-men",11.5,MUT,"middle")+T(180,138,"giữ ở tốc độ 0",11.5,INK,"middle","700")
save("rep-vfd-cautruc",W,H,b,"Biến tần cho cầu trục & palăng")

b=grid3(50,112)+arr(108,126,166,126,AMB,3)+vfd(166,62,104,150)
b+=arr(276,137,332,137,BLUE,3)
b+=f"<rect x='332' y='104' width='48' height='66' rx='8' fill='#fff' stroke='{STEEL}' stroke-width='2'/>"
b+=T(356,144,"HS",12,INK,"middle","700")+T(356,190,"hộp số",11,MUT,"middle")
b+=f"<path d='M410 96 l150 0 l-22 96 l-106 0 z' fill='#fff' stroke='{VIO}' stroke-width='2.5'/>"
b+=line(452,110,518,178,VIO,3)+line(518,110,452,178,VIO,3)
b+=line(380,137,410,137,STEEL,5)
b+=T(485,214,"thùng trộn / buồng nghiền",11.5,MUT,"middle")
b+=T(485,240,"mô-men khởi động lớn khi đầy liệu",11.5,INK,"middle","700")
save("rep-vfd-tron",W,H,b,"Biến tần cho máy trộn & máy nghiền")

b=f"<rect x='60' y='70' width='240' height='150' rx='10' fill='#fff' stroke='{STEEL}' stroke-width='2'/>"
b+=T(180,92,"AHU / buồng xử lý khí",12,INK,"middle","700")
b+=f"<circle cx='140' cy='158' r='34' fill='#eef3fb' stroke='{BLUE}' stroke-width='2.5'/>"
for a in (0,120,240):
    b+=f"<path d='M140 158 q20 -16 30 5 q-16 9 -30 -5' fill='{BLUE}' opacity='0.55' transform='rotate({a} 140 158)'/>"
b+=f"<rect x='210' y='120' width='16' height='76' fill='{TEAL}' opacity='0.5'/>"
b+=T(255,162,"coil",11,MUT,"middle")
b+=arr(300,145,368,145,BLUE,3)+T(334,134,"gió cấp",10.5,BLUE,"middle","700")
b+=f"<rect x='368' y='84' width='140' height='124' rx='9' fill='#f2f6fb' stroke='{BD}' stroke-width='2'/>"
b+=T(438,110,"Khu vực sử dụng",12,INK,"middle","700")
for k in range(3): b+=f"<rect x='{388+k*40}' y='{130}' width='28' height='58' rx='4' fill='#fff' stroke='{STEEL}' stroke-width='1.6'/>"
b+=box(540,100,140,52,"Cảm biến","#fff",GRN,INK,12,"nhiệt độ · CO₂")
b+=arrL(540,126,514,126,GRN,2.5)
b+=T(610,182,"PID hạ tốc khi tải nhiệt thấp",11,MUT,"middle")
save("rep-vfd-hvac",W,H,b,"Biến tần trong hệ HVAC")

b=vfd(280,60,150,160,"Biến tần + tủ")
b+=box(60,96,170,54,"Máy đang chạy","#fff",AMB,INK,12,"khởi động trực tiếp")
b+=arr(230,123,278,123,AMB,3)
b+=box(470,96,190,54,"Sau retrofit","#fff",GRN,INK,12,"tốc độ thay đổi được")
b+=arr(432,123,468,123,GRN,3)
b+=T(360,248,"giữ nguyên động cơ & cơ khí — chỉ đổi cách cấp nguồn",11.5,MUT,"middle")
save("rep-vfd-retrofit",W,H,b,"Lắp biến tần cho máy đang chạy")

# ================= PRIN (nguyên lý) =================
b=box(60,110,110,64,"Lưới","#fff",AMB,INK,13)
b+=box(230,110,130,64,"Chỉnh lưu","#fff",BLUE,INK,12,"AC → DC")
b+=box(420,110,130,64,"Nghịch lưu","#fff",BLUE,INK,12,"DC → AC")
b+=motor(636,142,30,GRN,"")
b+=arr(170,142,228,142,AMB,3)+arr(360,142,418,142,VIO,3)+arr(550,142,604,142,GRN,3)
b+=arrL(420,206,362,206,RED,2.5)+arrL(230,206,172,206,RED,2.5)
b+=T(300,228,"chiều năng lượng khi hãm (4 góc phần tư)",11.5,RED,"middle","700")
b+=T(295,196,"AFE trả điện về lưới",11,RED,"middle")
save("prin-vfd-regen",W,H,b,"Hoàn năng lượng về lưới (4 góc phần tư)")

b=box(60,64,150,52,"PLC / Master","#fff",VIO,INK,12)
for k in range(3):
    x=90+k*200
    b+=box(x,160,150,66,f"Biến tần {k+1}","#fff",BLUE,INK,12,"tốc độ tham chiếu")
    b+=arr(x+75,116,x+75,158,VIO,2.2,"5 4")
b+=line(135,116,535,116,VIO,2.2)
b+=T(360,146,"cùng một lệnh tốc độ · bù trượt riêng từng trục",11,MUT,"middle")
b+=T(360,258,"đồng bộ tốc độ nhiều trục trên một dây chuyền",11.5,INK,"middle","700")
save("prin-master-slave",W,H,b,"Đồng bộ nhiều biến tần")

b=axes(90,70,240,140,"tốc độ","mô-men")
b+=f"<path d='M90 100 L250 100 L300 200' fill='none' stroke='{GRN}' stroke-width='3'/>"
b+=T(200,92,"PM: mô-men cao, phẳng",11,GRN,"middle","700")
b+=f"<path d='M90 132 Q170 128 250 140 L300 210' fill='none' stroke='{STEEL}' stroke-width='3' stroke-dasharray='6 4'/>"
b+=T(196,158,"IM (không đồng bộ)",11,MUT,"middle")
b+=f"<circle cx='500' cy='140' r='58' fill='#fff' stroke='{VIO}' stroke-width='2.5'/>"
for k,a in enumerate((30,150,270)):
    b+=f"<rect x='488' y='90' width='24' height='30' rx='3' fill='{VIO}' opacity='0.6' transform='rotate({a} 500 140)'/>"
b+=T(500,146,"N/S",13,INK,"middle","700")
b+=T(500,220,"rotor gắn nam châm vĩnh cửu",11.5,MUT,"middle")
b+=T(620,110,"không có",11,MUT,"middle")+T(620,128,"tổn hao rotor",11,INK,"middle","700")
save("prin-pmsm",W,H,b,"Động cơ nam châm vĩnh cửu và biến tần")

b=vfd(250,60,140,155,"Biến tần")
b+=box(60,104,150,60,"Mạch an toàn","#fff",RED,INK,12,"nút dừng khẩn")
b+=arr(210,134,248,134,RED,2.6)
b+=T(320,240,"STO cắt xung kích IGBT — không qua phần mềm",11,RED,"middle","700")
b+=motor(520,137,30,GRN,"")
b+=arr(392,137,486,137,STEEL,3,"7 5")
b+=T(440,124,"mất mô-men",10.5,MUT,"middle")
b+=f"<circle cx='440' cy='170' r='11' fill='none' stroke='{RED}' stroke-width='2.5'/>"
b+=line(433,163,447,177,RED,2.5)
b+=box(556,104,120,60,"Trục","#fff",AMB,INK,12,"không sinh lực")
save("prin-vfd-sto",W,H,b,"Nguyên lý Safe Torque Off (STO)")

b=box(60,60,170,58,"PLC / SCADA","#fff",VIO,INK,12)
b+=line(145,118,145,150,VIO,2.5)+line(145,150,620,150,VIO,3)
for k in range(4):
    x=210+k*130
    b+=box(x-52,178,104,56,f"VFD {k+1}","#fff",BLUE,INK,12)
    b+=line(x,150,x,176,VIO,2.2)
b+=T(360,140,"một mạng — nhiều thiết bị · mỗi thiết bị một địa chỉ",11,MUT,"middle")
b+=T(360,262,"Modbus RTU · Modbus TCP · PROFINET · EtherNet/IP · CANopen",11.5,INK,"middle","700")
save("prin-fieldbus",W,H,b,"Biến tần trên mạng truyền thông công nghiệp")

b=axes(80,64,250,150,"thời gian","dòng")
b+=f"<path d='M80 140 q30 -60 62 0 q30 60 62 0 q30 -60 62 0 q30 60 62 0' fill='none' stroke='{GRN}' stroke-width='2.6'/>"
b+=T(205,84,"dòng hình sin (lý tưởng)",11,GRN,"middle","700")
b+=axes(410,64,250,150,"thời gian","dòng")
b+=f"<path d='M410 200 L452 200 L458 96 L470 96 L476 200 L534 200 L540 96 L552 96 L558 200 L616 200 L622 96 L634 96 L640 200 L660 200' fill='none' stroke='{RED}' stroke-width='2.6'/>"
b+=T(535,84,"dòng biến tần: xung nhọn",11,RED,"middle","700")
b+=T(535,244,"→ sinh sóng hài bậc 5, 7, 11, 13…",11.5,INK,"middle","700")
b+=T(205,244,"THD thấp",11.5,MUT,"middle")
save("prin-song-hai",W,H,b,"Vì sao biến tần sinh sóng hài")

b=box(60,110,120,64,"Lưới","#fff",AMB,INK,13)
b+=box(226,110,150,64,"Tụ bù","#fff",TEAL,INK,12,"cosφ cơ bản")
b+=box(440,110,220,64,"Biến tần","#fff",BLUE,INK,12,"cosφ đầu vào cao sẵn")
b+=arr(180,142,224,142,AMB,3)+arr(376,142,438,142,AMB,3)
b+=f"<path d='M232 216 q90 30 200 0' fill='none' stroke='{RED}' stroke-width='2.5' stroke-dasharray='6 4'/>"
b+=T(332,254,"cộng hưởng tụ bù ↔ sóng hài: rủi ro cần kiểm tra",11.5,RED,"middle","700")
save("prin-cosphi",W,H,b,"Biến tần, hệ số công suất và tụ bù")

b=f"<circle cx='140' cy='140' r='56' fill='#fff' stroke='{AMB}' stroke-width='2.5'/>"
b+=T(140,134,"G",22,INK,"middle","700")+T(140,158,"máy phát",11,MUT,"middle")
b+=arr(200,140,268,140,AMB,3)
b+=vfd(268,64,130,155,"Biến tần")
b+=motor(500,140,30,GRN,"")+arr(400,140,466,140,BLUE,3)
b+=arrL(400,206,270,206,RED,2.5)
b+=T(336,232,"sóng hài & năng lượng hãm dội ngược",11,RED,"middle","700")
b+=box(548,110,140,60,"Cần dự phòng","#fff",TEAL,INK,12,"công suất máy phát")
save("prin-may-phat",W,H,b,"Biến tần chạy trên máy phát điện")

b=vfd(90,64,130,155,"Biến tần")
b+=motor(420,124,30,GRN,"")+arr(222,124,386,124,BLUE,3)
b+=T(304,110,"cáp động cơ",10.5,MUT,"middle")
for k in range(5):
    x=250+k*30
    b+=f"<path d='M{x} 138 q0 22 0 30' fill='none' stroke='{RED}' stroke-width='1.8' stroke-dasharray='4 3'/>"
b+=line(160,236,620,236,WIRE,3)
for k in range(3): b+=line(280+k*90,236,280+k*90,246,WIRE,3)
b+=T(390,268,"dây nối đất — đường về của dòng rò cao tần",11.5,INK,"middle","700")
b+=T(370,186,"điện dung ký sinh → dòng rò",11,RED,"middle","700")
b+=box(496,96,180,56,"RCCB loại B","#fff",AMB,INK,12,"chịu được dòng một chiều")
save("prin-dong-ro",W,H,b,"Dòng rò cao tần và nối đất")

# ================= SPEC (cấu tạo / thông số) =================
rows=[("Giao thức","Modbus · PROFINET · EtherNet/IP"),("Card mở rộng","cắm thêm vào khe option"),
      ("Địa chỉ","duy nhất trên mạng"),("Chu kỳ cập nhật","theo yêu cầu điều khiển")]
b=""
for i,(k,v) in enumerate(rows):
    y=64+i*52
    b+=f"<rect x='60' y='{y}' width='600' height='42' rx='7' fill='#fff' stroke='{BD}'/>"
    b+=T(78,y+27,k,12.5,INK,"start","700")+T(300,y+27,v,12,MUT)
save("spec-vfd-fieldbus",W,H,b,"Thông số cấu hình truyền thông")

b=box(60,70,180,64,"Cấp an toàn","#fff",RED,INK,12,"theo tiêu chuẩn máy")
b+=box(270,70,180,64,"Số kênh STO","#fff",RED,INK,12,"thường 2 kênh")
b+=box(480,70,180,64,"Giám sát chéo","#fff",RED,INK,12,"phát hiện lỗi kênh")
b+=box(60,160,180,64,"Thời gian phản hồi","#fff",AMB,INK,12,"tính bằng ms")
b+=box(270,160,180,64,"Reset","#fff",AMB,INK,12,"thủ công / tự động")
b+=box(480,160,180,64,"Chứng nhận","#fff",AMB,INK,12,"hồ sơ kèm thiết bị")
b+=T(360,262,"STO không thay thế cho cách ly nguồn khi bảo trì",11.5,INK,"middle","700")
save("spec-vfd-sto",W,H,b,"Thông số chức năng an toàn")

b=box(60,64,150,58,"Diode thường","#fff",STEEL,INK,12,"1 chiều")
b+=box(60,148,150,58,"AFE / IGBT","#fff",GRN,INK,12,"2 chiều")
b+=box(280,64,180,58,"Không trả điện","#fff",STEEL,INK,12,"cần điện trở xả")
b+=box(280,148,180,58,"Trả về lưới","#fff",GRN,INK,12,"không cần điện trở")
b+=box(500,64,160,58,"Chi phí thấp","#fff",STEEL,INK,12)
b+=box(500,148,160,58,"Chi phí cao","#fff",GRN,INK,12,"hoàn vốn khi hãm nhiều")
b+=arr(212,93,276,93,STEEL,2.4)+arr(462,93,498,93,STEEL,2.4)
b+=arr(212,177,276,177,GRN,2.4)+arr(462,177,498,177,GRN,2.4)
b+=T(360,258,"chọn theo tần suất và thời lượng hãm",11.5,MUT,"middle")
save("spec-vfd-afe",W,H,b,"Cấu hình khối đầu vào biến tần")

items=["Khảo sát động cơ & cơ khí","Đo dòng, điện áp trước khi lắp","Kiểm tra tủ & tiết diện cáp",
       "Chọn công suất theo dòng thực","Lên phương án đấu nối & điều khiển","Kế hoạch dừng máy để lắp"]
b=""
for i,t in enumerate(items):
    x=60+(i%2)*310; y=64+(i//2)*66
    b+=f"<rect x='{x}' y='{y}' width='290' height='48' rx='8' fill='#fff' stroke='{BD}'/>"
    b+=f"<circle cx='{x+26}' cy='{y+24}' r='13' fill='{TEAL}' opacity='0.16'/>"
    b+=T(x+26,y+29,str(i+1),12,TEAL,"middle","700")+T(x+50,y+29,t,11.5,INK)
save("spec-retrofit",W,H,b,"Checklist khảo sát trước khi retrofit")

items=["Kiểm tra nguội: cách điện, siết cực","Cấp nguồn — không nối động cơ","Khai báo động cơ & giới hạn",
       "Chạy không tải, kiểm chiều quay","Chạy có tải, đo dòng 3 pha","Thử dừng khẩn & mất truyền thông",
       "Đo nhiệt độ tủ sau vài giờ","Bàn giao hồ sơ & bảng thông số"]
b=""
for i,t in enumerate(items):
    x=60+(i%2)*310; y=58+(i//2)*54
    b+=f"<rect x='{x}' y='{y}' width='290' height='40' rx='7' fill='#fff' stroke='{BD}'/>"
    b+=f"<path d='M{x+16} {y+20} l7 8 l13 -15' fill='none' stroke='{GRN}' stroke-width='2.6'/>"
    b+=T(x+46,y+25,t,11,INK)
save("spec-nghiem-thu",W,H,b,"Checklist nghiệm thu hệ biến tần")

b=box(60,100,140,64,"Biến tần","#fff",BLUE,INK,12,"dữ liệu vận hành")
b+=box(250,100,150,64,"Gateway","#fff",TEAL,INK,12,"Modbus → mạng")
b+=box(450,100,210,64,"Nền tảng giám sát","#fff",VIO,INK,12,"cảnh báo · báo cáo")
b+=arr(200,132,248,132,BLUE,2.6)+arr(400,132,448,132,TEAL,2.6)
tags=["dòng","tần số","điện năng","mã lỗi","giờ chạy"]
for i,t in enumerate(tags):
    x=70+i*128
    b+=f"<rect x='{x}' y='198' width='114' height='34' rx='16' fill='#fff' stroke='{BD}'/>"
    b+=T(x+57,220,t,11.5,MUT,"middle")
b+=T(360,262,"phát hiện bất thường trước khi máy dừng",11.5,INK,"middle","700")
save("spec-giam-sat",W,H,b,"Dữ liệu giám sát từ biến tần")

# ================= APP (ứng dụng) =================
b=f"<rect x='70' y='120' width='560' height='18' rx='5' fill='{STEEL}'/>"
for k in range(7): b+=f"<circle cx='{100+k*80}' cy='{160}' r='13' fill='none' stroke='{WIRE}' stroke-width='2'/>"
for k in range(4): b+=f"<rect x='{130+k*130}' y='92' width='40' height='28' rx='4' fill='#fff' stroke='{AMB}' stroke-width='2'/>"
b+=box(60,208,200,52,"Khởi động mềm","#fff",GRN,INK,12,"sản phẩm không đổ")
b+=box(280,208,180,52,"Đổi tốc độ","#fff",BLUE,INK,12,"theo nhịp sản xuất")
b+=box(480,208,180,52,"Đồng bộ đoạn","#fff",VIO,INK,12,"nhiều băng nối tiếp")
save("app-vfd-bangtai2",W,H,b,"Ứng dụng biến tần trên băng tải")

b=axes(80,64,250,140,"thời gian","điện")
b+=f"<path d='M80 90 L120 90 L120 190 L170 190 L170 90 L210 90 L210 190 L260 190 L260 90 L330 90' fill='none' stroke='{RED}' stroke-width='2.6'/>"
b+=T(205,232,"tải / không tải: vẫn tốn điện khi chạy không",11,RED,"middle","700")
b+=axes(410,64,250,140,"thời gian","điện")
b+=f"<path d='M410 160 Q470 130 520 150 T660 140' fill='none' stroke='{GRN}' stroke-width='2.8'/>"
b+=T(535,232,"biến tần: bám sát nhu cầu khí thực tế",11,GRN,"middle","700")
save("app-vfd-nenkhi",W,H,b,"Máy nén khí: tải/không tải so với biến tần")

b=box(60,64,180,56,"Nâng","#fff",GRN,INK,12,"cần mô-men lớn")
b+=box(60,146,180,56,"Hạ","#fff",RED,INK,12,"năng lượng dội về")
b+=box(280,64,190,56,"Giữ ở tốc độ 0","#fff",VIO,INK,12,"cần encoder")
b+=box(280,146,190,56,"Chống trôi tải","#fff",AMB,INK,12,"phối hợp phanh cơ")
b+=box(510,64,150,56,"Điện trở xả","#fff",TEAL,INK,12,"bắt buộc")
b+=box(510,146,150,56,"STO","#fff",RED,INK,12,"dừng an toàn")
b+=T(360,246,"tải thế năng: bốn yêu cầu phải có đủ",11.5,INK,"middle","700")
save("app-vfd-cautruc",W,H,b,"Yêu cầu cho ứng dụng nâng hạ")

b=axes(90,64,540,150,"thời gian","dòng")
b+=f"<path d='M90 200 L150 100 L200 118 L260 104 L320 126 L380 106 L440 130 L500 112 L560 132 L630 120' fill='none' stroke='{VIO}' stroke-width='2.6'/>"
b+=line(90,96,630,96,RED,2,)
b+=T(636,100,"ngưỡng",10.5,RED,"start","700")
b+=T(150,88,"đỉnh khởi động",10.5,VIO,"middle","700")
b+=T(360,248,"tải thay đổi mạnh — cần vector và giới hạn mô-men",11.5,INK,"middle","700")
save("app-vfd-tron",W,H,b,"Đặc tính tải máy trộn, máy nghiền")

b=box(60,64,170,56,"Chiller / bơm","#fff",TEAL,INK,12)
b+=box(60,146,170,56,"AHU / quạt gió","#fff",BLUE,INK,12)
b+=box(280,64,190,56,"Tháp giải nhiệt","#fff",GRN,INK,12)
b+=box(280,146,190,56,"Quạt hút thải","#fff",AMB,INK,12)
b+=box(510,100,150,66,"Tiết kiệm lớn","#fff",VIO,INK,12,"chạy nhiều giờ/ngày")
for y in (92,174): b+=arr(230,y,278,y,STEEL,2.2)
for y in (92,174): b+=arr(470,y,508,y,STEEL,2.2)
b+=T(360,248,"HVAC: tải thay đổi theo giờ, theo mùa",11.5,MUT,"middle")
save("app-vfd-hvac",W,H,b,"Biến tần trong các cụm HVAC")

b=box(60,64,190,56,"Trước: chạy trực tiếp","#fff",AMB,INK,12,"đóng/cắt, bóp van")
b+=arr(252,92,300,92,STEEL,2.6)
b+=box(300,64,190,56,"Sau: có biến tần","#fff",GRN,INK,12,"tốc độ theo nhu cầu")
b+=box(520,64,140,56,"Đo lại","#fff",VIO,INK,12,"xác nhận tiết kiệm")
items=["Giữ nguyên động cơ nếu còn tốt","Kiểm tra cách điện trước khi lắp",
       "Mở hết van / damper sau retrofit","Ghi lại thông số vào hồ sơ máy"]
for i,t in enumerate(items):
    x=60+(i%2)*310; y=148+(i//2)*52
    b+=f"<rect x='{x}' y='{y}' width='290' height='40' rx='7' fill='#fff' stroke='{BD}'/>"
    b+=f"<path d='M{x+16} {y+20} l7 8 l13 -15' fill='none' stroke='{GRN}' stroke-width='2.6'/>"
    b+=T(x+46,y+25,t,11,INK)
save("app-vfd-retrofit",W,H,b,"Quy trình retrofit thực tế")

b=box(60,100,150,64,"Tủ biến tần","#fff",BLUE,INK,12,"tại nhà máy")
b+=box(260,100,150,64,"Kết nối","#fff",TEAL,INK,12,"có dây / 4G")
b+=box(460,100,200,64,"Người vận hành","#fff",VIO,INK,12,"điện thoại · máy tính")
b+=arr(210,132,258,132,BLUE,2.6)+arr(410,132,458,132,TEAL,2.6)
b+=T(360,216,"cảnh báo tức thời khi có mã lỗi hoặc dòng bất thường",11.5,INK,"middle","700")
b+=T(360,244,"giảm thời gian phát hiện sự cố từ hàng giờ xuống vài phút",11,MUT,"middle")
save("app-vfd-monitor",W,H,b,"Giám sát biến tần từ xa")

# ================= COMP (so sánh) =================
cols=[("Sao – tam giác",STEEL,["Rẻ nhất","Vẫn sốc dòng","Không đổi tốc độ"]),
      ("Khởi động mềm",AMB,["Khởi động êm","Không tiết kiệm điện","Không đổi tốc độ"]),
      ("Biến tần",GRN,["Khởi động êm","Tiết kiệm điện","Đổi tốc độ tự do"])]
b=""
for i,(name,c,rows) in enumerate(cols):
    x=60+i*205
    b+=f"<rect x='{x}' y='58' width='185' height='196' rx='10' fill='#fff' stroke='{c}' stroke-width='2'/>"
    b+=f"<rect x='{x}' y='58' width='185' height='36' rx='10' fill='{c}' opacity='0.14'/>"
    b+=T(x+92,82,name,12.5,INK,"middle","700")
    for j,r in enumerate(rows): b+=T(x+92,124+j*38,r,11.5,MUT,"middle")
save("comp-vfd-khoidongmem",W,H,b,"Sao–tam giác · khởi động mềm · biến tần")

b=box(60,70,270,72,"Điện trở xả","#fff",AMB,INK,13,"đốt năng lượng thành nhiệt")
b+=box(60,166,270,72,"Hoàn năng lượng (AFE)","#fff",GRN,INK,13,"trả điện về lưới")
rows=[("Chi phí đầu tư","Thấp","Cao"),("Toả nhiệt trong tủ","Nhiều","Ít"),
      ("Tiết kiệm điện","Không","Có"),("Phù hợp","hãm thưa","hãm liên tục")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(370,y+24,k,11.5,INK,"start","700")+T(540,y+24,a,11.5,AMB,"middle","700")+T(636,y+24,bb,11.5,GRN,"middle","700")
save("comp-vfd-regen",W,H,b,"Điện trở xả so với hoàn năng lượng")

b=box(60,70,280,74,"Động cơ không đồng bộ (IM)","#fff",STEEL,INK,12,"phổ biến, rẻ, bền")
b+=box(60,166,280,74,"Động cơ nam châm (PM)","#fff",VIO,INK,12,"hiệu suất cao hơn")
rows=[("Hiệu suất","Tiêu chuẩn","Cao hơn"),("Giá động cơ","Thấp","Cao"),
      ("Chạy trực tiếp lưới","Được","Không"),("Yêu cầu biến tần","Tùy chọn","Bắt buộc")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(376,y+24,k,11.5,INK,"start","700")+T(552,y+24,a,11.5,STEEL,"middle","700")+T(648,y+24,bb,11.5,VIO,"middle","700")
save("comp-motor-im-pm",W,H,b,"Động cơ IM so với PM")

cols=[("Dây cứng (DI/AO)",STEEL,["Đơn giản","Nhiều dây","Không đọc lỗi"]),
      ("Modbus RTU",BLUE,["2 dây cho cả tuyến","Đọc được trạng thái","Tốc độ vừa"]),
      ("Fieldbus Ethernet",VIO,["Nhanh nhất","Chẩn đoán tốt","Chi phí cao hơn"])]
b=""
for i,(name,c,rows) in enumerate(cols):
    x=60+i*205
    b+=f"<rect x='{x}' y='58' width='185' height='196' rx='10' fill='#fff' stroke='{c}' stroke-width='2'/>"
    b+=f"<rect x='{x}' y='58' width='185' height='36' rx='10' fill='{c}' opacity='0.14'/>"
    b+=T(x+92,82,name,12,INK,"middle","700")
    for j,r in enumerate(rows): b+=T(x+92,124+j*38,r,11.5,MUT,"middle")
save("comp-fieldbus",W,H,b,"Ba cách kết nối biến tần")

b=axes(90,64,540,160,"thời gian","dòng tiền tích lũy")
b+=line(90,144,630,144,STEEL,1.6)
b+=f"<path d='M90 210 L150 210 L630 96' fill='none' stroke='{GRN}' stroke-width='3'/>"
b+=f"<circle cx='334' cy='144' r='7' fill='{GRN}'/>"
b+=T(334,132,"điểm hoàn vốn",11,GRN,"middle","700")
b+=T(120,232,"chi phí đầu tư ban đầu",11,MUT,"start")
b+=T(560,86,"lợi ích tích lũy",11,GRN,"middle","700")
save("comp-vfd-roi",W,H,b,"Đường hoàn vốn của dự án biến tần")

b=box(60,70,280,74,"Chỉ khoá điện (LOTO)","#fff",GRN,INK,12,"an toàn khi bảo trì")
b+=box(60,166,280,74,"Chỉ dùng STO","#fff",AMB,INK,12,"dừng nhanh khi vận hành")
rows=[("Cách ly nguồn","Có","Không"),("Tụ DC còn điện","Đã xả","Vẫn còn"),
      ("Dùng khi bảo trì","Bắt buộc","Không đủ"),("Dùng khi vận hành","Chậm","Phù hợp")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(376,y+24,k,11.5,INK,"start","700")+T(548,y+24,a,11.5,GRN,"middle","700")+T(646,y+24,bb,11.5,AMB,"middle","700")
save("comp-loto-sto",W,H,b,"Khoá điện so với STO")

b=box(60,70,270,72,"Chỉ lắp cuộn kháng","#fff",AMB,INK,13,"giảm sóng hài cơ bản")
b+=box(60,166,270,72,"Lọc sóng hài chủ động","#fff",GRN,INK,13,"bù theo thời gian thực")
rows=[("Chi phí","Thấp","Cao"),("Mức giảm THD","Vừa","Mạnh"),
      ("Nhiều biến tần","Từng máy","Cả tủ"),("Khi cần","THD chưa gắt","Có ràng buộc THD")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(370,y+24,k,11.5,INK,"start","700")+T(544,y+24,a,11.5,AMB,"middle","700")+T(644,y+24,bb,11.5,GRN,"middle","700")
save("comp-loc-song-hai",W,H,b,"Hai cách xử lý sóng hài")

print("done: gen_diagrams8 ->", OUT)
