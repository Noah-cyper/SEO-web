<!--
LOẠI TRANG : Bài ứng dụng (satellite) — Giải pháp + thương mại
URL SLUG   : /rhize-scheduling-lap-ke-hoach/
TỪ KHÓA    : điều độ | rhize scheduling | lập kế hoạch sản xuất | điều độ sản xuất | aps là gì | lịch sản xuất nhà máy | phân bổ lệnh sản xuất
INTENT     : Giải pháp + thương mại
TRẠNG THÁI : Sẵn đăng. Phạm vi chức năng lập kế hoạch phụ thuộc cách phối hợp với ERP/APS của từng nhà máy.
-->

TITLE TAG   : Rhize Scheduling – Điều Độ Sản Xuất Theo Dữ Liệu Thật
META (145)  : Rhize scheduling: nhận lệnh từ ERP, chia xuống work center theo ISA-95, điều độ dựa trên năng lực và trạng thái máy thật. So sánh với ERP và APS.
H1          : Rhize Scheduling – Điều Độ Theo Dữ Liệu Thật

---

## Vì sao kế hoạch từ ERP thường lệch thực tế?

<!--IMG:rep-->
![Rhize Scheduling - Điều Độ Theo Dữ Liệu Thật](assets/diagrams/rep-app.svg)


ERP lập kế hoạch dựa trên **năng lực danh nghĩa**: máy chạy 8 tiếng, tốc độ theo hồ sơ kỹ thuật, không hỏng, không đổi khuôn. Thực tế xưởng thì khác — máy vừa dừng 40 phút, một line đang chạy chậm vì nguyên liệu lô mới, và đơn gấp vừa chen ngang.

Khoảng cách đó khiến kế hoạch in ra buổi sáng thường vô nghĩa sau vài giờ, và việc điều độ sản xuất thật sự diễn ra qua **bảng trắng và điện thoại**.

Điều độ sản xuất vì thế trôi ra ngoài hệ thống. **Rhize scheduling** thu hẹp khoảng cách bằng cách đưa **trạng thái thật của nhà xưởng** vào bài toán điều độ sản xuất: máy nào đang chạy gì, còn bao lâu, năng lực thực tế gần đây ra sao, nguyên liệu lô nào sẵn sàng.

> **Muốn kế hoạch bám sát thực tế xưởng?** → [Nhận tư vấn điều độ sản xuất](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Phân vai giữa ERP, APS và Rhize

| Hệ thống | Phạm vi | Chu kỳ | Dựa trên |
|---|---|---|---|
| **ERP** | Kế hoạch tổng, vật tư, đơn hàng | Tuần / tháng | Năng lực danh nghĩa |
| **APS** | Tối ưu lịch chi tiết | Ngày | Ràng buộc năng lực |
| **Rhize** | Chia lệnh xuống work center, theo dõi thực thi | **Thời gian thực** | **Trạng thái thật của máy** |
| **Người điều độ sản xuất** | Quyết định khi có xung đột | Liên tục | Kinh nghiệm + dữ liệu |

**Rhize** không thay ERP hay APS. Nó cung cấp thứ mà cả hai đều thiếu: **dữ liệu thực thi thời gian thực** và cơ chế **chia lệnh xuống đúng work center** theo mô hình [ISA-95](/rhize-isa-95/).

---

## Luồng điều độ sản xuất qua Rhize

| Bước | Việc thực hiện | Thành phần |
|---|---|---|
| 1 | Nhận **operations schedule** từ ERP | [Tích hợp ERP](/rhize-tich-hop-erp/) |
| 2 | Kiểm tra điều kiện: vật tư, thiết bị, nhân sự | [BPMN workflow](/rhize-bpmn-workflow/) |
| 3 | Sinh **job order** cho từng work center | Model ISA-95 |
| 4 | Đẩy thông tin xuống màn hình line / nạp setpoint | [Rhize Agent](/rhize-agent-ket-noi/) |
| 5 | Thu **job response** khi chạy | Core + DB |
| 6 | So tiến độ thực với kế hoạch, cảnh báo lệch | Rules + workflow |
| 7 | Trả **operations performance** về ERP | Tích hợp ERP |

Bước 2 của luồng điều độ là chỗ ngăn được nhiều tổn thất nhất: phát hiện thiếu nguyên liệu **trước khi** lệnh xuống line rẻ hơn nhiều so với phát hiện khi công nhân đã chuẩn bị máy.

---

## Dữ liệu cần cho điều độ sản xuất theo thực tế

| Dữ liệu | Nguồn | Dùng để |
|---|---|---|
| **Năng lực thực tế theo mã hàng** | Lịch sử job response | Ước thời gian chạy sát thực tế |
| **Thời gian chuyển đổi thực tế** | Sự kiện dừng chuyển đổi | Xếp thứ tự đơn hợp lý |
| **Trạng thái máy hiện tại** | PLC | Biết máy nào sẵn sàng |
| **Tồn nguyên liệu tại xưởng** | Kho, quét mã | Kiểm tra điều kiện chạy |
| **Nhân sự có mặt theo ca** | Chấm công, khai báo | Ràng buộc nhân lực |
| **Lịch bảo trì** | CMMS | Tránh xếp lệnh vào thời gian bảo trì |

Dòng đầu tiên tạo khác biệt lớn: khi hệ thống biết **mã hàng A chạy trên máy 3 thực tế đạt 82% tốc độ danh định**, kế hoạch lập ra sát hơn hẳn so với dùng con số hồ sơ kỹ thuật.

---

## So sánh cách điều độ sản xuất

| Tiêu chí | Bảng trắng + Excel | Kế hoạch từ ERP | **Rhize scheduling** |
|---|---|---|---|
| Cập nhật khi máy hỏng | Thủ công | Không | **Tự động phát hiện** |
| Dựa trên năng lực thật | Kinh nghiệm cá nhân | Không | **Có, từ lịch sử** |
| Kiểm tra điều kiện trước khi chạy | Thủ công | Không | **Workflow tự kiểm** |
| Theo dõi tiến độ realtime | Không | Không | **Có** |
| Lưu vết quyết định điều độ sản xuất | Không | Hạn chế | **Có** |
| Phụ thuộc một người | Rất cao | Thấp | **Thấp** |

Dòng cuối đáng lưu tâm với nhiều nhà máy Việt Nam: năng lực điều độ sản xuất thường nằm trong đầu **một người có kinh nghiệm**. Đưa quy tắc và dữ liệu vào hệ thống làm giảm rủi ro khi người đó nghỉ.

---

## Ứng dụng theo ngành

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thực phẩm:** xếp thứ tự đơn theo nhóm hương/màu để giảm số lần vệ sinh chuyển đổi.
- **Bao bì, nhựa:** gộp đơn cùng khuôn, giảm thời gian setup — tác động trực tiếp lên [OEE](/rhize-oee/).
- **Cơ khí:** cân bằng tải giữa các máy theo năng lực thực tế từng mã hàng.
- **Dệt may:** điều độ sản xuất theo chuyền và theo tay nghề tổ, phản ứng nhanh khi đơn gấp chen ngang.

| Vấn đề điều độ hay gặp | Nguyên nhân | Dữ liệu Rhize bổ sung |
|---|---|---|
| Kế hoạch sáng ra, trưa đã lệch | Không biết máy dừng | Trạng thái máy thời gian thực |
| Ước sai thời gian chạy | Dùng tốc độ danh định | Năng lực thực tế theo mã hàng |
| Lệnh xuống line rồi mới biết thiếu vật tư | Không kiểm điều kiện trước | Workflow chặn trước khi chạy |
| Điều độ phụ thuộc một người | Quy tắc nằm trong đầu người đó | Quy tắc đưa vào workflow |

---

<a name="bao-gia"></a>
## Nhận tư vấn điều độ sản xuất với Rhize

Gửi cho chúng tôi: **cách đang lập kế hoạch · ERP/APS đang dùng · số dây chuyền và mã hàng · các ràng buộc chính (khuôn, vệ sinh, nhân lực) · vấn đề đang gặp.**

Chúng tôi đề xuất phân vai giữa ERP và Data Hub, thiết kế luồng chia lệnh và bộ dữ liệu năng lực thực tế.

**→ [Liên hệ tư vấn điều độ sản xuất](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize có phải hệ thống APS không?**
Không. **Rhize** cung cấp dữ liệu thực thi và cơ chế chia lệnh; thuật toán tối ưu lịch phức tạp vẫn thuộc về APS chuyên dụng. Hai bên bổ sung cho nhau.

**Chưa có ERP thì dùng được không?**
Được. Lệnh sản xuất có thể nhập trực tiếp hoặc từ file. Nhưng khi đó phần kế hoạch vật tư vẫn phải quản lý ở nơi khác.

**Có tự động điều độ tối ưu không?**
Nền tảng cung cấp dữ liệu và điều phối; quy tắc điều độ được cài trong workflow theo đặc thù nhà máy. Bài toán tối ưu phức tạp nên dùng APS.

**Điều độ viên có bị thay thế không?**
Không. Hệ thống lo phần dữ liệu và kiểm tra điều kiện; điều độ vẫn là việc của con người; quyết định khi có xung đột vẫn cần con người — nhưng quyết định dựa trên dữ liệu thay vì phỏng đoán.

**Bao lâu thì thấy hiệu quả?**
Việc kiểm tra điều kiện trước khi chạy cho kết quả gần như ngay lập tức. Phần điều độ theo năng lực thật cần vài tháng dữ liệu để đủ tin cậy.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-tich-hop-erp/, /rhize-oee/, /rhize-quan-ly-kho-vat-tu/, /lien-he/. -->
