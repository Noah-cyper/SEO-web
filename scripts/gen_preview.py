#!/usr/bin/env python3
# Render all VI article .md files into one browsable preview HTML.
import re, os, glob, html as _html

ROOT = "/home/user/SEO-web/content/vi"

# Ordered clusters -> list of file basenames (relative to ROOT)
GROUPS = [
    ("Thiết bị đo lường", "do-luong", [
        "cam-bien-ap-suat-la-gi-cach-chon.md",
        "cam-bien-nhiet-do.md",
        "cam-bien-chenh-ap.md",
        "dong-ho-do-ap-suat-wika.md",
        "dau-day-cam-bien-ap-suat-4-20ma.md",
    ]),
    ("PLC", "plc", [
        "plc-mitsubishi-fx3u-la-gi.md",
    ]),
    ("Thiết bị khó tìm & hàng ngừng sản xuất", "kho-tim", [
        "thiet-bi-cong-nghiep-kho-tim.md",
        "linh-kien-tu-dong-hoa-ngung-san-xuat.md",
        "tim-cam-bien-transmitter-kho-tim.md",
        "thay-the-plc-module-doi-cu.md",
    ]),
    ("Seneca — Hãng & danh mục", "seneca-cat", [
        "seneca/seneca-viet-nam.md",
        "seneca/bo-chuyen-doi-tin-hieu-seneca.md",
        "seneca/remote-io-seneca-z-pc.md",
        "seneca/datalogger-rtu-seneca.md",
        "seneca/gateway-modbus-seneca.md",
        "seneca/dong-ho-do-dien-nang-seneca.md",
        "seneca/bo-hien-thi-seneca.md",
    ]),
    ("Seneca — Sản phẩm", "seneca-prod", [
        "seneca/k109s-seneca.md",
        "seneca/k109pt-seneca.md",
        "seneca/k109lv-seneca.md",
        "seneca/k121-seneca.md",
        "seneca/z109reg2-1-seneca.md",
        "seneca/k120-seneca.md","seneca/z109reg2-2-seneca.md","seneca/t121-seneca.md",
        "seneca/z-4rtd2-seneca.md",
        "seneca/z-8ai-seneca.md",
        "seneca/z-4ao-seneca.md",
        "seneca/z-10-d-in-seneca.md",
        "seneca/z-logger3-seneca.md",
        "seneca/z-gprs3-seneca.md",
        "seneca/z-umts-seneca.md",
        "seneca/z-lte-seneca.md",
        "seneca/z-key-seneca.md",
        "seneca/r-key-lt-seneca.md",
        "seneca/z-pass2-seneca.md",
        "seneca/r-pass-seneca.md",
        "seneca/s504-seneca.md",
        "seneca/s604-seneca.md",
        "seneca/s311a-seneca.md",
    ]),
]

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(t):
    t = esc(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a class="ilink" title="Liên kết nội bộ → \2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    return t

def render_table(rows):
    def cells(r):
        return [c.strip() for c in r.strip().strip("|").split("|")]
    head = cells(rows[0])
    body = rows[2:] if len(rows) > 2 else []
    h = "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>"
    b = "<tbody>" + "".join(
        "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>" for r in body
    ) + "</tbody>"
    return f'<div class="tablewrap"><table>{h}{b}</table></div>'

def convert(md):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r'<a\s+name="[^"]*"></a>', "", md)
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        s = lines[i].strip()
        if not s:
            i += 1; continue
        mimg = re.match(r'!\[(.*?)\]\((.*?)\)\s*$', s)
        if mimg:
            alt, src = mimg.group(1), mimg.group(2)
            fig = ""
            if "assets/diagrams/" in src:
                p = os.path.join("/home/user/SEO-web", src)
                if os.path.exists(p):
                    svg = open(p, encoding="utf-8").read()
                    fig = f"<figure class='diagram'>{svg}<figcaption>{inline(alt)}</figcaption></figure>"
            if not fig:
                fig = f"<figure class='diagram'><img src='{esc(src)}' alt='{esc(alt)}'/><figcaption>{inline(alt)}</figcaption></figure>"
            out.append(fig); i += 1; continue
        if s.startswith("|"):
            tbl = []
            while i < n and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip()); i += 1
            out.append(render_table(tbl)); continue
        if s == "---":
            out.append("<hr>"); i += 1; continue
        m = re.match(r"(#{2,4})\s+(.*)", s)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if s.startswith(">"):
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            out.append(f"<blockquote>{inline(' '.join(q))}</blockquote>"); continue
        if re.match(r"[-*]\s+", s):
            items = []
            while i < n and re.match(r"[-*]\s+", lines[i].strip()):
                it = re.sub(r"^[-*]\s+", "", lines[i].strip())
                mm = re.match(r"\[( |x)\]\s+(.*)", it)
                if mm:
                    ch = "checked" if mm.group(1) == "x" else ""
                    items.append(f'<li class="cb"><input type="checkbox" disabled {ch}> {inline(mm.group(2))}</li>')
                else:
                    items.append(f"<li>{inline(it)}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if re.match(r"\d+\.\s+", s):
            items = []
            while i < n and re.match(r"\d+\.\s+", lines[i].strip()):
                it = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                items.append(f"<li>{inline(it)}</li>"); i += 1
            out.append("<ol>" + "".join(items) + "</ol>"); continue
        para = [s]; i += 1
        while i < n:
            nx = lines[i].strip()
            if not nx or nx == "---":
                break
            if nx.startswith(("|", ">", "#")):
                break
            if re.match(r"[-*]\s+", nx) or re.match(r"\d+\.\s+", nx):
                break
            para.append(nx); i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)

def field(name, text):
    m = re.search(name + r"[^:\n]*:\s*(.*)", text)
    return m.group(1).strip() if m else ""

def parse(path):
    raw = open(path, encoding="utf-8").read()
    mc = re.search(r"<!--(.*?)-->", raw, re.S)
    cmt = mc.group(1) if mc else ""
    after = raw[mc.end():] if mc else raw
    slug = field("URL SLUG", cmt).split()[0] if field("URL SLUG", cmt) else ""
    loai = field("LOẠI TRANG", cmt)
    tukhoa = field("TỪ KHÓA", cmt)
    title_tag = field("TITLE TAG", after)
    meta_desc = field("META", after)
    h1 = field("H1", after)
    parts = after.split("\n---\n", 1)
    body_md = parts[1] if len(parts) > 1 else after
    return dict(slug=slug, loai=loai, tukhoa=tukhoa, title_tag=title_tag,
                meta_desc=meta_desc, h1=h1, body=convert(body_md))

def anchor(slug):
    return slug.strip("/").replace("/", "-") or "art"

def serp_crumbs(slug):
    parts = [p for p in slug.strip("/").split("/") if p]
    return "hoantrantdh.com" + ("".join(f" › {p}" for p in parts))

# ---- build ----
articles = []
nav = []
total = 0
for gtitle, gid, files in GROUPS:
    nav.append(f'<li class="nav-group">{esc(gtitle)}</li>')
    for f in files:
        d = parse(os.path.join(ROOT, f))
        a = anchor(d["slug"])
        total += 1
        nav.append(f'<li><a href="#{a}">{esc(d["h1"])}</a></li>')
        kw = " · ".join([k.strip() for k in d["tukhoa"].split("|")][:6])
        cover_path = os.path.join("/home/user/SEO-web/assets/covers", a + ".svg")
        cover = ""
        if os.path.exists(cover_path):
            svg = open(cover_path, encoding="utf-8").read()
            svg = re.sub(r'width="\d+"\s+height="\d+"', 'width="100%" height="auto"', svg, count=1)
            cover = f'<div class="cover">{svg}</div>'
        articles.append(f"""
<article id="{a}" class="art">
  {cover}
  <div class="art-tag">{esc(d["loai"])}</div>
  <h1>{inline(d["h1"])}</h1>
  <div class="serp" aria-label="Xem trước trên Google">
    <div class="serp-label">Xem trước kết quả Google</div>
    <div class="serp-url">{esc(serp_crumbs(d["slug"]))}</div>
    <div class="serp-title">{esc(d["title_tag"])}</div>
    <div class="serp-desc">{esc(d["meta_desc"])}</div>
  </div>
  <div class="prose">
    {d["body"]}
  </div>
  <div class="kw"><span>Từ khoá</span>{esc(kw)}</div>
  <a class="toplink" href="#top">↑ Lên đầu</a>
</article>""")

CSS = """
<style>
:root{
  --bg:#eef1f5; --surface:#ffffff; --surface-2:#f4f6f9;
  --ink:#18202c; --muted:#5c6a7a; --faint:#8b97a6;
  --accent:#1657b8; --accent-ink:#0f3f88; --accent-soft:#e4edfb;
  --signal:#b5620a; --signal-soft:#fbeede;
  --border:#dbe1e9; --border-strong:#c3ccd8;
  --serp-title:#1a4fc4; --serp-url:#3b6b45;
  --shadow:0 1px 2px rgba(24,32,44,.05),0 6px 20px rgba(24,32,44,.06);
  --mono:ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;
  --sans:-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
}
:root:not([data-theme="light"]){
  @media (prefers-color-scheme:dark){
  :root{}
  }
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0d1219; --surface:#151d28; --surface-2:#111823;
    --ink:#e7ecf3; --muted:#9aa7b7; --faint:#6b7887;
    --accent:#5b9bf0; --accent-ink:#8fbcf6; --accent-soft:#182740;
    --signal:#e0913f; --signal-soft:#2c2113;
    --border:#26303d; --border-strong:#333f4e;
    --serp-title:#8ab4f8; --serp-url:#8bcf9a;
    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 26px rgba(0,0,0,.35);
  }
}
[data-theme="dark"]{
  --bg:#0d1219; --surface:#151d28; --surface-2:#111823;
  --ink:#e7ecf3; --muted:#9aa7b7; --faint:#6b7887;
  --accent:#5b9bf0; --accent-ink:#8fbcf6; --accent-soft:#182740;
  --signal:#e0913f; --signal-soft:#2c2113;
  --border:#26303d; --border-strong:#333f4e;
  --serp-title:#8ab4f8; --serp-url:#8bcf9a;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 26px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  line-height:1.65;-webkit-font-smoothing:antialiased;font-size:16px}
a{color:var(--accent-ink)}
.masthead{background:var(--surface);border-bottom:1px solid var(--border);padding:34px 24px 26px}
.masthead-in{max-width:1180px;margin:0 auto}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);margin:0 0 10px}
.masthead h1{font-size:clamp(24px,3.4vw,36px);line-height:1.12;margin:0 0 8px;letter-spacing:-.02em;
  text-wrap:balance;font-weight:750}
.masthead p{margin:0;color:var(--muted);max-width:70ch}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.stat{background:var(--surface-2);border:1px solid var(--border);border-radius:999px;
  padding:6px 13px;font-size:13px;color:var(--muted)}
.stat b{color:var(--ink);font-variant-numeric:tabular-nums}
.layout{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:262px 1fr;gap:34px;
  padding:30px 24px 80px;align-items:start}
.toc{position:sticky;top:18px;max-height:calc(100vh - 36px);overflow:auto;
  background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:14px 12px}
.toc ul{list-style:none;margin:0;padding:0}
.toc li a{display:block;padding:7px 10px;border-radius:8px;color:var(--muted);
  text-decoration:none;font-size:13.5px;line-height:1.35}
.toc li a:hover{background:var(--accent-soft);color:var(--accent-ink)}
.nav-group{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);padding:14px 10px 6px;border-top:1px solid var(--border);margin-top:6px}
.nav-group:first-child{border-top:0;margin-top:0}
main{min-width:0}
.art{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:30px clamp(18px,3.4vw,44px) 26px;margin-bottom:26px;box-shadow:var(--shadow);scroll-margin-top:16px}
.cover{margin:-30px clamp(-18px,-3.4vw,-44px) 22px;border-radius:16px 16px 0 0;overflow:hidden;
  border-bottom:1px solid var(--border);line-height:0}
.cover svg{display:block;width:100%;height:auto}
.diagram{margin:22px 0}
.diagram svg{display:block;width:100%;height:auto;border-radius:12px}
.diagram img{display:block;width:100%;height:auto;border-radius:12px}
.diagram figcaption{margin-top:8px;font-size:12.5px;color:var(--muted);text-align:center;font-style:italic}
.art-tag{display:inline-block;font-family:var(--mono);font-size:11px;letter-spacing:.05em;
  color:var(--signal);background:var(--signal-soft);border:1px solid var(--border);
  padding:4px 10px;border-radius:6px;margin-bottom:14px}
.art h1{font-size:clamp(21px,2.6vw,29px);line-height:1.18;letter-spacing:-.015em;margin:0 0 18px;
  font-weight:750;text-wrap:balance}
.serp{background:var(--surface-2);border:1px solid var(--border);border-left:3px solid var(--accent);
  border-radius:10px;padding:14px 16px;margin:0 0 26px}
.serp-label{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);margin-bottom:8px}
.serp-url{font-size:12.5px;color:var(--serp-url);font-family:var(--mono);margin-bottom:3px;word-break:break-word}
.serp-title{color:var(--serp-title);font-size:19px;line-height:1.3;font-weight:500;margin-bottom:3px}
.serp-desc{color:var(--muted);font-size:13.5px;line-height:1.5}
.prose{max-width:72ch}
.prose h2{font-size:20px;margin:30px 0 12px;letter-spacing:-.01em;font-weight:700;
  padding-bottom:7px;border-bottom:1px solid var(--border)}
.prose h3{font-size:16.5px;margin:22px 0 8px;font-weight:650}
.prose h4{font-size:15px;margin:18px 0 6px;font-weight:650;color:var(--muted)}
.prose p{margin:12px 0}
.prose ul,.prose ol{margin:12px 0;padding-left:22px}
.prose li{margin:5px 0}
.prose li.cb{list-style:none;margin-left:-22px;padding-left:2px}
.prose li.cb input{margin-right:8px}
.prose strong{font-weight:680;color:var(--ink)}
.prose code{font-family:var(--mono);font-size:.87em;background:var(--surface-2);
  border:1px solid var(--border);border-radius:5px;padding:1px 5px}
.prose a.ilink{color:var(--accent-ink);text-decoration:underline;text-decoration-color:var(--border-strong);
  text-underline-offset:2px;cursor:help}
.prose blockquote{margin:16px 0;padding:12px 16px;background:var(--accent-soft);
  border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:var(--ink)}
.prose blockquote strong{color:var(--accent-ink)}
.prose hr{border:0;border-top:1px solid var(--border);margin:22px 0}
.tablewrap{overflow-x:auto;margin:16px 0;border:1px solid var(--border);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
thead th{background:var(--surface-2);text-align:left;padding:9px 12px;font-weight:650;
  border-bottom:1px solid var(--border-strong);white-space:nowrap}
tbody td{padding:9px 12px;border-bottom:1px solid var(--border);vertical-align:top}
tbody tr:last-child td{border-bottom:0}
.kw{margin-top:24px;padding-top:14px;border-top:1px dashed var(--border);font-size:12.5px;
  color:var(--muted);font-family:var(--mono);line-height:1.6}
.kw span{color:var(--faint);text-transform:uppercase;letter-spacing:.1em;font-size:10.5px;margin-right:8px}
.toplink{display:inline-block;margin-top:14px;font-size:12.5px;color:var(--faint);text-decoration:none}
.toplink:hover{color:var(--accent-ink)}
.foot{max-width:1180px;margin:0 auto;padding:0 24px 60px;color:var(--faint);font-size:13px}
@media (max-width:860px){
  .layout{grid-template-columns:1fr;gap:18px}
  .toc{position:static;max-height:none}
  body{font-size:15.5px}
}
</style>
"""

nav_html = "<ul>" + "\n".join(nav) + "</ul>"
page = f"""{CSS}
<div id="top"></div>
<header class="masthead"><div class="masthead-in">
  <p class="eyebrow">Nội dung SEO · hoantrantdh.com</p>
  <h1>Bản xem trước {total} bài viết đã soạn</h1>
  <p>Nội dung tiếng Việt sẵn đăng cho website thiết bị đo lường – tự động hoá. Mỗi bài kèm bản xem trước cách hiển thị trên Google (thẻ tiêu đề + mô tả + đường dẫn). Số liệu kỹ thuật ở mức tham khảo — cần đối chiếu datasheet hãng và điền giá thật trước khi đăng.</p>
  <div class="stats">
    <span class="stat"><b>{total}</b> bài viết</span>
    <span class="stat"><b>4</b> cụm chủ đề</span>
    <span class="stat"><b>14</b> trang Seneca</span>
    <span class="stat">Kèm SERP preview &amp; FAQ</span>
  </div>
</div></header>
<div class="layout">
  <nav class="toc" aria-label="Mục lục">{nav_html}</nav>
  <main>
    {''.join(articles)}
    <a class="toplink" href="#top">↑ Lên đầu trang</a>
  </main>
</div>
<footer class="foot">Bản xem trước tạo tự động từ các file nội dung · hoantrantdh.com</footer>
"""

out = "/tmp/claude-0/-home-user-SEO-web/a0f20c8b-045d-51bf-b68b-8d2c7f8a16e9/scratchpad/preview.html"
open(out, "w", encoding="utf-8").write(page)
print("wrote", out, "articles:", total, "bytes:", len(page))
