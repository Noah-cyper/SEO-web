<!--
LOẠI TRANG : Bài kiến thức nền — chuỗi cảm biến lưu lượng — tầng 1
URL SLUG   : /don-vi-luu-luong-quy-doi/
TỪ KHÓA    : đơn vị lưu lượng | quy đổi m3/h sang l/min | nm3/h là gì | lưu lượng khối và thể tích | scfm
INTENT     : Thông tin
TRẠNG THÁI : Sẵn đăng. Bài 4/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Đơn Vị Lưu Lượng Và Cách Quy Đổi – m³/h, l/min, kg/h, Nm³/h
META (156)  : Bảng quy đổi đơn vị lưu lượng và giải thích Nm³/h khác m³/h thế nào. Vì sao nhầm điều kiện quy chiếu khi đo khí là sai số lớn nhất và tốn kém nhất.

H1          : Đơn Vị Lưu Lượng Và Cách Quy Đổi

---

## Sai số tốn kém nhất không nằm ở thiết bị

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-cam-bien-luu-luong.svg)


Trong đo lưu lượng, có một loại sai số lớn hơn mọi sai số thiết bị cộng lại, và nó **không tốn một đồng nào để sửa**: nhầm lẫn đơn vị và điều kiện quy chiếu.

Hai tình huống điển hình:

**Tình huống 1.** Nhà máy mua một máy nén khí ghi lưu lượng "10 m³/min". Lắp đồng hồ đo, đọc được con số nhỏ hơn hẳn. Tranh cãi với nhà cung cấp kéo dài nhiều tuần. Nguyên nhân: máy nén ghi theo **thể tích khí hút vào ở điều kiện môi trường**, đồng hồ đo báo theo **thể tích thực ở áp suất đường ống** — hai con số hoàn toàn khác nhau cho cùng một lượng khí.

**Tình huống 2.** Hợp đồng ghi lưu lượng "2000 Nm³/h". Bên thi công lắp thiết bị cấu hình ra "m³/h". Số hiển thị chênh nhiều lần so với hợp đồng, và không ai biết ai đúng.

Cả hai đều không phải lỗi thiết bị. Chúng là lỗi **đơn vị**, và chúng xảy ra thường xuyên hơn mọi lỗi kỹ thuật khác trong đo lưu lượng khí.

Bài này giải thích hệ thống đơn vị, cách quy đổi, và đặc biệt là **điều kiện quy chiếu** — khái niệm gây nhầm lẫn nhiều nhất.

> **Cần đối chiếu đơn vị trong hồ sơ dự án?** Gửi **thông số đang có · môi chất** → [Nhận hỗ trợ quy đổi](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-thermal-mass.svg)


Đây là bài **4/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: hai họ đơn vị khác nhau về bản chất

### Họ thể tích

Đo **bao nhiêu không gian** chất chiếm chỗ trong một đơn vị thời gian.

| Đơn vị | Đọc là | Thường dùng cho |
|---|---|---|
| **m³/h** | mét khối trên giờ | Nước, nước thải — phổ biến nhất |
| **m³/s** | mét khối trên giây | Tính toán kỹ thuật, ống lớn |
| **l/min** (lpm) | lít trên phút | Máy móc, dây chuyền, bơm nhỏ |
| **l/h** | lít trên giờ | Định lượng hóa chất |
| **l/s** | lít trên giây | Cấp nước, PCCC |
| **GPM** | gallon trên phút | Thiết bị theo chuẩn Mỹ |
| **CFM** | foot khối trên phút | Khí nén theo chuẩn Mỹ |

**Quy đổi trong họ thể tích rất đơn giản**, vì chúng chỉ khác nhau về hệ số:

- 1 m³ = 1000 lít
- 1 m³/h = 1000 l/h ≈ 16,67 l/min ≈ 0,278 l/s
- 1 l/min = 0,06 m³/h
- 1 l/s = 3,6 m³/h

Với nước, các quy đổi này luôn đúng và không có bẫy nào.

### Họ khối lượng

Đo **bao nhiêu kilôgam** chất đi qua trong một đơn vị thời gian.

| Đơn vị | Đọc là | Thường dùng cho |
|---|---|---|
| **kg/h** | kilôgam trên giờ | Hơi nước, hóa chất |
| **kg/min**, **kg/s** | | Định lượng nhanh |
| **t/h** | tấn trên giờ | Lò hơi công suất lớn, nguyên liệu |

Quy đổi trong họ khối lượng cũng đơn giản: 1 t/h = 1000 kg/h.

### Cầu nối giữa hai họ: khối lượng riêng

Muốn chuyển từ thể tích sang khối lượng, nhân với **khối lượng riêng (ρ)**:

> **Lưu lượng khối = Lưu lượng thể tích × Khối lượng riêng**

Đây là chỗ mọi rắc rối bắt đầu.

**Với nước**, khối lượng riêng gần như không đổi trong dải nhiệt độ thông thường — khoảng 1000 kg/m³. Vậy nên với nước, 1 m³/h ≈ 1000 kg/h, và người ta gần như có thể dùng lẫn hai đơn vị.

**Với khí**, khối lượng riêng **thay đổi rất mạnh theo áp suất và nhiệt độ**. Cùng một mét khối khí ở áp suất cao chứa nhiều khối lượng hơn nhiều so với ở áp suất khí quyển. Với **hơi nước** cũng vậy.

Đây là lý do với khí và hơi, nói "10 m³/h" mà không nói ở điều kiện nào thì **câu nói đó không có nghĩa**.

---

## Cấu tạo vấn đề: điều kiện quy chiếu với khí

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-donvi.svg)


Để thoát khỏi sự mơ hồ trên, ngành công nghiệp dùng khái niệm **thể tích quy chuẩn**: quy đổi thể tích khí về **một điều kiện áp suất và nhiệt độ tham chiếu đã thỏa thuận**.

Có hai họ ký hiệu:

**Nm³/h — normal cubic meter per hour.** Thể tích quy về **điều kiện "normal"**, thường dùng ở châu Âu và phổ biến tại Việt Nam.

**Sm³/h hoặc SCFM — standard.** Thể tích quy về **điều kiện "standard"**, thường dùng theo chuẩn Mỹ.

**Điểm quan trọng phải nắm:** "normal" và "standard" **không phải cùng một điều kiện**, và ngay trong mỗi họ cũng **có nhiều định nghĩa khác nhau** tùy tiêu chuẩn và tùy ngành. Nhiệt độ tham chiếu có thể là 0°C, 15°C, 20°C hoặc 21°C tùy nơi.

Vì vậy, quy tắc thực hành quan trọng nhất của bài này:

> **Luôn ghi rõ điều kiện quy chiếu bên cạnh con số.** Không viết "2000 Nm³/h" mà viết "2000 Nm³/h ở điều kiện tham chiếu ... theo tiêu chuẩn ...". Nếu tài liệu bạn nhận được không ghi rõ, **hãy hỏi** trước khi cấu hình thiết bị.

### Ba loại thể tích khí — phân biệt cho rõ

Với khí, có **ba con số khác nhau** mà người ta đều gọi là "thể tích":

**1. Thể tích thực tế (actual, ký hiệu am³/h hoặc ACFM).** Thể tích khí **tại chính điều kiện áp suất và nhiệt độ trong ống**. Đây là cái mà một đồng hồ đo thể tích thuần túy đọc được.

**2. Thể tích quy chuẩn (Nm³/h, Sm³/h, SCFM).** Quy về điều kiện tham chiếu. Đây là con số dùng trong hợp đồng, trong tính toán cân bằng vật chất, và trong so sánh giữa các điểm đo.

**3. Thể tích khí hút vào (FAD — Free Air Delivery).** Đặc thù của **máy nén khí**: lượng khí ở điều kiện môi trường mà máy hút vào được. Đây là cách các nhà sản xuất máy nén công bố công suất.

Ba con số này khác nhau đáng kể. So sánh nhầm giữa chúng chính là nguồn gốc của tình huống số 1 ở đầu bài ([xem bài khí nén](/do-luu-luong-khi-nen/)).

### Vì sao cảm biến đo khối lượng tránh được rắc rối này

Đây là lý do kỹ thuật khiến **Coriolis và cảm biến nhiệt** được ưa chuộng cho khí và hơi: chúng đo thẳng ra **khối lượng**, mà khối lượng **không phụ thuộc áp suất hay nhiệt độ**.

Một kilôgam khí vẫn là một kilôgam khí, dù nó đang ở áp suất nào. Không cần điều kiện quy chiếu, không cần bù, không có chỗ để nhầm.

Nhiều thiết bị đo khối lượng vẫn hiển thị Nm³/h cho tiện — nhưng đó là **kết quả tính toán từ khối lượng**, chính xác hơn nhiều so với việc đo thể tích rồi bù ngược lại ([xem nguyên lý](/nguyen-ly-do-luu-luong/)).

---

## Ứng dụng: bảng quy đổi và cách dùng

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-hoi.svg)


### Quy đổi thể tích (luôn đúng, không phụ thuộc môi chất)

| Từ | Sang m³/h | Sang l/min |
|---|---|---|
| **1 m³/h** | 1 | 16,67 |
| **1 l/min** | 0,06 | 1 |
| **1 l/s** | 3,6 | 60 |
| **1 m³/min** | 60 | 1000 |
| **1 GPM (US)** | ≈ 0,227 | ≈ 3,785 |
| **1 CFM** | ≈ 1,699 | ≈ 28,3 |

### Quy đổi thể tích ↔ khối lượng (phụ thuộc môi chất)

Công thức: **kg/h = m³/h × ρ (kg/m³)**

- **Nước ở nhiệt độ thường:** ρ ≈ 1000 kg/m³ → 1 m³/h ≈ 1000 kg/h.
- **Dầu:** ρ thấp hơn nước, tùy loại — **phải tra theo loại dầu cụ thể**.
- **Khí và hơi:** ρ **thay đổi theo áp suất và nhiệt độ** — không có hệ số cố định, phải tính theo điều kiện thực tế hoặc dùng bảng tra của môi chất đó.

**Khuyến nghị thực hành:** với khí và hơi, đừng tự quy đổi bằng một hệ số nhớ được. Hãy dùng bảng tra chính thức của môi chất, hoặc tốt hơn — **dùng thiết bị đo trực tiếp khối lượng** để loại bỏ hoàn toàn bước quy đổi.

### Vận tốc dòng — đại lượng trung gian hữu ích

Nhiều tính toán chọn thiết bị đi qua **vận tốc dòng (m/s)**:

> **Lưu lượng thể tích = Vận tốc × Diện tích tiết diện ống**

Diện tích tiết diện tính từ đường kính trong của ống. Lưu ý: dùng **đường kính trong**, không phải đường kính danh nghĩa — với ống thành dày, hai con số này khác nhau đáng kể.

**Vì sao vận tốc quan trọng khi chọn cỡ thiết bị:**

- **Vận tốc quá thấp** → cảm biến làm việc ở đáy dải đo, sai số tương đối lớn; với nước thải còn gây lắng cặn.
- **Vận tốc quá cao** → tổn thất áp suất lớn, mài mòn nhanh, ồn.

Mỗi công nghệ và mỗi môi chất có một **khoảng vận tốc khuyến nghị** riêng, ghi trong tài liệu nhà sản xuất. Đây là căn cứ để chọn cỡ cảm biến thay vì chọn bằng cỡ ống ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

### Đơn vị của lượng tích lũy

Ngoài lưu lượng tức thời, thiết bị còn cộng dồn **tổng lượng đã đi qua**:

- Thể tích tích lũy: **m³**, **lít**
- Khối lượng tích lũy: **kg**, **tấn**
- Với khí quy chuẩn: **Nm³**

Khi cấu hình bộ đếm tổng, cần chú ý **đơn vị của mỗi xung** nếu dùng đầu ra xung — ví dụ một xung bằng 1 lít hay 10 lít. Cấu hình sai chỗ này làm tổng sai theo bội số, và lỗi thường chỉ bị phát hiện sau cả tháng ([xem bài đấu dây](/dau-day-cam-bien-luu-luong/)).

---

## So sánh: khi nào dùng đơn vị nào

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-tichkhoi.svg)


| Tình huống | Nên dùng | Lý do |
|---|---|---|
| **Nước, nước thải** | m³/h | Quy ước ngành, khối lượng riêng ổn định |
| **Máy móc, dây chuyền nhỏ** | l/min | Con số dễ đọc ở dải nhỏ |
| **Hơi nước** | **kg/h** | Tránh hoàn toàn vấn đề bù áp/nhiệt |
| **Khí nén, khí công nghiệp** | **Nm³/h** (ghi rõ điều kiện) | Chuẩn ngành, so sánh được giữa các điểm |
| **Hóa chất, định lượng mẻ** | kg/h hoặc kg | Cân bằng vật chất theo khối lượng |
| **Mua bán, giao nhận** | Khối lượng hoặc thể tích quy chuẩn | Không mơ hồ về điều kiện |
| **Tính toán chọn thiết bị** | m/s (vận tốc) | Căn cứ chọn cỡ cảm biến |
| **Năng lượng nhiệt/lạnh** | kW, kWh | Đồng hồ nhiệt lượng tính sẵn |

### Quy tắc viết đơn vị trong hồ sơ

Để tránh tranh cãi về sau, hãy viết đủ ba thành phần:

1. **Con số**
2. **Đơn vị**
3. **Điều kiện quy chiếu** (bắt buộc với khí và hơi)

Ví dụ đúng: *"Lưu lượng thiết kế 2000 Nm³/h, quy về điều kiện tham chiếu theo tiêu chuẩn X, khí nén khô"*.

Ví dụ thiếu: *"Lưu lượng 2000 m³/h"* — với khí, câu này chưa đủ để ai đó cấu hình thiết bị cho đúng.

---

## Sai lầm thường gặp

1. **Viết m³/h cho khí mà không ghi điều kiện quy chiếu** — con số trở nên mơ hồ.
2. **So sánh FAD của máy nén với số đọc của đồng hồ trong đường ống** — hai đại lượng khác nhau.
3. **Nhầm Nm³/h với m³/h thực tế** — sai số theo bội số, không phải phần trăm.
4. **Giả định "normal" và "standard" là một** — chúng khác nhau.
5. **Dùng một hệ số cố định để quy đổi khí từ thể tích sang khối lượng** — ρ thay đổi theo P và T.
6. **Dùng đường kính danh nghĩa thay vì đường kính trong** khi tính vận tốc.
7. **Cấu hình sai đơn vị mỗi xung** của đầu ra — tổng sai theo bội số.
8. **Chọn cỡ cảm biến bằng cỡ ống** thay vì theo vận tốc khuyến nghị.
9. **Nhầm GPM (Mỹ) với gallon Anh** khi đọc tài liệu nước ngoài.
10. **Không thống nhất đơn vị giữa thiết kế, thiết bị và hệ SCADA** — mỗi nơi một kiểu.
11. **Đổi đơn vị hiển thị trên thiết bị mà quên đổi trong PLC** — số liệu lệch nhau.

---

## Cam kết tại HOANTRANTDH

- ✅ **Xác nhận rõ điều kiện quy chiếu** trước khi cấu hình thiết bị đo khí cho khách.
- ✅ Hỗ trợ **đối chiếu đơn vị giữa hồ sơ thiết kế, thiết bị và hệ điều khiển**.
- ✅ Tư vấn chọn **thiết bị đo khối lượng trực tiếp** khi ứng dụng dễ nhầm lẫn về quy đổi.
- ✅ **Cấu hình sẵn đơn vị và bộ đếm tổng** theo yêu cầu trước khi giao hàng.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ quy đổi & báo giá

Gửi cho chúng tôi: **con số và đơn vị đang có trong hồ sơ · môi chất · áp suất và nhiệt độ làm việc · đơn vị mà hệ điều khiển đang dùng · mục đích (thiết kế, nghiệm thu, mua bán).**

**→ [Liên hệ nhận hỗ trợ](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Nm³/h khác m³/h thế nào?**
**m³/h** là thể tích **ở điều kiện thực tế trong ống**. **Nm³/h** là thể tích đã **quy về một điều kiện áp suất và nhiệt độ tham chiếu**. Với khí, hai con số này khác nhau rất nhiều.

**1 m³/h bằng bao nhiêu l/min?**
**≈ 16,67 l/min**. Ngược lại, 1 l/min = 0,06 m³/h. Quy đổi này luôn đúng vì cùng họ thể tích.

**Quy đổi m³/h sang kg/h thế nào?**
Nhân với **khối lượng riêng**: kg/h = m³/h × ρ. Với nước ρ ≈ 1000 kg/m³ nên 1 m³/h ≈ 1000 kg/h. Với khí và hơi, **ρ thay đổi theo áp suất và nhiệt độ** nên không có hệ số cố định.

**"Normal" và "standard" có phải cùng một điều kiện không?**
**Không.** Chúng là hai họ quy ước khác nhau, và ngay trong mỗi họ cũng có nhiều định nghĩa tùy tiêu chuẩn và ngành. Luôn phải **ghi rõ điều kiện tham chiếu** bên cạnh con số.

**FAD của máy nén khí là gì?**
Là **lượng khí ở điều kiện môi trường mà máy hút vào được**. Đây là cách nhà sản xuất máy nén công bố công suất, và **không so sánh trực tiếp được** với số đọc của đồng hồ trong đường ống nén.

**Vì sao nên dùng kg/h cho hơi nước?**
Vì khối lượng **không phụ thuộc áp suất và nhiệt độ**, nên tránh được hoàn toàn bài toán bù — nguồn sai số lớn nhất khi đo hơi.

**Vận tốc dòng dùng để làm gì?**
Để **chọn cỡ cảm biến**. Lưu lượng = vận tốc × tiết diện ống. Vận tốc quá thấp thì sai số lớn, quá cao thì tổn thất áp và mài mòn.

**Tính vận tốc dùng đường kính nào?**
**Đường kính trong** của ống, không phải đường kính danh nghĩa. Với ống thành dày, hai con số này chênh nhau đáng kể.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /cach-chon-cam-bien-luu-luong/, /dau-day-cam-bien-luu-luong/, /do-luu-luong-khi-nen/, /do-luu-luong-hoi-nuoc/, /lien-he/. -->
