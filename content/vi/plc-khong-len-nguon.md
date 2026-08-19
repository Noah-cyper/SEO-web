<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting theo triệu chứng + dịch vụ)
URL SLUG   : /plc-khong-len-nguon/
TỪ KHÓA    : plc không lên nguồn | plc mất nguồn | đèn power plc tắt | plc không lên đèn | sụt áp 24v plc | plc chập chờn
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : PLC Không Lên Nguồn: Nguyên Nhân & Cách Khắc Phục
META (155)  : PLC không lên nguồn, đèn POWER tắt hoặc chập chờn? Nguyên nhân (cầu chì, bộ nguồn, sụt áp 24V, đấu sai) và cách khắc phục PLC không lên nguồn an toàn.
H1          : PLC Không Lên Nguồn (Đèn POWER Tắt): Nguyên Nhân Và Cách Khắc Phục

---

## Vì sao PLC không lên nguồn?

<!--IMG:rep-->
![PLC không lên nguồn: chuỗi cấp nguồn và điểm hay lỗi](assets/diagrams/power-plc.svg)


**PLC không lên nguồn** — đèn **POWER tắt hoàn toàn** hoặc **chập chờn, reset ngẫu nhiên** — thường không phải do CPU chết, mà do **chuỗi cấp nguồn**: mất điện lưới, đứt cầu chì, hỏng bộ nguồn 24VDC, **sụt áp do quá tải**, hoặc đấu sai/ngược cực. Kiểm tra tuần tự **từ nguồn vào đến PLC** sẽ tìm ra nguyên nhân nhanh.

> **PLC không lên nguồn?** Gửi **model + cách cấp nguồn (220V/24V)** → [Tư vấn kỹ thuật & báo giá bộ nguồn/PLC](#bao-gia).

---

## Nguyên nhân và cách khắc phục

### 1. Mất nguồn cấp / đứt cầu chì

- Đo điện áp cấp (**220VAC** hoặc **24VDC**) tại chân nguồn PLC.
- Kiểm tra **cầu chì, aptomat/CB, đầu cốt lỏng**; thay cầu chì đúng trị số.

### 2. Hỏng bộ nguồn 24VDC

Nếu 220V có nhưng ngõ ra 24V không đủ/không có → **bộ nguồn hỏng**. Đo ngõ ra bộ nguồn; thay bộ nguồn đúng công suất.

### 3. Sụt áp 24V do quá tải

Cấp 24V cho **quá nhiều cảm biến/van/relay** khiến điện áp tụt, PLC reset chập chờn. → **Tách tải**, dùng bộ nguồn công suất lớn hơn, tách riêng nguồn điều khiển và nguồn tải.

### 4. Đấu sai / ngược cực / sai điện áp

- Đấu **ngược cực 24V**, hoặc **cấp 220V vào ngõ 24V** (dễ gây hỏng).
- Kiểm tra kỹ sơ đồ chân nguồn theo tài liệu PLC.

### 5. Chập tải kéo nguồn xuống

Một ngõ ra hoặc thiết bị bị **chập** làm sập nguồn. Tháo bớt tải, cấp nguồn riêng để khoanh vùng điểm chập.

---

## Quy trình kiểm tra PLC không lên nguồn

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Ngắt điện, LOTO** trước khi thao tác.
2. **Đo điện áp cấp** 220VAC/24VDC tại chân nguồn.
3. **Kiểm tra cầu chì/CB/terminal** lỏng, thay đúng trị số.
4. **Đo ngõ ra bộ nguồn 24V**; tách bớt tải nếu sụt áp.
5. **Rà đấu nối** đúng cực, đúng điện áp.
6. **Khoanh vùng điểm chập**; nếu bộ nguồn/PLC hỏng thì thay thế.

---

## Khi nào cần thay bộ nguồn hoặc PLC?

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- Đứt cầu chì, lỏng terminal, quá tải 24V → **sửa tại chỗ**.
- **Bộ nguồn hỏng** → thay bộ nguồn đúng công suất.
- **Module nguồn/PLC chết** (đã loại trừ nguồn ngoài) → **thay thế**.

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/) và nếu PLC đời cũ khó tìm, [thay thế PLC & module đời cũ](/thay-the-plc-module-doi-cu/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **model PLC · cách cấp nguồn (220V/24V) · hiện tượng (tắt hẳn/chập chờn) · tải đang đấu.** Chúng tôi tư vấn và **báo giá bộ nguồn/PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PLC không lên đèn POWER thì kiểm tra gì đầu tiên?**
Đo **điện áp cấp** (220VAC hoặc 24VDC) tại chân nguồn PLC và kiểm tra **cầu chì/CB**. Nếu không có điện vào là do nguồn ngoài, không phải PLC.

**PLC lên nguồn chập chờn, reset liên tục vì sao?**
Thường do **sụt áp 24V vì quá tải** hoặc đấu nối lỏng. Tách bớt tải 24V, dùng bộ nguồn lớn hơn và siết lại terminal.

**Cấp nhầm 220V vào ngõ 24V có sao không?**
Rất dễ **hỏng bộ nguồn/PLC**. Luôn kiểm tra đúng điện áp và đúng cực trước khi cấp; nếu đã cấp nhầm, cần kiểm tra kỹ trước khi chạy lại.

**PLC lên nguồn (POWER sáng) nhưng vẫn không chạy, RUN tắt thì sao?**
Khi POWER sáng mà RUN tắt thì **không còn là lỗi nguồn** — PLC đang ở **STOP** hoặc **lỗi CPU/chương trình**. Kiểm tra công tắc RUN/STOP, đọc mã lỗi trong phần mềm và xem thêm [các lỗi PLC thường gặp](/loi-plc-thuong-gap-cach-khac-phuc/).

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › PLC không lên nguồn) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /thay-the-plc-module-doi-cu/, /lien-he/. -->
