#!/usr/bin/env python3
# Diagrams for the PLC troubleshooting article (khắc phục lỗi PLC – mọi hãng).
# Same light-card house style as gen_diagrams2/3/4.py.
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
def varr(x,y1,y2,c=WIRE,w=2.5):
    return (f"<line x1='{x}' y1='{y1}' x2='{x}' y2='{y2}' stroke='{c}' stroke-width='{w}'/>"
            f"<polygon points='{x},{y2} {x-5},{y2-9} {x+5},{y2-9}' fill='{c}'/>")
def led(cx,cy,color,lit=True,r=8):
    glow=f"<circle cx='{cx}' cy='{cy}' r='{r+5}' fill='{color}' opacity='0.22'/>" if lit else ""
    fill=color if lit else "#e4e9f1"
    stroke=color if lit else "#c3ccdb"
    return glow+f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"
def save(name,w,h,body,title):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(frame(w,h,body,title))

W,H=720,270

# ---------- REPRESENTATIVE: a PLC showing a fault (ERR lit) ----------
plc = f"<rect x='150' y='70' width='210' height='140' rx='12' fill='#fff' stroke='{RED}' stroke-width='2.5'/>"
plc += f"<rect x='166' y='86' width='178' height='40' rx='6' fill='#0f1720'/>" + T(255,113,'ERR',22,'#ff8a8a','middle','700')
plc += "".join(f"<circle cx='{178+k*47}' cy='198' r='4' fill='{RED}'/>" for k in range(4))
plc += T(255,158,'PLC',15,INK,'middle','700')
lx=430; rep = plc
rep += led(lx,95,GREEN,lit=False) + T(lx+18,100,'RUN — không chạy',12,INK,'start','700')
rep += led(lx,135,RED,lit=True)  + T(lx+18,140,'ERR — báo lỗi',12,INK,'start','700')
rep += led(lx,175,AMBER,lit=True)+ T(lx+18,180,'BAT — pin yếu',12,INK,'start','700')
rep += T(255,238,'PLC đang báo lỗi — đọc đèn để khoanh vùng',12.5,INK,'middle','700')
save("rep-plc-loi",W,H,rep,"Hình đại diện: PLC đang báo lỗi")

# ---------- PROCESS: 6-step troubleshooting flow (snake) ----------
steps=[("1. Đọc đèn báo","RUN / ERR / BAT + mã lỗi"),
       ("2. Kiểm tra nguồn","24VDC & 220V cấp"),
       ("3. Pin & chương trình","BAT · backup · nạp lại"),
       ("4. Soát I/O & đấu dây","cầu chì · terminal · cảm biến"),
       ("5. Kiểm tra truyền thông","Modbus / Ethernet / HMI"),
       ("6. Sửa hoặc thay","phục hồi & dự phòng")]
bw,bh=204,58
xs=[24,258,492]; y1,y2=64,168
fl=""
cols=[BLUE,AMBER,GREEN]
for i in range(3):
    fl+=box(xs[i],y1,bw,bh,steps[i][0],"#fff",cols[i],INK,12.5,steps[i][1])
fl+=arr(xs[0]+bw,y1+bh/2,xs[1],y1+bh/2)
fl+=arr(xs[1]+bw,y1+bh/2,xs[2],y1+bh/2)
fl+=varr(xs[2]+bw/2,y1+bh,y2)
cols2=[GREEN,BLUE,RED]
order=[2,1,0]
for j,i in enumerate([3,4,5]):
    xi=xs[order[j]]
    fl+=box(xi,y2,bw,bh,steps[i][0],"#fff",cols2[j],INK,12.5,steps[i][1])
fl+=arr(xs[2],y2+bh/2,xs[1]+bw,y2+bh/2)
fl+=arr(xs[1],y2+bh/2,xs[0]+bw,y2+bh/2)
save("flow-khac-phuc-loi-plc",W,H,fl,"Quy trình 6 bước khắc phục lỗi PLC")

# ---------- APPLICATION: 6 common fault groups ----------
groups=[("Nguồn","PLC không lên / chập chờn",AMBER),
        ("CPU & Pin nhớ","mất chương trình, lỗi CPU",RED),
        ("Ngõ vào / ra (I/O)","vào–ra không tác động",BLUE),
        ("Truyền thông","mất kết nối Modbus / HMI",GREEN),
        ("Chương trình / scan","WDT, treo, sai logic",WIRE),
        ("Môi trường","nhiệt · nhiễu · ẩm · rung",STEEL)]
gw,gh=214,74
gx=[24,254,484]; gy=[58,152]
ap=""
for idx,(name,sym,col) in enumerate(groups):
    x=gx[idx%3]; y=gy[idx//3]
    ap+=box(x,y,gw,gh,name,"#fff",col,INK,13.5,sym)
    ap+=f"<rect x='{x}' y='{y}' width='6' height='{gh}' rx='3' fill='{col}'/>"
save("app-nhom-loi-plc",W,H,ap,"6 nhóm lỗi PLC thường gặp")

print("wrote: rep-plc-loi, flow-khac-phuc-loi-plc, app-nhom-loi-plc -> assets/diagrams/")
