<!--
LOẠI TRANG : Bài kỹ thuật (pillar danh mục) — Kỹ thuật + giải pháp
URL SLUG   : /kien-truc-nen-tang-rhize/
TỪ KHÓA    : kiến trúc rhize | nền tảng rhize | thành phần rhize | microservice sản xuất | libre core | rhize db
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Tên dịch vụ và phụ thuộc theo tài liệu Rhize; đối chiếu bản phát hành đang dùng trước khi đăng.
-->

TITLE TAG   : Kiến Trúc Rhize – Các Thành Phần Nền Tảng MDH
META (146)  : Kiến trúc Rhize gồm những gì: Rhize DB, Libre Core, BPMN engine, Agent, Admin UI, Apollo Router, NATS, Keycloak. Luồng dữ liệu và yêu cầu hạ tầng.
H1          : Kiến Trúc Rhize – Các Thành Phần Nền Tảng

---

## Kiến trúc Rhize nhìn tổng thể

<!--IMG:rep-->
![Kiến Trúc Rhize - Các Thành Phần Nền Tảng](assets/diagrams/rep-mdh.svg)


**Kiến trúc Rhize** là tập hợp các **microservice ghép lỏng (loosely coupled)**, mỗi dịch vụ làm một việc và giao tiếp qua message bus. Cách tổ chức này không phải để chạy theo mốt: nó là điều kiện để một nhà máy có thể **mở rộng ngang** khi số điểm dữ liệu tăng gấp mười, mà không phải nâng cấp toàn hệ thống.

Toàn bộ kiến trúc Rhize triển khai trên **Kubernetes**, cài từng dịch vụ bằng **Helm**. Dịch vụ cơ sở dữ liệu **libreBaas** phải cài trước, vì các dịch vụ còn lại phụ thuộc vào schema và endpoint mà nó phát hành.

> **Cần đánh giá hạ tầng trước khi triển khai?** Gửi hiện trạng cluster/máy chủ → [Nhận tư vấn kiến trúc Rhize](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Các thành phần chính trong kiến trúc Rhize

| Thành phần | Tên dịch vụ | Vai trò |
|---|---|---|
| **Rhize DB** | libreBaas | Graph database, schema ISA-95, phát hành GraphQL |
| **Libre Core** | libreCore | Dịch vụ lõi: xử lý luật, sinh sự kiện có ngữ cảnh |
| **BPMN engine** | Workflow service | Chạy workflow low-code mô hình hoá trong UI |
| **Libre Agent** | libre-agent | Kết nối nguồn dữ liệu, subscribe tag, publish lên NATS |
| **Admin UI** | libreAdminUI | Quản trị model, người dùng, workflow |
| **Router** | libre router init (Apollo Router) | Cổng GraphQL hợp nhất, một điểm truy cập |

Sáu dịch vụ trên là phần lõi của kiến trúc Rhize. Ngoài ra nền tảng (kiến trúc Rhize) dựa trên một số thành phần mã nguồn mở đã trưởng thành, không viết lại từ đầu.

---

## Các dịch vụ nền tảng trong kiến trúc Rhize

| Dịch vụ | Vai trò trong kiến trúc Rhize | Ghi chú |
|---|---|---|
| **NATS** | Message broker cho sự kiện thời gian thực | Libre Agent publish thay đổi tag lên đây |
| **Keycloak** | Xác thực OIDC, quản lý vai trò | Vai trò libreBaas gắn vào libreAdminGroup |
| **Grafana** | Dashboard, quan sát hệ thống | Bộ Grafana LGTM |
| **Tempo** | Truy vết (tracing) tiến trình BPMN | Dò tìm workflow chạy chậm ở bước nào |
| **Restate** | Nền điều phối dịch vụ | Workflow service phụ thuộc |

Việc dùng các thành phần chuẩn công nghiệp có một hệ quả thực tế cho nhà máy Việt Nam: đội IT nội bộ **không phải học một hệ sinh thái độc quyền**. Kubernetes, Helm, Keycloak, Grafana đều là kỹ năng phổ biến, tuyển được và có tài liệu.

---

## Luồng dữ liệu đi qua kiến trúc Rhize

Đường đi của một giá trị từ hiện trường tới ứng dụng trong kiến trúc Rhize:

1. **PLC/SCADA** cập nhật một tag (ví dụ số sản phẩm đếm được trên Line 3).
2. **Libre Agent** đang subscribe tag đó, phát hiện thay đổi và **publish lên NATS**.
3. **Libre Core** nhận sự kiện, đối chiếu với **luật** đã cấu hình: giá trị này thuộc work unit nào, lệnh sản xuất nào đang chạy, lô vật tư nào đang dùng.
4. Sự kiện đã có ngữ cảnh được **ghi vào Rhize DB** như một nút trong đồ thị, liên kết với thiết bị, vật tư, nhân sự, lệnh sản xuất.
5. Nếu có **workflow BPMN** đăng ký lắng nghe sự kiện này, engine kích hoạt tiến trình — ví dụ gọi API sang ERP để báo sản lượng.
6. Ứng dụng bên ngoài truy vấn qua **GraphQL endpoint** và nhận về dữ liệu đã có đủ quan hệ.

Điểm mấu chốt nằm ở bước 3. Ở kiến trúc truyền thống, việc gắn ngữ cảnh xảy ra **muộn** — lúc làm báo cáo, nhiều tháng sau, khi không ai còn nhớ ca đó chạy gì. Trong **kiến trúc Rhize**, ngữ cảnh được gắn **ngay khi sự kiện xảy ra**.

---

## Vì sao kiến trúc Rhize dùng graph thay vì bảng quan hệ?

| Câu hỏi nghiệp vụ | SQL quan hệ | Graph (Rhize DB) |
|---|---|---|
| Lô này dùng nguyên liệu nào | 2–3 join | 1 bước duyệt |
| Nguyên liệu đó vào những lô nào | Truy vấn ngược, chậm | Duyệt cạnh ngược, nhanh |
| Thiết bị nào từng chạm lô này | Nhiều join qua bảng trung gian | Duyệt đồ thị |
| Đổi cấu trúc dây chuyền | Sửa schema, migrate | Thêm nút và cạnh |
| Truy xuất 5 cấp genealogy | Đệ quy, rất tốn | Tự nhiên với graph |

Truy xuất nguồn gốc về bản chất là **bài toán duyệt đồ thị**. Mô hình quan hệ mô tả được, nhưng phải trả giá bằng join lồng nhau và schema cứng. Với graph, thêm một loại quan hệ mới chỉ là thêm cạnh. Xem [Rhize DB](/rhize-db-graph-database/).

---

## Yêu cầu hạ tầng cho kiến trúc Rhize

| Hạng mục | Yêu cầu | Lưu ý khi triển khai tại Việt Nam |
|---|---|---|
| **Điều phối container** | Kubernetes | On-prem hoặc cloud; cần người vận hành cluster |
| **Cài đặt** | Helm chart theo từng dịch vụ | Cài **libreBaas trước tiên** |
| **Xác thực** | Keycloak / OIDC | Ghép được AD/SSO sẵn có |
| **Mạng OT–IT** | Truy cập OPC UA/MQTT | Tách VLAN, mở cổng theo chính sách |
| **Quan sát** | Grafana + Tempo | Bật tracing ngay từ đầu, đừng để sau |
| **Sao lưu** | Backup graph + time-series | Kiểm thử phục hồi trước khi lên production |

Kinh nghiệm thực tế: phần khiến dự án chậm ở nhà máy Việt Nam thường **không phải Kubernetes** mà là **quy tắc mạng OT–IT**. Nên đưa bộ phận an toàn thông tin vào từ giai đoạn thiết kế, không phải lúc sắp go-live.

---

## Kiến trúc Rhize trong nhà máy có sẵn hệ thống cũ

Rất ít nhà máy khởi động từ con số không, nên kiến trúc Rhize được thiết kế để ghép vào từng phần. Kiến trúc microservice cho phép **Rhize** ghép vào từng phần:

- **Giữ SCADA và historian**, chỉ lấy dữ liệu qua OPC UA — xem [tích hợp SCADA & historian](/rhize-tich-hop-scada-historian/).
- **Giữ ERP**, đồng bộ lệnh sản xuất hai chiều qua OData/REST — xem [tích hợp ERP](/rhize-tich-hop-erp/).
- **Giữ broker MQTT** nếu nhà máy đã có UNS — xem [Rhize với MQTT và UNS](/rhize-mqtt-uns/).
- **Thay dần MES cũ** theo từng phân hệ thay vì thay một lần.

Với nhà máy chưa có lớp thu thập, cần bổ sung phần cứng ở hiện trường trước: [bộ chuyển đổi tín hiệu](/bo-chuyen-doi-tin-hieu-seneca/), gateway Modbus, hoặc [nền tảng IIoT ei3](/ei3/) cho máy khó kết nối.

| Cách ghép kiến trúc Rhize | Phù hợp với nhà máy | Rủi ro |
|---|---|---|
| Bổ sung, giữ nguyên SCADA | Đã đầu tư nhiều, không muốn thay | Thấp — dây chuyền không phụ thuộc |
| Thay dần MES cũ | MES hết hỗ trợ, khó mở rộng | Trung bình, làm theo từng phân hệ |
| Kiến trúc Rhize làm lõi ngay từ đầu | Nhà máy xây mới | Cao hơn, cần đội kỹ thuật mạnh |
| Nhiều site, một model chung | Tập đoàn nhiều nhà máy | Thấp sau khi site đầu chạy ổn |

---

<a name="bao-gia"></a>
## Nhận tư vấn triển khai kiến trúc Rhize

Gửi cho chúng tôi: **hạ tầng hiện có (có Kubernetes chưa) · hệ thống SCADA/historian/ERP · số điểm dữ liệu ước tính · chính sách mạng OT–IT · mục tiêu giai đoạn 1.**

Chúng tôi sẽ đưa sơ đồ kiến trúc Rhize đề xuất, danh sách dịch vụ cần triển khai và ước lượng tài nguyên.

**→ [Liên hệ tư vấn kiến trúc Rhize](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)

## Câu hỏi thường gặp (FAQ)

**Kiến trúc Rhize bắt buộc chạy trên Kubernetes?**
Các dịch vụ trong kiến trúc Rhize được đóng gói và cài qua **Helm** trên Kubernetes. Nhà máy chưa có cluster nên chuẩn bị hạ tầng này trước, hoặc dùng managed Kubernetes trên cloud.

**Cài dịch vụ nào trước?**
**libreBaas (Rhize DB)** cài trước tiên, vì các dịch vụ khác phụ thuộc schema và endpoint của nó. Sau đó tới Core, Agent, BPMN engine, Admin UI và Router.

**Có cần cài đủ cả Grafana, Tempo, Keycloak không?**
Keycloak cần cho xác thực. Grafana và Tempo phục vụ quan sát và truy vết BPMN — bỏ qua được lúc thử nghiệm, nhưng nên có trước khi chạy thật, vì đó là cách duy nhất biết workflow nghẽn ở đâu.

**Một nút trong kiến trúc Rhize hỏng thì hệ thống dừng không?**
Vì các dịch vụ ghép lỏng và chạy trên cluster, phần lớn thành phần có thể chạy nhiều bản sao. Mức sẵn sàng cụ thể phụ thuộc cấu hình cluster và chiến lược lưu trữ.

**Đội IT nhà máy cần kỹ năng gì?**
Kubernetes/Helm cơ bản, hiểu OIDC, đọc được GraphQL. Phần logic nghiệp vụ viết bằng **BPMN low-code** nên không đòi hỏi đội lập trình lớn — xem [BPMN workflow](/rhize-bpmn-workflow/).

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-db-graph-database/, /rhize-bpmn-workflow/, /rhize-tich-hop-scada-historian/, /lien-he/. -->
