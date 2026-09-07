<!--
LOẠI TRANG : Bài tích hợp (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-tich-hop-erp/
TỪ KHÓA    : tích hợp erp | rhize tích hợp erp | kết nối erp mes | tích hợp sap sản xuất | odata erp | đồng bộ lệnh sản xuất | erp nhà máy
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Chi tiết giao diện với từng ERP phụ thuộc phiên bản và module; cần khảo sát trước khi cam kết.
-->

TITLE TAG   : Rhize Tích Hợp ERP – Đồng Bộ Lệnh Và Kết Quả SX
META (146)  : Rhize tích hợp ERP: đồng bộ lệnh sản xuất, vật tư và kết quả giữa ERP và nhà xưởng qua OData, REST và workflow BPMN. Luồng dữ liệu và lỗi hay gặp.
H1          : Rhize Tích Hợp ERP – Nối Văn Phòng Với Nhà Xưởng

---

## Bài toán tích hợp ERP với nhà xưởng ở nhà máy Việt Nam

<!--IMG:rep-->
![Rhize Tích Hợp ERP - Nối Văn Phòng Với Nhà Xưởng](assets/diagrams/rep-app.svg)


Ở phần lớn nhà máy Việt Nam, ERP và nhà xưởng nối với nhau bằng **con người**: kế hoạch in ra giấy đưa xuống line, cuối ca ghi sản lượng vào sổ, hôm sau nhập lại vào ERP. Hệ quả là ERP luôn nhìn thấy một nhà máy của **ngày hôm qua**.

**Rhize tích hợp ERP** giải bài toán này bằng cách đứng giữa hai bên: nhận lệnh sản xuất từ ERP, chia xuống đúng work center theo mô hình **ISA-95**, thu thập kết quả thực tế từ thiết bị, rồi trả kết quả đã được xác nhận ngược lên ERP.

Điểm khác biệt của cách tích hợp ERP này so với tích hợp point-to-point: dữ liệu không chảy thẳng từ PLC lên ERP mà đi qua lớp **có ngữ cảnh**, nên con số trả về ERP là con số đã gắn với lệnh sản xuất, lô vật tư và ca cụ thể.

> **Cần nối ERP với dữ liệu sản xuất thời gian thực?** → [Nhận tư vấn tích hợp ERP](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Luồng dữ liệu hai chiều giữa ERP và Rhize khi tích hợp ERP

| Chiều | Dữ liệu | Tần suất điển hình | Đối tượng ISA-95 |
|---|---|---|---|
| ERP → Rhize | Lệnh sản xuất, số lượng, hạn giao | Theo kế hoạch | **Operations schedule** |
| ERP → Rhize | Danh mục vật tư, BOM, công thức | Khi thay đổi | **Operations definition** |
| ERP → Rhize | Lô nguyên liệu đã nhập kho | Khi nhập | **Material lot** |
| Rhize → ERP | Sản lượng thực tế, phế phẩm | Thời gian thực / theo ca | **Job response** |
| Rhize → ERP | Tiêu hao nguyên liệu thực tế | Khi kết thúc mẻ | **Material actual** |
| Rhize → ERP | Thời gian chạy máy, nhân công | Theo ca | **Operations performance** |

Hai dòng cuối là phần mà ERP thường thiếu chính xác nhất, vì trước đây phải nhập tay. Khi lấy tự động từ thiết bị, chênh lệch giữa tiêu hao lý thuyết theo BOM và tiêu hao thực tế lộ ra ngay — và thường là phát hiện có giá trị nhất trong năm đầu triển khai.

---

## Cách Rhize kết nối với ERP khi tích hợp ERP

| Phương thức | Khi nào dùng | Ghi chú |
|---|---|---|
| **OData** | ERP hỗ trợ OData (SAP và nhiều hệ khác) | Chuẩn truy vấn dữ liệu qua HTTP |
| **REST API** | ERP có API mở | Phổ biến với ERP hiện đại |
| **File trung gian** | ERP cũ, không có API | CSV/XML theo lịch — phương án cuối |
| **B2MML** | Trao đổi theo chuẩn ISA-95 | Xem [Rhize và B2MML](/rhize-b2mml/) |
| **Cơ sở dữ liệu trung gian** | ERP đóng | Rủi ro, cần thoả thuận với nhà cung cấp ERP |

Phần điều phối do **workflow BPMN** đảm nhiệm: gọi API, biến đổi JSON, xử lý lỗi, thử lại khi ERP bận. Đây chính là loại việc mà [Rhize BPMN](/rhize-bpmn-workflow/) sinh ra để làm, thay vì viết script tích hợp ERP riêng.

---

## So sánh các cách nối ERP với nhà xưởng (tích hợp ERP)

| Tiêu chí | Nhập tay | Tích hợp point-to-point | **Qua Rhize Data Hub** |
|---|---|---|---|
| Độ trễ dữ liệu | 1 ngày trở lên | Theo lịch chạy | **Gần thời gian thực** |
| Sai sót | Cao | Trung bình | **Thấp** |
| Ngữ cảnh dữ liệu | Mất phần lớn | Hạn chế | **Đầy đủ ISA-95** |
| Thêm dây chuyền mới | Thêm người | Viết lại tích hợp ERP | **Nhân bản model** |
| Đổi ERP | Không ảnh hưởng | Làm lại toàn bộ | **Chỉ đổi lớp giao tiếp** |
| Truy vết khi lệch số | Rất khó | Khó | **Có vết đầy đủ** |

Dòng thứ năm đáng lưu ý với nhà máy đang cân nhắc đổi ERP: nếu tích hợp ERP nối thẳng từ thiết bị lên ERP, đổi ERP nghĩa là làm lại tất cả. Với kiến trúc hub, chỉ lớp giao tiếp với ERP phải thay.

| Câu hỏi trước khi tích hợp ERP | Vì sao phải chốt sớm |
|---|---|
| "Sản lượng" ở hai bên định nghĩa thế nào | Hai con số không bao giờ bằng nhau |
| Mã vật tư xưởng và ERP có khớp không | Quyết định khối lượng ánh xạ |
| ERP chịu được bao nhiêu giao dịch mỗi giờ | Tránh làm quá tải khi tích hợp ERP realtime |
| Ai sở hữu từng nhóm dữ liệu | Tránh tranh cãi khi số liệu lệch |
| Có kế hoạch đổi ERP không | Ảnh hưởng cách thiết kế lớp giao tiếp |

---

## Ứng dụng theo ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thực phẩm:** ERP đẩy kế hoạch tuần, Rhize chia xuống từng ca và trả về sản lượng theo lô. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Dược:** ERP giữ lệnh và vật tư, Rhize giữ hồ sơ lô điện tử; hai bên đồng bộ trạng thái lô. Xem [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Cơ khí, điện tử:** ghi nhận thời gian máy và nhân công thực tế để tính giá thành chính xác hơn.
- **Nhiều nhà máy:** cùng một cách tích hợp ERP cho mọi site vì model đã chuẩn hoá theo [ISA-95](/rhize-isa-95/).

| Mức độ tích hợp ERP | Việc đồng bộ | Phù hợp khi |
|---|---|---|
| Một chiều, thủ công | Xuất file kết quả cho ERP | ERP cũ, không có API |
| Một chiều, tự động | Rhize đẩy sản lượng lên ERP theo ca | Muốn bỏ nhập tay trước |
| Hai chiều cơ bản | Tích hợp ERP cả lệnh xuống và kết quả lên | Trường hợp phổ biến nhất |
| Hai chiều đầy đủ | Thêm vật tư, tiêu hao, nhân công | Cần tính giá thành chính xác |

Nên đi tuần tự khi tích hợp ERP: một chiều trước để kiểm chứng số liệu, rồi mới mở chiều còn lại.

---

## Lỗi thường gặp khi tích hợp ERP

| Vấn đề | Nguyên nhân | Cách xử lý |
|---|---|---|
| Số liệu hai bên lệch nhau | Định nghĩa "sản lượng" khác nhau | Thống nhất định nghĩa trước khi nối |
| Mã vật tư không khớp | Xưởng và ERP dùng mã khác | Chuẩn hoá danh mục, lập bảng ánh xạ |
| ERP quá tải khi ghi liên tục | Gửi từng sự kiện lên ERP | Gộp theo ca/mẻ thay vì realtime |
| Tiến trình treo khi ERP bận | Không có timeout | Đặt timeout và cơ chế thử lại trong BPMN |
| Không ai chịu trách nhiệm dữ liệu | Ranh giới IT–sản xuất mờ | Xác định chủ sở hữu từng nhóm dữ liệu |

Dòng đầu tiên là nguyên nhân số một khiến dự án tích hợp ERP bị mất niềm tin. "Sản lượng" ở xưởng có thể là số sản phẩm qua máy đếm; ở ERP là số đã nhập kho sau kiểm. Hai con số này **không bao giờ bằng nhau** — và điều đó bình thường, miễn là cả hai bên hiểu vì sao.

---

<a name="bao-gia"></a>
## Nhận tư vấn tích hợp ERP với Rhize Data Hub

Gửi cho chúng tôi: **ERP đang dùng (tên, phiên bản, module) · cách đang nhập số liệu sản xuất · dữ liệu cần đồng bộ hai chiều · tần suất mong muốn.**

Chúng tôi khảo sát khả năng tích hợp ERP, đề xuất luồng dữ liệu và thiết kế workflow đồng bộ.

**→ [Liên hệ tư vấn tích hợp ERP](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize có thay được module sản xuất của ERP không?**
**Rhize** đảm nhiệm phần **thực thi và dữ liệu ở nhà xưởng** — thứ ERP làm không tốt vì thiết kế cho nghiệp vụ giao dịch. Kế hoạch, mua hàng, kho, tài chính vẫn nên ở ERP.

**ERP cũ không có API thì sao?**
Phương án thường dùng là trao đổi file theo lịch hoặc qua cơ sở dữ liệu trung gian. Cần thoả thuận với nhà cung cấp ERP để không vi phạm điều kiện hỗ trợ.

**Có nên đẩy dữ liệu lên ERP theo thời gian thực không?**
Thường không nên. ERP không thiết kế để nhận hàng nghìn giao dịch mỗi giờ. Nên gộp theo ca hoặc theo mẻ, giữ dữ liệu chi tiết ở Data Hub.

**Tích hợp ERP mất bao lâu?**
Với ERP có API và danh mục đã chuẩn, thường vài tuần cho luồng đầu tiên. Phần lâu nhất là **thống nhất định nghĩa và mã danh mục** giữa hai bên.

**Ai nên chủ trì dự án tích hợp ERP?**
Dự án tích hợp ERP cần một người có quyền quyết định ở cả hai phía — nếu để IT và sản xuất tự thoả thuận, khác biệt về định nghĩa dữ liệu thường không được giải quyết dứt điểm.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-bpmn-workflow/, /rhize-isa-95/, /rhize-scheduling-lap-ke-hoach/, /lien-he/. -->
