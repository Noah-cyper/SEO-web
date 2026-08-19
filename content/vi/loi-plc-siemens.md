<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-siemens/
TỪ KHÓA    : lỗi plc siemens | đèn sf bf siemens | s7-1200 lỗi | s7-300 lỗi | diagnostic buffer siemens | plc siemens về stop
INTENT     : Thông tin → Thương mại (kỹ thuật viên tra lỗi Siemens + cần sửa/thay)
TRẠNG THÁI : Sẵn đăng. Đối chiếu tên đèn SF/BF/ERROR theo tài liệu Siemens từng dòng CPU trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Siemens: Đèn SF/BF, ERROR & Cách Khắc Phục
META (152)  : PLC Siemens S7 báo đèn SF, BF hay ERROR, hoặc CPU về STOP? Cách đọc Diagnostic buffer trong TIA Portal và khắc phục các lỗi PLC Siemens thường gặp.
H1          : Lỗi PLC Siemens (S7-1200/1500, S7-300/400) Và Cách Khắc Phục

---

## Lỗi PLC Siemens thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC Siemens: đèn SF, BF, ERROR](assets/diagrams/rep-loi-siemens.svg)


**Lỗi PLC Siemens** phổ biến trên **S7-1200, S7-1500, S7-300/400** và **LOGO!** gồm: đèn **SF (System Fault)** hoặc **ERROR** sáng, đèn **BF (Bus Fault)** báo lỗi mạng Profibus/Profinet, **CPU về STOP**, hoặc mất kết nối. Chìa khóa xử lý lỗi Siemens là đọc **bộ đệm chẩn đoán (Diagnostic buffer)** — nơi ghi lại **từng sự kiện lỗi kèm thời gian**.

> **PLC Siemens đang lỗi?** Gửi **model CPU + nội dung Diagnostic buffer** → [Tư vấn & báo giá sửa – thay thế PLC Siemens](#bao-gia).

---

## Đọc đèn báo trên PLC Siemens

| Dòng | Đèn chính | Ý nghĩa khi lỗi |
|---|---|---|
| **S7-300/400** | SF, BF, DC5V, FRCE, RUN, STOP | **SF** = lỗi hệ thống; **BF** = lỗi bus Profibus/Profinet |
| **S7-1200** | RUN/STOP, ERROR, MAINT | **ERROR đỏ nhấp nháy** = có lỗi; MAINT = cần bảo trì |
| **S7-1500** | RUN/STOP, ERROR, MAINT | Tương tự S7-1200, xem chi tiết ở màn hình CPU |

Công cụ chuẩn: **TIA Portal / STEP 7 → Online & Diagnostics → Diagnostic buffer**. S7-1500 có **màn hình hiển thị trực tiếp mã lỗi** trên CPU.

---

## Các lỗi PLC Siemens và cách khắc phục

### 1. Đèn SF sáng — lỗi hệ thống

SF (System Fault) báo lỗi phần cứng/hệ thống hoặc lỗi module. Mở **Diagnostic buffer** để xem sự kiện gần nhất; kiểm tra module I/O, nguồn, và cấu hình phần cứng (Device configuration) so với thực tế.

### 2. Đèn BF sáng — lỗi bus Profibus/Profinet

BF (Bus Fault) báo lỗi truyền thông mạng:

- Sai **địa chỉ trạm/Profinet device name**, trùng địa chỉ.
- Đứt/lỏng cáp bus, sai **điện trở đầu cuối** Profibus.
- Thiết bị tớ mất nguồn, sai **file GSD/GSDML**.

Khắc phục: rà lại device name/địa chỉ, kiểm tra cáp và terminator, so cấu hình mạng với thực tế.

### 3. CPU về STOP — lỗi chương trình

CPU chuyển sang STOP thường do lỗi lập trình khi chạy:

- Truy xuất vùng nhớ/địa chỉ không hợp lệ (thiếu khối xử lý lỗi **OB121/OB122** trên S7-300/400).
- Chia cho 0, tràn, hoặc lỗi thời gian quét (**watchdog**).

Khắc phục: đọc Diagnostic buffer để tới đúng khối/dòng lỗi, bổ sung OB xử lý lỗi, rà logic rồi chuyển lại RUN.

### 4. Đèn ERROR (S7-1200/1500) nhấp nháy

Báo có lỗi chẩn đoán. Mở **Online & Diagnostics**, xem module nào báo lỗi (I/O, analog, truyền thông) và xử lý theo thông báo.

### 5. Lỗi kết nối / tải chương trình

- **Sai IP/subnet** hoặc trùng IP, sai cổng.
- Chưa đặt đúng **Profinet device name**.
- Sai giao diện PG/PC, tường lửa chặn.

Khắc phục: đặt IP cùng lớp mạng, gán đúng device name, chọn đúng PG/PC interface trong TIA Portal.

---

## Quy trình khắc phục lỗi PLC Siemens

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** SF/BF/ERROR, RUN/STOP.
2. **Kiểm tra nguồn** và module I/O.
3. **Mở Diagnostic buffer** đọc sự kiện lỗi kèm thời gian.
4. **Xử lý theo mã lỗi** (hệ thống, bus, chương trình).
5. **Kiểm tra mạng/kết nối** (IP, device name, cáp bus).
6. **Sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác phần cứng.

---

## Khi nào nên thay PLC Siemens?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Lỗi cấu hình, sai địa chỉ, lỗi chương trình → **sửa/nạp lại**.
- Module I/O hỏng → **thay module**, giữ CPU.
- **CPU chết** → thay CPU cùng dòng, nạp lại chương trình từ backup.
- Dòng cũ (S7-200, một số S7-300) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

Xem thêm: [các lỗi PLC thường gặp & cách khắc phục — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC Siemens

- **Backup project TIA Portal/STEP 7** kèm ghi chú phiên bản; lưu ở nơi an toàn.
- Khi có sự cố, **xuất Diagnostic buffer** để lưu lại lịch sử lỗi phục vụ phân tích.
- **Dự phòng** CPU, module I/O và **thẻ nhớ (SIMATIC Memory Card)** cho dòng đang chạy.
- **Chống nhiễu bus** Profibus/Profinet: cáp đúng chuẩn, terminator, nối đất màn chống nhiễu.
- Đặt **tên Profinet device và IP** rõ ràng, ghi lại sơ đồ mạng để tra cứu nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Siemens

Gửi cho chúng tôi: **model CPU (S7-1200/1500/300…) · nội dung Diagnostic buffer · hiện tượng lỗi · sơ đồ mạng.** Chúng tôi tư vấn hướng khắc phục và **báo giá CPU/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Siemens](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn SF trên PLC Siemens nghĩa là gì?**
SF (System Fault) báo **lỗi hệ thống/phần cứng hoặc module**. Mở **Diagnostic buffer** trong TIA Portal để xem sự kiện lỗi gần nhất và xử lý theo đó.

**Đèn BF báo lỗi gì?**
BF (Bus Fault) là **lỗi mạng Profibus/Profinet**: sai địa chỉ/device name, đứt cáp, sai terminator hoặc thiết bị tớ mất nguồn.

**Vì sao CPU Siemens tự về STOP?**
Thường do **lỗi lập trình khi chạy** (truy xuất sai địa chỉ, thiếu OB xử lý lỗi, watchdog). Đọc Diagnostic buffer để tới đúng khối lỗi, bổ sung OB121/OB122 và rà logic.

**Không kết nối được TIA Portal với PLC thì sao?**
Kiểm tra **IP cùng lớp mạng**, đúng **Profinet device name**, chọn đúng **PG/PC interface** và tắt tường lửa chặn.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Siemens) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
