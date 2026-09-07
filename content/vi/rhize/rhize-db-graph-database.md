<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-db-graph-database/
TỪ KHÓA    : rhize db | librebaas | graph database sản xuất | đồ thị tri thức nhà máy | knowledge graph | cơ sở dữ liệu isa-95
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Tên dịch vụ theo tài liệu Rhize (libreBaas); đối chiếu bản phát hành đang dùng.
-->

TITLE TAG   : Rhize DB – Graph Database Chuẩn ISA-95 Cho Nhà Máy
META (150)  : Rhize DB (libreBaas) là graph database lưu toàn bộ trạng thái sản xuất theo schema ISA-95 và phát hành GraphQL. Vì sao dùng đồ thị và cách triển khai.
H1          : Rhize DB – Graph Database Chuẩn ISA-95

---

## Rhize DB là gì?

<!--IMG:rep-->
![Rhize DB - Graph Database Chuẩn ISA-95](assets/diagrams/rep-graphdb.svg)


**Rhize DB** — tên dịch vụ là **libreBaas** — là cơ sở dữ liệu đồ thị nằm ở trung tâm Manufacturing Data Hub. Nó lưu **toàn bộ trạng thái vận hành** của nhà máy dưới dạng một **đồ thị tri thức (knowledge graph)**: thiết bị, vật tư, con người, lệnh sản xuất, sự kiện — và quan trọng hơn cả, **các quan hệ giữa chúng**.

Schema của **Rhize DB** không phải một schema trống để tự thiết kế. Nó là **schema ISA-95** dựng sẵn, nên ngay khi cài xong, cơ sở dữ liệu đã hiểu thế nào là work unit, material lot, job response.

**Rhize DB** cũng là dịch vụ **phải cài đầu tiên** khi triển khai: các thành phần còn lại phụ thuộc vào schema và **GraphQL endpoint** mà nó phát hành.

> **Cần ước lượng dung lượng và hạ tầng cho Rhize DB?** Gửi số điểm dữ liệu và tần suất → [Nhận tư vấn hạ tầng](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-graph.svg)


---

## Rhize DB lưu những gì?

| Nhóm dữ liệu | Nội dung | Dạng lưu |
|---|---|---|
| **Mô hình (master data)** | Cây thiết bị, mã vật tư, công thức, vai trò | Nút + cạnh trong graph |
| **Giao dịch** | Lệnh sản xuất, job response, kết quả kiểm | Nút gắn quan hệ theo thời gian |
| **Sự kiện** | Dừng máy, đổi lô, cảnh báo | Nút sự kiện có ngữ cảnh |
| **Chuỗi thời gian** | Giá trị tag theo thời gian | Lưu trữ time-series |
| **Quan hệ genealogy** | Lô con ← lô cha, thành phẩm ← nguyên liệu | Cạnh nhiều cấp |

Việc **Rhize DB** giữ cả **graph giao dịch** lẫn **time-series** trong cùng một hub là điểm khác biệt so với kiến trúc tách rời historian và cơ sở dữ liệu nghiệp vụ. Không phải ghép hai nguồn ở tầng báo cáo nữa.

---

## Vì sao chọn graph database cho dữ liệu sản xuất?

Sản xuất về bản chất là một **mạng lưới quan hệ**, không phải một tập bảng phẳng. Một mẻ hàng liên quan tới nguyên liệu, thiết bị, con người, công thức, điều kiện môi trường — và mỗi thứ đó lại liên quan tiếp.

| Bài toán | Trên bảng quan hệ | Trên **Rhize DB** |
|---|---|---|
| Truy ngược 5 cấp genealogy | Truy vấn đệ quy, rất nặng | Duyệt cạnh, tự nhiên |
| Thêm loại quan hệ mới | Sửa schema, migrate dữ liệu | Thêm cạnh |
| Tìm mọi lô bị ảnh hưởng bởi 1 lô nguyên liệu | Nhiều join, chậm | Duyệt ngược nhanh |
| Cấu trúc dây chuyền thay đổi | Ảnh hưởng nhiều bảng | Thêm/sửa nút |
| Phân quyền theo nhánh nhà máy | Phải mô phỏng bằng cột | Theo vị trí trong graph |

Với nhà máy thực phẩm hoặc dược, dòng thứ ba là kịch bản sống còn: khi phát hiện một lô nguyên liệu có vấn đề, câu hỏi "những lô thành phẩm nào bị ảnh hưởng" phải trả lời trong vài phút, không phải vài ngày.

---

## Rhize DB trong kiến trúc nền tảng

| Quan hệ | Chi tiết |
|---|---|
| **Phát hành GraphQL** | Endpoint duy nhất, qua Apollo Router |
| **Nhận dữ liệu từ** | Libre Core (sự kiện đã gắn ngữ cảnh) |
| **Phục vụ cho** | BPMN engine, Admin UI, ứng dụng bên ngoài |
| **Xác thực** | Giữ public key từ **Keycloak** để xác minh JWT |
| **Thứ tự cài đặt** | **Cài trước tiên** trong các dịch vụ Rhize |
| **Triển khai** | Helm chart trên Kubernetes |

Xem thêm [kiến trúc nền tảng Rhize](/kien-truc-nen-tang-rhize/) và [Rhize GraphQL API](/rhize-graphql-api/).

---

## Ứng dụng Rhize DB theo ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thuỷ sản, thực phẩm xuất khẩu:** truy xuất từ container thành phẩm về ao nuôi/lô nguyên liệu để đáp ứng yêu cầu của nhà nhập khẩu. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Dược phẩm:** genealogy đầy đủ kèm nhân sự và thiết bị đo cho hồ sơ lô. Xem [ngành dược phẩm](/rhize-nganh-duoc-pham/).
- **Điện tử, linh kiện ô tô:** gắn serial thành phẩm với từng linh kiện và máy gia công. Xem [sản xuất rời rạc](/rhize-san-xuat-roi-rac-serial/).
- **Xi măng, thép:** ghép dữ liệu năng lượng theo công đoạn với sản lượng để tính suất tiêu hao.

| Ngành | Câu hỏi Rhize DB trả lời được | Dữ liệu cần có |
|---|---|---|
| Thực phẩm | Lô thành phẩm này từ lô nguyên liệu nào | Quét mã lô tại điểm nạp |
| Dược | Mẻ này chạy trên thiết bị nào, ai duyệt | Đăng nhập, xác nhận điện tử |
| Điện tử | Serial này lắp linh kiện lô nào | Quét mã tại từng trạm |
| Xi măng, thép | Suất tiêu hao theo công đoạn | Công tơ gắn với work unit |

---

## Vận hành Rhize DB: những điểm cần chuẩn bị

| Hạng mục | Khuyến nghị |
|---|---|
| **Dung lượng Rhize DB** | Ước theo số tag × tần suất × thời gian lưu; tách chính sách lưu graph và time-series |
| **Sao lưu** | Backup định kỳ **và kiểm thử phục hồi**, không chỉ chạy backup |
| **Phân quyền** | Vai trò libreBaas phải được thêm vào nhóm quản trị trong Keycloak |
| **Quan sát** | Theo dõi độ trễ truy vấn bằng Grafana ngay từ đầu |
| **Mô hình hoá** | Thống nhất danh mục thiết bị/vật tư trước khi nạp dữ liệu thật |

Lỗi phổ biến nhất khi triển khai **Rhize DB** không nằm ở kỹ thuật mà ở dữ liệu: nạp dữ liệu thật vào khi danh mục thiết bị chưa thống nhất, sau đó phải làm lại từ đầu.

---

<a name="bao-gia"></a>
## Nhận tư vấn triển khai Rhize DB

Gửi cho chúng tôi: **số tag/điểm dữ liệu ước tính · tần suất lấy mẫu · thời gian cần lưu · yêu cầu truy xuất · hạ tầng máy chủ hiện có.**

Chúng tôi sẽ ước lượng tài nguyên, đề xuất chính sách lưu trữ và kế hoạch mô hình hoá dữ liệu.

**→ [Liên hệ tư vấn Rhize DB](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize DB có thay thế historian không?**
Không nhất thiết. Nhiều nhà máy giữ historian cho tag tần số rất cao và để **Rhize DB** giữ phần dữ liệu có ngữ cảnh. Cũng có thể để **Rhize** đảm nhiệm cả hai nếu khối lượng phù hợp.

**Dữ liệu cũ trong historian có nạp vào được không?**
Được, nhưng chỉ nên nạp phần có thể gắn ngữ cảnh. Nạp dữ liệu tag thô không kèm lô/lệnh sản xuất thì vẫn không trả lời được câu hỏi truy xuất.

**Graph database có khó vận hành hơn SQL không?**
Khác chứ không khó hơn. Đội IT cần làm quen với mô hình đồ thị và **GraphQL**; bù lại không phải viết và bảo trì các truy vấn nhiều join.

**Rhize DB chạy on-premise được không?**
Được. Dịch vụ triển khai qua Helm trên Kubernetes, đặt tại chỗ hoặc trên cloud tuỳ chính sách dữ liệu.

**Cần cài dịch vụ nào trước Rhize DB không?**
Không — **libreBaas** là dịch vụ **cài đầu tiên**. Keycloak cần được cấu hình để xác thực hoạt động đúng.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-graphql-api/, /rhize-truy-xuat-nguon-goc/, /lien-he/. -->
