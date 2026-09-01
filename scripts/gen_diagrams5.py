#!/usr/bin/env python3
# ei3 (IIoT bảo mật / gateway / CPS) diagrams: representative / principle / application.
import os
OUT="/home/user/SEO-web/assets/diagrams"; os.makedirs(OUT,exist_ok=True)
BG="#f6f8fb"; BD="#d6deea"; INK="#1c2836"; MUT="#5a6b80"
BLUE="#0072CE"; GREEN="#12a06a"; AMBER="#d9862a"; RED="#e5484d"; WIRE="#48607a"; STEEL="#8794a6"; VIO="#6b4fd8"
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
def arr(x1,y1,x2,y2,c=WIRE,w=2.5,dash=""):
    d=f"stroke-dasharray='{dash}'" if dash else ""
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}' {d}/>"
            f"<polygon points='{x2},{y2} {x2-9},{y2-5} {x2-9},{y2+5}' fill='{c}'/>")
def save(name,w,h,body,title): open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))
def cloud(cx,cy,c=BLUE,label="Private Cloud"):
    s=(f"<path d='M{cx-46} {cy+12} a20 20 0 0 1 4 -39 a26 26 0 0 1 50 -6 a18 18 0 0 1 16 22 a16 16 0 0 1 -8 23 Z' "
       f"fill='#eef4fc' stroke='{c}' stroke-width='2'/>")
    s+=T(cx,cy+6,label,11.5,c,"middle","700")
    return s
def gw(x,y,w,h,label,accent=BLUE,sub=""):
    s=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='#fff' stroke='{accent}' stroke-width='2.5'/>"
    s+=f"<rect x='{x+10}' y='{y+10}' width='{w-20}' height='8' rx='3' fill='#dbe6f7'/>"
    for k in range(4): s+=f"<circle cx='{x+14+k*((w-28)/3)}' cy='{y+h-9}' r='3' fill='{accent}'/>"
    s+=T(x+w/2,y+h/2+6,label,12.5,INK,"middle","700")
    if sub: s+=T(x+w/2,y+h+16,sub,10.5,MUT,"middle")
    return s
def factory(x,y,c=STEEL):
    return (f"<path d='M{x} {y+40} L{x} {y+16} L{x+20} {y+28} L{x+20} {y+16} L{x+40} {y+28} L{x+40} {y+40} Z' "
            f"fill='#e6ecf5' stroke='{c}' stroke-width='2'/>")
def shield(cx,cy,r=34,c=BLUE):
    return (f"<path d='M{cx} {cy-r} L{cx+r*0.8} {cy-r*0.55} L{cx+r*0.8} {cy+r*0.15} "
            f"Q{cx+r*0.8} {cy+r*0.8} {cx} {cy+r} Q{cx-r*0.8} {cy+r*0.8} {cx-r*0.8} {cy+r*0.15} "
            f"L{cx-r*0.8} {cy-r*0.55} Z' fill='#eef4fc' stroke='{c}' stroke-width='2.5'/>")

W,H=720,270

# ---------- REPRESENTATIVE ----------
save("rep-gateway-ei3",W,H,
  gw(300,95,140,90,"Amphion",BLUE,"gateway edge · DIN-rail")
  +arr(370,95,370,60,GREEN)+T(430,72,"outbound-only",11,GREEN,"start","700")
  +cloud(600,80,BLUE)
  +T(360,235,"Gateway kết nối bảo mật ei3",13,INK,"middle","700"),"Hình đại diện")

save("rep-gateway-virtual",W,H,
  box(280,95,180,90,"Bộ điều khiển / edge có sẵn","#eef3fb",STEEL,INK,11,"")
  +box(315,120,110,44,"Zethus","#fff",BLUE,INK,12,"container phần mềm")
  +arr(370,95,370,60,GREEN)+cloud(600,80,BLUE)
  +T(360,235,"Gateway ảo (container) — không thêm phần cứng",12.5,INK,"middle","700"),"Hình đại diện")

save("rep-platform",W,H,
  box(60,70,150,130,"Thiết bị edge","#fff",BLUE,INK,12,"máy · PLC")
  +arr(210,135,255,135,GREEN)+box(255,70,150,130,"Mạng quản lý","#eef3fb",VIO,INK,12,"zero-trust")
  +arr(405,135,450,135,GREEN)+box(450,70,90,130,"Private\nCloud","#fff",BLUE,INK,11,"")
  +box(450,70,90,130,"","#fff",BLUE)+T(495,130,"Private",12,INK,"middle","700")+T(495,148,"Cloud",12,INK,"middle","700")
  +arr(540,135,585,135,GREEN)+box(585,70,110,130,"Ứng dụng","#fff",GREEN,INK,12,"IIoT")
  +T(360,235,"Kiến trúc CPS: edge → mạng quản lý → cloud → app",12.5,INK,"middle","700"),"Hình đại diện")

save("rep-analytics",W,H,
  ''.join(f"<circle cx='{120}' cy='{90+k*32}' r='6' fill='{BLUE}'/>" for k in range(4))
  +T(120,205,"dữ liệu máy",11,MUT,"middle")
  +''.join(arr(140,90+k*32,250,140,STEEL,1.6) for k in range(4))
  +f"<circle cx='300' cy='140' r='46' fill='#eef4fc' stroke='{VIO}' stroke-width='2.5'/>"+T(300,138,"AI",20,VIO,"middle","700")+T(300,160,"ConnectedAI",10.5,MUT,"middle")
  +arr(350,140,470,140,GREEN)
  +box(470,105,200,70,"Insight vận hành","#fff",GREEN,INK,12,"nguyên nhân gốc · dự đoán")
  +T(360,235,"Phân tích dữ liệu máy bằng AI",12.5,INK,"middle","700"),"Hình đại diện")

save("rep-app",W,H,
  f"<rect x='250' y='70' width='220' height='130' rx='10' fill='#fff' stroke='{BLUE}' stroke-width='2.5'/>"
  +f"<rect x='250' y='70' width='220' height='26' rx='10' fill='#eef4fc'/>"+T(360,88,"ei3 · Dashboard",11,BLUE,"middle","700")
  +f"<rect x='268' y='110' width='55' height='70' rx='4' fill='#dbe6f7'/>"
  +f"<rect x='333' y='140' width='55' height='40' rx='4' fill='#cfeede'/>"
  +f"<rect x='398' y='120' width='55' height='60' rx='4' fill='#fbe6d6'/>"
  +T(360,235,"Ứng dụng IIoT ei3 (dashboard/cảnh báo)",12.5,INK,"middle","700"),"Hình đại diện")

save("rep-security",W,H,
  shield(360,135,56,BLUE)
  +f"<rect x='344' y='125' width='32' height='26' rx='4' fill='#fff' stroke='{BLUE}' stroke-width='2'/>"
  +f"<path d='M350 125 v-8 a10 10 0 0 1 20 0 v8' fill='none' stroke='{BLUE}' stroke-width='2'/>"
  +T(360,225,"Zero-Trust · bảo vệ hệ thống cyber-physical",12.5,INK,"middle","700"),"Hình đại diện")

# ---------- PRINCIPLE ----------
save("prin-outbound",W,H,
  factory(70,120)+box(60,95,120,70,"Máy / gateway","#fff",BLUE,INK,11,"trong nhà máy")
  +f"<rect x='300' y='80' width='70' height='110' rx='8' fill='#fdeede' stroke='{RED}' stroke-width='2'/>"+T(335,72,"Firewall",11,RED,"middle","700")
  +f"<line x1='335' y1='90' x2='335' y2='180' stroke='{RED}' stroke-width='2' stroke-dasharray='4 4'/>"
  +arr(180,120,300,120,GREEN)+T(240,110,"đi RA (mã hoá)",10.5,GREEN,"middle","700")
  +f"<line x1='300' y1='150' x2='250' y2='150' stroke='{RED}' stroke-width='2.5'/><line x1='262' y1='142' x2='250' y2='158' stroke='{RED}' stroke-width='2.5'/>"+T(255,175,"không mở cổng VÀO",10,RED,"middle","700")
  +arr(370,120,470,120,GREEN)+cloud(560,105,BLUE)
  ,"Nguyên lý outbound-only: máy chủ động kết nối RA, không mở cổng vào")

save("prin-zerotrust",W,H,
  box(50,105,120,60,"Người dùng /","#fff",BLUE,INK,11,"thiết bị")
  +arr(170,135,225,135)
  +box(225,100,120,70,"Xác thực","#eef4fc",VIO,INK,12,"mọi phiên")
  +arr(345,135,400,135)
  +box(400,100,130,70,"Kiểm tra liên tục","#eef4fc",VIO,INK,11,"không tin ngầm")
  +arr(530,135,585,135,GREEN)
  +box(585,105,110,60,"Máy / dữ liệu","#fff",GREEN,INK,11,"")
  +T(360,205,"mọi người dùng · thiết bị · kết nối đều phải xác thực & giám sát",11,MUT,"middle")
  ,"Nguyên lý Zero-Trust: không tin tưởng ngầm theo vị trí mạng")

save("prin-ai",W,H,
  box(50,100,150,70,"Tín hiệu thô","#fff",BLUE,INK,12,"rung · nhiệt · chu kỳ")
  +arr(200,135,250,135)
  +f"<circle cx='320' cy='135' r='44' fill='#eef4fc' stroke='{VIO}' stroke-width='2.5'/>"+T(320,132,"AI",18,VIO,"middle","700")+T(320,153,"mô hình",10,MUT,"middle")
  +arr(365,135,420,135)
  +box(420,100,120,70,"Nguyên nhân gốc","#eef4fc",GREEN,INK,11,"& dự đoán")
  +arr(540,135,590,135,GREEN)
  +box(590,100,110,70,"Hành động","#fff",GREEN,INK,11,"bảo trì · tối ưu")
  ,"Nguyên lý: dữ liệu → mô hình AI → insight → hành động")

# ---------- APPLICATION ----------
save("app-fleet",W,H,
  ''.join(factory(60+i*70,150,STEEL)+T(80+i*70,210,f"NM{i+1}",10,MUT,"middle") for i in range(3))
  +''.join(arr(100+i*70,150,300,120,STEEL,1.6) for i in range(3))
  +cloud(360,105,BLUE)
  +arr(410,110,480,110,GREEN)
  +box(480,80,210,70,"Trung tâm / Dashboard","#fff",GREEN,INK,12,"giám sát toàn đội máy")
  +T(230,235,"kết nối nhiều nhà máy về một nền tảng an toàn",12,MUT,"middle")
  ,"Ứng dụng: quản lý fleet máy nhiều nhà máy (190.000+ tài sản)")

save("app-oee",W,H,
  ''.join(f"<circle cx='{150+k*180}' cy='120' r='40' fill='#fff' stroke='{[GREEN,AMBER,BLUE][k]}' stroke-width='4' "
          f"stroke-dasharray='{[210,170,230][k]} 260'/>"+T(150+k*180,126,['85%','72%','96%'][k],16,INK,'middle','700')
          +T(150+k*180,185,['Khả dụng','Hiệu suất','Chất lượng'][k],11.5,MUT,'middle') for k in range(3))
  +T(360,235,"Dashboard OEE thời gian thực",12.5,INK,"middle","700"),"Ứng dụng: theo dõi OEE (A · P · Q)")

save("app-remote-service",W,H,
  box(60,105,140,70,"Kỹ sư / PC","#fff",GREEN,INK,12,"từ xa")
  +arr(200,140,270,140,GREEN)+T(235,130,"VPN mã hoá",10,GREEN,"middle","700")
  +cloud(330,120,BLUE,"ei3 cloud")
  +arr(385,140,455,140,GREEN)
  +f"<rect x='455' y='90' width='70' height='110' rx='8' fill='#fdeede' stroke='{RED}' stroke-width='2'/>"+T(490,82,"Firewall",10.5,RED,"middle","700")
  +box(545,105,140,70,"Máy trong NM","#fff",BLUE,INK,11,"chẩn đoán từ xa")
  +arr(525,140,545,140,GREEN)
  +T(360,235,"truy cập & xử lý sự cố máy từ xa an toàn",12,MUT,"middle"),"Ứng dụng: remote service an toàn (zero-trust)")

print("ei3 diagrams saved. total svg:", len([f for f in os.listdir(OUT) if f.endswith('.svg')]))
