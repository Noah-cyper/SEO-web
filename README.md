# Nội dung SEO cho hoantrantdh.com

Kho nội dung SEO **tiếng Việt, sẵn đăng** cho **hoantrantdh.com** — nhà cung cấp thiết bị đo lường & tự động hóa công nghiệp (đồng hồ áp suất, cảm biến/transmitter, PLC Mitsubishi, đo mức/nhiệt/áp, đồng hồ lò hơi…), thị trường Việt Nam.

> Trọng tâm: **sản phẩm giao được ngay** (trang web viết sẵn), không phải hướng dẫn quy trình.

## Trang đã viết xong (thư mục `content/vi/`)

| Trang | Từ khóa nhắm tới | Loại | File |
|---|---|---|---|
| Cảm biến áp suất là gì? Cách chọn | cảm biến áp suất / là gì / cách chọn / báo giá | Bài trụ (thông tin + thương mại) | `content/vi/cam-bien-ap-suat-la-gi-cach-chon.md` |
| Đồng hồ đo áp suất WIKA chính hãng | đồng hồ đo áp suất wika / chính hãng / giá | Trang sản phẩm (thương mại) | `content/vi/dong-ho-do-ap-suat-wika.md` |
| PLC Mitsubishi FX3U là gì? | plc mitsubishi fx3u / ứng dụng / vs fx5u | Blog kỹ thuật + thương mại | `content/vi/plc-mitsubishi-fx3u-la-gi.md` |

Mỗi trang có sẵn: **title tag, meta description, URL slug, H1, nội dung, bảng phân loại/so sánh, FAQ, CTA báo giá, ghi chú schema + internal link**. Viết theo đúng khung đang rank top ở thị trường VN: *là gì → phân loại → nguyên lý → cách chọn → ứng dụng → báo giá / CO-CQ chính hãng*.

Các trang **link chéo vào nhau** (bài trụ ↔ trang sản phẩm ↔ blog), CTA đưa về `/lien-he/`.

## Cụm thương hiệu Seneca (thư mục `content/vi/seneca/`)

Đang phủ **toàn bộ sản phẩm Seneca** (Italy) theo cấu trúc hub → danh mục → model:

| Trang | Loại | File |
|---|---|---|
| Seneca Việt Nam (trang hãng) | Hub thương hiệu | `content/vi/seneca/seneca-viet-nam.md` |
| Bộ chuyển đổi tín hiệu Seneca | Danh mục (pillar) | `content/vi/seneca/bo-chuyen-doi-tin-hieu-seneca.md` |
| K109S | Sản phẩm | `content/vi/seneca/k109s-seneca.md` |
| K109PT (Pt100) | Sản phẩm | `content/vi/seneca/k109pt-seneca.md` |
| Z109REG2-1 | Sản phẩm | `content/vi/seneca/z109reg2-1-seneca.md` |
| _Template sản phẩm Seneca_ | Khung nhân bản | `content/vi/seneca/_TEMPLATE-san-pham-seneca.md` |

Kế hoạch phủ hết dòng/model Seneca (chuyển đổi tín hiệu, remote I/O Z-PC, datalogger/RTU, gateway Modbus, đồng hồ đo điện năng): `research/seneca-content-plan.md`.

## Đợt bổ sung: 18 trang khép backlog (`content/vi/`)

Toàn bộ backlog P0/P1/P2 trong `research/keyword-and-content-plan.md` **đã sản xuất xong**:

| Cụm | Trang |
|---|---|
| Bài trụ | cảm biến đo mức · biến tần · đồng hồ đo áp suất |
| Trang sản phẩm | cảm biến áp suất WIKA · PLC Mitsubishi FX5U · đồng hồ dạng màng · đồng hồ có dầu · đồng hồ lò hơi · HMI Weintek |
| Blog how-to | lỗi cảm biến áp suất · cách chọn thang đo · tín hiệu 4-20mA · truyền thông FX5U–FX3U |
| So sánh | đồng hồ hay cảm biến áp suất · cảm biến áp suất hãng nào tốt |
| Trang ngành | đo lường lò hơi · tự động hóa nhà máy xi măng · đo lường hóa chất – dầu khí |

## Kiểm tra chất lượng bài trước khi đăng

```bash
python3 scripts/check_seo.py            # chấm toàn bộ content/vi
python3 scripts/check_seo.py rhize      # chấm riêng một cụm
```

Script chấm theo checklist Rank Math của skill `seo-article-hoantrantdh`: 1 H1, 7–9 H2
(≥2 H2 chứa từ khoá chính), ≥5 bảng, FAQ 4–6 câu, meta 140–160 ký tự, mật độ từ khoá
1.5–2.5%, từ khoá trong slug – 10% đầu bài – alt ảnh, 2–4 internal link, CTA `/lien-he/`.

> ⚠️ 109 bài của các đợt đầu **chưa đạt** checklist này (viết trước khi có script).
> Chạy `check_seo.py` để xem danh sách cần rà soát.

## Cụm Rhize — Manufacturing Data Hub (thư mục `content/vi/rhize/`)

**30 bài** về nền tảng dữ liệu sản xuất **Rhize** (Manufacturing Data Hub chuẩn ISA-95),
theo cấu trúc hub → pillar → satellite:

| Nhóm | Số bài | Nội dung |
|---|---|---|
| Nền tảng & kiến trúc | 6 | Brand hub `/rhize/`, MDH là gì, kiến trúc, ISA-95, GraphQL API, so sánh MES/historian/data lake |
| Thành phần hệ thống | 9 | Rhize DB, Core, BPMN engine, Agent, NATS, Keycloak, Grafana/Tempo, Admin UI, triển khai Kubernetes |
| Tích hợp & chuẩn dữ liệu | 5 | OPC UA, MQTT/UNS, ERP, SCADA & historian, B2MML |
| Ứng dụng & ngành | 10 | OEE, batch record điện tử, track & trace, chất lượng, scheduling, kho, AI/ML, dược, thực phẩm, sản xuất rời rạc |

Bản đồ cụm, nguồn thông tin và checklist đối chiếu trước khi đăng: `research/rhize-content-plan.md`.

## Kế hoạch content (thư mục `research/`)

`research/keyword-and-content-plan.md` — backlog ~30 trang tiếng Việt cụ thể còn lại, xếp theo ROI, mỗi trang có từ khóa + URL + độ ưu tiên (đã đánh dấu trang nào xong). Gồm: bài trụ "là gì/cách chọn", trang sản phẩm theo hãng, blog kỹ thuật how-to, so sánh, trang ngành.

## Trước khi đăng — bắt buộc

⚠️ **Kiểm tra lại thông số kỹ thuật** (thang đo, tín hiệu ngõ ra, cấp bảo vệ, thông số dòng PLC…) theo **datasheet/catalog của hãng**. Nội dung được viết dựa trên kiến thức ngành + nguồn công khai; các chỗ cần xác nhận đã ghi chú trong file. Sai thông số thiết bị công nghiệp là rủi ro thật.

Sau đó: gắn schema (Product/FAQ/Breadcrumb), rà internal link, cập nhật giá/mã hàng thực tế còn bán.

## Còn lại

Backlog trong `research/` còn nhiều trang P0/P1. Cần viết tiếp nhóm nào (thêm bài trụ, trang sản phẩm theo hãng, hay blog how-to) chỉ cần yêu cầu là sản xuất tiếp.
