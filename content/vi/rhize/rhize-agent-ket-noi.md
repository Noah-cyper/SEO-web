<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-agent-ket-noi/
TỪ KHÓA    : rhize agent | libre agent | kết nối plc scada | thu thập dữ liệu nhà máy | subscribe tag | đọc ghi thiết bị
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Tên dịch vụ theo tài liệu Rhize (libre-agent); danh sách driver đối chiếu bản phát hành đang dùng.
-->

TITLE TAG   : Rhize Agent – Kết Nối PLC, SCADA Vào Data Hub
META (152)  : Rhize Agent (libre-agent) thu thập dữ liệu từ PLC, SCADA, thiết bị hiện trường: subscribe tag, publish lên NATS, cho phép BPMN đọc ghi ngược lại thiết bị.
H1          : Rhize Agent – Kết Nối Thiết Bị Vào Data Hub

---

## Rhize Agent là gì?

<!--IMG:rep-->
![Rhize Agent - Kết Nối Thiết Bị Vào Data Hub](assets/diagrams/rep-agent.svg)


**Rhize Agent** (tên dịch vụ **libre-agent**) là thành phần đứng ở ranh giới giữa **lớp OT** — PLC, SCADA, thiết bị hiện trường — và phần còn lại của Manufacturing Data Hub. Nó làm hai việc theo hai chiều:

- **Chiều đọc:** đăng ký (subscribe) các tag ở nguồn dữ liệu, phát hiện thay đổi và **publish lên NATS** để các dịch vụ khác xử lý.
- **Chiều ghi:** tạo giao diện cho **BPMN engine** gửi lệnh **đọc và ghi** xuống nguồn dữ liệu và thiết bị gắn với nó.

Chiều thứ hai là điều mà nhiều nền tảng thu thập dữ liệu không có. Nó cho phép workflow không chỉ *quan sát* nhà máy mà còn *tác động* — ví dụ nạp thông số công thức xuống máy khi bắt đầu một mẻ mới.

> **Cần khảo sát khả năng kết nối thiết bị hiện có?** Gửi danh sách PLC/SCADA → [Nhận tư vấn kết nối](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Rhize Agent kết nối được với nguồn nào?

| Nguồn dữ liệu | Giao thức | Ghi chú triển khai |
|---|---|---|
| **PLC/DCS hiện đại** | **OPC UA** | Cách kết nối chuẩn, hỗ trợ subscription |
| **Broker UNS** | **MQTT** | Ghép vào kiến trúc UNS sẵn có |
| **PLC đời cũ** | Modbus TCP/RTU qua gateway | Cần gateway chuyển đổi ở hiện trường |
| **SCADA / historian** | OPC UA hoặc API của hệ thống | Tránh trùng lặp đường lấy dữ liệu |
| **Thiết bị đo độc lập** | Qua bộ chuyển đổi tín hiệu | Xem [bộ chuyển đổi tín hiệu Seneca](/bo-chuyen-doi-tin-hieu-seneca/) |

Với nhà máy Việt Nam, dòng thứ ba là thực tế phổ biến nhất khi triển khai Rhize Agent: dây chuyền có tuổi đời 10–15 năm, PLC không nói OPC UA. Giải pháp thường là đặt **gateway Modbus–OPC UA/MQTT** ở tủ điện, hoặc dùng nền tảng kết nối máy cũ như [ei3](/ei3/) cho các máy OEM khó can thiệp.

---

## Rhize Agent hoạt động thế nào?

1. Rhize Agent được cấu hình danh sách **tag cần theo dõi** ở từng nguồn dữ liệu.
2. Rhize Agent **subscribe** các tag đó — nhận thông báo khi giá trị đổi, thay vì hỏi liên tục theo chu kỳ.
3. Mỗi thay đổi được **publish lên NATS** kèm định danh nguồn và mốc thời gian.
4. **Rhize Core** nhận sự kiện, gắn ngữ cảnh ISA-95 và ghi vào Rhize DB.
5. Ở chiều ngược lại, **BPMN engine** gửi yêu cầu đọc/ghi qua Rhize Agent xuống thiết bị.

Cơ chế **subscribe thay vì polling** của Rhize Agent ở bước 2 quan trọng hơn vẻ bề ngoài: nó giảm tải lên PLC và mạng OT, đồng thời giữ độ trễ thấp — điều kiện để tính downtime chính xác tới giây.

| Bước | Rhize Agent làm gì | Kết quả |
|---|---|---|
| 1 | Nhận cấu hình danh sách tag cần theo dõi | Biết phải nghe gì |
| 2 | Subscribe tag ở nguồn, không hỏi theo chu kỳ | Giảm tải lên PLC |
| 3 | Publish thay đổi lên NATS kèm mốc thời gian | Sự kiện vào nền tảng |
| 4 | Nhận lệnh đọc/ghi từ BPMN engine | Tác động ngược xuống thiết bị |

---

## So sánh cách thu thập dữ liệu

| Tiêu chí | Polling định kỳ | Xuất file/CSV | **Rhize Agent (subscribe)** |
|---|---|---|---|
| Độ trễ | Bằng chu kỳ quét | Hàng giờ | **Gần thời gian thực** |
| Tải lên PLC | Cao khi nhiều tag | Thấp | **Thấp** |
| Bắt được xung ngắn | Dễ bỏ sót | Không | **Có** |
| Ghi ngược xuống thiết bị | Hiếm khi có | Không | **Có, qua BPMN** |
| Thêm tag mới | Sửa cấu hình quét | Sửa script xuất | **Thêm vào danh sách subscribe** |

Việc bỏ sót xung ngắn (dòng 3) là nguyên nhân âm thầm khiến số liệu OEE của nhiều nhà máy không khớp với cảm nhận của quản đốc: những lần dừng vài chục giây không được ghi nhận.

---

## Ứng dụng Rhize Agent theo bài toán

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Đếm sản lượng và dừng máy chính xác:** nền tảng cho OEE đáng tin. Xem [Rhize và OEE](/rhize-oee/).
- **Ghi thông số quá trình vào hồ sơ lô:** nhiệt độ, áp suất, thời gian giữ nhiệt gắn thẳng vào batch record. Xem [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Nạp công thức xuống máy:** workflow ghi thông số setpoint khi đổi mã sản phẩm, giảm lỗi nhập tay.
- **Giám sát năng lượng theo công đoạn:** ghép công tơ với work unit để tính suất tiêu hao thật.

| Bài toán | Dữ liệu Rhize Agent cần lấy | Nguồn |
|---|---|---|
| OEE | Trạng thái máy, bộ đếm sản lượng | PLC |
| Hồ sơ lô | Nhiệt độ, áp suất, thời gian giữ | PLC / SCADA |
| Truy xuất | Sự kiện đổi lô nguyên liệu | Máy quét, cân |
| Năng lượng | Điện năng theo công đoạn | Công tơ Modbus |

---

## Chuẩn bị hạ tầng hiện trường trước khi triển khai Rhize Agent

| Hạng mục | Cần kiểm tra | Lý do |
|---|---|---|
| **Giao thức PLC** | Có OPC UA server không | Quyết định cần gateway hay không |
| **Danh mục tag** | Tên tag có quy tắc không | Ánh xạ vào model ISA-95 |
| **Mạng OT** | VLAN, tường lửa, băng thông | Chính sách an toàn thông tin |
| **Đồng hồ hệ thống** | NTP đồng bộ chưa | Sai giờ làm hỏng mọi phân tích |
| **Điểm đo còn thiếu** | Có cần thêm cảm biến | Xem [cảm biến áp suất](/cam-bien-ap-suat/), [cảm biến nhiệt độ](/cam-bien-nhiet-do/) |

Dòng thứ tư bị bỏ qua thường xuyên. Nếu PLC, SCADA và máy chủ lệch giờ nhau vài phút, mọi tương quan sự kiện đều sai — và lỗi này rất khó phát hiện về sau.

---

<a name="bao-gia"></a>
## Nhận tư vấn kết nối thiết bị với Rhize Agent

Gửi cho chúng tôi: **danh sách PLC/SCADA (hãng, đời) · giao thức đang có · số tag cần lấy · sơ đồ mạng OT · điểm đo còn thiếu.**

Chúng tôi khảo sát khả năng kết nối, đề xuất gateway/thiết bị bổ sung ở hiện trường và cách ánh xạ tag vào mô hình ISA-95.

**→ [Liên hệ tư vấn kết nối Rhize Agent](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PLC đời cũ không có OPC UA thì kết nối kiểu gì?**
Qua **gateway** chuyển Modbus/giao thức hãng sang OPC UA hoặc MQTT, đặt tại tủ điện. Với máy OEM không được phép can thiệp, dùng nền tảng kết nối chuyên biệt như [ei3](/ei3/).

**Rhize Agent có ghi được xuống PLC không?**
Có. Rhize Agent tạo giao diện để **BPMN engine** gửi lệnh đọc và ghi tới nguồn dữ liệu và thiết bị. Quyền ghi cần kiểm soát chặt và có ghi vết.

**Đặt Rhize Agent ở đâu trong mạng nhà máy?**
Thường đặt ở vùng có thể nhìn thấy lớp OT nhưng vẫn nằm trong chính sách phân vùng mạng. Chi tiết thống nhất với bộ phận an toàn thông tin.

**Có giới hạn số tag không?**
Giới hạn thực tế đến từ tài nguyên cluster và tải lên thiết bị nguồn, không phải từ một con số cố định. Nên thử tải với số tag thật trước khi mở rộng.

**Đang có historian rồi có cần Rhize Agent nữa không?**
Có thể lấy dữ liệu qua historian thay vì nối thẳng PLC. Nhưng nếu cần độ trễ thấp và bắt được sự kiện ngắn, kết nối trực tiếp qua Rhize Agent cho kết quả tốt hơn.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-opc-ua/, /rhize-nats-event-streaming/, /rhize-tich-hop-scada-historian/, /lien-he/. -->
