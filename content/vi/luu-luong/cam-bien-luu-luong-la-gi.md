<!--
LOẠI TRANG : Bài trụ (pillar) — chuỗi cảm biến lưu lượng — tầng 1
URL SLUG   : /cam-bien-luu-luong-la-gi/
TỪ KHÓA    : cảm biến lưu lượng | flow sensor | đồng hồ đo lưu lượng | lưu lượng kế | thiết bị đo lưu lượng
INTENT     : Thông tin + Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 1/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Cảm Biến Lưu Lượng Là Gì? Nguyên Lý, Phân Loại Và Cách Chọn
META (156)  : Cảm biến lưu lượng là gì, có mấy loại, đo thể tích hay khối lượng, chọn công nghệ nào cho nước, khí và hơi. Hướng dẫn đầy đủ kèm bảng so sánh thực tế.

H1          : Cảm Biến Lưu Lượng Là Gì?

---

## Đại lượng khó đo nhất trong bốn đại lượng cơ bản

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-cam-bien-luu-luong.svg)


Trong đo lường công nghiệp có bốn đại lượng nền tảng: **áp suất, nhiệt độ, mức và lưu lượng**. Ba đại lượng đầu tương đối dễ — bạn đặt một cảm biến vào đúng chỗ và đọc giá trị.

**Lưu lượng là đại lượng khó nhất**, vì một lý do căn bản: nó **không phải là một đại lượng tại một điểm**. Lưu lượng là lượng chất đi qua **một mặt cắt ngang** trong một đơn vị thời gian — và để biết nó, bạn phải biết cả **vận tốc dòng chảy trên toàn bộ tiết diện ống**.

Vấn đề là vận tốc **không đều trên tiết diện**: ở giữa ống nhanh, sát thành ống chậm. Biên dạng đó lại thay đổi theo lưu lượng, theo độ nhớt, theo việc phía trước có co, có van hay có bơm không.

Đây là lý do một cảm biến lưu lượng lắp sai vị trí có thể cho sai số rất lớn, trong khi bản thân thiết bị vẫn hoàn toàn tốt. Và cũng là lý do bài này — cùng cả chuỗi 20 bài — dành nhiều dung lượng cho **lắp đặt và điều kiện đo**, không chỉ cho thiết bị.

> **Cần chọn cảm biến lưu lượng cho hệ của bạn?** Gửi **môi chất · đường kính ống · dải lưu lượng** → [Nhận tư vấn chọn thiết bị](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-flow-profile.svg)


Đây là bài **1/20** — bài mở đầu chuỗi cảm biến lưu lượng.

---

## Nguyên lý: cảm biến lưu lượng đo cái gì

**Cảm biến lưu lượng (flow sensor / flow meter / lưu lượng kế)** là thiết bị đo lượng chất lỏng, khí hoặc hơi đi qua một đường ống trong một đơn vị thời gian, và **chuyển kết quả thành tín hiệu điện** để đưa về PLC, biến tần, bộ hiển thị hoặc hệ SCADA.

Cần phân biệt hai đại lượng mà người ta hay gọi chung là "lưu lượng":

**1. Lưu lượng thể tích (volumetric flow).** Bao nhiêu **mét khối, lít** chất đi qua trong một giờ hoặc một phút. Đơn vị: m³/h, l/min, l/s.

**2. Lưu lượng khối (mass flow).** Bao nhiêu **kilôgam** chất đi qua trong một đơn vị thời gian. Đơn vị: kg/h, t/h.

Với **nước ở nhiệt độ ổn định**, hai đại lượng này gần như quy đổi được cho nhau vì khối lượng riêng gần như không đổi. Nhưng với **khí và hơi**, chúng khác nhau rất xa: cùng một thể tích khí ở áp suất cao chứa nhiều khối lượng hơn nhiều so với ở áp suất thấp.

Đây là nguồn sai sót lớn và tốn kém nhất trong đo lưu lượng công nghiệp, nên nó có một bài riêng trong chuỗi này ([xem bài đơn vị và quy đổi](/don-vi-luu-luong-quy-doi/)).

### Ba cách tiếp cận bài toán đo

Các công nghệ đo lưu lượng, dù khác nhau thế nào, đều thuộc một trong ba nhóm:

**Nhóm 1 — Đo vận tốc rồi nhân với tiết diện.** Đo vận tốc trung bình của dòng chảy, biết đường kính ống thì tính ra lưu lượng thể tích. Thuộc nhóm này: **điện từ, siêu âm, vortex, tuabin**.

**Nhóm 2 — Đo chênh áp.** Đặt một vật cản làm dòng thu hẹp, đo chênh lệch áp suất trước và sau, rồi suy ra lưu lượng. Thuộc nhóm này: **tấm orifice, ống venturi, ống pitot**.

**Nhóm 3 — Đo trực tiếp khối lượng.** Không đi qua vận tốc, đo thẳng ra khối lượng. Thuộc nhóm này: **Coriolis** và **cảm biến nhiệt cho khí**.

Nhóm 1 và 2 cho ra **lưu lượng thể tích**; muốn có khối lượng phải bù áp suất và nhiệt độ. Nhóm 3 cho ra **khối lượng trực tiếp**, không cần bù — đây là ưu thế lớn của chúng trong ứng dụng khí, hơi và hóa chất ([xem chi tiết nguyên lý](/nguyen-ly-do-luu-luong/)).

---

## Cấu tạo và thông số: đọc nhãn cảm biến lưu lượng

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-donvi.svg)


Một cảm biến lưu lượng công nghiệp thường gồm hai phần:

- **Phần cảm biến (sensor / primary device)** — phần tiếp xúc hoặc tương tác với dòng chảy, lắp vào đường ống.
- **Bộ chuyển đổi (transmitter / converter)** — xử lý tín hiệu, hiển thị và xuất ra tín hiệu chuẩn. Có thể gắn liền cảm biến (compact) hoặc lắp rời (remote).

Các thông số cần đọc khi chọn mua:

| Thông số | Ý nghĩa | Lưu ý khi chọn |
|---|---|---|
| **Đường kính danh nghĩa (DN)** | Cỡ ống lắp vào | Chọn theo **vận tốc mong muốn**, không phải theo ống sẵn có |
| **Dải lưu lượng** | Nhỏ nhất – lớn nhất đo được | Lưu lượng thường ngày nên nằm **giữa dải** |
| **Tỷ số dải đo (turndown)** | Đo được rộng bao nhiêu | Quan trọng khi lưu lượng biến động mạnh |
| **Độ chính xác** | ±% giá trị đọc hoặc ±% dải đo | Hai cách ghi này **rất khác nhau** |
| **Áp suất làm việc** | PN / class | Phải cao hơn áp thực tế |
| **Nhiệt độ môi chất** | Dải cho phép | Hơi nóng cần loại chuyên dụng |
| **Vật liệu tiếp xúc** | Thép không gỉ, PTFE, cao su… | Theo tính ăn mòn của môi chất |
| **Kiểu kết nối** | Mặt bích, ren, clamp, wafer | Khớp đường ống sẵn có |
| **Cấp bảo vệ IP** | Chống bụi, nước | Ngoài trời cần cấp cao |
| **Tín hiệu ra** | 4–20mA, xung, Modbus, HART | Khớp hệ điều khiển ([xem đấu dây](/dau-day-cam-bien-luu-luong/)) |
| **Nguồn cấp** | 24VDC, 220VAC, hoặc loop-powered | Ảnh hưởng thiết kế tủ |
| **Yêu cầu đoạn ống thẳng** | Số lần đường kính trước/sau | **Rất quan trọng**, hay bị bỏ qua |

### Ba chi tiết hay bị hiểu sai

**1. "±0,5%" nghĩa là gì?** Có hai cách ghi hoàn toàn khác nhau:
- **±% giá trị đọc (of reading)** — sai số tỷ lệ với giá trị đang đo. Ở lưu lượng thấp vẫn giữ được độ chính xác tương đối.
- **±% dải đo (of full scale)** — sai số tính theo giá trị lớn nhất. Ở lưu lượng thấp, sai số tương đối **lớn hơn rất nhiều**.

Hai thiết bị cùng ghi "±0,5%" có thể chênh nhau rất xa trong thực tế ([xem bài về sai số](/sai-so-do-luu-luong/)).

**2. Chọn cỡ cảm biến theo cỡ ống là sai.** Thói quen phổ biến: ống DN100 thì mua cảm biến DN100. Nhưng nếu lưu lượng thực tế nhỏ, vận tốc trong ống sẽ quá thấp và cảm biến làm việc ở đáy dải đo — nơi sai số lớn nhất. Trong trường hợp đó, **thu nhỏ cỡ cảm biến** (kèm côn thu) cho kết quả tốt hơn nhiều.

**3. Đoạn ống thẳng không phải khuyến nghị mà là điều kiện.** Hầu hết cảm biến đo vận tốc đều yêu cầu một đoạn ống thẳng nhất định trước và sau vị trí lắp. Thiếu đoạn này, dòng chảy chưa ổn định biên dạng và kết quả sai — **dù thiết bị hoàn toàn tốt** ([xem bài lắp đặt](/lap-dat-cam-bien-luu-luong/)).

---

## Ứng dụng: lưu lượng dùng để làm gì

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-nuoc.svg)


Đo lưu lượng phục vụ bốn nhóm mục đích, và mục đích quyết định mức chính xác cần có:

**1. Giám sát vận hành.** Biết máy đang chạy đúng chế độ không, bơm có đủ nước không, lọc có tắc không. Yêu cầu chính xác vừa phải; quan trọng là **ổn định và tin cậy**.

**2. Điều khiển tự động.** Lưu lượng làm phản hồi cho vòng điều khiển — ví dụ giữ lưu lượng không đổi bằng biến tần điều tốc bơm ([xem điều khiển PID bằng biến tần](/dieu-khien-pid-bang-bien-tan/)). Yêu cầu **đáp ứng nhanh và ổn định**, không cần chính xác tuyệt đối.

**3. Cân bằng vật chất và tính chi phí.** Biết mỗi bộ phận dùng bao nhiêu nước, hơi, khí nén để phân bổ chi phí hoặc kiểm toán năng lượng. Yêu cầu **chính xác cao và đo được tổng tích lũy**.

**4. Mua bán, giao nhận.** Đo để thanh toán. Yêu cầu **chính xác cao nhất, có hiệu chuẩn và giấy chứng nhận** ([xem bài hiệu chuẩn](/hieu-chuan-cam-bien-luu-luong/)).

### Ứng dụng theo ngành

- **Cấp thoát nước:** đo lưu lượng nước sạch, nước thải, bùn ([xem bài nước thải](/do-luu-luong-nuoc-thai/)).
- **Nhà máy sản xuất:** đo khí nén để phát hiện rò rỉ và phân bổ chi phí ([xem bài khí nén](/do-luu-luong-khi-nen/)).
- **Nhiệt điện, lò hơi:** đo hơi, nước cấp ([xem bài hơi nước](/do-luu-luong-hoi-nuoc/)).
- **Hóa chất:** định lượng hóa chất theo mẻ, cần chính xác cao.
- **Thực phẩm, đồ uống:** yêu cầu vệ sinh, vật liệu tiếp xúc đạt chuẩn.
- **HVAC:** đo lưu lượng nước lạnh, tính năng lượng lạnh tiêu thụ ([xem bài HVAC](/bien-tan-trong-hvac/)).
- **Tưới tiêu, nông nghiệp:** đo nước tưới, thường ưu tiên bền và rẻ.

---

## So sánh nhanh các công nghệ đo

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-congnghe.svg)


Bảng dưới là bản tóm tắt; mỗi công nghệ có một bài riêng trong chuỗi:

| Công nghệ | Đo được gì | Ưu điểm chính | Hạn chế chính |
|---|---|---|---|
| **[Điện từ (MAG)](/dong-ho-luu-luong-dien-tu/)** | Chất lỏng **dẫn điện** | Không cản dòng, chính xác cao, chịu cặn bẩn | **Không đo được dầu, nước tinh khiết, khí** |
| **[Siêu âm](/cam-bien-luu-luong-sieu-am/)** | Lỏng, một số loại khí | **Kẹp ngoài được**, không cắt ống | Nhạy với bọt khí và cặn |
| **[Coriolis](/luu-luong-ke-coriolis/)** | Lỏng, khí, hơi | Đo **khối lượng thật**, chính xác nhất | Đắt nhất, nặng, tổn thất áp |
| **[Tuabin](/luu-luong-ke-tuabin/)** | Lỏng sạch, khí sạch | Chính xác tốt, giá hợp lý | Có bộ phận quay, sợ cặn bẩn |
| **[Vortex](/luu-luong-ke-vortex/)** | Lỏng, khí, **hơi** | Chịu nhiệt cao, không bộ phận quay | Không đo được lưu lượng rất thấp |
| **[Chênh áp / orifice](/luu-luong-ke-chenh-ap-orifice/)** | Lỏng, khí, hơi | Rẻ, đã chuẩn hóa, sửa được tại chỗ | Dải đo hẹp, tổn thất áp lớn |
| **[Nhiệt (thermal)](/cam-bien-luu-luong-khi-nhiet/)** | **Khí** | Ra khối lượng trực tiếp, đo được lưu lượng rất thấp | Phụ thuộc thành phần khí |

### Quy tắc chọn nhanh theo môi chất

- **Nước, nước thải, hóa chất dẫn điện** → **điện từ**, gần như luôn là lựa chọn đúng.
- **Dầu, nhiên liệu, chất lỏng không dẫn điện** → **Coriolis, tuabin, hoặc siêu âm**.
- **Cần đo mà không được dừng sản xuất** → **siêu âm kẹp ngoài**.
- **Khí nén** → **nhiệt (thermal mass)**.
- **Hơi nước** → **vortex** kèm bù áp suất và nhiệt độ.
- **Cần chính xác cao nhất, đo khối lượng** → **Coriolis**.
- **Ngân sách hạn chế, hệ đã có sẵn chuẩn** → **chênh áp / orifice**.

Chi tiết cách chọn theo tám tiêu chí xem tại bài [cách chọn cảm biến lưu lượng](/cach-chon-cam-bien-luu-luong/).

---

## Sai lầm thường gặp

1. **Chọn cỡ cảm biến bằng cỡ ống** mà không kiểm tra vận tốc thực tế.
2. **Bỏ qua yêu cầu đoạn ống thẳng** — sai số lớn dù thiết bị tốt.
3. **Nhầm lưu lượng thể tích với lưu lượng khối** khi đo khí và hơi.
4. **So sánh "±0,5%" giữa hai thiết bị** mà không xem là % giá trị đọc hay % dải đo.
5. **Dùng đồng hồ điện từ cho chất lỏng không dẫn điện** — không hoạt động.
6. **Lắp ở vị trí ống không đầy** — kết quả vô nghĩa với hầu hết công nghệ.
7. **Không tính tổn thất áp suất** mà thiết bị gây ra cho hệ thống.
8. **Chọn theo giá rẻ nhất** cho ứng dụng cần chính xác để tính chi phí.
9. **Không có van và đoạn ống để tháo cảm biến** khi cần bảo trì.
10. **Bỏ qua bọt khí trong đường ống** — nguyên nhân số một của số liệu nhảy loạn.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **chọn công nghệ theo môi chất và mục đích đo thật**, không mặc định một loại.
- ✅ **Tính chọn cỡ cảm biến theo vận tốc dòng**, không chỉ theo cỡ ống sẵn có.
- ✅ Cảnh báo rõ **yêu cầu đoạn ống thẳng và điều kiện lắp đặt** trước khi báo giá.
- ✅ Cung cấp đồng bộ cảm biến lưu lượng, [cảm biến áp suất](/cam-bien-ap-suat-la-gi-cach-chon/), [cảm biến nhiệt độ](/cam-bien-nhiet-do/) và thiết bị hiển thị.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **môi chất cần đo (nước, nước thải, dầu, khí, hơi…) · đường kính và vật liệu ống · dải lưu lượng nhỏ nhất và lớn nhất · áp suất và nhiệt độ làm việc · mục đích đo (giám sát, điều khiển, tính chi phí, mua bán) · tín hiệu ra cần dùng · ảnh vị trí dự kiến lắp.**

**→ [Liên hệ nhận tư vấn cảm biến lưu lượng](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến lưu lượng là gì?**
Là thiết bị đo **lượng chất lỏng, khí hoặc hơi đi qua đường ống trong một đơn vị thời gian**, và chuyển kết quả thành tín hiệu điện để đưa về PLC, bộ hiển thị hoặc hệ giám sát.

**Lưu lượng thể tích và lưu lượng khối khác nhau thế nào?**
**Thể tích** đo bao nhiêu m³ hay lít đi qua; **khối lượng** đo bao nhiêu kg. Với nước thì gần như quy đổi được, nhưng với **khí và hơi thì khác nhau rất xa** vì khối lượng riêng thay đổi theo áp suất và nhiệt độ.

**Có mấy loại cảm biến lưu lượng?**
Phổ biến nhất là **điện từ, siêu âm, Coriolis, tuabin, vortex, chênh áp (orifice)** và **cảm biến nhiệt cho khí**. Mỗi loại phù hợp một nhóm môi chất và mục đích khác nhau.

**Đo nước nên chọn loại nào?**
**Đồng hồ điện từ (MAG)** gần như luôn là lựa chọn đúng cho nước và nước thải — không cản dòng, chịu được cặn bẩn và chính xác cao. Điều kiện duy nhất là chất lỏng phải **dẫn điện**.

**Đo được lưu lượng mà không cần cắt ống không?**
Được, bằng **cảm biến siêu âm kẹp ngoài**. Không phải dừng sản xuất, có thể tháo ra dùng cho ống khác, nhưng độ chính xác thường thấp hơn loại lắp trong ống.

**Vì sao cần đoạn ống thẳng trước cảm biến?**
Vì co, van, bơm làm **biên dạng dòng chảy bị méo**. Cảm biến đo vận tốc cần dòng ổn định mới cho kết quả đúng — thiếu đoạn thẳng là sai số lớn dù thiết bị hoàn toàn tốt.

**"Độ chính xác ±0,5%" nghĩa là gì?**
Phải xem là **±% giá trị đọc** hay **±% dải đo**. Loại thứ hai có sai số tương đối **lớn hơn nhiều ở lưu lượng thấp**, nên hai thiết bị cùng ghi ±0,5% có thể rất khác nhau trong thực tế.

**Chọn cỡ cảm biến theo cỡ ống có đúng không?**
**Không hẳn.** Phải chọn theo **vận tốc dòng mong muốn**. Nếu lưu lượng nhỏ so với ống, nên thu nhỏ cỡ cảm biến kèm côn thu để thiết bị làm việc ở giữa dải đo.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /nguyen-ly-do-luu-luong/, /don-vi-luu-luong-quy-doi/, /cach-chon-cam-bien-luu-luong/, /dong-ho-luu-luong-dien-tu/, /cam-bien-luu-luong-sieu-am/, /luu-luong-ke-coriolis/, /luu-luong-ke-tuabin/, /luu-luong-ke-vortex/, /luu-luong-ke-chenh-ap-orifice/, /cam-bien-luu-luong-khi-nhiet/, /lap-dat-cam-bien-luu-luong/, /dau-day-cam-bien-luu-luong/, /hieu-chuan-cam-bien-luu-luong/, /sai-so-do-luu-luong/, /do-luu-luong-nuoc-thai/, /do-luu-luong-khi-nen/, /do-luu-luong-hoi-nuoc/, /cam-bien-ap-suat-la-gi-cach-chon/, /lien-he/. -->
