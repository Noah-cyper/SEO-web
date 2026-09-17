<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /cam-bien-luu-luong-khi-nhiet/
TỪ KHÓA    : cảm biến lưu lượng khí kiểu nhiệt | thermal mass flow meter | đo lưu lượng khí nén | nm3/h | đo khí không cần bù
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 12/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Cảm Biến Lưu Lượng Khí Kiểu Nhiệt – Ra Nm³/h Không Cần Bù
META (156)  : Cảm biến nhiệt đo trực tiếp lưu lượng khối của khí, không cần bù áp suất và nhiệt độ. Nguyên lý, vì sao phụ thuộc thành phần khí và cách lắp loại insertion.

H1          : Cảm Biến Lưu Lượng Khí Kiểu Nhiệt

---

## Công nghệ được thiết kế riêng cho khí

Hầu hết công nghệ đo lưu lượng được phát triển cho chất lỏng rồi mở rộng sang khí. **Cảm biến nhiệt thì ngược lại** — nó sinh ra để đo khí, và đó là nơi nó vượt trội.

Ba lý do khiến nó được chọn cho khí nén và khí công nghiệp:

**1. Cho ra lưu lượng khối trực tiếp.** Kết quả là **Nm³/h hoặc kg/h ngay lập tức**, không cần đo thêm áp suất và nhiệt độ để bù. Với khí — nơi khối lượng riêng thay đổi mạnh theo áp suất — đây là ưu điểm rất lớn ([xem bài đơn vị](/don-vi-luu-luong-quy-doi/)).

**2. Đo được lưu lượng rất thấp.** Đây là điểm mà vortex và orifice đều thất bại. Cảm biến nhiệt vẫn hoạt động ở vận tốc khí rất nhỏ, và có **dải đo rộng**.

**3. Gần như không gây tổn thất áp.** Chỉ có một thanh dò nhỏ trong dòng khí. Với hệ khí nén — nơi mỗi bar áp suất đều là tiền điện của máy nén — đây là ưu điểm kinh tế thật.

Cộng thêm một lợi thế triển khai: loại **insertion (cắm vào ống)** chỉ cần **khoan một lỗ và hàn một cổ nối**. Không cắt ống, không tháo đoạn ống nào. Với ống khí nén lớn, đây là khác biệt lớn về chi phí lắp đặt.

Nhưng nó có một ràng buộc mà bất kỳ ai dùng cũng phải hiểu: **kết quả phụ thuộc vào thành phần khí**.

> **Cần đo khí nén hoặc khí công nghiệp?** Gửi **loại khí · đường kính ống · dải lưu lượng** → [Nhận tư vấn](#bao-gia).

Đây là bài **12/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: khí mang nhiệt đi

Nguyên lý dựa trên một hiện tượng quen thuộc: **gió thổi qua làm vật nóng nguội nhanh hơn**. Càng nhiều khí đi qua, càng mất nhiệt nhanh.

Thiết bị có hai đầu dò nhiệt độ đặt trong dòng khí:

1. **Đầu dò tham chiếu** — chỉ đo nhiệt độ của khí, không được sấy.
2. **Đầu dò gia nhiệt** — được sấy nóng lên cao hơn nhiệt độ khí một khoảng nhất định.

Khi khí chảy qua, nó **mang nhiệt đi khỏi đầu dò gia nhiệt**. Mạch điều khiển phải cấp thêm công suất để duy trì chênh lệch nhiệt độ giữa hai đầu dò.

**Công suất cần cấp tỷ lệ với lượng khối khí đi qua.**

Có hai cách vận hành:
- **Giữ chênh nhiệt độ không đổi**, đo công suất — cách phổ biến, đáp ứng nhanh.
- **Giữ công suất không đổi**, đo chênh nhiệt độ — đơn giản hơn.

### Vì sao ra thẳng lưu lượng khối

Đây là điểm cốt lõi và đáng hiểu kỹ.

Lượng nhiệt mà dòng khí mang đi **phụ thuộc vào số phân tử khí đi qua**, chứ không phụ thuộc vào chúng chiếm bao nhiêu thể tích.

Nếu bạn tăng áp suất khí lên gấp đôi mà giữ nguyên thể tích đi qua, thì **số phân tử tăng gấp đôi** — và lượng nhiệt bị mang đi cũng tăng tương ứng. Cảm biến "cảm nhận" đúng phần tăng đó.

Nói cách khác: **cảm biến nhiệt đo trực tiếp lượng khối, không qua thể tích**. Không cần biết áp suất, không cần biết nhiệt độ, không cần bù gì cả.

Đây chính là ưu thế quyết định so với vortex hay orifice — những công nghệ cho ra thể tích rồi phải đo thêm áp suất và nhiệt độ để quy về khối lượng, với mỗi phép đo thêm là một nguồn sai số ([xem so sánh nguyên lý](/nguyen-ly-do-luu-luong/)).

### Ràng buộc: phụ thuộc thành phần khí

Đây là mặt trái của nguyên lý.

Mỗi loại khí có **khả năng dẫn nhiệt và nhiệt dung riêng khác nhau**. Cùng một lượng khối, khí này mang nhiệt đi nhiều hơn khí kia.

Hệ quả:

- **Thiết bị được hiệu chuẩn cho một loại khí cụ thể** — thường là không khí, hoặc loại khí bạn khai báo khi đặt hàng.
- **Dùng cho loại khí khác thì kết quả sai** — có thể sai đáng kể.
- **Nếu thành phần hỗn hợp khí thay đổi**, kết quả cũng thay đổi theo.

**Ba điều cần làm:**

1. **Khai rõ loại khí khi đặt hàng.** Không khí, nitơ, oxy, CO₂, argon, khí đốt, biogas — mỗi loại một hệ số.
2. **Với hỗn hợp khí, cung cấp thành phần cụ thể** để nhà sản xuất hiệu chuẩn đúng.
3. **Nếu thành phần thay đổi theo thời gian** (ví dụ biogas có tỷ lệ metan biến động), cân nhắc công nghệ khác — hoặc chấp nhận sai số tương ứng.

Nhiều thiết bị cho phép **chọn loại khí trong menu** từ một danh sách đã lập trình sẵn. Tiện, nhưng độ chính xác thường thấp hơn so với hiệu chuẩn riêng cho loại khí đó tại nhà máy.

---

## Cấu tạo và thông số

### Hai kiểu lắp đặt

**Loại inline (lắp trong ống).**
Toàn bộ khí đi qua thiết bị. Chính xác hơn, dùng cho ống nhỏ và vừa.

**Loại insertion (cắm vào ống).**
Một thanh dò cắm xuyên thành ống vào giữa dòng khí.

| Tiêu chí | **Inline** | **Insertion** |
|---|---|---|
| Cách lắp | Cắt ống, lắp đoạn | **Khoan lỗ, hàn cổ nối** |
| Dừng sản xuất | Có | Ngắn hoặc không (với van cách ly) |
| Chi phí theo cỡ ống | Tăng nhanh | **Gần như không tăng** |
| Độ chính xác | **Cao hơn** | Thấp hơn |
| Nhạy với biên dạng dòng | Thấp hơn | **Cao** |
| Phù hợp | Ống nhỏ và vừa | **Ống lớn** |

**Loại insertion là lựa chọn phổ biến nhất cho khí nén** trong nhà máy, vì đường ống khí nén thường lớn và chi phí lắp đặt thấp là yếu tố quyết định.

**Lưu ý quan trọng với insertion:** vì nó đo vận tốc **tại một điểm** rồi suy ra trung bình toàn tiết diện, nên:

- **Độ sâu cắm phải đúng** — nhà sản xuất quy định vị trí cụ thể theo đường kính ống. Cắm sai độ sâu là sai số hệ thống.
- **Hướng đầu dò phải đúng** — có dấu chỉ hướng dòng chảy trên thân.
- **Cần đoạn ống thẳng dài hơn** so với loại inline.

Nhiều thiết bị insertion có **van bi cách ly** cho phép rút thanh dò ra để vệ sinh **mà không cần dừng hệ thống** — tính năng rất đáng có cho hệ chạy liên tục.

### Thông số cần đọc

| Thông số | Lưu ý |
|---|---|
| **Loại khí hiệu chuẩn** | **Quan trọng nhất** — phải khớp khí thực tế |
| **Dải lưu lượng** | Theo Nm³/h hoặc kg/h |
| **Turndown** | Rộng — ưu điểm của công nghệ này |
| **Điều kiện quy chiếu** | Nm³ quy về điều kiện nào — **phải ghi rõ** |
| **Áp suất, nhiệt độ cho phép** | |
| **Vật liệu đầu dò** | Thép không gỉ là tiêu chuẩn |
| **Độ sâu cắm** (insertion) | Theo bảng của nhà sản xuất |
| **Đường kính ống áp dụng** | Thiết bị được cấu hình theo cỡ ống cụ thể |
| **Tín hiệu ra** | 4–20mA, xung, Modbus |
| **Có đếm tổng không** | Cần cho tính chi phí khí nén |

### Ba điều kiện làm sai kết quả

**1. Khí ẩm hoặc có giọt lỏng.** Nước ngưng bám vào đầu dò làm **thay đổi hoàn toàn đặc tính truyền nhiệt** — thiết bị đọc sai rất nhiều. Với khí nén, phải đảm bảo **lắp sau máy sấy khí**, hoặc ít nhất sau bình tách nước.

**2. Dầu và bụi bám vào đầu dò.** Lớp bám tạo ra **cách nhiệt**, làm thiết bị đọc thấp dần theo thời gian. Trong hệ khí nén có dầu (máy nén có dầu), đây là vấn đề thực tế — cần vệ sinh đầu dò định kỳ.

**3. Đầu dò bị mòn.** Với khí có hạt bụi ở vận tốc cao, lớp phủ đầu dò có thể mòn dần.

Cả ba đều dẫn tới **sai lệch từ từ**, không phải hỏng đột ngột — nên chỉ phát hiện được bằng **kiểm tra định kỳ hoặc so sánh với nguồn tham chiếu** ([xem bài hiệu chuẩn](/hieu-chuan-cam-bien-luu-luong/)).

---

## Ứng dụng: khí nén là ứng dụng số một

### Đo khí nén trong nhà máy

Đây là ứng dụng phổ biến nhất, và nó phục vụ ba mục đích khác nhau:

**1. Phát hiện rò rỉ.** Đo lưu lượng khí nén **vào lúc không sản xuất** — ban đêm, ngày nghỉ, giữa ca. Về lý thuyết lưu lượng phải bằng 0. Nếu vẫn có dòng đáng kể, đó chính là **lượng khí rò rỉ**, đang được máy nén tạo ra và trả tiền điện suốt 24/7.

Đây là phép đo đơn giản nhất mà cho giá trị cao nhất trong toàn bộ hệ khí nén. Rất nhiều nhà máy phát hiện lượng rò rỉ đáng kể chỉ bằng một lần đo ban đêm ([xem bài khí nén](/do-luu-luong-khi-nen/)).

**2. Phân bổ chi phí theo bộ phận.** Lắp đồng hồ ở nhánh cấp cho từng xưởng để biết ai dùng bao nhiêu. Khi chi phí được gán cho từng đơn vị, hành vi sử dụng thay đổi rõ rệt.

**3. Theo dõi hiệu suất máy nén.** So sánh lưu lượng khí sản xuất ra với điện năng tiêu thụ. Tỷ lệ này xấu đi theo thời gian là dấu hiệu máy nén cần bảo trì.

### Các ứng dụng khác

- **Khí công nghiệp** — nitơ, oxy, argon, CO₂ trong sản xuất và y tế.
- **Khí đốt, LPG** — đo tiêu thụ cho lò, nồi hơi.
- **Biogas** — đo sản lượng hầm biogas (lưu ý thành phần biến động).
- **Khí thải, ống khói** — giám sát phát thải.
- **Khí cấp cho lò** — kiểm soát tỷ lệ nhiên liệu–không khí, ảnh hưởng trực tiếp hiệu suất cháy.
- **Thông gió, hút bụi** — đo lưu lượng gió trong ống lớn.
- **Sục khí trong xử lý nước thải** — đây là hộ tiêu thụ điện lớn trong trạm xử lý, đo được là quản lý được.

### Vị trí lắp đặt cho khí nén

Thứ tự ưu tiên trong hệ khí nén điển hình:

1. **Sau máy sấy khí** — quan trọng nhất, để khí đã khô.
2. **Trên đường ống chính sau bình chứa** — đo tổng lượng tiêu thụ.
3. **Trên từng nhánh cấp cho xưởng** — để phân bổ chi phí.
4. **Đủ đoạn ống thẳng** — insertion cần khá dài.
5. **Tránh ngay sau van điều áp** — dòng nhiễu mạnh.

---

## So sánh với các công nghệ đo khí khác

| Tiêu chí | **Nhiệt (thermal)** | Vortex | Orifice | Coriolis |
|---|---|---|---|---|
| Ra khối lượng trực tiếp | **Có** | Không | Không | **Có** |
| Cần bù P, T | **Không** | Có | Có | **Không** |
| Đo được lưu lượng rất thấp | **Rất tốt** | **Không** | Kém | Tốt |
| Turndown | **Rộng** | Trung bình | **Hẹp** | **Rộng nhất** |
| Tổn thất áp | **Rất thấp** | Trung bình | **Cao** | Đáng kể |
| Phụ thuộc thành phần khí | **Có** | Không | Có (qua ρ) | Không |
| Chịu khí ẩm | **Kém** | Trung bình | Trung bình | Tốt |
| Lắp trên ống lớn | **Dễ (insertion)** | Khó | Trung bình | **Rất khó** |
| Chi phí | Trung bình | Trung bình | **Thấp** | **Cao** |
| Bộ phận chuyển động | Không | Không | Không | Không |

**Cách chọn cho khí nén:**

- **Ứng dụng tiêu chuẩn (phát hiện rò rỉ, phân bổ chi phí)** → **cảm biến nhiệt insertion**. Đây là lựa chọn mặc định và thường là đúng.
- **Lưu lượng rất lớn và ổn định, ngân sách thấp** → orifice.
- **Cần chính xác rất cao, thành phần khí biến động** → Coriolis.
- **Đã có hệ đo áp suất và nhiệt độ sẵn** → vortex đa biến cũng là phương án.

**Điểm quyết định:** nếu bạn cần đo **lưu lượng khí nén ở mức thấp** — ví dụ để phát hiện rò rỉ ban đêm — thì **chỉ cảm biến nhiệt làm được**. Vortex sẽ đọc 0 vì dưới ngưỡng, orifice thì chênh áp quá nhỏ để đo. Đây là lý do nó gần như không có đối thủ trong ứng dụng này ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

---

## Sai lầm thường gặp

1. **Không khai đúng loại khí** — kết quả sai theo hệ số của loại khí.
2. **Dùng thiết bị hiệu chuẩn cho không khí để đo khí khác** mà không đổi cấu hình.
3. **Lắp trước máy sấy khí** — khí ẩm làm sai lệch nghiêm trọng.
4. **Không vệ sinh đầu dò định kỳ** trong hệ khí nén có dầu — đọc thấp dần.
5. **Cắm sai độ sâu** với loại insertion — sai số hệ thống.
6. **Lắp ngược hướng đầu dò** so với chiều dòng chảy.
7. **Thiếu đoạn ống thẳng** — insertion rất nhạy với biên dạng dòng.
8. **Nhầm Nm³/h với m³/h thực tế** khi so với thông số máy nén.
9. **Không ghi rõ điều kiện quy chiếu** của Nm³ trong hồ sơ.
10. **Dùng cho hỗn hợp khí có thành phần biến động** mà không tính tới sai số.
11. **Bỏ qua chức năng đếm tổng** — mất khả năng tính chi phí theo tháng.
12. **Không đo lúc không sản xuất** — bỏ lỡ phép đo phát hiện rò rỉ có giá trị nhất.

---

## Cam kết tại HOANTRANTDH

- ✅ **Xác nhận đúng loại khí và điều kiện quy chiếu** trước khi cấu hình thiết bị.
- ✅ Tư vấn **vị trí lắp trong hệ khí nén** — đặc biệt là yêu cầu lắp sau máy sấy khí.
- ✅ Đề xuất **loại insertion có van cách ly** để rút đầu dò vệ sinh mà không dừng hệ.
- ✅ Hỗ trợ **quy trình đo phát hiện rò rỉ** — phép đo cho giá trị cao nhất trong hệ khí nén.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **loại khí (hoặc thành phần hỗn hợp) · đường kính và vật liệu ống · áp suất và nhiệt độ làm việc · dải lưu lượng nhỏ nhất và lớn nhất · khí đã qua máy sấy chưa · máy nén có dầu hay không dầu · mục đích đo · sơ đồ đoạn ống thẳng khả dụng.**

**→ [Liên hệ nhận tư vấn đo khí](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến lưu lượng khí kiểu nhiệt hoạt động thế nào?**
Một đầu dò được **sấy nóng** đặt trong dòng khí; khí chảy qua **mang nhiệt đi**. Công suất cần cấp để giữ chênh nhiệt độ **tỷ lệ với lưu lượng khối**.

**Vì sao không cần bù áp suất và nhiệt độ?**
Vì lượng nhiệt bị mang đi phụ thuộc **số phân tử khí đi qua**, tức là khối lượng — không phụ thuộc thể tích. Kết quả ra thẳng Nm³/h hoặc kg/h.

**Vì sao phải khai đúng loại khí?**
Vì mỗi loại khí có **khả năng dẫn nhiệt và nhiệt dung riêng khác nhau**. Thiết bị hiệu chuẩn cho không khí dùng để đo CO₂ sẽ cho kết quả sai đáng kể.

**Đo được lưu lượng khí rất thấp không?**
**Được, rất tốt** — đây là ưu điểm nổi bật. Vortex sẽ đọc 0 và orifice không đủ chênh áp ở dải này, nên cảm biến nhiệt gần như không có đối thủ khi cần đo lưu lượng khí nhỏ.

**Vì sao phải lắp sau máy sấy khí?**
Vì **nước ngưng bám vào đầu dò làm thay đổi hoàn toàn đặc tính truyền nhiệt**, khiến thiết bị đọc sai rất nhiều. Khí phải khô.

**Loại insertion lắp thế nào?**
**Khoan một lỗ và hàn cổ nối** trên ống, rồi cắm thanh dò vào. Không cần cắt ống. Phải **cắm đúng độ sâu** theo bảng của nhà sản xuất và đúng hướng dòng chảy.

**Vì sao thiết bị đọc thấp dần theo thời gian?**
Thường do **dầu hoặc bụi bám vào đầu dò**, tạo lớp cách nhiệt. Cần vệ sinh đầu dò định kỳ, nhất là trong hệ khí nén dùng máy nén có dầu.

**Đo khí nén để phát hiện rò rỉ làm thế nào?**
**Đo vào lúc không sản xuất** — ban đêm hoặc ngày nghỉ. Về lý thuyết lưu lượng phải bằng 0; phần còn lại chính là lượng khí rò rỉ đang tốn tiền điện suốt ngày đêm.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /don-vi-luu-luong-quy-doi/, /luu-luong-ke-vortex/, /luu-luong-ke-coriolis/, /hieu-chuan-cam-bien-luu-luong/, /do-luu-luong-khi-nen/, /cach-chon-cam-bien-luu-luong/, /lien-he/. -->
