<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-delta/
TỪ KHÓA    : lỗi plc delta | đèn error delta | wplsoft ispsoft báo lỗi | pin plc delta | lỗi dvp | plc delta báo lỗi
INTENT     : Thông tin → Thương mại (kỹ thuật viên tra lỗi Delta + cần sửa/thay)
TRẠNG THÁI : Sẵn đăng. Đối chiếu đèn ERROR và cờ M1067/M1068/D1067 theo tài liệu Delta trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Delta: Đèn ERROR, Pin & Cách Khắc Phục
META (154)  : PLC Delta DVP/AS báo đèn ERROR, pin yếu hay lỗi truyền thông Modbus? Cách đọc mã lỗi trong WPLSoft/ISPSoft và khắc phục các lỗi PLC Delta thường gặp.
H1          : Lỗi PLC Delta (DVP/AS) Thường Gặp Và Cách Khắc Phục

---

## Lỗi PLC Delta thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC Delta: đèn ERROR báo lỗi](assets/diagrams/rep-loi-delta.svg)


**Lỗi PLC Delta** hay gặp trên dòng **DVP (DVP-SS/SA/SX/EH/ES)** và **AS/AH** gồm: đèn **ERROR** đỏ (sáng hoặc nhấp nháy), **pin yếu (BAT.LOW)** trên dòng AS, **lỗi truyền thông Modbus**, hoặc không kết nối được WPLSoft/ISPSoft. Cách xử lý: **đọc đèn → đọc mã lỗi trong phần mềm → kiểm tra chương trình, thông số truyền thông và phần cứng.**

> **PLC Delta đang lỗi?** Gửi **model + mã lỗi** → [Tư vấn & báo giá sửa – thay thế PLC Delta](#bao-gia).

---

## Đọc đèn báo trên PLC Delta

| Đèn | Bình thường | Khi lỗi |
|---|---|---|
| **POWER** | Sáng | Tắt = mất nguồn / hỏng bộ nguồn |
| **RUN** | Sáng = đang chạy | Tắt = ở STOP hoặc lỗi |
| **ERROR** | Tắt | Sáng/nhấp nháy = lỗi chương trình, cú pháp hoặc phần cứng |
| **BAT.LOW** (AS) | Tắt | Sáng = **pin yếu** (mất giờ RTC / vùng nhớ chốt) |

Công cụ: **WPLSoft** (DVP đời cũ), **ISPSoft** (AS/AH và DVP mới) và **COMMGR** để quản lý cổng truyền thông. Đọc mã lỗi trong phần mềm và các cờ **M1067/M1068** (lỗi thực thi) với thanh ghi **D1067** (mã lỗi).

---

## Các lỗi PLC Delta và cách khắc phục

### 1. Đèn ERROR sáng/nhấp nháy — lỗi chương trình

Thường là **lỗi cú pháp/biên dịch, lệnh không hợp lệ, truy xuất địa chỉ (device) sai**. Khắc phục: dùng **Check/Compile** trong phần mềm để tìm lỗi; đọc **D1067** (mã lỗi) và **D1069**; sửa rồi nạp lại. Cờ **M1067/M1068** báo có lỗi thực thi ở chu kỳ hiện tại.

### 2. Lỗi Watchdog (WDT) — scan quá dài

Quét vượt thời gian giám sát (liên quan **M1008/D1008**). **Tối ưu chương trình**, tránh vòng lặp dài, kiểm tra lệnh nhảy.

### 3. Pin yếu (BAT.LOW) trên dòng AS

Dòng AS dùng pin cho **RTC và vùng nhớ chốt**. Khi báo yếu: **backup**, **thay pin khi PLC còn điện**, cập nhật lại đồng hồ nếu cần.

### 4. Lỗi truyền thông Modbus

- Sai thông số cổng trong **COMMGR** (baud/parity/stop bit).
- Sai **địa chỉ trạm (station address)**, sai chế độ master/slave.
- Đấu sai **A/B RS485**, thiếu điện trở đầu cuối.

Khắc phục: đồng bộ thông số trong COMMGR, đặt đúng địa chỉ, đấu đúng A/B và gắn terminator.

### 5. Không kết nối được WPLSoft/ISPSoft

Do **driver/cổng COM** sai, chưa cấu hình đúng **COMMGR driver**, hoặc chọn sai model PLC. Cài driver, tạo đúng driver trong COMMGR, chọn đúng dòng CPU.

---

## Quy trình khắc phục lỗi PLC Delta

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** POWER/RUN/ERROR/BAT.LOW.
2. **Kiểm tra nguồn** và đấu nối.
3. **Compile & đọc mã lỗi** (D1067, M1067/M1068).
4. **Xử lý pin & chương trình** (thay pin khi còn điện, nạp lại).
5. **Kiểm tra truyền thông** (COMMGR, địa chỉ, A/B).
6. **Sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác.

---

## Khi nào nên thay PLC Delta?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Lỗi chương trình, thông số, pin → **sửa tại chỗ**.
- Cổng/kênh I/O hỏng → **thay module/PLC**.
- **CPU chết** → thay cùng dòng, nạp lại chương trình.
- Dòng DVP đời cũ khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC Delta

- **Backup chương trình** (WPLSoft/ISPSoft) kèm ghi chú phiên bản.
- **Thay pin định kỳ** trên dòng AS (giữ RTC và vùng nhớ chốt).
- **Dự phòng** CPU/module cho dòng DVP đời cũ đang chạy.
- **Chống nhiễu RS485**: cáp shielded, terminator 120Ω, tách dây động lực.
- Tài liệu hóa **thông số COMMGR** (baud/parity, địa chỉ trạm) để khôi phục nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Delta

Gửi cho chúng tôi: **model PLC (DVP-EH, AS228, AH…) · mã lỗi/đèn báo · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá CPU/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Delta](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn ERROR trên PLC Delta báo gì?**
Báo **lỗi chương trình/cú pháp hoặc phần cứng**. Hãy **Compile/Check** trong WPLSoft/ISPSoft và đọc mã lỗi **D1067** để tìm nguyên nhân cụ thể.

**PLC Delta AS báo BAT.LOW phải làm gì?**
Đèn BAT.LOW báo **pin yếu** (giữ RTC và vùng nhớ chốt). Hãy **backup**, **thay pin khi PLC còn điện** rồi cập nhật lại đồng hồ nếu cần.

**Lỗi truyền thông Modbus với PLC Delta khắc phục sao?**
Kiểm tra thông số trong **COMMGR** (baud/parity), đặt đúng **địa chỉ trạm** và chế độ master/slave, đấu đúng **A/B RS485** và gắn điện trở đầu cuối.

**Không kết nối được WPLSoft/ISPSoft?**
Thường do **driver/cổng COM** hoặc **COMMGR** chưa cấu hình đúng. Cài driver, tạo đúng driver trong COMMGR và chọn đúng model PLC.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Delta) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
