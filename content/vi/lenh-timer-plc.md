<!--
LOẠI TRANG : Blog kỹ thuật (hướng dẫn lập trình) + Thương mại
URL SLUG   : /lenh-timer-plc/
TỪ KHÓA    : lệnh timer plc | timer trong plc | bộ định thời plc | on delay off delay | ton tof | timer mitsubishi siemens
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Lệnh Timer PLC: Bộ Định Thời Và Cách Dùng
META (149)  : Lệnh Timer PLC (bộ định thời) là gì? Phân biệt ON-delay/OFF-delay, cách đặt thời gian, ví dụ ứng dụng và tên lệnh Timer trên Mitsubishi, Siemens, Delta.
H1          : Lệnh Timer PLC (Bộ Định Thời): Nguyên Lý Và Cách Dùng

---

## Lệnh Timer PLC là gì?

<!--IMG:rep-->
![Nguyên lý lệnh Timer PLC](assets/diagrams/timer-plc.svg)


**Lệnh Timer PLC** (bộ định thời) dùng để **tạo trễ thời gian** trong chương trình: bật/tắt ngõ ra sau một khoảng thời gian đặt trước. Timer là một trong những lệnh **được dùng nhiều nhất** — có mặt trong hầu hết bài toán điều khiển (chạy trễ, dừng trễ, tạo chu kỳ).

> **Cần hỗ trợ lập trình PLC?** Gửi **yêu cầu ứng dụng** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## Các loại Timer thường gặp

- **ON-delay (TON):** ngõ vào bật, sau thời gian T thì **ngõ ra mới bật**. Phổ biến nhất.
- **OFF-delay (TOF):** ngõ vào tắt, sau thời gian T thì **ngõ ra mới tắt**.
- **Retentive (tích lũy):** cộng dồn thời gian qua nhiều lần bật/tắt cho đến khi đạt T.

---

## Nguyên lý ON-delay

<!--IMG:prin-->
![Ví dụ chương trình Ladder](assets/diagrams/ladder-co-ban.svg)


Với **ON-delay**: khi điều kiện đầu vào **duy trì bật** đủ thời gian đặt **T**, timer "đếm đủ" và **bật ngõ ra**. Nếu đầu vào tắt trước khi đủ T, timer **reset**. Đây là cách tạo trễ an toàn (ví dụ: bật quạt làm mát 5 giây trước khi chạy động cơ chính).

---

## Đặt thời gian và độ phân giải

- Timer có **giá trị đặt (preset)** và **đơn vị** (thường 0.1s, 0.01s, 1ms tùy timer).
- Chọn đúng **độ phân giải** cho yêu cầu (chính xác cao dùng timer mili-giây).
- Chú ý **số lượng timer** tối đa của PLC.

---

## Tên lệnh Timer theo hãng

<!--IMG:app-->
![Nguyên lý PLC](assets/diagrams/prin-plc.svg)


| Hãng | Lệnh/ký hiệu Timer |
|---|---|
| **Mitsubishi** | T0, T1… (OUT T + giá trị K) |
| **Siemens** | TON, TOF, TP (IEC timer) |
| **Omron** | TIM, TIMH |
| **Delta** | T0, T1… (TMR) |
| **LS** | TON, TOFF, TMR |

Xem thêm: [lập trình PLC Ladder](/lap-trinh-ladder-plc/) và [lệnh Counter PLC](/lenh-counter-plc/).

---

## Ví dụ ứng dụng Timer

- **Chạy trễ:** bật động cơ sau khi bơm dầu bôi trơn vài giây.
- **Dừng trễ:** tắt quạt sau khi máy dừng để làm mát.
- **Tạo chu kỳ nhấp nháy:** kết hợp 2 timer để tạo xung ON/OFF.

---

## Lưu ý khi dùng Timer

- Với **ON-delay**, timer chỉ đếm khi **điều kiện đầu vào duy trì**; mất điều kiện là **reset** về 0.
- Chọn **đúng loại** (ON-delay/OFF-delay/retentive) cho bài toán.
- Chú ý **giới hạn số timer** và tầm giá trị đặt của PLC.
- Với yêu cầu chính xác cao, dùng timer **độ phân giải nhỏ (ms)**.
- Đặt **tên/comment rõ ràng** để dễ đọc và bảo trì.

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **ứng dụng · hãng PLC.** Chúng tôi hỗ trợ lập trình và **báo giá PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Timer ON-delay và OFF-delay khác nhau thế nào?**
**ON-delay** trễ khi bật (ngõ ra bật sau thời gian T kể từ khi vào bật); **OFF-delay** trễ khi tắt (ngõ ra tắt sau T kể từ khi vào tắt).

**Timer PLC đặt thời gian bằng đơn vị gì?**
Tùy timer, thường theo **0.1s, 0.01s hoặc 1ms**. Chọn timer có **độ phân giải** phù hợp độ chính xác cần thiết.

**Lệnh Timer trên Mitsubishi và Siemens gọi là gì?**
Mitsubishi dùng **T0, T1…** (đặt giá trị K); Siemens dùng **TON, TOF, TP** theo chuẩn IEC.

**Timer bị reset ngoài ý muốn, vì sao?**
Với ON-delay, nếu **điều kiện đầu vào chập chờn hoặc mất** trước khi đủ thời gian đặt, timer sẽ **reset**. Kiểm tra tín hiệu vào ổn định, hoặc dùng timer **retentive** nếu cần cộng dồn thời gian.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lệnh Timer PLC) + Article.
     INTERNAL LINK RA: /lap-trinh-ladder-plc/, /lenh-counter-plc/, /plc-la-gi/, /lien-he/. -->
