<!--
LOẠI TRANG : Bài ứng dụng (satellite) — Giải pháp + thương mại
URL SLUG   : /rhize-truy-xuat-nguon-goc/
TỪ KHÓA    : truy xuất | rhize track and trace | truy xuất nguồn gốc | genealogy sản xuất | truy vết lô hàng | thu hồi sản phẩm | truy xuất chuỗi cung ứng
INTENT     : Giải pháp + thương mại
TRẠNG THÁI : Sẵn đăng. Yêu cầu truy xuất theo ngành và thị trường xuất khẩu cần đối chiếu quy định hiện hành.
-->

TITLE TAG   : Rhize Track & Trace – Truy Xuất Nguồn Gốc Trong Phút
META (154)  : Rhize truy xuất nguồn gốc: truy ngược từ thành phẩm về nguyên liệu và truy xuôi khoanh vùng thu hồi trên đồ thị ISA-95. Dữ liệu cần thu thập và điều kiện.
H1          : Rhize Track & Trace – Truy Xuất Nguồn Gốc Nhanh

---

## Bài toán truy xuất nguồn gốc trong nhà máy

<!--IMG:rep-->
![Rhize Track & Trace - Truy Xuất Nguồn Gốc Nhanh](assets/diagrams/rep-graphdb.svg)


Khi có khiếu nại chất lượng hoặc yêu cầu thu hồi, nhà máy phải trả lời hai câu hỏi ngược chiều nhau trong thời gian ngắn:

- **Truy ngược (trace):** lô thành phẩm này làm từ nguyên liệu lô nào, chạy trên máy nào, ca nào, thông số ra sao?
- **Truy xuôi (track):** lô nguyên liệu có vấn đề này đã đi vào những lô thành phẩm nào, đã xuất cho ai?

Với hồ sơ giấy và Excel, câu trả lời thường mất **vài ngày**. Trong thời gian đó, phạm vi thu hồi phải mở rộng theo nguyên tắc an toàn — thu hồi thừa rất nhiều so với mức cần thiết.

**Rhize track and trace** rút thời gian này xuống mức **phút**, vì truy xuất nguồn gốc bản chất là **bài toán duyệt đồ thị**, và dữ liệu đã nằm sẵn dưới dạng đồ thị trong [Rhize DB](/rhize-db-graph-database/).

> **Cần rút ngắn thời gian truy xuất?** Gửi quy trình hiện tại → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-graph.svg)


---

## Truy xuất nguồn gốc ghi nhận những liên kết nào?

| Liên kết | Nguồn dữ liệu | Ghi nhận khi nào |
|---|---|---|
| Thành phẩm ← bán thành phẩm | Sự kiện công đoạn | Mỗi lần chuyển công đoạn |
| Bán thành phẩm ← nguyên liệu | Quét mã lô, cân | Khi nạp liệu |
| Lô ← thiết bị đã chạy | Model + sự kiện | Liên tục |
| Lô ← người vận hành | Đăng nhập, xác nhận | Theo ca, theo thao tác |
| Lô ← thông số quá trình | PLC/SCADA | Liên tục |
| Lô ← kết quả kiểm | LIMS, QC | Khi có kết quả |
| Lô → khách hàng, lô xuất | ERP, kho | Khi xuất hàng |

Mắt xích yếu nhất ở hầu hết nhà máy là **dòng thứ hai**: thời điểm nạp nguyên liệu vào máy. Nếu công nhân đổ nguyên liệu mà không quét mã lô, toàn bộ chuỗi truy xuất đứt tại đó — không phần mềm nào cứu được.

---

## Truy xuất trên đồ thị hoạt động thế nào?

Mỗi lô là một **nút**; mỗi lần nguyên liệu đi vào một mẻ là một **cạnh**. Truy xuất chỉ là duyệt các cạnh:

| Loại truy vấn | Cách duyệt | Kết quả |
|---|---|---|
| **Truy ngược 1 cấp** | Đi ngược cạnh "được làm từ" | Danh sách lô nguyên liệu trực tiếp |
| **Truy ngược nhiều cấp** | Duyệt đệ quy tới nguyên liệu gốc | Cây genealogy đầy đủ |
| **Truy xuôi** | Đi xuôi cạnh từ lô nguyên liệu | Mọi lô thành phẩm bị ảnh hưởng |
| **Truy theo thiết bị** | Từ nút equipment ra các lô | Mọi lô đã chạy trên máy đó |
| **Truy theo con người** | Từ nút personnel ra các lô | Mọi lô có người đó tham gia |

Ba loại truy vấn cuối là thứ mà hồ sơ giấy gần như không làm được. Khi phát hiện một máy bị lệch hiệu chuẩn, câu hỏi "những lô nào đã chạy trên máy này từ lần hiệu chuẩn trước" phải trả lời được ngay — nếu không, phạm vi thu hồi lại phải mở rộng theo phỏng đoán.

---

## So sánh các cách truy xuất

| Tiêu chí | Hồ sơ giấy | Excel tổng hợp | Phần mềm truy xuất riêng | **Rhize** |
|---|---|---|---|---|
| Thời gian truy ngược | Ngày | Giờ | Phút | **Phút** |
| Truy xuôi (khoanh vùng thu hồi) | Rất khó | Khó | Có | **Có** |
| Truy theo thiết bị, con người | Không | Không | Hạn chế | **Có** |
| Kèm thông số quá trình | Không | Không | Hạn chế | **Có** |
| Dùng chung dữ liệu với OEE, chất lượng | Không | Không | Không | **Có** |
| Chi phí mở rộng thêm dây chuyền | Tuyến tính | Tuyến tính | Theo license | **Nhân bản model** |

| Loại truy xuất | Câu hỏi thực tế | Thời gian mong đợi |
|---|---|---|
| Truy ngược | Lô này làm từ nguyên liệu nào | Vài phút |
| Truy xuôi | Lô nguyên liệu lỗi đã vào những lô nào | Vài phút |
| Theo thiết bị | Máy lệch hiệu chuẩn đã chạy lô nào | Vài phút |
| Theo con người | Ca đó ai đứng máy | Vài phút |
| Ra ngoài nhà máy | Đã xuất cho khách nào | Ghép với dữ liệu ERP |

---

## Ứng dụng theo ngành tại Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Thuỷ sản, nông sản xuất khẩu:** thị trường EU, Nhật, Mỹ yêu cầu truy xuất tới lô nguyên liệu và điều kiện bảo quản.
- **Thực phẩm – đồ uống:** khoanh vùng thu hồi chính xác giúp giảm chi phí và tổn thất thương hiệu. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Dược phẩm:** genealogy đầy đủ là thành phần bắt buộc của hồ sơ lô. Xem [batch record điện tử](/rhize-batch-record-dien-tu/).
- **Điện tử, linh kiện ô tô:** truy xuất theo serial tới từng linh kiện và máy gia công. Xem [sản xuất rời rạc](/rhize-san-xuat-roi-rac-serial/).

---

## Điều kiện để truy xuất chạy được

| Điều kiện | Vì sao cần | Nếu thiếu thì sao |
|---|---|---|
| **Mã lô duy nhất, in/dán được** | Định danh nút trong đồ thị | Không ghép được liên kết |
| **Thiết bị quét tại điểm nạp liệu** | Ghi nhận cạnh nguyên liệu → mẻ | Chuỗi đứt tại công đoạn đó |
| **Model ISA-95 đúng thực tế** | Gắn ngữ cảnh chính xác | Truy xuất sai địa chỉ |
| **Đồng bộ thời gian** | Xác định lô nào đang chạy | Ghép nhầm dữ liệu giữa các lô |
| **Kỷ luật vận hành** | Người thao tác quét đúng | Dữ liệu đẹp nhưng sai sự thật |

Dòng cuối cùng là rủi ro lớn nhất và không giải được bằng công nghệ. Nếu quy trình quét mã làm chậm công nhân, họ sẽ bỏ qua. Thiết kế thao tác **nhanh hơn cách cũ** là điều kiện sống còn của mọi hệ thống truy xuất.

---

<a name="bao-gia"></a>
## Nhận tư vấn hệ thống truy xuất nguồn gốc

Gửi cho chúng tôi: **sơ đồ công đoạn · cách đang đánh mã lô · điểm nạp nguyên liệu · yêu cầu truy xuất từ khách hàng/thị trường · thời gian truy xuất hiện tại.**

Chúng tôi chỉ ra các điểm đứt chuỗi, đề xuất thiết bị định danh cần bổ sung và thiết kế mô hình genealogy.

**→ [Liên hệ tư vấn truy xuất nguồn gốc](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Truy xuất được bao nhiêu cấp?**
Về nguyên tắc là không giới hạn, vì đồ thị duyệt được nhiều cấp. Giới hạn thực tế nằm ở chỗ dữ liệu có được ghi nhận đầy đủ ở mọi công đoạn hay không.

**Nguyên liệu đổ liên tục (bồn, silo) thì truy xuất kiểu gì?**
Với quá trình liên tục, truy xuất theo **khoảng thời gian** và mô hình trộn lẫn thay vì theo lô rời rạc. Cần thiết kế quy ước riêng và thống nhất với QA.

**Có cần đầu tư mã vạch, RFID không?**
Cần phương tiện định danh ở các điểm chuyển giao. Mã vạch/QR thường đủ và rẻ; RFID hợp lý khi môi trường bẩn, ướt hoặc cần quét nhanh không tiếp xúc.

**Dữ liệu quá khứ có truy xuất được không?**
Chỉ từ thời điểm hệ thống bắt đầu ghi nhận liên kết. Dữ liệu cũ trong historian không có thông tin lô nên không dựng lại được genealogy.

**Truy xuất có làm chậm sản xuất không?**
Nếu thiết kế đúng thì không — thao tác quét chỉ mất vài giây. Nếu thiết kế bắt công nhân nhập tay nhiều trường, hệ thống sẽ bị bỏ qua trong thực tế.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-db-graph-database/, /rhize-batch-record-dien-tu/, /rhize-nganh-thuc-pham-do-uong/, /lien-he/. -->
