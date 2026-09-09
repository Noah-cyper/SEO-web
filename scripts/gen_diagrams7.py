#!/usr/bin/env python3
# Biến tần (VFD) diagrams — 5 vai trò/bài: rep · prin · spec · app · comp
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
def line(x1,y1,x2,y2,c=WIRE,w=2.5): return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
def save(name,w,h,body,title): open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

# ---- blocks ----
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
    s+=T(cx,cy+r+20,label,12,INK,"middle","700")
    return s
def pump(cx,cy,r=30,accent=TEAL):
    s=f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#eef6f6' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<path d='M{cx-14} {cy} a14 14 0 0 1 28 0 a14 14 0 0 1 -28 0' fill='none' stroke='{accent}' stroke-width='2'/>"
    s+=T(cx,cy+6,"P",16,INK,"middle","700")
    return s
def fan(cx,cy,r=30,accent=BLUE):
    s=f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#eef3fb' stroke='{accent}' stroke-width='2.5'/>"
    for a in (0,120,240):
        s+=f"<path d='M{cx} {cy} q18 -14 26 4 q-14 8 -26 -4' fill='{accent}' opacity='0.55' transform='rotate({a} {cx} {cy})'/>"
    return s
def grid3(x,y,label="Lưới 3 pha"):
    s=""
    for k in range(3): s+=line(x,y+k*14,x+52,y+k*14,AMB,3)
    s+=T(x+26,y+58,label,11.5,INK,"middle","700")
    return s

W,H=720,290

# ================= REPRESENTATIVE =================
save("rep-bien-tan",W,H, vfd(300,70,120,160,"Biến tần (VFD)")
  +grid3(140,110,"Lưới vào")+arr(200,124,300,124,AMB)
  +arr(420,124,530,124,GRN)+motor(600,124,34)
  +T(360,262,"Biến tần điều khiển tốc độ động cơ 3 pha",13,INK,"middle","700"),"Hình đại diện")

save("rep-bien-tan-1p3p",W,H,
  ''.join(line(120,110+k*16,180,110+k*16,AMB,3) for k in range(2))+T(150,158,"1 pha 220V",11.5,INK,"middle","700")
  +arr(190,118,290,118,AMB)+vfd(290,65,130,165,"Biến tần 1P→3P")
  +arr(420,118,520,118,GRN)+''.join(line(520,102+k*16,570,102+k*16,GRN,3) for k in range(3))
  +motor(630,118,32,GRN,"ĐC 3 pha")
  +T(360,268,"Vào 1 pha 220V — ra 3 pha 220V cho động cơ",12.5,INK,"middle","700"),"Hình đại diện")

save("rep-bien-tan-loi",W,H, vfd(300,70,120,160,"")
  +f"<rect x='314' y='84' width='92' height='30' rx='4' fill='#2a0f13'/>"+T(360,105,"OC.1",14,"#ff8a8a","middle","700")
  +f"<circle cx='470' cy='110' r='26' fill='#fdeede' stroke='{RED}' stroke-width='2.5'/>"+T(470,118,"!",22,RED,"middle","700")
  +T(470,158,"Báo lỗi",11.5,RED,"middle","700")
  +T(360,262,"Biến tần báo mã lỗi trên màn hình",13,INK,"middle","700"),"Hình đại diện")

save("rep-tu-dien-bien-tan",W,H,
  f"<rect x='230' y='55' width='260' height='190' rx='8' fill='#eef3fb' stroke='{WIRE}' stroke-width='2.5'/>"
  +T(360,48,"Tủ điện",12,INK,"middle","700")
  +f"<rect x='248' y='70' width='60' height='36' rx='4' fill='#fff' stroke='{AMB}'/>"+T(278,93,"MCCB",10,INK,"middle","700")
  +vfd(320,70,150,120,"Biến tần")
  +f"<rect x='248' y='118' width='60' height='36' rx='4' fill='#fff' stroke='{VIO}'/>"+T(278,141,"Lọc",10,INK,"middle","700")
  +f"<rect x='248' y='166' width='222' height='30' rx='4' fill='#fff' stroke='{TEAL}'/>"+T(359,186,"Cuộn kháng · thanh cái",10.5,INK,"middle","700")
  +''.join(f"<path d='M{250+k*20} 210 l10 18 l10 -18' fill='none' stroke='{STEEL}' stroke-width='1.6'/>" for k in range(11))
  +T(360,262,"Bố trí biến tần trong tủ điện",13,INK,"middle","700"),"Hình đại diện")

save("rep-bien-tan-bom",W,H, vfd(180,70,110,150,"Biến tần")
  +arr(290,120,360,120,GRN)+motor(400,120,30)+line(432,120,470,120,STEEL,6)
  +pump(510,120,32)+line(542,120,610,120,TEAL,8)
  +T(610,100,"→ đường ống",11,MUT,"start")
  +T(360,262,"Biến tần điều khiển bơm nước",13,INK,"middle","700"),"Hình đại diện")

# ================= PRINCIPLE =================
save("prin-vfd-pwm",W,H,
  grid3(60,100,"AC vào")
  +arr(120,114,175,114,AMB)+box(175,80,110,80,"Chỉnh lưu","#fdf0e0",AMB,INK,12,"AC→DC")
  +arr(285,120,335,120)+box(335,80,110,80,"Tụ DC","#eef4fc",VIO,INK,12,"lọc phẳng")
  +arr(445,120,495,120)+box(495,80,120,80,"Nghịch lưu","#e8f5ee",GRN,INK,12,"IGBT · PWM")
  +arr(615,120,672,120,GRN)
  +T(360,200,"Điện lưới cố định 50Hz → một chiều → tạo lại AC với tần số thay đổi",12,MUT,"middle")
  +T(360,228,"Đổi tần số ⇒ đổi tốc độ động cơ · giữ tỉ lệ V/f để mô-men ổn định",12,INK,"middle","700")
  ,"Nguyên lý biến tần: AC → DC → AC (PWM)")

save("prin-vf-ratio",W,H,
  line(90,220,640,220,WIRE,2)+line(90,220,90,70,WIRE,2)
  +T(70,140,"U",12,INK,"middle","700")+T(650,236,"f (Hz)",11,MUT,"start")
  +f"<line x1='90' y1='220' x2='430' y2='90' stroke='{BLUE}' stroke-width='3'/>"
  +f"<line x1='430' y1='90' x2='620' y2='90' stroke='{RED}' stroke-width='3'/>"
  +f"<line x1='430' y1='90' x2='430' y2='220' stroke='{STEEL}' stroke-width='1.6' stroke-dasharray='4 4'/>"
  +T(430,238,"50 Hz",11,INK,"middle","700")
  +T(250,120,"vùng V/f không đổi",11.5,BLUE,"middle","700")+T(250,142,"mô-men giữ nguyên",11,MUT,"middle")
  +T(530,118,"vùng suy giảm từ thông",11.5,RED,"middle","700")+T(530,140,"mô-men giảm dần",11,MUT,"middle")
  ,"Nguyên lý V/f: giữ tỉ lệ điện áp trên tần số")

save("prin-affinity",W,H,
  T(80,80,"Luật đồng dạng (bơm · quạt)",13,INK,"start","700")
  +box(60,105,180,60,"Lưu lượng","#eef3fb",BLUE,INK,12,"Q ∝ n")
  +box(265,105,180,60,"Cột áp","#eef6f6",TEAL,INK,12,"H ∝ n²")
  +box(470,105,190,60,"Công suất","#e8f5ee",GRN,INK,12,"P ∝ n³")
  +T(360,205,"Giảm tốc độ 20% ⇒ công suất còn ≈ 51%",13.5,GRN,"middle","700")
  +T(360,235,"Đây là lý do biến tần tiết kiệm điện rất mạnh cho bơm và quạt",11.5,MUT,"middle")
  ,"Nguyên lý tiết kiệm điện: quan hệ bậc ba của công suất")

save("prin-vfd-pid",W,H,
  box(50,105,120,60,"Đặt (SP)","#fff",BLUE,INK,12,"áp suất mong muốn")
  +arr(170,135,215,135)
  +f"<circle cx='235' cy='135' r='20' fill='#fff' stroke='{VIO}' stroke-width='2'/>"+T(235,141,"Σ",16,VIO,"middle","700")
  +arr(255,135,300,135)+box(300,105,110,60,"PID","#eef4fc",VIO,INK,13,"trong biến tần")
  +arr(410,135,455,135,GRN)+vfd(455,80,80,110,"")+T(495,200,"Biến tần",11,INK,"middle","700")
  +arr(535,135,575,135,GRN)+motor(615,135,26,GRN,"bơm")
  +line(615,161,615,225,STEEL,2)+line(615,225,235,225,STEEL,2)+arr(235,225,235,157,STEEL,2)
  +T(420,245,"phản hồi từ cảm biến áp suất (4-20mA)",11,MUT,"middle")
  ,"Nguyên lý PID: giữ áp suất ổn định bằng cách đổi tốc độ bơm")

save("prin-vfd-nhieu",W,H,
  vfd(120,90,110,120,"Biến tần")
  +''.join(f"<path d='M{240+k*8} {110+k*6} q10 -10 20 0' fill='none' stroke='{RED}' stroke-width='1.8' opacity='0.7'/>" for k in range(5))
  +T(300,95,"nhiễu tần số cao",11,RED,"middle","700")
  +box(390,90,120,55,"Cáp cảm biến","#fff",BLUE,INK,11,"tín hiệu yếu")
  +box(390,160,120,55,"Truyền thông","#fff",TEAL,INK,11,"RS485")
  +f"<circle cx='585' cy='120' r='24' fill='#fdeede' stroke='{RED}' stroke-width='2'/>"+T(585,127,"!",18,RED,"middle","700")
  +T(585,162,"sai số · mất kết nối",10.5,RED,"middle","700")
  +T(360,255,"IGBT đóng cắt rất nhanh ⇒ phát nhiễu ra cáp và đất",12,MUT,"middle")
  ,"Nguyên lý phát sinh nhiễu EMC từ biến tần")

save("prin-vfd-loi",W,H,
  vfd(60,90,100,120,"")
  +box(200,75,150,50,"Quá dòng (OC)","#fdeede",RED,INK,11,"tăng tốc quá nhanh · kẹt tải")
  +box(200,135,150,50,"Quá áp (OV)","#fdf0e0",AMB,INK,11,"giảm tốc nhanh · tải kéo")
  +box(200,195,150,50,"Quá nhiệt (OH)","#fdeede",RED,INK,11,"quạt bẩn · tủ nóng")
  +box(400,75,150,50,"Quá tải (OL)","#fdf0e0",AMB,INK,11,"chọn thiếu công suất")
  +box(400,135,150,50,"Thấp áp (LV)","#eef3fb",BLUE,INK,11,"sụt áp nguồn")
  +box(400,195,150,50,"Chạm đất (GF)","#fdeede",RED,INK,11,"cách điện hỏng")
  +T(630,140,"Đọc mã lỗi",11.5,INK,"middle","700")+T(630,162,"→ tra sổ tay",11,MUT,"middle")
  ,"Nguyên lý: nhóm lỗi biến tần theo nguyên nhân")

# ================= SPEC / CẤU TẠO =================
save("spec-vfd-parts",W,H,
  f"<rect x='60' y='70' width='600' height='150' rx='10' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +box(78,90,110,110,"Chỉnh lưu","#fdf0e0",AMB,INK,11,"diode/SCR")
  +box(198,90,110,110,"Tụ DC bus","#eef4fc",VIO,INK,11,"lọc & tích năng")
  +box(318,90,110,110,"IGBT","#e8f5ee",GRN,INK,11,"nghịch lưu")
  +box(438,90,110,110,"Vi điều khiển","#eef3fb",BLUE,INK,11,"thuật toán")
  +box(558,90,90,110,"Tản nhiệt","#f2f4f7",STEEL,INK,11,"+ quạt")
  +T(360,250,"Các khối chính bên trong một biến tần",12.5,INK,"middle","700")
  ,"Cấu tạo bên trong biến tần")

save("spec-vfd-dauday",W,H,
  grid3(70,95,"R · S · T")
  +arr(130,109,200,109,AMB)+f"<rect x='200' y='75' width='50' height='60' rx='4' fill='#fff' stroke='{AMB}'/>"+T(225,110,"CB",11,INK,"middle","700")
  +arr(250,105,300,105,AMB)+vfd(300,60,130,170,"")
  +T(365,50,"L1 L2 L3  →  U V W",11.5,INK,"middle","700")
  +arr(430,105,500,105,GRN)+motor(560,105,30,GRN,"Động cơ")
  +f"<path d='M365 232 l0 22' stroke='{TEAL}' stroke-width='2.5'/>"
  +''.join(f"<line x1='{352+k*7}' y1='{258+k*4}' x2='{378-k*7}' y2='{258+k*4}' stroke='{TEAL}' stroke-width='2.5'/>" for k in range(3))
  +T(410,266,"nối đất PE bắt buộc",11,TEAL,"start","700")
  ,"Cấu tạo đấu dây động lực: vào R/S/T — ra U/V/W")

save("spec-vfd-dieukhien",W,H,
  vfd(60,80,110,140,"")
  +box(220,70,150,45,"DI — ngõ vào số","#eef3fb",BLUE,INK,11,"chạy/dừng · đảo chiều")
  +box(220,125,150,45,"AI — ngõ vào analog","#e8f5ee",GRN,INK,11,"0-10V · 4-20mA")
  +box(220,180,150,45,"RS485 — Modbus","#eef6f6",TEAL,INK,11,"điều khiển từ PLC")
  +box(430,70,150,45,"AO — ngõ ra analog","#fdf0e0",AMB,INK,11,"phản hồi tần số")
  +box(430,125,150,45,"Relay — ngõ ra","#fdeede",RED,INK,11,"báo lỗi · đang chạy")
  +box(430,180,150,45,"Biến trở ngoài","#fff",VIO,INK,11,"chỉnh tay tốc độ")
  +''.join(line(170,150,220,92+k*55,STEEL,1.6) for k in range(3))
  +T(360,262,"Các kiểu ra lệnh và lấy tín hiệu từ biến tần",12.5,INK,"middle","700")
  ,"Cấu tạo mạch điều khiển biến tần")

save("spec-vfd-sizing",W,H,
  box(50,95,150,70,"Công suất ĐC","#eef3fb",BLUE,INK,12,"kW trên nhãn")
  +arr(200,130,240,130)
  +box(240,95,150,70,"Dòng định mức","#e8f5ee",GRN,INK,12,"A — quan trọng nhất")
  +arr(390,130,430,130)
  +box(430,95,230,70,"Chọn biến tần","#fdf0e0",AMB,INK,12,"I biến tần ≥ I động cơ")
  +T(360,205,"Chọn theo DÒNG, không chỉ theo kW — tải nặng cần chọn dư 1 cấp",12.5,INK,"middle","700")
  +T(360,235,"Kiểm tra thêm: loại tải · số lần khởi động/giờ · nhiệt độ tủ · độ cao lắp đặt",11.5,MUT,"middle")
  ,"Cấu tạo bài toán chọn công suất biến tần")

save("spec-vfd-emc",W,H,
  grid3(60,100,"Nguồn")
  +arr(120,114,165,114,AMB)+box(165,85,95,60,"Lọc EMC","#eef4fc",VIO,INK,11,"đầu vào")
  +arr(260,115,300,115)+box(300,85,95,60,"Cuộn kháng","#eef6f6",TEAL,INK,11,"AC reactor")
  +arr(395,115,435,115)+vfd(435,70,95,120,"")
  +arr(530,115,570,115,GRN)+box(570,85,90,60,"Cáp bọc","#e8f5ee",GRN,INK,11,"che chắn")
  +T(360,215,"Lọc + cuộn kháng + cáp bọc + nối đất đúng = giảm nhiễu hiệu quả",12.5,INK,"middle","700")
  +T(360,245,"Cáp động lực và cáp tín hiệu phải đi riêng máng, cắt nhau vuông góc",11.5,MUT,"middle")
  ,"Cấu tạo giải pháp chống nhiễu EMC")

save("spec-vfd-thongso",W,H,
  f"<rect x='150' y='60' width='420' height='180' rx='10' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +T(360,82,"Nhóm thông số cần cài đầu tiên",12.5,BLUE,"middle","700")
  +''.join([T(175,110,"• Thông số động cơ: U, I, f, tốc độ, cosφ",12),
            T(175,136,"• Nguồn lệnh chạy: bàn phím · terminal · Modbus",12),
            T(175,162,"• Nguồn đặt tần số: biến trở · AI · truyền thông",12),
            T(175,188,"• Thời gian tăng tốc / giảm tốc (ACC/DEC)",12),
            T(175,214,"• Giới hạn tần số min/max · bảo vệ quá tải",12)])
  +T(360,266,"Cài đúng thông số động cơ trước — sai ở đây gây lỗi về sau",12,MUT,"middle")
  ,"Cấu tạo bộ thông số cơ bản của biến tần")

save("spec-vfd-baotri",W,H,
  f"<rect x='120' y='60' width='480' height='185' rx='10' fill='#fff' stroke='{TEAL}' stroke-width='2.5'/>"
  +T(360,84,"Checklist bảo trì định kỳ",12.5,TEAL,"middle","700")
  +''.join([T(145,112,"☐ Vệ sinh bụi tản nhiệt & lưới lọc gió",12),
            T(145,138,"☐ Kiểm tra quạt làm mát có quay êm không",12),
            T(145,164,"☐ Siết lại đầu cốt động lực (nguội, đã cắt điện)",12),
            T(145,190,"☐ Đo nhiệt độ tủ, kiểm tra thông gió",12),
            T(145,216,"☐ Xem lịch sử lỗi & tuổi tụ DC bus",12)])
  +T(360,268,"Bụi và nhiệt là hai nguyên nhân hỏng biến tần phổ biến nhất",12,MUT,"middle")
  ,"Cấu tạo quy trình bảo trì biến tần")

# ================= APPLICATION =================
save("app-vfd-bom",W,H,
  vfd(60,85,100,120,"Biến tần")+arr(160,130,215,130,GRN)+motor(250,130,28)+line(278,130,310,130,STEEL,6)
  +pump(345,130,28)+line(373,130,470,130,TEAL,8)
  +f"<circle cx='500' cy='130' r='22' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"+T(500,136,"P",13,INK,"middle","700")
  +T(500,168,"cảm biến áp",10.5,MUT,"middle")
  +line(500,108,500,80,STEEL,2)+line(500,80,110,80,STEEL,2)+arr(110,80,110,85,STEEL,2)
  +box(555,105,120,50,"Bồn / mạng ống","#eef6f6",TEAL,INK,11,"")
  +T(360,255,"Giữ áp suất ổn định, bơm chỉ chạy đúng nhu cầu",12,MUT,"middle")
  ,"Ứng dụng: biến tần cho hệ bơm nước")

save("app-vfd-quat",W,H,
  vfd(70,85,100,120,"Biến tần")+arr(170,130,225,130,GRN)+motor(258,130,26)+line(284,130,320,130,STEEL,6)
  +fan(360,130,32)
  +f"<path d='M400 110 h90 M400 130 h110 M400 150 h90' stroke='{BLUE}' stroke-width='2' opacity='0.6'/>"
  +box(520,100,150,60,"Hệ thống ống gió","#eef3fb",BLUE,INK,11,"HVAC · hút bụi")
  +T(360,255,"Điều chỉnh lưu lượng gió bằng tốc độ thay vì đóng bớt van",12,MUT,"middle")
  ,"Ứng dụng: biến tần cho quạt và hệ thống gió")

save("app-vfd-bangtai",W,H,
  vfd(60,80,100,120,"Biến tần")+arr(160,125,210,125,GRN)+motor(240,125,24)
  +f"<circle cx='300' cy='180' r='22' fill='none' stroke='{STEEL}' stroke-width='3'/>"
  +f"<circle cx='600' cy='180' r='22' fill='none' stroke='{STEEL}' stroke-width='3'/>"
  +line(300,158,600,158,STEEL,4)+line(300,202,600,202,STEEL,4)
  +''.join(f"<rect x='{330+k*70}' y='138' width='34' height='20' rx='3' fill='#e8f5ee' stroke='{GRN}'/>" for k in range(4))
  +line(264,125,300,158,STEEL,2)
  +T(450,240,"đổi tốc độ băng tải theo nhịp sản xuất, khởi động êm",12,MUT,"middle")
  ,"Ứng dụng: biến tần cho băng tải")

save("app-vfd-plc",W,H,
  box(60,100,130,70,"PLC","#eef3fb",BLUE,INK,13,"lập trình")
  +arr(190,125,255,125,TEAL)+T(222,116,"RS485",10,TEAL,"middle","700")
  +vfd(255,70,110,140,"")+T(310,225,"Biến tần",11.5,INK,"middle","700")
  +arr(365,125,420,125,GRN)+motor(455,125,28)
  +box(545,95,130,70,"HMI / SCADA","#e8f5ee",GRN,INK,12,"giám sát")
  +line(125,100,125,60,STEEL,2)+line(125,60,610,60,STEEL,2)+arr(610,60,610,95,STEEL,2)
  +T(360,262,"PLC ra lệnh chạy/dừng và đặt tần số qua Modbus RTU",12,MUT,"middle")
  ,"Ứng dụng: điều khiển biến tần bằng PLC")

save("app-vfd-tietkiem",W,H,
  T(120,75,"Van tiết lưu (cũ)",12,RED,"start","700")+T(430,75,"Biến tần (mới)",12,GRN,"start","700")
  +f"<rect x='120' y='90' width='190' height='120' rx='8' fill='#fdeede' stroke='{RED}'/>"
  +f"<rect x='140' y='190' width='150' height='0' fill='{RED}'/>"
  +f"<rect x='150' y='110' width='130' height='85' rx='4' fill='{RED}' opacity='0.35'/>"
  +T(215,160,"100% điện",13,INK,"middle","700")+T(215,182,"bóp van, phí năng lượng",10.5,MUT,"middle")
  +f"<rect x='430' y='90' width='190' height='120' rx='8' fill='#e8f5ee' stroke='{GRN}'/>"
  +f"<rect x='460' y='152' width='130' height='43' rx='4' fill='{GRN}' opacity='0.45'/>"
  +T(525,145,"≈51% điện",13,INK,"middle","700")+T(525,182,"giảm tốc 20% theo P ∝ n³",10.5,MUT,"middle")
  +T(360,250,"Cùng một mức lưu lượng, cách điều khiển quyết định hoá đơn điện",12,MUT,"middle")
  ,"Ứng dụng: tiết kiệm điện so với van tiết lưu")

save("app-vfd-suachua",W,H,
  vfd(90,80,100,130,"")
  +box(240,80,150,55,"Kiểm tra cơ bản","#eef3fb",BLUE,INK,11,"nguồn · đầu cốt · quạt")
  +box(240,145,150,55,"Đọc mã lỗi","#fdf0e0",AMB,INK,11,"tra sổ tay hãng")
  +box(430,80,150,55,"Đo cách điện ĐC","#e8f5ee",GRN,INK,11,"loại trừ động cơ")
  +box(430,145,150,55,"Thử tải nhẹ","#eef6f6",TEAL,INK,11,"xác nhận")
  +''.join(line(190,145,240,107+k*65,STEEL,1.6) for k in range(2))
  +T(360,250,"Chẩn đoán theo thứ tự — đừng thay linh kiện khi chưa xác định nguyên nhân",12,MUT,"middle")
  ,"Ứng dụng: quy trình chẩn đoán khi biến tần báo lỗi")

# ================= COMPARE =================
save("comp-vf-vector",W,H,
  box(60,80,280,150,"","#eef3fb",BLUE)+T(200,105,"V/f (vô hướng)",14,BLUE,"middle","700")
  +T(80,135,"• Cài đặt đơn giản",12)+T(80,160,"• Chạy nhiều động cơ song song",12)
  +T(80,185,"• Mô-men khởi động vừa phải",12)+T(80,210,"→ bơm, quạt, tải nhẹ",11.5,BLUE,"start","700")
  +box(380,80,280,150,"","#e8f5ee",GRN)+T(520,105,"Vector",14,GRN,"middle","700")
  +T(400,135,"• Mô-men khởi động cao",12)+T(400,160,"• Giữ tốc độ chính xác khi tải đổi",12)
  +T(400,185,"• Cần cài đúng thông số ĐC",12)+T(400,210,"→ băng tải, nâng hạ, máy ép",11.5,GRN,"start","700")
  ,"So sánh chế độ điều khiển V/f và Vector")

save("comp-vfd-saobam",W,H,
  box(60,80,280,150,"","#fdf0e0",AMB)+T(200,105,"Khởi động sao–tam giác",14,AMB,"middle","700")
  +T(80,135,"• Rẻ, đơn giản",12)+T(80,160,"• Vẫn có cú giật khi chuyển",12)
  +T(80,185,"• Chỉ có 1 tốc độ chạy",12)+T(80,210,"→ tải đơn giản, ít khởi động",11.5,AMB,"start","700")
  +box(380,80,280,150,"","#e8f5ee",GRN)+T(520,105,"Biến tần",14,GRN,"middle","700")
  +T(400,135,"• Khởi động êm, không giật",12)+T(400,160,"• Đổi tốc độ tuỳ ý, tiết kiệm điện",12)
  +T(400,185,"• Bảo vệ động cơ tốt hơn",12)+T(400,210,"→ bơm, quạt, dây chuyền",11.5,GRN,"start","700")
  ,"So sánh: khởi động sao–tam giác và biến tần")

save("comp-vfd-tai",W,H,
  box(60,80,280,150,"","#eef6f6",TEAL)+T(200,105,"Tải bậc ba (bơm · quạt)",13.5,TEAL,"middle","700")
  +T(80,135,"• Mô-men tăng theo tốc độ²",12)+T(80,160,"• Chọn biến tần dòng tiêu chuẩn",12)
  +T(80,185,"• Tiết kiệm điện rất lớn",12)+T(80,210,"→ chọn đúng công suất là đủ",11.5,TEAL,"start","700")
  +box(380,80,280,150,"","#fdf0e0",AMB)+T(520,105,"Mô-men không đổi",13.5,AMB,"middle","700")
  +T(400,135,"• Băng tải, máy ép, nâng hạ",12)+T(400,160,"• Cần mô-men cao khi khởi động",12)
  +T(400,185,"• Nên chọn dư 1 cấp công suất",12)+T(400,210,"→ ưu tiên chế độ vector",11.5,AMB,"start","700")
  ,"So sánh: chọn biến tần theo loại tải")

save("comp-vfd-hang",W,H,
  f"<rect x='60' y='70' width='600' height='160' rx='10' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
  +T(360,92,"Tiêu chí so sánh khi chọn hãng biến tần",12.5,BLUE,"middle","700")
  +''.join([T(85,120,"• Sẵn hàng & thời gian giao",12), T(85,146,"• Có phụ tùng thay thế lâu dài",12),
            T(85,172,"• Hỗ trợ kỹ thuật tiếng Việt",12), T(85,198,"• Tài liệu & phần mềm dễ tìm",12),
            T(390,120,"• Dải công suất phù hợp",12), T(390,146,"• Tính năng cần (PID, Modbus…)",12),
            T(390,172,"• Chính sách bảo hành",12), T(390,198,"• Tổng chi phí sở hữu, không chỉ giá mua",12)])
  +T(360,258,"Hãng tốt nhất là hãng bạn mua được phụ tùng sau 5 năm",12,MUT,"middle")
  ,"So sánh: tiêu chí chọn hãng biến tần")

save("comp-sua-thay",W,H,
  box(60,80,280,150,"","#eef3fb",BLUE)+T(200,105,"Nên SỬA khi",14,BLUE,"middle","700")
  +T(80,135,"• Lỗi ngoại vi: quạt, bàn phím",12)+T(80,160,"• Máy còn mới, còn phụ tùng",12)
  +T(80,185,"• Chi phí sửa < 30–40% giá mới",12)+T(80,210,"• Có đơn vị sửa uy tín",11.5,BLUE,"start","700")
  +box(380,80,280,150,"","#e8f5ee",GRN)+T(520,105,"Nên THAY khi",14,GRN,"middle","700")
  +T(400,135,"• Cháy IGBT, hỏng nhiều khối",12)+T(400,160,"• Đời cũ, hết phụ tùng",12)
  +T(400,185,"• Đã sửa nhiều lần, hay lỗi lại",12)+T(400,210,"• Dừng máy gây thiệt hại lớn",11.5,GRN,"start","700")
  ,"So sánh: nên sửa hay nên thay biến tần")

save("comp-vfd-that-gia",W,H,
  box(60,80,280,150,"","#e8f5ee",GRN)+T(200,105,"Hàng chính hãng",14,GRN,"middle","700")
  +T(80,135,"• Tem, mã QR tra được",12)+T(80,160,"• Có CO/CQ, hoá đơn VAT",12)
  +T(80,185,"• Bảo hành chính hãng",12)+T(80,210,"• Vỏ, nhãn in sắc nét",11.5,GRN,"start","700")
  +box(380,80,280,150,"","#fdeede",RED)+T(520,105,"Hàng trôi nổi",14,RED,"middle","700")
  +T(400,135,"• Giá rẻ bất thường",12)+T(400,160,"• Không hoá đơn, không CO/CQ",12)
  +T(400,185,"• Tem mờ, sai font, seri lạ",12)+T(400,210,"• Rủi ro hỏng, mất bảo hành",11.5,RED,"start","700")
  ,"So sánh: nhận biết biến tần chính hãng")

print("VFD diagrams saved. total svg:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]))
