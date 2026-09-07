<!--
LOẠI TRANG : Bài kỹ thuật (satellite) — Kỹ thuật + giải pháp
URL SLUG   : /rhize-isa-95/
TỪ KHÓA    : isa-95 | rhize isa-95 | isa-95 là gì | iec 62264 | mô hình dữ liệu isa 95 | ontology sản xuất | phân cấp thiết bị isa-95
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Nội dung ISA-95 theo chuẩn công khai ANSI/ISA-95 – IEC 62264; cách hiện thực hoá đối chiếu tài liệu Rhize.
-->

TITLE TAG   : Rhize ISA-95 – Mô Hình Dữ Liệu Chuẩn Cho Nhà Máy
META (154)  : Rhize ISA-95: mô hình dữ liệu chuẩn IEC 62264 trong Manufacturing Data Hub. Phân cấp thiết bị, vật tư, nhân sự, công thức và cách dùng để truy xuất, tính OEE.
H1          : Rhize ISA-95 – Mô Hình Dữ Liệu Chuẩn Nhà Máy

---

## ISA-95 là gì và vì sao Rhize chọn chuẩn này?

<!--IMG:rep-->
![Rhize ISA-95 - Mô Hình Dữ Liệu Chuẩn Nhà Máy](assets/diagrams/rep-isa95.svg)


**ISA-95** (chuẩn quốc tế tương đương **IEC 62264**) mô tả cách hệ thống doanh nghiệp và hệ thống điều khiển sản xuất trao đổi dữ liệu với nhau. Chuẩn này ra đời để giải một vấn đề rất cũ: mỗi nhà máy, mỗi nhà cung cấp phần mềm lại gọi cùng một thứ bằng một cái tên khác nhau.

**Rhize ISA-95** không phải một tuỳ chọn cấu hình — mô hình dữ liệu của **Rhize** được xây **trực tiếp trên schema ISA-95**, chủ yếu từ **Part 2** (mô hình phân cấp thiết bị theo vai trò và các mô hình tài nguyên). Nói cách khác, cơ sở dữ liệu đã "biết" thế nào là một work unit, một material lot, một operations definition ngay từ lúc cài.

Hệ quả thực tế: hai nhà máy khác nhau, cùng dựng model theo **ISA-95**, có thể dùng chung một truy vấn OEE, chung một báo cáo truy xuất, chung một workflow. Đây là điều không thể làm được với tích hợp point-to-point.

> **Cần dựng model ISA-95 cho nhà máy?** Gửi sơ đồ dây chuyền → [Nhận tư vấn mô hình hoá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-isa95.svg)


---

## Phân cấp thiết bị theo ISA-95 trong Rhize

Trục xương sống của **Rhize ISA-95** là cây thiết bị theo vai trò. Mỗi sự kiện trong hệ thống đều móc vào một nút của cây này.

| Cấp | Tên chuẩn | Ví dụ nhà máy Việt Nam |
|---|---|---|
| 1 | **Enterprise** | Tập đoàn |
| 2 | **Site** | Nhà máy Hải Phòng |
| 3 | **Area** | Khu chiết rót |
| 4 | **Work center** | Dây chuyền 3 |
| 5 | **Work unit** | Máy chiết, máy dán nhãn, máy đóng thùng |

Nhiều nhà máy dựng cây này lần đầu mới phát hiện ra mình chưa từng có một danh mục thiết bị thống nhất: bảo trì gọi máy là "chiết 3", sản xuất gọi là "line C", ERP ghi mã tài sản khác hẳn. **ISA-95** ép việc hợp nhất ba cách gọi đó lại — và đó là giá trị đầu tiên thu được, trước cả khi lấy được dữ liệu.

---

## Bốn mô hình tài nguyên của ISA-95

| Mô hình | Định nghĩa (definition) | Thực thể (actual) | Dùng để làm gì |
|---|---|---|---|
| **Equipment** | Loại thiết bị, năng lực | Máy cụ thể, trạng thái | Gắn ngữ cảnh, tính OEE |
| **Material** | Mã vật tư, quy cách | Lô, sublot, vị trí | Truy xuất nguồn gốc |
| **Personnel** | Vai trò, kỹ năng | Người, ca, chứng chỉ | Ghi nhận trách nhiệm, tuân thủ |
| **Physical asset** | Loại tài sản | Tài sản có số hiệu | Quản lý thiết bị đo, hiệu chuẩn |

Sự tách đôi **definition / actual** là chi tiết dễ bị bỏ qua nhưng quan trọng. "Bột mì loại A" là *definition*; "lô NL-2026-118, 1.200 kg, nhập ngày 3/9" là *actual*. Truy xuất nguồn gốc chỉ chạy được khi hệ thống ghi đúng *actual*.

---

## Rhize ISA-95 mô hình hoá công việc thế nào?

Phần **models of work** của **ISA-95** mô tả vòng đời một mệnh lệnh sản xuất, từ định nghĩa tới kết quả.

| Đối tượng | Trả lời câu hỏi | Nguồn dữ liệu điển hình |
|---|---|---|
| **Operations definition** | Làm cái gì, theo công thức nào | Recipe, BOM, quy trình |
| **Operations schedule** | Làm khi nào, ở đâu, bao nhiêu | ERP đẩy xuống |
| **Job order** | Lệnh cụ thể xuống work center | Rhize sinh hoặc nhận từ ERP |
| **Job response** | Đã làm được gì | PLC, cân, QC, thao tác viên |
| **Operations performance** | Tổng kết so với kế hoạch | Tổng hợp từ job response |

Khi năm đối tượng này đầy đủ, những câu hỏi vốn phải mở nhiều hệ thống mới trả lời được trở thành **một truy vấn GraphQL**: lệnh nào chạy chậm, chậm ở work unit nào, lúc đó đang dùng lô nguyên liệu nào, ai đứng máy.

---

## So sánh mô hình ISA-95 với cách làm tự phát

| Tiêu chí | Model tự đặt tên | **Rhize ISA-95** |
|---|---|---|
| Thời gian dựng ban đầu | Nhanh | Chậm hơn |
| Dùng lại giữa các nhà máy | Gần như không | Nhân bản được |
| Ghép với ERP/MES khác | Phải ánh xạ thủ công | Có B2MML làm cầu nối |
| Tuyển người biết sẵn | Khó | Có tài liệu chuẩn công khai |
| Rủi ro khi đổi nhân sự | Cao — kiến thức trong đầu người | Thấp — mô tả theo chuẩn |
| Kiểm toán, tuân thủ | Phải giải thích lại | Nói cùng ngôn ngữ với auditor |

Chi phí thật của model tự phát không xuất hiện ở dây chuyền đầu tiên, mà ở dây chuyền thứ ba — khi phát hiện không có gì dùng lại được.

---

## Ứng dụng mô hình ISA-95 tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Dược phẩm:** ISA-95 gắn sẵn personnel và physical asset, phục vụ yêu cầu ai làm – thiết bị nào – hiệu chuẩn còn hạn không. Xem [ngành dược phẩm](/rhize-nganh-duoc-pham/).
- **Thực phẩm:** material lot và sublot cho phép truy ngược từ thùng thành phẩm về lô nguyên liệu trong vài phút. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Điện tử:** physical asset gắn serial thành phẩm với máy và thông số gia công. Xem [sản xuất rời rạc](/rhize-san-xuat-roi-rac-serial/).
- **Đa nhà máy:** dựng model một lần ở nhà máy đầu, nhân bản sang các nhà máy sau, báo cáo tập đoàn tự động khớp nhau.

| Bước dựng model ISA-95 | Việc cụ thể | Hay vướng ở đâu |
|---|---|---|
| 1. Cây thiết bị | Enterprise → site → area → work center → unit | Ba phòng ban gọi máy ba tên khác nhau |
| 2. Danh mục vật tư | Definition và lot theo ISA-95 | Mã vật tư xưởng khác mã ERP |
| 3. Nhân sự, tài sản | Vai trò, thiết bị đo, hiệu chuẩn | Chưa có danh mục thiết bị đo |
| 4. Công thức | Operations definition kèm giới hạn | Giới hạn thông số chưa được số hoá |
| 5. Ánh xạ tag | Nối tag PLC vào work unit | Tên tag đặt tuỳ hứng |

---

<a name="bao-gia"></a>
## Nhận tư vấn mô hình hoá ISA-95

Gửi cho chúng tôi: **sơ đồ dây chuyền · danh mục thiết bị hiện có · cách đang đặt mã vật tư · hệ thống ERP đang dùng · yêu cầu tuân thủ (nếu có).**

Chúng tôi sẽ phác cây thiết bị theo **ISA-95**, chỉ ra chỗ dữ liệu hiện tại còn thiếu và ước lượng khối lượng mô hình hoá.

**→ [Liên hệ tư vấn mô hình ISA-95](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**ISA-95 và IEC 62264 có khác nhau không?**
Về nội dung là một. **ISA-95** là tên chuẩn của ISA (Mỹ), **IEC 62264** là bản quốc tế tương ứng. Tài liệu kỹ thuật hay dùng lẫn cả hai tên.

**Nhà máy nhỏ có cần ISA-95 không?**
Nếu chỉ có một dây chuyền và không có ý định mở rộng, model tự đặt vẫn chạy. Nhưng ngay khi có nhà máy thứ hai, hoặc phải trả lời auditor, **ISA-95** tiết kiệm hơn nhiều.

**Rhize dùng phần nào của ISA-95?**
Mô hình dữ liệu lấy chủ yếu từ **Part 2** — phân cấp thiết bị theo vai trò và các mô hình tài nguyên; phần trao đổi giao dịch tham chiếu **B2MML**. Xem [Rhize và B2MML](/rhize-b2mml/).

**Mô hình hoá ISA-95 mất bao lâu?**
Với một dây chuyền có sơ đồ rõ ràng, thường tính bằng tuần. Phần lâu nhất không phải nhập model mà là **thống nhất danh mục** giữa sản xuất, bảo trì và ERP.

**Đã có model riêng rồi thì chuyển sang ISA-95 thế nào?**
Ánh xạ dần: giữ hệ thống cũ chạy, dựng model **ISA-95** song song cho một dây chuyền, so kết quả, rồi chuyển. Không nên chuyển đổi một lần toàn nhà máy.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /manufacturing-data-hub-la-gi/, /rhize-b2mml/, /rhize-truy-xuat-nguon-goc/, /lien-he/. -->
