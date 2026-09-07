<!--
LOẠI TRANG : Bài trụ khái niệm (pillar) — Thông tin + giải pháp
URL SLUG   : /manufacturing-data-hub-la-gi/
TỪ KHÓA    : manufacturing data hub | mdh là gì | trung tâm dữ liệu sản xuất | rhize | data hub nhà máy | dữ liệu sản xuất thời gian thực
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu tài liệu rhize.com trước khi đăng.
-->

TITLE TAG   : Manufacturing Data Hub Là Gì? MDH Trong Nhà Máy Số
META (141)  : Manufacturing Data Hub là gì, khác gì MES, historian, data lake và UNS. Kiến trúc MDH hướng sự kiện chuẩn ISA-95 và cách bắt đầu tại nhà máy.
H1          : Manufacturing Data Hub Là Gì Trong Nhà Máy Số?

---

## Manufacturing Data Hub là gì?

<!--IMG:rep-->
![Manufacturing Data Hub Là Gì Trong Nhà Máy Số?](assets/diagrams/rep-mdh.svg)


**Manufacturing Data Hub** (viết tắt **Manufacturing Data Hub**, tạm dịch *trung tâm dữ liệu sản xuất*) là lớp phần mềm đứng giữa hệ thống điều khiển ở xưởng và hệ thống quản trị doanh nghiệp, làm ba việc: **thu thập** dữ liệu từ mọi nguồn, **chuẩn hoá** theo một mô hình thống nhất, và **phục vụ lại** cho mọi ứng dụng qua một giao diện duy nhất.

Điểm khiến **Manufacturing Data Hub** khác các kiến trúc trước đó nằm ở chữ *Manufacturing Data Hub*: thay vì nối từng cặp hệ thống với nhau (SCADA ↔ ERP, historian ↔ BI, MES ↔ LIMS), mọi hệ thống chỉ nối vào **một trung tâm**. Số kết nối giảm từ cấp số nhân xuống cấp số cộng.

**Rhize** là nền tảng đầu tiên tự định danh là **Manufacturing Data Hub** thời gian thực, hướng sự kiện và chuẩn **ISA-95**. Xem [trang hãng Rhize](/rhize/).

> **Đang cân nhắc kiến trúc dữ liệu cho nhà máy?** Gửi hiện trạng hệ thống → [Nhận tư vấn kiến trúc](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Vì sao nhà máy cần một Manufacturing Data Hub?

Nhà máy Việt Nam hiếm khi thiếu dữ liệu. Cái thiếu là **ngữ cảnh** và **khả năng dùng lại**.

Một ví dụ quen thuộc: dây chuyền chiết rót có PLC ghi tốc độ, historian lưu nhiệt độ, cân ghi khối lượng, phòng QC nhập kết quả vào Excel, ERP giữ lệnh sản xuất. Khi khách hàng khiếu nại một lô, việc ghép năm nguồn đó lại mất vài ngày — vì không nguồn nào biết "lô" là gì.

| Triệu chứng thường gặp | Nguyên nhân gốc | Manufacturing Data Hub xử lý thế nào |
|---|---|---|
| Truy xuất lô mất nhiều ngày | Dữ liệu không gắn với lô | Mọi sự kiện gắn sẵn material lot |
| Mỗi báo cáo OEE ra một số khác | Mỗi nơi định nghĩa downtime khác | Định nghĩa chuẩn hoá ở tầng model |
| Thêm một dây chuyền là làm lại tích hợp | Tích hợp point-to-point | Nhân bản model, không viết lại kết nối |
| Dự án AI dừng ở PoC | Dữ liệu bẩn, không nhãn | Luồng sự kiện có ngữ cảnh sẵn |
| Đổi nhà cung cấp MES rất đắt | Dữ liệu khoá trong MES | Dữ liệu nằm ở Manufacturing Data Hub, ứng dụng thay được |

---

## Kiến trúc một Manufacturing Data Hub gồm những gì?

| Lớp | Chức năng | Ở Rhize là thành phần nào |
|---|---|---|
| **Thu thập** | Đọc tag, nhận bản tin từ thiết bị | **Libre Agent** (OPC UA, MQTT) |
| **Truyền sự kiện** | Bus tin nhắn độ trễ thấp | **NATS** |
| **Ontology / mô hình** | Định nghĩa ISA-95, quan hệ | Schema trong **Rhize DB** |
| **Lưu trữ** | Đồ thị giao dịch + chuỗi thời gian | **Rhize DB (libreBaas)** |
| **Xử lý luật** | Biến dữ liệu thành sự kiện có nghĩa | **Libre Core** / rules engine |
| **Điều phối** | Workflow nghiệp vụ low-code | **BPMN engine** |
| **Truy cập** | Một endpoint cho mọi ứng dụng | **GraphQL** qua **Apollo Router** |

Bốn lớp giữa là phần làm nên giá trị. Không có ontology, Manufacturing Data Hub chỉ là một cái ống dẫn; không có xử lý luật, dữ liệu vẫn thô; không có điều phối, mọi logic lại rơi về code tích hợp rời rạc.

Chi tiết kiến trúc: [kiến trúc nền tảng Rhize](/kien-truc-nen-tang-rhize/).

---

## Manufacturing Data Hub và ISA-95

**ISA-95** (**IEC 62264**) cho **Manufacturing Data Hub** thứ mà mọi kiến trúc dữ liệu đều cần nhưng ít nơi có: một **từ vựng chung** đã được ngành thống nhất.

| Đối tượng ISA-95 | Trả lời câu hỏi | Ví dụ trong nhà máy |
|---|---|---|
| **Equipment** | Chạy ở đâu | Site → Area → Line 3 → Máy chiết |
| **Material lot** | Nguyên liệu nào | Lô bột mì NL-2024-118 |
| **Personnel** | Ai làm | Ca B, tổ trưởng Nguyễn |
| **Operations definition** | Làm theo công thức nào | Recipe bánh quy 250g rev.4 |
| **Job response** | Kết quả ra sao | 4.820 sp, 12 phút dừng, 3 phế |

Khi năm đối tượng này có mặt trong mọi sự kiện, truy xuất nguồn gốc trở thành **một truy vấn**, không phải một dự án. Xem [Rhize và ISA-95](/rhize-isa-95/).

---

## So sánh Manufacturing Data Hub với các kiến trúc dữ liệu khác

| Tiêu chí | Historian | Data lake | UNS thuần MQTT | **Manufacturing Data Hub** |
|---|---|---|---|---|
| Độ trễ | Thấp | Cao | Rất thấp | **Thấp** |
| Ngữ cảnh sản xuất | Không | Dựng ở tầng BI | Theo quy ước topic | **Có sẵn theo ISA-95** |
| Truy vấn theo quan hệ | Không | Chậm | Không | **Có (graph)** |
| Lưu trạng thái | Theo tag | Có | Không | **Có** |
| Điều phối quy trình | Không | Không | Không | **Có (BPMN)** |
| Phù hợp làm nền cho AI | Hạn chế | Có nhưng tốn xử lý | Hạn chế | **Tốt** |

**MDH** không loại bỏ những thứ trên. Historian vẫn tốt cho tag tần số cao; data lake vẫn hợp lý cho phân tích dài hạn; UNS vẫn là cách truyền tin gọn. **Manufacturing Data Hub** ngồi giữa và làm phần mà cả ba đều không làm: **giữ ngữ cảnh sản xuất ở thời gian thực**. Xem [so sánh chi tiết Rhize với MES, historian, data lake](/rhize-vs-mes-historian-data-lake/).

---

## Ứng dụng thực tế của Manufacturing Data Hub tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thực phẩm – đồ uống:** một nhà máy nước giải khát cần chứng minh chuỗi lạnh và truy xuất lô trong 4 giờ khi có sự cố. Với **MDH**, dữ liệu nhiệt độ đã gắn sẵn với lô và thiết bị. Xem [ngành thực phẩm – đồ uống](/rhize-nganh-thuc-pham-do-uong/).
- **Dược phẩm:** hồ sơ lô điện tử hình thành trong lúc chạy thay vì tổng hợp cuối mẻ, rút ngắn thời gian xuất lô. Xem [ngành dược phẩm](/rhize-nganh-duoc-pham/).
- **Điện tử, cơ khí chính xác:** gắn serial thành phẩm với linh kiện, máy và thông số gia công. Xem [sản xuất rời rạc có serial](/rhize-san-xuat-roi-rac-serial/).
- **Xi măng, thép, hoá chất:** ghép dữ liệu năng lượng với sản lượng theo từng công đoạn để tính suất tiêu hao thật.

---

## Bắt đầu triển khai Manufacturing Data Hub như thế nào?

| Giai đoạn | Việc cần làm | Thời lượng tham khảo |
|---|---|---|
| **1. Chọn phạm vi** | Một dây chuyền, một bài toán đo được | 1–2 tuần |
| **2. Mô hình hoá ISA-95** | Cây thiết bị, vật tư, công thức | 2–4 tuần |
| **3. Kết nối nguồn** | OPC UA/MQTT từ PLC, SCADA, cân, LIMS | 2–3 tuần |
| **4. Workflow & ứng dụng** | BPMN, dashboard, báo cáo | 2–4 tuần |
| **5. Nhân rộng** | Nhân bản model sang dây chuyền khác | Ngắn dần theo từng lần |

Nguyên tắc thực dụng: **đừng mô hình hoá cả nhà máy trước khi có kết quả đầu tiên**. Giá trị của một **Manufacturing Data Hub** nằm ở chỗ model dùng lại được — nhưng chỉ chứng minh được điều đó sau khi dây chuyền đầu tiên chạy thật.

---

<a name="bao-gia"></a>
## Nhận tư vấn kiến trúc dữ liệu sản xuất

Gửi cho chúng tôi: **hệ thống đang chạy (SCADA/historian/MES/ERP) · số dây chuyền · giao thức sẵn có · bài toán ưu tiên · mốc thời gian.**

HOANTRANTDH sẽ phác kiến trúc **Manufacturing Data Hub** phù hợp hiện trạng, chỉ rõ phần nào giữ lại, phần nào thay, và khối lượng công việc từng giai đoạn.

**→ [Liên hệ tư vấn Manufacturing Data Hub](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Manufacturing Data Hub có thay được MES không?**
Có thể thay dần theo từng phân hệ. **MDH** giữ dữ liệu và logic; các chức năng MES được dựng lại như ứng dụng chạy trên Manufacturing Data Hub. Cách an toàn hơn là để **MDH** đóng vai lớp tích hợp trước, rồi chuyển dần chức năng sang.

**Nhà máy chưa có historian thì triển khai được không?**
Được. **MDH** đọc trực tiếp từ PLC/SCADA qua OPC UA hoặc MQTT. Historian không phải điều kiện bắt buộc.

**Chi phí lớn nhất của dự án MDH nằm ở đâu?**
Ở **mô hình hoá dữ liệu** và làm sạch nguồn, không phải ở license hay hạ tầng. Đây cũng là phần quyết định dự án có nhân rộng được hay không.

**Manufacturing Data Hub có cần cloud không?**
Không bắt buộc. Nền tảng như **Rhize** chạy trên Kubernetes, triển khai on-premise hoặc cloud tuỳ chính sách dữ liệu của nhà máy.

**Làm sao biết nhà máy đã sẵn sàng cho MDH?**
Ba dấu hiệu: đã có lớp thu thập dữ liệu tự động ở ít nhất một dây chuyền; có người chịu trách nhiệm về dữ liệu sản xuất; và có một bài toán nghiệp vụ đo được bằng tiền hoặc thời gian.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-isa-95/, /rhize-vs-mes-historian-data-lake/, /lien-he/. -->
