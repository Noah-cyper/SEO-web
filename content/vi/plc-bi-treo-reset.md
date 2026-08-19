<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo triệu chứng + dịch vụ)
URL SLUG   : /plc-bi-treo-reset/
TỪ KHÓA    : plc bị treo | plc reset liên tục | plc tự khởi động lại | plc bị đứng | watchdog plc | plc chạy không ổn định
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : PLC Bị Treo / Reset Liên Tục: Nguyên Nhân & Khắc Phục
META (151)  : PLC bị treo, tự reset hoặc chạy chập chờn? Nguyên nhân (nguồn, nhiễu, watchdog, chương trình, nhiệt) và cách khắc phục PLC bị treo/reset ổn định.
H1          : PLC Bị Treo / Reset Liên Tục: Nguyên Nhân Và Cách Khắc Phục

---

## Vì sao PLC bị treo hoặc reset liên tục?

<!--IMG:rep-->
![PLC bị treo/reset: các nhóm nguyên nhân](assets/diagrams/app-nhom-loi-plc.svg)


**PLC bị treo** (đứng, không quét chương trình) hoặc **tự reset liên tục** là lỗi khó chịu vì **khó tái hiện**. Nguyên nhân thường thuộc bốn nhóm: **nguồn không ổn định, nhiễu điện từ, lỗi chương trình/watchdog** và **nhiệt độ/môi trường**. Xác định đúng nhóm giúp xử lý dứt điểm thay vì reset tạm thời.

> **PLC treo/reset liên tục?** Gửi **model + khi nào hay xảy ra** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## Nguyên nhân và cách khắc phục

### 1. Nguồn không ổn định / sụt áp

Sụt áp 24V khi tải nặng, nguồn yếu, terminal lỏng → PLC reset. **Tách tải 24V**, dùng bộ nguồn lớn hơn, siết terminal, cấp nguồn ổn định.

### 2. Nhiễu điện từ

Nhiễu từ **biến tần, động cơ, đóng cắt contactor** làm PLC treo/reset ngẫu nhiên. → **Tách dây tín hiệu khỏi động lực**, cáp chống nhiễu, **nối đất tốt**, lắp lọc nhiễu cho biến tần.

### 3. Lỗi chương trình / Watchdog

Vòng lặp dài, truy xuất địa chỉ sai, chia cho 0 → **watchdog** kích hoạt làm PLC dừng/khởi động lại. Đọc **mã lỗi trong phần mềm**, tối ưu chương trình, kiểm tra vòng lặp và tầm địa chỉ.

### 4. Nhiệt độ / môi trường

Tủ quá nóng, ẩm, rung → linh kiện chập chờn. → **Làm mát tủ**, chống ẩm, chống rung, chừa thông gió cho PLC.

### 5. Phần cứng xuống cấp

Tụ nguồn phồng, mối hàn nứt, pin cạn → cần **kiểm tra/sửa hoặc thay** CPU/bộ nguồn.

---

## Quy trình khoanh vùng lỗi treo/reset

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Ghi lại điều kiện** khi lỗi xảy ra (tải nặng, trời nóng, khi biến tần chạy…).
2. **Đo nguồn 24V** lúc tải nặng, kiểm tra sụt áp.
3. **Đọc mã lỗi/watchdog** trong phần mềm.
4. **Kiểm tra nhiễu & nối đất**, tách dây.
5. **Đo nhiệt độ tủ**, cải thiện làm mát.
6. **Nghi ngờ phần cứng → kiểm tra/thay** nếu các bước trên không dứt điểm.

> **An toàn:** ngắt điện, LOTO trước khi thao tác phần cứng.

---

## Khi nào cần sửa/thay PLC?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Nguồn, nhiễu, nhiệt, chương trình → **xử lý tại chỗ**, thường dứt điểm.
- **Phần cứng xuống cấp** (tụ, mối hàn, CPU) → **sửa hoặc thay** CPU/bộ nguồn.

Xem thêm: [lỗi PLC do nhiễu & nối đất](/loi-plc-do-nhieu/) và [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **model PLC · điều kiện hay lỗi · sơ đồ nguồn/nối đất.** Chúng tôi tư vấn khoanh vùng và **báo giá linh kiện/PLC** nếu cần.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PLC tự reset liên tục là do đâu?**
Phổ biến nhất là **sụt áp nguồn 24V khi tải nặng** và **nhiễu điện từ**. Đo nguồn lúc tải nặng, tách dây tín hiệu khỏi động lực và nối đất tốt.

**PLC bị treo (đứng) nhưng đèn POWER vẫn sáng?**
Thường do **watchdog/lỗi chương trình** hoặc nhiễu. Đọc mã lỗi trong phần mềm, tối ưu chương trình và kiểm tra chống nhiễu.

**Lỗi treo/reset khó tái hiện thì xử lý sao?**
**Ghi lại điều kiện xảy ra** (tải, nhiệt, thời điểm biến tần chạy) để khoanh vùng; xử lý lần lượt nguồn → nhiễu → nhiệt → chương trình.

**PLC chỉ treo/reset khi máy chạy tải nặng, nguyên nhân?**
Rất có thể **sụt áp nguồn 24V** hoặc **nhiễu tăng mạnh khi động cơ/biến tần chạy nặng**. Hãy đo nguồn ngay lúc tải nặng và cải thiện chống nhiễu, nối đất; xem thêm [lỗi PLC do nhiễu](/loi-plc-do-nhieu/).

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › PLC bị treo/reset) + Article.
     INTERNAL LINK RA: /loi-plc-do-nhieu/, /loi-plc-thuong-gap-cach-khac-phuc/, /lien-he/. -->
