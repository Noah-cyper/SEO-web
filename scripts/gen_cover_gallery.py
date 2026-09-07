#!/usr/bin/env python3
"""Dựng trang thư viện ảnh bìa: xem toàn bộ cover của các bài trong content/vi.

    python3 scripts/gen_cover_gallery.py          # -> cover-gallery.html

Ảnh nhúng thẳng vào trang dưới dạng data URI (thu nhỏ 800px từ chính file .jpg
đã xuất) nên trang chạy được offline và không phụ thuộc đường dẫn ảnh.
Dùng lại bộ token màu của preview.html để hai trang nhìn đồng bộ.
"""
import os, re, io, ast, base64, html
from PIL import Image

ROOT = "/home/user/SEO-web"
CONTENT = f"{ROOT}/content/vi"
COVERS = f"{ROOT}/assets/covers"
THUMB_W, THUMB_Q = 800, 80

# lấy đúng danh sách nhóm/bài mà gen_meta_covers.py đang dùng
src = open(f"{ROOT}/scripts/gen_meta_covers.py", encoding="utf-8").read()
GROUPS = ast.literal_eval(re.search(r"^GROUPS = (\[.*?^\])", src, re.S | re.M).group(1))

def field(name, text):
    m = re.search(name + r"[^:\n]*:\s*(.*)", text)
    return m.group(1).strip() if m else ""

def kb(p):
    return f"{os.path.getsize(p) // 1024} KB" if os.path.exists(p) else "—"

def thumb(p):
    im = Image.open(p).convert("RGB")
    im = im.resize((THUMB_W, round(THUMB_W * im.height / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=THUMB_Q, optimize=True, progressive=True)
    return base64.b64encode(b.getvalue()).decode()

cards, n, missing = [], 0, []
for gtitle, _accent, files in GROUPS:
    items = []
    for f in files:
        raw = open(os.path.join(CONTENT, f), encoding="utf-8").read()
        cmt = re.search(r"<!--(.*?)-->", raw, re.S).group(1)
        slug = field("URL SLUG", cmt).split()[0]
        anchor = slug.strip("/").replace("/", "-") or "art"
        h1 = field("H1", raw[raw.index("TITLE TAG"):]) or anchor
        jpg = f"{COVERS}/{anchor}.jpg"
        if not os.path.exists(jpg):
            missing.append(anchor); continue
        items.append(dict(slug=slug, anchor=anchor, h1=h1, b64=thumb(jpg),
                          jpg=kb(jpg), png=kb(f"{COVERS}/{anchor}.png"),
                          svg=kb(f"{COVERS}/{anchor}.svg")))
        n += 1
    if items:
        cards.append((gtitle, items))

def card_html(it):
    e = lambda t: html.escape(t, quote=True)
    return f'''<article class="card" data-q="{e((it['h1'] + ' ' + it['slug']).lower())}">
  <button class="shot" type="button" data-title="{e(it['h1'])}"
          data-slug="{e(it['slug'])}" aria-label="Xem lớn ảnh bìa {e(it['h1'])}">
    <img src="data:image/jpeg;base64,{it['b64']}" alt="Ảnh bìa bài {e(it['h1'])}"
         width="1200" height="630" decoding="async">
  </button>
  <div class="meta">
    <h3>{e(it['h1'])}</h3>
    <p class="slug">{e(it['slug'])}</p>
    <p class="files"><span>{it['anchor']}</span>
      <b>JPG</b> {it['jpg']} · <b>PNG</b> {it['png']} · <b>SVG</b> {it['svg']}</p>
  </div>
</article>'''

sections = "\n".join(
    f'<section class="group" data-group="{html.escape(g, quote=True)}">'
    f'<h2><span class="eyebrow">{html.escape(g)}</span><span class="count">{len(its)} ảnh</span></h2>'
    f'<div class="grid">{"".join(card_html(i) for i in its)}</div></section>'
    for g, its in cards)

page = f'''<title>Thư Viện Ảnh Bìa HOANTRANTDH</title>
<style>
:root{{
  --bg:#eef1f5; --surface:#ffffff; --surface-2:#f4f6f9;
  --ink:#18202c; --muted:#5c6a7a; --faint:#8b97a6;
  --accent:#1657b8; --accent-ink:#0f3f88; --accent-soft:#e4edfb;
  --border:#dbe1e9; --border-strong:#c3ccd8;
  --shadow:0 1px 2px rgba(24,32,44,.05),0 6px 20px rgba(24,32,44,.06);
  --scrim:rgba(13,18,25,.72);
  --mono:ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;
  --sans:-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --bg:#0d1219; --surface:#151d28; --surface-2:#111823;
    --ink:#e7ecf3; --muted:#9aa7b7; --faint:#6b7887;
    --accent:#5b9bf0; --accent-ink:#8fbcf6; --accent-soft:#182740;
    --border:#26303d; --border-strong:#333f4e;
    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 26px rgba(0,0,0,.35);
    --scrim:rgba(4,7,11,.82);
  }}
}}
:root[data-theme="dark"]{{
  --bg:#0d1219; --surface:#151d28; --surface-2:#111823;
  --ink:#e7ecf3; --muted:#9aa7b7; --faint:#6b7887;
  --accent:#5b9bf0; --accent-ink:#8fbcf6; --accent-soft:#182740;
  --border:#26303d; --border-strong:#333f4e;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 26px rgba(0,0,0,.35);
  --scrim:rgba(4,7,11,.82);
}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55;
  -webkit-font-smoothing:antialiased}}
.wrap{{max-width:1500px;margin:0 auto;padding:0 24px 72px}}

header.top{{position:sticky;top:0;z-index:20;background:var(--bg);
  border-bottom:1px solid var(--border);padding:18px 0 14px;margin-bottom:28px}}
.topin{{max-width:1500px;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;
  align-items:baseline;gap:10px 22px}}
h1{{font-size:21px;font-weight:700;letter-spacing:-.2px;margin:0;text-wrap:balance}}
.sub{{color:var(--muted);font-size:13.5px;margin:0}}
.sub b{{color:var(--ink);font-variant-numeric:tabular-nums}}
.search{{margin-left:auto;display:flex;align-items:center;gap:8px}}
.search input{{font:14px var(--sans);color:var(--ink);background:var(--surface);
  border:1px solid var(--border-strong);border-radius:8px;padding:8px 12px;width:260px}}
.search input:focus-visible{{outline:2px solid var(--accent);outline-offset:1px}}
#hits{{color:var(--muted);font-size:13px;font-variant-numeric:tabular-nums;min-width:74px}}

section.group{{margin:0 0 40px}}
section.group h2{{display:flex;align-items:baseline;gap:12px;margin:0 0 14px;
  padding-bottom:8px;border-bottom:1px solid var(--border)}}
.eyebrow{{font:600 12px/1.2 var(--mono);letter-spacing:.09em;text-transform:uppercase;
  color:var(--accent-ink)}}
.count{{font:12px var(--mono);color:var(--faint);font-variant-numeric:tabular-nums}}

.grid{{display:grid;gap:20px;grid-template-columns:repeat(auto-fill,minmax(288px,1fr))}}
.card{{display:flex;flex-direction:column;background:var(--surface);
  border:1px solid var(--border);border-radius:10px;overflow:hidden;box-shadow:var(--shadow)}}
.shot{{display:block;padding:0;border:0;background:var(--surface-2);cursor:zoom-in;
  border-bottom:1px solid var(--border);line-height:0}}
.shot img{{display:block;width:100%;height:auto;aspect-ratio:1200/630;object-fit:cover}}
.shot:focus-visible{{outline:2px solid var(--accent);outline-offset:-2px}}
.meta{{padding:12px 14px 14px;display:flex;flex-direction:column;gap:5px}}
.meta h3{{margin:0;font-size:14.5px;font-weight:650;line-height:1.35;text-wrap:balance}}
.slug{{margin:0;font:12.5px var(--mono);color:var(--accent-ink);word-break:break-all}}
.files{{margin:0;font:11.5px var(--mono);color:var(--faint)}}
.files span{{display:block;color:var(--muted);word-break:break-all;margin-bottom:2px}}
.files b{{font-weight:600;color:var(--muted)}}

dialog#lb{{border:0;padding:0;background:transparent;max-width:min(1200px,94vw);width:100%}}
dialog#lb::backdrop{{background:var(--scrim)}}
.lbbox{{background:var(--surface);border:1px solid var(--border-strong);border-radius:12px;
  overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.35)}}
.lbbox img{{display:block;width:100%;height:auto}}
.lbbar{{display:flex;align-items:baseline;gap:12px;padding:12px 16px;border-top:1px solid var(--border)}}
.lbbar h4{{margin:0;font-size:14px;font-weight:650}}
.lbbar code{{font:12px var(--mono);color:var(--accent-ink)}}
.lbbar button{{margin-left:auto;font:13px var(--sans);color:var(--ink);background:var(--surface-2);
  border:1px solid var(--border-strong);border-radius:7px;padding:6px 14px;cursor:pointer}}
.lbbar button:hover{{background:var(--accent-soft);border-color:var(--accent)}}

.empty{{display:none;color:var(--muted);font-size:14px;padding:28px 0}}
.empty.on{{display:block}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
@media (max-width:620px){{.search{{margin-left:0;width:100%}}.search input{{width:100%}}}}
</style>

<header class="top">
  <div class="topin">
    <h1>Thư viện ảnh bìa</h1>
    <p class="sub"><b>{n}</b> ảnh · 1200×630 · JPG + PNG + SVG · hoantrantdh.com</p>
    <div class="search">
      <label for="q" class="sub">Lọc</label>
      <input id="q" type="search" placeholder="tên bài hoặc slug…" autocomplete="off">
      <span id="hits">{n}/{n}</span>
    </div>
  </div>
</header>

<div class="wrap">
{sections}
<p class="empty" id="empty">Không có ảnh bìa nào khớp từ khoá.</p>
</div>

<dialog id="lb">
  <div class="lbbox">
    <img id="lbimg" alt="">
    <div class="lbbar"><h4 id="lbt"></h4><code id="lbs"></code>
      <button type="button" id="lbx">Đóng</button></div>
  </div>
</dialog>

<script>
const cards=[...document.querySelectorAll('.card')],hits=document.getElementById('hits'),
      groups=[...document.querySelectorAll('section.group')],empty=document.getElementById('empty');
document.getElementById('q').addEventListener('input',e=>{{
  const q=e.target.value.trim().toLowerCase();let n=0;
  cards.forEach(c=>{{const on=!q||c.dataset.q.includes(q);c.hidden=!on;if(on)n++;}});
  groups.forEach(g=>{{g.hidden=![...g.querySelectorAll('.card')].some(c=>!c.hidden);}});
  hits.textContent=n+'/'+cards.length;empty.classList.toggle('on',n===0);
}});
const lb=document.getElementById('lb'),lbi=document.getElementById('lbimg'),
      lbt=document.getElementById('lbt'),lbs=document.getElementById('lbs');
document.querySelectorAll('.shot').forEach(b=>b.addEventListener('click',()=>{{
  lbi.src=b.querySelector('img').src;
  lbi.alt='Ảnh bìa bài '+b.dataset.title;
  lbt.textContent=b.dataset.title;lbs.textContent=b.dataset.slug;lb.showModal();
}}));
document.getElementById('lbx').addEventListener('click',()=>lb.close());
lb.addEventListener('click',e=>{{if(e.target===lb)lb.close();}});
</script>
'''

out = os.environ.get("GALLERY_OUT", f"{ROOT}/cover-gallery.html")
open(out, "w", encoding="utf-8").write(page)
print(f"gallery: {n} ảnh bìa -> {out} ({len(page)//1024//1024} MB)"
      + (f" · THIẾU jpg: {missing}" if missing else ""))
