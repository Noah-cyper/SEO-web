#!/usr/bin/env python3
# Cảm biến lưu lượng — bộ sơ đồ cho chuỗi 20 bài
import os, math
OUT="/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT,exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#1f6feb"; GRN="#12a06a"; AMB="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"; VIO="#6b4fd8"; TEAL="#0e8f8f"
WATER="#3aa3d8"
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
def save(n,w,h,b,t): open(os.path.join(OUT,n+".svg"),"w",encoding="utf-8").write(frame(w,h,b,t))

# ---- khối dùng chung ----
def pipe(x,y,w,h=52,fill="#e9f2f8",stroke=STEEL):
    """ống nằm ngang"""
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='{stroke}' stroke-width='2.5'/>")
def flowarrows(x,y,w,n=4,c=WATER,lab=""):
    s=""
    step=w/(n+1)
    for k in range(n):
        xx=x+step*(k+1)-14
        s+=arr(xx,y,xx+26,y,c,2.6)
    if lab: s+=T(x+w/2,y-14,lab,11,c,"middle","700")
    return s
def txm(x,y,w=110,h=54,label="Bộ chuyển đổi",accent=BLUE):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<rect x='{x+10}' y='{y+9}' width='{w-20}' height='20' rx='3' fill='#0f1720'/>"
    s+=T(x+w/2,y+24,"12.4 m³/h",11,"#7ff0c0","middle","700")
    s+=T(x+w/2,y+46,label,10.5,MUT,"middle")
    return s
def axes(x,y,w,h,xl="",yl=""):
    s=line(x,y,x,y+h,STEEL,2)+line(x,y+h,x+w,y+h,STEEL,2)
    if xl: s+=T(x+w,y+h+18,xl,11,MUT,"end")
    if yl: s+=T(x-4,y-6,yl,11,MUT,"end")
    return s

W,H=720,290

# ================= REP =================
b=pipe(60,118,600)+flowarrows(60,144,600,5,WATER,"dòng chảy")
b+=f"<rect x='300' y='104' width='120' height='80' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='3'/>"
b+=T(360,150,"FLOW",14,BLUE,"middle","700")
b+=txm(300,32,120,54,"hiển thị & tín hiệu ra")
b+=line(360,86,360,104,BLUE,2.5)
b+=arr(424,144,560,144,GRN,2.6)+T(500,132,"4–20mA / xung",10.5,GRN,"middle","700")
b+=T(360,238,"đo lượng chất lỏng hoặc khí đi qua ống trong một đơn vị thời gian",11.5,MUT,"middle")
save("rep-cam-bien-luu-luong",W,H,b,"Cảm biến lưu lượng là gì")

b=pipe(60,118,600)+flowarrows(60,144,600,5,WATER)
b+=f"<rect x='296' y='96' width='128' height='96' rx='8' fill='#eef3fb' stroke='{BLUE}' stroke-width='3'/>"
b+=f"<rect x='288' y='108' width='16' height='72' rx='4' fill='{VIO}'/>"
b+=f"<rect x='416' y='108' width='16' height='72' rx='4' fill='{VIO}'/>"
b+=T(360,92,"cuộn kích từ",10.5,VIO,"middle","700")
b+=f"<circle cx='330' cy='144' r='6' fill='{AMB}'/><circle cx='390' cy='144' r='6' fill='{AMB}'/>"
b+=T(360,214,"điện cực tiếp xúc chất lỏng",11,AMB,"middle","700")
b+=txm(520,60,130,54)
b+=line(424,120,520,92,BLUE,2)
b+=T(180,238,"chỉ đo được chất lỏng DẪN ĐIỆN",12,INK,"middle","700")
save("rep-dong-ho-dien-tu",W,H,b,"Đồng hồ lưu lượng điện từ")

b=pipe(60,130,600,48)+flowarrows(60,154,600,5,WATER)
b+=f"<rect x='250' y='100' width='64' height='30' rx='5' fill='#fff' stroke='{TEAL}' stroke-width='2.5'/>"
b+=f"<rect x='410' y='178' width='64' height='30' rx='5' fill='#fff' stroke='{TEAL}' stroke-width='2.5'/>"
b+=T(282,120,"A",13,INK,"middle","700")+T(442,198,"B",13,INK,"middle","700")
b+=f"<path d='M282 130 L442 178' stroke='{TEAL}' stroke-width='2.4' stroke-dasharray='6 4'/>"
b+=T(362,160,"chùm siêu âm",10.5,TEAL,"middle","700")
b+=T(362,238,"kẹp ngoài ống — không cắt ống, không tiếp xúc môi chất",11.5,INK,"middle","700")
b+=txm(540,56,130,54)
save("rep-sieu-am-clamp",W,H,b,"Cảm biến siêu âm kẹp ngoài")

b=f"<path d='M110 150 L230 150 Q300 150 300 96 Q300 60 360 60 Q420 60 420 96 Q420 150 490 150 L610 150' fill='none' stroke='{VIO}' stroke-width='14' stroke-linecap='round'/>"
b+=arr(70,150,108,150,WATER,3)+arr(612,150,656,150,WATER,3)
b+=f"<ellipse cx='360' cy='60' rx='86' ry='22' fill='none' stroke='{AMB}' stroke-width='2' stroke-dasharray='5 4'/>"
b+=T(360,32,"ống dao động",11,AMB,"middle","700")
b+=T(360,200,"lực Coriolis làm ống xoắn — đo trực tiếp KHỐI LƯỢNG",12,INK,"middle","700")
b+=T(360,226,"đồng thời đo được khối lượng riêng và nhiệt độ",11,MUT,"middle")
save("rep-coriolis",W,H,b,"Lưu lượng kế Coriolis")

b=pipe(60,118,600)+flowarrows(60,144,300,3,WATER)
b+=f"<circle cx='400' cy='144' r='34' fill='none' stroke='{STEEL}' stroke-width='2.5'/>"
for a in range(0,360,45):
    r=math.radians(a)
    b+=f"<line x1='400' y1='144' x2='{400+31*math.cos(r):.0f}' y2='{144+31*math.sin(r):.0f}' stroke='{BLUE}' stroke-width='3'/>"
b+=f"<circle cx='400' cy='144' r='6' fill='{INK}'/>"
b+=flowarrows(440,144,220,2,WATER)
b+=f"<rect x='368' y='72' width='64' height='30' rx='5' fill='#fff' stroke='{GRN}' stroke-width='2.5'/>"
b+=T(400,92,"pickup",11,INK,"middle","700")
b+=T(400,214,"cánh tuabin quay — mỗi vòng sinh một số xung",11.5,INK,"middle","700")
b+=T(400,238,"tần số xung tỷ lệ với lưu lượng",11,MUT,"middle")
save("rep-tuabin",W,H,b,"Lưu lượng kế tuabin")

b=pipe(60,118,600)+flowarrows(60,144,220,2,WATER)
b+=f"<rect x='330' y='118' width='20' height='52' fill='{STEEL}'/>"
b+=T(340,106,"thanh cản",10.5,INK,"middle","700")
for k in range(4):
    x=380+k*62
    b+=f"<circle cx='{x}' cy='{130}' r='11' fill='none' stroke='{WATER}' stroke-width='2.2'/>"
    b+=f"<circle cx='{x+31}' cy='{158}' r='11' fill='none' stroke='{WATER}' stroke-width='2.2'/>"
b+=T(500,214,"xoáy Karman sinh luân phiên hai bên",11.5,INK,"middle","700")
b+=T(500,238,"tần số xoáy tỷ lệ với vận tốc dòng",11,MUT,"middle")
save("rep-vortex",W,H,b,"Lưu lượng kế vortex")

b=pipe(60,112,600,62)+flowarrows(60,143,200,2,WATER)
b+=f"<rect x='330' y='112' width='12' height='22' fill='{STEEL}'/><rect x='330' y='152' width='12' height='22' fill='{STEEL}'/>"
b+=T(336,100,"tấm orifice",10.5,INK,"middle","700")
b+=flowarrows(380,143,260,2,WATER)
b+=f"<circle cx='250' cy='112' r='7' fill='{AMB}'/><circle cx='430' cy='112' r='7' fill='{AMB}'/>"
b+=line(250,112,250,74,AMB,2)+line(430,112,430,74,AMB,2)
b+=line(250,74,430,74,AMB,2)
b+=box(280,44,120,44,"ΔP","#fff",AMB,INK,13)
b+=T(360,214,"thu hẹp dòng → chênh áp → tính ra lưu lượng",11.5,INK,"middle","700")
b+=T(360,238,"lưu lượng tỷ lệ với căn bậc hai của chênh áp",11,MUT,"middle")
save("rep-orifice",W,H,b,"Đo lưu lượng bằng chênh áp")

b=pipe(60,118,600,52,"#eef6fb")+flowarrows(60,144,600,5,TEAL,"khí")
b+=f"<rect x='344' y='72' width='32' height='72' rx='5' fill='#fff' stroke='{RED}' stroke-width='2.5'/>"
b+=T(360,64,"đầu dò nhiệt",10.5,RED,"middle","700")
b+=f"<circle cx='360' cy='128' r='7' fill='{RED}'/>"
for k in range(3):
    b+=f"<path d='M{372+k*7} 118 q6 -8 0 -16' fill='none' stroke='{RED}' stroke-width='1.6'/>"
b+=T(360,214,"khí mang nhiệt đi — đo công suất bù nhiệt",11.5,INK,"middle","700")
b+=T(360,238,"cho ra trực tiếp lưu lượng khối, không cần bù áp/nhiệt",11,MUT,"middle")
b+=txm(530,52,130,54)
save("rep-thermal-khi",W,H,b,"Cảm biến lưu lượng khí kiểu nhiệt")

b=pipe(60,118,600,56,"#e8ece4")
b+=flowarrows(60,146,600,5,"#6b7a52","nước thải có cặn")
for k in range(9):
    b+=f"<circle cx='{92+k*66}' cy='{160}' r='{4+(k%3)}' fill='#6b7a52' opacity='0.7'/>"
b+=f"<rect x='300' y='104' width='120' height='84' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='3'/>"
b+=T(360,152,"MAG",13,BLUE,"middle","700")
b+=T(360,224,"ống thông suốt, không vật cản trong dòng",11.5,INK,"middle","700")
b+=T(360,248,"lựa chọn mặc định cho nước thải và bùn",11,MUT,"middle")
save("rep-flow-nuocthai",W,H,b,"Đo lưu lượng nước thải")

b=pipe(60,118,600,52,"#fbf0e6")
b+=flowarrows(60,144,600,5,AMB,"hơi nước quá nhiệt")
b+=f"<rect x='300' y='106' width='110' height='76' rx='6' fill='#fff' stroke='{AMB}' stroke-width='3'/>"
b+=T(355,150,"VORTEX",11.5,AMB,"middle","700")
b+=box(452,66,110,46,"Áp suất","#fff",VIO,INK,11.5)
b+=box(578,66,100,46,"Nhiệt độ","#fff",RED,INK,11.5)
b+=line(507,112,430,124,VIO,2,)+line(628,112,440,130,RED,2)
b+=T(360,226,"bắt buộc bù áp suất và nhiệt độ để ra lưu lượng khối",11.5,INK,"middle","700")
save("rep-flow-hoi",W,H,b,"Đo lưu lượng hơi nước")

# ================= PRIN =================
b=pipe(150,110,420,70,"#eef3fb")
b+=f"<rect x='142' y='104' width='16' height='82' rx='4' fill='{VIO}'/>"
b+=f"<rect x='562' y='104' width='16' height='82' rx='4' fill='{VIO}'/>"
b+=T(360,94,"từ trường B",11,VIO,"middle","700")
for k in range(4): b+=arr(190+k*96,146,190+k*96+40,146,WATER,2.4)
b+=T(360,68,"chất lỏng dẫn điện chuyển động cắt từ trường",11.5,INK,"middle","700")
b+=f"<circle cx='360' cy='112' r='7' fill='{AMB}'/><circle cx='360' cy='178' r='7' fill='{AMB}'/>"
b+=line(360,112,360,60,AMB,1.8)+line(360,178,360,230,AMB,1.8)
b+=T(430,244,"sinh sức điện động tỷ lệ với vận tốc dòng",11.5,AMB,"middle","700")
b+=T(150,244,"U ∝ v",13,INK,"start","700")
save("prin-faraday",W,H,b,"Nguyên lý cảm ứng điện từ (Faraday)")

b=pipe(80,120,560,60,"#eef6fb")
b+=box(160,66,80,38,"A","#fff",TEAL,INK,13)
b+=box(480,196,80,38,"B","#fff",TEAL,INK,13)
b+=f"<path d='M200 104 L520 196' stroke='{GRN}' stroke-width='2.6'/>"
b+=T(300,128,"xuôi dòng: nhanh hơn",10.5,GRN,"middle","700")
b+=f"<path d='M520 196 L200 104' stroke='{RED}' stroke-width='2.6' stroke-dasharray='6 4'/>"
b+=T(430,178,"ngược dòng: chậm hơn",10.5,RED,"middle","700")
b+=flowarrows(240,150,240,3,WATER)
b+=T(360,262,"chênh lệch thời gian truyền tỷ lệ với vận tốc dòng",11.5,INK,"middle","700")
save("prin-transit-time",W,H,b,"Nguyên lý siêu âm chênh lệch thời gian")

b=f"<path d='M120 150 L220 150 Q290 150 290 100 Q290 66 360 66 Q430 66 430 100 Q430 150 500 150 L600 150' fill='none' stroke='{STEEL}' stroke-width='12' stroke-linecap='round' opacity='0.4'/>"
b+=f"<path d='M120 158 L220 158 Q290 158 290 112 Q290 82 360 78 Q430 74 430 108 Q430 158 500 158 L600 158' fill='none' stroke='{VIO}' stroke-width='11' stroke-linecap='round'/>"
b+=T(360,40,"ống bị xoắn khi có dòng chảy",11.5,VIO,"middle","700")
b+=arr(200,196,268,196,GRN,2.4)+T(234,214,"vào",10.5,GRN,"middle","700")
b+=arr(452,196,520,196,GRN,2.4)+T(486,214,"ra",10.5,GRN,"middle","700")
b+=T(360,246,"độ lệch pha giữa hai đầu ống ∝ lưu lượng khối",12,INK,"middle","700")
b+=T(360,268,"tần số dao động ∝ khối lượng riêng",11,MUT,"middle")
save("prin-coriolis",W,H,b,"Nguyên lý Coriolis")

b=axes(90,64,250,150,"lưu lượng","tần số xung")
b+=f"<path d='M90 200 L300 84' fill='none' stroke='{GRN}' stroke-width='3'/>"
b+=T(210,76,"tuyến tính trong dải làm việc",10.5,GRN,"middle","700")
b+=f"<path d='M90 200 Q110 190 130 176' fill='none' stroke='{RED}' stroke-width='3'/>"
b+=T(140,212,"phi tuyến ở",10,RED,"middle","700")+T(140,226,"lưu lượng thấp",10,RED,"middle","700")
b+=box(400,80,260,50,"Hệ số K (xung/lít)","#fff",BLUE,INK,12,"do nhà sản xuất hiệu chuẩn")
b+=box(400,150,260,50,"Cần đoạn ống thẳng","#fff",AMB,INK,12,"để dòng ổn định trước cánh")
b+=T(530,240,"độ nhớt thay đổi làm lệch hệ số K",11,RED,"middle","700")
save("prin-tuabin",W,H,b,"Nguyên lý tuabin và hệ số K")

b=pipe(70,116,580,56,"#eef6fb")
b+=f"<rect x='200' y='116' width='18' height='56' fill='{STEEL}'/>"
for k in range(5):
    x=250+k*78
    b+=f"<circle cx='{x}' cy='{130}' r='12' fill='none' stroke='{WATER}' stroke-width='2.3'/>"
    b+=f"<circle cx='{x+39}' cy='{158}' r='12' fill='none' stroke='{WATER}' stroke-width='2.3'/>"
b+=T(420,96,"xoáy sinh luân phiên trên – dưới",11,INK,"middle","700")
b+=T(360,206,"tần số xoáy f = St · v / d",13,INK,"middle","700")
b+=T(360,230,"St là hằng số Strouhal, gần như không đổi trong dải Reynolds làm việc",11,MUT,"middle")
b+=T(360,256,"⇒ tần số chỉ phụ thuộc vận tốc, không phụ thuộc môi chất",11.5,GRN,"middle","700")
save("prin-vortex",W,H,b,"Nguyên lý xoáy Karman")

b=pipe(70,104,580,72,"#eef6fb")
b+=f"<rect x='330' y='104' width='12' height='26' fill='{STEEL}'/><rect x='330' y='150' width='12' height='26' fill='{STEEL}'/>"
b+=axes(90,196,240,70)
b+=f"<path d='M90 210 L200 210 L228 252 L300 236' fill='none' stroke='{AMB}' stroke-width='2.6'/>"
b+=T(210,268,"áp suất tụt tại chỗ thu hẹp",10.5,AMB,"middle","700")
b+=T(470,206,"Q ∝ √ΔP",16,INK,"middle","700")
b+=T(470,236,"chênh áp gấp 4 lần thì lưu lượng chỉ gấp 2",11,MUT,"middle")
b+=T(470,260,"⇒ dải đo hữu dụng hẹp hơn các công nghệ khác",11.5,RED,"middle","700")
save("prin-bernoulli-dp",W,H,b,"Nguyên lý chênh áp và căn bậc hai")

b=pipe(70,110,580,60,"#eef6fb")+flowarrows(70,140,580,5,TEAL,"khí")
b+=f"<circle cx='300' cy='140' r='13' fill='{RED}'/>"
b+=T(300,92,"đầu dò được sấy nóng",10.5,RED,"middle","700")
b+=f"<circle cx='430' cy='140' r='13' fill='{BLUE}'/>"
b+=T(430,92,"đầu dò tham chiếu",10.5,BLUE,"middle","700")
for k in range(3):
    b+=f"<path d='M{316+k*8} 130 q6 -9 0 -18' fill='none' stroke='{RED}' stroke-width='1.6'/>"
b+=T(360,208,"khí chảy qua mang nhiệt đi — càng nhiều khí, càng mất nhiệt nhanh",11.5,INK,"middle","700")
b+=T(360,234,"đo công suất cần để giữ chênh nhiệt ⇒ ra lưu lượng khối",11.5,GRN,"middle","700")
b+=T(360,260,"kết quả phụ thuộc thành phần khí — phải khai đúng loại khí",11,RED,"middle","700")
save("prin-thermal-mass",W,H,b,"Nguyên lý đo khối lượng bằng nhiệt")

b=T(180,62,"Chảy tầng (Re thấp)",12,INK,"middle","700")
b+=pipe(70,80,220,70,"#eef6fb")
b+=f"<path d='M80 115 Q180 78 280 115' fill='none' stroke='{WATER}' stroke-width='2.6'/>"
for k in range(5): b+=arr(100+k*36,115,100+k*36+22,115,WATER,1.8)
b+=T(180,170,"biên dạng nhọn, đỉnh ở giữa",10.5,MUT,"middle")
b+=T(530,62,"Chảy rối (Re cao)",12,INK,"middle","700")
b+=pipe(420,80,230,70,"#eef6fb")
b+=f"<path d='M430 115 Q470 92 530 92 Q590 92 640 115' fill='none' stroke='{GRN}' stroke-width='2.6'/>"
for k in range(5): b+=arr(450+k*38,115,450+k*38+24,115,GRN,1.8)
b+=T(535,170,"biên dạng phẳng — đo chính xác hơn",10.5,MUT,"middle")
b+=T(360,214,"Nhiều loại cảm biến yêu cầu dòng ổn định, biên dạng đầy đủ",12,INK,"middle","700")
b+=T(360,244,"⇒ vì sao phải có đoạn ống thẳng trước và sau cảm biến",11.5,AMB,"middle","700")
save("prin-flow-profile",W,H,b,"Biên dạng dòng chảy và độ chính xác")

b=box(60,64,180,56,"Đọc số 0","#fff",RED,INK,12,"dù có dòng chảy")
b+=box(270,64,180,56,"Số nhảy loạn","#fff",AMB,INK,12,"không ổn định")
b+=box(480,64,180,56,"Sai lệch dần","#fff",VIO,INK,12,"so với thực tế")
b+=box(60,150,180,56,"Bọt khí trong ống","#fff",WATER,INK,12,"nguyên nhân số 1")
b+=box(270,150,180,56,"Ống không đầy","#fff",WATER,INK,12,"lắp sai vị trí")
b+=box(480,150,180,56,"Đóng cặn, bám bẩn","#fff",STEEL,INK,12,"lệch dần theo tháng")
for x in (150,360,570): b+=arr(x,122,x,148,STEEL,2,"4 3")
b+=T(360,246,"triệu chứng ở hàng trên — nguyên nhân thường gặp ở hàng dưới",11.5,MUT,"middle")
save("prin-flow-loi",W,H,b,"Triệu chứng và nguyên nhân")

# ================= SPEC =================
items=["Môi chất: lỏng, khí hay hơi","Có dẫn điện không (quyết định MAG)","Dải lưu lượng nhỏ nhất – lớn nhất",
       "Đường kính và vật liệu ống","Áp suất và nhiệt độ làm việc","Độ chính xác yêu cầu",
       "Đo thể tích hay khối lượng","Tín hiệu ra và hệ điều khiển"]
b=""
for i,t in enumerate(items):
    x=60+(i%2)*310; y=58+(i//2)*54
    b+=f"<rect x='{x}' y='{y}' width='290' height='42' rx='7' fill='#fff' stroke='{BD}'/>"
    b+=f"<circle cx='{x+24}' cy='{y+21}' r='12' fill='{BLUE}' opacity='0.15'/>"
    b+=T(x+24,y+26,str(i+1),11.5,BLUE,"middle","700")+T(x+46,y+26,t,11,INK)
save("spec-flow-chon",W,H,b,"Tám câu hỏi trước khi chọn")

b=pipe(60,130,600,52)
b+=f"<rect x='330' y='118' width='60' height='76' rx='6' fill='#fff' stroke='{BLUE}' stroke-width='3'/>"
b+=line(150,120,150,196,AMB,2,)+line(330,120,330,196,AMB,2)
b+=f"<path d='M150 206 L330 206' stroke='{AMB}' stroke-width='2'/>"
b+=T(240,226,"đoạn thẳng trước (dài hơn)",11,AMB,"middle","700")
b+=line(390,120,390,196,GRN,2)+line(540,120,540,196,GRN,2)
b+=f"<path d='M390 206 L540 206' stroke='{GRN}' stroke-width='2'/>"
b+=T(465,226,"đoạn thẳng sau",11,GRN,"middle","700")
b+=f"<path d='M96 130 q16 26 0 52' fill='none' stroke='{RED}' stroke-width='3'/>"
b+=T(96,110,"co, van, bơm",10.5,RED,"middle","700")
b+=T(360,266,"tính theo số lần đường kính ống — tra tài liệu từng model",11.5,INK,"middle","700")
save("spec-flow-lapdat",W,H,b,"Yêu cầu đoạn ống thẳng")

rows=[("4–20mA","tín hiệu analog, chống nhiễu tốt, đi xa"),
      ("Xung / tần số","mỗi xung = một đơn vị thể tích, dùng để cộng dồn"),
      ("Modbus RTU","đọc nhiều giá trị: lưu lượng, tổng, nhiệt độ"),
      ("HART","4–20mA kèm dữ liệu số, cấu hình từ xa")]
b=""
for i,(k,v) in enumerate(rows):
    y=62+i*54
    b+=f"<rect x='60' y='{y}' width='600' height='44' rx='7' fill='#fff' stroke='{BD}'/>"
    b+=T(80,y+28,k,12.5,INK,"start","700")+T(230,y+28,v,11.5,MUT)
save("spec-flow-dauday",W,H,b,"Các kiểu tín hiệu đầu ra")

b=box(60,68,180,58,"Hiệu chuẩn ướt","#fff",WATER,INK,12,"dùng chất lỏng thật")
b+=box(270,68,180,58,"Hiệu chuẩn khô","#fff",AMB,INK,12,"mô phỏng tín hiệu")
b+=box(480,68,180,58,"So sánh tại chỗ","#fff",GRN,INK,12,"với thiết bị chuẩn")
b+=box(60,154,180,58,"Hệ số K","#fff",VIO,INK,12,"xung trên lít")
b+=box(270,154,180,58,"Điểm 0","#fff",VIO,INK,12,"kiểm khi không có dòng")
b+=box(480,154,180,58,"Giấy chứng nhận","#fff",TEAL,INK,12,"lưu vào hồ sơ")
b+=T(360,252,"kiểm điểm 0 là việc rẻ nhất và phát hiện được nhiều lỗi nhất",11.5,INK,"middle","700")
save("spec-flow-hieuchuan",W,H,b,"Các hình thức hiệu chuẩn")

b=axes(90,64,540,160,"lưu lượng (% dải đo)","sai số")
b+=f"<path d='M110 90 Q150 176 230 196 L620 200' fill='none' stroke='{RED}' stroke-width='3'/>"
b+=T(150,80,"sai số lớn ở lưu lượng thấp",10.5,RED,"middle","700")
b+=line(230,70,230,224,STEEL,1.6)
b+=T(232,66,"giới hạn dưới của dải làm việc",10.5,MUT,"start")
b+=f"<rect x='230' y='186' width='390' height='28' fill='{GRN}' opacity='0.12'/>"
b+=T(430,204,"vùng đo tin cậy",11,GRN,"middle","700")
b+=T(360,258,"chọn cỡ ống sao cho lưu lượng thường ngày nằm giữa dải đo",11.5,INK,"middle","700")
save("spec-flow-saiso",W,H,b,"Sai số theo phần trăm dải đo")

rows=[("m³/h","thể tích theo giờ — phổ biến nhất cho nước"),
      ("l/min","thể tích theo phút — máy móc, dây chuyền nhỏ"),
      ("kg/h","khối lượng theo giờ — hơi, khí, hóa chất"),
      ("Nm³/h","thể tích khí quy về điều kiện chuẩn"),
      ("m/s","vận tốc dòng — nhân tiết diện ra lưu lượng")]
b=""
for i,(k,v) in enumerate(rows):
    y=56+i*44
    b+=f"<rect x='60' y='{y}' width='600' height='36' rx='6' fill='#fff' stroke='{BD}'/>"
    b+=T(82,y+24,k,12.5,BLUE,"start","700")+T(200,y+24,v,11.5,MUT)
b+=T(360,278,"nhầm Nm³/h với m³/h là sai số rất lớn khi đo khí",11,RED,"middle","700")
save("spec-flow-donvi",W,H,b,"Đơn vị lưu lượng thường dùng")

# ================= APP =================
b=box(60,64,150,52,"Cấp nước","#fff",WATER,INK,12)
b+=box(60,140,150,52,"Nước thải","#fff",GRN,INK,12)
b+=box(240,64,150,52,"Hóa chất","#fff",VIO,INK,12)
b+=box(240,140,150,52,"Thực phẩm","#fff",AMB,INK,12)
b+=box(420,64,150,52,"Làm mát","#fff",TEAL,INK,12)
b+=box(420,140,150,52,"Tưới tiêu","#fff",GRN,INK,12)
b+=box(590,100,80,56,"MAG","#fff",BLUE,INK,13)
for y in (90,166):
    b+=arr(210,y,238,y,STEEL,2)+arr(390,y,418,y,STEEL,2)
b+=arr(570,90,588,110,BLUE,2)+arr(570,166,588,146,BLUE,2)
b+=T(360,242,"chất lỏng dẫn điện → đồng hồ điện từ là lựa chọn mặc định",11.5,INK,"middle","700")
save("app-flow-nuoc",W,H,b,"Ứng dụng đo lưu lượng chất lỏng")

b=pipe(60,112,300,46,"#eef6fb")+flowarrows(60,135,300,3,TEAL,"khí nén")
b+=f"<rect x='300' y='100' width='70' height='70' rx='6' fill='#fff' stroke='{TEAL}' stroke-width='3'/>"
b+=T(335,142,"FI",13,INK,"middle","700")
b+=pipe(370,112,290,46,"#eef6fb")+flowarrows(370,135,290,3,TEAL)
b+=box(60,196,180,56,"Phát hiện rò rỉ","#fff",RED,INK,12,"đo lúc không sản xuất")
b+=box(270,196,180,56,"Phân bổ chi phí","#fff",VIO,INK,12,"theo từng xưởng")
b+=box(480,196,180,56,"Theo dõi hiệu suất","#fff",GRN,INK,12,"máy nén khí")
b+=T(360,80,"đo lưu lượng khí nén: ba mục đích chính",11.5,MUT,"middle")
save("app-flow-khinen",W,H,b,"Đo lưu lượng khí nén")

b=f"<rect x='60' y='96' width='120' height='90' rx='8' fill='#fff' stroke='{RED}' stroke-width='2.5'/>"
b+=T(120,148,"Lò hơi",12.5,INK,"middle","700")
b+=pipe(180,124,180,36,"#fbf0e6")+flowarrows(180,142,180,2,AMB)
b+=f"<rect x='360' y='110' width='70' height='64' rx='6' fill='#fff' stroke='{AMB}' stroke-width='3'/>"
b+=T(395,148,"FT",13,INK,"middle","700")
b+=pipe(430,124,120,36,"#fbf0e6")+flowarrows(430,142,120,1,AMB)
b+=box(556,110,110,64,"Hộ tiêu thụ","#fff",TEAL,INK,11.5)
b+=box(300,202,180,48,"Bù P & T","#fff",VIO,INK,12,"bắt buộc với hơi")
b+=arr(395,198,395,178,VIO,2.2)
b+=T(150,222,"tính chi phí hơi theo từng bộ phận",11,MUT,"start")
save("app-flow-hoi",W,H,b,"Đo lưu lượng hơi trong nhà máy")

items=["Kiểm tra ống có đầy không","Xả bọt khí trong đường ống","So với thiết bị đo độc lập",
       "Kiểm tra điểm 0 khi đóng van","Vệ sinh điện cực / mặt cảm biến","Đối chiếu cấu hình với hồ sơ gốc"]
b=""
for i,t in enumerate(items):
    x=60+(i%2)*310; y=64+(i//2)*62
    b+=f"<rect x='{x}' y='{y}' width='290' height='48' rx='8' fill='#fff' stroke='{BD}'/>"
    b+=f"<path d='M{x+18} {y+24} l7 8 l13 -15' fill='none' stroke='{GRN}' stroke-width='2.6'/>"
    b+=T(x+48,y+29,t,11.5,INK)
save("app-flow-suachua",W,H,b,"Quy trình kiểm tra khi nghi ngờ sai số")

# ================= COMP =================
cols=[("Điện từ",BLUE,["Chỉ chất lỏng dẫn điện","Không cản dòng","Chính xác cao"]),
      ("Siêu âm",TEAL,["Kẹp ngoài được","Không cắt ống","Nhạy với bọt khí"]),
      ("Coriolis",VIO,["Đo khối lượng thật","Chính xác nhất","Đắt nhất"])]
b=""
for i,(n,c,rows) in enumerate(cols):
    x=60+i*205
    b+=f"<rect x='{x}' y='58' width='185' height='196' rx='10' fill='#fff' stroke='{c}' stroke-width='2'/>"
    b+=f"<rect x='{x}' y='58' width='185' height='36' rx='10' fill='{c}' opacity='0.14'/>"
    b+=T(x+92,82,n,12.5,INK,"middle","700")
    for j,r in enumerate(rows): b+=T(x+92,124+j*38,r,11.5,MUT,"middle")
save("comp-flow-congnghe",W,H,b,"Ba công nghệ đo phổ biến nhất")

b=box(60,70,270,72,"Lưu lượng thể tích","#fff",WATER,INK,13,"m³/h · l/min")
b+=box(60,166,270,72,"Lưu lượng khối","#fff",VIO,INK,13,"kg/h · Nm³/h")
rows=[("Phụ thuộc P, T","Có","Không"),("Dùng cho hơi, khí","Phải bù","Dùng thẳng"),
      ("Mua bán, cân bằng vật chất","Kém phù hợp","Phù hợp"),("Chi phí thiết bị","Thấp hơn","Cao hơn")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(368,y+24,k,11.5,INK,"start","700")+T(566,y+24,a,11.5,WATER,"middle","700")+T(650,y+24,bb,11.5,VIO,"middle","700")
save("comp-flow-tichkhoi",W,H,b,"Thể tích so với khối lượng")

b=box(60,70,270,72,"Lắp trong đường ống","#fff",BLUE,INK,13,"phải cắt ống")
b+=box(60,166,270,72,"Kẹp ngoài ống","#fff",TEAL,INK,13,"không dừng sản xuất")
rows=[("Phải dừng nước","Có","Không"),("Độ chính xác","Cao hơn","Thấp hơn"),
      ("Di chuyển sang ống khác","Không","Được"),("Phù hợp","Lắp cố định","Khảo sát, kiểm tra")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*46
    b+=T(368,y+24,k,11.5,INK,"start","700")+T(562,y+24,a,11.5,BLUE,"middle","700")+T(650,y+24,bb,11.5,TEAL,"middle","700")
save("comp-flow-clamp-inline",W,H,b,"Lắp trong ống so với kẹp ngoài")

b=axes(90,64,540,160,"chi phí đầu tư","độ chính xác")
pts=[(150,196,"Orifice",AMB),(240,168,"Tuabin",GRN),(330,140,"Vortex",TEAL),
     (430,112,"Điện từ",BLUE),(560,84,"Coriolis",VIO)]
for x,y,n,c in pts:
    b+=f"<circle cx='{x}' cy='{y}' r='10' fill='{c}'/>"
    b+=T(x,y-18,n,11,c,"middle","700")
b+=f"<path d='M150 196 Q330 150 560 84' fill='none' stroke='{STEEL}' stroke-width='1.6' stroke-dasharray='5 4'/>"
b+=T(360,258,"chính xác hơn thường đắt hơn — chọn theo yêu cầu thật, không theo tối đa",11.5,MUT,"middle")
save("comp-flow-chiphi",W,H,b,"Chi phí và độ chính xác")

b=box(60,70,290,74,"Lỗi do lắp đặt","#fff",AMB,INK,13,"thiếu ống thẳng, ống không đầy")
b+=box(60,168,290,74,"Lỗi do thiết bị","#fff",RED,INK,13,"hỏng cảm biến, mất hiệu chuẩn")
rows=[("Tần suất","Phổ biến hơn","Ít hơn"),("Chi phí sửa","Thấp","Cao"),
      ("Phát hiện bằng","Xem lại vị trí lắp","So với thiết bị chuẩn"),("Xử lý trước","Có","Sau")]
for i,(k,a,bb) in enumerate(rows):
    y=70+i*48
    b+=T(386,y+26,k,11.5,INK,"start","700")+T(570,y+26,a,11.5,AMB,"middle","700")+T(654,y+26,bb,11.5,RED,"middle","700")
save("comp-flow-loi",W,H,b,"Lỗi lắp đặt so với lỗi thiết bị")

print("done gen_diagrams9 ->",OUT)
