<!--
LOẠI TRANG : Bài tích hợp (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-opc-ua/
TỪ KHÓA    : opc ua | rhize opc ua | opc ua là gì | kết nối plc opc ua | opc ua sang mqtt | thu thập dữ liệu opc ua | tích hợp opc ua nhà máy
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu khả năng hỗ trợ OPC UA của bản Rhize đang dùng và của từng dòng PLC trước khi cam kết.
-->

TITLE TAG   : Rhize OPC UA – Kết Nối PLC Vào Manufacturing Data Hub
META (149)  : Rhize OPC UA: cách kết nối PLC, SCADA vào Manufacturing Data Hub. Subscription, deadband, bảo mật, xử lý PLC đời cũ và lỗi thường gặp khi triển khai.
H1          : Rhize OPC UA – Kết Nối PLC Vào Data Hub

---

## Vì sao Rhize OPC UA là đường kết nối chuẩn?

<!--IMG:rep-->
![Rhize OPC UA - Kết Nối PLC Vào Data Hub](assets/diagrams/rep-agent.svg)


**OPC UA** (Unified Architecture) là chuẩn truyền thông công nghiệp độc lập nhà cung cấp, thay thế OPC Classic vốn phụ thuộc Windows/DCOM. Đây là giao thức mà **Rhize** dùng phổ biến nhất để lấy dữ liệu từ lớp điều khiển.

Ba lý do khiến **Rhize OPC UA** là lựa chọn mặc định khi PLC hỗ trợ:

- **Có mô hình thông tin**, không chỉ truyền giá trị thô — tag mang theo kiểu dữ liệu, đơn vị, chất lượng và mốc thời gian.
- **Hỗ trợ subscription**: máy chủ chủ động báo khi giá trị đổi, giảm tải so với hỏi liên tục.
- **Bảo mật tích hợp**: mã hoá và xác thực nằm trong chuẩn, không phải thêm ngoài.

Việc kết nối do [Rhize Agent](/rhize-agent-ket-noi/) đảm nhiệm: đăng ký tag, nhận thay đổi và publish lên NATS.

> **Cần kiểm tra PLC hiện có nói được OPC UA không?** Gửi danh sách thiết bị → [Nhận khảo sát](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Rhize OPC UA lấy được những gì từ PLC?

| Loại dữ liệu | Ví dụ | Dùng cho bài toán nào |
|---|---|---|
| **Bộ đếm sản lượng** | Số sản phẩm qua cảm biến đếm | OEE, job response |
| **Trạng thái máy** | Chạy / dừng / chờ / lỗi | Downtime, phân tích dừng máy |
| **Thông số quá trình** | Nhiệt độ, áp suất, tốc độ | Batch record, chất lượng |
| **Mã lỗi, cảnh báo** | Alarm từ PLC | Bảo trì, phân loại nguyên nhân dừng |
| **Thông tin mẻ đang chạy** | Mã sản phẩm, số lệnh | Gắn ngữ cảnh cho mọi sự kiện |
| **Setpoint** | Thông số cài đặt hiện tại | Đối chiếu công thức, ghi vào hồ sơ |

Dòng thứ năm quan trọng hơn vẻ bề ngoài: nếu PLC không cho biết **đang chạy mã sản phẩm nào**, hệ thống phải suy ra từ ERP hoặc thao tác viên nhập — nguồn sai số lớn. Nên kiểm tra sớm xem PLC có công bố thông tin này không.

---

## Subscription và cách giảm tải cho PLC

| Cơ chế | Cách hoạt động | Ưu / nhược |
|---|---|---|
| **Polling** | Client hỏi định kỳ | Đơn giản, nhưng tải cao và dễ bỏ sót |
| **Subscription** | Server báo khi giá trị đổi | Độ trễ thấp, tải thấp — **ưu tiên dùng** |
| **Deadband** | Chỉ báo khi đổi quá ngưỡng | Lọc nhiễu, giảm bản tin vô nghĩa |
| **Sampling interval** | Chu kỳ server lấy mẫu nội bộ | Cân bằng độ chính xác và tải |
| **Publishing interval** | Chu kỳ gửi gói thay đổi | Gộp nhiều thay đổi thành một gói |

Cấu hình sai ba tham số cuối là nguyên nhân phổ biến khiến PLC bị quá tải sau khi lắp hệ thống thu thập. Nguyên tắc: **lấy mẫu dày cho tag quyết định OEE và chất lượng, thưa cho tag chỉ để tham khảo**.

---

## PLC đời cũ không hỗ trợ OPC UA thì làm sao?

| Tình huống | Giải pháp | Lưu ý |
|---|---|---|
| PLC chỉ có **Modbus TCP/RTU** | Gateway Modbus → OPC UA/MQTT | Xem [gateway Modbus](/gateway-modbus-seneca/) |
| PLC dùng **giao thức riêng của hãng** | Driver chuyên dụng hoặc gateway đa giao thức | Kiểm tra bản quyền driver |
| Máy **OEM không được can thiệp** | Nền tảng kết nối máy chuyên biệt | Xem [ei3](/ei3/) |
| Chỉ có **tín hiệu analog 4–20mA** | Bộ chuyển đổi tín hiệu sang Modbus | Xem [bộ chuyển đổi tín hiệu Seneca](/bo-chuyen-doi-tin-hieu-seneca/) |
| Có **SCADA nhưng PLC đóng** | Lấy qua OPC UA của SCADA | Chấp nhận độ trễ cao hơn |

Thực tế ở Việt Nam, phần lớn dây chuyền có tuổi trên 10 năm rơi vào ba dòng đầu. Chi phí gateway ở hiện trường thường nhỏ so với giá trị dữ liệu thu được — nhưng cần khảo sát trước, không giả định.

---

## Bảo mật khi mở kết nối OPC UA

| Rủi ro | Biện pháp |
|---|---|
| Kết nối không mã hoá | Bật security policy, dùng chứng chỉ |
| Tài khoản mặc định | Tạo tài khoản riêng cho Agent, quyền tối thiểu |
| Quyền ghi mở rộng | Chỉ cấp quyền ghi cho tag thật sự cần |
| OT phơi ra mạng IT | Phân vùng VLAN, tường lửa theo chiều |
| Không ghi vết lệnh ghi | Ghi nhật ký mọi thao tác ghi xuống thiết bị |

Nguyên tắc chung: **mặc định chỉ đọc**. Quyền ghi xuống PLC chỉ mở cho những tag đã thống nhất với bộ phận điều khiển, kèm phê duyệt trong workflow — xem [phân quyền trong Rhize](/rhize-keycloak-phan-quyen/).

| Việc cần làm trước khi mở OPC UA | Vì sao |
|---|---|
| Kiểm tra từng PLC có OPC UA server không | Không suy từ tên hãng, phải kiểm từng model |
| Rà soát quy tắc đặt tên tag | Quyết định công ánh xạ vào model ISA-95 |
| Đo tải hiện tại của PLC | Biết còn dư bao nhiêu cho OPC UA |
| Thống nhất chính sách mạng OT–IT | Tránh vướng phê duyệt lúc sắp go-live |
| Đồng bộ NTP toàn hệ thống | Sai giờ làm hỏng mọi phân tích |

---

## Ứng dụng thực tế theo ngành

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thực phẩm – đồ uống:** lấy nhiệt độ thanh trùng và thời gian giữ nhiệt qua OPC UA, ghi thẳng vào hồ sơ lô. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Dược phẩm:** đọc thông số quá trình và setpoint để đối chiếu với công thức phê duyệt. Xem [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Cơ khí, điện tử:** đọc bộ đếm và mã lỗi để tính OEE và phân tích dừng máy. Xem [Rhize và OEE](/rhize-oee/).
- **Xi măng, thép:** ghép dữ liệu năng lượng theo công đoạn với sản lượng.

---

<a name="bao-gia"></a>
## Nhận khảo sát kết nối OPC UA

Gửi cho chúng tôi: **danh sách PLC/SCADA (hãng, model, đời máy) · đã có OPC UA server chưa · danh mục tag cần lấy · sơ đồ mạng OT.**

Chúng tôi khảo sát khả năng kết nối từng máy, đề xuất gateway cho máy chưa hỗ trợ và phương án cấu hình subscription.

**→ [Liên hệ khảo sát kết nối OPC UA](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**OPC UA và OPC Classic khác nhau thế nào?**
**OPC UA** độc lập hệ điều hành, có mô hình thông tin và bảo mật tích hợp; OPC Classic phụ thuộc Windows/DCOM và khó xuyên tường lửa. Hệ thống mới nên dùng OPC UA.

**PLC Mitsubishi, Siemens, Omron có hỗ trợ OPC UA không?**
Các dòng đời mới thường có, dòng cũ thì không — phụ thuộc model và firmware cụ thể. Cần kiểm tra từng máy, không suy từ tên hãng. Xem thêm [phân loại PLC](/phan-loai-plc/).

**Kết nối OPC UA có làm chậm PLC không?**
Có nếu cấu hình sai — lấy mẫu quá dày trên quá nhiều tag. Dùng **subscription** kèm **deadband** và chu kỳ hợp lý thì tải thêm rất nhỏ.

**Có nên lấy dữ liệu qua SCADA thay vì thẳng từ PLC?**
Tuỳ. Qua SCADA đơn giản hơn nhưng độ trễ cao hơn và có thể bỏ sót sự kiện ngắn. Với tag quyết định OEE nên lấy thẳng từ PLC.

**Cần bao lâu để kết nối một dây chuyền?**
Nếu PLC đã có OPC UA và danh mục tag rõ ràng, thường tính bằng ngày. Phần lâu là **chuẩn hoá tên tag** và ánh xạ vào model ISA-95.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-agent-ket-noi/, /rhize-mqtt-uns/, /rhize-tich-hop-scada-historian/, /lien-he/. -->
