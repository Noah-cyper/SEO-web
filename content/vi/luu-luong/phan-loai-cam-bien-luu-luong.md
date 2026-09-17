<!--
LOẠI TRANG : Bài kiến thức nền — chuỗi cảm biến lưu lượng — tầng 1
URL SLUG   : /phan-loai-cam-bien-luu-luong/
TỪ KHÓA    : phân loại cảm biến lưu lượng | các loại lưu lượng kế | flow meter types | đồng hồ nước cơ | công tắc lưu lượng
INTENT     : Thông tin
TRẠNG THÁI : Sẵn đăng. Bài 3/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Phân Loại Cảm Biến Lưu Lượng – Bảng Tra Đầy Đủ Theo 4 Cách
META (156)  : Phân loại lưu lượng kế theo nguyên lý, theo môi chất, theo kiểu lắp và theo chức năng. Bảng tra nhanh giúp khoanh vùng loại phù hợp trước khi đi vào chi tiết.

H1          : Phân Loại Cảm Biến Lưu Lượng

---

## Cùng một thiết bị, bốn cách gọi tên khác nhau

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-cam-bien-luu-luong.svg)


Khi đi mua cảm biến lưu lượng, bạn sẽ gặp một mớ tên gọi chồng chéo: "đồng hồ nước điện từ", "lưu lượng kế dạng wafer", "flow switch", "mass flow meter", "clamp-on ultrasonic". Chúng nghe như bảy loại khác nhau, nhưng thực ra là **cùng một nhóm thiết bị được gọi theo bốn tiêu chí khác nhau**:

1. Theo **nguyên lý đo** — điện từ, siêu âm, Coriolis, tuabin, vortex, chênh áp, nhiệt.
2. Theo **môi chất** — cho chất lỏng, cho khí, cho hơi.
3. Theo **kiểu lắp đặt** — lắp trong ống, kẹp ngoài, cắm vào (insertion).
4. Theo **chức năng đầu ra** — đo liên tục, đếm tổng, hay chỉ báo có/không dòng chảy.

Hiểu bốn trục phân loại này giúp bạn **khoanh vùng nhanh** trước khi đi vào từng công nghệ cụ thể, và tránh mua nhầm một thiết bị đúng nguyên lý nhưng sai kiểu lắp hoặc sai chức năng.

Bài này đưa ra bảng tra theo cả bốn trục.

> **Cần khoanh vùng loại phù hợp cho ứng dụng của bạn?** Gửi **môi chất · ống · mục đích đo** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-flow-profile.svg)


Đây là bài **3/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: phân loại theo cách đo

Đây là trục phân loại quan trọng nhất, vì nó quyết định thiết bị **làm được gì và không làm được gì** ([xem chi tiết nguyên lý](/nguyen-ly-do-luu-luong/)).

| Nhóm | Công nghệ | Đo được | Không đo được |
|---|---|---|---|
| **Điện từ** | Đồng hồ điện từ (MAG) | Chất lỏng **dẫn điện**: nước, nước thải, hóa chất, bùn | Dầu, xăng, nước siêu tinh khiết, khí, hơi |
| **Siêu âm** | Transit-time, Doppler | Chất lỏng tương đối sạch; một số loại khí | Chất lỏng nhiều bọt khí nặng |
| **Cơ khí quay** | Tuabin, bánh răng oval, cánh gạt | Chất lỏng sạch, khí sạch | Môi chất có cặn, sợi, hạt rắn |
| **Xoáy** | Vortex | Lỏng, khí, **hơi** | Lưu lượng rất thấp, môi chất nhớt |
| **Chênh áp** | Orifice, venturi, pitot, nozzle | Gần như mọi môi chất | Lưu lượng biến động rất rộng |
| **Khối lượng** | Coriolis | Lỏng, khí, hơi — **khối lượng thật** | Ống rất lớn (chi phí quá cao) |
| **Nhiệt** | Thermal mass | **Khí** — kể cả lưu lượng rất thấp | Chất lỏng (một số loại có, nhưng hạn chế) |
| **Diện tích thay đổi** | Rotameter (ống thủy tinh có phao) | Lỏng, khí — chỉ báo tại chỗ | Không có tín hiệu ra (trừ loại có bộ phát) |

### Hai loại ít được nhắc nhưng rất phổ biến

**Rotameter (lưu lượng kế phao).** Một ống côn trong suốt có phao bên trong; dòng chảy đẩy phao lên cao, vị trí phao chỉ lưu lượng. Đơn giản, rẻ, không cần nguồn điện, đọc trực tiếp bằng mắt.

Hạn chế: **phải lắp thẳng đứng**, độ chính xác vừa phải, và loại cơ bản **không có tín hiệu điện ra**. Vẫn rất hữu dụng cho các điểm cần quan sát tại chỗ — làm mát máy, nước rửa, khí mẫu.

**Đồng hồ nước cơ kiểu cánh quạt.** Loại phổ biến nhất trong dân dụng và nhiều hệ công nghiệp nhẹ. Rẻ, bền, không cần nguồn, có bộ đếm tổng cơ khí. Nhiều loại có thêm **bộ phát xung** để đưa tín hiệu về PLC.

Hạn chế: có bộ phận quay nên **sợ cặn bẩn**, mất chính xác dần theo thời gian, và **tổn thất áp suất đáng kể**.

---

## Cấu tạo: phân loại theo kiểu lắp đặt

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-chon.svg)


Trục phân loại này quyết định **công lắp đặt và khả năng bảo trì** — thường ảnh hưởng tới tổng chi phí nhiều hơn giá thiết bị.

### Lắp trong đường ống (inline / in-line)

Thiết bị trở thành **một đoạn của đường ống**. Toàn bộ môi chất đi qua nó.

- **Ưu:** chính xác nhất, ổn định nhất.
- **Nhược:** phải **cắt ống và dừng sản xuất** để lắp; cỡ lớn thì thiết bị nặng và đắt.
- **Kiểu kết nối:** mặt bích (flange), ren (threaded), wafer (kẹp giữa hai mặt bích), clamp vệ sinh (tri-clamp cho thực phẩm).

**Về kiểu wafer:** thiết bị mỏng, kẹp giữa hai mặt bích có sẵn bằng bu lông dài. Nhẹ hơn và rẻ hơn loại mặt bích đầy đủ, nhưng cần căn tâm cẩn thận khi lắp.

### Kẹp ngoài ống (clamp-on)

Chỉ có ở công nghệ **siêu âm**. Đầu dò kẹp bên ngoài thành ống, sóng âm xuyên qua thành ống vào môi chất.

- **Ưu:** **không cắt ống, không dừng sản xuất**, tháo ra dùng cho ống khác được, không tiếp xúc môi chất nên không bị ăn mòn.
- **Nhược:** độ chính xác thấp hơn, phụ thuộc **vật liệu và tình trạng thành ống**, cần biết chính xác đường kính và độ dày ống để cấu hình.

Đây là lựa chọn rất giá trị cho **khảo sát, kiểm tra chéo và đo tạm thời** ([xem chi tiết](/cam-bien-luu-luong-sieu-am/)).

### Cắm vào ống (insertion)

Một thanh dò được cắm xuyên qua thành ống vào giữa dòng chảy. Có ở công nghệ điện từ, vortex, nhiệt, pitot.

- **Ưu:** **chi phí gần như không tăng theo cỡ ống** — đây là ưu thế quyết định với ống lớn. Chỉ cần khoan một lỗ và hàn một cổ nối.
- **Nhược:** đo vận tốc **tại một điểm** rồi suy ra trung bình, nên **nhạy với biên dạng dòng chảy** hơn nhiều. Vị trí cắm và độ sâu cắm phải đúng.

**Khi nào insertion là lựa chọn đúng:** ống rất lớn (nơi thiết bị inline có giá rất cao), yêu cầu chính xác vừa phải, và có đủ đoạn ống thẳng.

---

## Ứng dụng: phân loại theo chức năng đầu ra

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-nuoc.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-congnghe.svg)

Đây là trục hay bị bỏ qua nhất khi đặt hàng, và cũng là nguồn của nhiều lần mua nhầm.

### Đo liên tục (flow transmitter)

Cho giá trị lưu lượng **tức thời**, xuất tín hiệu 4–20mA, Modbus hoặc HART. Dùng cho giám sát và điều khiển.

### Đếm tổng (totalizer / flow counter)

Cộng dồn **tổng lượng đã đi qua** — bao nhiêu m³ từ đầu tháng. Dùng cho tính chi phí, phân bổ và kiểm toán.

Hầu hết thiết bị hiện đại làm **cả hai**: vừa hiển thị lưu lượng tức thời vừa có bộ đếm tổng. Nhưng cần kiểm tra khi mua, đặc biệt với các loại cơ bản.

Lưu ý quan trọng: nếu cần tổng chính xác, nên dùng **đầu ra xung** thay vì tích phân tín hiệu 4–20mA — mỗi xung tương ứng một đơn vị thể tích cố định, không tích lũy sai số ([xem bài đấu dây](/dau-day-cam-bien-luu-luong/)).

### Công tắc lưu lượng (flow switch)

**Không đo giá trị** — chỉ báo **có dòng chảy hay không**, hoặc lưu lượng có vượt ngưỡng hay không. Đầu ra là một tiếp điểm đóng/mở.

Đây là thiết bị rất khác về bản chất, nhưng hay bị gọi chung là "cảm biến lưu lượng". Ứng dụng điển hình:

- **Bảo vệ bơm chạy khô** — không có dòng thì dừng bơm.
- **Bảo vệ hệ làm mát** — mất nước làm mát thì báo động và dừng máy.
- **Xác nhận quạt gió đang chạy** trong hệ thông gió.
- **Khóa liên động an toàn** — chỉ cho máy chạy khi có dòng làm mát.

Ưu điểm: **rẻ hơn rất nhiều** so với thiết bị đo. Nếu bạn chỉ cần biết "có nước hay không", đừng mua một đồng hồ đo đắt tiền.

Nhược điểm: không cho biết giá trị, không tích hợp vào hệ giám sát năng lượng.

### Kết hợp đo nhiều đại lượng

Một số thiết bị cho ra nhiều hơn lưu lượng:

- **Coriolis** — lưu lượng khối, khối lượng riêng, nhiệt độ, và từ đó suy ra nồng độ dung dịch.
- **Vortex đa biến (multivariable)** — lưu lượng, áp suất, nhiệt độ trong một thiết bị, tự bù để ra khối lượng.
- **Đồng hồ nhiệt lượng (energy meter)** — lưu lượng cộng hai nhiệt độ vào/ra, tính ra **năng lượng nhiệt hoặc lạnh tiêu thụ**. Rất hữu dụng cho hệ HVAC ([xem bài HVAC](/bien-tan-trong-hvac/)).

---

## So sánh: bảng tra nhanh theo môi chất

Đây là cách khoanh vùng thực dụng nhất khi mới bắt đầu:

| Môi chất | Lựa chọn hàng đầu | Lựa chọn thay thế | Tránh dùng |
|---|---|---|---|
| **Nước sạch** | Điện từ | Siêu âm, tuabin | — |
| **Nước thải, bùn** | **Điện từ** | Siêu âm Doppler | Tuabin, orifice |
| **Nước siêu tinh khiết (DI)** | Coriolis, siêu âm | — | **Điện từ** (không dẫn điện) |
| **Dầu, nhiên liệu** | Coriolis, bánh răng oval | Tuabin | **Điện từ** |
| **Hóa chất ăn mòn** | Điện từ (lót PTFE), Coriolis | — | Loại có bộ phận quay |
| **Khí nén** | **Nhiệt (thermal)** | Vortex, orifice | Điện từ |
| **Hơi nước** | **Vortex** + bù P, T | Orifice + bù | Điện từ, tuabin |
| **Khí công nghiệp (N₂, O₂, CO₂)** | Nhiệt, Coriolis | Vortex | Điện từ |
| **Chất lỏng nhớt** | Coriolis, bánh răng oval | — | Tuabin, vortex |
| **Thực phẩm, đồ uống** | Điện từ (chuẩn vệ sinh), Coriolis | — | Loại khó vệ sinh |
| **Nước làm mát (chỉ cần báo có/không)** | **Công tắc lưu lượng** | — | Thiết bị đo đắt tiền |

### Ba câu hỏi quyết định nhanh

Nếu chỉ có thời gian cho ba câu hỏi, hãy hỏi:

**1. Môi chất có dẫn điện không?**
Có → **điện từ** là ứng viên số một. Không → loại điện từ ra khỏi danh sách ngay.

**2. Cần đo giá trị hay chỉ cần biết có dòng?**
Chỉ cần biết có/không → **công tắc lưu lượng**, rẻ hơn nhiều lần.

**3. Có được dừng sản xuất để cắt ống không?**
Không → **siêu âm kẹp ngoài** là lựa chọn gần như duy nhất.

Ba câu này loại bỏ được phần lớn phương án không phù hợp trong vài phút. Các tiêu chí còn lại — dải đo, chính xác, ngân sách — đi vào chi tiết ở bài [cách chọn cảm biến lưu lượng](/cach-chon-cam-bien-luu-luong/).

---

## Sai lầm thường gặp

1. **Mua thiết bị đo trong khi chỉ cần công tắc lưu lượng** — tốn gấp nhiều lần.
2. **Ngược lại: mua công tắc rồi mới phát hiện cần giá trị** để tính chi phí.
3. **Chọn đồng hồ điện từ cho dầu hoặc nước siêu tinh khiết** — không hoạt động.
4. **Chọn tuabin cho nước thải có cặn** — kẹt cánh, hỏng nhanh.
5. **Mua loại inline rồi mới biết không được dừng sản xuất để lắp.**
6. **Chọn loại insertion cho ống nhỏ** — không tiết kiệm mà lại kém chính xác hơn.
7. **Mua rotameter rồi cần tín hiệu về PLC** — loại cơ bản không có đầu ra.
8. **Quên kiểm tra thiết bị có bộ đếm tổng không** khi cần tính chi phí.
9. **Lắp rotameter nằm ngang** — nó bắt buộc phải thẳng đứng.
10. **Dùng tín hiệu 4–20mA để tính tổng** thay vì đầu ra xung — sai số tích lũy.
11. **Mua loại wafer mà không tính tới việc căn tâm** khi lắp giữa hai mặt bích.

---

## Cam kết tại HOANTRANTDH

- ✅ **Hỏi rõ mục đích đo trước** — nếu bạn chỉ cần biết có dòng hay không, chúng tôi đề xuất công tắc lưu lượng.
- ✅ Tư vấn **kiểu lắp phù hợp với điều kiện thi công thực tế**, không chỉ theo công nghệ.
- ✅ Kiểm tra **khả năng dẫn điện của môi chất** trước khi đề xuất đồng hồ điện từ.
- ✅ Cung cấp đủ các nhóm: đồng hồ điện từ, siêu âm, vortex, tuabin, công tắc lưu lượng và rotameter.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **môi chất và tính chất · đường kính và vật liệu ống · dải lưu lượng · mục đích (giám sát, điều khiển, tính tổng, báo động) · có được cắt ống không · yêu cầu tín hiệu ra · môi trường lắp đặt.**

**→ [Liên hệ nhận tư vấn phân loại](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến lưu lượng có mấy loại?**
Có thể phân loại theo bốn trục: **nguyên lý đo** (điện từ, siêu âm, Coriolis, tuabin, vortex, chênh áp, nhiệt), **môi chất**, **kiểu lắp** (inline, kẹp ngoài, insertion) và **chức năng** (đo, đếm tổng, công tắc).

**Công tắc lưu lượng khác cảm biến lưu lượng thế nào?**
**Công tắc chỉ báo có dòng chảy hay không**, đầu ra là tiếp điểm đóng/mở, giá rẻ hơn nhiều lần. **Cảm biến đo** cho giá trị cụ thể và tín hiệu 4–20mA hoặc số.

**Khi nào nên dùng loại kẹp ngoài (clamp-on)?**
Khi **không được cắt ống hoặc không được dừng sản xuất**, hoặc khi cần một thiết bị **di động để khảo sát nhiều điểm**. Đổi lại độ chính xác thấp hơn loại lắp trong ống.

**Loại insertion (cắm vào ống) phù hợp khi nào?**
Khi **ống rất lớn** — chi phí gần như không tăng theo cỡ ống. Đổi lại nó đo vận tốc tại một điểm nên nhạy với biên dạng dòng chảy hơn.

**Rotameter có xuất tín hiệu điện được không?**
Loại cơ bản **không có** — chỉ đọc bằng mắt tại chỗ. Có loại kèm bộ phát tín hiệu, nhưng cần xác nhận khi đặt hàng.

**Đo nước thải nên chọn loại nào?**
**Đồng hồ điện từ**, vì nó không có vật cản trong dòng nên không bị kẹt bởi cặn, sợi và rác. Tuyệt đối tránh tuabin và orifice.

**Đồng hồ nước cơ có dùng cho công nghiệp được không?**
Được với **nước sạch và yêu cầu vừa phải**. Ưu điểm là rẻ, bền, không cần nguồn. Nhược điểm là có bộ phận quay nên sợ cặn, và tổn thất áp suất đáng kể.

**Thiết bị nào đo được nhiều đại lượng cùng lúc?**
**Coriolis** (khối lượng, khối lượng riêng, nhiệt độ), **vortex đa biến** (lưu lượng, áp suất, nhiệt độ) và **đồng hồ nhiệt lượng** (lưu lượng + hai nhiệt độ ⇒ năng lượng nhiệt).

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /cam-bien-luu-luong-sieu-am/, /cach-chon-cam-bien-luu-luong/, /dau-day-cam-bien-luu-luong/, /bien-tan-trong-hvac/, /lien-he/. -->
