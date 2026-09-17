<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /dong-ho-luu-luong-dien-tu/
TỪ KHÓA    : đồng hồ lưu lượng điện từ | cảm biến lưu lượng điện từ | magnetic flow meter | đo nước thải | độ dẫn điện tối thiểu
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 6/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Đồng Hồ Lưu Lượng Điện Từ – Nguyên Lý, Ưu Nhược Và Cách Chọn
META (156)  : Đồng hồ lưu lượng điện từ hoạt động thế nào, vì sao chỉ đo được chất lỏng dẫn điện, cách chọn lớp lót và điện cực, yêu cầu lắp đặt và các lỗi hay gặp.

H1          : Đồng Hồ Lưu Lượng Điện Từ (MAG)

---

## Lựa chọn mặc định cho chất lỏng dẫn điện

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-dong-ho-dien-tu.svg)


Nếu bạn cần đo nước, nước thải, bùn hoặc hóa chất dẫn điện, **đồng hồ điện từ gần như luôn là câu trả lời đúng** — và nên là thiết bị đầu tiên bạn xét, trước khi cân nhắc bất kỳ công nghệ nào khác.

Lý do nằm ở một đặc điểm cấu tạo rất đặc biệt: **bên trong đồng hồ điện từ không có gì cả**. Không cánh quạt, không vật cản, không lỗ thu hẹp. Chỉ là một đoạn ống trơn có lớp lót cách điện, hai điện cực nhỏ nằm ngang mức thành ống, và hai cuộn dây bên ngoài.

Từ cấu tạo "không có gì" đó sinh ra một loạt ưu điểm mà các công nghệ khác khó có cùng lúc:

- **Không gây tổn thất áp suất** — dòng chảy đi qua như đi qua một đoạn ống bình thường.
- **Không bị kẹt bởi cặn, sợi, rác** — không có gì để kẹt vào.
- **Không mài mòn** — không có bộ phận chuyển động.
- **Đo được cả bùn và chất lỏng có hạt rắn** — điều mà tuabin và orifice không làm được.
- **Không nhạy với độ nhớt, áp suất, nhiệt độ** trong dải làm việc.
- **Ít nhạy với biên dạng dòng chảy** hơn các công nghệ đo vận tốc khác.

Đổi lại, nó có **một điều kiện bắt buộc không thể thỏa hiệp**: chất lỏng phải **dẫn điện**.

> **Cần đồng hồ điện từ cho hệ của bạn?** Gửi **môi chất · đường kính ống · dải lưu lượng** → [Nhận tư vấn chọn model](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-faraday.svg)


Đây là bài **6/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: định luật cảm ứng điện từ Faraday

Nguyên lý hoạt động dựa trên một định luật vật lý cơ bản: **khi một vật dẫn chuyển động cắt ngang các đường sức từ, trong vật dẫn xuất hiện một sức điện động tỷ lệ với vận tốc chuyển động**.

Áp dụng vào đường ống:

1. **Hai cuộn dây** bên ngoài ống tạo ra **từ trường** xuyên ngang qua dòng chảy.
2. **Chất lỏng dẫn điện** chảy qua chính là vật dẫn đang chuyển động cắt từ trường.
3. Trong chất lỏng xuất hiện một **sức điện động** vuông góc với cả từ trường lẫn hướng dòng chảy.
4. **Hai điện cực** đặt đối diện nhau trên thành ống thu lấy hiệu điện thế này.
5. Bộ chuyển đổi khuếch đại, xử lý và tính ra **vận tốc trung bình**, rồi nhân với tiết diện ống để ra **lưu lượng thể tích**.

Điểm đáng chú ý: sức điện động sinh ra **tỷ lệ tuyến tính với vận tốc** — không phải căn bậc hai như phương pháp chênh áp. Đây là lý do đồng hồ điện từ có **dải đo rộng** và giữ độ chính xác tốt cả ở lưu lượng thấp ([xem so sánh nguyên lý](/nguyen-ly-do-luu-luong/)).

### Vì sao ít nhạy với biên dạng dòng chảy

Đây là ưu điểm kỹ thuật quan trọng nhưng ít được nói tới.

Các công nghệ như tuabin hay vortex đo vận tốc **tại một vùng cục bộ** rồi suy ra trung bình. Nếu biên dạng dòng bị méo, vùng cục bộ đó không còn đại diện cho toàn tiết diện và kết quả sai.

Đồng hồ điện từ khác: sức điện động mà điện cực thu được là **kết quả tổng hợp trên toàn bộ mặt cắt ngang** của dòng chảy. Nhờ vậy, biên dạng có hơi méo thì ảnh hưởng vẫn nhỏ hơn đáng kể.

Đây là lý do đồng hồ điện từ **yêu cầu đoạn ống thẳng ngắn hơn** so với tuabin, vortex hay orifice — một lợi thế thực tế lớn khi đường ống chật.

### Kích từ xung — vì sao số liệu ổn định

Các đồng hồ điện từ hiện đại không cấp từ trường một chiều liên tục, mà dùng **kích từ xung (pulsed DC)**: đảo chiều từ trường theo chu kỳ.

Lý do: từ trường một chiều liên tục gây **phân cực điện hóa trên bề mặt điện cực**, làm tín hiệu trôi dần. Đảo chiều theo chu kỳ triệt tiêu hiện tượng này, đồng thời cho phép thiết bị **tự xác định điểm không** trong mỗi chu kỳ — nhờ vậy giữ được ổn định lâu dài mà không cần hiệu chuẩn thường xuyên.

Đây là lý do đồng hồ điện từ nổi tiếng về **độ ổn định theo thời gian**.

---

## Cấu tạo và thông số: chọn đúng lớp lót và điện cực

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-lapdat.svg)


Hai thành phần tiếp xúc trực tiếp với môi chất quyết định tuổi thọ thiết bị.

### Lớp lót (liner)

Thân ống bằng thép không thể tiếp xúc trực tiếp với chất lỏng — vì nó sẽ nối tắt sức điện động. Nên bên trong phải có một **lớp lót cách điện**.

| Loại lót | Đặc điểm | Phù hợp với |
|---|---|---|
| **Cao su cứng (hard rubber)** | Rẻ, bền cơ học | Nước sạch, nước thải thông thường |
| **Cao su mềm (soft rubber)** | **Chịu mài mòn tốt** | Bùn, nước có cát, hạt rắn |
| **PTFE (Teflon)** | **Chịu hóa chất rất tốt**, chịu nhiệt cao | Hóa chất ăn mòn, thực phẩm, dược |
| **PFA** | Như PTFE, bề mặt nhẵn hơn | Thực phẩm, dược phẩm, độ tinh khiết cao |
| **Polyurethane** | Chịu mài mòn tốt, giá vừa phải | Bùn khoáng, nước có cát |
| **Ceramic** | Rất bền, chịu chân không | Ứng dụng đặc biệt, mài mòn nặng |

**Ba lưu ý khi chọn lót:**

1. **Lót PTFE có thể bị hút sập nếu đường ống bị chân không.** Nếu hệ có khả năng tạo chân không (ví dụ khi bơm dừng đột ngột), phải chọn loại chịu được hoặc dùng lót khác.
2. **Lót cao su không chịu được nhiệt độ cao** như PTFE.
3. **Với môi chất mài mòn** (bùn có cát), lót mềm chịu tốt hơn lót cứng — điều này trái trực giác nhưng đúng: vật liệu đàn hồi hấp thụ va đập của hạt.

### Điện cực

| Vật liệu điện cực | Phù hợp với |
|---|---|
| **Thép không gỉ 316** | Nước, nước thải thông thường — lựa chọn mặc định |
| **Hastelloy** | Hóa chất ăn mòn |
| **Titan, Tantalum** | Môi chất ăn mòn mạnh, nước biển |
| **Platinum** | Ứng dụng đặc biệt |

**Điện cực kiểu đặc biệt:**
- **Điện cực có mũ nhọn (bullet nose)** — chống bám bẩn ở môi chất dễ đóng cặn.
- **Điện cực cạo được (scraper)** — cho phép làm sạch mà không tháo thiết bị.

**Điện cực nối đất (grounding electrode).** Chất lỏng phải được nối đất để có điểm chuẩn điện thế. Nếu ống là kim loại và tiếp xúc tốt với chất lỏng thì ống làm việc đó. Nhưng nếu ống là **nhựa, PVC, hoặc có lớp lót** thì phải có **vòng nối đất (grounding ring)** hoặc điện cực nối đất riêng.

Đây là lỗi lắp đặt phổ biến nhất của đồng hồ điện từ, gây triệu chứng **số liệu nhảy loạn hoặc trôi** ([xem bài lỗi thường gặp](/loi-cam-bien-luu-luong/)).

### Điều kiện bắt buộc: độ dẫn điện tối thiểu

Đây là ranh giới quyết định dùng được hay không.

Mỗi model có một **ngưỡng độ dẫn điện tối thiểu** ghi trong tài liệu (đơn vị thường là µS/cm). Dưới ngưỡng đó, tín hiệu quá yếu và thiết bị không hoạt động tin cậy.

| Môi chất | Đo được không? |
|---|---|
| **Nước máy, nước giếng, nước thải** | **Được** — độ dẫn thừa đủ |
| **Nước biển, dung dịch muối** | **Được** |
| **Axit, kiềm, dung dịch hóa chất** | **Được** |
| **Bùn, hỗn hợp nước – hạt rắn** | **Được** |
| **Nước siêu tinh khiết (DI water)** | **Thường không** — độ dẫn quá thấp |
| **Dầu, xăng, dầu diesel** | **Không** |
| **Dung môi hữu cơ** | **Không** |
| **Khí, hơi** | **Không** |

**Trường hợp ranh giới — nước siêu tinh khiết:** có model chuyên dụng cho độ dẫn rất thấp, nhưng cần xác nhận cụ thể với nhà sản xuất. Đây không phải điều nên giả định.

Nếu môi chất không dẫn điện, hãy chuyển sang [Coriolis](/luu-luong-ke-coriolis/), [tuabin](/luu-luong-ke-tuabin/) hoặc [siêu âm](/cam-bien-luu-luong-sieu-am/).

---

## Ứng dụng: lắp đặt đúng cách

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-nuoc.svg)


Đồng hồ điện từ dễ tính hơn nhiều công nghệ khác, nhưng vẫn có bốn điều kiện bắt buộc.

### 1. Ống phải luôn đầy

Đây là điều kiện quan trọng nhất và cũng hay bị vi phạm nhất. Nếu ống chỉ đầy một phần, thiết bị vẫn đo vận tốc nhưng nhân với **toàn bộ tiết diện** — kết quả cao hơn thực tế rất nhiều.

**Cách đảm bảo:**
- Lắp ở **đoạn ống thấp nhất** trong hệ, hoặc ở đoạn đi lên.
- **Tránh lắp ở điểm cao nhất** — nơi khí tích tụ.
- **Tránh lắp ngay sau van xả hoặc chỗ ống chảy tự do.**
- Với đường ống có thể chảy không đầy, cân nhắc lắp theo hình chữ U để giữ ống luôn ngập nước.

Nhiều model có chức năng **phát hiện ống rỗng (empty pipe detection)** — nên bật để thiết bị báo lỗi thay vì đọc số sai.

### 2. Không có bọt khí tại vị trí đo

Bọt khí làm giảm diện tích dẫn điện hiệu dụng và gây nhiễu tín hiệu. Triệu chứng: **số liệu nhảy loạn**.

**Xử lý:** lắp ở đoạn ống nằm ngang hoặc đi lên, tránh điểm cao; lắp van xả khí ở điểm cao phía trước nếu cần.

### 3. Nối đất đúng cách

Như đã nói ở trên — với ống nhựa hoặc ống có lót, **bắt buộc phải có vòng nối đất**. Với ống kim loại, cần dây nối đẳng thế giữa thiết bị và hai mặt bích hai bên.

### 4. Đoạn ống thẳng

Yêu cầu ngắn hơn nhiều công nghệ khác, nhưng vẫn cần — tra theo tài liệu của model cụ thể. Phía trước cần dài hơn phía sau ([xem bài lắp đặt](/lap-dat-cam-bien-luu-luong/)).

### Ứng dụng điển hình

- **Cấp nước sạch** — đo tổng, phân bổ, phát hiện rò rỉ.
- **Nước thải và bùn** — ứng dụng mà điện từ gần như không có đối thủ ([xem bài nước thải](/do-luu-luong-nuoc-thai/)).
- **Nước làm mát, nước tuần hoàn** trong hệ HVAC và sản xuất.
- **Hóa chất dẫn điện** — axit, kiềm, dung dịch muối (chọn lót PTFE).
- **Thực phẩm, đồ uống** — sữa, nước ép, dung dịch đường (lót PFA, kết nối clamp vệ sinh).
- **Khai khoáng** — bùn quặng, nước có cát (lót cao su mềm hoặc polyurethane).
- **Định lượng theo mẻ** — kết hợp van và bộ đếm tổng.

---

## So sánh với các công nghệ khác

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-congnghe.svg)


| Tiêu chí | **Điện từ** | Siêu âm | Tuabin | Orifice |
|---|---|---|---|---|
| Môi chất | Chỉ **lỏng dẫn điện** | Lỏng, một số khí | Lỏng/khí **sạch** | Gần như mọi loại |
| Tổn thất áp | **Không** | **Không** | Có | **Cao** |
| Chịu cặn bẩn | **Rất tốt** | Kém | **Rất kém** | Kém |
| Bộ phận chuyển động | Không | Không | **Có** | Không |
| Dải đo (turndown) | **Rộng** | Rộng | Trung bình | **Hẹp** |
| Nhạy với biên dạng dòng | **Thấp** | Trung bình | Cao | Cao |
| Đoạn ống thẳng cần | **Ngắn hơn** | Trung bình | Dài | Dài |
| Độ ổn định lâu dài | **Rất tốt** | Tốt | Giảm dần | Tốt |
| Chi phí | Trung bình | Trung bình | Thấp | **Thấp** |
| Đo được khối lượng | Không | Không | Không | Không |

**Kết luận thực dụng:** với **chất lỏng dẫn điện**, điện từ thắng gần như mọi tiêu chí trừ giá mua ban đầu. Và nếu tính cả **tổn thất áp suất suốt vòng đời**, nó thường thắng cả về chi phí tổng ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

Điện từ chỉ thua trong hai trường hợp: **môi chất không dẫn điện**, và **cần đo khối lượng thật** — khi đó Coriolis là lựa chọn.

---

## Sai lầm thường gặp

1. **Dùng cho dầu, xăng, dung môi** — không dẫn điện, thiết bị không hoạt động.
2. **Quên vòng nối đất** với ống nhựa hoặc ống có lót — số liệu nhảy loạn.
3. **Lắp ở điểm cao nhất của đường ống** — khí tích tụ, ống không đầy.
4. **Lắp ở đoạn ống chảy tự do** không đầy — số đọc cao hơn thực tế nhiều.
5. **Không bật chức năng phát hiện ống rỗng.**
6. **Chọn lót PTFE cho hệ có khả năng tạo chân không** — lót bị hút sập.
7. **Chọn lót cứng cho bùn có cát** — mòn nhanh hơn lót mềm.
8. **Chọn cỡ bằng cỡ ống** khiến vận tốc quá thấp, gây lắng cặn trong thiết bị.
9. **Bỏ qua kiểm tra độ dẫn điện tối thiểu** với môi chất lạ.
10. **Lắp ngay sau van điều tiết** — dù ít nhạy, vẫn cần đoạn thẳng tối thiểu.
11. **Không vệ sinh điện cực** ở môi chất dễ đóng cặn — sai lệch dần theo tháng.
12. **Dùng chung dây nối đất với thiết bị công suất lớn** — nhiễu vào tín hiệu.

---

## Cam kết tại HOANTRANTDH

- ✅ **Kiểm tra độ dẫn điện của môi chất** trước khi đề xuất — không bán thiết bị không dùng được.
- ✅ Tư vấn **chọn lớp lót và vật liệu điện cực** theo tính chất môi chất thực tế.
- ✅ **Tính chọn cỡ theo vận tốc dòng**, kèm côn thu nếu cần để tránh lắng cặn.
- ✅ Hướng dẫn **nối đất và vị trí lắp** — hai yếu tố quyết định số liệu có ổn định hay không.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá đồng hồ điện từ

Gửi cho chúng tôi: **môi chất và tính chất (có cặn, hạt rắn, ăn mòn không) · đường kính và vật liệu ống · dải lưu lượng nhỏ nhất và lớn nhất · áp suất và nhiệt độ · ống luôn đầy hay có lúc chảy không đầy · tín hiệu ra cần dùng · yêu cầu vệ sinh nếu có.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đồng hồ lưu lượng điện từ hoạt động thế nào?**
Theo **định luật cảm ứng Faraday**: chất lỏng dẫn điện chảy qua từ trường sinh ra sức điện động tỷ lệ với vận tốc; hai điện cực thu tín hiệu này và bộ chuyển đổi tính ra lưu lượng.

**Vì sao chỉ đo được chất lỏng dẫn điện?**
Vì nguyên lý cần chất lỏng đóng vai trò **vật dẫn chuyển động** trong từ trường. Dầu, xăng, dung môi và khí không dẫn điện nên không sinh ra tín hiệu.

**Có đo được nước siêu tinh khiết không?**
**Thường là không**, vì độ dẫn điện quá thấp. Có model chuyên dụng cho độ dẫn rất thấp nhưng phải xác nhận cụ thể với nhà sản xuất.

**Chọn lớp lót nào cho nước thải có cát?**
**Cao su mềm hoặc polyurethane** — vật liệu đàn hồi hấp thụ va đập của hạt nên chịu mài mòn tốt hơn lót cứng.

**Vì sao số liệu nhảy loạn?**
Ba nguyên nhân phổ biến nhất: **thiếu vòng nối đất**, **bọt khí trong ống**, hoặc **ống không đầy** tại vị trí lắp.

**Đồng hồ điện từ có gây tổn thất áp suất không?**
**Gần như không** — bên trong là ống trơn, không có vật cản. Đây là ưu điểm kinh tế lớn suốt vòng đời so với tấm orifice.

**Lắp ở vị trí nào là tốt nhất?**
Ở **đoạn ống thấp hoặc đoạn đi lên** để đảm bảo ống luôn đầy. Tránh điểm cao nhất của hệ thống — nơi khí tích tụ.

**Có cần đoạn ống thẳng không?**
**Có**, nhưng ngắn hơn đáng kể so với tuabin, vortex hay orifice — vì thiết bị lấy tín hiệu trên toàn mặt cắt nên ít nhạy với biên dạng dòng.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /luu-luong-ke-coriolis/, /luu-luong-ke-tuabin/, /cam-bien-luu-luong-sieu-am/, /lap-dat-cam-bien-luu-luong/, /do-luu-luong-nuoc-thai/, /loi-cam-bien-luu-luong/, /cach-chon-cam-bien-luu-luong/, /lien-he/. -->
