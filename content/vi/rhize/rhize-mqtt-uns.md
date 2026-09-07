<!--
LOẠI TRANG : Bài tích hợp (satellite) — Kỹ thuật + giải pháp
URL SLUG   : /rhize-mqtt-uns/
TỪ KHÓA    : mqtt | rhize mqtt | uns là gì | unified namespace | mqtt nhà máy | sparkplug b | kiến trúc uns sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu khả năng hỗ trợ MQTT/Sparkplug của bản Rhize đang dùng trước khi cam kết chi tiết.
-->

TITLE TAG   : Rhize MQTT & UNS – Ghép Data Hub Vào Unified Namespace
META (147)  : Rhize MQTT và UNS: Unified Namespace là gì, vì sao broker MQTT chưa đủ, và cách Data Hub bổ sung lớp trạng thái, ngữ cảnh ISA-95 cho kiến trúc UNS.
H1          : Rhize MQTT & UNS – Bổ Sung Ngữ Cảnh Cho Namespace

---

## UNS là gì và Rhize MQTT đứng ở đâu?

<!--IMG:rep-->
![Rhize MQTT & UNS - Bổ Sung Ngữ Cảnh Cho Namespace](assets/diagrams/rep-nats.svg)


**UNS (Unified Namespace)** là kiến trúc trong đó mọi hệ thống của nhà máy — PLC, SCADA, MES, ERP — cùng publish và subscribe vào **một không gian tên thống nhất**, thường chạy trên broker **MQTT**. Thay vì nối từng cặp hệ thống, tất cả nói chuyện qua một nơi.

UNS giải rất tốt bài toán **truyền tin**. Nhưng nó để lại hai khoảng trống:

- **Không lưu trạng thái.** Broker MQTT chuyển bản tin đi rồi thôi. Muốn biết tuần trước lô nào chạy trên máy nào thì broker không trả lời được.
- **Ngữ cảnh nằm trong quy ước topic.** Cấu trúc topic do người thiết kế đặt ra; nó là thoả thuận, không phải mô hình dữ liệu có thể truy vấn.

**Rhize MQTT** không thay thế UNS — nó **lấp đúng hai khoảng trống đó**: nhận dữ liệu từ broker, gắn ngữ cảnh **ISA-95**, lưu vào đồ thị và cho phép truy vấn theo quan hệ.

> **Đang có UNS và muốn bổ sung lớp dữ liệu?** → [Nhận tư vấn kiến trúc](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Rhize MQTT bổ sung gì cho UNS?

| Nhu cầu | Broker MQTT thuần | **Rhize MQTT + Data Hub** |
|---|---|---|
| Truyền tin thời gian thực | **Có** | Có (giữ nguyên broker) |
| Lưu lịch sử | Không | **Có (graph + time-series)** |
| Truy vấn theo quan hệ | Không | **Có (GraphQL)** |
| Ngữ cảnh sản xuất | Theo quy ước topic | **Theo mô hình ISA-95** |
| Điều phối quy trình | Không | **Có (BPMN)** |
| Truy xuất nguồn gốc | Không | **Có** |

Cách hình dung đơn giản: **UNS là hệ thần kinh, Data Hub là trí nhớ**. Hệ thần kinh truyền tín hiệu rất nhanh nhưng không nhớ; trí nhớ giữ lại và cho phép suy luận về quá khứ.

---

## Kiến trúc kết hợp MQTT và Rhize

| Lớp | Thành phần | Vai trò |
|---|---|---|
| Thiết bị | PLC, cảm biến, gateway | Publish dữ liệu |
| **Broker MQTT** | Broker sẵn có của nhà máy | Không gian tên thống nhất |
| **Rhize Agent** | libre-agent | Subscribe topic, đưa vào nền tảng |
| **NATS** | Bus nội bộ Rhize | Truyền sự kiện giữa dịch vụ |
| **Rhize Core** | libreCore | Gắn ngữ cảnh ISA-95 |
| **Rhize DB** | libreBaas | Lưu graph + time-series |

Cần phân biệt rõ **MQTT** và **NATS**: MQTT là lớp UNS ở phía nhà máy; **NATS** là bus nội bộ giữa các dịch vụ Rhize. Hai thứ tồn tại song song, không thay nhau — xem [NATS trong Rhize](/rhize-nats-event-streaming/).

---

## Thiết kế topic MQTT để ghép được với ISA-95

| Nguyên tắc | Ví dụ topic | Lý do |
|---|---|---|
| Phản ánh cấu trúc vật lý | `nhamay/khu-chiet/line3/may-chiet-2/counter` | Ánh xạ thẳng vào cây thiết bị |
| Một giá trị một topic | Tách nhiệt độ và áp suất | Dễ đăng ký chọn lọc |
| Đặt tên nhất quán giữa các line | Cùng quy ước ở mọi dây chuyền | Nhân bản model được |
| Tránh nhúng thông tin biến động | Không đưa mã lô vào topic | Lô đổi liên tục, topic thì không |
| Kèm mốc thời gian và chất lượng | Payload có timestamp | Phân tích chính xác |

Sai lầm phổ biến nhất là **nhúng dữ liệu biến động vào topic** — ví dụ đưa số lệnh sản xuất vào đường dẫn topic. Khi đó số topic bùng nổ và không ánh xạ được sang mô hình ISA-95. Thông tin biến động thuộc về **payload**, không thuộc về **cấu trúc**.

---

## Ứng dụng thực tế tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Nhà máy đã đầu tư UNS:** giữ nguyên broker và toàn bộ thiết bị đã publish; chỉ thêm lớp Data Hub để có truy xuất và OEE. Không phải làm lại từ đầu.
- **Nhà máy đang xây mới:** thiết kế topic theo cấu trúc ISA-95 ngay từ đầu, tiết kiệm công ánh xạ về sau.
- **Nhiều nhà máy trong tập đoàn:** mỗi site một broker cục bộ, dữ liệu có ngữ cảnh gom về hub chung để so sánh giữa các site.
- **Máy OEM khó can thiệp:** dùng gateway đẩy lên MQTT — xem [ei3](/ei3/) và [gateway Modbus](/gateway-modbus-seneca/).

| Tình huống nhà máy | Vai trò của broker MQTT | Việc Rhize làm thêm |
|---|---|---|
| Đã có UNS chạy ổn định | Giữ nguyên, không đụng tới | Thêm lưu trữ và truy xuất |
| Đang xây UNS mới | Thiết kế topic theo ISA-95 ngay | Ánh xạ thẳng, không phải sửa sau |
| Nhiều nhà máy, mỗi nơi một broker MQTT | Truyền tin cục bộ | Gom dữ liệu có ngữ cảnh về hub chung |
| Máy OEM đẩy dữ liệu qua MQTT | Nhận bản tin từ gateway | Gắn máy vào cây thiết bị |

---

## Lỗi thường gặp khi ghép MQTT với Data Hub

| Vấn đề | Biểu hiện | Cách xử lý |
|---|---|---|
| Payload không có mốc thời gian | Không phân tích được thứ tự | Chuẩn hoá payload có timestamp |
| Publish quá dày từ tag nhiễu | Ngập broker và bus | Đặt deadband tại nguồn |
| Topic đặt tuỳ hứng theo từng line | Không nhân bản được model | Thống nhất quy ước trước khi mở rộng |
| Không có QoS phù hợp | Mất bản tin quan trọng | Chọn QoS theo mức quan trọng dữ liệu |
| Broker không phân quyền | Rủi ro bảo mật | Cấu hình quyền theo topic và client |

---

<a name="bao-gia"></a>
## Nhận tư vấn ghép UNS với Rhize

Gửi cho chúng tôi: **broker MQTT đang dùng · cấu trúc topic hiện tại · số thiết bị đang publish · bài toán cần giải (truy xuất, OEE, báo cáo).**

Chúng tôi đánh giá cấu trúc topic hiện có, đề xuất cách ánh xạ sang mô hình **ISA-95** và kiến trúc kết hợp.

**→ [Liên hệ tư vấn Rhize MQTT & UNS](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Có phải bỏ broker MQTT khi dùng Rhize không?**
Không. Broker giữ nguyên vai trò lớp UNS. **Rhize** đăng ký nhận dữ liệu từ đó và bổ sung phần lưu trữ, ngữ cảnh, truy vấn.

**Chưa có UNS thì bắt buộc phải xây UNS trước không?**
Không. **Rhize Agent** kết nối trực tiếp qua [OPC UA](/rhize-opc-ua/). UNS là một lựa chọn kiến trúc, không phải điều kiện.

**Sparkplug B có cần thiết không?**
Sparkplug bổ sung quy ước về cấu trúc payload và quản lý trạng thái phiên cho MQTT. Hữu ích, nhưng cần kiểm tra khả năng hỗ trợ của bản Rhize và thiết bị đang dùng.

**Dữ liệu trong MQTT có lưu lại được không?**
Broker không phải nơi lưu lịch sử. Việc lưu do [Rhize DB](/rhize-db-graph-database/) đảm nhiệm sau khi dữ liệu được gắn ngữ cảnh.

**Topic đang đặt lộn xộn thì có phải làm lại hết không?**
Không nhất thiết. Có thể ánh xạ topic hiện tại sang model trong giai đoạn đầu, đồng thời thống nhất quy ước mới cho các dây chuyền bổ sung về sau.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-nats-event-streaming/, /rhize-opc-ua/, /rhize-db-graph-database/, /lien-he/. -->
