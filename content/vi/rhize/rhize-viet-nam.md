<!--
LOẠI TRANG : Trang hãng (brand hub / pillar) — Thương mại + giải pháp
URL SLUG   : /rhize/
TỪ KHÓA    : rhize | rhize việt nam | manufacturing data hub | nền tảng dữ liệu sản xuất | isa-95 | mes thế hệ mới
INTENT     : Thương mại + thương hiệu + giải pháp
TRẠNG THÁI : Sẵn đăng. Đối chiếu tài liệu rhize.com & docs.rhize.com trước khi đăng; số hiệu phiên bản và phụ thuộc thay đổi theo bản phát hành. Giá & phạm vi triển khai theo dự án.
-->

TITLE TAG   : Rhize Việt Nam – Manufacturing Data Hub Chuẩn ISA-95
META (148)  : Rhize – Manufacturing Data Hub thời gian thực chuẩn ISA-95: graph database, GraphQL API, BPMN workflow, kết nối OPC UA và MQTT. Tư vấn & triển khai.
H1          : Rhize – Manufacturing Data Hub Chuẩn ISA-95

---

## Rhize là gì?

<!--IMG:rep-->
![Rhize - Manufacturing Data Hub Chuẩn ISA-95](assets/diagrams/rep-mdh.svg)


**Rhize** là **Manufacturing Data Hub (MDH)** — nền tảng dữ liệu sản xuất **thời gian thực, hướng sự kiện (event-driven)** và **headless**, cho phép nhà máy dựng một **mô hình dữ liệu chuẩn ISA-95** cho toàn bộ hoạt động: từ thiết bị, vật tư, con người tới quy trình và đơn hàng.

Khác với một MES đóng gói sẵn, **Rhize** không áp đặt giao diện hay quy trình cố định. Nó cung cấp **lớp dữ liệu và lớp điều phối** — phần ứng dụng (giao diện vận hành, báo cáo, tích hợp) do nhà máy hoặc đối tác xây trên **một endpoint GraphQL duy nhất**. Đây chính là ý nghĩa của chữ *headless*: dữ liệu và logic tách khỏi giao diện.

Ba việc mà **Rhize** làm khác với kho dữ liệu truyền thống:

- **Chuẩn hoá theo ISA-95** ngay ở tầng lưu trữ, thay vì đổ dữ liệu thô vào data lake rồi mới đi làm ngữ cảnh.
- **Xử lý sự kiện phức hợp**: dữ liệu tag từ PLC/SCADA được biến thành sự kiện có ngữ cảnh (mẻ nào, máy nào, ca nào, lệnh sản xuất nào).
- **Điều phối quy trình bằng BPMN** low-code, để logic nghiệp vụ nằm trong workflow chứ không nằm rải rác trong code tích hợp.

> **Cần đánh giá Rhize cho nhà máy của bạn?** Gửi **hiện trạng hệ thống · số máy/dòng · mục tiêu (OEE, truy xuất, batch record)** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Manufacturing Data Hub khác gì MES, historian và data lake?

Nhà máy Việt Nam thường có sẵn 3 lớp: **PLC/SCADA** ở dưới, **historian** ghi tag, **ERP** ở trên. Vấn đề không nằm ở chỗ thiếu dữ liệu — mà ở chỗ dữ liệu **không có ngữ cảnh**: một tag `Line3_Temp` trong historian không tự biết nó thuộc mẻ nào, sản phẩm nào, ca nào.

| Hệ thống | Lưu gì | Điểm mạnh | Điểm yếu với bài toán truy xuất |
|---|---|---|---|
| **Historian** | Chuỗi thời gian theo tag | Nén tốt, truy vấn tag nhanh | Không có quan hệ vật tư – lệnh SX – nhân sự |
| **MES đóng gói** | Giao dịch sản xuất | Có sẵn quy trình, triển khai nhanh | Khó mở rộng, khoá vào một nhà cung cấp |
| **Data lake / warehouse** | Dữ liệu thô, theo lô | Rẻ khi lưu lượng lớn | Độ trễ cao, ngữ cảnh phải dựng lại ở tầng BI |
| **UNS (MQTT broker)** | Luồng tin nhắn theo topic | Realtime, dễ mở rộng | Không lưu trạng thái, không truy vấn lịch sử theo quan hệ |
| **Rhize MDH** | Đồ thị tri thức ISA-95 + chuỗi thời gian | Realtime, có ngữ cảnh, truy vấn theo quan hệ | Cần đầu tư mô hình hoá dữ liệu ban đầu |

Data Hub không thay thế toàn bộ những lớp trên. Trên thực tế nó thường đóng vai **lớp tích hợp**: nhận dữ liệu từ SCADA/historian/PLC, chuẩn hoá theo ISA-95, rồi phục vụ lại cho ERP và ứng dụng phân tích. Xem chi tiết trong bài [Manufacturing Data Hub là gì](/manufacturing-data-hub-la-gi/) và [so sánh Rhize với MES, historian, data lake](/rhize-vs-mes-historian-data-lake/).

---

## Kiến trúc và các thành phần hệ thống Rhize

Nền tảng này là tập hợp các **microservice ghép lỏng**, triển khai trên **Kubernetes** qua **Helm**. Kiến trúc phân tán này là điều kiện để mở rộng ngang và giữ độ sẵn sàng cao khi nhà máy tăng số điểm dữ liệu.

| Thành phần | Vai trò | Ghi chú kỹ thuật |
|---|---|---|
| **Rhize DB (libreBaas)** | Cơ sở dữ liệu đồ thị, schema ISA-95 | Cài trước tiên; phát hành GraphQL endpoint |
| **Libre Core** | Dịch vụ lõi, xử lý luật & sự kiện | Biến dữ liệu tag thành sự kiện có ngữ cảnh |
| **BPMN engine (Workflow)** | Engine chạy workflow low-code | Phụ thuộc libreBaas, Restate, Tempo |
| **Libre Agent** | Kết nối nguồn dữ liệu & thiết bị | Subscribe tag, publish thay đổi lên NATS |
| **Libre Admin UI** | Giao diện quản trị & mô hình hoá | Quản lý model, người dùng, workflow |
| **Router (Apollo Router)** | Cổng GraphQL hợp nhất | Một điểm truy cập duy nhất cho ứng dụng |

Các dịch vụ nền tảng đi kèm: **NATS** làm message broker, **Keycloak** cho xác thực OIDC/SSO, **Grafana + Tempo** cho giám sát và truy vết (tracing) tiến trình BPMN, **Restate** cho điều phối dịch vụ.

Chi tiết từng thành phần trong nền tảng: [kiến trúc](/kien-truc-nen-tang-rhize/), [cơ sở dữ liệu đồ thị](/rhize-db-graph-database/), [BPMN workflow](/rhize-bpmn-workflow/), [Libre Agent](/rhize-agent-ket-noi/).

---

## Rhize dùng ISA-95 như thế nào?

**ISA-95** (tương đương **IEC 62264**) là chuẩn quốc tế mô tả cách trao đổi dữ liệu giữa hệ thống doanh nghiệp và hệ thống điều khiển sản xuất. Mô hình dữ liệu của nền tảng lấy phần lớn từ **Part 2** — mô hình phân cấp thiết bị theo vai trò (enterprise → site → area → work center → work unit) và bốn nhóm tài nguyên: **thiết bị, vật tư, nhân sự, tài sản vật lý**.

| Khái niệm ISA-95 | Ý nghĩa trong nhà máy | Dùng để làm gì trong Rhize |
|---|---|---|
| **Equipment hierarchy** | Cây thiết bị theo vai trò | Gắn ngữ cảnh cho mọi sự kiện |
| **Material** | Định nghĩa & lô vật tư | Truy xuất nguồn gốc, genealogy |
| **Personnel** | Người, tổ, kỹ năng | Ghi nhận ai vận hành, ai duyệt |
| **Operations definition** | Công thức / định nghĩa công đoạn | Chuẩn hoá quy trình giữa các nhà máy |
| **Operations schedule / performance** | Kế hoạch và kết quả thực thi | So kế hoạch với thực tế, tính OEE |

Vì mô hình đã chuẩn hoá, cùng một truy vấn OEE chạy được ở nhiều nhà máy khác nhau mà không phải viết lại. Đây là điểm khác biệt lớn nhất so với cách tích hợp point-to-point. Xem thêm [Rhize và ISA-95](/rhize-isa-95/) và [B2MML](/rhize-b2mml/).

---

## Rhize kết nối được với những hệ thống nào?

| Lớp | Giao thức / chuẩn | Vai trò trong Rhize |
|---|---|---|
| Thiết bị, PLC | **OPC UA**, Modbus qua gateway | Đọc/ghi tag qua Libre Agent |
| Đường truyền sự kiện | **MQTT**, **NATS** | Nhận và phát sự kiện thời gian thực |
| Ứng dụng, dashboard | **GraphQL** | Một endpoint duy nhất, truy vấn theo quan hệ |
| ERP (SAP…) | **OData**, REST | Đồng bộ lệnh sản xuất, vật tư, kết quả |
| Trao đổi chuẩn ngành | **B2MML** | Xuất/nhập dữ liệu ISA-95 dạng XML |

Nếu nhà máy đang chạy **UNS trên MQTT**, nền tảng ghép vào mà không phá kiến trúc sẵn có: broker vẫn giữ vai trò truyền tin, **Rhize** bổ sung phần lưu trạng thái và ngữ cảnh mà broker không làm. Xem [Rhize với MQTT và UNS](/rhize-mqtt-uns/), [Rhize với OPC UA](/rhize-opc-ua/), [tích hợp ERP](/rhize-tich-hop-erp/), [tích hợp SCADA & historian](/rhize-tich-hop-scada-historian/).

---

## Ứng dụng Rhize theo bài toán nhà máy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **OEE và quản lý hiệu suất** — tính OEE từ sự kiện có ngữ cảnh thay vì từ tag rời rạc: [Rhize và OEE](/rhize-oee/).
- **Batch record điện tử thời gian thực** — hồ sơ lô hình thành ngay trong lúc chạy, không chờ tổng hợp cuối mẻ: [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Truy xuất nguồn gốc (track & trace)** — đi ngược từ thành phẩm về lô nguyên liệu, thiết bị và ca vận hành: [track & trace](/rhize-truy-xuat-nguon-goc/).
- **Quản lý chất lượng** — gắn kết quả kiểm với đúng lô, đúng thiết bị: [quản lý chất lượng](/rhize-quan-ly-chat-luong/).
- **Lập kế hoạch và điều độ** — nhận lệnh từ ERP, chia xuống work center: [scheduling](/rhize-scheduling-lap-ke-hoach/).
- **Quản lý kho và vật tư tại xưởng** — [warehouse](/rhize-quan-ly-kho-vat-tu/).
- **Nền dữ liệu cho AI/ML** — luồng sự kiện sạch, có nhãn, dùng trực tiếp cho mô hình: [AI/ML trên dữ liệu Rhize](/rhize-ai-ml-du-lieu-san-xuat/).

Theo ngành: [dược phẩm & life sciences](/rhize-nganh-duoc-pham/), [thực phẩm – đồ uống](/rhize-nganh-thuc-pham-do-uong/), [sản xuất rời rạc có serial](/rhize-san-xuat-roi-rac-serial/).

| Bài toán ưu tiên | Dữ liệu tối thiểu cần có | Thời gian tới kết quả đầu tiên |
|---|---|---|
| OEE một dây chuyền | Trạng thái máy + bộ đếm sản lượng | Ngắn nhất — không đổi thao tác vận hành |
| Truy xuất nguồn gốc | Mã lô + điểm quét tại nơi nạp liệu | Trung bình — cần đổi thao tác ở xưởng |
| Hồ sơ lô điện tử | Thông số quá trình + xác nhận điện tử | Dài — phụ thuộc thẩm định của QA |
| Giám sát năng lượng | Công tơ gắn với từng công đoạn | Ngắn — chủ yếu là lắp thêm đồng hồ đo |
| Nền dữ liệu cho AI | Sự kiện có nhãn chất lượng | Tích luỹ dần, tính theo quý |

---

## Điều kiện triển khai Rhize tại nhà máy Việt Nam

| Hạng mục | Yêu cầu tối thiểu | Ghi chú |
|---|---|---|
| Nền tảng chạy | **Kubernetes** (on-prem hoặc cloud) | Cài từng dịch vụ bằng **Helm**; libreBaas trước |
| Xác thực | **Keycloak** / OIDC | Có thể ghép SSO/AD sẵn có của nhà máy |
| Mạng | Kết nối tới lớp OT (OPC UA/MQTT) | Tách VLAN OT/IT, tường lửa theo chính sách |
| Nhân sự | 1 kỹ sư dữ liệu + 1 kỹ sư tự động hoá | Mô hình hoá ISA-95 là phần tốn công nhất |
| Giai đoạn | Bắt đầu 1 dây chuyền | Nhân bản model sang dây chuyền khác gần như miễn phí |

Sai lầm hay gặp là triển khai đồng loạt cả nhà máy ngay từ đầu. Cách chắc ăn hơn: chọn **một dây chuyền có bài toán rõ** (thường là OEE hoặc truy xuất lô), dựng model ISA-95 cho dây chuyền đó, chạy ổn định 4–8 tuần, rồi mới nhân rộng. Xem [triển khai trên Kubernetes](/rhize-trien-khai-kubernetes/).

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá Rhize

Vì sao chọn HOANTRANTDH:

- ✅ Tư vấn **theo bài toán**, không bán phần mềm theo danh sách tính năng.
- ✅ Hiểu lớp OT: đội ngũ làm **cảm biến, transmitter, PLC** — biết dữ liệu từ hiện trường thực sự trông như thế nào. Xem [SCADA là gì](/scada-la-gi/), [PLC và IoT](/plc-va-iot/).
- ✅ Ghép được với thiết bị hiện trường sẵn có: [bộ chuyển đổi tín hiệu Seneca](/bo-chuyen-doi-tin-hieu-seneca/), gateway Modbus, [nền tảng IIoT ei3](/ei3/).
- ✅ Hỗ trợ giai đoạn mô hình hoá ISA-95 — phần quyết định thành bại của dự án.

Gửi cho chúng tôi: **danh sách hệ thống đang chạy (SCADA/historian/ERP) · số dây chuyền · giao thức hiện có (OPC UA/MQTT/Modbus) · mục tiêu ưu tiên (OEE, batch record, truy xuất) · mốc thời gian.**

Đội kỹ thuật HOANTRANTDH sẽ phác kiến trúc, ước lượng khối lượng mô hình hoá và đưa phương án theo giai đoạn.

**→ [Liên hệ tư vấn & báo giá Rhize](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize có phải là MES không?**
Không hẳn. **Rhize** là **Manufacturing Data Hub** — lớp dữ liệu và điều phối chuẩn ISA-95. Nó có thể làm **backend cho MES**, hoặc thay dần một MES cũ theo từng phân hệ, nhưng bản thân nó headless, không kèm giao diện vận hành đóng gói sẵn.

**Đang có historian và SCADA rồi thì lắp Rhize vào để làm gì?**
Historian trả lời "giá trị tag lúc 9h là bao nhiêu". **Rhize** trả lời "lô hàng X chạy trên máy nào, ai vận hành, nguyên liệu lô nào, vì sao chậm 12 phút". Đó là câu hỏi mà truy xuất và OEE cần.

**Rhize chạy on-premise được không?**
Được. Nền tảng chạy trên **Kubernetes**, triển khai tại chỗ hoặc trên cloud. Nhà máy có yêu cầu dữ liệu không ra khỏi biên giới vẫn triển khai được on-prem.

**Triển khai mất bao lâu?**
Phụ thuộc phạm vi. Một dây chuyền với bài toán rõ ràng thường tính theo tuần cho bản chạy được; phần tốn thời gian nhất là **mô hình hoá ISA-95** và làm sạch dữ liệu nguồn, không phải cài đặt.

**Cần đội ngũ như thế nào để vận hành?**
Tối thiểu một người hiểu dữ liệu (GraphQL, mô hình hoá) và một kỹ sư tự động hoá nắm lớp OT. Không cần đội lập trình lớn vì phần lớn logic viết bằng **BPMN low-code**.

**HOANTRANTDH hỗ trợ được đến đâu?**
Tư vấn kiến trúc, mô hình hoá ISA-95, kết nối lớp hiện trường và bàn giao kèm tài liệu. Phạm vi cụ thể thống nhất theo dự án.

<!-- SCHEMA: Organization + FAQPage + BreadcrumbList. INTERNAL LINK: /manufacturing-data-hub-la-gi/, /kien-truc-nen-tang-rhize/, /rhize-isa-95/, /rhize-oee/, /ei3/, /lien-he/. -->
