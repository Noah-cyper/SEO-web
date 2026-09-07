# Cụm nội dung Rhize (Manufacturing Data Hub) — 30 bài

Cụm topic cluster cho **Rhize**, nền tảng Manufacturing Data Hub chuẩn ISA-95.
Cấu trúc: **1 brand hub → pillar khái niệm → satellite theo thành phần / tích hợp / ứng dụng / ngành**.

Màu nhận diện cụm trong ảnh bìa và sơ đồ: `#6E56CF`.

## Bản đồ cụm

### Nền tảng & kiến trúc (6 bài)

| Trang | Loại | Slug |
|---|---|---|
| Rhize – Manufacturing Data Hub chuẩn ISA-95 | **Brand hub (pillar)** | `/rhize/` |
| Manufacturing Data Hub là gì | **Pillar khái niệm** | `/manufacturing-data-hub-la-gi/` |
| Kiến trúc Rhize – các thành phần nền tảng | Pillar danh mục | `/kien-truc-nen-tang-rhize/` |
| Rhize ISA-95 – mô hình dữ liệu chuẩn | Satellite kỹ thuật | `/rhize-isa-95/` |
| Rhize GraphQL API | Satellite kỹ thuật | `/rhize-graphql-api/` |
| Rhize vs MES, historian, data lake | Satellite so sánh | `/rhize-vs-mes-historian-data-lake/` |

### Thành phần hệ thống (9 bài)

| Trang | Dịch vụ | Slug |
|---|---|---|
| Rhize DB – graph database | libreBaas | `/rhize-db-graph-database/` |
| Rhize Core – rules engine | libreCore | `/rhize-core/` |
| Rhize BPMN – workflow low-code | Workflow service | `/rhize-bpmn-workflow/` |
| Rhize Agent – kết nối thiết bị | libre-agent | `/rhize-agent-ket-noi/` |
| Rhize NATS – bus sự kiện | NATS | `/rhize-nats-event-streaming/` |
| Rhize Keycloak – xác thực & phân quyền | Keycloak | `/rhize-keycloak-phan-quyen/` |
| Rhize Grafana & Tempo – giám sát, tracing | Grafana LGTM | `/rhize-grafana-tempo/` |
| Rhize Admin UI – giao diện quản trị | libreAdminUI | `/rhize-admin-ui/` |
| Triển khai Rhize trên Kubernetes | Helm / hạ tầng | `/rhize-trien-khai-kubernetes/` |

### Tích hợp & chuẩn dữ liệu (5 bài)

| Trang | Slug |
|---|---|
| Rhize OPC UA – kết nối PLC | `/rhize-opc-ua/` |
| Rhize MQTT & UNS | `/rhize-mqtt-uns/` |
| Rhize tích hợp ERP | `/rhize-tich-hop-erp/` |
| Rhize tích hợp SCADA & historian | `/rhize-tich-hop-scada-historian/` |
| Rhize B2MML | `/rhize-b2mml/` |

### Ứng dụng & ngành (10 bài)

| Trang | Slug |
|---|---|
| Rhize OEE | `/rhize-oee/` |
| Batch record điện tử | `/rhize-batch-record-dien-tu/` |
| Track & trace – truy xuất nguồn gốc | `/rhize-truy-xuat-nguon-goc/` |
| Quản lý chất lượng | `/rhize-quan-ly-chat-luong/` |
| Scheduling – điều độ sản xuất | `/rhize-scheduling-lap-ke-hoach/` |
| Quản lý kho & vật tư tại xưởng | `/rhize-quan-ly-kho-vat-tu/` |
| AI/ML trên dữ liệu sản xuất | `/rhize-ai-ml-du-lieu-san-xuat/` |
| Ngành dược phẩm | `/rhize-nganh-duoc-pham/` |
| Ngành thực phẩm – đồ uống | `/rhize-nganh-thuc-pham-do-uong/` |
| Sản xuất rời rạc (serial) | `/rhize-san-xuat-roi-rac-serial/` |

## Liên kết nội bộ

- Brand hub `/rhize/` link xuống **toàn bộ 29 satellite**.
- Mỗi satellite link ngược về `/rhize/` và 2–4 satellite liên quan.
- Link chéo sang cụm sẵn có: `/ei3/`, `/bo-chuyen-doi-tin-hieu-seneca/`, `/gateway-modbus-seneca/`,
  `/scada-la-gi/`, `/plc-va-iot/`, `/cam-bien-ap-suat/`, `/cam-bien-nhiet-do/`, `/bao-mat-zero-trust-ei3/`.
- CTA: `/lien-he/` (script `gen_preview.py` tự đổi sang Zalo khi xuất bản WordPress).

## Nguồn thông tin đã dùng

Nội dung kỹ thuật dựa trên nguồn công khai của hãng, thu thập 09/2026:

- `rhize.com` — trang chủ và `rhize.com/platform/`: định nghĩa Manufacturing Data Hub,
  ISA-95, Rules Engine, BPMN, Apollo Router, GraphQL, các giao thức MQTT/OPC/OData,
  nhóm giải pháp (Life Sciences, F&B/CPG, Serialized Discrete), nhóm use case
  (batch records, track & trace, event-driven workflows, OEE, scheduling, warehouse).
- `rhize.com/blog/first-manufacturing-data-hub/` — khái niệm MDH.
- `docs.rhize.com` — tài liệu kỹ thuật: tên dịch vụ (**Libre Agent, libreBaas, Libre Core,
  Libre Admin UI, BPMN engine, libre router init**), phụ thuộc (**Restate, Tempo**),
  hạ tầng (**NATS, Keycloak, Grafana**), cài đặt qua **Helm** trên Kubernetes,
  thứ tự cài **libreBaas trước tiên**, mô hình ISA-95 lấy chủ yếu từ **Part 2**.
- **ISA-95 / IEC 62264** và **B2MML (MESA International)** — chuẩn công khai.

⚠️ **Trước khi đăng, bắt buộc đối chiếu lại:**

1. **Số hiệu phiên bản và phụ thuộc** (NATS, Keycloak, Grafana…) thay đổi theo bản phát hành
   Rhize đang triển khai — bài viết cố ý **không nêu số phiên bản cụ thể**, giữ nguyên như vậy
   trừ khi xác nhận được với bản đang dùng.
2. **Tên dịch vụ** có thể đổi giữa các phiên bản lớn — đối chiếu `docs.rhize.com`.
3. **Nội dung tuân thủ** (GMP, EU Annex 11, 21 CFR Part 11) trong bài
   `/rhize-nganh-duoc-pham/` và `/rhize-batch-record-dien-tu/` được viết ở dạng
   **năng lực nền tảng + trách nhiệm thẩm định thuộc về nhà máy** — **không** được sửa
   thành cam kết tuân thủ.
4. **Quan hệ phân phối/đối tác với Rhize** — trang hub hiện viết ở dạng năng lực tư vấn &
   triển khai. Chỉ đổi thành "phân phối chính hãng" khi thực tế có thoả thuận.

## Việc còn lại trước khi đăng

- [ ] Đối chiếu tên dịch vụ & kiến trúc với bản Rhize thực tế triển khai.
- [ ] Thay ảnh bìa mặc định bằng ảnh chụp màn hình dashboard/model thật (nếu có).
- [ ] Gắn schema: `Organization` cho hub, `TechArticle`/`Article` + `FAQPage` + `BreadcrumbList` cho satellite.
- [ ] Rà lại internal link sau khi các slug lên WordPress.

## Kết quả tự chấm theo checklist (đã kiểm bằng script)

Cả **30/30 bài** đạt toàn bộ checklist trong skill `seo-article-hoantrantdh`:

| Tiêu chí | Ngưỡng | Kết quả |
|---|---|---|
| H1 | đúng 1, chứa từ khoá chính | 30/30 |
| H2 | 7–9, ≥2 H2 chứa từ khoá chính | 30/30 |
| Bảng | ≥5, mỗi bảng ≥3 dòng dữ liệu | 30/30 (5–7 bảng) |
| FAQ | 4–6 câu | 30/30 (5–6 câu) |
| Meta description | 140–160 ký tự, có từ khoá chính | 30/30 |
| Mật độ từ khoá chính | 1.5–2.5% (công thức Rank Math: số lần ÷ tổng từ) | 30/30 |
| Từ khoá trong 10% đầu bài | có | 30/30 |
| Từ khoá trong slug | có | 30/30 |
| Alt ảnh đầu tiên | chứa từ khoá chính | 30/30 |
| Internal link | 2–4 link nội bộ, ≤1 external | 30/30 |
| CTA có thông tin liên hệ | có | 30/30 |

Độ dài thân bài **1.160–2.180 từ/bài**, tổng khoảng **43.000 từ**.

### Từ khoá chính đã chọn

Dòng `TỪ KHÓA` trong mỗi file xếp **từ khoá chính đứng đầu**, các từ khoá phụ theo sau
(Rank Math hỗ trợ nhiều focus keyword; chỉ từ đầu tiên được chấm mật độ).

Ba slug đã đổi sang tiếng Việt cho đúng ý định tìm kiếm và để chứa từ khoá chính:

| Slug cũ | Slug đang dùng |
|---|---|
| `/rhize-track-and-trace/` | `/rhize-truy-xuat-nguon-goc/` |
| `/rhize-quan-ly-kho/` | `/rhize-quan-ly-kho-vat-tu/` |
| `/rhize-nganh-san-xuat-roi-rac/` | `/rhize-san-xuat-roi-rac-serial/` |

### Script liên quan

- `scripts/gen_diagrams9.py` — sinh 13 sơ đồ SVG riêng của cụm Rhize (màu `#6E56CF`).
- `scripts/insert_images.py` — bảng `_RHIZE` ánh xạ slug → bộ 3 sơ đồ, và `_RHIZE_ALT`
  cho alt ảnh đại diện chứa từ khoá chính. Chạy lại script không làm hỏng bài.
- `scripts/gen_meta_covers.py` — 4 nhóm `Rhize — …` trong `GROUPS`, sinh ảnh bìa + sheet metadata.
