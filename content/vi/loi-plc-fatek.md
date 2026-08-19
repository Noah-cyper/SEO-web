<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-fatek/
TỪ KHÓA    : lỗi plc fatek | plc fatek báo lỗi | đèn err fatek | winproladder báo lỗi | lỗi fbs | plc fatek fbs fb
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu tên đèn/cổng theo tài liệu Fatek (FBs/FB) trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Fatek (FBs/FB): Đèn ERR & Cách Khắc Phục
META (149)  : PLC Fatek FBs/FB báo đèn ERR, không RUN hay lỗi truyền thông Modbus? Cách đọc lỗi trong WinProladder và khắc phục các lỗi PLC Fatek thường gặp.
H1          : Lỗi PLC Fatek (FBs/FB) Thường Gặp Và Cách Khắc Phục

---

## Lỗi PLC Fatek thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC Fatek: đèn ERR báo lỗi](assets/diagrams/rep-loi-fatek.svg)


**Lỗi PLC Fatek** (dòng **FBs, FB, B1/B1z**) rất phổ biến trên máy móc giá tốt tại Việt Nam, hay gặp: đèn **ERR** sáng, PLC không RUN, **lỗi truyền thông Modbus** (các cổng Port0–Port4), hoặc không kết nối được WinProladder. Cách xử lý: **đọc đèn → đọc lỗi trong WinProladder → kiểm tra chương trình, I/O và truyền thông.**

> **PLC Fatek đang lỗi?** Gửi **model + mô tả lỗi** → [Tư vấn & báo giá sửa – thay thế PLC Fatek](#bao-gia).

---

## Đọc đèn báo trên PLC Fatek

| Đèn | Bình thường | Khi lỗi |
|---|---|---|
| **POWER / PWR** | Sáng | Tắt = mất nguồn / hỏng bộ nguồn |
| **RUN** | Sáng = đang chạy | Tắt = ở STOP hoặc lỗi |
| **ERR** | Tắt | Sáng = lỗi hệ thống/chương trình |

Công cụ: **WinProladder** (FBs/FB). Kết nối để đọc **trạng thái lỗi và mã lỗi**, kiểm tra chương trình bằng chức năng biên dịch/kiểm tra.

---

## Các lỗi PLC Fatek và cách khắc phục

### 1. Đèn ERR sáng — lỗi hệ thống/chương trình

Thường do **lỗi chương trình, cú pháp, hoặc phần cứng**. Kết nối WinProladder, biên dịch/kiểm tra chương trình để tìm lỗi; nạp lại chương trình đúng.

### 2. Lỗi Watchdog / scan

Chương trình quét quá dài → PLC báo lỗi. **Tối ưu chương trình**, kiểm tra vòng lặp và lệnh nhảy.

### 3. Lỗi I/O

Ngõ vào/ra không tác động: kiểm tra **đấu dây, cầu chì ngõ ra, kiểu Sink/Source**; đo tín hiệu tại terminal; thay thế nếu kênh cháy.

### 4. Lỗi truyền thông Modbus

Fatek hỗ trợ **nhiều cổng (Port0–Port4)** với Modbus RTU/ASCII. Lỗi thường do:

- Sai thông số cổng (baud/parity), sai **địa chỉ trạm**.
- Đấu sai **A/B RS485**, thiếu điện trở đầu cuối.

Khắc phục: đồng bộ thông số, đặt đúng địa chỉ, đấu đúng A/B và gắn terminator.

### 5. Không kết nối được WinProladder

Do **sai cổng/driver**, chọn sai model, hoặc cáp lập trình hỏng. Chọn đúng model FBs/FB, cài driver USB-RS232 (nếu dùng), thử cáp khác.

---

## Quy trình khắc phục lỗi PLC Fatek

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** POWER/RUN/ERR.
2. **Kiểm tra nguồn** và đấu nối.
3. **Biên dịch & đọc lỗi** trong WinProladder.
4. **Soát I/O & đấu dây.**
5. **Kiểm tra truyền thông** (cổng, địa chỉ, A/B).
6. **Sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác.

---

## Khi nào nên thay PLC Fatek?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Lỗi chương trình, thông số, đấu dây → **sửa tại chỗ**.
- Kênh I/O cháy → **thay module/PLC**.
- **CPU chết** → thay cùng dòng, nạp lại chương trình.
- Dòng cũ (FB, B1) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC Fatek

- **Backup chương trình** (WinProladder) kèm ghi chú phiên bản.
- **Thay pin RTC** (nếu dùng) và kiểm tra định kỳ.
- **Dự phòng** PLC/module cho dòng đang chạy.
- **Chống nhiễu RS485**: cáp shielded, terminator, tách dây động lực.
- Ghi lại **thông số các cổng truyền thông** (Port0–Port4) để khôi phục nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Fatek

Gửi cho chúng tôi: **model PLC (FBs-24MC, FB…) · mô tả lỗi/đèn báo · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá PLC/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Fatek](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn ERR trên PLC Fatek báo gì?**
Báo **lỗi hệ thống hoặc chương trình**. Kết nối **WinProladder**, biên dịch/kiểm tra chương trình để tìm nguyên nhân rồi nạp lại.

**Lỗi truyền thông Modbus với PLC Fatek khắc phục sao?**
Kiểm tra thông số **cổng (baud/parity)**, đúng **địa chỉ trạm**, đấu đúng **A/B RS485** và gắn điện trở đầu cuối.

**Không kết nối được WinProladder?**
Thường do **cổng/driver** hoặc chọn sai model. Chọn đúng dòng FBs/FB, cài driver và thử cáp lập trình khác.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Fatek) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
