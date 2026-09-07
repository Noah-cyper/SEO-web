<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + vận hành
URL SLUG   : /rhize-admin-ui/
TỪ KHÓA    : admin ui | rhize admin ui | giao diện quản trị rhize | mô hình hoá dữ liệu sản xuất | workflow ui | quản lý model isa-95 | cấu hình data hub
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Bố cục giao diện thay đổi theo bản phát hành; đối chiếu tài liệu Rhize trước khi đăng ảnh chụp màn hình.
-->

TITLE TAG   : Rhize Admin UI – Quản Trị Model, Người Dùng, Workflow
META (148)  : Rhize Admin UI là giao diện quản trị Data Hub: dựng model ISA-95, quản lý người dùng và vai trò, mô hình hoá workflow BPMN. Ai dùng và dùng thế nào.
H1          : Rhize Admin UI – Giao Diện Quản Trị Data Hub

---

## Rhize Admin UI là gì?

<!--IMG:rep-->
![Rhize Admin UI - Giao Diện Quản Trị Data Hub](assets/diagrams/rep-app.svg)


**Rhize Admin UI** (dịch vụ **libreAdminUI**) là giao diện quản trị của nền tảng. Vì **Rhize** là hệ thống **headless** — không kèm giao diện vận hành đóng gói sẵn — Admin UI không phải màn hình cho công nhân đứng máy. Nó là **bàn làm việc của người xây dựng hệ thống**.

Ba nhóm việc chính diễn ra trong Admin UI:

- **Mô hình hoá dữ liệu**: dựng cây thiết bị, danh mục vật tư, công thức, vai trò nhân sự theo **ISA-95**.
- **Quản trị người dùng**: gán vai trò, phạm vi dữ liệu, phối hợp với Keycloak.
- **Mô hình hoá workflow**: vẽ và quản lý các quy trình **BPMN** low-code.

> **Cần hướng dẫn đội kỹ thuật sử dụng Admin UI?** → [Nhận tư vấn đào tạo](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-isa95.svg)


---

## Các nhóm chức năng trong Rhize Admin UI

| Nhóm chức năng | Nội dung | Ai thường dùng |
|---|---|---|
| **Model / master data** | Cây thiết bị, vật tư, nhân sự, công thức | Kỹ sư dữ liệu, kỹ sư quy trình |
| **Nguồn dữ liệu** | Cấu hình kết nối, ánh xạ tag | Kỹ sư tự động hoá |
| **Luật xử lý sự kiện** | Định nghĩa downtime, ngưỡng, phân loại | Kỹ sư vận hành |
| **Workflow (BPMN UI)** | Vẽ, kiểm thử, phát hành workflow | Kỹ sư triển khai |
| **Người dùng & vai trò** | Gán quyền, phạm vi dữ liệu | Quản trị hệ thống |
| **Nhật ký & phiên bản** | Ai đổi gì, khi nào | Quản trị, kiểm toán |

Dòng cuối cùng đáng chú ý với nhà máy có yêu cầu tuân thủ: mọi thay đổi model và workflow đều cần để lại vết, vì model chính là thứ quyết định số liệu trong hồ sơ lô.

---

## Mô hình hoá dữ liệu trong Admin UI

Mô hình hoá trong Admin UI là công việc tốn thời gian nhất của cả dự án, và cũng là phần quyết định chất lượng mọi báo cáo về sau.

| Bước | Việc làm | Kết quả |
|---|---|---|
| 1 | Dựng cây **enterprise → site → area → work center → work unit** | Khung ngữ cảnh cho mọi sự kiện |
| 2 | Nhập danh mục vật tư (definition) | Nền cho truy xuất nguồn gốc |
| 3 | Khai báo vai trò nhân sự | Ghi nhận trách nhiệm |
| 4 | Khai báo tài sản vật lý, thiết bị đo | Quản lý hiệu chuẩn |
| 5 | Định nghĩa công thức / operations definition | Chuẩn hoá quy trình |
| 6 | Ánh xạ tag từ nguồn vào work unit | Nối dữ liệu thật vào model |

Bước 6 là chỗ mô hình gặp thực tế. Nếu tên tag trong PLC đặt tuỳ hứng — điều rất phổ biến — bước này sẽ lộ ra ngay và cần chuẩn hoá trước. Xem [Rhize và ISA-95](/rhize-isa-95/).

---

## Admin UI so với giao diện vận hành

| Tiêu chí | **Rhize Admin UI** | Ứng dụng vận hành (tự dựng) |
|---|---|---|
| Đối tượng dùng | Kỹ sư xây dựng hệ thống | Công nhân, tổ trưởng, QC |
| Tần suất dùng | Khi cấu hình, thay đổi | Liên tục trong ca |
| Nội dung | Model, luật, workflow, quyền | Nhập liệu, xác nhận, xem chỉ số |
| Cách xây | Có sẵn trong nền tảng | Dựng riêng trên **GraphQL API** |
| Yêu cầu thiết kế | Đầy đủ chức năng | Đơn giản, ít thao tác, chữ lớn |

Đây là điểm cần làm rõ ngay từ đầu dự án để tránh hiểu nhầm: **Rhize không đi kèm màn hình cho công nhân**. Phần đó nhà máy hoặc đối tác dựng trên [GraphQL API](/rhize-graphql-api/), theo đúng quy trình thực tế của xưởng.

---

## Ứng dụng thực tế tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Giai đoạn triển khai:** đội dự án dùng Admin UI dựng model cho dây chuyền đầu tiên, kiểm thử luật và workflow trước khi chạy thật.
- **Nhân rộng sang dây chuyền mới:** sao chép cấu trúc model đã chuẩn, chỉnh phần khác biệt — nhanh hơn nhiều so với làm lại.
- **Thay đổi quy trình:** đổi cách phân loại downtime hoặc thêm bước kiểm tra mà không cần nhà thầu phần mềm.
- **Bàn giao cho đội nội bộ:** đào tạo kỹ sư nhà máy tự vận hành, giảm phụ thuộc bên ngoài.

Điểm cuối cùng là mục tiêu nên đặt ra ngay từ hợp đồng: nếu sau nghiệm thu nhà máy không tự sửa được model trong Admin UI, hệ thống sẽ lệch dần khỏi thực tế và bị bỏ.

| Giai đoạn dự án | Việc làm trong Admin UI | Ai thực hiện |
|---|---|---|
| Triển khai đầu | Dựng model dây chuyền đầu tiên bằng Admin UI | Đội dự án |
| Nhân rộng | Sao chép cấu trúc model đã chuẩn | Kỹ sư nhà máy |
| Thay đổi quy trình | Sửa luật, sửa workflow trong Admin UI | Kỹ sư vận hành |
| Sau nghiệm thu | Tự vận hành, không phụ thuộc nhà thầu | Đội nội bộ |

---

## Lưu ý khi vận hành Admin UI

| Rủi ro | Hệ quả | Biện pháp |
|---|---|---|
| Sửa model trực tiếp trên production | Số liệu lịch sử lệch | Có môi trường test, quản lý phiên bản |
| Nhiều người cùng sửa không phối hợp | Model mâu thuẫn | Phân quyền rõ, quy trình duyệt thay đổi |
| Không ghi lý do thay đổi | Không giải thích được với auditor | Bắt buộc ghi chú khi đổi model |
| Đặt tên không theo quy tắc | Khó bảo trì, khó nhân rộng | Thống nhất quy ước đặt tên từ đầu |
| Chỉ một người biết dùng Admin UI | Rủi ro khi người đó nghỉ | Đào tạo ít nhất hai người |

---

<a name="bao-gia"></a>
## Nhận tư vấn và đào tạo sử dụng Rhize Admin UI

Gửi cho chúng tôi: **quy mô model dự kiến (số dây chuyền, số work unit) · đội ngũ sẽ vận hành · yêu cầu quản lý thay đổi và tuân thủ.**

Chúng tôi hỗ trợ dựng model ban đầu, thống nhất quy ước đặt tên và đào tạo đội nội bộ tự vận hành.

**→ [Liên hệ tư vấn Rhize Admin UI](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Công nhân có dùng Rhize Admin UI không?**
Không nên. Admin UI dành cho người xây dựng và quản trị hệ thống. Màn hình cho xưởng nên dựng riêng, đơn giản, trên [GraphQL API](/rhize-graphql-api/).

**Cần bao nhiêu người biết dùng Admin UI?**
Tối thiểu hai — một chính, một dự phòng. Đây là kinh nghiệm rút ra từ nhiều dự án: hệ thống phụ thuộc một người là rủi ro lớn nhất sau khi nghiệm thu.

**Sửa model có ảnh hưởng dữ liệu cũ không?**
Có thể, tuỳ loại thay đổi. Với thay đổi cấu trúc, cần kiểm tra trên môi trường test trước và ghi rõ mốc thời gian áp dụng để báo cáo lịch sử vẫn giải thích được.

**Có thể nhập model hàng loạt thay vì gõ tay không?**
Với nhà máy nhiều work unit, nên chuẩn bị dữ liệu model theo dạng có cấu trúc và nạp vào qua API thay vì nhập tay từng mục.

**Ai nên chịu trách nhiệm về model?**
Một người có hiểu biết cả về quy trình sản xuất lẫn dữ liệu. Giao hẳn cho IT thường dẫn tới model đúng kỹ thuật nhưng sai thực tế vận hành.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-isa-95/, /rhize-graphql-api/, /rhize-bpmn-workflow/, /lien-he/. -->
