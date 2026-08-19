<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-ls/
TỪ KHÓA    : lỗi plc ls | plc ls báo lỗi | đèn err ls | xg5000 báo lỗi | lỗi plc lsis | plc ls xgb xgt
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu tên đèn/PLC Error theo tài liệu LS Electric trước khi lên web.
-->

TITLE TAG   : Lỗi PLC LS (XGB/XGT): Đèn ERR & Cách Khắc Phục
META (150)  : PLC LS (LSIS) XGB/XGK/XGT báo đèn ERR hay lỗi cấu hình? Cách đọc mã lỗi trong XG5000 và khắc phục các lỗi PLC LS thường gặp nhanh, an toàn.
H1          : Lỗi PLC LS (XGB/XGK/XGT) Thường Gặp Và Cách Khắc Phục

---

## Lỗi PLC LS thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC LS: đèn ERR báo lỗi](assets/diagrams/rep-loi-ls.svg)


**Lỗi PLC LS** (LS Electric / LSIS) hay gặp trên dòng **XGB, XGK/XGI, XGT** và **Master-K, GLOFA** gồm: đèn **ERR** sáng/nhấp nháy, PLC ở STOP, **lỗi cấu hình**, pin yếu hoặc mất truyền thông. Cách xử lý chung: **đọc đèn → đọc mã lỗi trong XG5000 → kiểm tra từ nguồn, chương trình đến I/O và truyền thông.**

> **PLC LS đang lỗi?** Gửi **model + mã lỗi** → [Tư vấn & báo giá sửa – thay thế PLC LS](#bao-gia).

---

## Đọc đèn báo trên PLC LS

| Đèn | Bình thường | Khi lỗi |
|---|---|---|
| **PWR** | Sáng | Tắt = mất nguồn / hỏng bộ nguồn |
| **RUN** | Sáng = đang chạy | Tắt = ở STOP hoặc lỗi |
| **STOP** | Tắt khi chạy | Sáng = đang dừng |
| **ERR** | Tắt | Sáng/nhấp nháy = lỗi hệ thống, cấu hình hoặc I/O |

Công cụ: **XG5000** (XGT/XGB), **KGLWIN** (Master-K), **GMWIN** (GLOFA) → cửa sổ **PLC Error/Warning** để đọc mã lỗi; kiểm tra cờ báo lỗi cấu hình **_CNF_ER** và vùng cờ hệ thống (F/K).

---

## Các lỗi PLC LS và cách khắc phục

### 1. Đèn ERR sáng — lỗi hệ thống/cấu hình

Thường là **lỗi cấu hình I/O**, sai module so với khai báo, hoặc lỗi bộ nhớ. Mở **XG5000 → PLC Error** đọc mã lỗi; so **I/O configuration** với thực tế; nạp lại chương trình đúng cấu hình.

### 2. Lỗi Watchdog (scan) 

Chương trình quét quá dài vượt thời gian giám sát. **Tối ưu chương trình**, tách tác vụ nặng, kiểm tra vòng lặp và lệnh nhảy.

### 3. Pin yếu / mất dữ liệu chốt

Một số dòng XGK dùng **pin** giữ vùng nhớ chốt và đồng hồ. Khi báo yếu: **backup**, **thay pin khi PLC còn điện**, dùng đúng loại.

### 4. Lỗi I/O và module

Đèn/trạng thái I/O không khớp thực tế, hoặc báo lỗi module mở rộng. Kiểm tra **cáp, base, địa chỉ module**, đo tín hiệu tại terminal, thay module nếu kênh cháy.

### 5. Lỗi truyền thông & kết nối XG5000

- Sai thông số **Cnet (RS232/485)** hoặc **Enet (Ethernet)**, sai IP.
- Không kết nối XG5000: sai **cổng/driver**, chọn sai **CPU type**, cáp hỏng.

Khắc phục: đồng bộ thông số, đúng IP cùng lớp mạng, chọn đúng dòng CPU trong Online Settings.

---

## Quy trình khắc phục lỗi PLC LS

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** PWR/RUN/STOP/ERR.
2. **Kiểm tra nguồn** và đấu nối.
3. **Đọc mã lỗi** trong XG5000 (PLC Error, _CNF_ER).
4. **Soát cấu hình I/O & module** so thực tế.
5. **Kiểm tra truyền thông/kết nối** (Cnet/Enet, IP).
6. **Sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác phần cứng.

---

## Khi nào nên thay PLC LS?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Cấu hình, thông số, pin → **sửa/nạp lại**.
- Module I/O cháy → **thay module**.
- **CPU chết** → thay CPU cùng dòng, nạp lại chương trình.
- Dòng cũ (Master-K, GLOFA) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC LS

- **Backup chương trình** (XG5000) kèm ghi chú phiên bản, lưu an toàn.
- **Thay pin định kỳ** cho dòng có pin để giữ vùng nhớ chốt và đồng hồ.
- **Dự phòng** CPU/module cho dây chuyền quan trọng.
- **Chống nhiễu**: tách dây tín hiệu khỏi động lực, nối đất tốt, siết cọc đấu.
- Ghi lại **cấu hình I/O và thông số truyền thông** (Cnet/Enet) để khôi phục nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC LS

Gửi cho chúng tôi: **model PLC (XGB, XGK, XGI…) · mã lỗi/đèn báo · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá CPU/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC LS](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn ERR trên PLC LS báo gì?**
Báo **lỗi hệ thống/cấu hình hoặc I/O**. Mở **XG5000 → PLC Error** để đọc mã lỗi cụ thể và kiểm tra cấu hình I/O so với thực tế.

**Không kết nối được XG5000 với PLC LS?**
Kiểm tra **cổng/driver**, chọn đúng **CPU type**, đặt đúng thông số **Cnet/Enet** (hoặc IP cùng lớp mạng) trong Online Settings.

**PLC LS báo pin yếu thì sao?**
Với dòng có pin, hãy **backup**, **thay pin khi PLC còn điện** bằng đúng loại để giữ vùng nhớ chốt và đồng hồ.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC LS) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
