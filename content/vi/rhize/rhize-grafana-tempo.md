<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + vận hành
URL SLUG   : /rhize-grafana-tempo/
TỪ KHÓA    : grafana | rhize grafana | rhize tempo | giám sát nền tảng sản xuất | tracing bpmn | observability nhà máy | dashboard Grafana dữ liệu sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Phiên bản Grafana/Tempo theo bản phát hành Rhize; đối chiếu tài liệu trước khi đăng.
-->

TITLE TAG   : Rhize Grafana & Tempo – Giám Sát Và Truy Vết BPMN
META (146)  : Rhize Grafana và Tempo: bảng giám sát nền tảng và tracing tiến trình BPMN. Cách phát hiện workflow chậm, truy vấn nặng và các chỉ số cần theo dõi.
H1          : Rhize Grafana & Tempo – Giám Sát Và Truy Vết

---

## Vì sao Rhize cần Grafana và Tempo?

<!--IMG:rep-->
![Rhize Grafana & Tempo - Giám Sát Và Truy Vết](assets/diagrams/rep-analytics.svg)


Một Manufacturing Data Hub gồm nhiều microservice chạy song song: Agent, Core, BPMN engine, Rhize DB, Router, NATS. Khi hệ thống chậm, câu hỏi "chậm ở đâu" không có câu trả lời hiển nhiên — trừ khi có Grafana và Tempo.

**Rhize Grafana** cung cấp **dashboard Grafana** theo dõi tình trạng nền tảng theo thời gian thực; **Tempo** cung cấp **tracing** — theo dấu một tiến trình đi qua từng dịch vụ và đo thời gian ở mỗi chặng. Nền tảng dùng **Tempo để truy vết tiến trình BPMN**, nghĩa là xem được workflow nào chậm và chậm ở **bước nào**.

Đây không phải phần "làm sau nếu có thời gian". Bật quan sát từ giai đoạn thử nghiệm rẻ hơn nhiều so với đi tìm nguyên nhân khi hệ thống đã chạy thật và đang nghẽn.

> **Cần thiết lập giám sát cho nền tảng dữ liệu?** → [Nhận tư vấn vận hành](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Grafana và Tempo khác nhau ở đâu?

| Tiêu chí | **Grafana** | **Tempo** |
|---|---|---|
| Trả lời câu hỏi | Hệ thống đang thế nào | Vì sao lần chạy này chậm |
| Dữ liệu | Chỉ số theo thời gian | Vết (trace) của từng tiến trình |
| Dùng khi | Theo dõi hằng ngày | Điều tra sự cố cụ thể |
| Ví dụ | Độ trễ trung bình tăng dần | Workflow X mất 8 giây ở bước gọi ERP |
| Ai dùng | Vận hành, IT | Kỹ sư triển khai |

Hai công cụ bổ sung cho nhau: **Grafana** cho biết **có vấn đề**; **Tempo** cho biết **vấn đề ở đâu**.

---

## Những chỉ số nên theo dõi ngay từ đầu

| Nhóm | Chỉ số | Dấu hiệu cần xử lý |
|---|---|---|
| **Thu thập** (Grafana) | Số tag đang subscribe, tần suất publish | Tụt đột ngột = mất kết nối nguồn |
| **Bus sự kiện** (Grafana) | Thông lượng NATS, độ trễ | Tăng liên tục = có dịch vụ tiêu thụ chậm |
| **Cơ sở dữ liệu** | Thời gian truy vấn, dung lượng | Truy vấn chậm dần = cần tối ưu hoặc phân trang |
| **Workflow** | Số tiến trình đang chạy, thời gian trung bình | Dồn ứ = nghẽn ở một bước |
| **API** | Số truy vấn, độ sâu, lỗi | Truy vấn quá sâu = rủi ro quá tải |
| **Hạ tầng** (Grafana) | CPU, RAM, đĩa của cluster | Cạn đĩa = mất dữ liệu |

Chỉ số quan trọng nhưng hay bị bỏ qua là **"số tag đang subscribe"**. Nếu một gateway ở hiện trường mất kết nối, dữ liệu đơn giản là ngừng chảy — không có báo lỗi nào, và đến khi làm báo cáo cuối tháng mới phát hiện thiếu.

---

## Dùng Tempo để gỡ workflow chậm

| Bước | Việc làm | Kết quả thu được |
|---|---|---|
| 1 | Đặt tên rõ ràng cho workflow và task | Trace đọc được |
| 2 | Mở trace của một lần chạy chậm | Thấy timeline từng bước |
| 3 | Xác định bước chiếm nhiều thời gian nhất | Thường là gọi hệ thống ngoài |
| 4 | Kiểm tra bước đó có timeout chưa | Tránh treo tiến trình |
| 5 | Tối ưu hoặc chuyển sang xử lý bất đồng bộ | Giảm thời gian tổng |

Kinh nghiệm phổ biến: bước chậm nhất trong workflow sản xuất thường **không nằm trong Rhize** mà ở hệ thống bên ngoài — ERP phản hồi chậm, LIMS quá tải. Không có trace thì rất dễ đổ lỗi nhầm chỗ. Xem [Rhize BPMN](/rhize-bpmn-workflow/).

---

## Ứng dụng dashboard trong vận hành nhà máy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


Ngoài giám sát kỹ thuật bằng Grafana, **Grafana** còn thường được dùng cho dashboard nghiệp vụ lấy dữ liệu từ Manufacturing Data Hub:

- **Màn hình OEE tại đầu dây chuyền** — cập nhật liên tục cho ca đang chạy. Xem [Rhize và OEE](/rhize-oee/).
- **Bảng theo dõi tiến độ lệnh sản xuất** — so kế hoạch với thực tế. Xem [scheduling](/rhize-scheduling-lap-ke-hoach/).
- **Dashboard năng lượng theo công đoạn** — suất tiêu hao trên đơn vị sản phẩm.
- **Theo dõi thông số quá trình** — cho tổ vận hành và QC.

Điểm mạnh: dữ liệu đã có ngữ cảnh ISA-95, nên một dashboard dựng một lần dùng được cho nhiều dây chuyền.

| Dashboard Grafana | Người xem | Yêu cầu thiết kế |
|---|---|---|
| Sức khoẻ nền tảng trên Grafana | Đội IT | Đủ chi tiết, có cảnh báo |
| OEE tại đầu dây chuyền | Tổ vận hành | Chữ lớn, ít màu, xem từ xa |
| Tiến độ lệnh sản xuất | Kế hoạch, quản đốc | So kế hoạch với thực tế |
| Thông số quá trình | QC, kỹ sư công nghệ | Có ngưỡng và lịch sử |
| Năng lượng theo công đoạn | Ban giám đốc | Tổng hợp theo tháng |

---

## Lưu ý khi thiết lập giám sát

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Grafana chỉ theo dõi hạ tầng, bỏ qua luồng dữ liệu | Máy chủ xanh nhưng dữ liệu không về | Theo dõi cả chỉ số nghiệp vụ |
| Đặt cảnh báo quá nhạy | Nhiễu, nhân viên tắt thông báo | Hiệu chỉnh ngưỡng sau 2–4 tuần dữ liệu thật |
| Không lưu trace đủ lâu | Sự cố xảy ra đêm, sáng không còn vết | Đặt thời gian lưu hợp lý |
| Dashboard Grafana không có người xem | Giám sát vô nghĩa | Gán trách nhiệm theo dõi rõ ràng |
| Bật tracing sau khi lên production | Khó tái hiện sự cố | Bật từ giai đoạn thử nghiệm |

---

<a name="bao-gia"></a>
## Nhận tư vấn giám sát và vận hành Rhize

Gửi cho chúng tôi: **quy mô hệ thống dự kiến · các dashboard nghiệp vụ cần có · yêu cầu cảnh báo · đội ngũ sẽ vận hành.**

Chúng tôi thiết lập bộ chỉ số theo dõi, dashboard vận hành và quy trình xử lý cảnh báo.

**→ [Liên hệ tư vấn giám sát Rhize](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Grafana và Tempo có bắt buộc phải cài không?**
Không bắt buộc để hệ thống chạy, nhưng nên có trước khi lên production. Không có chúng thì mọi sự cố đều phải đoán.

**Có dùng Grafana làm dashboard cho công nhân được không?**
Được, và nhiều nhà máy làm vậy với Grafana. Cần thiết kế đơn giản, chữ lớn, ít màu — màn hình treo ở xưởng khác hẳn dashboard cho kỹ sư.

**Tempo lưu trace bao lâu?**
Tuỳ cấu hình lưu trữ. Nên đủ dài để điều tra sự cố xảy ra ngoài giờ làm việc — tối thiểu vài ngày.

**Đang có hệ thống giám sát riêng thì sao?**
Có thể đẩy chỉ số từ Grafana sang hệ thống giám sát sẵn có của IT. Điểm cần giữ là **tracing tiến trình BPMN**, vì đó là thứ đặc thù của nền tảng.

**Cần bao nhiêu tài nguyên cho giám sát?**
Không lớn so với phần còn lại, nhưng cần tính vào dung lượng lưu trữ. Chi phí này nhỏ hơn nhiều so với thời gian mò sự cố mà không có dữ liệu.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-bpmn-workflow/, /rhize-oee/, /kien-truc-nen-tang-rhize/, /lien-he/. -->
