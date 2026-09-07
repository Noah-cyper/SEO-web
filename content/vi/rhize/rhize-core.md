<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-core/
TỪ KHÓA    : rhize core | librecore | rules engine sản xuất | xử lý sự kiện phức hợp | complex event processing | gắn ngữ cảnh dữ liệu
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Tên dịch vụ theo tài liệu Rhize (libreCore); đối chiếu bản phát hành đang dùng.
-->

TITLE TAG   : Rhize Core – Rules Engine Gắn Ngữ Cảnh Cho Dữ Liệu
META (151)  : Rhize Core (libreCore) là dịch vụ lõi xử lý luật và sự kiện: biến giá trị tag thô từ PLC thành sự kiện có ngữ cảnh ISA-95 để tính OEE, truy xuất và cảnh báo.
H1          : Rhize Core – Rules Engine Xử Lý Sự Kiện Sản Xuất

---

## Rhize Core làm gì trong nền tảng?

<!--IMG:rep-->
![Rhize Core - Rules Engine Xử Lý Sự Kiện Sản Xuất](assets/diagrams/rep-core.svg)


**Rhize Core** (tên dịch vụ **libreCore**) là dịch vụ lõi đứng giữa luồng dữ liệu thô và cơ sở dữ liệu đồ thị. Việc của nó gói gọn trong một câu: **biến con số thành sự kiện có nghĩa**.

Ví dụ: một PLC báo `Line3_Counter = 4820` cho **Rhize Core**. Con số đó tự nó không nói được gì. **Rhize Core** đối chiếu với luật đã cấu hình và trả lời: đây là sản lượng của **work unit** máy chiết số 2, thuộc **lệnh sản xuất** JO-2026-0912, đang chạy **lô nguyên liệu** NL-2026-118, **ca B**, và so với kế hoạch thì đang chậm 6%.

Đó là khác biệt giữa một historian và một Manufacturing Data Hub. Historian lưu `4820`. **Rhize Core** lưu **ý nghĩa** của `4820`.

> **Cần thiết kế bộ luật xử lý sự kiện cho dây chuyền?** Gửi mô tả quy trình → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Rhize Core xử lý những loại luật nào?

| Loại luật trong Rhize Core | Ví dụ trong nhà máy | Kết quả sinh ra |
|---|---|---|
| **Gắn ngữ cảnh** | Tag này thuộc work unit nào | Sự kiện có đủ quan hệ ISA-95 |
| **Phát hiện thay đổi trạng thái** | Máy chạy → dừng | Sự kiện downtime, tính thời lượng |
| **Phân loại** | Dừng do sự cố hay do đổi khuôn | Mã lý do dừng chuẩn hoá |
| **Tổng hợp** | Cộng dồn sản lượng theo ca | Job response, operations performance |
| **Ngưỡng & cảnh báo** | Nhiệt độ vượt dải cho phép | Sự kiện chất lượng, kích hoạt workflow |
| **Tương quan nhiều nguồn** | Cân + nhiệt độ + kết quả QC cùng một lô | Sự kiện phức hợp |

Dòng cuối cùng — **xử lý sự kiện phức hợp (complex event processing)** — là thứ khó làm bằng cách viết script rời rạc, vì nó đòi hỏi giữ trạng thái theo thời gian và biết dữ liệu từ nhiều nguồn thuộc về cùng một ngữ cảnh.

---

## Luồng xử lý qua Rhize Core

1. **Libre Agent** đọc tag từ PLC/SCADA và publish thay đổi lên **NATS**.
2. **Rhize Core** đăng ký nhận các sự kiện đó.
3. Với mỗi sự kiện, Core tra **mô hình ISA-95** trong Rhize DB: tag này ánh xạ tới work unit nào, work unit đó đang chạy job order nào.
4. Core áp **bộ luật**: phát hiện chuyển trạng thái, phân loại, tổng hợp, so ngưỡng.
5. Sự kiện đã đầy đủ ngữ cảnh được **ghi vào Rhize DB** như nút trong đồ thị.
6. Nếu có **workflow BPMN** lắng nghe loại sự kiện này, engine được kích hoạt.

Bước 3 trong **Rhize Core** là lý do vì sao mô hình hoá dữ liệu quyết định chất lượng toàn hệ thống: **Rhize Core** chỉ gắn được ngữ cảnh nếu mô hình ISA-95 mô tả đúng nhà máy. Xem [Rhize và ISA-95](/rhize-isa-95/).

| Bước trong luồng | Rhize Core làm gì | Kết quả |
|---|---|---|
| Nhận sự kiện | Đọc bản tin từ NATS | Giá trị thô + mốc thời gian |
| Tra mô hình | Đối chiếu tag với work unit | Biết sự kiện thuộc về đâu |
| Áp luật | Phân loại, tổng hợp, so ngưỡng | Sự kiện có nghĩa |
| Ghi nhận | Đưa vào Rhize DB | Nút trong đồ thị |
| Phát tín hiệu | Kích hoạt workflow nếu cần | Quy trình tự chạy |

---

## So sánh Rhize Core với cách xử lý dữ liệu truyền thống

| Tiêu chí | Script tích hợp tự viết | SQL job theo lịch | **Rhize Core** |
|---|---|---|---|
| Độ trễ | Tuỳ script | Theo chu kỳ (phút–giờ) | **Thời gian thực** |
| Giữ trạng thái | Tự cài đặt | Khó | **Có sẵn** |
| Đổi quy tắc nghiệp vụ | Sửa code, triển khai lại | Sửa query | **Cấu hình luật** |
| Ai sửa được | Lập trình viên | DBA | Kỹ sư vận hành |
| Truy vết khi sai | Khó | Khó | Trace qua **Tempo** |
| Dùng lại cho dây chuyền khác | Copy-paste, phân nhánh | Hạn chế | **Nhân bản theo model** |

Điểm quan trọng với nhà máy Việt Nam nằm ở dòng "ai sửa được". Nếu mỗi lần đổi cách tính downtime lại phải chờ nhà thầu phần mềm, hệ thống sẽ nhanh chóng lệch khỏi thực tế vận hành.

---

## Ứng dụng Rhize Core theo bài toán

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Tính OEE đúng nghĩa:** downtime, tốc độ, chất lượng đều sinh từ sự kiện có ngữ cảnh thay vì ước lượng từ tag. Xem [Rhize và OEE](/rhize-oee/).
- **Cảnh báo chất lượng tức thì:** thông số vượt dải kích hoạt workflow ngay trong lúc chạy, không chờ kiểm cuối mẻ. Xem [quản lý chất lượng](/rhize-quan-ly-chat-luong/).
- **Phân tích dừng máy:** mã lý do dừng chuẩn hoá cho phép so sánh giữa các dây chuyền và nhà máy.
- **Nền dữ liệu sạch cho AI:** sự kiện đã gắn nhãn dùng trực tiếp cho mô hình. Xem [AI/ML trên dữ liệu Rhize](/rhize-ai-ml-du-lieu-san-xuat/).

| Bài toán | Luật Rhize Core cần cấu hình | Kết quả dùng được ngay |
|---|---|---|
| OEE | Chuyển trạng thái chạy/dừng, mã lý do | Availability, Performance |
| Chất lượng | Ngưỡng thông số theo công thức | Cảnh báo trong lúc chạy |
| Truy xuất | Sự kiện đổi lô nguyên liệu | Liên kết genealogy |
| Năng lượng | Ghép công tơ với work unit | Suất tiêu hao theo công đoạn |

---

## Lưu ý khi cấu hình luật trong Rhize Core

| Sai lầm thường gặp | Hậu quả | Cách tránh |
|---|---|---|
| Định nghĩa downtime mỗi line một kiểu | OEE không so sánh được | Chuẩn hoá ở tầng model, không ở từng line |
| Ngưỡng cảnh báo đặt quá nhạy | Nhiễu cảnh báo, nhân viên bỏ qua | Hiệu chỉnh theo dữ liệu thật 2–4 tuần |
| Luật viết cứng theo tên tag | Đổi PLC là hỏng | Ánh xạ qua model ISA-95 |
| Không ghi lý do dừng | Phân tích vô nghĩa | Bắt buộc nhập/tự suy luận mã lý do |
| Bỏ qua tracing | Không biết luật nào chạy sai | Bật Tempo từ đầu |

---

<a name="bao-gia"></a>
## Nhận tư vấn cấu hình Rhize Core

Gửi cho chúng tôi: **mô tả quy trình dây chuyền · danh sách tag hiện có · cách đang định nghĩa downtime và phế phẩm · yêu cầu cảnh báo.**

Chúng tôi sẽ đề xuất bộ luật xử lý sự kiện và cách chuẩn hoá để dùng lại được cho các dây chuyền sau.

**→ [Liên hệ tư vấn Rhize Core](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize Core khác gì BPMN engine?**
**Rhize Core** xử lý **dữ liệu và sự kiện** — gắn ngữ cảnh, phân loại, tổng hợp. **BPMN engine** điều phối **quy trình nghiệp vụ** — gọi hệ thống khác, chờ phê duyệt, rẽ nhánh. Xem [BPMN workflow](/rhize-bpmn-workflow/).

**Cấu hình luật có cần lập trình không?**
Phần lớn là cấu hình dựa trên mô hình dữ liệu, không phải viết ứng dụng. Logic phức tạp hơn được đưa sang workflow BPMN low-code.

**Rhize Core xử lý được bao nhiêu sự kiện?**
Nền tảng thiết kế cho khối lượng sự kiện lớn và mở rộng ngang trên Kubernetes. Con số cụ thể phụ thuộc cấu hình cluster — cần thử tải theo số tag thật của nhà máy.

**Nếu dữ liệu tag bị mất một khoảng thì sao?**
Sự kiện sinh ra sẽ khuyết trong khoảng đó. Nên thiết kế luật có khả năng phát hiện gián đoạn nguồn và đánh dấu, thay vì im lặng bỏ qua.

**Có sửa lại được sự kiện đã ghi không?**
Với dữ liệu phục vụ tuân thủ, nguyên tắc là **không sửa** mà ghi bản hiệu chỉnh kèm lý do và người thực hiện, giữ nguyên vết cũ.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /kien-truc-nen-tang-rhize/, /rhize-bpmn-workflow/, /rhize-oee/, /lien-he/. -->
