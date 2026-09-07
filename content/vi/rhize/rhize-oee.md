<!--
LOẠI TRANG : Bài ứng dụng (satellite) — Giải pháp + thương mại
URL SLUG   : /rhize-oee/
TỪ KHÓA    : oee | rhize oee | tính oee | oee là gì | hiệu suất thiết bị tổng thể | phân tích dừng máy | quản lý hiệu suất sản xuất
INTENT     : Giải pháp + thương mại
TRẠNG THÁI : Sẵn đăng. Công thức OEE theo chuẩn phổ biến; cách tính chi tiết cần thống nhất với từng nhà máy.
-->

TITLE TAG   : Rhize OEE – Tính Hiệu Suất Thiết Bị Từ Dữ Liệu Thật
META (154)  : Rhize OEE: tính hiệu suất thiết bị tổng thể từ sự kiện có ngữ cảnh ISA-95 thay vì ước lượng. Công thức, dữ liệu cần thu thập, phân tích dừng máy và lỗi hay gặp.
H1          : Rhize OEE – Hiệu Suất Thiết Bị Từ Dữ Liệu Thật

---

## Vì sao số OEE của nhiều nhà máy không đáng tin?

<!--IMG:rep-->
![Rhize OEE - Hiệu Suất Thiết Bị Từ Dữ Liệu Thật](assets/diagrams/rep-analytics.svg)


**OEE (Overall Equipment Effectiveness)** là chỉ số quen thuộc, nhưng ở phần lớn nhà máy Việt Nam nó được tính từ **sổ ghi tay và Excel**. Hệ quả là ba vấn đề lặp đi lặp lại:

- **Dừng ngắn không được ghi.** Những lần dừng 30 giây đến 2 phút — kẹt phôi, chỉnh nhẹ — không ai chép vào sổ. Cộng lại chúng thường chiếm nhiều thời gian hơn cả sự cố lớn.
- **Lý do dừng ghi tuỳ hứng.** Cùng một sự cố, ca sáng ghi "lỗi máy", ca chiều ghi "kỹ thuật xử lý". Không tổng hợp được.
- **Mỗi dây chuyền tính một kiểu.** Không so sánh được giữa các line, càng không so sánh được giữa các nhà máy.

**Rhize OEE** giải quyết cả ba bằng cách tính từ **sự kiện có ngữ cảnh** do nền tảng ghi nhận tự động, với định nghĩa chuẩn hoá ở tầng model chứ không ở từng dây chuyền.

> **Muốn có số OEE tin được?** Gửi mô tả dây chuyền → [Nhận tư vấn OEE](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Rhize OEE tính như thế nào?

| Thành phần | Công thức | Dữ liệu Rhize lấy từ đâu |
|---|---|---|
| **Availability** | Thời gian chạy / thời gian kế hoạch | Sự kiện trạng thái máy từ PLC |
| **Performance** | Sản lượng thực / sản lượng lý thuyết | Bộ đếm + tốc độ danh định trong model |
| **Quality** | Sản phẩm đạt / tổng sản lượng | Kết quả kiểm, sự kiện phế phẩm |
| **OEE** | Availability × Performance × Quality | Tổng hợp ba thành phần |
| **TEEP** | OEE × tỷ lệ khai thác lịch | Thêm dữ liệu lịch sản xuất |

Điểm mấu chốt không nằm ở công thức — công thức ai cũng biết — mà ở **nguồn của từng con số**. Khi "thời gian chạy" lấy từ sự kiện trạng thái thật của PLC thay vì từ sổ ghi ca, con số OEE mới phản ánh đúng.

---

## Dữ liệu cần thu thập cho OEE đáng tin

| Dữ liệu | Nguồn điển hình | Vì sao cần |
|---|---|---|
| **Trạng thái máy** (chạy/dừng/chờ) | PLC qua [OPC UA](/rhize-opc-ua/) | Nền của Availability |
| **Bộ đếm sản lượng** | Cảm biến đếm, PLC | Nền của Performance |
| **Tốc độ danh định** | Model ISA-95 | Mẫu số của Performance |
| **Phế phẩm, tái chế** | QC, cân, thao tác viên | Nền của Quality |
| **Lý do dừng** | PLC alarm + xác nhận của tổ trưởng | Phân tích nguyên nhân |
| **Lịch sản xuất** | ERP qua [tích hợp ERP](/rhize-tich-hop-erp/) | Xác định thời gian kế hoạch |
| **Mã sản phẩm đang chạy** | PLC hoặc ERP | Phân tích OEE theo mặt hàng |

Dòng cuối hay bị bỏ sót. Không biết đang chạy mã nào thì OEE trung bình của dây chuyền trộn lẫn sản phẩm dễ làm và khó làm — con số ra vô nghĩa với người muốn cải tiến.

---

## Phân tích dừng máy: từ con số sang hành động

| Nhóm nguyên nhân | Ví dụ | Hướng cải tiến |
|---|---|---|
| **Sự cố thiết bị** | Hỏng vòng bi, cháy cảm biến | Bảo trì dự phòng, dự trữ vật tư |
| **Chuyển đổi** | Đổi khuôn, đổi mã hàng | SMED, gộp đơn hàng cùng loại |
| **Dừng ngắn** | Kẹt phôi, lệch nhãn | Chỉnh cơ cấu, cải tiến đồ gá |
| **Giảm tốc** | Chạy dưới tốc độ danh định | Tìm nút thắt trong chuỗi |
| **Chờ** | Thiếu nguyên liệu, chờ QC | Điều độ, [scheduling](/rhize-scheduling-lap-ke-hoach/) |
| **Chất lượng** | Phế, tái chế đầu ca | Ổn định thông số khởi động |

Nhóm **dừng ngắn** thường là phát hiện gây bất ngờ nhất khi nhà máy lần đầu có dữ liệu tự động: nó âm thầm nhưng cộng dồn lớn, và trước đó không ai nhìn thấy vì sổ ghi tay không bắt được.

---

## So sánh cách tính OEE

| Tiêu chí | Sổ tay + Excel | Phần mềm OEE đóng gói | **Rhize OEE** |
|---|---|---|---|
| Bắt được dừng ngắn | Không | Có | **Có** |
| Định nghĩa thống nhất nhiều line | Khó | Trong phạm vi phần mềm | **Chuẩn hoá theo ISA-95** |
| Gắn OEE với lô, mã hàng | Rất khó | Hạn chế | **Có sẵn** |
| Truy ngược nguyên nhân | Không | Hạn chế | **Đi theo quan hệ trong graph** |
| Mở rộng sang bài toán khác | Không | Không | **Dùng chung nền dữ liệu** |
| Độ trễ | Cuối ca / cuối tuần | Gần thời gian thực | **Thời gian thực** |

Dòng áp chót là lý do chính để chọn Data Hub thay vì phần mềm OEE riêng: cùng một dữ liệu đã thu thập, nhà máy dùng tiếp cho [truy xuất nguồn gốc](/rhize-truy-xuat-nguon-goc/), [batch record](/rhize-batch-record-dien-tu/), [quản lý chất lượng](/rhize-quan-ly-chat-luong/) mà không phải lắp thêm hệ thống.

---

## Ứng dụng theo ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-oee.svg)


- **Thực phẩm – đồ uống:** dây chuyền chiết rót tốc độ cao, dừng ngắn chiếm tỷ trọng lớn — đo được mới cải tiến được.
- **Bao bì, nhựa:** thời gian chuyển đổi khuôn là nút thắt chính; OEE theo mã hàng chỉ ra đơn nào nên gộp.
- **Dệt may, da giày:** OEE theo chuyền và theo ca giúp cân bằng năng lực giữa các chuyền.
- **Cơ khí, điện tử:** ghép OEE với dữ liệu chất lượng để tìm quan hệ giữa tốc độ chạy và tỷ lệ lỗi.

---

## Lỗi thường gặp khi triển khai OEE

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Chưa thống nhất định nghĩa đã đo | Mỗi bên một số, mất niềm tin | Chốt định nghĩa bằng văn bản trước |
| Dùng OEE để đánh giá công nhân | Số liệu bị bóp méo có chủ ý | Dùng để cải tiến quy trình, không để phạt |
| Đặt mục tiêu OEE quá cao ngay | Nản, bỏ hệ thống | Lấy 4–8 tuần đầu làm mốc nền |
| Không xác nhận lý do dừng | Phân tích rỗng | Thêm bước xác nhận nhanh cho tổ trưởng |
| So OEE giữa các ngành khác nhau | Kết luận sai | Chỉ so trong cùng loại thiết bị, sản phẩm |

Dòng thứ hai quyết định thành bại nhiều hơn mọi yếu tố kỹ thuật. Khi công nhân hiểu OEE là công cụ tìm lỗi **của quy trình**, dữ liệu sẽ trung thực; khi họ nghĩ nó là công cụ chấm điểm **con người**, số liệu sẽ bị bóp méo và hệ thống mất giá trị.

---

<a name="bao-gia"></a>
## Nhận tư vấn triển khai OEE với Rhize

Gửi cho chúng tôi: **số dây chuyền · loại thiết bị · cách đang ghi nhận dừng máy · dữ liệu sẵn có từ PLC · mục tiêu cải tiến.**

Chúng tôi đề xuất bộ dữ liệu cần thu thập, cách chuẩn hoá định nghĩa và lộ trình triển khai theo giai đoạn.

**→ [Liên hệ tư vấn OEE với Rhize](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**OEE bao nhiêu là tốt?**
Không có con số chung. Mức hợp lý phụ thuộc loại thiết bị, sản phẩm và mô hình đơn hàng. Điều đáng quan tâm là **xu hướng của chính dây chuyền đó**, không phải so với con số của ngành khác.

**Cần lắp thêm cảm biến gì để tính OEE?**
Tối thiểu cần tín hiệu trạng thái máy và bộ đếm sản lượng. Nếu PLC chưa có, thường bổ sung cảm biến đếm và [bộ chuyển đổi tín hiệu](/bo-chuyen-doi-tin-hieu-seneca/) là đủ.

**Bao lâu thì có số OEE đầu tiên?**
Với một dây chuyền có sẵn dữ liệu PLC, thường tính bằng tuần. Nhưng cần thêm 4–8 tuần chạy thật để số liệu ổn định và định nghĩa được hiệu chỉnh.

**Rhize OEE khác phần mềm OEE chuyên dụng ở điểm nào?**
Cùng cho ra OEE, nhưng **Rhize** giữ dữ liệu ở dạng có ngữ cảnh ISA-95 nên dùng tiếp được cho truy xuất, chất lượng, batch record — không phải lắp thêm hệ thống cho từng bài toán.

**Có tính OEE cho dây chuyền thủ công không?**
Được, nhưng dữ liệu phải đến từ thao tác nhập của người vận hành. Chất lượng số liệu phụ thuộc kỷ luật ghi nhận, nên thường kém tin hơn dây chuyền tự động.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-core/, /rhize-opc-ua/, /rhize-scheduling-lap-ke-hoach/, /lien-he/. -->
