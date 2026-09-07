<!--
LOẠI TRANG : Blog kỹ thuật — Thông tin + thương mại
URL SLUG   : /tin-hieu-4-20ma-la-gi/
TỪ KHÓA    : 4-20ma | tín hiệu 4-20ma là gì | vòng dòng 4-20ma | 4-20ma 2 dây | chuyển 4-20ma sang 0-10v | tín hiệu analog công nghiệp
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. Nguyên lý chung; điện trở tải và điện áp nguồn tối thiểu tra datasheet từng thiết bị.
-->

TITLE TAG   : Tín Hiệu 4-20mA Là Gì? Vì Sao Công Nghiệp Dùng
META (149)  : Tín hiệu 4-20mA là gì, vì sao chuẩn công nghiệp chọn dòng thay vì áp, cách đấu 2 dây và 4 dây, tính điện trở tải và xử lý nhiễu. Kèm cách chuyển đổi tín hiệu.
H1          : Tín Hiệu 4-20mA Là Gì Và Vì Sao Được Dùng?

---

## Tín hiệu 4-20mA là gì?

<!--IMG:rep-->
![Tín hiệu 4-20mA trong hệ thống đo lường](assets/diagrams/rep-converter.svg)


**4-20mA** là chuẩn tín hiệu analog phổ biến nhất trong đo lường công nghiệp: thiết bị đo biểu diễn giá trị đo bằng **cường độ dòng điện** chạy trong vòng mạch, với **4mA ứng với giá trị đầu thang** và **20mA ứng với giá trị cuối thang**.

Ví dụ một cảm biến áp suất thang 0–10 bar dùng **4-20mA**: 0 bar → 4mA, 5 bar → 12mA, 10 bar → 20mA.

Điểm tinh tế nằm ở con số **4** chứ không phải 0. Vì đầu thang là 4mA chứ không phải 0mA, nên hệ thống **phân biệt được** giữa "giá trị đo bằng 0" và "đứt dây, mất nguồn". Dòng dưới 4mA luôn có nghĩa là **sự cố**, không phải giá trị đo hợp lệ. Đây gọi là đặc tính *live zero*.

> **Cần chuyển đổi hoặc cách ly tín hiệu 4-20mA?** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/signal-chain.svg)


---

## Vì sao công nghiệp chọn dòng thay vì điện áp?

| Tiêu chí | **4-20mA (dòng)** | 0-10V (điện áp) |
|---|---|---|
| Sụt áp trên dây dài | **Không ảnh hưởng giá trị** | Gây sai số trực tiếp |
| Khoảng cách truyền | **Hàng trăm mét** | Ngắn hơn nhiều |
| Chống nhiễu | **Tốt** | Kém hơn |
| Phát hiện đứt dây | **Có (dòng < 4mA)** | Không phân biệt được với 0V |
| Số dây tối thiểu | **2 dây** (vừa cấp nguồn vừa truyền tín hiệu) | Thường 3 dây |
| Chi phí thiết bị | Tương đương | Tương đương |

Dòng đầu bảng là lý do cốt lõi: trong một **vòng dòng**, cường độ dòng điện **như nhau tại mọi điểm** trên mạch. Dây dài bao nhiêu, điện trở dây bao nhiêu thì dòng vẫn giữ nguyên — điều mà tín hiệu điện áp không làm được.

---

## Đấu dây 4-20mA: 2 dây, 3 dây và 4 dây

| Kiểu đấu | Cách hoạt động | Dùng khi |
|---|---|---|
| **2 dây (loop powered)** | Cùng một cặp dây vừa cấp nguồn vừa mang tín hiệu | Phổ biến nhất, tiết kiệm dây |
| **3 dây** | Nguồn chung, tín hiệu riêng | Khi thiết bị cần dòng tiêu thụ lớn hơn |
| **4 dây** | Nguồn và tín hiệu tách hoàn toàn | Thiết bị có màn hình, xử lý nhiều |

Kiểu **2 dây** là lý do khiến chuẩn **4-20mA** trở nên phổ biến: một cặp dây làm hai việc. Đây cũng là lý do đầu thang phải là 4mA — thiết bị cần một dòng tối thiểu để tự nuôi mạch bên trong. Chi tiết đấu nối thực tế: [đấu dây cảm biến áp suất 4-20mA](/dau-day-cam-bien-ap-suat-4-20ma/).

---

## Điện trở tải và điện áp nguồn tối thiểu

| Khái niệm | Ý nghĩa | Hệ quả thực tế |
|---|---|---|
| **Điện trở tải** | Tổng trở của module analog + dây + thiết bị nối tiếp | Càng nhiều thiết bị nối tiếp, tải càng lớn |
| **Điện áp rơi trên tải** | Bằng dòng nhân điện trở tải | Ở 20mA, 250Ω tạo sụt 5V |
| **Điện áp nguồn tối thiểu** | Đủ nuôi cảm biến sau khi trừ sụt áp | Datasheet ghi rõ theo tải |
| **Tải tối đa cho phép** | Giới hạn của thiết bị phát | Vượt quá thì tín hiệu bị "cắt ngọn" |

Đây là nguyên nhân của một lỗi khó chịu: hệ chạy tốt ở giá trị thấp nhưng **không bao giờ lên tới 20mA**. Nguyên nhân gần như luôn là **điện trở tải quá lớn** so với điện áp nguồn — thêm một bộ hiển thị nối tiếp vào vòng cũng đủ gây ra.

⚠️ Con số điện trở tải tối đa và điện áp nguồn tối thiểu **khác nhau theo từng model** — phải tra datasheet, không suy đoán.

---

## Chuyển đổi và cách ly tín hiệu 4-20mA

| Nhu cầu | Thiết bị cần dùng | Vì sao |
|---|---|---|
| Một tín hiệu, nhiều nơi nhận | Bộ chia tín hiệu | Nối tiếp nhiều thiết bị làm tải quá lớn |
| Chống nhiễu, cắt vòng lặp đất | Bộ cách ly tín hiệu | Xử lý dứt điểm hiện tượng số nhảy loạn |
| Đổi sang 0-10V | Bộ chuyển đổi dòng sang áp | Khi thiết bị nhận chỉ hiểu điện áp |
| Đổi sang Modbus | Bộ chuyển đổi analog sang số | Giảm dây khi nhiều điểm đo |
| Nhận tín hiệu từ Pt100, can nhiệt | Bộ chuyển đổi nhiệt độ sang **4-20mA** | Xem [cảm biến nhiệt độ](/cam-bien-nhiet-do/) |

Dải thiết bị chuyển đổi và cách ly đang phân phối: [bộ chuyển đổi tín hiệu Seneca](/bo-chuyen-doi-tin-hieu-seneca/). Nhiều điểm đo phân tán thì cân nhắc [remote I/O](/remote-io-seneca-z-pc/) thay vì kéo từng cặp dây về tủ.

---

## Lỗi thường gặp với tín hiệu 4-20mA

| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Dòng dưới 4mA | Mất nguồn, đứt dây, đấu ngược cực | Kiểm tra nguồn và thông mạch |
| Không lên được 20mA | Điện trở tải quá lớn | Giảm số thiết bị nối tiếp, tăng điện áp nguồn |
| Số nhảy loạn | Nhiễu, vòng lặp tiếp đất | Cách ly tín hiệu, tách máng cáp |
| Đọc lệch so với đồng hồ cơ | Khai báo thang đo sai trong PLC | Đối chiếu thang đo thiết bị và cấu hình PLC |
| Nhiều kênh cùng sai | Nguồn chung kém chất lượng | Thay nguồn, cân nhắc nguồn riêng cho analog |
| Hỏng module analog | Đấu nhầm nguồn vào ngõ vào | Kiểm tra kỹ trước khi cấp điện |

Chẩn đoán chi tiết theo triệu chứng: [lỗi cảm biến áp suất](/loi-cam-bien-ap-suat/) và [lỗi ngõ vào ra PLC](/loi-ngo-vao-ra-plc/).

---

## Khi nào không nên dùng 4-20mA?

- **Nhiều điểm đo trên cùng tuyến** — mỗi tín hiệu **4-20mA** cần một cặp dây riêng; trên 20–30 điểm thì truyền thông số (Modbus) rẻ hơn về dây và công thi công.
- **Cần truyền thêm dữ liệu chẩn đoán** — dòng analog chỉ mang một giá trị, không mang được trạng thái thiết bị.
- **Khoảng cách rất xa hoặc qua nhiều khu vực** — cân nhắc gateway và mạng truyền thông.
- **Đo tần số cao, biến thiên nhanh** — cần đường tín hiệu chuyên dụng.

Với phần lớn nhà máy Việt Nam, **4-20mA** vẫn là lựa chọn mặc định đúng: đơn giản, bền, ai cũng biết xử lý khi sự cố.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá thiết bị tín hiệu 4-20mA

Gửi cho chúng tôi: **loại tín hiệu vào và ra cần có · số điểm · khoảng cách truyền · môi trường có nhiễu không · nguồn cấp sẵn có.**

Chúng tôi đề xuất bộ chuyển đổi, cách ly hoặc phương án remote I/O phù hợp, kèm báo giá và datasheet.

**→ [Liên hệ tư vấn thiết bị 4-20mA](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/signal-converter.svg)

## Câu hỏi thường gặp (FAQ)

**Vì sao đầu thang là 4mA mà không phải 0mA?**
Để phân biệt "giá trị đo bằng 0" với "đứt dây, mất nguồn", và để có dòng tối thiểu nuôi mạch bên trong thiết bị 2 dây. Dòng dưới 4mA luôn là dấu hiệu sự cố.

**Tín hiệu 4-20mA truyền được bao xa?**
Hàng trăm mét trong điều kiện thông thường. Giới hạn thực tế đến từ **điện trở tải** và điện áp nguồn, không phải từ khoảng cách thuần túy.

**Có chuyển 4-20mA sang 0-10V được không?**
Được, bằng bộ chuyển đổi dòng sang áp. Không nên dùng điện trở đơn thuần vì ảnh hưởng tới điện trở tải của cả vòng.

**Nối được mấy thiết bị trên một vòng 4-20mA?**
Phụ thuộc tổng điện trở tải và điện áp nguồn. Khi cần nhiều nơi nhận cùng một tín hiệu, dùng bộ chia tín hiệu thay vì nối tiếp thêm.

**4-20mA và Modbus nên chọn cái nào?**
Ít điểm đo, cần đơn giản và bền thì **4-20mA**. Nhiều điểm đo, cần thêm dữ liệu chẩn đoán và tiết kiệm dây thì Modbus có lợi hơn.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /dau-day-cam-bien-ap-suat-4-20ma/, /bo-chuyen-doi-tin-hieu-seneca/, /loi-cam-bien-ap-suat/, /cam-bien-ap-suat/, /lien-he/. -->
