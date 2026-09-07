<!--
LOẠI TRANG : Trang ngành (satellite) — Giải pháp + thương mại
URL SLUG   : /rhize-san-xuat-roi-rac-serial/
TỪ KHÓA    : serial | rhize sản xuất rời rạc | truy xuất theo serial | serialized manufacturing | mes điện tử | truy xuất linh kiện ô tô | quản lý sản xuất cơ khí
INTENT     : Giải pháp + thương mại
TRẠNG THÁI : Sẵn đăng. Yêu cầu truy xuất theo chuỗi cung ứng ô tô/điện tử cần đối chiếu tiêu chuẩn khách hàng áp dụng.
-->

TITLE TAG   : Rhize Sản Xuất Rời Rạc – Truy Xuất Theo Từng Serial
META (153)  : Rhize sản xuất rời rạc: truy xuất theo serial từng sản phẩm, gắn linh kiện với máy và thông số gia công, quản lý as-built cho điện tử, cơ khí và linh kiện ô tô.
H1          : Rhize Sản Xuất Rời Rạc – Truy Xuất Theo Serial

---

## Sản xuất rời rạc khác sản xuất theo mẻ ở đâu?

<!--IMG:rep-->
![Rhize Sản Xuất Rời Rạc - Truy Xuất Theo Serial](assets/diagrams/rep-platform.svg)


Trong sản xuất theo mẻ, đơn vị truy xuất là **lô**. Trong **sản xuất rời rạc** — điện tử, cơ khí chính xác, linh kiện ô tô — đơn vị truy xuất thường là **từng sản phẩm có serial riêng**.

Khác biệt này thay đổi bản chất bài toán dữ liệu. Thay vì "lô 5.000 sản phẩm dùng nguyên liệu lô X", câu hỏi trở thành "sản phẩm serial ABC-00417 lắp linh kiện nào, gia công trên máy nào, với thông số gì, ai kiểm".

Khối lượng liên kết vì thế lớn hơn nhiều bậc — và đây chính là loại bài toán mà **mô hình đồ thị** xử lý tự nhiên hơn hẳn bảng quan hệ. Xem [Rhize DB](/rhize-db-graph-database/).

> **Cần truy xuất tới từng serial?** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-graph.svg)


---

## Rhize hỗ trợ gì cho sản xuất rời rạc?

| Bài toán | Cách giải trong Rhize |
|---|---|
| **Hồ sơ as-built theo serial** | Mỗi serial là một nút, liên kết tới linh kiện, máy, người, thông số |
| **Truy xuất ngược khi lỗi hàng loạt** | Duyệt ngược từ linh kiện lỗi ra mọi serial bị ảnh hưởng |
| **Ghép thông số gia công với chất lượng** | Cùng một đồ thị, truy vấn theo quan hệ |
| **Kiểm soát thứ tự công đoạn** | Workflow chặn nếu bỏ qua công đoạn |
| **Quản lý dụng cụ, khuôn, đồ gá** | Physical asset gắn với từng lần gia công |
| **OEE theo máy và theo mã hàng** | Xem [Rhize OEE](/rhize-oee/) |

Dòng thứ tư đáng chú ý với ngành ô tô và điện tử: **poka-yoke ở tầng dữ liệu**. Nếu một sản phẩm chưa qua trạm kiểm 3, hệ thống không cho nó vào trạm 4 — chặn lỗi bằng quy trình chứ không bằng nhắc nhở.

---

## Hồ sơ as-built theo serial gồm những gì?

| Thành phần | Nội dung | Nguồn |
|---|---|---|
| **Danh sách linh kiện thực lắp** | Mã, lô, nhà cung cấp | Quét mã tại trạm lắp |
| **Máy và trạm đã đi qua** | Thứ tự, thời gian | Sự kiện từ thiết bị |
| **Thông số gia công** | Lực siết, nhiệt độ, dòng hàn | PLC qua [OPC UA](/rhize-opc-ua/) |
| **Dụng cụ, khuôn đã dùng** | Mã dụng cụ, số lần đã dùng | Physical asset |
| **Kết quả kiểm từng trạm** | Đạt/không, giá trị đo | Thiết bị kiểm, nhập có kiểm soát |
| **Người thực hiện** | Theo trạm, theo ca | Đăng nhập, xác nhận |

Hồ sơ **as-built** khác **as-designed** ở chỗ nó ghi thứ **thực sự đã lắp**, không phải thứ **lẽ ra phải lắp**. Với ngành ô tô, đây là yêu cầu bắt buộc khi có triệu hồi.

---

## Truy xuất serial khi phát hiện linh kiện lỗi

| Bước | Câu hỏi | Cách trả lời trong Rhize |
|---|---|---|
| 1 | Lô linh kiện nào bị nghi ngờ | Từ thông báo nhà cung cấp |
| 2 | Những serial nào đã lắp lô đó | Duyệt xuôi từ nút lô linh kiện |
| 3 | Trong số đó, đã xuất cho ai | Ghép với dữ liệu xuất hàng từ ERP |
| 4 | Còn bao nhiêu trong kho, trên chuyền | Trạng thái hiện tại của từng serial |
| 5 | Có dấu hiệu bất thường ở thông số không | Truy vấn thông số của các serial đó |

Bước 5 là thứ tạo khác biệt về chi phí: nếu dữ liệu cho thấy **chỉ những serial gia công trong một khoảng thời gian nhất định** có thông số bất thường, phạm vi triệu hồi thu hẹp rất nhiều so với thu hồi toàn bộ lô linh kiện.

---

## So sánh cách quản lý truy xuất rời rạc

| Tiêu chí | Sổ + Excel theo lô | Phần mềm truy xuất riêng | **Rhize** |
|---|---|---|---|
| Mức chi tiết | Theo lô | Theo serial | **Theo serial** |
| Ghép với thông số gia công | Không | Hạn chế | **Có, cùng đồ thị** |
| Truy ngược nhiều cấp linh kiện | Rất khó | Hạn chế | **Duyệt đồ thị** |
| Chặn sai thứ tự công đoạn | Không | Tuỳ hệ | **Workflow** |
| Dùng chung dữ liệu với OEE | Không | Không | **Có** |
| Mở rộng thêm dây chuyền | Làm lại | Theo license | **Nhân bản model** |

---

## Ứng dụng theo nhóm ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Linh kiện ô tô, xe máy:** khách hàng OEM yêu cầu truy xuất as-built và khả năng khoanh vùng triệu hồi.
- **Điện tử, PCB:** ghép dữ liệu SMT, AOI, ICT theo serial để phân tích nguyên nhân lỗi.
- **Cơ khí chính xác:** gắn thông số CNC và dụng cụ với từng chi tiết, phát hiện lệch do mòn dao.
- **Thiết bị gia dụng:** hồ sơ as-built phục vụ bảo hành và xử lý khiếu nại.
- **Gia công xuất khẩu:** đáp ứng yêu cầu dữ liệu của khách hàng nước ngoài — xem [B2MML](/rhize-b2mml/).

---

## Điều kiện triển khai

| Điều kiện | Vì sao cần | Nếu thiếu |
|---|---|---|
| **Đánh serial được ở đầu chuyền** | Tạo nút gốc cho mọi liên kết | Không truy xuất theo serial được |
| **Thiết bị quét tại mỗi trạm** | Ghi nhận sản phẩm qua trạm | Đứt chuỗi tại trạm đó |
| **Linh kiện có mã lô của nhà cung cấp** | Truy ngược ra ngoài nhà máy | Chỉ truy xuất được nội bộ |
| **PLC cung cấp thông số gia công** | Ghép thông số với serial | Chỉ có dữ liệu đạt/không đạt |
| **Model ISA-95 đúng cấu trúc chuyền** | Gắn ngữ cảnh chính xác | Dữ liệu sai địa chỉ |

Với dây chuyền tốc độ cao, thời gian quét ở mỗi trạm là ràng buộc thật. Nên tính vào nhịp chuyền ngay từ khâu thiết kế, không lắp thêm sau khi chuyền đã cân bằng.

---

<a name="bao-gia"></a>
## Nhận tư vấn truy xuất theo serial

Gửi cho chúng tôi: **sơ đồ chuyền và các trạm · cách đang đánh serial · thiết bị quét hiện có · yêu cầu truy xuất từ khách hàng · nhịp chuyền.**

Chúng tôi thiết kế mô hình as-built, chỉ ra điểm ghi nhận cần bổ sung và đánh giá tác động lên nhịp chuyền.

**→ [Liên hệ tư vấn sản xuất rời rạc](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Sản phẩm nhỏ, giá rẻ có cần truy xuất theo serial không?**
Không phải lúc nào cũng cần. Có thể truy xuất theo **lô nhỏ** hoặc theo khoảng thời gian. Mức chi tiết nên chọn theo chi phí rủi ro khi phải thu hồi.

**Dữ liệu theo serial có quá lớn không?**
Khối lượng lớn hơn quản lý theo lô, nhưng nằm trong khả năng của nền tảng. Cần ước lượng dung lượng theo sản lượng thật — xem [Rhize DB](/rhize-db-graph-database/).

**Có ghép được với hệ thống SMT, AOI sẵn có không?**
Có, qua API hoặc file xuất của các hệ thống đó. Dữ liệu được gắn vào đúng serial trong đồ thị.

**Quét mã ở mỗi trạm có làm chậm chuyền không?**
Có ảnh hưởng nhỏ và cần tính vào nhịp chuyền. Nhiều trường hợp dùng đọc mã tự động thay vì quét tay để không thêm thao tác cho công nhân.

**Bắt đầu từ đâu?**
Từ một chuyền và những trạm quan trọng nhất cho truy xuất, thay vì lắp quét ở mọi trạm ngay từ đầu.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-truy-xuat-nguon-goc/, /rhize-db-graph-database/, /rhize-oee/, /lien-he/. -->
