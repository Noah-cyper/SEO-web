<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo triệu chứng + dịch vụ)
URL SLUG   : /loi-ngo-vao-ra-plc/
TỪ KHÓA    : lỗi ngõ vào ra plc | lỗi i/o plc | ngõ vào plc không ăn | ngõ ra plc không tác động | sink source npn pnp | cháy ngõ ra plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Lỗi Ngõ Vào Ra PLC (I/O): Nguyên Nhân & Khắc Phục
META (152)  : Ngõ vào PLC không ăn, ngõ ra không tác động? Nguyên nhân (cảm biến, đứt dây, sai NPN/PNP, cháy kênh) và cách khắc phục lỗi ngõ vào ra PLC từng bước.
H1          : Lỗi Ngõ Vào Ra PLC (I/O): Nguyên Nhân Và Cách Khắc Phục

---

## Lỗi ngõ vào ra PLC là gì?

<!--IMG:rep-->
![Lỗi ngõ vào ra PLC: đấu NPN/PNP sink source](assets/diagrams/io-sink-source.svg)


**Lỗi ngõ vào ra PLC (I/O)** là khi **cảm biến tác động nhưng đèn Input không sáng**, hoặc **ra lệnh nhưng Output không đóng**. Nguyên nhân thường ở **đấu dây, cảm biến, kiểu Sink/Source (NPN/PNP)** hoặc **kênh cháy** — không nhất thiết do CPU. Cách xác định: **so đèn I/O với tín hiệu đo tại terminal**.

> **Ngõ vào/ra PLC không hoạt động?** Gửi **model + kênh lỗi** → [Tư vấn kỹ thuật & báo giá module I/O](#bao-gia).

---

## Lỗi ngõ vào (Input) và cách khắc phục

### 1. Đèn Input không sáng dù cảm biến tác động

- **Cảm biến hỏng / đứt dây / lỏng terminal** → đo tín hiệu tại chân vào.
- **Sai kiểu Sink/Source (NPN/PNP)** so với cấu hình ngõ vào → đấu đúng chân COM (+V hay 0V).
- **Sai điện áp** tín hiệu → kiểm tra mức 24V.

### 2. Đèn Input sáng nhưng chương trình không nhận

Thường do **địa chỉ/ánh xạ sai** trong chương trình, hoặc **force** đang bật. Kiểm tra bảng I/O và gỡ force.

---

## Lỗi ngõ ra (Output) và cách khắc phục

### 3. Ngõ ra không tác động

- **Cháy relay/transistor output** do quá dòng/quá áp → thay kênh dự phòng hoặc **thay module**.
- **Thiếu nguồn tải** hoặc đấu tải sai → kiểm tra nguồn cấp cho tải.

### 4. Bảo vệ ngõ ra

Dùng **relay trung gian** cho tải lớn/tải cảm, thêm **diode/RC dập** cho tải cuộn dây, đấu đúng dòng cho phép để tránh cháy kênh.

---

## Quy trình kiểm tra I/O

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Xác định kênh lỗi** (vào hay ra, địa chỉ nào).
2. **Đo tín hiệu tại terminal** và so với đèn I/O.
3. **Kiểm tra cảm biến, dây, kiểu NPN/PNP, chân COM.**
4. **Kiểm tra ánh xạ địa chỉ** và gỡ force trong chương trình.
5. **Với ngõ ra:** kiểm tra tải, dòng, relay bảo vệ.
6. **Kênh cháy → chuyển dự phòng hoặc thay module.**

> **An toàn:** ngắt điện, LOTO trước khi đấu lại dây.

---

## Khi nào nên thay module I/O?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Đứt dây, sai NPN/PNP, sai địa chỉ → **sửa tại chỗ**.
- **Cháy 1–2 kênh** → chuyển kênh dự phòng.
- **Nhiều kênh hỏng** → **thay module I/O** (hoặc dùng module mở rộng/remote I/O).

Xem thêm: [mở rộng I/O cho PLC](/mo-rong-io-plc/) và [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá module I/O

Gửi cho chúng tôi: **model PLC · kênh lỗi (vào/ra) · loại tín hiệu · số lượng.** Chúng tôi tư vấn và **báo giá module I/O chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến tác động nhưng đèn Input PLC không sáng, vì sao?**
Thường do **đứt dây/lỏng terminal**, **sai kiểu NPN/PNP** (sai chân COM), cảm biến hỏng hoặc sai điện áp. Đo tín hiệu tại chân vào để xác định.

**Ngõ ra PLC không tác động thì sao?**
Kiểm tra **cháy relay/transistor output**, thiếu nguồn tải hoặc đấu sai. Kênh cháy thì chuyển dự phòng hoặc thay module; nên dùng relay trung gian bảo vệ.

**NPN và PNP khác nhau thế nào khi đấu vào PLC?**
**NPN (sink)** dùng chân COM là **+V**, **PNP (source)** dùng COM là **0V**. Đấu sai kiểu sẽ khiến ngõ vào không tác động.

**Ngõ ra PLC nóng bất thường hoặc nhảy CB khi bật, vì sao?**
Đây là dấu hiệu **quá dòng hoặc chập tải** ở ngõ ra. Ngắt điện, tách tải để kiểm tra; dùng **relay trung gian** cho tải lớn/tải cảm và đấu đúng dòng cho phép để tránh cháy kênh output.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi ngõ vào ra PLC) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /lien-he/. -->
