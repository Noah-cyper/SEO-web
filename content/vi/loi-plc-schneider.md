<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-schneider/
TỪ KHÓA    : lỗi plc schneider | plc modicon báo lỗi | đèn err schneider | ecostruxure báo lỗi | lỗi m221 m340 | plc schneider modicon
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu tên đèn/chẩn đoán theo tài liệu Schneider (EcoStruxure) trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Schneider (Modicon): Đèn ERR & Khắc Phục
META (156)  : PLC Schneider Modicon M221/M241/M340 báo đèn ERR, I/O hay mất truyền thông? Cách chẩn đoán trong EcoStruxure và khắc phục các lỗi PLC Schneider thường gặp.
H1          : Lỗi PLC Schneider (Modicon M221/M340) Và Cách Khắc Phục

---

## Lỗi PLC Schneider thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC Schneider: đèn ERR, I/O báo lỗi](assets/diagrams/rep-loi-schneider.svg)


**Lỗi PLC Schneider** (dòng **Modicon M221, M241/M251, M340, M580** và **Twido, Zelio**) hay gặp: đèn **ERR** sáng, đèn **I/O** báo lỗi vào/ra, **mất truyền thông** (Modbus serial line), chưa nạp ứng dụng, hoặc pin backup yếu. Cách xử lý: **đọc đèn → chẩn đoán trong EcoStruxure → kiểm tra cấu hình, I/O và truyền thông.**

> **PLC Schneider đang lỗi?** Gửi **model + mô tả đèn/lỗi** → [Tư vấn & báo giá sửa – thay thế PLC Schneider](#bao-gia).

---

## Đọc đèn báo trên PLC Schneider Modicon

| Đèn | Bình thường | Khi lỗi |
|---|---|---|
| **PWR / RUN** | Sáng = có nguồn/đang chạy | Tắt = mất nguồn hoặc ở STOP |
| **ERR** | Tắt | Sáng/nhấp nháy = lỗi hệ thống/ứng dụng |
| **I/O** | Tắt | Sáng = lỗi vào/ra hoặc module |
| **SL / MB / NS** | Nhấp nháy khi truyền | Bất thường = lỗi Modbus serial / mạng |

Công cụ: **EcoStruxure Machine Expert** (M221/M241/M251 — trước là SoMachine) và **EcoStruxure Control Expert** (M340/M580 — trước là Unity Pro) → xem **Diagnostics / Detected errors**.

---

## Các lỗi PLC Schneider và cách khắc phục

### 1. Đèn ERR sáng — lỗi hệ thống/ứng dụng

Thường do **chưa nạp ứng dụng**, ứng dụng lỗi, hoặc **cấu hình phần cứng lệch** so với thực tế. Kết nối phần mềm đọc **Detected errors**, nạp lại ứng dụng đúng cấu hình.

### 2. Đèn I/O báo lỗi vào/ra

Sai cấu hình kênh, module lỗi, hoặc đứt dây. Kiểm tra **cấu hình I/O** trong phần mềm so thực tế; đo tín hiệu tại terminal; thay module nếu hỏng.

### 3. Lỗi Watchdog / ứng dụng dừng

Task quét quá thời gian giám sát → CPU dừng. **Tối ưu chương trình**, kiểm tra task và thời gian chu kỳ.

### 4. Mất truyền thông (Modbus serial line / Ethernet)

- Sai thông số **serial line** (baud/parity), sai **địa chỉ Modbus**.
- Ethernet: **sai IP/subnet**, trùng IP.

Khắc phục: đồng bộ thông số, đặt đúng địa chỉ/IP, đấu đúng RS485 và gắn terminator.

### 5. Pin backup yếu (M241/M251/M340)

Pin giữ vùng nhớ/đồng hồ. Khi yếu: **backup**, **thay pin khi còn điện** đúng loại.

---

## Quy trình khắc phục lỗi PLC Schneider

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** PWR/RUN/ERR/I/O.
2. **Kiểm tra nguồn** và đấu nối.
3. **Chẩn đoán trong EcoStruxure** (Detected errors), nạp lại ứng dụng.
4. **Soát cấu hình I/O & module.**
5. **Kiểm tra truyền thông** (serial line/IP).
6. **Sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác.

---

## Khi nào nên thay PLC Schneider?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Ứng dụng, cấu hình, pin → **sửa/nạp lại**.
- Module I/O hỏng → **thay module**.
- **CPU chết** → thay cùng dòng, nạp lại ứng dụng.
- Dòng cũ (Twido, Modicon đời đầu) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC Schneider

- **Backup ứng dụng** (EcoStruxure) kèm ghi chú phiên bản.
- **Thay pin backup định kỳ** (M241/M251/M340) trước khi báo yếu.
- **Dự phòng** CPU/module I/O cho dòng đang chạy.
- **Chống nhiễu bus** và nối đất đúng chuẩn; đấu RS485 đúng A/B + terminator.
- Ghi lại **địa chỉ Modbus/IP** và sơ đồ mạng để khôi phục nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Schneider

Gửi cho chúng tôi: **model PLC (M221, M340…) · mã lỗi/đèn báo · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá CPU/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Schneider](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn ERR trên PLC Schneider báo gì?**
Báo **lỗi hệ thống/ứng dụng** (chưa nạp ứng dụng, ứng dụng lỗi, cấu hình lệch). Kết nối EcoStruxure đọc **Detected errors** để biết nguyên nhân cụ thể.

**PLC Schneider mất truyền thông Modbus xử lý sao?**
Kiểm tra thông số **serial line** (baud/parity), đúng **địa chỉ Modbus**, đấu đúng **A/B RS485** và terminator; với Ethernet thì đặt **IP cùng lớp mạng**, không trùng.

**Phần mềm nào để chẩn đoán PLC Schneider?**
**EcoStruxure Machine Expert** cho M221/M241/M251 và **EcoStruxure Control Expert** cho M340/M580.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Schneider) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
