# Workflow 1 — GSC → cơ hội SEO từ dữ liệu đang có

> Ý tưởng content không đến từ "đoán người dùng tìm gì", mà đến từ dữ liệu Google **đã cho bạn**. Một lần export GSC tốt = vài chục cơ hội đã có tín hiệu sẵn.

## Khi nào dùng
Đầu mỗi tháng, hoặc khi cần danh sách việc làm ngay ("nên tối ưu trang nào tuần này"). Đây là workflow ra kết quả nhanh nhất.

## Bước 1 — Export dữ liệu GSC (90 ngày)
Google Search Console → **Performance** → chọn khoảng **Last 3 months** → bật cả 4 metric (Clicks, Impressions, CTR, Position).

Export 2 file (nút Export → CSV/Google Sheets):
1. **Queries** (tab Queries) — từ khóa.
2. **Pages** (tab Pages) — URL.

Mẹo cho niche này: lọc thêm 1 bản chỉ chứa trang `/en/` (dùng filter **Page → contains → /en/**) để tách riêng thị trường global.

## Bước 2 — (tùy chọn) chạy script phân loại nhanh
Script gom sẵn cơ hội thành nhóm, đỡ phải nhìn thô:

```bash
python3 scripts/gsc_opportunities.py path/to/Queries.csv
```

Script không cần cài gì (chỉ Python 3). Nó xuất các nhóm: *Striking distance (pos 8–20)*, *High-impression low-CTR*, *Near top 10*, *Part-number queries chưa có trang riêng*. Xem [`scripts/gsc_opportunities.py`](../scripts/gsc_opportunities.py).

## Bước 3 — Đưa cho Claude/ChatGPT phân tích
Dùng prompt **P1 — GSC Opportunity Finder** trong [`prompts/prompt-library.md`](prompts/prompt-library.md). Nó yêu cầu AI tìm:

- Trang đang **gần Top 10** (position 8–15) → đẩy nhanh.
- Query **impression cao nhưng CTR thấp** → sửa title/meta là tăng click ngay.
- Query xuất hiện nhiều nhưng **chưa có trang riêng** → tạo trang mới.
- Trang có dấu hiệu **nên cập nhật** (impression giảm).
- Query **position 8–20** có khả năng đẩy lên nhanh (striking distance).
- Nội dung **mở rộng thành cluster** mới.

## Bước 4 — Đọc kết quả qua lăng kính niche (điểm khác biệt)
Với hoantrantdh, yêu cầu AI phân loại thêm theo **loại query đặc thù**:

| Nhóm phát hiện | Hành động cho niche sourcing |
|---|---|
| **Part-number query** (vd "7MF0340-1DM01-5AF2") impression cao, chưa có trang | Tạo **product/part-number page** theo template |
| Query chứa `obsolete / replacement / alternative / end of life` | Tạo trang **Obsolete→Replacement** (ROI cao nhất) |
| Query chứa `cross reference / equivalent` | Tạo trang **cross-reference chart** |
| Query chứa `datasheet / manual / wiring` | Bổ sung tài liệu/spec vào product page (top-funnel kéo về) |
| Query chứa `distributor / supplier / buy / price / lead time` | Tối ưu trang service/brand hub, thêm CTA hỏi giá |
| Trang `/en/` position 5→10+ (tụt) | Chuyển sang Workflow 5 (audit & refresh) |

## Bước 5 — Ưu tiên & giao việc
Chấm mỗi cơ hội theo **Impact × Ease**:
- *Impact* = impression × (khoảng cách tới top) × mức intent thương mại.
- *Ease* = đã có trang chưa? chỉ sửa meta hay phải viết mới?

Quick win thường là: **trang /en/ striking-distance có intent thương mại + chỉ cần refresh** → làm trước.

## Output kỳ vọng
Một bảng cơ hội (Sheet) với cột: query/URL, position, impression, CTR, loại-trang-cần, hành động (mới/refresh/meta), ưu tiên. Đây là backlog SEO của tháng.

## Nối tiếp
- Cơ hội "tạo trang mới" → sang **Workflow 7** (đọc SERP) trước khi viết.
- Cơ hội "refresh" → sang **Workflow 5**.
