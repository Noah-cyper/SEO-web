<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-bpmn-workflow/
TỪ KHÓA    : bpmn | rhize bpmn | workflow sản xuất | bpmn low-code | điều phối quy trình nhà máy | workflow engine | tự động hoá quy trình sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Tên dịch vụ và phụ thuộc (Restate, Tempo) theo tài liệu Rhize; đối chiếu bản phát hành.
-->

TITLE TAG   : Rhize BPMN – Workflow Low-Code Điều Phối Nhà Máy
META (155)  : Rhize BPMN workflow engine: mô hình hoá quy trình sản xuất bằng BPMN low-code, gọi API, biến đổi JSON, điều phối ERP–MES–thiết bị. Cách dùng và lỗi thường gặp.
H1          : Rhize BPMN – Workflow Low-Code Cho Nhà Máy

---

## Rhize BPMN workflow engine là gì?

<!--IMG:rep-->
![Rhize BPMN - Workflow Low-Code Cho Nhà Máy](assets/diagrams/rep-workflow.svg)


**Rhize BPMN** là engine chạy các **workflow low-code** được vẽ trong giao diện Workflow UI theo chuẩn **BPMN 2.0** — ngôn ngữ mô hình hoá quy trình nghiệp vụ đã dùng phổ biến trong ngành phần mềm doanh nghiệp.

Điểm khác biệt của BPMN: thay vì viết code tích hợp rải rác giữa các hệ thống, kỹ sư **vẽ quy trình** — sự kiện nào kích hoạt, gọi hệ thống nào, rẽ nhánh theo điều kiện gì, ghi kết quả về đâu. Logic nghiệp vụ nằm ở một chỗ, đọc được bằng sơ đồ, và người vận hành hiểu được mà không cần đọc mã nguồn.

Việc xử lý phần lớn chỉ cần **gọi API và biến đổi JSON**. Dịch vụ Workflow phụ thuộc **libreBaas**, **Restate** (nền điều phối) và **Tempo** (truy vết tiến trình).

> **Cần tự động hoá một quy trình đang làm thủ công?** Mô tả quy trình → [Nhận tư vấn workflow](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-bpmn.svg)


---

## Rhize BPMN dùng để điều phối những gì?

| Kịch bản | Kích hoạt bởi | Workflow làm gì |
|---|---|---|
| **Bắt đầu lệnh sản xuất** | ERP đẩy lệnh xuống | Kiểm nguyên liệu, đặt thông số máy, ghi job order |
| **Đổi lô nguyên liệu** | Thao tác viên quét mã | Xác thực lô, cập nhật genealogy, cảnh báo nếu sai |
| **Thông số vượt ngưỡng** | Sự kiện từ Rhize Core | Ghi sự kiện chất lượng, thông báo QC, giữ lô |
| **Kết thúc mẻ** | Sự kiện hoàn thành | Tổng hợp job response, đẩy kết quả sang ERP |
| **Yêu cầu bảo trì** | Sự kiện dừng máy lặp lại | Tạo phiếu trong hệ thống CMMS |
| **Xuất hồ sơ lô** | Yêu cầu từ QA | Gom dữ liệu, sinh báo cáo, ghi vết phê duyệt |

Điểm chung: tất cả đều là những việc mà nhà máy đang làm bằng **email, Excel và điện thoại**. Đưa vào workflow không chỉ nhanh hơn — quan trọng hơn là **để lại vết** cho kiểm toán.

---

## Các thành phần của một workflow BPMN

| Phần tử BPMN 2.0 | Ý nghĩa | Ví dụ trong sản xuất |
|---|---|---|
| **Start event** | Điểm khởi động | Sự kiện dừng máy từ Rhize Core |
| **Task / service task** | Một bước xử lý | Gọi API ERP, ghi dữ liệu vào Rhize DB |
| **Gateway** | Rẽ nhánh theo điều kiện | Nếu dừng > 10 phút thì tạo phiếu bảo trì |
| **Timer event** | Chờ theo thời gian | Nhắc nếu quá 30 phút chưa xử lý |
| **User task** | Bước cần người | Tổ trưởng xác nhận lý do dừng |
| **End event** | Kết thúc tiến trình | Ghi kết quả, đóng sự kiện |

Người từng dùng BPMN ở hệ thống ERP sẽ thấy quen ngay. Với kỹ sư tự động hoá chưa gặp BPMN, cách hiểu đơn giản: đây là **lưu đồ có thể chạy được** — vẽ xong là chạy, không phải viết lại bằng ngôn ngữ khác.

---

## So sánh Rhize BPMN với các cách tự động hoá khác

| Tiêu chí | Script tích hợp | Logic viết trong PLC | Chức năng có sẵn của MES | **Rhize BPMN** |
|---|---|---|---|---|
| Ai đọc hiểu được | Lập trình viên | Kỹ sư điều khiển | Người dùng hệ thống đó | **Sơ đồ, ai cũng đọc** |
| Sửa nhanh không | Cần triển khai lại | Phải dừng máy | Tuỳ nhà cung cấp | **Sửa trên UI** |
| Gọi hệ thống ngoài | Có | Rất hạn chế | Tuỳ | **Có, qua API** |
| Chờ người phê duyệt | Tự cài đặt | Không | Có | **Có (user task)** |
| Truy vết khi lỗi | Log rời rạc | Khó | Tuỳ | **Tracing với Tempo** |
| Ghi vết cho kiểm toán | Tự làm | Không | Có | **Có sẵn** |

Đặc biệt lưu ý dòng thứ hai: đưa logic nghiệp vụ vào PLC là cách làm phổ biến ở Việt Nam, nhưng mỗi lần đổi quy tắc lại phải **dừng dây chuyền**. Chuyển phần logic nghiệp vụ lên workflow giữ PLC chỉ làm đúng việc điều khiển.

---

## Ứng dụng Rhize BPMN trong nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thực phẩm:** workflow kiểm tra lô nguyên liệu còn hạn trước khi cho phép bắt đầu mẻ — chặn lỗi tại nguồn thay vì phát hiện khi đã đóng gói.
- **Dược:** chuỗi phê duyệt điện tử với user task và ghi vết đầy đủ, phục vụ hồ sơ lô. Xem [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Cơ khí, điện tử:** tự động tạo phiếu bảo trì khi cùng một máy dừng quá số lần trong ca.
- **Đa nhà máy:** cùng một workflow triển khai cho nhiều site vì model dữ liệu đã chuẩn hoá theo [ISA-95](/rhize-isa-95/).

---

## Lỗi thường gặp khi xây workflow và cách xử lý

| Vấn đề | Biểu hiện | Cách xử lý |
|---|---|---|
| Workflow chạy chậm | Tiến trình dồn ứ | Bật **Tempo**, tìm task nghẽn — xem [Grafana & Tempo](/rhize-grafana-tempo/) |
| Gọi hệ thống ngoài lỗi | Tiến trình treo | Đặt timeout và nhánh xử lý lỗi rõ ràng |
| Quy trình vẽ quá phức tạp | Không ai bảo trì nổi | Tách thành nhiều workflow nhỏ, gọi lồng nhau |
| Thiếu bước xác nhận người | Tự động hoá sai không ai biết | Thêm user task ở điểm rủi ro cao |
| Không có phiên bản | Sửa xong không quay lại được | Quản lý phiên bản workflow, ghi nhật ký thay đổi |

| Trước khi vẽ workflow BPMN | Cần trả lời |
|---|---|
| Sự kiện nào kích hoạt | Từ Rhize Core, từ người, hay theo lịch |
| Hệ thống nào bị gọi | ERP, LIMS, CMMS — có API không |
| Bước nào cần người duyệt | Đặt user task đúng chỗ rủi ro cao |
| Lỗi thì đi nhánh nào | Timeout và nhánh xử lý lỗi bắt buộc có |
| Ai bảo trì workflow về sau | Tránh phụ thuộc một người |

---

<a name="bao-gia"></a>
## Nhận tư vấn xây workflow BPMN

Gửi cho chúng tôi: **mô tả quy trình đang làm thủ công · các hệ thống cần gọi (ERP, LIMS, CMMS) · điểm cần người phê duyệt · yêu cầu ghi vết.**

Chúng tôi sẽ phác sơ đồ **BPMN**, chỉ rõ bước nào tự động được và bước nào nên giữ con người trong vòng lặp.

**→ [Liên hệ tư vấn Rhize BPMN](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize BPMN có thay được lập trình tích hợp không?**
Phần lớn công việc tích hợp trong nhà máy là **gọi API và biến đổi JSON** — những việc này làm được bằng workflow low-code. Trường hợp đặc thù vẫn cần code, nhưng gọi từ trong workflow.

**Người vận hành có tự vẽ workflow được không?**
Vẽ sơ đồ thì được; phần cấu hình gọi API và ánh xạ dữ liệu thường cần kỹ sư. Thực tế tốt nhất là vận hành mô tả quy trình, kỹ sư hiện thực hoá, rồi cùng rà lại trên sơ đồ.

**Workflow có chạy được khi mất mạng ra ngoài không?**
Các bước nội bộ vẫn chạy; bước gọi hệ thống bên ngoài sẽ chờ hoặc rẽ sang nhánh lỗi tuỳ cấu hình. Nên thiết kế nhánh dự phòng ngay từ đầu.

**BPMN có phải chuẩn riêng của Rhize không?**
Không. **BPMN 2.0** là chuẩn mở, dùng rộng rãi ngoài ngành sản xuất. Kỹ năng này chuyển giao được và tuyển được người biết sẵn.

**Làm sao biết workflow nào đang chạy chậm?**
Nền tảng dùng **Tempo** để truy vết tiến trình BPMN — xem được từng bước mất bao lâu, thay vì đoán.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-core/, /rhize-grafana-tempo/, /rhize-batch-record-dien-tu/, /lien-he/. -->
