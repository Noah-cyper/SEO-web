# Workflow 2 — Sitemap đối thủ → bản đồ SEO

> Sitemap không chỉ cho crawler. Đọc đúng cách, nó gần như là **bản thiết kế SEO** của một website. Thay vì mở vài trăm URL đọc tay, để AI nhìn ra cấu trúc tổng thể trước.

## Khi nào dùng
Khi bắt đầu phủ một mảng mới (vd "obsolete replacement"), hoặc mỗi quý để soi khoảng trống so với đối thủ.

## Bước 1 — Lấy sitemap đối thủ
Đối thủ EN của hoantrantdh (xem `00-phan-tich-website.md` mục F):
- `https://www.euautomation.com/sitemap.xml`
- `https://www.radwell.com/sitemap.xml`
- `https://www.industrialautomationco.com/sitemap.xml`
- `automa.net`, `classicautomation.com`, `santaclarasystems.com`…

Sitemap lớn thường là **sitemap index** (trỏ tới nhiều sitemap con). Lấy hết các URL con. Nếu bị chặn/nặng, dùng `curl`:

```bash
curl -s https://www.euautomation.com/sitemap.xml -o competitor_sitemap.xml
# nếu là index, lặp lại với từng <loc> con
```

## Bước 2 — Đưa toàn bộ URL cho AI phân tích cấu trúc
Dùng prompt **P2 — Competitor Sitemap Mapper** trong [`prompts/prompt-library.md`](prompts/prompt-library.md). Hỏi:

- Họ xây những **topic cluster** nào?
- Dùng những **loại landing page** nào?
- Cấu trúc URL / phân tầng thư mục ra sao? (vd `/parts/<brand>/<part-no>`)
- Chủ đề nào **đầu tư nhiều nhất** (đếm số URL theo nhánh)?
- Mình đang **thiếu** nhánh nào?
- Nhóm keyword nào có **giá trị thương mại cao**?

## Bước 3 — Đối chiếu với "menu loại trang" của niche
AI dễ nhận ra các dạng sau trong sitemap đối thủ ngành MRO/automation — đánh dấu dạng nào đối thủ có mà mình chưa:

- [ ] Part-number / product pages (theo brand)
- [ ] **Obsolete / EOL / discontinued** hub
- [ ] **Replacement / alternative** pages
- [ ] **Cross-reference / equivalent** charts
- [ ] Comparison pages
- [ ] Brand hub (Siemens, Rosemount, Mitsubishi…)
- [ ] Repair / refurbishment service
- [ ] Industry pages (cement, power, oil & gas…)
- [ ] Glossary / technical guides
- [ ] Location / region pages
- [ ] Case study / project

## Bước 4 — Trích cấu trúc URL & quy mô
Yêu cầu AI trả về **bảng nhánh**: prefix URL · loại trang · số lượng URL ước tính · ví dụ. Cột "số lượng" cho biết đối thủ **dồn lực vào đâu** → đó thường là nơi có tiền.

Ví dụ diễn giải:
> "euautomation dồn ~60% URL vào part-number pages theo brand, có hub `/obsolete/` riêng và nhiều trang `/repair/`." → gợi ý: hoantrantdh nên ưu tiên **product page theo part + hub Obsolete→Replacement**, còn "repair" có thể bỏ qua nếu không làm dịch vụ đó.

## Bước 5 — Chuyển thành backlog cluster
Với mỗi khoảng trống, tạo một dòng: cluster · trang pillar cần tạo · các trang con · keyword lõi EN · độ ưu tiên. Đưa các cluster ưu tiên cao vào [`templates/keyword-topic-map.md`](templates/keyword-topic-map.md).

## Lưu ý
- **Đừng copy nguyên si cấu trúc đối thủ.** Chọn nhánh khớp năng lực thật của hoantrantdh (bạn mạnh về sourcing/obsolete/counterfeit-screening, có thể không làm repair).
- Sitemap chỉ cho biết *họ xây gì*, không cho biết *cái gì đang rank*. Kết hợp Workflow 7 (đọc SERP) để xác nhận trước khi đầu tư lớn.

## Nối tiếp
Cluster đã chọn → **Workflow 4** (lấy ngôn ngữ khách hàng) → **Workflow 7** (đọc SERP) → viết theo template.
