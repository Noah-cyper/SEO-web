<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật
URL SLUG   : /rhize-nats-event-streaming/
TỪ KHÓA    : nats | rhize nats | nats message broker | event streaming sản xuất | luồng sự kiện nhà máy | pub sub công nghiệp | truyền sự kiện thời gian thực
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Phiên bản NATS thay đổi theo bản phát hành Rhize; đối chiếu tài liệu trước khi đăng.
-->

TITLE TAG   : Rhize NATS – Bus Sự Kiện Thời Gian Thực Nhà Máy
META (150)  : Rhize NATS là message broker truyền sự kiện giữa Agent, Core và BPMN engine. Vai trò trong kiến trúc hướng sự kiện, so sánh với MQTT và Kafka, lưu ý triển khai.
H1          : Rhize NATS – Bus Sự Kiện Thời Gian Thực

---

## Rhize NATS đóng vai trò gì?

<!--IMG:rep-->
![Rhize NATS - Bus Sự Kiện Thời Gian Thực](assets/diagrams/rep-nats.svg)


**NATS** là **message broker** mà nền tảng **Rhize** dùng làm đường truyền sự kiện nội bộ. Mọi thay đổi dữ liệu từ hiện trường đi qua đây trước khi tới các dịch vụ xử lý.

Vai trò của **NATS** trong nền tảng không phải lưu trữ mà là **tách rời (decouple)**: **Libre Agent** publish sự kiện lên bus mà không cần biết ai sẽ dùng; **Libre Core**, **BPMN engine** hay bất kỳ dịch vụ nào khác đăng ký nhận phần mình quan tâm. Thêm một dịch vụ tiêu thụ mới không phải sửa gì ở phía phát.

Đây chính là điều làm nên chữ **hướng sự kiện (event-driven)** trong Manufacturing Data Hub — khác hẳn kiến trúc hỏi–đáp (request–response) truyền thống, nơi mỗi hệ thống phải chủ động đi hỏi hệ thống khác.

> **Đang thiết kế kiến trúc dữ liệu hướng sự kiện?** → [Nhận tư vấn kiến trúc](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


| Đặc điểm | Vì sao quan trọng với nhà máy |
|---|---|
| Độ trễ rất thấp | Bắt được cả những lần dừng máy vài chục giây |
| Tách rời bên phát và bên nhận | Thêm hệ thống mới không phải sửa cấu hình Agent |
| Nhẹ, dễ vận hành | Không cần đội chuyên trách như hệ thống log lớn |
| Chạy trên cluster | Mở rộng ngang khi số điểm dữ liệu tăng |

---

## Luồng sự kiện đi qua Rhize NATS

| Bước | Dịch vụ | Việc thực hiện |
|---|---|---|
| 1 | **Libre Agent** | Phát hiện tag đổi giá trị, publish lên NATS |
| 2 | **NATS** | NATS định tuyến bản tin tới các bên đăng ký |
| 3 | **Libre Core** | Nhận, gắn ngữ cảnh ISA-95, ghi vào Rhize DB |
| 4 | **BPMN engine** | Nhận sự kiện đã có ngữ cảnh, kích hoạt workflow |
| 5 | Dịch vụ khác | Đăng ký thêm mà không ảnh hưởng bên phát |

Bước 5 là giá trị dài hạn của kiến trúc NATS. Khi nhà máy muốn thêm một hệ thống mới — ví dụ dashboard năng lượng — hệ thống đó chỉ cần đăng ký luồng sự kiện, không phải mở thêm kết nối tới PLC hay sửa cấu hình Agent.

---

## Vì sao dùng NATS thay vì chỉ dùng MQTT?

| Tiêu chí | MQTT | Kafka | **NATS trong Rhize** |
|---|---|---|---|
| Thiết kế cho | Thiết bị, băng thông hẹp | Log sự kiện khối lượng lớn | **Nhắn tin giữa dịch vụ** |
| Độ trễ | Thấp | Trung bình | **Rất thấp** |
| Vận hành | Đơn giản | Nặng, cần đội chuyên | **Nhẹ** |
| Vai trò điển hình | Lớp thiết bị / UNS | Kho sự kiện dài hạn | **Bus nội bộ nền tảng** |
| Quan hệ với Rhize | Nguồn dữ liệu vào | Có thể ghép ở tầng phân tích | **Thành phần lõi** |

Cần phân biệt rõ: **MQTT và NATS không loại trừ nhau**. Nhà máy đã có UNS trên MQTT vẫn giữ nguyên broker đó làm nguồn dữ liệu; **NATS** làm việc khác — truyền sự kiện **giữa các dịch vụ của nền tảng**. Xem [Rhize với MQTT và UNS](/rhize-mqtt-uns/).

---

## Ứng dụng luồng sự kiện trong nhà máy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


| Bài toán | Vì sao cần luồng sự kiện độ trễ thấp |
|---|---|
| **Cảnh báo chất lượng** | Phát hiện lệch thông số trong lúc chạy, không phải sau mẻ |
| **Đếm downtime chính xác** | Bắt được cả những lần dừng vài chục giây |
| **Dashboard tại xưởng** | Cập nhật liên tục thay vì làm mới theo phút |
| **Kích hoạt workflow** | Quy trình chạy ngay khi sự kiện xảy ra |
| **Nạp dữ liệu cho AI** | Suy luận theo thời gian thực, không chỉ theo lô |

Xem thêm [Rhize và OEE](/rhize-oee/), [quản lý chất lượng](/rhize-quan-ly-chat-luong/), [AI/ML trên dữ liệu Rhize](/rhize-ai-ml-du-lieu-san-xuat/).

---

## Lưu ý khi vận hành Rhize NATS

| Vấn đề | Rủi ro | Cách xử lý |
|---|---|---|
| Publish quá dày từ tag nhiễu | Ngập bus, tốn tài nguyên | Đặt deadband/lọc ngay ở Agent |
| Không đồng bộ thời gian | Sự kiện lệch thứ tự | Bắt buộc NTP toàn hệ thống |
| Thiếu giám sát bus | Mất sự kiện mà không biết | Theo dõi bằng Grafana — xem [Grafana & Tempo](/rhize-grafana-tempo/) |
| Một dịch vụ tiêu thụ chậm | Dồn ứ lan sang dịch vụ khác | Tách luồng, mở rộng dịch vụ chậm |
| Không phân quyền chủ đề | Rủi ro truy cập chéo | Cấu hình quyền theo dịch vụ |

Dòng đầu tiên hay gặp nhất: một cảm biến rung nhẹ khiến tag đổi giá trị liên tục, sinh hàng nghìn bản tin mỗi phút mà không mang thông tin gì. Đặt **deadband** ngay tại Agent, trước khi bản tin vào NATS, giải quyết gọn.

---

<a name="bao-gia"></a>
## Nhận tư vấn kiến trúc hướng sự kiện

Gửi cho chúng tôi: **số tag và tần suất thay đổi ước tính · các hệ thống cần nhận sự kiện · yêu cầu độ trễ · hạ tầng cluster hiện có.**

Chúng tôi sẽ đề xuất cách tổ chức luồng sự kiện, chính sách lọc và cấu hình tài nguyên phù hợp.

**→ [Liên hệ tư vấn kiến trúc sự kiện](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize NATS có thay thế broker MQTT của nhà máy không?**
Không. Broker MQTT phục vụ lớp thiết bị/UNS; **NATS** là bus nội bộ giữa các dịch vụ Rhize. Hai lớp này tồn tại song song.

**Sự kiện có được lưu lại không?**
Bus làm nhiệm vụ truyền. Việc lưu trữ lâu dài do **Rhize DB** đảm nhiệm sau khi sự kiện đã được gắn ngữ cảnh.

**Nếu một dịch vụ tạm dừng thì sự kiện có mất không?**
Tuỳ cấu hình bền vững của bus và thiết kế xử lý lại. Với dữ liệu quan trọng cho tuân thủ, cần thiết kế cơ chế đảm bảo không mất ngay từ đầu.

**Mở rộng khi nhà máy tăng gấp nhiều lần số tag thì sao?**
Nền tảng chạy trên Kubernetes và mở rộng ngang. Cần thử tải trước với số tag mục tiêu để xác định cấu hình cluster.

**Đội IT cần biết gì về NATS?**
Đủ để giám sát và xử lý sự cố cơ bản: theo dõi thông lượng, độ trễ, dịch vụ tiêu thụ chậm. Phần lớn công việc hằng ngày nằm ở tầng model và workflow, không ở bus.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-agent-ket-noi/, /rhize-mqtt-uns/, /lien-he/. -->
