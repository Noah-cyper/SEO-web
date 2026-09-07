<!--
LOẠI TRANG : Bài kỹ thuật (satellite) — Kỹ thuật
URL SLUG   : /rhize-b2mml/
TỪ KHÓA    : b2mml | rhize b2mml | b2mml là gì | mesa b2mml | trao đổi dữ liệu isa-95 | xml sản xuất | chuẩn tích hợp mes erp
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. B2MML là chuẩn công khai của MESA International; đối chiếu mức hỗ trợ của bản Rhize đang dùng.
-->

TITLE TAG   : Rhize B2MML – Chuẩn Trao Đổi Dữ Liệu ISA-95
META (151)  : Rhize B2MML: B2MML là gì, quan hệ với ISA-95, dùng để trao đổi dữ liệu giữa ERP, MES và Data Hub. Khi nào nên dùng B2MML và khi nào dùng GraphQL.
H1          : Rhize B2MML – Chuẩn Trao Đổi Dữ Liệu ISA-95

---

## B2MML là gì?

<!--IMG:rep-->
![Rhize B2MML - Chuẩn Trao Đổi Dữ Liệu ISA-95](assets/diagrams/rep-isa95.svg)


**B2MML** (Business To Manufacturing Markup Language) là bộ lược đồ **XML** hiện thực hoá chuẩn **ISA-95**, do tổ chức **MESA International** xây dựng và công bố. Nói ngắn gọn: **ISA-95 định nghĩa khái niệm, B2MML định nghĩa cách viết chúng ra để hai hệ thống trao đổi với nhau**.

Vì sao điều này quan trọng? ISA-95 mô tả "material lot có những thuộc tính gì" nhưng không quy định định dạng file. Không có định dạng chung thì mỗi lần nối hai hệ thống lại phải thoả thuận cấu trúc riêng. **B2MML** loại bỏ vòng thương lượng đó.

Trong bối cảnh **Rhize B2MML**, chuẩn này đóng vai **cầu nối với hệ thống bên ngoài** — ERP, MES của nhà cung cấp khác, hệ thống của khách hàng hoặc tập đoàn mẹ.

> **Cần trao đổi dữ liệu chuẩn với hệ thống của tập đoàn?** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-isa95.svg)


---

## B2MML bao gồm những lược đồ nào?

| Nhóm lược đồ | Nội dung | Tương ứng ISA-95 |
|---|---|---|
| **Equipment** | Thiết bị, phân cấp, năng lực | Part 2 |
| **Material** | Định nghĩa vật tư, lô, sublot | Part 2 |
| **Personnel** | Nhân sự, vai trò, kỹ năng | Part 2 |
| **Physical asset** | Tài sản vật lý, thiết bị đo | Part 2 |
| **Production schedule** | Kế hoạch sản xuất | Part 4 |
| **Production performance** | Kết quả thực hiện | Part 4 |

Hai nhóm cuối là phần được dùng nhiều nhất trong tích hợp ERP: ERP gửi xuống **production schedule**, nhà máy trả về **production performance**. Xem thêm [Rhize và ISA-95](/rhize-isa-95/).

---

## Khi nào dùng B2MML, khi nào dùng GraphQL?

| Tình huống | Nên dùng | Lý do |
|---|---|---|
| Ứng dụng nội bộ đọc dữ liệu | **GraphQL** | Linh hoạt, chỉ lấy trường cần |
| Dashboard, báo cáo | **GraphQL** | Truy vấn theo quan hệ |
| Trao đổi với ERP hỗ trợ B2MML | **B2MML** | Không phải thoả thuận cấu trúc |
| Gửi dữ liệu cho tập đoàn mẹ | **B2MML** | Chuẩn chung, bên nhận đọc được |
| Tích hợp với MES hãng khác | **B2MML** | Ngôn ngữ trung gian |
| Nạp dữ liệu khối lượng lớn | Tuỳ | Cân nhắc kích thước file XML |

Quy tắc thực dụng: **bên trong nhà máy dùng GraphQL, ra ngoài ranh giới tổ chức dùng B2MML**. XML dài dòng hơn nhưng bù lại bên nhận không cần biết gì về hệ thống của bạn ngoài chuẩn công khai.

---

## So sánh B2MML với các cách trao đổi khác

| Tiêu chí | File CSV tự định nghĩa | API riêng của từng hệ | **B2MML** |
|---|---|---|---|
| Bên nhận hiểu ngay | Không | Không | **Có (chuẩn công khai)** |
| Công thoả thuận ban đầu | Cao | Cao | **Thấp** |
| Diễn đạt quan hệ phức tạp | Kém | Tuỳ | **Tốt** |
| Kiểm tra tính hợp lệ | Thủ công | Tuỳ | **Theo XSD** |
| Kích thước dữ liệu | Nhỏ | Nhỏ | Lớn hơn |
| Đổi đối tác tích hợp | Làm lại | Làm lại | **Giữ nguyên** |

Dòng "kiểm tra tính hợp lệ" đáng chú ý trong ngành có yêu cầu tuân thủ: file **B2MML** kiểm tra được theo lược đồ **XSD**, nên lỗi cấu trúc lộ ra ngay khi nhận, không phải phát hiện muộn khi số liệu đã vào hệ thống.

---

## Ứng dụng B2MML tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Nhà máy thuộc tập đoàn nước ngoài:** công ty mẹ yêu cầu báo cáo sản xuất theo chuẩn; **B2MML** tránh phải viết bộ chuyển đổi riêng cho từng yêu cầu.
- **Gia công cho khách hàng lớn:** khách yêu cầu dữ liệu truy xuất theo định dạng chuẩn khi có sự cố chất lượng.
- **Nhà máy nhiều hệ thống khác hãng:** MES cũ, ERP mới, LIMS riêng — B2MML làm ngôn ngữ trung gian.
- **Chuyển đổi hệ thống:** xuất dữ liệu model theo B2MML để đưa sang nền tảng mới mà không mất cấu trúc.

Xem thêm [tích hợp ERP](/rhize-tich-hop-erp/) và [track & trace](/rhize-truy-xuat-nguon-goc/).

| Bên trao đổi | Dữ liệu gửi đi | Dữ liệu nhận về |
|---|---|---|
| ERP ↔ nhà máy | Kế hoạch sản xuất, vật tư | Kết quả thực hiện |
| Tập đoàn mẹ ← nhà máy | Báo cáo sản lượng, hiệu suất | — |
| Khách hàng ← nhà máy | Hồ sơ truy xuất khi có sự cố | — |
| MES hãng khác ↔ nhà máy | Định nghĩa công đoạn | Trạng thái thực thi |

---

## Lưu ý khi triển khai trao đổi B2MML

| Vấn đề | Hệ quả | Cách xử lý |
|---|---|---|
| Mỗi bên dùng phiên bản B2MML khác | File không đọc được | Thống nhất phiên bản trước |
| Dùng trường mở rộng tuỳ tiện | Mất tính chuẩn | Chỉ mở rộng khi thật cần, có tài liệu |
| Mã danh mục không khớp | Dữ liệu vào sai chỗ | Lập bảng ánh xạ mã hai bên |
| File quá lớn | Xử lý chậm, dễ lỗi | Chia theo lô hoặc theo khoảng thời gian |
| Không kiểm tra XSD khi nhận | Lỗi phát hiện muộn | Bắt buộc validate trước khi nạp |

---

<a name="bao-gia"></a>
## Nhận tư vấn trao đổi dữ liệu chuẩn B2MML

Gửi cho chúng tôi: **hệ thống cần trao đổi dữ liệu · yêu cầu định dạng từ đối tác/tập đoàn · loại dữ liệu (kế hoạch, kết quả, vật tư) · tần suất trao đổi.**

Chúng tôi đánh giá mức phù hợp của **B2MML**, thiết kế ánh xạ dữ liệu và workflow xuất/nhập.

**→ [Liên hệ tư vấn B2MML](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**B2MML có bắt buộc khi dùng ISA-95 không?**
Không. **ISA-95** là mô hình khái niệm; **B2MML** chỉ là một cách viết ra để trao đổi. Nội bộ có thể dùng GraphQL và vẫn đúng chuẩn ISA-95.

**B2MML có mất phí không?**
Đây là chuẩn công khai do **MESA International** phát hành. Cần đối chiếu điều kiện sử dụng hiện hành trên trang của MESA.

**XML có lỗi thời so với JSON không?**
Với trao đổi giữa các tổ chức, XML kèm XSD vẫn có lợi thế về kiểm tra tính hợp lệ. Nội bộ thì JSON/GraphQL tiện hơn.

**ERP không hỗ trợ B2MML thì sao?**
Dùng API hoặc file theo định dạng ERP hỗ trợ, và giữ B2MML cho trao đổi ra ngoài tổ chức. Xem [tích hợp ERP](/rhize-tich-hop-erp/).

**Ai chuẩn bị bảng ánh xạ mã danh mục?**
Nên do người nắm nghiệp vụ ở cả hai phía làm cùng nhau. Đây là phần tốn thời gian nhất và cũng là nơi phát sinh lỗi nhiều nhất.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-isa-95/, /rhize-tich-hop-erp/, /rhize-truy-xuat-nguon-goc/, /lien-he/. -->
