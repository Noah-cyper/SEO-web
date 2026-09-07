<!--
LOẠI TRANG : Trang sản phẩm/thương hiệu — Thương mại
URL SLUG   : /plc-mitsubishi-fx5u/
TỪ KHÓA    : fx5u | plc mitsubishi fx5u | fx5u giá | fx5u và fx3u | plc fx5u chính hãng | mở rộng io fx5u
INTENT     : Thương mại / giao dịch + kỹ thuật
TRẠNG THÁI : Sẵn đăng. Đối chiếu catalog Mitsubishi cho số I/O, mã module và phần mềm hỗ trợ trước khi chào giá.
-->

TITLE TAG   : PLC Mitsubishi FX5U – Nâng Cấp Từ FX3U, Báo Giá
META (148)  : PLC Mitsubishi FX5U: khác gì FX3U, khi nào nên nâng cấp, cách chọn số I/O và module mở rộng, phần mềm lập trình. Hàng chính hãng, CO/CQ, báo giá nhanh.
H1          : PLC Mitsubishi FX5U – Chọn Đúng Và Báo Giá

---

## PLC Mitsubishi FX5U là gì?

<!--IMG:rep-->
![PLC Mitsubishi FX5U chính hãng](assets/diagrams/rep-plc.svg)


**FX5U** là dòng PLC compact thuộc dòng **MELSEC iQ-F** của Mitsubishi Electric — thế hệ kế nhiệm của **FX3U** quen thuộc trong nhà máy Việt Nam.

Điểm khác biệt lớn nhất của **FX5U** so với đời trước nằm ở phần **truyền thông tích hợp sẵn**: cổng Ethernet có ngay trên CPU, không phải mua module rời như trên FX3U. Với nhà máy đang đi theo hướng thu thập dữ liệu và giám sát tập trung, đây là thứ tiết kiệm cả tiền lẫn không gian tủ điện.

**FX5U** giữ triết lý của dòng FX: **compact, dễ lắp DIN rail, có sẵn I/O trên thân**, mở rộng thêm bằng module cắm cạnh. Nếu chưa quen dòng FX, xem trước [PLC Mitsubishi FX3U là gì](/plc-mitsubishi-fx3u-la-gi/).

> **Cần báo giá FX5U theo số I/O cụ thể?** Gửi **số ngõ vào/ra · loại tín hiệu · yêu cầu truyền thông** → [Nhận báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-plc.svg)


---

## FX5U khác FX3U ở những điểm nào?

| Hạng mục | FX3U | **FX5U** |
|---|---|---|
| Ethernet | Cần module rời | **Tích hợp sẵn trên CPU** |
| Truyền thông nối tiếp | Qua board/module | Có sẵn cổng, mở rộng thêm được |
| Lập trình | GX Works2 | **GX Works3** (hỗ trợ nhiều ngôn ngữ hơn) |
| Xử lý lệnh | Thế hệ cũ | Nhanh hơn đáng kể |
| Analog tích hợp | Không | Một số model có sẵn |
| Chuyển chương trình cũ | — | Có công cụ chuyển đổi từ FX3U |

Cột bên phải là lý do phần lớn dự án mới chọn **FX5U** thay vì tiếp tục FX3U. Nhưng cần nói rõ: **chương trình FX3U không chạy thẳng trên FX5U** — phải chuyển đổi và kiểm thử lại. Xem [truyền thông FX5U với FX3U](/truyen-thong-fx5u-fx3u/) khi hai đời cùng tồn tại trong một hệ.

---

## Khi nào nên chọn FX5U?

| Tình huống | Nên chọn FX5U? | Lý do |
|---|---|---|
| Máy mới, cần kết nối SCADA/IoT | **Có** | Ethernet sẵn, tiết kiệm module |
| Thay thế PLC hỏng trong máy cũ | Cân nhắc | Phải chuyển chương trình, kiểm thử lại |
| Cần tốc độ xử lý cao hơn | **Có** | Chu kỳ quét nhanh hơn rõ rệt |
| Chỉ điều khiển logic đơn giản, ít điểm | Không bắt buộc | Dòng nhỏ hơn có thể đủ và rẻ hơn |
| Hệ nhiều trạm, cần mạng | **Có** | Truyền thông tích hợp thuận lợi |
| Nhà máy đã chuẩn hóa trên FX3U | Cân nhắc | Cân giữa đồng bộ vật tư và lợi ích kỹ thuật |

Sai lầm hay gặp: thay một CPU hỏng bằng **FX5U** rồi phát hiện chương trình cũ không nạp được, dây chuyền dừng thêm nhiều giờ. Khi thay khẩn cấp, nên tìm đúng đời cũ — xem [thay thế PLC/module đời cũ](/thay-the-plc-module-doi-cu/).

---

## Chọn cấu hình FX5U theo số I/O

| Bước | Việc cần làm | Lưu ý |
|---|---|---|
| 1 | Đếm ngõ vào số (nút, cảm biến ON/OFF) | Cộng 15–20% dự phòng |
| 2 | Đếm ngõ ra số và loại ngõ ra | Relay hay transistor quyết định mã CPU |
| 3 | Đếm kênh analog vào/ra | Xem [kết nối PLC với cảm biến 4-20mA](/ket-noi-plc-cam-bien-4-20ma/) |
| 4 | Xác định nhu cầu truyền thông | Ethernet, RS-485, Modbus |
| 5 | Chọn CPU FX5U phù hợp | Rồi mới tính module mở rộng |
| 6 | Kiểm tra công suất nguồn | Module mở rộng tiêu thụ từ CPU |

Chọn **ngõ ra relay hay transistor** là quyết định không đảo ngược được sau khi mua: relay chịu tải lớn nhưng chậm và có tuổi thọ cơ khí; transistor nhanh, hợp phát xung điều khiển servo/step. Chi tiết cách mở rộng: [mở rộng I/O cho PLC](/mo-rong-io-plc/).

---

## Ghép FX5U vào hệ thống nhà máy

| Thiết bị ghép với FX5U | Cách kết nối | Ghi chú |
|---|---|---|
| **HMI** | Ethernet hoặc nối tiếp | Xem [HMI là gì](/hmi-la-gi/) |
| **Biến tần** | Modbus hoặc analog | Xem [kết nối PLC – biến tần](/ket-noi-plc-bien-tan/) |
| **Cảm biến 4-20mA** | Module analog | Cần [bộ chuyển đổi tín hiệu](/bo-chuyen-doi-tin-hieu-seneca/) khi đi xa |
| **SCADA** | Ethernet | Xem [SCADA là gì](/scada-la-gi/) |
| **Remote I/O** | Mạng truyền thông | Giảm dây khi điểm đo phân tán |

Với nhà máy muốn đưa dữ liệu **FX5U** lên hệ thống phân tích, cổng Ethernet tích hợp giúp bỏ qua bước mua module truyền thông — xem thêm [PLC và IoT](/plc-va-iot/).

---

## Lỗi thường gặp trên FX5U và cách xử lý

| Hiện tượng | Nguyên nhân thường gặp | Hướng xử lý |
|---|---|---|
| Không kết nối được máy tính | Sai dải IP, tường lửa chặn | Kiểm tra IP, tắt tạm tường lửa — xem [PLC không kết nối máy tính](/plc-khong-ket-noi-may-tinh/) |
| Chương trình FX3U không nạp được | Khác nền tảng, cần chuyển đổi | Dùng công cụ chuyển đổi của GX Works3, kiểm thử lại |
| Module mở rộng không nhận | Thiếu công suất nguồn, sai cấu hình | Rà lại bảng công suất, khai báo lại phần cứng |
| Ngõ ra không tác động | Chọn nhầm loại relay/transistor | Kiểm tra mã CPU và tải thực tế |
| Nhiễu gây sai tín hiệu analog | Đi chung máng với cáp động lực | Tách máng, dùng cáp có lưới — xem [lỗi PLC do nhiễu](/loi-plc-do-nhieu/) |

---

## Mua FX5U chính hãng ở đâu

| Cam kết | Nội dung |
|---|---|
| **Nguồn hàng** | Chính hãng Mitsubishi, có CO/CQ |
| **Chứng từ** | Hóa đơn VAT đầy đủ |
| **Hỗ trợ kỹ thuật** | Tư vấn chọn CPU và module theo số I/O thực tế |
| **Hàng đời cũ** | Hỗ trợ tìm FX3U và module ngừng sản xuất |
| **Phân biệt hàng thật** | Xem [cách phân biệt PLC thật giả](/phan-biet-plc-that-gia/) |

---

<a name="bao-gia"></a>
## Nhận báo giá PLC Mitsubishi FX5U

Gửi cho chúng tôi: **số ngõ vào/ra số · số kênh analog · loại ngõ ra (relay/transistor) · yêu cầu truyền thông · số lượng · có cần module mở rộng không.**

Nếu đang nâng cấp từ FX3U, cho biết thêm **model CPU hiện tại** để chúng tôi tư vấn phương án chuyển đổi chương trình.

**→ [Liên hệ báo giá FX5U](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/topo-plc-hmi-scada.svg)

## Câu hỏi thường gặp (FAQ)

**Chương trình FX3U có chạy được trên FX5U không?**
Không chạy trực tiếp. GX Works3 có công cụ chuyển đổi, nhưng vẫn phải rà lại và kiểm thử — đặc biệt các lệnh đặc biệt và phần truyền thông.

**FX5U có sẵn Ethernet không?**
Có. Đây là khác biệt đáng giá nhất so với FX3U: kết nối HMI, SCADA hoặc máy tính lập trình không cần mua module rời.

**Nên chọn ngõ ra relay hay transistor?**
Relay khi tải lớn, đóng cắt chậm. Transistor khi cần tốc độ cao hoặc phát xung điều khiển servo/step. Chọn sai thì phải đổi cả CPU, nên cần xác định trước.

**FX5U dùng phần mềm lập trình nào?**
**GX Works3**. Dự án cũ trên GX Works2 cần chuyển đổi sang, không mở trực tiếp được.

**Có hàng chính hãng và CO/CQ không?**
Có. Hàng chính hãng kèm CO/CQ và hóa đơn VAT; hỗ trợ chọn cấu hình theo số I/O và nhu cầu truyền thông thực tế.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /plc-mitsubishi-fx3u-la-gi/, /mo-rong-io-plc/, /ket-noi-plc-bien-tan/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
