<!--
LOẠI TRANG : Blog kỹ thuật (ứng dụng/thiết kế) + Thương mại
URL SLUG   : /tu-dien-plc/
TỪ KHÓA    : tủ điện plc | tủ điều khiển plc | thiết kế tủ plc | bố trí tủ điện plc | đấu tủ plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Tủ Điện PLC: Bố Trí, Thành Phần & Lưu Ý
META (148)  : Tủ điện PLC gồm những gì? Cách bố trí bảo vệ, nguồn, PLC, relay, terminal, HMI và lưu ý chống nhiễu – nối đất để tủ điều khiển PLC chạy ổn định.
H1          : Tủ Điện PLC: Bố Trí, Thành Phần Và Lưu Ý Thiết Kế

---

## Tủ điện PLC gồm những gì?

<!--IMG:rep-->
![Bố trí tủ điện PLC](assets/diagrams/tu-dien-plc.svg)


**Tủ điện PLC** (tủ điều khiển) là nơi lắp đặt PLC cùng các thiết bị phụ trợ để điều khiển máy móc an toàn, gọn gàng. Một tủ tiêu chuẩn gồm: **thiết bị bảo vệ (MCB/CB), bộ nguồn 24VDC, PLC + module I/O, relay trung gian, cầu đấu (terminal)** và thường có **HMI trên cánh tủ**. Bố trí hợp lý giúp **dễ đấu nối, chống nhiễu và dễ bảo trì**.

> **Cần thiết kế/đóng tủ điện PLC?** Gửi **yêu cầu điều khiển** → [Tư vấn & báo giá](#bao-gia).

---

## Các thành phần chính

- **Bảo vệ:** MCB/CB, aptomat, cầu chì — bảo vệ ngắn mạch/quá tải.
- **Bộ nguồn 24VDC:** cấp cho PLC, cảm biến, relay (tính dư tải).
- **PLC + module I/O:** bộ điều khiển trung tâm ([cấu tạo PLC](/cau-tao-plc/)).
- **Relay trung gian:** cách ly và bảo vệ ngõ ra PLC khi tải lớn.
- **Cầu đấu (terminal):** điểm đấu dây hiện trường gọn gàng.
- **HMI:** giao diện vận hành trên cánh tủ ([HMI là gì](/hmi-la-gi/)).

---

## Nguyên tắc bố trí

<!--IMG:prin-->
![Chống nhiễu và nối đất cho PLC](assets/diagrams/chong-nhieu-plc.svg)


- **Tách dây động lực và dây tín hiệu**, đi máng riêng, giao nhau vuông góc.
- Đặt **biến tần/thiết bị nhiễu** xa PLC; dùng **lọc nhiễu**.
- **Nối đất** tủ, PLC và màn chống nhiễu về điểm đất chung.
- Bố trí **thông gió/làm mát** (quạt lọc/điều hòa) tránh quá nhiệt.
- Đi dây gọn, **đánh số terminal**, chừa không gian mở rộng.

---

## Lưu ý an toàn và bảo trì

<!--IMG:app-->
![Cấu tạo PLC](assets/diagrams/cautao-plc.svg)


- **Dừng khẩn (E-Stop)** cắt trực tiếp mạch động lực.
- Tuân thủ **an toàn điện (LOTO)** khi thao tác.
- Dán **sơ đồ đấu nối**, ghi IP/thông số để bảo trì nhanh.

Xem thêm: [lỗi PLC do nhiễu](/loi-plc-do-nhieu/) và [bảo trì PLC định kỳ](/bao-tri-plc-dinh-ky/).

---

## Các bước đóng một tủ điện PLC

1. **Thiết kế sơ đồ:** liệt kê I/O, chọn PLC/thiết bị, vẽ sơ đồ nguyên lý và đấu nối.
2. **Bố trí thiết bị** trên tấm nền: bảo vệ – nguồn – PLC – relay – terminal hợp lý, chừa khoảng mở rộng.
3. **Đi dây:** tách động lực/tín hiệu, đánh số đầu dây, dùng máng và đầu cốt.
4. **Nối đất & chống nhiễu** đúng chuẩn.
5. **Kiểm tra nguội** (thông mạch, cách điện) trước khi cấp điện.
6. **Nạp chương trình, chạy thử** từng chức năng, rồi vận hành đầy đủ.

## Kích thước và cấp bảo vệ tủ

Chọn **kích thước tủ** đủ chỗ cho thiết bị và tản nhiệt; chọn **cấp bảo vệ (IP)** phù hợp môi trường (bụi, ẩm). Môi trường khắc nghiệt cần **quạt lọc/điều hòa tủ** và gioăng kín.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá

Gửi cho chúng tôi: **yêu cầu điều khiển · số I/O · thiết bị hiện trường.** Chúng tôi tư vấn thiết kế tủ và **báo giá PLC, HMI, thiết bị**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Tủ điện PLC gồm những thiết bị nào?**
Gồm **bảo vệ (MCB/CB), bộ nguồn 24VDC, PLC + module I/O, relay trung gian, terminal** và thường có **HMI** trên cánh tủ.

**Bố trí tủ PLC cần lưu ý gì để chống nhiễu?**
**Tách dây động lực khỏi dây tín hiệu**, đặt biến tần xa PLC, **nối đất tốt** và dùng lọc nhiễu; đảm bảo thông gió tránh quá nhiệt.

**Vì sao ngõ ra PLC nên qua relay trung gian?**
Để **cách ly và bảo vệ** ngõ ra khi điều khiển tải lớn/tải cảm, tránh cháy kênh output của PLC.

**Nên chừa dư không gian trong tủ điện PLC không?**
Nên. Chừa **khoảng trống và cầu đấu dự phòng** giúp dễ **mở rộng I/O** và bảo trì về sau mà không phải thay hay đóng lại tủ.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Tủ điện PLC) + Article.
     INTERNAL LINK RA: /cau-tao-plc/, /hmi-la-gi/, /loi-plc-do-nhieu/, /bao-tri-plc-dinh-ky/, /lien-he/. -->
