<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /luu-luong-ke-vortex/
TỪ KHÓA    : lưu lượng kế vortex | vortex flow meter | đo lưu lượng hơi | xoáy karman | vortex đa biến
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 10/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Lưu Lượng Kế Vortex – Lựa Chọn Số Một Cho Hơi Nước
META (156)  : Vortex đo lưu lượng bằng tần số xoáy Karman, chịu nhiệt cao và đo được cả lỏng, khí, hơi. Nguyên lý, giới hạn dưới, loại đa biến và yêu cầu lắp đặt.

H1          : Lưu Lượng Kế Vortex

---

## Công nghệ được chọn khi môi chất quá nóng cho mọi thứ khác

Khi cần đo **hơi nước**, danh sách lựa chọn thu hẹp rất nhanh. Đồng hồ điện từ không dùng được (hơi không dẫn điện). Tuabin không chịu nổi nhiệt độ và sẽ hỏng. Coriolis dùng được nhưng đắt và tổn thất áp lớn. Siêu âm gặp khó với hơi.

Còn lại hai phương án thực tế: **chênh áp (orifice)** và **vortex**. Và giữa hai cái đó, vortex thường thắng vì một lý do đơn giản — **dải đo rộng hơn nhiều**.

Đó là lý do vortex trở thành **lựa chọn mặc định cho đo hơi nước công nghiệp**, và cũng được dùng rộng rãi cho khí và chất lỏng ở nhiệt độ cao.

Điểm mạnh nền tảng của vortex: **không có bộ phận chuyển động nào**. Chỉ một thanh cản đặt ngang dòng và một cảm biến. Không có gì để mòn, để kẹt, để thay. Trong môi trường hơi nóng, đó là ưu điểm quyết định về tuổi thọ.

Đổi lại, vortex có một ràng buộc rõ rệt mà ai dùng cũng phải biết: **dưới một vận tốc nhất định, nó không đo được gì cả**.

> **Cần đo hơi, khí hoặc chất lỏng nhiệt độ cao?** Gửi **môi chất · áp suất · nhiệt độ · dải lưu lượng** → [Nhận tư vấn](#bao-gia).

Đây là bài **10/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: xoáy Karman

Hiện tượng vật lý nền tảng rất quen thuộc: khi dòng chảy gặp một vật cản, nó không đi vòng qua một cách êm ả mà **sinh ra các xoáy luân phiên ở hai bên vật cản**. Đó là lý do dây điện rung và phát ra tiếng u u khi gió thổi qua, và là lý do cờ bay phần phật.

Chuỗi xoáy luân phiên này gọi là **dãy xoáy Karman (Karman vortex street)**.

Lưu lượng kế vortex khai thác hiện tượng đó:

1. Một **thanh cản (bluff body)** được đặt ngang dòng chảy trong lòng ống.
2. Dòng chảy qua thanh cản sinh ra **các xoáy luân phiên** — một xoáy bên trên, rồi một xoáy bên dưới, đều đặn.
3. Mỗi xoáy tạo ra một **dao động áp suất cục bộ**.
4. Một **cảm biến** (thường là phần tử áp điện) phát hiện các dao động này và đếm chúng.
5. **Tần số xoáy tỷ lệ thuận với vận tốc dòng chảy.**

Quan hệ này được mô tả bằng công thức: **f = St · v / d**, trong đó f là tần số xoáy, v là vận tốc, d là bề rộng thanh cản, và **St là hằng số Strouhal**.

### Vì sao hằng số Strouhal là chìa khóa

Điểm đáng chú ý nhất của công nghệ vortex nằm ở chỗ này: **hằng số Strouhal gần như không đổi** trong một dải số Reynolds rộng.

Nghĩa là tần số xoáy **chỉ phụ thuộc vào vận tốc và hình dạng thanh cản** — không phụ thuộc vào:

- Khối lượng riêng của môi chất
- Độ nhớt
- Nhiệt độ
- Áp suất
- Loại môi chất (lỏng, khí hay hơi)

Hệ quả rất thực tế: **cùng một thiết bị vortex đo được nước, đo được khí, đo được hơi** — với cùng một hệ số hiệu chuẩn. Đây là điều mà tuabin không làm được (hệ số K phụ thuộc độ nhớt) và orifice cũng không (cần biết khối lượng riêng).

Vì lý do đó, vortex được hiệu chuẩn **một lần bằng nước** tại nhà máy, và hệ số đó dùng được cho mọi môi chất ([xem so sánh nguyên lý](/nguyen-ly-do-luu-luong/)).

### Nhưng: có một ngưỡng vận tốc tối thiểu

Đây là hạn chế quan trọng nhất của vortex.

Xoáy Karman chỉ hình thành **rõ ràng và đều đặn khi dòng chảy đủ nhanh** — cụ thể là khi số Reynolds vượt một ngưỡng nhất định. Dưới ngưỡng đó, xoáy không hình thành ổn định, tín hiệu quá yếu hoặc thất thường, và **thiết bị không đo được gì cả**.

Đây không phải chuyện sai số tăng lên như các công nghệ khác — mà là **không có tín hiệu**. Thiết bị sẽ đọc 0.

Hệ quả thực tế:

- **Vortex có giới hạn dưới cứng**, khác với điện từ hay Coriolis vốn chỉ suy giảm độ chính xác dần.
- **Chọn cỡ thiết bị rất quan trọng.** Nếu chọn cỡ bằng cỡ ống mà lưu lượng thực tế nhỏ, vận tốc sẽ dưới ngưỡng và thiết bị vô dụng ở chế độ vận hành bình thường.
- **Thường phải thu nhỏ cỡ vortex** so với cỡ ống, kèm côn thu và côn mở, để nâng vận tốc lên vùng làm việc.

Với môi chất **nhớt** hoặc **lưu lượng rất thấp**, vortex không phải lựa chọn phù hợp ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

---

## Cấu tạo và thông số

### Ba kiểu cảm biến phát hiện xoáy

| Kiểu | Cách hoạt động | Đặc điểm |
|---|---|---|
| **Áp điện (piezo)** | Phần tử áp điện cảm nhận dao động áp suất | Phổ biến nhất, bền, không tiếp xúc môi chất trực tiếp |
| **Cảm biến điện dung** | Đo dao động của một màng | Nhạy ở lưu lượng thấp hơn |
| **Nhiệt (thermal)** | Đo dao động truyền nhiệt | Ít phổ biến |

Với hầu hết ứng dụng công nghiệp, kiểu **áp điện** là lựa chọn tiêu chuẩn.

### Vortex đa biến — điểm cộng lớn cho đo hơi

Đây là tính năng đáng chú ý nhất khi đo hơi và khí.

Vortex cơ bản cho ra **lưu lượng thể tích**. Nhưng với hơi và khí, cái người ta thực sự cần là **lưu lượng khối (kg/h)** — và muốn có nó phải biết khối lượng riêng, tức phải biết áp suất và nhiệt độ ([xem bài đơn vị](/don-vi-luu-luong-quy-doi/)).

**Vortex đa biến (multivariable)** tích hợp sẵn **cảm biến áp suất và cảm biến nhiệt độ** trong cùng một thiết bị, và **tự tính ra lưu lượng khối**.

Lợi ích so với việc lắp ba thiết bị riêng:

- **Một điểm đấu nối thay vì ba** — ít lỗ khoan, ít mối nối, ít rủi ro rò rỉ.
- **Không cần bộ tính toán riêng (flow computer)** — thiết bị tự tính.
- **Ba đại lượng đo tại cùng một điểm** — chính xác hơn so với đo ở ba vị trí khác nhau.
- **Chi phí lắp đặt thấp hơn đáng kể.**
- **Ít điểm hỏng hơn.**

Với ứng dụng đo hơi để tính chi phí hoặc phân bổ cho các phân xưởng, vortex đa biến thường là phương án tối ưu về tổng chi phí ([xem bài hơi nước](/do-luu-luong-hoi-nuoc/)).

### Thông số cần đọc

| Thông số | Lưu ý |
|---|---|
| **Dải lưu lượng** | Chú ý **giới hạn dưới cứng** |
| **Vận tốc tối thiểu** | Khác nhau cho lỏng, khí và hơi |
| **Nhiệt độ cho phép** | Điểm mạnh của vortex — chịu được rất cao |
| **Áp suất định mức** | |
| **Vật liệu thân và thanh cản** | Thép không gỉ là tiêu chuẩn |
| **Kiểu kết nối** | Wafer (rẻ, nhẹ) hoặc mặt bích |
| **Có tích hợp P và T không** | Quyết định có cần thiết bị phụ |
| **Yêu cầu đoạn ống thẳng** | **Dài** — vortex nhạy với biên dạng dòng |
| **Khả năng chịu rung động** | Quan trọng nếu lắp gần bơm, máy nén |

### Điểm yếu: nhạy với rung động

Cảm biến vortex phát hiện **dao động áp suất rất nhỏ**. Rung động cơ khí từ bên ngoài — bơm, máy nén, van rung — có thể tạo ra dao động tương tự và **bị thiết bị hiểu nhầm là xoáy**.

Hậu quả: thiết bị **đọc ra một giá trị lưu lượng dù thực tế không có dòng chảy**, hoặc đọc cao hơn thực tế.

Các thiết bị hiện đại có thuật toán lọc nhiễu khá tốt, nhưng vẫn cần:

- **Không lắp trực tiếp cạnh bơm hoặc máy nén.**
- **Đỡ đường ống chắc chắn** ở hai bên thiết bị.
- Dùng **khớp nối mềm** để cách ly rung nếu cần.
- Kiểm tra khi nghiệm thu: **đóng van hoàn toàn và xác nhận thiết bị đọc 0** ([xem bài lỗi](/loi-cam-bien-luu-luong/)).

Phép kiểm tra cuối cùng rất đáng làm và mất chưa tới một phút.

---

## Ứng dụng: nơi vortex tỏa sáng

### Rất phù hợp

- **Hơi nước bão hòa và hơi quá nhiệt** — ứng dụng số một của vortex.
- **Khí công nghiệp** — nitơ, khí nén ở lưu lượng lớn, khí đốt.
- **Chất lỏng nhiệt độ cao** — dầu tải nhiệt, nước nóng.
- **Nước cấp lò hơi.**
- **Ứng dụng cần độ bền lâu dài** — không có bộ phận mòn.
- **Môi chất không dẫn điện ở nhiệt độ cao** — nơi điện từ và tuabin đều loại.
- **Cần một thiết bị dùng được cho nhiều loại môi chất** — nhờ hằng số Strouhal.

### Không phù hợp

- **Lưu lượng thấp hoặc biến động xuống rất thấp** — dưới ngưỡng thì không đo được.
- **Chất lỏng nhớt** — xoáy không hình thành tốt.
- **Môi chất có nhiều hạt rắn hoặc sợi** — có thể bám vào thanh cản làm sai tần số.
- **Dòng chảy hai pha** (hơi lẫn nước ngưng) — tín hiệu thất thường.
- **Vị trí rung động mạnh** không cách ly được.
- **Đường ống không đủ đoạn thẳng** — vortex khá nhạy.
- **Ống rất nhỏ** — thường không có cỡ phù hợp.

### Lưu ý riêng cho đo hơi

Hơi nước là ứng dụng chính của vortex, và có hai chi tiết đặc thù:

**1. Nước ngưng trong đường ống.** Nếu hơi bị ngưng tụ một phần, dòng trở thành hai pha và tín hiệu vortex thất thường. Cần:
- **Bẫy hơi (steam trap)** hoạt động tốt phía trước.
- **Bọc cách nhiệt đường ống** để giảm ngưng tụ.
- Với hơi bão hòa, **lắp ở đoạn ống nằm ngang** và bố trí thoát nước ngưng.

**2. Bảo vệ cảm biến khỏi nhiệt.** Với hơi quá nhiệt ở nhiệt độ rất cao, phần điện tử cần được đặt cách xa phần đo — dùng loại có **bộ chuyển đổi lắp rời (remote)** thay vì gắn liền.

---

## So sánh với các công nghệ khác cho hơi và khí

| Tiêu chí | **Vortex** | Orifice | Coriolis | Nhiệt (thermal) |
|---|---|---|---|---|
| Đo được hơi | **Tốt** | Tốt | Tốt | Hạn chế |
| Đo được khí | **Tốt** | Tốt | Tốt | **Rất tốt** |
| Dải đo (turndown) | **Khá rộng** | **Hẹp** | Rộng nhất | Rộng |
| Cần bù P, T | Có (hoặc dùng đa biến) | **Có** | **Không** | **Không** |
| Tổn thất áp | Trung bình | **Cao** | Đáng kể | Thấp |
| Bộ phận chuyển động | **Không** | Không | Không | Không |
| Chịu nhiệt cao | **Rất tốt** | Rất tốt | Tốt | Hạn chế |
| Nhạy với rung động | **Có** | Không | Có | Ít |
| Giới hạn dưới | **Cứng** | Mềm | Mềm | Mềm |
| Chi phí | Trung bình | **Thấp** | **Cao** | Trung bình |
| Tích hợp P, T sẵn | **Có (đa biến)** | Không | Không cần | Không cần |

**Cách chọn giữa vortex và orifice cho hơi:**

- **Lưu lượng khá ổn định, ngân sách hạn chế, hệ đã có chuẩn orifice** → orifice.
- **Lưu lượng biến động theo ca hoặc theo mùa** → **vortex** (dải đo rộng hơn hẳn).
- **Cần lưu lượng khối mà không muốn lắp nhiều thiết bị** → **vortex đa biến**.
- **Cần chính xác cao nhất và ngân sách cho phép** → Coriolis.

---

## Sai lầm thường gặp

1. **Chọn cỡ vortex bằng cỡ ống** — vận tốc dưới ngưỡng, thiết bị đọc 0 ở chế độ vận hành bình thường.
2. **Không biết vortex có giới hạn dưới cứng** — tưởng thiết bị hỏng khi nó đọc 0.
3. **Lắp cạnh bơm hoặc máy nén** — rung động gây đọc sai khi không có dòng.
4. **Không kiểm tra thiết bị đọc 0 khi đóng van** lúc nghiệm thu.
5. **Đo hơi mà không bù áp suất và nhiệt độ** — chỉ có thể tích, không có khối lượng.
6. **Lắp thiếu đoạn ống thẳng** — vortex khá nhạy với biên dạng dòng.
7. **Đo hơi có nước ngưng** mà không xử lý bẫy hơi và cách nhiệt.
8. **Dùng cho chất lỏng nhớt** — xoáy không hình thành ổn định.
9. **Đường ống không được đỡ chắc** ở hai bên thiết bị.
10. **Dùng loại gắn liền cho hơi quá nhiệt nhiệt độ rất cao** — nên dùng loại lắp rời.
11. **Không tính tới môi chất có thể bám vào thanh cản** làm sai tần số.
12. **Lắp ba thiết bị riêng (lưu lượng, áp, nhiệt)** khi vortex đa biến rẻ hơn và ít lỗi hơn.

---

## Cam kết tại HOANTRANTDH

- ✅ **Tính chọn cỡ theo vận tốc**, đảm bảo thiết bị làm việc trên ngưỡng tối thiểu ở mọi chế độ vận hành.
- ✅ Tư vấn **vortex đa biến** khi cần lưu lượng khối — thường rẻ hơn lắp ba thiết bị riêng.
- ✅ Cảnh báo rõ **giới hạn dưới cứng** và các điều kiện rung động trước khi báo giá.
- ✅ Cung cấp đồng bộ vortex, [cảm biến áp suất](/cam-bien-ap-suat-la-gi-cach-chon/) và [cảm biến nhiệt độ](/cam-bien-nhiet-do/) cho bài toán bù.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá lưu lượng kế vortex

Gửi cho chúng tôi: **môi chất (hơi bão hòa, hơi quá nhiệt, khí, chất lỏng) · áp suất và nhiệt độ làm việc · dải lưu lượng **nhỏ nhất** và lớn nhất · đường kính ống · vị trí lắp có gần bơm hoặc máy nén không · cần lưu lượng thể tích hay khối lượng · sơ đồ đoạn ống thẳng khả dụng.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lưu lượng kế vortex hoạt động thế nào?**
Một **thanh cản** đặt ngang dòng sinh ra **các xoáy luân phiên** hai bên. Cảm biến đếm tần số xoáy, và **tần số này tỷ lệ với vận tốc dòng chảy**.

**Vì sao vortex đo được cả lỏng, khí và hơi?**
Vì **hằng số Strouhal gần như không đổi** trong dải Reynolds làm việc, nên tần số xoáy chỉ phụ thuộc vận tốc — không phụ thuộc khối lượng riêng, độ nhớt hay loại môi chất.

**Vì sao vortex đọc 0 dù có dòng chảy?**
Vì **vận tốc dưới ngưỡng tối thiểu** — xoáy không hình thành ổn định. Đây là **giới hạn dưới cứng** của vortex, thường do chọn cỡ thiết bị quá lớn so với lưu lượng thực tế.

**Vortex đa biến là gì?**
Là loại **tích hợp sẵn cảm biến áp suất và nhiệt độ**, tự tính ra **lưu lượng khối (kg/h)**. Rẻ hơn và ít điểm hỏng hơn so với lắp ba thiết bị riêng.

**Vortex có bị ảnh hưởng bởi rung động không?**
**Có.** Rung từ bơm hoặc máy nén có thể bị hiểu nhầm là xoáy, khiến thiết bị đọc giá trị dù không có dòng. Cần đỡ ống chắc và **kiểm tra đọc 0 khi đóng van**.

**Vortex hay orifice tốt hơn cho hơi?**
**Vortex** khi lưu lượng biến động (dải đo rộng hơn hẳn) hoặc khi cần tích hợp bù P, T. **Orifice** khi lưu lượng ổn định, ngân sách hạn chế và hệ đã theo chuẩn orifice.

**Đo hơi có nước ngưng thì sao?**
Dòng hai pha làm tín hiệu thất thường. Cần **bẫy hơi hoạt động tốt**, **bọc cách nhiệt đường ống** và bố trí thoát nước ngưng phía trước thiết bị.

**Vortex có cần bảo trì không?**
**Rất ít** — không có bộ phận chuyển động nào. Chủ yếu là kiểm tra thanh cản không bị bám bẩn và xác nhận thiết bị vẫn đọc 0 khi không có dòng.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /don-vi-luu-luong-quy-doi/, /luu-luong-ke-chenh-ap-orifice/, /luu-luong-ke-coriolis/, /do-luu-luong-hoi-nuoc/, /loi-cam-bien-luu-luong/, /cach-chon-cam-bien-luu-luong/, /cam-bien-ap-suat-la-gi-cach-chon/, /cam-bien-nhiet-do/, /lien-he/. -->
