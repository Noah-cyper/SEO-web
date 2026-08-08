# SEO Playbook — hoantrantdh.com (Global / EN market)

Bộ workflow SEO thực chiến cho **hoantrantdh.com**, được tùy biến cho thị trường **toàn cầu (tiếng Anh)** — mảng **Global Sourcing Center** (cung ứng linh kiện & thiết bị đo lường / tự động hóa công nghiệp).

Toàn bộ tài liệu viết bằng **tiếng Việt**, nhưng mọi tài sản dùng để SEO (keyword, prompt, template trang, mẫu bài) đều được viết sẵn bằng **tiếng Anh** để bạn copy–paste dùng ngay. Bạn không cần giỏi tiếng Anh: các prompt luôn yêu cầu AI viết bằng English bản ngữ, chuẩn B2B kỹ thuật, và **đánh dấu chỗ cần người bản ngữ review**.

---

## 1. Website đang là gì? (tóm tắt phân tích)

| | |
|---|---|
| **Doanh nghiệp** | Hoan Tran Automation Technology — thiết bị đo lường & tự động hóa công nghiệp |
| **Thị trường lõi (VI)** | Việt Nam + Đông Nam Á. Đồng hồ áp suất, cảm biến/transmitter, PLC Mitsubishi, đo mức/nhiệt/áp cho nhiệt điện, xi măng, hóa chất, dầu khí |
| **Thị trường global (EN)** | `/en/` — **Global Sourcing Center**: mua hàng đa quốc gia, **linh kiện obsolete/EOL**, cấp hàng khẩn cấp **line-down (AOG)**, chống hàng giả (counterfeit screening), truy xuất nguồn gốc, AVL, VMI, giảm chi phí BOM |
| **Đối tượng (ICP)** | Procurement/purchasing manager, maintenance & reliability engineer, MRO buyer, plant/instrumentation engineer ở nhà máy & EPC |
| **Loại trang chính** | Product/part-number page, brand hub, **obsolete→replacement**, cross-reference, comparison, glossary, solution/service, industry page, location page |

Chi tiết đầy đủ: [`docs/00-phan-tich-website.md`](docs/00-phan-tich-website.md)

> **Tại sao niche này hợp với 7 workflow?** Mỗi part number (vd `7MF0340-1DM01-5AF2`) là một truy vấn long-tail. Mảng "obsolete → replacement" và "cross-reference / equivalent" có **intent thương mại rất cao** và đối thủ phương Tây (EU Automation, Radwell…) đã chứng minh mô hình. Dữ liệu (GSC, sitemap đối thủ, SERP part-number) dồi dào → giảm tối đa việc "đoán".

---

## 2. Bảy workflow (đã tùy biến cho hoantrantdh)

| # | Workflow | Dùng để | File |
|---|----------|---------|------|
| 1 | GSC → cơ hội SEO từ dữ liệu sẵn có | Tìm trang gần Top 10, part-number impression cao CTR thấp | [`docs/01-gsc-co-hoi.md`](docs/01-gsc-co-hoi.md) |
| 2 | Sitemap đối thủ → bản đồ SEO | Đọc cấu trúc EU Automation / Radwell, tìm cluster đang thiếu | [`docs/02-sitemap-doi-thu.md`](docs/02-sitemap-doi-thu.md) |
| 3 | 1 bài → hệ thống phân phối | Biến 1 trang thành 15–20 điểm chạm | [`docs/03-tai-su-dung-content.md`](docs/03-tai-su-dung-content.md) |
| 4 | Reddit/forum → ngôn ngữ khách hàng thật | r/PLC, Eng-Tips, PLCTalk — hiểu "vì sao họ tìm" | [`docs/04-reddit-voice-of-customer.md`](docs/04-reddit-voice-of-customer.md) |
| 5 | Audit content cũ trước khi viết mới | Tìm URL tụt hạng / lỗi thời để refresh | [`docs/05-audit-content-cu.md`](docs/05-audit-content-cu.md) |
| 6 | Không chỉ publish trên website | LinkedIn / YouTube / cộng đồng kỹ thuật | [`docs/06-phan-phoi-da-kenh.md`](docs/06-phan-phoi-da-kenh.md) |
| 7 | Google keyword TRƯỚC khi nhờ AI viết | Đọc SERP để không viết sai loại trang | [`docs/07-serp-intent-truoc.md`](docs/07-serp-intent-truoc.md) |

**Tài sản dùng chung:**
- [`docs/prompts/prompt-library.md`](docs/prompts/prompt-library.md) — Toàn bộ prompt EN, copy-paste ngay
- [`docs/templates/page-templates.md`](docs/templates/page-templates.md) — Khung trang Product / Alternatives / Comparison / Glossary…
- [`docs/templates/keyword-topic-map.md`](docs/templates/keyword-topic-map.md) — Topic cluster + keyword EN mẫu cho niche
- [`docs/templates/editorial-checklist.md`](docs/templates/editorial-checklist.md) — Checklist trước khi publish (E-E-A-T, schema, internal link)
- [`scripts/gsc_opportunities.py`](scripts/gsc_opportunities.py) — Script phân loại cơ hội từ file GSC export (chỉ cần Python, không cần cài gì)

---

## 3. Bắt đầu từ đâu? (thứ tự đề xuất)

1. **Tuần 1 — Nhìn lại dữ liệu của chính mình.** Chạy Workflow 1 (GSC) + Workflow 5 (audit content cũ). Đây là nơi ra kết quả nhanh nhất vì website đã có tín hiệu sẵn.
2. **Tuần 2 — Nhìn ra ngoài.** Workflow 2 (sitemap đối thủ) + Workflow 4 (Reddit) để dựng bản đồ topic cluster và lấy "ngôn ngữ khách hàng".
3. **Tuần 3 trở đi — Sản xuất đúng loại.** Mỗi bài mới: bắt buộc qua Workflow 7 (đọc SERP) trước, rồi mới viết theo template. Mỗi bài xong: chạy Workflow 3 + 6 để phân phối.

Nguyên tắc xuyên suốt (giống case study gốc): **AI để xử lý tín hiệu nhanh hơn, không để AI quyết định Search Intent thay bạn.**

---

## 4. Ghi chú vận hành

- **Claude vs Codex/ChatGPT luân phiên:** dùng Claude cho phân tích dài (sitemap, GSC, đọc SERP tổng hợp) và viết bản EN có chiều sâu; dùng ChatGPT/Codex cho lặp nhanh, biến thể ngắn (social, meta). Prompt trong repo dùng được cho cả hai.
- **Ngôn ngữ:** website có cả VI (root) và EN (`/en/`). Playbook này tập trung mảng **EN/global**; nguyên tắc áp dụng ngược lại cho VI.
- File này + toàn bộ `docs/` là tài liệu sống — cập nhật khi bạn học được điều mới từ dữ liệu.
