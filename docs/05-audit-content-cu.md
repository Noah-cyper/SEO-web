# Workflow 5 — Audit content cũ trước khi viết mới

> SEO không phải lúc nào cũng là publish thêm. Tăng trưởng nhanh nhất thường đến từ URL **đã có dữ liệu**: lịch sử, backlink, impression. Trước khi hỏi "tháng này viết thêm bao nhiêu bài?", hãy hỏi "bao nhiêu bài cũ đang bị lãng phí?".

## Khi nào dùng
Song song Workflow 1, đầu mỗi tháng/quý. Ưu tiên trước khi sản xuất trang mới.

## Bước 1 — Lập danh sách URL cần soi (từ GSC)
Xuất từ GSC (tab Pages, 90 ngày, hoặc so sánh 2 kỳ) và lọc trang có dấu hiệu:
- Impression **đang giảm** (so kỳ trước).
- Ranking **tụt** từ Top 5 → Top 10–20.
- **CTR thấp** bất thường so với position.
- Nội dung **đã cũ** (part/brand có bản mới, hoặc năm cũ trong title như "…-2024").

Với hoantrantdh, chú ý riêng cụm `/en/` và các trang product/obsolete — spec lỗi thời ở đây nguy hiểm hơn blog thường.

## Bước 2 — Cho AI chẩn đoán từng URL
Dùng prompt **P5 — Content Refresh Auditor** trong [`prompts/prompt-library.md`](prompts/prompt-library.md). Dán URL/nội dung + số liệu GSC + Top 3 kết quả hiện tại (từ Workflow 7). AI so sánh và chỉ ra **thiếu gì so với trang đang thắng**.

## Bước 3 — Danh sách hạng mục refresh (checklist)
Cập nhật khi cần:
- [ ] **Title** — thêm modifier intent (obsolete/replacement/datasheet), cập nhật năm.
- [ ] **Meta description** — viết lại để tăng CTR (đề cập lead time / in-stock / traceability).
- [ ] **Heading (H2/H3)** — bám các câu hỏi thật từ Workflow 4.
- [ ] **Nội dung chính** — bổ sung spec mới, phương án thay thế mới.
- [ ] **Ví dụ / bảng cross-reference** — cập nhật part number thay thế còn hàng.
- [ ] **FAQ** — thêm câu hỏi lặp lại từ cộng đồng + schema FAQ.
- [ ] **Internal link** — nối tới product/brand hub/obsolete liên quan.
- [ ] **Hình ảnh** — ảnh part đúng, alt text chứa part number.
- [ ] **Schema** — Product / FAQ / Breadcrumb (xem editorial-checklist).
- [ ] **CTA** — với trang có mục tiêu chuyển đổi: "request quote & lead time".

## Bước 4 — Đặc thù niche: kiểm tính chính xác kỹ thuật
Trước khi publish bản refresh, **người kiểm tra** phải xác nhận: part number, chứng nhận (SIL/ATEX), độ chính xác, phương án thay thế **vẫn đúng với datasheet OEM**. Ghi chú "verified against OEM datasheet, <ngày>". Sai số liệu = mất niềm tin + rủi ro an toàn.

## Bước 5 — Đo lại
Đánh dấu ngày refresh. Sau 4–8 tuần, đối chiếu GSC: position/CTR/impression trước–sau. Ghi vào log để biết loại refresh nào hiệu quả nhất.

## Quy tắc quyết định "refresh hay viết mới"
- Đã có URL, có backlink/impression, cùng intent → **refresh**.
- Intent đã đổi hẳn, hoặc là chủ đề mới hoàn toàn → **viết mới** (qua Workflow 7).
- URL trùng/ăn thịt nhau (cannibalization) → **gộp** & redirect 301 về bản mạnh nhất.

## Nối tiếp
Trang refresh xong → chạy **Workflow 3 + 6** để phân phối lại (báo cho khách biết đã cập nhật).
