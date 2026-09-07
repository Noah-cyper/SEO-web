<!--
LOẠI TRANG : Bài kỹ thuật (satellite) — Kỹ thuật + vận hành
URL SLUG   : /rhize-trien-khai-kubernetes/
TỪ KHÓA    : kubernetes | triển khai rhize | rhize kubernetes | cài đặt rhize helm | hạ tầng data hub | on-premise hay cloud | vận hành nền tảng sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Thứ tự cài đặt và phụ thuộc theo tài liệu Rhize; đối chiếu bản phát hành cụ thể trước khi triển khai.
-->

TITLE TAG   : Triển Khai Rhize Trên Kubernetes – Hạ Tầng Và Lộ Trình
META (150)  : Triển khai Rhize trên Kubernetes bằng Helm: thứ tự cài dịch vụ, yêu cầu hạ tầng, on-premise hay cloud, mạng OT–IT, sao lưu và lộ trình theo giai đoạn.
H1          : Triển Khai Rhize Trên Kubernetes – Hạ Tầng

---

## Triển khai Rhize trên Kubernetes cần hạ tầng gì?

<!--IMG:rep-->
![Triển Khai Rhize Trên Kubernetes - Hạ Tầng](assets/diagrams/rep-platform.svg)


Nền tảng **Rhize** gồm nhiều microservice, đóng gói và cài qua **Helm** trên **Kubernetes**. Đây là điểm cần làm rõ sớm với bộ phận IT của nhà máy, vì nó quyết định phần chuẩn bị hạ tầng Kubernetes.

| Hạng mục | Yêu cầu | Ghi chú |
|---|---|---|
| **Cluster Kubernetes** | Kubernetes (on-prem hoặc cloud) | Cần người vận hành cluster Kubernetes |
| **Cài đặt** | Helm chart theo từng dịch vụ | **libreBaas cài trước tiên** |
| **Xác thực** | Keycloak / OIDC | Ghép SSO/AD sẵn có |
| **Lưu trữ** | Bền vững cho graph + time-series | Tính theo số tag và thời gian lưu |
| **Quan sát** | Grafana + Tempo | Bật từ giai đoạn thử nghiệm |
| **Mạng** | Truy cập lớp OT (OPC UA/MQTT) | Theo chính sách phân vùng |

Nhà máy chưa có Kubernetes có hai lựa chọn: dựng cluster Kubernetes tại chỗ, hoặc dùng managed Kubernetes trên cloud. Lựa chọn phụ thuộc chính sách dữ liệu và năng lực đội IT hơn là kỹ thuật thuần tuý.

> **Cần đánh giá hạ tầng Kubernetes trước khi triển khai?** → [Nhận khảo sát hạ tầng Kubernetes](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Thứ tự cài đặt các dịch vụ

| Thứ tự | Dịch vụ | Vì sao ở vị trí này |
|---|---|---|
| 1 | **libreBaas (Rhize DB)** | Các dịch vụ khác phụ thuộc schema và endpoint |
| 2 | **Keycloak** | Xác thực cho toàn hệ thống |
| 3 | **NATS** | Bus sự kiện giữa các dịch vụ |
| 4 | **Libre Core** | Xử lý luật, sinh sự kiện có ngữ cảnh |
| 5 | **Workflow (BPMN engine)** | Cần libreBaas, Restate, Tempo |
| 6 | **Libre Agent** | Kết nối nguồn dữ liệu |
| 7 | **Router, Admin UI** | Cổng truy cập và giao diện quản trị |

Thứ tự trên là hướng dẫn chung; chi tiết phụ thuộc bản phát hành cụ thể. Điểm cố định cần nhớ: **libreBaas luôn cài đầu tiên**. Xem [kiến trúc nền tảng Rhize](/kien-truc-nen-tang-rhize/).

---

## On-premise hay cloud?

| Tiêu chí | On-premise | Cloud |
|---|---|---|
| Dữ liệu ra khỏi nhà máy | Không | Có, cần chính sách |
| Độ trễ tới lớp OT | Thấp | Phụ thuộc đường truyền |
| Năng lực IT cần có | Cao hơn | Thấp hơn |
| Chi phí ban đầu | Cao hơn | Thấp hơn |
| Chạy khi mất Internet | **Vẫn chạy** | Gián đoạn |
| Mở rộng nhanh | Chậm hơn | Nhanh |

Dòng "chạy khi mất Internet" thường quyết định với nhà máy Việt Nam. Nếu Data Hub tham gia vào việc **chặn lỗi trước khi chạy mẻ**, mất kết nối nghĩa là dừng sản xuất — rủi ro này phải được cân nhắc, hoặc thiết kế phương án dự phòng rõ ràng.

Mô hình lai cũng phổ biến: dịch vụ lõi đặt tại nhà máy, phần phân tích và tổng hợp nhiều site đặt trên cloud.

---

## Chuẩn bị mạng OT–IT

| Việc cần làm | Lý do | Ai tham gia |
|---|---|---|
| Xác định vùng đặt Libre Agent | Cần nhìn thấy lớp OT | IT + tự động hoá |
| Mở cổng theo chiều cần thiết | Giảm bề mặt tấn công | An toàn thông tin |
| Đồng bộ NTP toàn hệ thống | Sai giờ làm hỏng mọi phân tích | IT |
| Quy định quyền ghi xuống thiết bị | Rủi ro vận hành | Tự động hoá + sản xuất |
| Kiểm thử tải lên PLC | Tránh ảnh hưởng dây chuyền | Tự động hoá |

Kinh nghiệm thực tế: phần khiến dự án chậm ở nhà máy Việt Nam thường **không phải Kubernetes** mà là **thoả thuận về mạng OT–IT**. Đưa bộ phận an toàn thông tin vào từ giai đoạn thiết kế tiết kiệm nhiều tuần so với xin phê duyệt lúc sắp go-live.

---

## Lộ trình triển khai theo giai đoạn

| Giai đoạn | Nội dung | Tiêu chí hoàn thành |
|---|---|---|
| **0. Khảo sát** | Hạ tầng, nguồn dữ liệu, bài toán | Có sơ đồ kiến trúc và phạm vi |
| **1. Dựng nền** | Cluster Kubernetes, cài dịch vụ, xác thực | Hệ thống chạy, quan sát được |
| **2. Mô hình hoá** | Cây thiết bị, vật tư, công thức | Model phản ánh đúng một dây chuyền |
| **3. Kết nối** | Agent, tag, kiểm chứng dữ liệu | Dữ liệu về đúng và đủ |
| **4. Ứng dụng đầu tiên** | Thường là OEE | Có số liệu tin được |
| **5. Mở rộng** | Workflow, bài toán tiếp theo | Nhân rộng dây chuyền |

Nguyên tắc: **không mở rộng khi giai đoạn trước chưa chạy ổn định**. Nhà máy nhân rộng sớm thường phải quay lại sửa model cho tất cả dây chuyền cùng lúc — tốn hơn nhiều so với làm chắc một chỗ.

---

## Vận hành sau khi go-live

| Hạng mục | Việc cần làm định kỳ |
|---|---|
| **Sao lưu** | Backup **và kiểm thử phục hồi**, không chỉ chạy backup |
| **Cập nhật phiên bản** | Đọc ghi chú phát hành, thử trên môi trường test trước |
| **Rà soát quyền** | Thu hồi quyền của người đã nghỉ, nhà thầu đã hết dự án |
| **Theo dõi chỉ số** | Độ trễ, thông lượng, dung lượng — xem [Grafana & Tempo](/rhize-grafana-tempo/) |
| **Cập nhật model** | Khi dây chuyền thay đổi, model phải đổi theo |

Dòng cuối là nguyên nhân phổ biến khiến hệ thống mất giá trị sau 1–2 năm: nhà máy thay máy, đổi công đoạn, nhưng model không được cập nhật, và số liệu dần lệch khỏi thực tế.

---

<a name="bao-gia"></a>
## Nhận khảo sát hạ tầng Kubernetes cho Rhize

Gửi cho chúng tôi: **hạ tầng máy chủ hiện có · đã có Kubernetes chưa · chính sách dữ liệu (on-prem/cloud) · sơ đồ mạng OT–IT · số điểm dữ liệu ước tính · đội ngũ IT sẵn có.**

Chúng tôi đưa ra kiến trúc đề xuất, ước lượng tài nguyên và lộ trình triển khai theo giai đoạn.

**→ [Liên hệ khảo sát triển khai Rhize](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)

## Câu hỏi thường gặp (FAQ)

**Không có Kubernetes thì triển khai được không?**
Cần chuẩn bị hạ tầng Kubernetes trước, hoặc dùng managed Kubernetes trên cloud. Đây là yêu cầu của cách nền tảng được đóng gói.

**Đội IT nhà máy cần kỹ năng gì?**
Kubernetes/Helm cơ bản, hiểu OIDC, biết đọc GraphQL và theo dõi Grafana. Không cần đội lập trình lớn vì logic nghiệp vụ viết bằng [BPMN low-code](/rhize-bpmn-workflow/).

**Triển khai một dây chuyền mất bao lâu?**
Phần cài đặt trên Kubernetes tính bằng ngày. Tổng thời gian tới lúc có số liệu tin được thường tính bằng tháng, phần lớn dành cho **mô hình hoá và kiểm chứng dữ liệu**.

**Cần bao nhiêu tài nguyên máy chủ?**
Phụ thuộc số tag, tần suất và thời gian lưu. Cần ước lượng theo số liệu thật của nhà máy thay vì áp con số chung.

**Nâng cấp phiên bản có rủi ro không?**
Như mọi hệ thống sản xuất: đọc ghi chú phát hành, thử trên môi trường test, có kế hoạch quay lui. Không nâng cấp trực tiếp trên production.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-db-graph-database/, /rhize-grafana-tempo/, /lien-he/. -->
