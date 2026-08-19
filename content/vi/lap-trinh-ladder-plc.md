<!--
LOẠI TRANG : Blog kỹ thuật (hướng dẫn lập trình) + Thương mại
URL SLUG   : /lap-trinh-ladder-plc/
TỪ KHÓA    : lập trình plc ladder | ladder cơ bản | tiếp điểm cuộn dây plc | tự giữ seal-in | lập trình plc cho người mới | ladder logic
INTENT     : Thông tin (người mới học) → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Lập Trình PLC Ladder Cơ Bản Cho Người Mới
META (151)  : Hướng dẫn lập trình PLC Ladder cơ bản cho người mới: tiếp điểm thường mở/đóng, cuộn dây, cách đọc rung và ví dụ điều khiển động cơ start/stop dễ hiểu.
H1          : Lập Trình PLC Ladder Cơ Bản Cho Người Mới Bắt Đầu

---

## Lập trình PLC Ladder là gì?

<!--IMG:rep-->
![Ví dụ lập trình PLC Ladder](assets/diagrams/ladder-co-ban.svg)


**Lập trình PLC Ladder** (LAD) là cách viết chương trình PLC theo dạng **sơ đồ hình bậc thang**, mô phỏng mạch relay quen thuộc với thợ điện. Đây là ngôn ngữ **trực quan và phổ biến nhất**, rất hợp cho **người mới bắt đầu**. Chương trình gồm các "bậc thang" (rung) nằm giữa hai thanh ray dọc; mỗi rung là một mạch logic điều khiển ngõ ra.

> **Cần hỗ trợ lập trình PLC?** Gửi **yêu cầu ứng dụng** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## Các thành phần cơ bản

- **Tiếp điểm thường mở (NO) `-| |-`:** dẫn điện khi tín hiệu vào **bật (ON)**.
- **Tiếp điểm thường đóng (NC) `-|/|-`:** dẫn điện khi tín hiệu vào **tắt (OFF)**.
- **Cuộn dây (coil) `-( )-`:** ngõ ra, bật khi đường dẫn từ trái sang phải **thông mạch**.
- **Thanh ray (rail):** hai đường dọc hai bên, tượng trưng nguồn.

Ký hiệu địa chỉ tùy hãng: ngõ vào **X/I**, ngõ ra **Y/Q**, bit nội **M**.

---

## Cách PLC quét chương trình Ladder

PLC đọc chương trình **từ trên xuống dưới, mỗi rung từ trái sang phải**, lặp lại theo **chu kỳ quét**. Ở mỗi vòng: đọc ngõ vào → tính logic từng rung → cập nhật ngõ ra. Vì quét rất nhanh nên hệ phản ứng gần như tức thời. Xem thêm [PLC là gì](/plc-la-gi/).

---

## Ví dụ: mạch Start/Stop có tự giữ (seal-in)

<!--IMG:prin-->
![Nguyên lý PLC: đọc vào - xử lý - xuất ra](assets/diagrams/prin-plc.svg)


Bài toán kinh điển: nhấn **Start** thì động cơ chạy và **giữ chạy** dù nhả nút; nhấn **Stop** thì dừng.

- Rung: `-[Start]-+-[/Stop]-( Y0 )` với **tiếp điểm tự giữ Y0** song song với Start.
- Khi nhấn Start, Y0 bật; **tiếp điểm Y0 tự giữ** duy trì mạch dù nhả Start.
- Nhấn Stop (tiếp điểm thường đóng) → cắt mạch, Y0 tắt.

Đây là nền tảng của hầu hết mạch điều khiển động cơ. Xem chi tiết: [lập trình PLC điều khiển động cơ](/lap-trinh-dieu-khien-dong-co-plc/).

---

## Kết hợp Timer và Counter

<!--IMG:app-->
![Nguyên lý lệnh Timer](assets/diagrams/timer-plc.svg)


Chương trình thực tế thường thêm:

- **Timer** để tạo trễ (ví dụ chạy sau 3 giây) — xem [lệnh Timer PLC](/lenh-timer-plc/).
- **Counter** để đếm sản phẩm/số lần — xem [lệnh Counter PLC](/lenh-counter-plc/).

---

## Mẹo cho người mới

- Đặt **tên/địa chỉ rõ ràng**, ghi chú (comment) từng rung.
- Viết logic **đơn giản, dễ đọc**; tránh rung quá phức tạp.
- **Mô phỏng** trước khi nạp (nhiều phần mềm có simulator).
- **Backup** chương trình sau khi hoàn thiện.

Phần mềm theo hãng: **GX Works (Mitsubishi), TIA Portal (Siemens), CX-Programmer (Omron), ISPSoft (Delta), XG5000 (LS)…**

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **ứng dụng · hãng PLC · số I/O.** Chúng tôi hỗ trợ lập trình/đào tạo và **báo giá PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Tiếp điểm thường mở và thường đóng khác nhau thế nào?**
**Thường mở (NO)** dẫn điện khi tín hiệu **bật**; **thường đóng (NC)** dẫn điện khi tín hiệu **tắt**. Nút Stop thường dùng NC để khi nhấn sẽ cắt mạch.

**Mạch tự giữ (seal-in) là gì?**
Là mạch dùng **tiếp điểm của chính ngõ ra** mắc song song với nút Start để **duy trì trạng thái** dù nhả nút — nền tảng của điều khiển Start/Stop.

**Người mới nên bắt đầu học Ladder ở đâu?**
Bắt đầu với **tiếp điểm – cuộn dây – mạch tự giữ**, rồi thêm **Timer/Counter**. Dùng **simulator** của phần mềm để luyện trước khi nạp vào PLC thật.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lập trình PLC Ladder) + Article.
     INTERNAL LINK RA: /plc-la-gi/, /lenh-timer-plc/, /lenh-counter-plc/, /lap-trinh-dieu-khien-dong-co-plc/, /lien-he/. -->
