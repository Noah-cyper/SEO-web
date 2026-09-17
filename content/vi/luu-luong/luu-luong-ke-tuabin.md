<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /luu-luong-ke-tuabin/
TỪ KHÓA    : lưu lượng kế tuabin | turbine flow meter | hệ số k | đồng hồ đo dầu | bánh răng oval
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 9/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Lưu Lượng Kế Tuabin – Hệ Số K, Ưu Nhược Và Khi Nào Nên Dùng
META (156)  : Lưu lượng kế tuabin hoạt động ra sao, hệ số K là gì, vì sao độ nhớt làm sai số và những môi chất tuyệt đối không dùng. So sánh với bánh răng oval.

H1          : Lưu Lượng Kế Tuabin

---

## Công nghệ cơ khí vẫn giữ chỗ đứng sau nhiều thập kỷ

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-tuabin.svg)


Giữa các công nghệ điện tử hiện đại, **lưu lượng kế tuabin** vẫn được dùng rộng rãi — và không phải vì thói quen. Nó có ba ưu điểm mà các công nghệ khác khó có cùng lúc:

- **Độ chính xác tốt** với chất lỏng sạch, ở mức giá thấp hơn nhiều so với Coriolis.
- **Đầu ra xung tự nhiên** — mỗi vòng quay sinh ra một số xung cố định, rất phù hợp để **đếm tổng chính xác**.
- **Đo được chất lỏng không dẫn điện** — dầu, xăng, dung môi — nơi đồng hồ điện từ bất lực.

Đó là lý do tuabin thống trị trong đo nhiên liệu, đo dầu và đo các chất lỏng sạch cần tính tổng.

Nhưng nó cũng là công nghệ **kén môi chất nhất** trong toàn bộ họ thiết bị đo lưu lượng. Một hạt rắn, một sợi rác, hay một thay đổi độ nhớt đủ để làm sai số tăng vọt hoặc hỏng thiết bị.

Bài này trình bày rõ ranh giới đó: tuabin làm được gì rất tốt, và tuyệt đối không nên dùng ở đâu.

> **Cần đo dầu, nhiên liệu hoặc chất lỏng sạch?** Gửi **môi chất · dải lưu lượng · độ nhớt** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-tuabin.svg)


Đây là bài **9/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: cánh quay và tần số xung

Cấu tạo rất trực quan:

1. Một **rotor có cánh** được đặt trong lòng ống, quay tự do trên hai ổ đỡ.
2. **Dòng chảy đẩy vào các cánh** làm rotor quay. Lưu lượng càng lớn, rotor quay càng nhanh.
3. Một **đầu thu (pickup)** gắn bên ngoài thành ống phát hiện mỗi lần một cánh đi qua — thường bằng cảm ứng từ, nên **không cần tiếp xúc trực tiếp với rotor**.
4. Mỗi lần cánh đi qua sinh ra **một xung điện**.
5. **Tần số xung tỷ lệ với lưu lượng thể tích.**

Đơn giản, bền và không cần nguồn điện phức tạp — nhiều loại pickup tự sinh tín hiệu mà không cần cấp nguồn.

### Hệ số K — con số quan trọng nhất

Mỗi thiết bị tuabin có một **hệ số K**, cho biết **bao nhiêu xung tương ứng với một lít (hoặc một mét khối) chất lỏng đi qua**.

Hệ số này được nhà sản xuất xác định bằng **hiệu chuẩn thực tế** — cho chất lỏng chảy qua với lưu lượng đã biết và đếm số xung. Nó được ghi trên nhãn thiết bị và trong giấy chứng nhận đi kèm.

Lưu lượng được tính từ: **tần số xung chia cho hệ số K**.

**Ba điều cần nhớ về hệ số K:**

1. **Mỗi thiết bị có hệ số K riêng** — ngay cả hai thiết bị cùng model cũng chênh nhau chút ít do dung sai chế tạo. Khi thay thiết bị, **phải nhập lại hệ số K mới** vào bộ hiển thị hoặc PLC. Quên bước này là lỗi phổ biến gây sai số ngay từ ngày đầu.
2. **Hệ số K không hoàn toàn cố định** — nó thay đổi theo độ nhớt và theo lưu lượng (xem phần dưới).
3. **Hệ số K thay đổi khi ổ đỡ mòn** — đây là lý do tuabin cần hiệu chuẩn lại định kỳ ([xem bài hiệu chuẩn](/hieu-chuan-cam-bien-luu-luong/)).

### Vì sao độ nhớt ảnh hưởng lớn

Đây là điểm yếu kỹ thuật quan trọng nhất của tuabin.

Rotor quay được là nhờ dòng chảy đẩy vào cánh, nhưng nó cũng bị **ma sát nhớt của chất lỏng cản lại**. Chất lỏng càng nhớt, lực cản càng lớn, rotor quay **chậm hơn so với lưu lượng thực tế** — và thiết bị đọc thấp hơn thực tế.

Hệ quả:

- **Thiết bị được hiệu chuẩn với một loại chất lỏng ở một độ nhớt nhất định.** Dùng cho chất lỏng khác thì hệ số K không còn đúng.
- **Độ nhớt thay đổi theo nhiệt độ.** Dầu lạnh nhớt hơn dầu nóng đáng kể. Đo dầu vào sáng sớm mùa đông và trưa mùa hè có thể cho hai kết quả khác nhau — dù lưu lượng thật như nhau.
- **Ở lưu lượng thấp, ảnh hưởng của ma sát nhớt lớn hơn tương đối**, nên **hệ số K trở nên phi tuyến** ở đáy dải đo.

Đây là lý do tuabin có **giới hạn dưới rõ rệt**: dưới một lưu lượng nhất định, sai số tăng nhanh và thiết bị không còn đáng tin.

Nếu ứng dụng của bạn có **độ nhớt biến động mạnh**, tuabin không phải lựa chọn tốt — hãy xem [Coriolis](/luu-luong-ke-coriolis/), vốn hoàn toàn không bị ảnh hưởng bởi độ nhớt.

---

## Cấu tạo và thông số

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-lapdat.svg)


### Các bộ phận và điểm yếu của chúng

| Bộ phận | Vai trò | Điểm yếu |
|---|---|---|
| **Rotor có cánh** | Quay theo dòng | Cong vênh, mòn cánh nếu có hạt rắn |
| **Ổ đỡ (bearing)** | Đỡ rotor quay | **Bộ phận mòn chính** — quyết định tuổi thọ |
| **Bộ định hướng dòng** | Nắn dòng trước và sau rotor | Có thể bị kẹt bởi rác |
| **Pickup từ** | Đếm xung | Ít hỏng |
| **Thân đo** | Chịu áp | — |

**Ổ đỡ là điểm quyết định tuổi thọ.** Nó quay liên tục suốt thời gian có dòng chảy, và được bôi trơn bằng chính chất lỏng đang đo. Vậy nên:

- **Chất lỏng có tính bôi trơn tốt** (dầu) → ổ đỡ bền.
- **Chất lỏng không bôi trơn** (nước) → ổ đỡ mòn nhanh hơn.
- **Chất lỏng có hạt rắn** → ổ đỡ mòn rất nhanh, có thể kẹt.

Khi ổ đỡ mòn, rotor quay chậm dần và thiết bị **đọc thấp hơn thực tế**. Sai lệch này diễn ra **từ từ** nên rất khó phát hiện nếu không hiệu chuẩn định kỳ — đây là rủi ro lớn nhất của tuabin trong ứng dụng tính chi phí.

### Thông số cần đọc

| Thông số | Lưu ý |
|---|---|
| **Hệ số K** | Ghi trên nhãn, riêng cho từng thiết bị |
| **Dải lưu lượng** | Chú ý **giới hạn dưới** — nơi sai số tăng nhanh |
| **Dải độ nhớt cho phép** | Ngoài dải này thì hệ số K không còn đúng |
| **Độ chính xác** | Thường theo % giá trị đọc trong dải làm việc |
| **Vật liệu ổ đỡ** | Quyết định tuổi thọ với môi chất cụ thể |
| **Áp suất, nhiệt độ** | |
| **Kiểu tín hiệu ra** | Xung là gốc; loại có bộ chuyển đổi thì thêm 4–20mA |
| **Yêu cầu đoạn ống thẳng** | **Dài** — tuabin rất nhạy với biên dạng dòng |
| **Có cần lọc phía trước không** | Với hầu hết ứng dụng là **có** |

### Bộ lọc phía trước — gần như bắt buộc

Vì tuabin rất sợ hạt rắn, hầu hết ứng dụng đều cần một **bộ lọc (strainer) lắp phía trước** thiết bị.

Điều này kéo theo hai hệ quả phải tính vào thiết kế:

1. **Tổn thất áp suất tăng thêm** — cộng vào tổn thất của bản thân tuabin.
2. **Phải vệ sinh lọc định kỳ** — lọc tắc làm giảm lưu lượng và có thể gây hiểu nhầm là thiết bị sai.

---

## Ứng dụng: nơi tuabin là lựa chọn tốt và nơi tuyệt đối tránh

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-nuoc.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-chiphi.svg)

### Rất phù hợp

- **Đo dầu, nhiên liệu, dầu thủy lực** — chất lỏng sạch, có tính bôi trơn tốt cho ổ đỡ.
- **Đo xăng, dầu diesel** trong giao nhận nhiên liệu.
- **Nước sạch đã lọc** — nước cấp cho máy móc, nước làm mát tuần hoàn kín.
- **Dung môi sạch** trong công nghiệp hóa chất.
- **Ứng dụng cần đếm tổng chính xác** — đầu ra xung là ưu thế tự nhiên.
- **Ngân sách trung bình** cần độ chính xác khá.
- **Chất lỏng không dẫn điện** — nơi điện từ không dùng được.

### Tuyệt đối tránh

- **Nước thải, bùn** — kẹt rotor, mòn ổ đỡ, hỏng nhanh. Dùng [đồng hồ điện từ](/dong-ho-luu-luong-dien-tu/).
- **Chất lỏng có sợi, rác, hạt rắn** — kể cả với lọc, rủi ro vẫn cao.
- **Chất lỏng có độ nhớt biến động mạnh** — hệ số K không còn đúng.
- **Chất lỏng rất nhớt** — rotor quay quá chậm, sai số lớn.
- **Lưu lượng dao động đột ngột** — quán tính rotor gây trễ và sai số.
- **Dòng chảy hai pha (có khí lẫn trong lỏng)** — rotor có thể **quay vọt (overspeed)** và hỏng.
- **Ứng dụng không được dừng để bảo trì** — tuabin cần vệ sinh và thay ổ đỡ định kỳ.

### Cảnh báo về hiện tượng quay vọt

Đây là tình huống làm hỏng tuabin nhanh nhất và đáng được nói riêng.

Nếu đường ống **đang rỗng rồi đột ngột được cấp đầy** — ví dụ khi mở van sau khi bảo trì, hoặc khởi động bơm vào ống đã xả cạn — dòng khí và chất lỏng lao qua với tốc độ rất cao. Rotor **quay vượt xa tốc độ thiết kế**, và ổ đỡ có thể hỏng ngay lập tức.

**Phòng ngừa:**
- **Mở van từ từ** khi cấp đầy đường ống lần đầu.
- Bố trí quy trình sao cho **ống được làm đầy chậm** trước khi đạt lưu lượng vận hành.
- Với hệ thường xuyên xả cạn, cân nhắc **van khởi động (bypass)** để nạp ống trước.

Đây là một quy trình vận hành phải được đưa vào hướng dẫn cho người vận hành, không chỉ là chuyện của người lắp đặt.

### Anh em gần: bánh răng oval và cánh gạt

Cùng họ "đo thể tích bằng cơ khí" nhưng nguyên lý khác: **đồng hồ thể tích dương (positive displacement)** đếm số lần một buồng có thể tích cố định được nạp đầy và xả ra.

**Bánh răng oval (oval gear)** là loại phổ biến nhất trong nhóm này.

| Tiêu chí | **Tuabin** | **Bánh răng oval** |
|---|---|---|
| Nguyên lý | Đo vận tốc qua tốc độ quay | **Đếm thể tích từng buồng** |
| Chất lỏng nhớt | **Kém** | **Rất tốt** |
| Chất lỏng loãng | Tốt | Kém hơn |
| Cần đoạn ống thẳng | **Dài** | **Gần như không cần** |
| Tổn thất áp | Trung bình | Cao hơn |
| Chịu hạt rắn | Kém | Kém |
| Ứng dụng điển hình | Nhiên liệu, nước sạch | **Dầu nhớt, mật ong, siro, keo** |

**Quy tắc chọn nhanh:** chất lỏng **loãng** → tuabin; chất lỏng **nhớt** → bánh răng oval. Đây là một trong số ít trường hợp độ nhớt cao lại là ưu điểm — nó giúp bịt kín khe giữa các bánh răng, giảm rò rỉ nội bộ và tăng độ chính xác.

---

## So sánh với các công nghệ khác

| Tiêu chí | **Tuabin** | Điện từ | Coriolis | Siêu âm |
|---|---|---|---|---|
| Môi chất không dẫn điện | **Được** | Không | Được | Được |
| Chịu cặn bẩn | **Rất kém** | Rất tốt | Trung bình | Kém |
| Bộ phận chuyển động | **Có** | Không | Không | Không |
| Ảnh hưởng của độ nhớt | **Lớn** | Không | Không | Ít |
| Độ ổn định theo thời gian | **Giảm dần (mòn ổ)** | Rất tốt | Rất tốt | Tốt |
| Đầu ra xung để đếm tổng | **Tự nhiên** | Có (tạo ra) | Có | Có |
| Đoạn ống thẳng | **Dài** | Ngắn | Gần như không | Trung bình |
| Bảo trì | **Định kỳ, cần lọc** | Rất ít | Ít | Ít |
| Chi phí | **Thấp** | Trung bình | Cao | Trung bình |

**Vị trí của tuabin trong bức tranh chung:** nó là lựa chọn **kinh tế cho chất lỏng sạch, đặc biệt là chất lỏng không dẫn điện**. Ở đó nó cho độ chính xác tốt với chi phí thấp hơn Coriolis nhiều lần.

Ngoài phạm vi đó — môi chất bẩn, nhớt, hoặc biến động — nó thua rõ rệt và không nên cố dùng ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

---

## Sai lầm thường gặp

1. **Dùng cho nước thải hoặc chất lỏng có cặn** — kẹt rotor, hỏng nhanh.
2. **Quên nhập hệ số K mới** khi thay thiết bị — sai số ngay từ đầu.
3. **Không lắp bộ lọc phía trước** — rút ngắn tuổi thọ đáng kể.
4. **Mở van đột ngột vào ống rỗng** — rotor quay vọt và hỏng ổ đỡ.
5. **Bỏ qua ảnh hưởng của độ nhớt** khi môi chất hoặc nhiệt độ thay đổi.
6. **Vận hành ở đáy dải đo** — nơi hệ số K phi tuyến và sai số lớn.
7. **Không hiệu chuẩn lại định kỳ** — ổ đỡ mòn làm thiết bị đọc thấp dần mà không ai biết.
8. **Thiếu đoạn ống thẳng** — tuabin rất nhạy với biên dạng dòng.
9. **Không vệ sinh bộ lọc** — tắc lọc làm giảm lưu lượng, bị hiểu nhầm là thiết bị sai.
10. **Dùng cho chất lỏng nhớt** thay vì chọn bánh răng oval.
11. **Để dòng hai pha (có khí) đi qua** — nguy cơ quay vọt.
12. **Tính tổng từ tín hiệu 4–20mA** thay vì dùng đầu ra xung vốn là thế mạnh của tuabin.

---

## Cam kết tại HOANTRANTDH

- ✅ **Cảnh báo rõ giới hạn môi chất** — chúng tôi không bán tuabin cho nước thải.
- ✅ Tư vấn **chọn tuabin hay bánh răng oval** theo độ nhớt thực tế của chất lỏng.
- ✅ Cung cấp kèm **hệ số K và giấy chứng nhận hiệu chuẩn** của từng thiết bị.
- ✅ Tư vấn **bộ lọc phía trước và quy trình cấp đầy ống** để tránh hỏng ổ đỡ.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **loại chất lỏng và độ nhớt · nhiệt độ làm việc (ảnh hưởng độ nhớt) · dải lưu lượng nhỏ nhất và lớn nhất · đường kính ống · chất lỏng có cặn hay hạt rắn không · mục đích đo (giám sát hay đếm tổng) · đường ống có bị xả cạn thường xuyên không.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lưu lượng kế tuabin hoạt động thế nào?**
Dòng chảy làm **rotor có cánh quay**; đầu thu đếm số lần cánh đi qua và sinh xung. **Tần số xung tỷ lệ với lưu lượng thể tích**.

**Hệ số K là gì?**
Là **số xung tương ứng với một đơn vị thể tích** đi qua thiết bị. Mỗi thiết bị có hệ số K riêng, ghi trên nhãn — **phải nhập đúng vào bộ hiển thị hoặc PLC**.

**Vì sao độ nhớt ảnh hưởng tới kết quả?**
Vì ma sát nhớt **cản rotor quay**, khiến thiết bị đọc thấp hơn thực tế. Độ nhớt lại thay đổi theo nhiệt độ, nên cùng một lưu lượng có thể cho hai kết quả ở hai thời điểm khác nhau.

**Tuabin có đo được nước thải không?**
**Tuyệt đối không nên.** Cặn, sợi và rác sẽ kẹt rotor và làm mòn ổ đỡ rất nhanh. Dùng **đồng hồ điện từ** cho nước thải.

**Vì sao cần lắp bộ lọc phía trước?**
Vì **hạt rắn làm mòn và kẹt rotor**. Nhưng phải tính thêm **tổn thất áp của bộ lọc** và có lịch vệ sinh — lọc tắc gây giảm lưu lượng và dễ bị hiểu nhầm là thiết bị sai.

**Quay vọt (overspeed) là gì?**
Là khi **ống rỗng được cấp đầy đột ngột**, dòng lao qua làm rotor quay vượt xa tốc độ thiết kế và **hỏng ổ đỡ ngay lập tức**. Phòng ngừa bằng cách mở van từ từ.

**Tuabin hay bánh răng oval tốt hơn?**
Tùy độ nhớt: **chất lỏng loãng → tuabin**; **chất lỏng nhớt (dầu nhớt, siro, keo) → bánh răng oval**. Bánh răng oval còn gần như không cần đoạn ống thẳng.

**Vì sao tuabin đọc thấp dần theo năm?**
Vì **ổ đỡ mòn** làm rotor quay chậm hơn. Sai lệch diễn ra từ từ nên chỉ phát hiện được bằng **hiệu chuẩn định kỳ**.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /dong-ho-luu-luong-dien-tu/, /luu-luong-ke-coriolis/, /hieu-chuan-cam-bien-luu-luong/, /cach-chon-cam-bien-luu-luong/, /lien-he/. -->
