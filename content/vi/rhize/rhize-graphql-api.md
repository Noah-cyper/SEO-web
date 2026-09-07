<!--
LOẠI TRANG : Bài kỹ thuật (satellite) — Kỹ thuật + giải pháp
URL SLUG   : /rhize-graphql-api/
TỪ KHÓA    : graphql | rhize graphql api | graphql sản xuất | apollo router | api dữ liệu nhà máy | endpoint duy nhất | truy vấn dữ liệu sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu schema GraphQL của bản Rhize đang dùng trước khi đăng ví dụ truy vấn.
-->

TITLE TAG   : Rhize GraphQL API – Một Endpoint Cho Mọi Ứng Dụng
META (152)  : Rhize GraphQL API: một endpoint duy nhất truy vấn toàn bộ dữ liệu sản xuất chuẩn ISA-95. Vì sao GraphQL hợp với graph, phân quyền và ví dụ dùng thực tế.
H1          : Rhize GraphQL API – Một Endpoint Cho Mọi Ứng Dụng

---

## Rhize GraphQL API là gì?

<!--IMG:rep-->
![Rhize GraphQL API - Một Endpoint Cho Mọi Ứng Dụng](assets/diagrams/rep-graphql.svg)


**Rhize GraphQL API** là **điểm truy cập duy nhất** vào toàn bộ dữ liệu của Manufacturing Data Hub. Mọi ứng dụng — dashboard vận hành, báo cáo OEE, hệ thống ERP, mô hình AI — đều đi qua cùng một endpoint, thay vì mỗi hệ thống một kiểu kết nối riêng.

Đây không phải lựa chọn ngẫu nhiên. Cơ sở dữ liệu của **Rhize** là **graph**, và ngôn ngữ truy vấn **GraphQL** khớp gần như một-một với mô hình đồ thị: truy vấn mô tả **hình dạng dữ liệu muốn lấy**, đi theo quan hệ, và trả về đúng phần đó — không thừa, không thiếu.

Cổng vào GraphQL được đảm nhiệm bởi **Apollo Router**, giữ cho bề mặt API nhỏ và ổn định kể cả khi số dịch vụ phía sau tăng lên.

> **Cần đánh giá khả năng tích hợp qua API?** Gửi danh sách ứng dụng cần kết nối → [Nhận tư vấn tích hợp](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Vì sao dùng GraphQL thay vì REST cho dữ liệu sản xuất?

| Tiêu chí | REST truyền thống | **Rhize GraphQL API** |
|---|---|---|
| Số endpoint | Nhiều, tăng theo nhu cầu | **Một** |
| Lấy dữ liệu liên quan | Nhiều lần gọi (N+1) | **Một truy vấn, đi theo quan hệ** |
| Dữ liệu thừa | Thường trả cả object | Chỉ trả trường được hỏi |
| Đổi yêu cầu báo cáo | Sửa backend, phát hành lại | Sửa truy vấn phía client |
| Khám phá schema | Đọc tài liệu | **Introspection** ngay trên schema |
| Hợp với mô hình graph | Không tự nhiên | **Khớp trực tiếp** |

Với nhà máy, khác biệt lớn nhất nằm ở dòng thứ tư. Yêu cầu báo cáo trong sản xuất thay đổi liên tục — hôm nay tính OEE theo ca, tuần sau theo lô, tháng sau theo mã sản phẩm. Với REST, mỗi lần đổi là một vòng phát triển. Với **GraphQL**, phần lớn thay đổi chỉ là viết lại truy vấn.

---

## Rhize GraphQL API trả lời những câu hỏi nào?

| Câu hỏi nghiệp vụ | Đi qua quan hệ nào trong graph |
|---|---|
| Lô thành phẩm này dùng nguyên liệu lô nào | Material lot → sublot → nguyên liệu đầu vào |
| Máy nào đã chạm vào lô này | Job response → work unit → equipment |
| Ca nào có OEE thấp nhất tuần qua | Operations performance → personnel → thời gian |
| Lệnh sản xuất nào đang chậm tiến độ | Operations schedule ↔ job response |
| Thiết bị đo dùng cho mẻ này còn hạn hiệu chuẩn không | Job response → physical asset → hiệu chuẩn |

Điểm đáng chú ý: tất cả những câu hỏi trên chạy trên **cùng một endpoint**, không cần dựng thêm data mart hay ETL riêng cho từng loại báo cáo.

---

## Bảo mật và phân quyền trên Rhize GraphQL API

Một endpoint duy nhất chỉ an toàn khi phân quyền chặt. **Rhize** áp dụng ba lớp kiểm soát:

| Lớp kiểm soát | Cơ chế | Ví dụ áp dụng |
|---|---|---|
| **Role-based (RBAC)** | Vai trò trong Keycloak | Kỹ sư QC đọc dữ liệu chất lượng |
| **Attribute-based (ABAC)** | Thuộc tính người dùng/dữ liệu | Chỉ xem dữ liệu nhà máy mình |
| **Graph-based** | Vị trí trong đồ thị | Chỉ xem nhánh work center phụ trách |
| **Xác thực** | OIDC qua **Keycloak**, JWT | Ghép SSO/AD sẵn có |

Lớp thứ ba là thứ khó làm với API truyền thống: phân quyền theo **vị trí trong cấu trúc nhà máy**, không phải theo bảng dữ liệu. Xem [Keycloak và phân quyền trong Rhize](/rhize-keycloak-phan-quyen/).

---

## Ứng dụng Rhize GraphQL API trong nhà máy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Dashboard vận hành tại xưởng:** màn hình treo tại line lấy dữ liệu realtime qua **GraphQL**, không cần trung gian.
- **Báo cáo OEE:** một truy vấn cho cả nhà máy, thay vì mỗi dây chuyền một file Excel. Xem [Rhize và OEE](/rhize-oee/).
- **Đồng bộ ERP:** ERP đọc kết quả sản xuất và ghi lệnh mới. Xem [tích hợp ERP](/rhize-tich-hop-erp/).
- **Truy xuất nguồn gốc:** bộ phận QA tự chạy truy vấn khi có khiếu nại. Xem [track & trace](/rhize-truy-xuat-nguon-goc/).
- **Nạp dữ liệu cho AI/ML:** kéo luồng sự kiện đã gắn nhãn. Xem [AI/ML trên dữ liệu Rhize](/rhize-ai-ml-du-lieu-san-xuat/).

| Ai dùng GraphQL | Dùng để làm gì | Tần suất |
|---|---|---|
| Kỹ sư vận hành | Xem tiến độ, tình trạng máy | Liên tục trong ca |
| QA / QC | Truy xuất lô, kết quả kiểm | Khi có sự cố |
| Kế hoạch | Đối chiếu lệnh với thực tế bằng GraphQL | Hằng ngày |
| Đội phân tích | Kéo dữ liệu huấn luyện mô hình | Theo dự án |
| Hệ thống ERP | Đồng bộ tự động qua GraphQL | Theo ca hoặc theo mẻ |

---

## Lưu ý khi thiết kế truy vấn GraphQL cho hệ thống sản xuất

| Vấn đề hay gặp | Hậu quả | Cách xử lý |
|---|---|---|
| Truy vấn lồng quá sâu | Tải nặng lên DB | Giới hạn độ sâu, phân trang |
| Kéo toàn bộ lịch sử | Chậm, tốn băng thông | Lọc theo khoảng thời gian |
| Dashboard poll liên tục | Nghẽn không cần thiết | Dùng subscription / sự kiện |
| Không đặt tên truy vấn | Khó truy vết khi chậm | Đặt tên, bật tracing với Tempo |
| Cấp quyền quá rộng | Rủi ro lộ dữ liệu | Phân quyền theo nhánh graph |

Đây là những lỗi lặp lại ở hầu hết dự án đầu tiên. Bật **tracing bằng Tempo** ngay từ giai đoạn thử nghiệm giúp phát hiện truy vấn nặng trước khi lên production — xem [Grafana và Tempo trong Rhize](/rhize-grafana-tempo/).

---

<a name="bao-gia"></a>
## Nhận tư vấn tích hợp qua Rhize GraphQL API

Gửi cho chúng tôi: **danh sách ứng dụng cần lấy dữ liệu · loại báo cáo cần ra · tần suất truy vấn · yêu cầu phân quyền theo phòng ban/nhà máy.**

Chúng tôi sẽ đề xuất cách tổ chức truy vấn, mô hình phân quyền và cách ghép với hệ thống hiện có.

**→ [Liên hệ tư vấn Rhize GraphQL API](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize GraphQL API có thay được kết nối ODBC/SQL không?**
Với phần lớn nhu cầu báo cáo thì có, và tiện hơn vì dữ liệu đã có ngữ cảnh. Công cụ BI chỉ hỗ trợ SQL vẫn kết nối được qua lớp trung gian.

**Truy vấn GraphQL có chậm hơn SQL không?**
Không hẳn — với các câu hỏi đi theo quan hệ nhiều cấp (truy xuất nguồn gốc chẳng hạn), truy vấn trên graph thường **nhanh hơn** SQL nhiều join. Với tổng hợp bảng phẳng khối lượng lớn thì SQL vẫn có lợi thế.

**Ứng dụng cũ chỉ nói REST thì sao?**
Đặt một lớp adapter mỏng chuyển REST sang **GraphQL**, hoặc dùng workflow BPMN để đẩy dữ liệu sang hệ thống cũ theo định dạng nó hiểu.

**API có hỗ trợ dữ liệu thời gian thực không?**
Có. Nền tảng hướng sự kiện, dữ liệu thay đổi được phát qua **NATS** và ứng dụng nhận theo cơ chế đăng ký thay vì hỏi liên tục — xem [NATS trong Rhize](/rhize-nats-event-streaming/).

**Ai trong nhà máy sẽ viết truy vấn?**
Thường là kỹ sư dữ liệu hoặc IT. **GraphQL** có introspection nên người dùng có thể tự khám phá schema; các truy vấn hay dùng nên đóng gói sẵn cho bộ phận nghiệp vụ.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-db-graph-database/, /rhize-keycloak-phan-quyen/, /lien-he/. -->
