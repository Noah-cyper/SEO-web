# 00 — Phân tích website hoantrantdh.com

> Cơ sở để tùy biến toàn bộ 7 workflow. Đọc file này một lần để hiểu "ta đang SEO cho ai, bán gì, ở SERP nào".

## A. Doanh nghiệp & hai thị trường

**Hoan Tran Automation Technology** (Công ty TNHH Kỹ Thuật Tự Động Hóa Hoàn Trần) — cung cấp thiết bị đo lường & tự động hóa công nghiệp; nguồn hàng EU/G7 + China; 5+ năm, ~400 dự án, khách ở Việt Nam & Đông Nam Á.

Website có **2 lớp**:

1. **VI (root domain)** — blog kỹ thuật + trang sản phẩm/danh mục tiếng Việt.
   Ví dụ: `/ung-dung-plc-mitsubishi-trong-may-cnc/`, `/hieu-chinh-zero-va-span-cam-bien/`, danh mục `đồng hồ đo áp suất`, `đồng hồ lò hơi`.
2. **EN (`/en/`)** — mảng **global**, định vị là **Global Sourcing Center**.
   Ví dụ: `/en/sourcing/`, `/en/products/siemens-sitrans-p320/` (part `7MF0340-1DM01-5AF2`, độ chính xác 0.065%, SIL2/3).

> Playbook này tập trung lớp **EN/global** — nơi bạn muốn mở rộng. Nhưng mọi nguyên tắc dùng lại được cho lớp VI.

## B. Định vị mảng global (rất quan trọng)

Không phải "bán thiết bị công nghiệp" chung chung, mà là **industrial MRO sourcing & obsolescence management** — giải một nỗi đau cụ thể của nhà máy:

- **Global procurement** — mua hàng đa quốc gia, một đầu mối chịu trách nhiệm.
- **Hard-to-find & obsolete / EOL / last-time-buy** — linh kiện ngừng sản xuất, tìm hàng còn tồn, đề xuất thay thế tương đương. *(đây là mỏ vàng SEO)*
- **Emergency / AOG / line-down** — cấp hàng khẩn khi dây chuyền dừng.
- **Counterfeit screening & traceability** — chống hàng giả, truy xuất nguồn gốc, kiểm tra nhiều lớp.
- **AVL (Approved Vendor List)** — nhà cung cấp được chấm điểm & giám sát.
- **VMI & BOM cost reduction** — quản lý tồn kho hộ khách, tối ưu chi phí BOM.

→ Insight SEO: khách không tìm "sản phẩm", họ tìm **giải pháp cho một tình huống**: "part này ngừng sản xuất rồi thay bằng gì", "cần gấp trong 48h", "làm sao chắc không phải hàng giả". Content phải bám các tình huống này.

## C. Chân dung khách hàng (ICP) & intent

| Persona | Họ tìm gì trên Google | Intent |
|---|---|---|
| **Procurement / purchasing manager** | "obsolete PLC replacement", "distributor <brand> Southeast Asia", "lead time", "price" | Thương mại / mua |
| **Maintenance & reliability engineer** | part number cụ thể, "datasheet", "cross reference", "equivalent" | Nghiên cứu → mua |
| **MRO buyer** | "in stock", "buy <part no>", "last time buy" | Giao dịch |
| **Plant / instrumentation engineer** | "how to calibrate", "HART vs 4-20mA", "SIL2 meaning", "wiring" | Học (top-funnel) |
| **Line-down / emergency** | "urgent <part>", "AOG supply", "line down parts" | Giao dịch khẩn |

## D. Loại trang & mức ưu tiên SEO

Xếp theo **ROI** cho niche này (cao → thấp):

1. **Obsolete → Replacement / Alternative** ★ cao nhất. VD "Rosemount 3051 obsolete replacement", "Mitsubishi FX3U end of life alternative". Intent thương mại cao, đối thủ chưa phủ hết.
2. **Cross-reference / Equivalent** — "<brand A part> equivalent", "<part> cross reference chart".
3. **Product / Part-number page** — mỗi part number 1 trang (như `/en/products/siemens-sitrans-p320/`). Long-tail khổng lồ.
4. **Comparison** — "Rosemount 3051 vs Siemens SITRANS P320".
5. **Solution / Service** — AOG supply, VMI, counterfeit screening, BOM optimization (định vị + convert).
6. **Brand hub** — "Siemens instrumentation sourcing", gom part cùng brand.
7. **Industry page** — "spare parts sourcing for cement plants / thermal power / oil & gas".
8. **Location page** — "industrial automation parts supplier Vietnam / Southeast Asia".
9. **Glossary / technical explainer** — SIL, HART, 4-20mA, ATEX/Ex, IP rating (top-funnel, xây thẩm quyền E-E-A-T).

## E. Bộ từ khóa lõi (brand + modifier)

**Brand/dòng hay gặp:** Siemens (SITRANS), Rosemount / Emerson, Yokogawa, Endress+Hauser (E+H), ABB, Honeywell, Mitsubishi (PLC FX/Q, inverter FR), Schneider, Allen-Bradley / Rockwell, WIKA, Ashcroft, Danfoss, Omron.

**Loại thiết bị:** pressure transmitter, pressure gauge, level transmitter, temperature transmitter / RTD / thermocouple, flow meter, PLC, HMI, VFD / inverter, proximity sensor, control valve, positioner.

**Modifier intent (ghép với brand/loại/part):** `obsolete`, `replacement for`, `alternative to`, `cross reference`, `equivalent`, `datasheet`, `price`, `buy`, `supplier`, `distributor`, `in stock`, `lead time`, `part number`, `end of life`, `last time buy`, `AOG`, `line down`, `counterfeit`.

→ Công thức keyword: **[brand/loại/part number] + [modifier]**. Xem thêm [`templates/keyword-topic-map.md`](templates/keyword-topic-map.md).

## F. Đối thủ tiếng Anh (để mining sitemap & SERP)

- **euautomation.com** — obsolete/automation parts, mô hình gần nhất, sitemap rất giàu.
- **radwell.com** — bán + sửa, danh mục part-number khổng lồ.
- **industrialautomationco.com**, **classicautomation.com**, **santaclarasystems.com**, **automa.net** (marketplace).
- Instrumentation-specific: distributor Siemens/Rosemount/E+H khu vực.

Dùng ở Workflow 2 (đọc sitemap) và Workflow 7 (đọc SERP theo từng part number).

## G. Cộng đồng để nghe "ngôn ngữ khách hàng" (Workflow 4)

r/PLC, r/IndustrialAutomation, r/ControlSystems, r/instrumentation, r/AskEngineers (Reddit); **Eng-Tips**, **PLCTalk.net**, **Control.com**, LinkedIn groups ngành automation/MRO.

## H. Rào cản đã biết & lưu ý

- **Song ngữ:** đảm bảo `hreflang` VI/EN đúng, `/en/` không bị coi là nội dung trùng.
- **E-E-A-T ngành kỹ thuật:** số liệu part phải chính xác (part number, cert, accuracy). Sai số liệu = mất niềm tin + rủi ro. Mọi trang product/alternative cần người kiểm tra thông số.
- **Tiếng Anh không phải bản ngữ:** mọi prompt trong repo ép AI viết English B2B chuẩn và gắn cờ `[NEEDS NATIVE REVIEW]` ở chỗ rủi ro.
- **YMYL nhẹ:** sai part cho thiết bị SIL/an toàn có thể nguy hiểm → luôn ghi rõ "verify against OEM datasheet".
