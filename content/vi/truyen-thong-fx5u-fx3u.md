<!--
LOẠI TRANG : Blog kỹ thuật — Thông tin + kỹ thuật
URL SLUG   : /truyen-thong-fx5u-fx3u/
TỪ KHÓA    : truyền thông | truyền thông fx5u fx3u | kết nối fx5u với fx3u | modbus fx5u | ethernet fx5u | nối hai plc mitsubishi
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu manual Mitsubishi cho mã module và tham số cấu hình cụ thể trước khi thi công.
-->

TITLE TAG   : Truyền Thông FX5U Với FX3U – Các Cách Kết Nối
META (150)  : Truyền thông FX5U với FX3U: chọn Modbus RTU, Ethernet hay N:N, cách đấu RS-485, tham số cần khớp và lỗi hay gặp khi hai đời PLC cùng tồn tại trong một hệ.
H1          : Truyền Thông FX5U Với FX3U – Chọn Cách Nào?

---

## Vì sao cần truyền thông giữa hai đời PLC?

<!--IMG:rep-->
![Truyền thông giữa PLC FX5U và FX3U](assets/diagrams/rep-plc.svg)


Rất ít nhà máy thay toàn bộ PLC cùng lúc. Thực tế phổ biến là **máy mới dùng FX5U, máy cũ vẫn chạy FX3U**, và đến một lúc nào đó hai đời phải nói chuyện với nhau — để đồng bộ nhịp dây chuyền, chia sẻ tín hiệu cho phép chạy, hoặc gom dữ liệu về một màn hình.

Bài toán **truyền thông** giữa hai đời này không khó, nhưng có vài điểm khác biệt dễ vướng:

- **FX5U có Ethernet tích hợp**, FX3U thì không — nên phương án **truyền thông** qua LAN chỉ đối xứng khi FX3U được bổ sung module.
- **Phần mềm khác nhau**: FX5U dùng GX Works3, FX3U dùng GX Works2 — cấu hình **truyền thông** làm ở hai nơi.
- **Cách khai báo vùng nhớ khác nhau** giữa hai thế hệ.

Xem trước [PLC Mitsubishi FX5U](/plc-mitsubishi-fx5u/) và [FX3U là gì](/plc-mitsubishi-fx3u-la-gi/).

> **Cần tư vấn phương án truyền thông cho hệ đang có?** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-plc.svg)


---

## Ba phương án truyền thông thường dùng

| Phương án | Cách làm | Ưu điểm | Hạn chế |
|---|---|---|---|
| **Modbus RTU qua RS-485** | Một PLC làm master, một làm slave | Phổ biến, dễ tìm tài liệu, rẻ | Tốc độ thấp, cần đi dây |
| **Ethernet** | Kết nối qua switch công nghiệp | Nhanh, mở rộng dễ, dùng chung hạ tầng mạng | FX3U cần module Ethernet |
| **Mạng N:N (nối tiếp)** | Chia sẻ vùng nhớ giữa các trạm FX | Cấu hình đơn giản, không cần lập trình nhiều | Giới hạn số trạm và dung lượng dữ liệu |

Lựa chọn thực dụng ở đa số dự án: nếu chỉ cần trao đổi **vài chục bit và vài word**, dùng **Modbus RTU qua RS-485** là nhanh và rẻ nhất. Nếu hệ đã có hạ tầng mạng và dự kiến mở rộng thêm HMI, SCADA thì đầu tư **truyền thông Ethernet** có lợi về sau.

---

## Đấu dây RS-485 đúng cách

| Hạng mục | Yêu cầu | Hậu quả nếu làm sai |
|---|---|---|
| **Cáp** | Cáp xoắn đôi có lưới chống nhiễu | Nhiễu, mất gói dữ liệu |
| **Topo** | Nối dạng bus (daisy chain) | Nối hình sao gây phản xạ tín hiệu |
| **Điện trở đầu cuối** | Gắn ở hai đầu tuyến | Truyền thông chập chờn ở tốc độ cao |
| **Nối đất lưới cáp** | Nối đất một đầu | Nối hai đầu tạo vòng lặp đất |
| **Đi máng riêng** | Tách khỏi cáp động lực | Biến tần gây nhiễu lên tuyến |
| **Chiều dài tuyến** | Theo giới hạn chuẩn RS-485 | Vượt quá thì cần bộ lặp |

Lỗi **truyền thông** phổ biến nhất tại hiện trường không phải do cấu hình mà do **đi dây**: nối hình sao thay vì bus, thiếu điện trở đầu cuối, hoặc đi chung máng với cáp biến tần. Xem thêm [lỗi truyền thông PLC – HMI – Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Tham số truyền thông phải khớp giữa hai trạm

| Tham số truyền thông | Ghi chú |
|---|---|
| **Tốc độ (baudrate)** | Phải giống hệt nhau ở hai đầu |
| **Data bit / Parity / Stop bit** | Sai một mục là không bắt tay được |
| **Địa chỉ trạm (slave ID)** | Không được trùng trên cùng tuyến |
| **Vùng nhớ trao đổi** | Khai rõ vùng đọc và vùng ghi |
| **Chu kỳ hỏi (polling)** | Quá nhanh gây nghẽn, quá chậm thì trễ |
| **Thời gian timeout** | Đủ dài để không báo lỗi giả |

Khi thiết lập **truyền thông** lần đầu, nên bắt đầu ở **tốc độ thấp** để loại trừ vấn đề đường dây, chạy ổn định rồi mới tăng dần. Cách này tiết kiệm rất nhiều thời gian so với đặt tốc độ cao ngay từ đầu rồi đi mò lỗi.

---

## Lỗi truyền thông thường gặp và cách xử lý

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| Không bắt tay được ngay từ đầu | Sai tham số cổng hoặc đấu ngược A/B | Đối chiếu lại tham số, đảo A/B thử |
| Chạy được lúc đầu rồi mất | Nhiễu, thiếu điện trở đầu cuối | Gắn terminator, kiểm tra tuyến cáp |
| Mất gói khi biến tần khởi động | Nhiễu từ cáp động lực | Tách máng, dùng cáp có lưới |
| Dữ liệu sai lệch, nhảy giá trị | Khai sai vùng nhớ hoặc kiểu dữ liệu | Đối chiếu bảng vùng nhớ hai bên |
| Trễ phản hồi lâu | Chu kỳ hỏi quá dài, quá nhiều trạm | Giảm số điểm trao đổi, tăng tốc độ |
| Một trạm chết kéo cả tuyến | Sự cố phần cứng trên tuyến bus | Tách trạm để khoanh vùng |

---

## Khi nào nên dùng gateway thay vì nối trực tiếp?

| Tình huống | Vì sao nên dùng gateway |
|---|---|
| Nhiều PLC khác hãng trong cùng hệ | Gateway chuẩn hóa giao thức về một mối |
| Cần đưa dữ liệu lên SCADA/IoT | Xem [gateway Modbus](/gateway-modbus-seneca/) |
| Hai vùng mạng cần cách ly | Gateway đóng vai ranh giới |
| PLC đời cũ không đủ cổng | Thêm cổng mà không thay CPU |
| Cần gom dữ liệu nhiều điểm đo | Kết hợp [remote I/O](/remote-io-seneca-z-pc/) |

Với nhà máy có nhiều thế hệ thiết bị, việc dồn **truyền thông** về một gateway thường gọn hơn là nối chằng chịt từng cặp PLC — và dễ mở rộng khi thêm máy mới.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá thiết bị truyền thông

Gửi cho chúng tôi: **model PLC hai đầu · dữ liệu cần trao đổi (bao nhiêu bit/word) · khoảng cách · môi trường có biến tần không · đã có hạ tầng mạng chưa.**

Chúng tôi đề xuất phương án **truyền thông** phù hợp, module hoặc gateway cần bổ sung, kèm báo giá và tài liệu cấu hình.

**→ [Liên hệ tư vấn truyền thông PLC](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/topo-plc-hmi-scada.svg)

## Câu hỏi thường gặp (FAQ)

**FX5U và FX3U nối trực tiếp với nhau được không?**
Được, phổ biến nhất là qua **RS-485 với giao thức Modbus RTU**. Qua Ethernet cũng được nhưng FX3U cần bổ sung module vì không có cổng LAN tích hợp.

**Nên chọn Modbus hay Ethernet?**
Trao đổi ít dữ liệu, ngân sách hạn chế thì Modbus RTU đủ dùng. Hệ dự kiến mở rộng thêm HMI, SCADA thì đầu tư Ethernet có lợi hơn về lâu dài.

**Vì sao truyền thông chạy được lúc đầu rồi mất?**
Thường do **nhiễu hoặc thiếu điện trở đầu cuối**. Hãy kiểm tra tuyến cáp, gắn terminator hai đầu và tách khỏi cáp động lực trước khi nghi phần mềm.

**Có cần lập trình nhiều không?**
Với mạng N:N giữa các trạm FX thì cấu hình là chính, lập trình rất ít. Với Modbus thì cần viết phần đọc/ghi thanh ghi ở phía master.

**Nên đặt tốc độ bao nhiêu?**
Bắt đầu ở tốc độ thấp để loại trừ vấn đề đường dây, chạy ổn định rồi tăng dần. Tốc độ cao nhất không phải lúc nào cũng là lựa chọn tốt nhất.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /plc-mitsubishi-fx5u/, /plc-mitsubishi-fx3u-la-gi/, /loi-truyen-thong-plc-hmi-modbus/, /gateway-modbus-seneca/, /lien-he/. -->
