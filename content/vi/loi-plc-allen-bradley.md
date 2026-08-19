<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo hãng + dịch vụ sửa/thay thế)
URL SLUG   : /loi-plc-allen-bradley/
TỪ KHÓA    : lỗi plc allen-bradley | lỗi plc allen bradley | plc rockwell báo lỗi | major fault | lỗi compactlogix micrologix | studio 5000 báo lỗi
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Đối chiếu đèn OK/FAULT và Major Fault Type/Code theo tài liệu Rockwell trước khi lên web.
-->

TITLE TAG   : Lỗi PLC Allen-Bradley: Đèn OK Đỏ & Cách Khắc Phục
META (154)  : PLC Allen-Bradley báo đèn OK đỏ, major fault hay lỗi I/O? Cách đọc Major Fault Type/Code trong Studio 5000 và khắc phục lỗi PLC Allen-Bradley thường gặp.
H1          : Lỗi PLC Allen-Bradley (Rockwell) Và Cách Khắc Phục

---

## Lỗi PLC Allen-Bradley thường gặp là gì?

<!--IMG:rep-->
![Lỗi PLC Allen-Bradley: đèn OK đỏ báo major fault](assets/diagrams/rep-loi-allen-bradley.svg)


**Lỗi PLC Allen-Bradley** (Rockwell — dòng **MicroLogix, SLC500, CompactLogix, ControlLogix, Micro800**) hay gặp: đèn **OK đỏ** (major fault), đèn **I/O** báo lỗi module, **FAULT** trên MicroLogix, hoặc mất truyền thông. Cách xử lý: **đọc đèn → đọc Major Fault (Type/Code) trong phần mềm → xử lý theo mã lỗi.**

> **PLC Allen-Bradley đang lỗi?** Gửi **model + Major Fault Type/Code** → [Tư vấn & báo giá sửa – thay thế PLC Allen-Bradley](#bao-gia).

---

## Đọc đèn báo trên PLC Allen-Bradley

| Đèn | Ý nghĩa |
|---|---|
| **OK** | Xanh = bình thường; **đỏ nhấp nháy = major fault (khắc phục được)**; **đỏ liên tục = lỗi nặng/không phục hồi** |
| **RUN** | Sáng = đang chạy chương trình |
| **I/O** | Nhấp nháy/đỏ = lỗi module hoặc kết nối I/O |
| **FORCE** | Sáng = đang ép (force) I/O — cần lưu ý khi chạy |
| **FAULT** (MicroLogix) | Đỏ = có lỗi; đọc code trong RSLogix 500 |

Công cụ: **Studio 5000 Logix Designer** (CompactLogix/ControlLogix), **RSLogix 500** (SLC/MicroLogix), **Connected Components Workbench** (Micro800).

---

## Các lỗi PLC Allen-Bradley và cách khắc phục

### 1. Đèn OK đỏ — Major Fault

Controller vào **major fault** và dừng. Kết nối phần mềm, mở **Controller Properties → Major Faults** để đọc **Type/Code** (ví dụ lỗi chương trình, truy xuất mảng ngoài phạm vi, watchdog). Sửa theo mã, xử lý fault routine, rồi **clear fault** và chuyển RUN.

### 2. Lỗi I/O module

Đèn I/O báo lỗi kết nối/cấu hình module (đèn trạng thái module đỏ). Kiểm tra **module, cáp, RPI/cấu hình**, so I/O tree với thực tế; thay module nếu hỏng.

### 3. Watchdog / lỗi chương trình

Task quét vượt watchdog hoặc lỗi logic → major fault Type 6. **Tối ưu chương trình**, kiểm tra vòng lặp/mảng, đặt watchdog hợp lý.

### 4. Pin yếu (BAT) dòng cũ

SLC500/ControlLogix đời cũ dùng **pin** giữ chương trình/RAM. Đèn BAT báo yếu → **backup**, **thay pin khi còn điện**.

### 5. Lỗi truyền thông (EtherNet/IP, DH+, RS232)

- Sai **IP/subnet**, trùng IP (EtherNet/IP).
- Sai node/cấu hình DH+/DH-485.

Khắc phục: đặt IP đúng lớp mạng, đúng node, kiểm tra cáp/switch.

---

## Quy trình khắc phục lỗi PLC Allen-Bradley

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Đọc đèn** OK/RUN/I/O/FORCE.
2. **Kiểm tra nguồn** và đấu nối.
3. **Đọc Major Fault Type/Code** trong Studio 5000/RSLogix.
4. **Soát I/O tree & module.**
5. **Kiểm tra truyền thông** (EtherNet/IP, node).
6. **Clear fault, sửa hoặc thay thế + dự phòng.**

> **An toàn:** ngắt điện, LOTO trước khi thao tác.

---

## Khi nào nên thay PLC Allen-Bradley?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Lỗi chương trình, cấu hình, pin → **sửa/nạp lại**.
- Module I/O hỏng → **thay module**.
- **Controller chết** → thay cùng dòng, nạp lại từ backup.
- Dòng cũ (SLC500, PLC-5 EOL) khó tìm → xem [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/) và [linh kiện ngừng sản xuất](/linh-kien-tu-dong-hoa-ngung-san-xuat/).

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và [lỗi truyền thông PLC – HMI, Modbus](/loi-truyen-thong-plc-hmi-modbus/).

---

## Phòng ngừa lỗi PLC Allen-Bradley

- **Backup project** (Studio 5000/RSLogix) kèm ghi chú phiên bản.
- **Thay pin định kỳ** cho dòng cũ (SLC500/ControlLogix) trước khi đèn BAT báo yếu.
- **Dự phòng** controller/module I/O cho dây chuyền quan trọng.
- **Chống nhiễu và nối đất** đúng chuẩn; kiểm tra cáp EtherNet/IP.
- Ghi lại **IP, node và cấu hình I/O tree** để khôi phục nhanh.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá sửa – thay thế PLC Allen-Bradley

Gửi cho chúng tôi: **model (CompactLogix, MicroLogix…) · Major Fault Type/Code · hiện tượng · số I/O.** Chúng tôi tư vấn hướng khắc phục và **báo giá controller/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC Allen-Bradley](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đèn OK đỏ trên PLC Allen-Bradley nghĩa là gì?**
**Đỏ nhấp nháy = major fault khắc phục được**; **đỏ liên tục = lỗi nặng/không phục hồi**. Đọc **Major Fault Type/Code** trong Studio 5000 để biết nguyên nhân.

**Major Fault Type/Code đọc ở đâu?**
Trong **Controller Properties → Major Faults** (Studio 5000) hoặc cửa sổ lỗi của RSLogix 500. Type/Code cho biết nhóm và mã lỗi cụ thể.

**PLC Allen-Bradley báo pin yếu (BAT) thì sao?**
Dòng cũ dùng pin giữ chương trình. Hãy **backup**, **thay pin khi controller còn điện** để không mất dữ liệu.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi PLC Allen-Bradley) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-truyen-thong-plc-hmi-modbus/, /thay-the-plc-module-doi-cu/, /linh-kien-tu-dong-hoa-ngung-san-xuat/, /lien-he/. -->
