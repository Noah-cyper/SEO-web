<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-mitsubishi/
TỪ KHÓA    : lỗi plc mitsubishi | plc mitsubishi báo lỗi | đèn error mitsubishi | pin plc mitsubishi | lỗi fx3u | mã lỗi plc mitsubishi
INTENT     : Thông tin → Thương mại (kỹ thuật viên tra lỗi Mitsubishi + cần sửa/thay)
TRẠNG THÁI : Sẵn đăng. Đối chiếu tên đèn/thanh ghi D8060–D8069 theo tài liệu Mitsubishi trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Mitsubishi: Đèn ERROR/BATT & Cách Khắc Phục
META (155)  : PLC Mitsubishi báo đèn ERROR, BATT hoặc mất kết nối GX Works? Tổng hợp các lỗi PLC Mitsubishi FX/Q thường gặp, cách đọc mã lỗi và khắc phục nhanh, an toàn.
H1          : Lỗi PLC Mitsubishi (FX/Q) Thường Gặp Và Cách Khắc Phục

---

## Lỗi PLC Mitsubishi thường gặp là gì?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-plc.svg)


**Lỗi PLC Mitsubishi** hay gặp nhất trên dòng **FX (FX1N/FX2N/FX3U/FX5U)** và **Q/L, iQ-R** gồm: đèn **ERROR** sáng, đèn **BATT** báo pin yếu, PLC về STOP, mất chương trình, hoặc **không kết nối được GX Works**. Cách xử lý chung: **đọc đèn báo → đọc mã lỗi trong phần mềm → kiểm tra từ nguồn, pin, chương trình đến I/O và truyền thông.**

> **PLC Mitsubishi đang lỗi?** Gửi **model + mô tả đèn/mã lỗi** → [Tư vấn & báo giá sửa – thay thế PLC Mitsubishi](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-plc.svg)


---

## Đọc đèn báo trên PLC Mitsubishi

| Đèn | Bình thường | Khi lỗi |
|---|---|---|
| **POWER** | Sáng ổn định | Tắt = mất nguồn / hỏng bộ nguồn |
| **RUN** | Sáng = đang chạy | Tắt = ở STOP hoặc CPU lỗi |
| **ERROR / ERR** | Tắt | Sáng = lỗi CPU/chương trình; nhấp nháy = lỗi tham số/cấu hình |
| **BATT / BAT.V** | Tắt | Sáng = **pin nhớ yếu**, nguy cơ mất chương trình |

Với dòng Q, chú ý thêm đèn **MODE, USER, BAT, BOOT**. Dùng **GX Works2/GX Works3 → PLC Diagnostics** để đọc **mã lỗi và bước (step)** gây lỗi.

---

## Các lỗi PLC Mitsubishi và cách khắc phục

### 1. Đèn BATT sáng — pin yếu, nguy cơ mất chương trình

Dòng FX/Q lưu chương trình và vùng nhớ chốt bằng **pin**. Khi pin yếu (đèn BATT sáng), mất điện có thể **xóa chương trình**.

- **Backup chương trình ngay** bằng GX Works.
- **Thay pin đúng loại khi PLC còn điện** (ví dụ FX3U dùng pin chuyên dụng), không tháo pin lúc mất điện.
- Máy mới nên dùng dòng lưu **Flash/ROM** để bớt phụ thuộc pin.

### 2. Đèn ERROR sáng hoặc PLC về STOP

- **Sáng liên tục:** thường là lỗi **CPU/phần cứng** hoặc lỗi chương trình nặng.
- **Nhấp nháy:** thường là lỗi **tham số/cấu hình (parameter)** hoặc I/O.

Cách khắc phục: mở **PLC Diagnostics** đọc mã lỗi; kiểm tra các thanh ghi chẩn đoán **D8060–D8069** (ví dụ **D8061** lỗi phần cứng, **D8062** lỗi link, **D8063** lỗi truyền thông nối tiếp, **D8064** lỗi tham số, **D8065–D8066** lỗi cú pháp/mạch, **D8067** lỗi thực thi). Sửa đúng dòng lệnh/tham số rồi nạp lại.

### 3. Lỗi Watchdog (WDT) — scan quá dài

Chương trình quét vượt thời gian giám sát khiến PLC báo lỗi và dừng. Hãy **tối ưu chương trình**, tránh vòng lặp dài, kiểm tra lệnh nhảy; nếu cần, chỉnh **D8000 (thời gian WDT)** hợp lý.

### 4. Lỗi I/O và module mở rộng

Đèn I/O không khớp thực tế, hoặc báo lỗi **special block (BFM)**. Kiểm tra **cáp mở rộng lỏng**, địa chỉ module, nguồn cấp cho module; đo tín hiệu tại terminal; kênh cháy thì chuyển kênh dự phòng hoặc **thay module**.

### 5. Không kết nối được GX Works

- Sai **cổng COM/USB** hoặc thiếu **driver** (cáp FX-USB-AW/SC-09…).
- **Chọn sai PLC Type/Series** trong phần mềm.
- Cáp hỏng, hoặc đang kẹt ở chế độ khác.

Khắc phục: cài đúng driver, chọn đúng dòng CPU, thử cáp khác, kiểm tra Transfer Setup.

> ⚠️ **FX3U bị làm giả nhiều** — hàng giả rất hay lỗi vặt và chết sớm. Khi mua để thay thế, chọn nguồn chính hãng có kiểm tra, CO/CQ.

---

## Quy trình khắc phục lỗi PLC Mitsubishi

1. **Đọc đèn** POWER/RUN/ERROR/BATT.
2. **Kiểm tra nguồn** 220V/24V, cầu chì, terminal.
3. **Backup + xử lý pin/chương trình** (thay pin khi còn điện).
4. **Đọc mã lỗi** trong GX Works (PLC Diagnostics, D8060–D8069).
5. **Soát I/O & module** mở rộng, cáp, địa chỉ.
6. **Kiểm tra truyền thông/kết nối**, rồi sửa hoặc **thay thế + dự phòng**.

> **An toàn:** ngắt điện, khóa – treo biển (LOTO) trước khi tháo đấu dây.

---

## Khi nào nên thay PLC Mitsubishi?

- Pin yếu, lỏng terminal, sai tham số → **sửa tại chỗ**.
- Cháy kênh I/O → **thay module**.
- **CPU chết**, không nạp được → **thay CPU/PLC** cùng dòng để giữ chương trình.
- Dòng cũ (như **FX3U đang dần EOL**) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/) và [linh kiện ngừng sản xuất](/linh-kien-tu-dong-hoa-ngung-san-xuat/).

Xem thêm bài tổng quan: [các lỗi PLC thường gặp & cách khắc phục (mọi hãng)](/loi-plc-thuong-gap-cach-khac-phuc/) và [PLC Mitsubishi FX3U là gì, khi nào lên FX5U](/plc-mitsubishi-fx3u-la-gi/).

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Mitsubishi

Gửi cho chúng tôi: **model PLC (FX3U, FX5U, Q…) · mô tả đèn báo/mã lỗi · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá PLC/module/pin chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Mitsubishi](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-plc.svg)

## Câu hỏi thường gặp (FAQ)

**PLC Mitsubishi sáng đèn BATT phải làm gì?**
Đèn BATT báo **pin nhớ yếu**. Hãy **backup chương trình** rồi **thay pin khi PLC vẫn còn điện** để không mất RAM; dùng đúng loại pin cho dòng CPU.

**Đèn ERROR trên PLC Mitsubishi nghĩa là gì?**
Báo lỗi CPU/chương trình (sáng liên tục) hoặc lỗi tham số/cấu hình (nhấp nháy). Đọc **PLC Diagnostics** và thanh ghi **D8060–D8069** để biết mã lỗi cụ thể.

**Vì sao không kết nối được GX Works với PLC?**
Thường do **sai cổng/driver cáp** (FX-USB-AW…), **chọn sai dòng CPU**, hoặc cáp hỏng. Cài đúng driver, chọn đúng series và kiểm tra Transfer Setup.

**FX3U ngừng sản xuất, hỏng thì thay bằng gì?**
Có thể tìm **FX3U chính hãng còn tồn** để giữ nguyên hệ thống, hoặc nâng cấp lên **FX5U** (cần chuyển chương trình sang GX Works3, không cắm thay 1:1).

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Mitsubishi) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /plc-mitsubishi-fx3u-la-gi/, /thay-the-plc-module-doi-cu/, /linh-kien-tu-dong-hoa-ngung-san-xuat/, /lien-he/. -->
