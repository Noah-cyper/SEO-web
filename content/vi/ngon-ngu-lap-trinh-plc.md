<!--
LOẠI TRANG : Blog kỹ thuật (kiến thức) + Thương mại
URL SLUG   : /ngon-ngu-lap-trinh-plc/
TỪ KHÓA    : ngôn ngữ lập trình plc | ladder logic | fbd st sfc il | iec 61131-3 | lập trình plc | ngôn ngữ ladder
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Ngôn Ngữ Lập Trình PLC: 5 Loại Theo IEC 61131-3
META (150)  : Ngôn ngữ lập trình PLC gồm 5 loại chuẩn IEC 61131-3: Ladder, FBD, ST, SFC, IL. Đặc điểm, khi nào dùng loại nào và vì sao Ladder phổ biến nhất.
H1          : Ngôn Ngữ Lập Trình PLC: 5 Loại Chuẩn IEC 61131-3

---

## Có những ngôn ngữ lập trình PLC nào?

<!--IMG:rep-->
![Ngôn ngữ lập trình PLC theo IEC 61131-3](assets/diagrams/ngon-ngu-plc.svg)


**Ngôn ngữ lập trình PLC** được chuẩn hóa trong tiêu chuẩn **IEC 61131-3** với **5 loại**: **Ladder (LAD), FBD, ST, SFC và IL**. Mỗi ngôn ngữ có thế mạnh riêng; hiểu chúng giúp bạn **chọn cách lập trình phù hợp** với bài toán và với phần mềm của hãng.

> **Cần hỗ trợ lập trình PLC?** Gửi **yêu cầu ứng dụng** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## 1. Ladder (LAD) — bậc thang

Giống **sơ đồ mạch relay**: tiếp điểm và cuộn dây trên các "bậc thang". **Trực quan, dễ đọc**, phổ biến nhất, hợp logic ON/OFF. Xem: [lập trình Ladder cơ bản](/lap-trinh-ladder-plc/).

## 2. FBD — sơ đồ khối hàm

Dùng các **khối hàm** (AND, OR, timer, PID…) nối với nhau bằng đường tín hiệu. Hợp xử lý **tín hiệu và điều khiển liên tục**.

## 3. ST — văn bản có cấu trúc

Ngôn ngữ **giống Pascal/C** (IF, FOR, WHILE…). Mạnh cho **tính toán, thuật toán phức tạp**, xử lý dữ liệu.

## 4. SFC — biểu đồ tuần tự

Mô tả quy trình theo **các bước và chuyển tiếp**. Rất hợp **quy trình tuần tự** (máy chạy theo công đoạn).

## 5. IL — danh sách lệnh

Ngôn ngữ **giống hợp ngữ (assembly)**, ngắn gọn nhưng khó đọc; ngày nay ít dùng dần.

---

## Nên học ngôn ngữ nào trước?

<!--IMG:prin-->
![Ví dụ chương trình Ladder](assets/diagrams/ladder-co-ban.svg)


Với người mới, nên bắt đầu bằng **Ladder (LAD)** vì trực quan và được hỗ trợ trên hầu hết PLC. Khi cần tính toán phức tạp, học thêm **ST**; quy trình nhiều công đoạn thì dùng **SFC**.

---

## Ưu, nhược điểm từng ngôn ngữ

| Ngôn ngữ | Ưu điểm | Hợp với |
|---|---|---|
| **Ladder (LAD)** | Trực quan, dễ đọc, phổ biến | Logic ON/OFF, người mới |
| **FBD** | Gọn khi nhiều khối hàm | Xử lý tín hiệu, điều khiển |
| **ST** | Mạnh cho tính toán, thuật toán | Bài toán phức tạp, dữ liệu |
| **SFC** | Rõ ràng theo bước | Quy trình tuần tự nhiều công đoạn |
| **IL** | Ngắn gọn | Ngày nay ít dùng |

Nhiều dự án **kết hợp** nhiều ngôn ngữ trong cùng chương trình: Ladder cho logic, ST cho tính toán, SFC cho quy trình.

## Ngôn ngữ nào tùy theo hãng?

<!--IMG:app-->
![Nguyên lý PLC](assets/diagrams/prin-plc.svg)


Hầu hết hãng đều hỗ trợ **Ladder**; nhiều phần mềm hỗ trợ thêm FBD/ST/SFC (GX Works, TIA Portal, CX-Programmer, ISPSoft…). Chọn ngôn ngữ theo **bài toán và thói quen nhóm kỹ thuật**.

Xem thêm: [PLC là gì](/plc-la-gi/) và [cách chọn PLC](/cach-chon-plc/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **ứng dụng · hãng PLC · độ phức tạp logic.** Chúng tôi tư vấn ngôn ngữ/PLC phù hợp và **báo giá chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Có bao nhiêu ngôn ngữ lập trình PLC?**
Theo chuẩn **IEC 61131-3** có **5 ngôn ngữ**: Ladder (LAD), FBD, ST, SFC và IL. Ladder phổ biến nhất.

**Ngôn ngữ Ladder là gì?**
Ladder mô phỏng **sơ đồ mạch relay** với tiếp điểm và cuộn dây trên các bậc thang — trực quan, dễ đọc, hợp logic ON/OFF.

**Người mới nên học ngôn ngữ PLC nào?**
Nên bắt đầu với **Ladder (LAD)** vì trực quan và được hỗ trợ rộng rãi; sau đó học thêm ST/SFC khi cần.

**Có thể dùng nhiều ngôn ngữ trong một chương trình PLC không?**
Có. Nhiều phần mềm cho phép **kết hợp** — ví dụ dùng **Ladder** cho logic điều khiển, **ST** cho tính toán và **SFC** cho quy trình tuần tự — trong cùng một dự án.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Ngôn ngữ lập trình PLC) + Article.
     INTERNAL LINK RA: /lap-trinh-ladder-plc/, /plc-la-gi/, /cach-chon-plc/, /lien-he/. -->
