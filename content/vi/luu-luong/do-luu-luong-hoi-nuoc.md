<!--
LOẠI TRANG : Bài ứng dụng — chuỗi cảm biến lưu lượng — tầng 4
URL SLUG   : /do-luu-luong-hoi-nuoc/
TỪ KHÓA    : đo lưu lượng hơi nước | đồng hồ hơi | bù áp suất nhiệt độ | hơi bão hòa quá nhiệt | tính chi phí hơi
INTENT     : Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 19/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Đo Lưu Lượng Hơi Nước – Bù Áp Suất, Nhiệt Độ Và Chọn Thiết Bị
META (156)  : Đo hơi bão hòa và hơi quá nhiệt: vì sao bắt buộc bù áp suất và nhiệt độ, chọn vortex hay orifice, xử lý nước ngưng và cách tính chi phí hơi theo bộ phận.

H1          : Đo Lưu Lượng Hơi Nước

---

## Môi chất mà một con số không đủ để mô tả

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-flow-hoi.svg)


Đo hơi nước khác mọi môi chất khác ở một điểm căn bản: **thể tích của hơi không nói lên bao nhiêu năng lượng bạn đang dùng**.

Cùng một mét khối hơi, ở áp suất cao chứa nhiều khối lượng và nhiều năng lượng hơn hẳn so với ở áp suất thấp. Và khối lượng riêng của hơi **thay đổi rất mạnh theo áp suất và nhiệt độ** — mạnh hơn nhiều so với khí thông thường.

Hệ quả thực tế: nếu ai đó nói "đường ống này đang chạy 500 m³/h hơi", câu nói đó **gần như vô nghĩa** nếu không kèm áp suất và nhiệt độ.

Vì vậy với hơi, đơn vị được dùng luôn là **kg/h hoặc t/h** — khối lượng, không phải thể tích. Và để có được con số đó, hệ đo hơi **luôn phức tạp hơn** hệ đo nước hay khí thông thường.

Bài này trình bày cách xây dựng một hệ đo hơi đúng: chọn công nghệ, bố trí phép bù, xử lý nước ngưng, và dùng số liệu để phân bổ chi phí.

> **Cần đo hơi cho lò hoặc phân bổ chi phí theo phân xưởng?** Gửi **áp suất · nhiệt độ · dải lưu lượng · đường kính ống** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vortex.svg)


Đây là bài **19/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: vì sao bắt buộc phải bù

### Hơi bão hòa và hơi quá nhiệt

Trước hết cần phân biệt hai loại hơi, vì cách xử lý khác nhau:

**Hơi bão hòa (saturated steam).** Hơi ở đúng nhiệt độ sôi ứng với áp suất của nó. Với hơi bão hòa, **áp suất và nhiệt độ có quan hệ xác định** — biết một cái là suy ra cái kia.

Điều này có ý nghĩa thực tế lớn: với hơi bão hòa, **chỉ cần đo áp suất là đủ** để xác định khối lượng riêng. Không cần đo nhiệt độ.

**Hơi quá nhiệt (superheated steam).** Hơi được gia nhiệt thêm sau khi đã bay hơi hoàn toàn, nên nhiệt độ **cao hơn** nhiệt độ bão hòa ứng với áp suất đó.

Với hơi quá nhiệt, áp suất và nhiệt độ **độc lập với nhau** — nên phải **đo cả hai** mới xác định được khối lượng riêng.

| Loại hơi | Cần đo gì để bù |
|---|---|
| **Hơi bão hòa** | **Áp suất** (nhiệt độ suy ra được) |
| **Hơi quá nhiệt** | **Cả áp suất và nhiệt độ** |

**Lưu ý thực tế:** nhiều hệ được thiết kế cho hơi bão hòa nhưng thực tế hơi có thể bị quá nhiệt nhẹ ở một số chế độ vận hành, hoặc ngược lại bị ẩm. Nếu muốn an toàn, **đo cả hai** — chi phí thêm không lớn so với rủi ro sai số.

### Chuỗi phép đo và sai số cộng dồn

Với công nghệ đo thể tích (vortex, orifice), quá trình để ra kg/h gồm:

1. **Đo lưu lượng thể tích** → sai số của thiết bị lưu lượng.
2. **Đo áp suất** → sai số của cảm biến áp suất.
3. **Đo nhiệt độ** (với hơi quá nhiệt) → sai số của cảm biến nhiệt độ.
4. **Tra bảng hơi** để ra khối lượng riêng.
5. **Nhân với nhau** để ra lưu lượng khối.

Mỗi bước là một nguồn sai số, và chúng **cộng dồn vào kết quả cuối cùng** ([xem bài sai số](/sai-so-do-luu-luong/)).

Đây là lý do một hệ đo hơi cần được thiết kế cẩn thận hơn — sai số không chỉ đến từ đồng hồ lưu lượng.

### Ba cách thực hiện phép bù

**Cách 1 — Thiết bị đa biến (multivariable).** Vortex có tích hợp sẵn cảm biến áp suất và nhiệt độ, **tự tính ra kg/h**.

- **Ưu:** một thiết bị, một điểm đấu nối, ba phép đo tại cùng một điểm, không cần bộ tính toán riêng.
- **Đây là phương án gọn nhất và thường kinh tế nhất** cho hệ mới.

**Cách 2 — Bộ tính toán lưu lượng (flow computer) riêng.** Ba thiết bị riêng (lưu lượng, áp suất, nhiệt độ) đưa tín hiệu về một bộ tính toán chuyên dụng có sẵn bảng hơi.

- **Ưu:** linh hoạt, dùng được với thiết bị của nhiều hãng, phù hợp khi nâng cấp hệ cũ đã có sẵn cảm biến.
- **Nhược:** nhiều điểm đấu nối, ba thiết bị đo ở ba vị trí khác nhau.

**Cách 3 — Tính trong PLC hoặc SCADA.** Đưa ba tín hiệu về PLC và lập trình phép tính.

- **Ưu:** không tốn thiết bị thêm nếu đã có PLC.
- **Nhược:** cần lập trình bảng hơi hoặc công thức xấp xỉ; **dễ sai và khó kiểm chứng**. Nếu chọn cách này, phải kiểm tra kỹ kết quả tại vài điểm vận hành khác nhau.

**Khuyến nghị:** với hệ mới, **vortex đa biến** thường là lựa chọn tốt nhất về tổng chi phí và độ tin cậy ([xem bài vortex](/luu-luong-ke-vortex/)).

---

## Cấu tạo: chọn công nghệ cho hơi

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-saiso.svg)


Danh sách lựa chọn cho hơi ngắn hơn nhiều so với chất lỏng:

| Công nghệ | Dùng được? | Ghi chú |
|---|---|---|
| **Vortex** | **Có — lựa chọn số một** | Chịu nhiệt cao, dải đo khá rộng, có loại đa biến |
| **Orifice** | **Có** | Rẻ, chuẩn hóa, nhưng dải đo hẹp và tổn thất áp cao |
| **Coriolis** | Có | Ra kg/h trực tiếp, chính xác nhất, nhưng đắt và tổn thất áp |
| **Pitot trung bình** | Có | Tổn thất áp thấp, phù hợp ống lớn |
| **Điện từ** | **Không** | Hơi không dẫn điện |
| **Tuabin** | **Không** | Không chịu được nhiệt độ và điều kiện hơi |
| **Siêu âm** | Hạn chế | Khó với hơi |
| **Nhiệt (thermal)** | Hạn chế | Chủ yếu cho khí, không phải hơi |

### Vortex so với orifice — lựa chọn thực tế nhất

Đây là quyết định phải đưa ra trong đa số dự án:

| Tiêu chí | **Vortex** | **Orifice** |
|---|---|---|
| Dải đo (turndown) | **Rộng hơn nhiều** | **Hẹp** |
| Tổn thất áp | Trung bình | **Cao** |
| Tích hợp bù P, T | **Có (loại đa biến)** | Không — cần thiết bị riêng |
| Chi phí thiết bị | Cao hơn | **Thấp hơn** |
| Chi phí hệ hoàn chỉnh | **Thường thấp hơn** (đa biến) | Cộng thêm cảm biến P, T, flow computer |
| Ống xung | **Không cần** | **Cần — nguồn sự cố chính** |
| Bảo trì | Rất ít | Vệ sinh ống xung, thay tấm |
| Nhạy với rung động | **Có** | Không |
| Phù hợp ống rất lớn | Khó | **Tốt** |

**Cách chọn:**

- **Lưu lượng biến động theo ca, theo mùa** → **vortex** (dải đo rộng hơn hẳn).
- **Lưu lượng ổn định, ngân sách hạn chế, hệ đã chuẩn hóa orifice** → orifice.
- **Cần kg/h mà không muốn lắp nhiều thiết bị** → **vortex đa biến**.
- **Ống rất lớn** → orifice hoặc pitot trung bình.
- **Cần chính xác cao nhất** → Coriolis.

**Về ống xung của hệ orifice — điểm yếu thực tế lớn nhất.** Với hơi, hai ống xung cần **bình ngưng (condensate pot)** ở cả hai phía để tạo và duy trì cột nước ngưng cân bằng. Nếu hai bình không cân nhau — một bên có nước, một bên cạn — **sai số rất lớn**.

Đây là nguồn sự cố phổ biến nhất của hệ đo hơi bằng orifice, và nó đòi hỏi bảo trì thường xuyên ([xem bài orifice](/luu-luong-ke-chenh-ap-orifice/)).

---

## Ứng dụng: xử lý nước ngưng và lắp đặt

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-hoi.svg)


### Nước ngưng — vấn đề đặc thù của hơi

Hơi nước luôn có xu hướng **ngưng tụ** khi mất nhiệt qua thành ống. Nước ngưng trong đường ống gây ba vấn đề:

1. **Dòng hai pha** — tín hiệu đo thất thường với mọi công nghệ.
2. **Búa nước (water hammer)** — nước ngưng bị hơi đẩy đi với tốc độ cao, va đập vào co và van, có thể **làm hỏng cả thiết bị đo lẫn đường ống**.
3. **Sai số** — thiết bị đo cả phần nước lẫn phần hơi.

**Biện pháp xử lý:**

- **Bẫy hơi (steam trap) hoạt động tốt** phía trước điểm đo — quan trọng nhất.
- **Bọc cách nhiệt đường ống** để giảm ngưng tụ.
- **Bố trí điểm thoát nước ngưng** ở các điểm thấp.
- **Kiểm tra bẫy hơi định kỳ** — bẫy hỏng ở trạng thái mở thì xả hơi lãng phí; hỏng ở trạng thái đóng thì nước ngưng tích tụ.

**Một lưu ý về vị trí:** với hơi bão hòa, nên lắp thiết bị ở **đoạn ống nằm ngang** và đảm bảo nước ngưng có đường thoát, thay vì ở đoạn ống đi xuống nơi nước ngưng chảy dồn.

### Bảo vệ thiết bị khỏi nhiệt độ

Phần điện tử của thiết bị đo có giới hạn nhiệt độ **thấp hơn nhiều** so với nhiệt độ hơi.

Với hơi ở nhiệt độ cao, cần dùng loại có **bộ chuyển đổi lắp rời (remote)** — phần cảm biến trên đường ống, phần điện tử đặt cách xa ở nơi mát hơn.

Với cảm biến áp suất dùng để bù, cần **ống xi-phông (siphon)** — một đoạn ống uốn cong giữ một ít nước ngưng, ngăn hơi nóng tiếp xúc trực tiếp với màng cảm biến.

### Vị trí đặt cảm biến bù

Để phép bù đúng, các cảm biến áp suất và nhiệt độ nên đặt **gần điểm đo lưu lượng** — vì áp suất và nhiệt độ thay đổi dọc đường ống.

Đặt cảm biến áp suất ở đầu đường ống rồi dùng để bù cho đồng hồ ở cuối đường ống là một nguồn sai số không cần thiết. Đây là một lý do nữa khiến **vortex đa biến** hấp dẫn — cả ba phép đo tại đúng một điểm.

### Tính chi phí hơi theo bộ phận

Đây là ứng dụng thương mại phổ biến nhất của đo hơi trong nhà máy.

**Cách triển khai:**

1. **Đo tổng lượng hơi sản xuất** tại đầu ra lò hơi.
2. **Đo lượng hơi cấp cho từng phân xưởng** ở các nhánh chính.
3. **So sánh tổng các nhánh với tổng sản xuất** — chênh lệch là tổn thất trên đường ống và rò rỉ.
4. **Quy ra chi phí** dựa trên chi phí nhiên liệu và hiệu suất lò.
5. **Phân bổ cho từng bộ phận.**

**Giá trị của bước 3 đáng được nhấn mạnh.** Chênh lệch giữa tổng sản xuất và tổng tiêu thụ cho biết **tổn thất trên hệ phân phối hơi** — bao gồm mất nhiệt qua đường ống không cách nhiệt, bẫy hơi hỏng đang xả hơi ra ngoài, và rò rỉ tại các mối nối.

Với hệ hơi lớn, khoản tổn thất này thường đáng kể và **hoàn toàn khắc phục được** bằng cách bọc cách nhiệt và sửa bẫy hơi — những việc rẻ hơn nhiều so với đầu tư thiết bị mới.

**Về nước ngưng hồi lưu:** một hệ hơi hoàn chỉnh nên thu hồi nước ngưng về lò. Đo lưu lượng nước ngưng hồi (bằng đồng hồ điện từ, vì đây là nước) cho biết **tỷ lệ thu hồi** — chỉ số quan trọng vì nước ngưng đã nóng sẵn, thu hồi được là tiết kiệm cả nước lẫn nhiên liệu.

---

## So sánh: thiết kế hệ đo hơi

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-tichkhoi.svg)


| Cấu hình | Thành phần | Phù hợp với |
|---|---|---|
| **Vortex đa biến** | Một thiết bị | **Hệ mới, gọn, dễ bảo trì** |
| **Vortex + P + T + flow computer** | Bốn thiết bị | Khi cần linh hoạt hoặc đã có sẵn cảm biến |
| **Orifice + DP + P + T + flow computer** | Năm thiết bị | Ống rất lớn, ngân sách thiết bị hạn chế |
| **Coriolis** | Một thiết bị | Chính xác cao nhất, ống vừa và nhỏ |
| **Pitot trung bình + DP + P + T** | Bốn thiết bị | Ống rất lớn, tổn thất áp là vấn đề |

**Về tổng chi phí:** đừng chỉ so giá thiết bị lưu lượng. Một hệ orifice hoàn chỉnh cần thêm cảm biến chênh áp, cảm biến áp suất, cảm biến nhiệt độ, bộ tính toán, ống xung, bình ngưng, cụm van manifold — và công lắp đặt cho tất cả.

Khi cộng đủ, **vortex đa biến thường không đắt hơn**, mà lại ít điểm hỏng và ít bảo trì hơn nhiều ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

---

## Sai lầm thường gặp

1. **Đo hơi mà không bù áp suất** — con số thể tích không nói lên gì.
2. **Bù bằng một giá trị áp suất cố định** thay vì đo thực tế — áp suất trong hệ luôn biến động.
3. **Chỉ đo áp suất cho hơi quá nhiệt** — cần cả nhiệt độ vì hai đại lượng độc lập.
4. **Đặt cảm biến bù xa điểm đo lưu lượng** — áp suất và nhiệt độ thay đổi dọc đường ống.
5. **Bỏ qua bẫy hơi** — nước ngưng làm tín hiệu thất thường và gây búa nước.
6. **Không bọc cách nhiệt đường ống** — tăng ngưng tụ và tổn thất nhiệt.
7. **Hai bình ngưng không cân nhau** trong hệ orifice — sai số rất lớn.
8. **Dùng loại gắn liền cho hơi nhiệt độ rất cao** — nên dùng loại lắp rời.
9. **Không có ống xi-phông** cho cảm biến áp suất — hỏng màng.
10. **Chọn cỡ vortex quá lớn** — vận tốc dưới ngưỡng, thiết bị đọc 0.
11. **Lắp vortex cạnh thiết bị rung** — đọc sai khi không có dòng.
12. **Chỉ so giá thiết bị lưu lượng** mà không tính toàn bộ hệ orifice.
13. **Không đo tổng sản xuất để đối chiếu với tổng tiêu thụ** — bỏ lỡ thông tin về tổn thất.
14. **Lập trình bảng hơi trong PLC mà không kiểm chứng** ở nhiều điểm vận hành.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **cấu hình bù phù hợp** theo loại hơi — bão hòa cần gì, quá nhiệt cần gì.
- ✅ **So sánh tổng chi phí hệ hoàn chỉnh** giữa vortex đa biến và orifice, không chỉ giá thiết bị lưu lượng.
- ✅ Tính chọn cỡ vortex theo vận tốc để đảm bảo **không rơi dưới ngưỡng ở mọi chế độ vận hành**.
- ✅ Cung cấp đồng bộ thiết bị lưu lượng, [cảm biến áp suất](/cam-bien-ap-suat-la-gi-cach-chon/), [cảm biến nhiệt độ](/cam-bien-nhiet-do/) và phụ kiện cho hệ hơi.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá hệ đo hơi

Gửi cho chúng tôi: **hơi bão hòa hay quá nhiệt · áp suất và nhiệt độ làm việc · dải lưu lượng **nhỏ nhất** và lớn nhất · đường kính ống · mục đích đo (giám sát, phân bổ chi phí, kiểm soát lò) · đã có cảm biến áp suất, nhiệt độ chưa · sơ đồ đoạn ống thẳng khả dụng.**

**→ [Liên hệ nhận tư vấn đo hơi](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Vì sao đo hơi phải bù áp suất và nhiệt độ?**
Vì **khối lượng riêng của hơi thay đổi rất mạnh** theo áp suất và nhiệt độ. Cùng một thể tích hơi ở hai áp suất khác nhau chứa lượng khối và lượng năng lượng rất khác nhau.

**Hơi bão hòa cần đo gì để bù?**
Chỉ cần **đo áp suất** — vì với hơi bão hòa, áp suất và nhiệt độ có **quan hệ xác định**, biết một cái là suy ra cái kia.

**Hơi quá nhiệt cần đo gì?**
**Cả áp suất và nhiệt độ**, vì với hơi quá nhiệt hai đại lượng này **độc lập với nhau**.

**Nên chọn vortex hay orifice cho hơi?**
**Vortex** khi lưu lượng biến động (dải đo rộng hơn hẳn) hoặc khi muốn tích hợp bù trong một thiết bị. **Orifice** khi lưu lượng ổn định, ống rất lớn và ngân sách hạn chế.

**Vortex đa biến là gì và có lợi gì?**
Là loại **tích hợp sẵn cảm biến áp suất và nhiệt độ**, tự tính ra kg/h. Lợi ích: một điểm đấu nối, ba phép đo tại cùng một vị trí, không cần bộ tính toán riêng, ít điểm hỏng hơn.

**Nước ngưng ảnh hưởng thế nào?**
Gây **dòng hai pha** làm tín hiệu thất thường, gây **búa nước** có thể hỏng thiết bị, và làm sai số. Cần **bẫy hơi hoạt động tốt** và **bọc cách nhiệt đường ống**.

**Có thể tính bù trong PLC thay vì dùng flow computer không?**
Được, nhưng cần lập trình bảng hơi hoặc công thức xấp xỉ, và **dễ sai, khó kiểm chứng**. Nếu chọn cách này, phải kiểm tra kết quả ở nhiều điểm vận hành khác nhau.

**Đo hơi để phân bổ chi phí làm thế nào?**
**Đo tổng sản xuất tại lò** và **đo từng nhánh cấp cho các phân xưởng**. Chênh lệch giữa hai tổng cho biết **tổn thất trên hệ phân phối** — thường đáng kể và khắc phục được bằng cách nhiệt và sửa bẫy hơi.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /don-vi-luu-luong-quy-doi/, /luu-luong-ke-vortex/, /luu-luong-ke-chenh-ap-orifice/, /luu-luong-ke-coriolis/, /sai-so-do-luu-luong/, /cach-chon-cam-bien-luu-luong/, /cam-bien-ap-suat-la-gi-cach-chon/, /cam-bien-nhiet-do/, /lien-he/. -->
