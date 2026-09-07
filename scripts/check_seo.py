#!/usr/bin/env python3
"""Chấm bài theo checklist Rank Math của skill seo-article-hoantrantdh.

    python3 scripts/check_seo.py                # chấm toàn bộ content/vi
    python3 scripts/check_seo.py rhize          # chấm các bài có slug/đường dẫn chứa 'rhize'

Mật độ từ khoá tính theo đúng công thức Rank Math: số lần xuất hiện / tổng số từ.
Từ khoá chính = phần tử đầu trong dòng 'TỪ KHÓA' của header.
"""
import re, sys, glob, unicodedata

ROOT = "/home/user/SEO-web/content/vi"
def N(t): return unicodedata.normalize("NFC", t).lower()

def audit(path):
    raw = open(path, encoding="utf-8").read()
    cmt = re.search(r"<!--(.*?)-->", raw, re.S)
    if not cmt: return None
    slug = re.search(r"URL SLUG[^:\n]*:\s*(\S+)", cmt.group(1))
    kwline = re.search(r"TỪ KHÓA[^:\n]*:\s*(.*)", cmt.group(1))
    if not (slug and kwline): return None
    slug, kw = slug.group(1), N(kwline.group(1).split("|")[0].strip())
    meta = re.search(r"^META[^:\n]*:\s*(.*)$", raw, re.M)
    meta = meta.group(1).strip() if meta else ""
    h1 = re.findall(r"^H1\s*:\s*(.*)$", raw, re.M)
    body = raw[raw.index("---", raw.index("H1")):] if "H1" in raw else raw
    h2 = re.findall(r"^## (.*)$", body, re.M)
    tables = len(re.findall(r"^\|[^\n]*\|\n\|[ :\-|]+\|", body, re.M))
    faq = len(re.findall(r"^\*\*.*\?\*\*", body.split("Câu hỏi thường gặp")[-1], re.M))
    words = len(body.split())
    hits = len(re.findall(r'(?<![0-9a-zà-ỹ])' + re.escape(kw) + r'(?![0-9a-zà-ỹ])', N(body)))
    dens = hits / words * 100 if words else 0
    first10 = N(" ".join(body.split()[:max(60, words // 10)]))
    alt = re.search(r"!\[([^\]]*)\]", body)
    links = len(re.findall(r"\]\(/[a-z0-9-]+/\)", body))
    ext = len(re.findall(r"\]\(https?://", body))

    err = []
    if len(h1) != 1: err.append("H1")
    if not 7 <= len(h2) <= 9: err.append(f"H2={len(h2)}")
    if sum(1 for h in h2 if kw in N(h)) < 2: err.append("H2 thiếu từ khoá")
    if tables < 5: err.append(f"bảng={tables}")
    if not 4 <= faq <= 6: err.append(f"FAQ={faq}")
    if not 140 <= len(meta) <= 160: err.append(f"meta={len(meta)}")
    if not 1.5 <= dens <= 2.5: err.append(f"mật độ={dens:.2f}%")
    if kw not in N(meta): err.append("từ khoá ∉ meta")
    if kw not in first10: err.append("từ khoá ∉ 10% đầu")
    if alt and kw not in N(alt.group(1)): err.append("từ khoá ∉ alt")
    if not all(w in N(slug) for w in kw.replace("-", " ").split() if w.isascii()):
        err.append("từ khoá ∉ slug")
    if links < 2: err.append(f"internal link={links}")
    if ext > 1: err.append(f"external link={ext}")
    if "/lien-he/" not in body: err.append("thiếu CTA")
    return dict(f=path.split("/")[-1][:-3], kw=kw, w=words, h2=len(h2), t=tables,
                faq=faq, meta=len(meta), d=dens, err=err)

pat = sys.argv[1] if len(sys.argv) > 1 else ""
rows = [r for p in sorted(glob.glob(f"{ROOT}/**/*.md", recursive=True))
        if pat in p and not p.split("/")[-1].startswith("_")
        for r in [audit(p)] if r]
print(f"{'bài':38}{'từ':>6}{'H2':>4}{'bảng':>6}{'FAQ':>5}{'meta':>6}{'mật độ':>9}  lỗi")
for r in rows:
    print(f"{r['f']:38}{r['w']:6}{r['h2']:4}{r['t']:6}{r['faq']:5}{r['meta']:6}{r['d']:8.2f}%  "
          + ("; ".join(r["err"]) if r["err"] else "—"))
bad = [r for r in rows if r["err"]]
print(f"\n{len(rows)-len(bad)}/{len(rows)} bài đạt checklist" + ("" if not bad else f" — còn {len(bad)} bài cần sửa"))
sys.exit(1 if bad else 0)
