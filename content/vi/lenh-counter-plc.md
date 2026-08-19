<!--
LOẠI TRANG : Blog kỹ thuật (hướng dẫn lập trình) + Thương mại
URL SLUG   : /lenh-counter-plc/
TỪ KHÓA    : lệnh counter plc | bộ đếm plc | counter trong plc | đếm sản phẩm plc | ctu ctd | counter mitsubishi siemens
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Lệnh Counter PLC: Bộ Đếm Và Cách Sử Dụng
META (148)  : Lệnh Counter PLC (bộ đếm) là gì? Phân biệt đếm lên/đếm xuống, giá trị preset, reset, ví dụ đếm sản phẩm và tên lệnh Counter theo từng hãng PLC.
H1          : Lệnh Counter PLC (Bộ Đếm): Nguyên Lý Và Cách Sử Dụng

---

## Lệnh Counter PLC là gì?

<!--IMG:rep-->
![Nguyên lý lệnh Counter PLC](assets/diagrams/counter-plc.svg)


**Lệnh Counter PLC** (bộ đếm) dùng để **đếm số lần** một sự kiện xảy ra — ví dụ đếm sản phẩm qua cảm biến, đếm số vòng, số lần đóng cắt. Khi đếm đủ **giá trị đặt (preset)**, bộ đếm **bật ngõ ra** để kích hoạt hành động tiếp theo (đóng gói, dừng, báo).

> **Cần hỗ trợ lập trình PLC?** Gửi **yêu cầu ứng dụng** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## Các loại Counter

- **Đếm lên (CTU / Up):** mỗi xung vào tăng giá trị đếm; đạt preset thì bật ngõ ra.
- **Đếm xuống (CTD / Down):** giảm dần từ preset về 0.
- **Đếm lên–xuống (CTUD):** vừa tăng vừa giảm theo hai đầu vào.
- **Counter tốc độ cao (HSC):** đếm xung nhanh (encoder) bằng phần cứng.

---

## Nguyên lý hoạt động

<!--IMG:prin-->
![Ví dụ chương trình Ladder](assets/diagrams/ladder-co-ban.svg)


Bộ đếm có ba yếu tố chính:

- **Ngõ vào đếm:** mỗi cạnh lên của tín hiệu tăng (hoặc giảm) giá trị.
- **Giá trị đặt (preset):** ngưỡng để bật ngõ ra.
- **Reset:** đưa giá trị đếm về 0 để đếm lại.

Ví dụ: đếm đủ **10 sản phẩm** thì bật van gạt sang thùng mới, rồi **reset** để đếm mẻ tiếp theo.

---

## Tên lệnh Counter theo hãng

<!--IMG:app-->
![Nguyên lý PLC](assets/diagrams/prin-plc.svg)


| Hãng | Lệnh/ký hiệu Counter |
|---|---|
| **Mitsubishi** | C0, C1… (OUT C + giá trị K) |
| **Siemens** | CTU, CTD, CTUD (IEC counter) |
| **Omron** | CNT, CNTR |
| **Delta** | C0, C1… (CNT) |
| **LS** | CTU, CTD, CTUD |

Xem thêm: [lập trình PLC Ladder](/lap-trinh-ladder-plc/) và [lệnh Timer PLC](/lenh-timer-plc/).

---

## Ví dụ ứng dụng Counter

- **Đếm sản phẩm** trên băng tải để đóng gói theo lô.
- **Đếm số lần** đóng cắt để bảo trì định kỳ.
- **Đo tốc độ/số vòng** kết hợp encoder (dùng HSC).

---

## Lưu ý khi dùng Counter

- Nhớ **reset đúng lúc** để bắt đầu mẻ đếm mới, tránh cộng dồn sai.
- Đếm **xung nhanh (encoder)** phải dùng **HSC** phần cứng, không dùng counter thường trong chu kỳ quét.
- Chú ý **giá trị đếm tối đa** và kiểu số (16/32 bit) của PLC.
- Với cảm biến, đảm bảo **một sự kiện chỉ tạo một xung** (tránh rung tiếp điểm gây đếm sai).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **ứng dụng đếm · tốc độ xung · hãng PLC.** Chúng tôi hỗ trợ lập trình và **báo giá PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Counter đếm lên và đếm xuống khác nhau thế nào?**
**Đếm lên (CTU)** tăng giá trị mỗi xung đến khi đạt preset; **đếm xuống (CTD)** giảm dần từ preset về 0. CTUD kết hợp cả hai.

**Đếm xung tốc độ cao (encoder) dùng lệnh gì?**
Dùng **bộ đếm tốc độ cao (HSC)** bằng phần cứng, vì counter thường không theo kịp xung nhanh trong chu kỳ quét.

**Làm sao reset bộ đếm PLC?**
Dùng **ngõ vào Reset** của lệnh counter (hoặc lệnh RST tùy hãng) để đưa giá trị về 0 và bắt đầu đếm mẻ mới.

**Counter đếm sai/nhảy số, khắc phục sao?**
Thường do **rung tiếp điểm** hoặc nhiễu tạo nhiều xung cho một sự kiện. Dùng cảm biến ổn định, thêm **lọc/độ trễ**, hoặc dùng **HSC** cho xung nhanh để đếm chính xác.

**Counter và Timer khác nhau thế nào?**
**Timer** đếm **thời gian**, còn **Counter** đếm **số lần/sự kiện**. Nhiều bài toán kết hợp cả hai — ví dụ đếm số sản phẩm trong một khoảng thời gian nhất định.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lệnh Counter PLC) + Article.
     INTERNAL LINK RA: /lap-trinh-ladder-plc/, /lenh-timer-plc/, /plc-la-gi/, /lien-he/. -->
