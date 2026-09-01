<!--
LOẠI TRANG : Danh mục giải pháp (pillar) — Thương mại
URL SLUG   : /gateway-ket-noi-bao-mat-ei3/
TỪ KHÓA    : gateway ei3 | gateway kết nối máy | iiot gateway bảo mật | amphion zethus portara | gateway outbound-only
INTENT     : Thương mại + kỹ thuật
TRẠNG THÁI : Sẵn đăng. Đối chiếu tài liệu ei3.com; cấu hình theo nhu cầu.
-->

TITLE TAG   : Gateway Kết Nối Bảo Mật ei3 – Amphion, Zethus, Portara
META (155)  : Gateway kết nối bảo mật ei3: Amphion (phần cứng edge), Zethus (ảo/container), Portara (nâng cấp hệ cũ). Kết nối máy mới & legacy outbound-only, kiến trúc zero-trust, 30+ giao thức. Tư vấn dự án.
H1          : Gateway Kết Nối Bảo Mật ei3 (Amphion · Zethus · Portara)

---

## Gateway kết nối bảo mật ei3 là gì?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-gateway-ei3.svg)


Là bộ **gateway edge** giúp **kết nối máy mới và máy cũ (legacy)** lên nền tảng ei3 theo mô hình **outbound-only** — máy **chủ động kết nối ra ngoài**, **không mở cổng firewall vào** mạng nhà máy. Cả ba dùng chung một **kiến trúc zero-trust**: gom, đệm dữ liệu tại biên, phân tích cho bảo trì dự đoán, quản lý fleet tập trung, ghi phiên và tích hợp **SSO/SIEM**. Bộ ba ra mắt tại **Pack Expo Las Vegas 2025**.

> **Cần chọn gateway?** Gửi **máy mới hay cũ · có sẵn edge compute không · số giao thức/PLC** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-outbound.svg)


---

## Ba loại gateway — chọn loại nào?

| Gateway | Dạng | Chọn khi |
|---|---|---|
| **[Amphion](/amphion-gateway-ei3/)** | **Phần cứng** edge, DIN-rail, made in USA | Cần thiết bị chuyên dụng, kết nối cả máy legacy, cache tốc độ cao + phân tích biên |
| **[Zethus](/zethus-gateway-ei3/)** | **Ảo (container)** — chỉ phần mềm | Đã có bộ điều khiển/edge compute, không muốn thêm phần cứng |
| **[Portara](/portara-gateway-ei3/)** | **Nâng cấp** hạ tầng remote access cũ | Muốn bọc hệ remote access hiện có vào zero-trust, gom về một mạng quản lý |

---

## Điểm chung của cả ba

- **Outbound-only:** không mở cổng vào mạng nhà máy → giảm bề mặt tấn công.
- **30+ giao thức / họ điều khiển:** kết nối máy mới lẫn cũ.
- **Zero-trust:** ghi phiên, giám sát, tích hợp **SSO/directory & SIEM**.
- **Quản lý fleet tập trung:** vận hành nhiều máy/nhà máy từ một nơi.

---

## Ứng dụng

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-fleet.svg)


- **OEM** kết nối máy đã bán cho khách để làm **remote service**.
- **Nhà máy** gom dữ liệu máy phân tán về nền tảng để [giám sát & phân tích](/ung-dung-iiot-ei3/).
- Bổ sung cho [gateway Modbus/IIoT Seneca](/gateway-modbus-seneca/) khi cần lớp bảo mật kết nối từ xa.

---

## Cam kết

- ✅ Phân phối ei3 (Mỹ), tư vấn kiến trúc & triển khai theo dự án.
- ✅ Chọn đúng gateway theo hiện trạng máy/PLC và mục tiêu.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá gateway ei3

Gửi: **máy mới/cũ · có edge compute sẵn không · giao thức/PLC · số máy · mục tiêu.**

**→ [Liên hệ tư vấn gateway ei3](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Gateway ei3 có mở cổng firewall vào nhà máy không?**
Không — mô hình **outbound-only**: máy chủ động kết nối ra, không cần mở cổng vào.

**Amphion, Zethus, Portara khác nhau thế nào?**
[Amphion](/amphion-gateway-ei3/) là **phần cứng**; [Zethus](/zethus-gateway-ei3/) là **ảo/container**; [Portara](/portara-gateway-ei3/) **nâng cấp** hạ tầng remote access cũ.

**Có kết nối được máy đời cũ (legacy) không?**
Được — gateway hỗ trợ **30+ giao thức/họ điều khiển**, kết nối cả máy mới lẫn cũ.

<!-- SCHEMA: FAQPage + BreadcrumbList (Trang chủ › ei3 › Gateway).
     INTERNAL LINK: /ei3/, /amphion-gateway-ei3/, /zethus-gateway-ei3/, /portara-gateway-ei3/, /lien-he/. -->
