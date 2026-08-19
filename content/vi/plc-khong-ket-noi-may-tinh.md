<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo triệu chứng + dịch vụ)
URL SLUG   : /plc-khong-ket-noi-may-tinh/
TỪ KHÓA    : plc không kết nối máy tính | không nạp được chương trình plc | lỗi driver cáp plc | plc không kết nối phần mềm | lỗi cổng com plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : PLC Không Kết Nối Máy Tính: Nguyên Nhân & Khắc Phục
META (153)  : PLC không kết nối máy tính, không nạp được chương trình? Nguyên nhân (cáp, driver, cổng COM, sai model, IP) và cách khắc phục PLC không kết nối máy tính.
H1          : PLC Không Kết Nối Máy Tính (Không Nạp Được Chương Trình): Cách Khắc Phục

---

## Vì sao PLC không kết nối máy tính?

<!--IMG:rep-->
![PLC không kết nối máy tính: cổng, driver, model](assets/diagrams/ket-noi-pc-plc.svg)


**PLC không kết nối máy tính** — phần mềm báo *"cannot connect / timeout"*, không nạp được chương trình — hầu hết do phía **kết nối và cấu hình**: sai **cáp/cổng**, thiếu **driver**, **chọn sai model/loại cổng**, hoặc sai **IP** (với Ethernet). Rất hiếm khi do CPU hỏng.

> **Không kết nối được PLC?** Gửi **model PLC + loại cáp/cổng đang dùng** → [Tư vấn kỹ thuật & báo giá cáp/PLC](#bao-gia).

---

## Nguyên nhân và cách khắc phục

### 1. Cáp và cổng sai / hỏng

- Dùng **đúng loại cáp lập trình** (USB, RS232, RS485, Ethernet) cho dòng PLC.
- Thử **cáp khác**; kiểm tra đầu cắm lỏng.

### 2. Thiếu / sai driver

Cáp **USB-Serial** cần **driver** đúng (ví dụ cáp lập trình Mitsubishi, Delta…). Cài driver, kiểm tra **Device Manager** xem cổng COM có nhận không.

### 3. Sai cổng COM / thông số

- Chọn **đúng cổng COM** trong phần mềm.
- Đồng bộ **baud/parity** với PLC (một số cổng lập trình cố định thông số).

### 4. Chọn sai model / loại kết nối

Chọn **đúng dòng CPU/PLC type** và **đúng kiểu kết nối** (USB/COM/Ethernet) trong Transfer/Online Settings.

### 5. Ethernet: sai IP / mạng

- Đặt **IP máy tính cùng lớp mạng** với PLC, không trùng.
- Kiểm tra bằng lệnh **ping**; tắt tường lửa chặn; đúng cổng/giao diện.

### 6. PLC đang bận / bị khóa

PLC có thể **bị đặt mật khẩu**, đang ở chế độ khác, hoặc cổng đang bị phần mềm khác chiếm. Đóng phần mềm khác, kiểm tra chế độ và mật khẩu.

---

## Quy trình kiểm tra kết nối

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Kiểm tra cáp/đầu cắm** và thử cáp khác.
2. **Cài/kiểm tra driver**, xem cổng COM trong Device Manager.
3. **Chọn đúng model + kiểu kết nối** trong phần mềm.
4. **Đồng bộ cổng/thông số** (COM/baud) hoặc **IP cùng lớp mạng**.
5. **Ping** kiểm tra (Ethernet); tắt tường lửa nếu cần.
6. **Kiểm tra mật khẩu/chế độ PLC**.

---

## Khi nào là lỗi phần cứng?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


Nếu đã đúng cáp/driver/model/IP mà vẫn không kết nối trên **nhiều máy tính**, nghi ngờ **cổng lập trình của PLC hỏng** — cần kiểm tra/sửa hoặc thay CPU.

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá cáp/PLC

Gửi cho chúng tôi: **model PLC · loại cáp/cổng · phần mềm đang dùng · thông báo lỗi.** Chúng tôi tư vấn và **báo giá cáp lập trình/PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PLC không kết nối máy tính, kiểm tra gì trước?**
Kiểm tra **cáp/đầu cắm**, **driver** (cổng COM có nhận không), rồi chọn **đúng model và kiểu kết nối** trong phần mềm.

**Cắm cáp USB nhưng phần mềm không thấy PLC?**
Thường do **thiếu driver USB-Serial** hoặc chọn **sai cổng COM**. Cài driver, xem Device Manager và chọn đúng cổng.

**Kết nối PLC qua Ethernet không được?**
Đặt **IP máy tính cùng lớp mạng** với PLC (không trùng), **ping** kiểm tra, chọn đúng giao diện mạng và tắt tường lửa chặn.

**Kết nối được nhưng nạp chương trình báo lỗi giữa chừng thì sao?**
Có thể do **cáp chập chờn, nhiễu, hoặc PLC đang chạy/bị khóa**. Dùng cáp tốt, tránh nhiễu, chuyển PLC về đúng chế độ cho phép ghi rồi thử lại. Nếu PLC đặt **mật khẩu**, cần nhập đúng mật khẩu mới nạp được.

**Windows mới không nhận cáp lập trình đời cũ?**
Nhiều cáp **USB-Serial đời cũ** cần **driver tương thích Windows 10/11**. Hãy cài đúng driver của hãng, hoặc dùng cáp/bộ chuyển đổi được hỗ trợ và kiểm tra cổng COM trong Device Manager.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › PLC không kết nối máy tính) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /lien-he/. -->
