# Keyword & Content Plan — hoantrantdh.com/en (Global Sourcing)

Đây là **backlog trang cụ thể để sản xuất**, không phải hướng dẫn. Mỗi dòng = một trang thật, đã có target keyword + URL + loại + ưu tiên. Xếp theo ROI (obsolete→replacement và cross-reference lên trước vì intent thương mại cao và đối thủ đã chứng minh nhu cầu).

Ký hiệu ưu tiên: **P0** = làm ngay (đã có bằng chứng nhu cầu) · **P1** = đợt 2 · **P2** = mở rộng.

---

## Cluster A — Obsolete → Replacement (money pages, P0)

Bằng chứng nhu cầu: Emerson/Radwell/EU Automation/Galco đều có trang cho các part này; người dùng chủ động tìm "replacement / obsolete / discontinued".

| Trang | Target keyword | URL slug | Ưu tiên | Trạng thái |
|---|---|---|---|---|
| Rosemount 1151 replacement | rosemount 1151 replacement / obsolete | `/en/obsolete/rosemount-1151-replacement/` | P0 | ✅ **Đã viết** (`content/en/obsolete-rosemount-1151-replacement.md`) |
| Mitsubishi FX3U replacement (FX5U) | mitsubishi fx3u replacement / end of life | `/en/obsolete/mitsubishi-fx3u-replacement-fx5u/` | P0 | ✅ **Đã viết** (`content/en/mitsubishi-fx3u-fx5u-replacement.md`) |
| Rosemount 3051 obsolete models replacement | rosemount 3051 obsolete replacement | `/en/obsolete/rosemount-3051-replacement/` | P0 | ⬜ Chờ viết |
| Siemens SITRANS P (legacy) replacement | siemens sitrans p obsolete replacement | `/en/obsolete/siemens-sitrans-p-replacement/` | P1 | ⬜ |
| Allen-Bradley PLC-5 / SLC 500 replacement | plc-5 replacement / slc 500 obsolete | `/en/obsolete/allen-bradley-plc5-slc500-replacement/` | P1 | ⬜ |
| Mitsubishi FX3G / FX3UC replacement | fx3g replacement / fx3uc end of life | `/en/obsolete/mitsubishi-fx3g-fx3uc-replacement/` | P1 | ⬜ |
| Yokogawa EJA obsolete replacement | yokogawa eja replacement | `/en/obsolete/yokogawa-eja-replacement/` | P2 | ⬜ |
| Endress+Hauser Cerabar (legacy) replacement | e+h cerabar obsolete replacement | `/en/obsolete/endress-hauser-cerabar-replacement/` | P2 | ⬜ |

**Hub cha:** `/en/obsolete/` — trang pillar "Obsolete Industrial Automation Parts — Replacement & Sourcing" gom toàn bộ cluster (P0, làm sau khi có 3–4 trang con).

---

## Cluster B — Cross-reference / Equivalent (P0–P1)

Bằng chứng: Galco "How to Cross-Reference Obsolete Automation Parts", US Control Tech cross-reference cho AB/Siemens/Schneider/ABB/Eaton/Mitsubishi.

| Trang | Target keyword | URL slug | Ưu tiên |
|---|---|---|---|
| How to cross-reference obsolete automation parts | cross reference obsolete parts | `/en/guides/cross-reference-obsolete-parts/` | P0 |
| Rosemount 1151 → 3051 cross-reference chart | rosemount 1151 3051 cross reference | `/en/cross-reference/rosemount-1151-to-3051/` | P0 |
| Mitsubishi FX3U → FX5U cross-reference | fx3u fx5u cross reference | `/en/cross-reference/mitsubishi-fx3u-to-fx5u/` | P1 |
| Pressure transmitter cross-reference (multi-brand) | pressure transmitter cross reference | `/en/cross-reference/pressure-transmitters/` | P1 |

---

## Cluster C — Product / Part-number pages (P0, long-tail lớn)

Mỗi part number = 1 trang (giống `/en/products/siemens-sitrans-p320/` đã có). Ưu tiên các part hay tìm + hoantrantdh cấp được.

| Nhóm part | URL pattern | Ưu tiên |
|---|---|---|
| Siemens SITRANS (P320/P500/…) | `/en/products/siemens-sitrans-<model>/` | P0 |
| Rosemount 3051 variants | `/en/products/rosemount-3051-<variant>/` | P0 |
| Mitsubishi FX5U CPUs | `/en/products/mitsubishi-fx5u-<model>/` | P1 |
| WIKA pressure gauges | `/en/products/wika-<model>/` | P1 |
| Endress+Hauser transmitters | `/en/products/endress-hauser-<model>/` | P2 |

> Template dùng chung: `content/en/_TEMPLATE_product-page.md` (chờ tạo). Mỗi trang cần: part number chính + phụ, spec bảng, cert (SIL/ATEX), datasheet link, "obsolete? xem replacement", CTA hỏi giá/lead time, schema Product.

---

## Cluster D — Solution / Service pages (định vị + convert, P0)

Nâng cấp/viết mới cho chính các dịch vụ ở `/en/sourcing/`:

| Trang | Target keyword | URL slug | Ưu tiên |
|---|---|---|---|
| Obsolete & hard-to-find parts sourcing | obsolete parts sourcing / hard to find automation parts | `/en/services/obsolete-parts-sourcing/` | P0 |
| Emergency / line-down (AOG) supply | line down parts / emergency industrial parts | `/en/services/emergency-line-down-supply/` | P0 |
| Counterfeit screening & traceability | counterfeit electronic components prevention | `/en/services/counterfeit-screening/` | P1 |
| VMI & BOM cost reduction | vendor managed inventory industrial / bom cost reduction | `/en/services/vmi-bom-optimization/` | P1 |

---

## Cluster E — Comparison (P1)

| Trang | Target keyword | URL slug |
|---|---|---|
| FX3U vs FX5U | mitsubishi fx3u vs fx5u | (gộp vào trang obsolete FX3U đã viết, đủ mạnh) |
| Rosemount 3051 vs Siemens SITRANS P320 | rosemount 3051 vs sitrans p320 | `/en/compare/rosemount-3051-vs-siemens-sitrans-p320/` |
| Rosemount 3051 vs Yokogawa EJA | rosemount 3051 vs yokogawa eja | `/en/compare/rosemount-3051-vs-yokogawa-eja/` |

---

## Cluster F — Glossary / Technical (top-funnel, xây E-E-A-T, P2)

Ngắn, mỗi trang 1 khái niệm, internal-link về product/obsolete.

`4-20mA vs HART` · `SIL2 / SIL3 rating explained` · `ATEX / Ex zones` · `IP rating for instruments` · `pressure transmitter vs pressure gauge` · `RTD vs thermocouple` · `what is a last-time-buy (LTB)` · `what is AOG in industrial supply`.

URL: `/en/glossary/<term>/`

---

## Cluster G — Industry & Location (P2)

- `/en/industries/thermal-power-mro-sourcing/`
- `/en/industries/cement-plant-spare-parts/`
- `/en/industries/oil-gas-instrumentation-sourcing/`
- `/en/locations/industrial-parts-supplier-southeast-asia/`
- `/en/locations/automation-parts-supplier-vietnam/`

---

## Bộ modifier để nhân keyword (ghép với mọi brand/part/loại)

`obsolete` · `replacement for` · `alternative to` · `cross reference` · `equivalent` · `datasheet` · `price` · `buy` · `supplier` · `distributor` · `in stock` · `lead time` · `part number` · `end of life` · `last time buy` · `discontinued` · `AOG` · `line down` · `counterfeit` · `reconditioned`

**Công thức:** `[brand / device type / part number] + [modifier]` → mỗi tổ hợp là 1 target keyword tiềm năng.

---

## Đợt sản xuất đề xuất (thứ tự làm)

1. **Đợt 1 (đã bắt đầu):** 2 trang obsolete P0 ✅ + 2 trang service P0 (obsolete sourcing, emergency supply) + cross-reference guide P0.
2. **Đợt 2:** 3051 obsolete + cross-reference charts + 3–5 product page Siemens/Rosemount.
3. **Đợt 3:** comparison + glossary + industry/location.

> Mỗi trang trước khi publish: chạy qua `docs/templates/editorial-checklist.md` (schema, internal link, kiểm spec kỹ thuật với datasheet OEM).
