<!--
LOẠI TRANG : Blog kỹ thuật (kiến thức) + Thương mại
URL SLUG   : /hmi-la-gi/
TỪ KHÓA    : hmi là gì | màn hình hmi | hmi và plc | hmi weintek | chức năng hmi | kết nối hmi với plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : HMI Là Gì? Chức Năng Và Kết Nối HMI Với PLC
META (150)  : HMI là gì? Tìm hiểu màn hình HMI, chức năng giám sát – điều khiển, cách kết nối HMI với PLC và cách chọn HMI phù hợp cho hệ thống tự động hóa.
H1          : HMI Là Gì? Chức Năng Và Cách Kết Nối HMI Với PLC

---

## HMI là gì?

<!--IMG:rep-->
![HMI là gì - kết nối PLC HMI SCADA](assets/diagrams/topo-plc-hmi-scada.svg)


**HMI là gì?** HMI (viết tắt của **Human–Machine Interface** — *giao diện người–máy*) là **màn hình cảm ứng** giúp người vận hành **theo dõi và điều khiển** máy móc: xem thông số, ra lệnh chạy/dừng, cài đặt, và **cảnh báo lỗi**. HMI thường **kết nối với PLC** để hiển thị dữ liệu và gửi lệnh xuống PLC.

> **Cần tư vấn HMI + PLC?** Gửi **yêu cầu ứng dụng** → [Tư vấn & báo giá HMI/PLC](#bao-gia).

---

## Chức năng chính của HMI

- **Giám sát:** hiển thị trạng thái, thông số, đồ thị theo thời gian thực.
- **Điều khiển:** nút bấm ảo, cài đặt tham số, chạy/dừng.
- **Cảnh báo (alarm):** báo lỗi, lịch sử sự kiện.
- **Lưu dữ liệu:** ghi số liệu, xuất báo cáo (tùy dòng).

---

## HMI kết nối với PLC như thế nào?

<!--IMG:prin-->
![Nguyên lý PLC](assets/diagrams/prin-plc.svg)


HMI kết nối PLC qua **RS232/RS485 (Modbus)** hoặc **Ethernet (Modbus TCP…)**. HMI đọc/ghi **thanh ghi của PLC** để hiển thị và điều khiển. Cần **đồng bộ thông số** (baud/ID hoặc IP) và **ánh xạ đúng địa chỉ**; sai thông số sẽ gây [mất kết nối PLC–HMI](/loi-truyen-thong-plc-hmi-modbus/).

---

## HMI, PLC và SCADA khác nhau thế nào?

<!--IMG:app-->
![Kết nối PLC HMI SCADA](assets/diagrams/topo-plc-hmi-scada.svg)


- **PLC:** bộ điều khiển (bộ não).
- **HMI:** màn hình vận hành **tại máy/tủ**.
- **SCADA:** hệ **giám sát – điều khiển tập trung** nhiều máy trên máy tính/mạng.

Xem thêm: [SCADA là gì](/scada-la-gi/) và [PLC là gì](/plc-la-gi/).

---

## Các loại màn hình HMI

- **Theo kích thước:** từ 4.3", 7", 10" đến 15" — chọn theo lượng thông tin và không gian tủ.
- **Theo tính năng:** HMI cơ bản (hiển thị/điều khiển) và HMI nâng cao (đồ thị, lưu dữ liệu, web server, cảnh báo qua email).
- **Theo môi trường:** loại thường và loại chịu bụi/nước (IP cao) cho hiện trường khắc nghiệt.

## Chọn HMI phù hợp

Cân nhắc **kích thước màn hình, cổng truyền thông, số thanh ghi/màn hình, thương hiệu** (Weintek, Delta, Siemens, Proface…) và **khả năng tương thích với PLC** đang dùng. Nên chọn HMI có **cùng hệ giao thức** với PLC (Modbus/Ethernet) để ghép nối dễ dàng, và dự phòng bộ nhớ/màn hình cho mở rộng sau này.

---

<a name="bao-gia"></a>
## Tư vấn & báo giá HMI/PLC

Gửi cho chúng tôi: **model PLC · kích thước HMI · giao thức · số màn hình.** Chúng tôi tư vấn ghép nối và **báo giá HMI/PLC chính hãng**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**HMI là viết tắt của gì?**
HMI là **Human–Machine Interface** — *giao diện người–máy*, thường là **màn hình cảm ứng** để giám sát và điều khiển máy móc.

**HMI kết nối với PLC bằng gì?**
Qua **RS232/RS485 (Modbus)** hoặc **Ethernet (Modbus TCP…)**. Cần đồng bộ thông số và ánh xạ đúng thanh ghi PLC.

**HMI và SCADA khác nhau thế nào?**
**HMI** là màn hình vận hành **tại máy**; **SCADA** là hệ **giám sát – điều khiển tập trung** nhiều máy trên máy tính/mạng.

**HMI có bắt buộc phải có trong hệ PLC không?**
Không bắt buộc, nhưng **rất nên có** để người vận hành **theo dõi thông số, ra lệnh và xem cảnh báo** thuận tiện, thay vì chỉ dùng nút nhấn và đèn báo cứng trên tủ.

**Một HMI điều khiển được nhiều PLC không?**
Có, tùy dòng HMI: nhiều HMI hỗ trợ **nhiều cổng và giao thức** để kết nối, giám sát và điều khiển **nhiều PLC/thiết bị** cùng lúc.

**Màn hình HMI thường dùng nguồn gì?**
Phổ biến là **24VDC** — giống nguồn điều khiển của PLC, nên có thể **dùng chung bộ nguồn** trong tủ điện, thuận tiện khi thiết kế và đấu nối.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › HMI là gì) + Article.
     INTERNAL LINK RA: /scada-la-gi/, /plc-la-gi/, /loi-truyen-thong-plc-hmi-modbus/, /lien-he/. -->
