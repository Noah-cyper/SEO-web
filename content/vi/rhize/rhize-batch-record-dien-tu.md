<!--
LOẠI TRANG : Bài ứng dụng (satellite) — Giải pháp + thương mại
URL SLUG   : /rhize-batch-record-dien-tu/
TỪ KHÓA    : batch record | batch record điện tử | hồ sơ lô điện tử | ebr sản xuất | rhize batch record | review by exception | hồ sơ lô thời gian thực
INTENT     : Giải pháp + thương mại
TRẠNG THÁI : Sẵn đăng. Yêu cầu tuân thủ (GMP, 21 CFR Part 11, Annex 11) cần đối chiếu với quy định hiện hành và bộ phận QA của nhà máy.
-->

TITLE TAG   : Batch Record Điện Tử Với Rhize – Hồ Sơ Lô Realtime
META (155)  : Batch record điện tử với Rhize: hồ sơ lô hình thành ngay trong lúc chạy thay vì tổng hợp cuối mẻ. Dữ liệu cần thu thập, review by exception và yêu cầu tuân thủ.
H1          : Batch Record Điện Tử Với Rhize – Hồ Sơ Lô Realtime

---

## Batch record điện tử là gì và vì sao cần realtime?

<!--IMG:rep-->
![Batch Record Điện Tử Với Rhize - Hồ Sơ Lô Realtime](assets/diagrams/rep-app.svg)


**Batch record** (hồ sơ lô) là tập hợp toàn bộ bằng chứng về việc một mẻ sản phẩm đã được sản xuất đúng quy trình: thông số quá trình, nguyên liệu đã dùng, thiết bị đã chạy, người thực hiện, kết quả kiểm và các sai lệch phát sinh.

Ở nhiều nhà máy, batch record vẫn là một **tập giấy**, và quy trình quen thuộc là: chạy mẻ → ghi chép → cuối mẻ gom lại → QA rà soát → phát hiện thiếu chữ ký hoặc số liệu → đi tìm người ghi → chậm xuất lô vài ngày.

**Batch record điện tử** với **Rhize** đảo ngược trình tự: batch record **hình thành ngay trong lúc mẻ đang chạy**. Mỗi thông số, mỗi thao tác xác nhận, mỗi lần đổi lô nguyên liệu được ghi vào đồ thị dữ liệu ngay khi xảy ra. Đến cuối mẻ, batch record đã sẵn — việc còn lại chỉ là rà soát các sai lệch.

> **Cần rút ngắn thời gian xuất lô?** Gửi quy trình hiện tại → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Batch record điện tử ghi nhận những dữ liệu gì?

| Nhóm dữ liệu | Nguồn | Đối tượng ISA-95 |
|---|---|---|
| **Thông số quá trình** | PLC/SCADA qua [OPC UA](/rhize-opc-ua/) | Job response |
| **Nguyên liệu đã dùng** | Quét mã lô, cân | Material actual |
| **Thiết bị đã chạy** | Model + sự kiện trạng thái | Equipment actual |
| **Người thực hiện, người duyệt** | Đăng nhập, xác nhận điện tử | Personnel actual |
| **Thiết bị đo, hiệu chuẩn** | Danh mục tài sản | Physical asset actual |
| **Kết quả kiểm** | LIMS, nhập tay có kiểm soát | Test result |
| **Sai lệch và xử lý** | Sự kiện + workflow phê duyệt | Deviation |

Bốn dòng đầu của batch record **tự động** — không cần ai chép. Ba dòng cuối cần con người, nhưng được ghi nhận qua thao tác có kiểm soát trong workflow chứ không phải ký vào giấy.

---

## Batch record hình thành như thế nào trong Rhize

| Giai đoạn mẻ | Việc hệ thống làm | Thành phần Rhize |
|---|---|---|
| **Chuẩn bị** | Kiểm nguyên liệu còn hạn, thiết bị đã hiệu chuẩn | [BPMN workflow](/rhize-bpmn-workflow/) |
| **Bắt đầu** | Ghi lệnh, công thức, người vận hành | Rhize DB |
| **Đang chạy** | Ghi liên tục thông số, đổi lô, sự kiện | [Rhize Agent](/rhize-agent-ket-noi/) + Core |
| **Sai lệch** | Phát hiện vượt ngưỡng, mở quy trình xử lý | [Rhize Core](/rhize-core/) + workflow |
| **Kết thúc** | Tổng hợp, gắn kết quả kiểm | Rhize DB |
| **Rà soát & duyệt** | QA xem sai lệch, ký điện tử | Workflow user task |

Bước "chuẩn bị" trong batch record là nơi hệ thống tạo ra giá trị lớn nhất mà ít người nghĩ tới: **chặn lỗi trước khi mẻ bắt đầu**. Phát hiện nguyên liệu hết hạn ở phút đầu rẻ hơn rất nhiều so với phát hiện sau khi đã đóng gói.

---

## Review by exception: chỉ xem cái bất thường

| Cách làm | QA phải xem gì | Thời gian rà soát |
|---|---|---|
| **Hồ sơ giấy** | Toàn bộ tập hồ sơ giấy, từng trang | Rất lâu |
| **Scan hồ sơ giấy** | Vẫn toàn bộ, chỉ trên màn hình | Không cải thiện nhiều |
| **EBR cơ bản** | Toàn bộ dữ liệu số | Nhanh hơn |
| **Review by exception** | **Chỉ các sai lệch được đánh dấu** | **Ngắn nhất** |

Review batch record theo kiểu **review by exception** chỉ khả thi khi hệ thống tự phát hiện được đâu là bất thường — nghĩa là phải biết **giới hạn cho phép của từng thông số theo từng công thức**. Đây chính là thứ mô hình **operations definition** trong [ISA-95](/rhize-isa-95/) mô tả sẵn.

---

## Yêu cầu tuân thủ cần chú ý

| Yêu cầu | Nội dung | Cách Rhize hỗ trợ |
|---|---|---|
| **Ghi vết kiểm toán** | Ai làm gì, khi nào, giá trị cũ/mới | Nhật ký ở tầng dữ liệu và workflow |
| **Chữ ký điện tử** | Định danh người ký, ý nghĩa chữ ký | User task + [Keycloak](/rhize-keycloak-phan-quyen/) |
| **Không sửa dữ liệu gốc** | Chỉ ghi bản hiệu chỉnh kèm lý do | Lưu bất biến, ghi bản đính chính |
| **Phân quyền** | Đúng người mới được duyệt | RBAC/ABAC/graph-based |
| **Toàn vẹn dữ liệu** | Dữ liệu đầy đủ, đúng thời điểm | Ghi tự động từ nguồn, đồng bộ NTP |

⚠️ **Cần lưu ý:** mức độ đáp ứng các quy định cụ thể (GMP, 21 CFR Part 11, EU Annex 11) phụ thuộc **cách cấu hình và quy trình vận hành của từng nhà máy**, không phải chỉ phụ thuộc phần mềm. Việc thẩm định (validation) phải do bộ phận QA của nhà máy thực hiện theo quy định hiện hành.

---

## Ứng dụng theo ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Dược phẩm:** rút ngắn thời gian xuất lô, giảm sai sót chép tay. Xem [ngành dược phẩm](/rhize-nganh-duoc-pham/).
- **Thực phẩm chức năng, mỹ phẩm:** yêu cầu batch record ngày càng chặt từ thị trường xuất khẩu.
- **Thực phẩm – đồ uống:** hồ sơ CCP theo HACCP gắn với lô. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Hoá chất:** ghi nhận thông số phản ứng và điều kiện an toàn theo mẻ.

| Mức số hoá batch record | Đặc điểm | Thời gian rà soát |
|---|---|---|
| Giấy | Ghi tay, ký tay | Dài nhất |
| Batch record scan | Lưu ảnh, vẫn đọc từng trang | Gần như không cải thiện |
| Batch record điện tử cơ bản | Dữ liệu số, nhập tay phần lớn | Ngắn hơn |
| Batch record realtime | Ghi tự động từ thiết bị | Ngắn |
| Batch record + review by exception | Chỉ xem sai lệch | Ngắn nhất |

---

## Lỗi thường gặp khi số hoá batch record

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| Số hoá nguyên xi biểu mẫu giấy | Giữ nguyên bất hợp lý cũ | Thiết kế lại theo dữ liệu sẵn có |
| Vẫn nhập tay số liệu máy đã có | Tốn công, dễ sai | Ưu tiên lấy tự động từ thiết bị |
| Không định nghĩa giới hạn thông số | Không làm được review by exception | Khai báo giới hạn trong công thức |
| Chạy song song giấy và điện tử quá lâu | Gấp đôi khối lượng, nhân viên phản ứng | Đặt mốc dừng bản giấy rõ ràng |
| Bỏ qua QA từ đầu | Làm xong không dùng được | Đưa QA vào từ giai đoạn thiết kế |

---

<a name="bao-gia"></a>
## Nhận tư vấn batch record điện tử

Gửi cho chúng tôi: **mẫu batch record đang dùng · các thông số đang ghi tay · dữ liệu sẵn có từ PLC · yêu cầu tuân thủ áp dụng · thời gian xuất lô hiện tại.**

Chúng tôi phân tích tỷ lệ dữ liệu có thể tự động hoá, thiết kế luồng phê duyệt và lộ trình chuyển đổi từ giấy sang điện tử.

**→ [Liên hệ tư vấn batch record điện tử](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Batch record điện tử có thay hoàn toàn hồ sơ giấy không?**
Về mặt kỹ thuật thì có. Nhưng việc bỏ hẳn bản giấy phải được bộ phận QA thẩm định và phù hợp quy định hiện hành áp dụng cho nhà máy.

**Bao nhiêu phần trăm dữ liệu tự động hoá được?**
Phụ thuộc mức độ tự động của dây chuyền. Thông số quá trình, thiết bị, thời gian thường tự động hoàn toàn; nguyên liệu tự động nếu có quét mã; kết quả kiểm cảm quan vẫn cần người.

**Rhize có phải hệ thống EBR chuyên dụng không?**
**Rhize** là Manufacturing Data Hub — nó cung cấp **dữ liệu, ngữ cảnh và điều phối** để dựng batch record điện tử, cùng nền dữ liệu dùng chung cho OEE, truy xuất, chất lượng.

**Chuyển đổi mất bao lâu?**
Với một dòng sản phẩm và dữ liệu PLC sẵn có, thường vài tháng tính cả thẩm định. Phần lâu nhất là **thiết kế lại biểu mẫu và thẩm định**, không phải kỹ thuật.

**Nếu mất điện hoặc mất mạng giữa mẻ thì sao?**
Cần thiết kế phương án dự phòng ngay từ đầu — ghi đệm tại chỗ, quy trình ghi tạm bằng giấy và nhập bù có kiểm soát. Đây là nội dung bắt buộc trong hồ sơ thẩm định.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-bpmn-workflow/, /rhize-nganh-duoc-pham/, /rhize-quan-ly-chat-luong/, /lien-he/. -->
