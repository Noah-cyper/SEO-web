<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /luu-luong-ke-chenh-ap-orifice/
TỪ KHÓA    : tấm orifice | đo lưu lượng chênh áp | ống venturi | ống pitot | tỷ số beta
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 11/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Đo Lưu Lượng Bằng Chênh Áp – Tấm Orifice, Venturi Và Pitot
META (156)  : Phương pháp chênh áp đo lưu lượng: nguyên lý căn bậc hai, tỷ số beta, cách lắp ống xung, tổn thất áp và vì sao dải đo hẹp. So sánh orifice, venturi, pitot.

H1          : Đo Lưu Lượng Bằng Chênh Áp (Orifice)

---

## Công nghệ lâu đời nhất — và vẫn được dùng nhiều nhất trên thế giới

Trong một ngành thay đổi nhanh như đo lường công nghiệp, **phương pháp chênh áp** vẫn giữ vị trí đặc biệt: nó là công nghệ đo lưu lượng **lâu đời nhất, được chuẩn hóa kỹ nhất, và vẫn chiếm tỷ trọng rất lớn** trong các nhà máy hiện hữu.

Lý do không phải quán tính mà là ba ưu điểm thực chất:

**1. Được chuẩn hóa quốc tế đầy đủ.** Kích thước tấm, cách gia công, vị trí lỗ trích áp, hệ số tính toán — tất cả đều có trong các tiêu chuẩn quốc tế. Nghĩa là bạn có thể **tự chế tạo hoặc mua từ bất kỳ đâu** và biết trước nó sẽ hoạt động thế nào, không phụ thuộc một hãng nào.

**2. Chi phí không tăng nhanh theo cỡ ống.** Với ống rất lớn, một tấm thép có lỗ vẫn chỉ là một tấm thép có lỗ. Trong khi đồng hồ điện từ hay Coriolis cỡ lớn có giá rất cao.

**3. Đo được gần như mọi môi chất.** Lỏng, khí, hơi, nhiệt độ cao, áp suất cao — chỉ cần chọn vật liệu phù hợp.

Đổi lại, nó có hai nhược điểm lớn không thể khắc phục được bằng thiết bị tốt hơn: **dải đo hẹp** và **tổn thất áp suất vĩnh viễn**.

Bài này trình bày rõ cả hai mặt để bạn biết khi nào chênh áp là lựa chọn kinh tế đúng, và khi nào nó là lựa chọn tưởng rẻ mà hóa đắt.

> **Đang cân nhắc phương án orifice?** Gửi **môi chất · cỡ ống · dải lưu lượng** → [Nhận tính toán và so sánh](#bao-gia).

Đây là bài **11/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: thu hẹp dòng và định luật bảo toàn

Nguyên lý dựa trên một quy luật cơ bản của cơ học chất lỏng: khi dòng chảy đi qua một chỗ thu hẹp, **vận tốc phải tăng lên** (vì cùng một lượng chất phải đi qua tiết diện nhỏ hơn), và khi vận tốc tăng thì **áp suất giảm xuống**.

Đo chênh lệch áp suất giữa **trước** và **tại chỗ thu hẹp** thì suy ra được vận tốc, từ đó ra lưu lượng.

Hệ thống đo gồm ba phần:

1. **Phần tử sơ cấp (primary element)** — vật tạo ra chỗ thu hẹp: tấm orifice, ống venturi, hoặc vòi phun.
2. **Ống xung (impulse lines)** — hai ống nhỏ dẫn áp suất từ hai điểm trích về thiết bị đo.
3. **Cảm biến chênh áp (DP transmitter)** — đo hiệu áp suất và xuất tín hiệu ([xem bài cảm biến chênh áp](/cam-bien-chenh-ap/)).

### Quan hệ căn bậc hai — gốc rễ của mọi hạn chế

Quan hệ giữa lưu lượng và chênh áp **không tuyến tính**:

> **Lưu lượng tỷ lệ với căn bậc hai của chênh áp**

Nghĩa là để lưu lượng tăng gấp đôi, chênh áp phải tăng **gấp bốn lần**.

Đây là đặc điểm quyết định mọi ưu nhược của phương pháp này, và nó có ba hệ quả:

**Hệ quả 1 — Dải đo hẹp.** Ở lưu lượng bằng một nửa dải đo, chênh áp chỉ còn **một phần tư**. Ở một phần ba dải đo, chênh áp chỉ còn **một phần chín**. Chênh áp trở nên quá nhỏ để đo chính xác, và sai số tương đối tăng vọt.

Đây là lý do phương pháp chênh áp có **turndown hẹp nhất** trong tất cả các công nghệ — thường chỉ khoảng 3:1 với một cảm biến chênh áp thông thường.

**Hệ quả 2 — Sai số ở lưu lượng thấp bị khuếch đại.** Sai số của cảm biến chênh áp **được khuếch đại lên khi lấy căn bậc hai** ở vùng giá trị nhỏ. Một sai số nhỏ trong phép đo chênh áp trở thành sai số lớn hơn trong lưu lượng.

**Hệ quả 3 — Cần tính toán.** Thiết bị không đọc trực tiếp ra lưu lượng mà phải qua một phép tính, trong đó cần biết **khối lượng riêng của môi chất**. Với khí và hơi, khối lượng riêng phụ thuộc áp suất và nhiệt độ — nên phải đo thêm hai đại lượng này để bù ([xem bài đơn vị](/don-vi-luu-luong-quy-doi/)).

### Giải pháp cho dải đo hẹp

Có hai cách mở rộng dải đo, cả hai đều tốn thêm chi phí:

**Cách 1 — Dùng nhiều cảm biến chênh áp song song.** Một cái cho dải thấp, một cái cho dải cao, hệ điều khiển tự chuyển. Mở rộng được dải đo đáng kể nhưng phức tạp hơn.

**Cách 2 — Dùng cảm biến chênh áp có turndown rộng.** Các thiết bị hiện đại tốt hơn nhiều so với trước, nhưng vẫn không xóa được giới hạn cơ bản của quan hệ căn bậc hai.

Nếu ứng dụng có **lưu lượng biến động rất rộng**, hãy cân nhắc [vortex](/luu-luong-ke-vortex/) hoặc [Coriolis](/luu-luong-ke-coriolis/) thay vì cố mở rộng dải đo của orifice.

---

## Cấu tạo: các kiểu phần tử sơ cấp

### Tấm orifice

Phổ biến nhất: một **tấm kim loại phẳng có lỗ** kẹp giữa hai mặt bích.

**Tỷ số beta (β)** là thông số quan trọng nhất: tỷ số giữa đường kính lỗ và đường kính trong của ống.

- **β nhỏ** (lỗ nhỏ) → chênh áp lớn, dễ đo, nhưng **tổn thất áp vĩnh viễn lớn**.
- **β lớn** (lỗ to) → tổn thất áp ít hơn, nhưng chênh áp nhỏ, khó đo chính xác.

Chọn β là một bài toán cân bằng, thường nằm trong khoảng giữa hai thái cực.

**Các kiểu lỗ:**

| Kiểu | Đặc điểm | Dùng cho |
|---|---|---|
| **Lỗ đồng tâm (concentric)** | Lỗ tròn ở giữa — tiêu chuẩn | Đa số ứng dụng |
| **Lỗ lệch tâm (eccentric)** | Lỗ lệch xuống dưới hoặc lên trên | Chất lỏng có cặn (lỗ dưới) hoặc có khí (lỗ trên) |
| **Lỗ hình khuyên (segmental)** | Lỗ dạng cung tròn | Môi chất có cặn nặng |
| **Có lỗ thoát (drain/vent hole)** | Thêm lỗ nhỏ ở mép | Thoát nước ngưng hoặc khí tích tụ |

**Chi tiết quan trọng: mép vào của lỗ phải sắc.** Toàn bộ tính toán tiêu chuẩn dựa trên giả định mép lỗ sắc cạnh. Sau thời gian sử dụng, mép này **bị mài mòn tròn đi**, và thiết bị bắt đầu **đọc thấp hơn thực tế**.

Đây là nguồn sai số âm thầm của orifice, và là lý do tấm orifice cần được **kiểm tra và thay định kỳ** — nhất là với môi chất có hạt hoặc chảy nhanh.

**Và: tấm phải lắp đúng chiều.** Mép sắc hướng về phía dòng chảy tới. Lắp ngược là sai số đáng kể. Nhà sản xuất luôn đánh dấu chiều trên tay cầm của tấm — **hãy đọc nó trước khi siết bu lông**.

### Ống venturi

Thay vì một tấm đột ngột, venturi có **đoạn côn thu từ từ, đoạn cổ, rồi côn mở từ từ**.

| Tiêu chí | **Tấm orifice** | **Ống venturi** |
|---|---|---|
| Tổn thất áp vĩnh viễn | **Cao** | **Thấp hơn nhiều** |
| Chi phí | **Thấp** | Cao |
| Chiều dài lắp đặt | Ngắn | **Dài** |
| Chịu môi chất có cặn | Kém | **Tốt hơn** |
| Thay thế, sửa chữa | **Dễ, rẻ** | Khó |

**Khi nào venturi đáng tiền:** khi **tổn thất áp là vấn đề nghiêm trọng** — hệ đã yếu áp, hoặc lưu lượng lớn chạy liên tục khiến điện năng bơm bù vào tổn thất trở nên đáng kể. Trong trường hợp đó, chênh lệch giá thiết bị có thể được bù lại qua tiền điện.

### Ống pitot và pitot trung bình (averaging pitot)

Một thanh dò cắm ngang dòng, có các lỗ hướng về phía dòng chảy tới và lỗ ở phía sau.

**Ưu điểm lớn:**
- **Tổn thất áp rất thấp** — chỉ có một thanh nhỏ trong dòng.
- **Lắp bằng cách khoan một lỗ** — không cần cắt ống, chi phí lắp đặt thấp.
- **Rất kinh tế với ống lớn.**

**Nhược điểm:**
- **Độ chính xác thấp hơn** orifice và venturi.
- **Rất nhạy với biên dạng dòng chảy** — cần đoạn ống thẳng dài.
- **Các lỗ nhỏ dễ tắc** với môi chất bẩn.

**Pitot trung bình** là phiên bản cải tiến: thanh dò có **nhiều lỗ trải dọc đường kính ống**, lấy trung bình vận tốc trên nhiều điểm thay vì một điểm. Chính xác hơn pitot đơn giản đáng kể, và vẫn giữ được ưu điểm tổn thất áp thấp.

Đây là lựa chọn rất đáng cân nhắc cho **ống gió lớn trong hệ HVAC** và **ống khói**, nơi tổn thất áp là vấn đề và độ chính xác yêu cầu vừa phải.

---

## Ứng dụng: lắp đặt và những chi tiết quyết định

### Ống xung — nơi phần lớn sự cố xảy ra

Đây là điểm yếu thực tế lớn nhất của hệ đo chênh áp, và nó không nằm ở thiết bị mà ở **hai ống nhỏ dẫn áp suất**.

**Với chất lỏng:** ống xung phải **luôn đầy chất lỏng, không có bọt khí**. Bọt khí trong một ống làm cột áp hai bên khác nhau → sai số.
- Đặt cảm biến chênh áp **thấp hơn điểm trích áp**.
- Ống xung dốc xuống liên tục về phía thiết bị.
- Lắp van xả khí ở điểm cao.

**Với khí:** ngược lại — ống xung phải **luôn khô, không có chất lỏng ngưng tụ**.
- Đặt cảm biến **cao hơn điểm trích áp**.
- Ống xung dốc lên liên tục.
- Lắp bình thu nước ngưng nếu cần.

**Với hơi:** phức tạp nhất. Cần **bình ngưng (condensate pot)** ở cả hai phía để tạo và duy trì **cột nước ngưng cân bằng**. Nếu hai bình không cân nhau — một bên có nước, một bên không — sai số rất lớn ([xem bài hơi nước](/do-luu-luong-hoi-nuoc/)).

**Nguyên tắc chung:** hai ống xung phải **đối xứng hoàn toàn** — cùng chiều dài, cùng độ dốc, cùng nhiệt độ môi trường. Bất đối xứng là nguồn sai số.

### Cụm van (manifold)

Giữa ống xung và cảm biến chênh áp thường có **cụm van 3 hoặc 5 van**, cho phép:
- **Cô lập** thiết bị để bảo trì mà không dừng quá trình.
- **Cân bằng hai phía** để kiểm tra điểm 0.
- **Xả khí** hoặc xả nước ngưng.

Đây là phụ kiện nên có, không phải tùy chọn. Nó cho phép **kiểm điểm 0 định kỳ** mà không cần dừng hệ — thao tác phát hiện được nhiều sai lệch nhất với chi phí thấp nhất ([xem bài hiệu chuẩn](/hieu-chuan-cam-bien-luu-luong/)).

**Quan trọng: thứ tự thao tác van.** Mở và đóng van sai thứ tự có thể **đặt toàn bộ áp suất quá trình lên một phía màng cảm biến** và làm hỏng nó. Quy trình đúng phải được dán tại chỗ và người vận hành phải được hướng dẫn.

### Yêu cầu đoạn ống thẳng

Phương pháp chênh áp **rất nhạy với biên dạng dòng chảy** — nằm trong nhóm yêu cầu đoạn ống thẳng dài nhất.

Số lần đường kính cần thiết phụ thuộc vào **loại vật cản phía trước** và **tỷ số beta**: beta càng lớn thì càng cần nhiều ống thẳng. Tra bảng trong tiêu chuẩn hoặc tài liệu nhà sản xuất.

Nếu không đủ, có thể dùng **bộ nắn dòng (flow conditioner)** — nhưng nó thêm chi phí và thêm tổn thất áp ([xem bài lắp đặt](/lap-dat-cam-bien-luu-luong/)).

### Tổn thất áp suất — chi phí ẩn suốt vòng đời

Đây là khoản mà so sánh giá mua không nhìn thấy.

Tấm orifice gây **tổn thất áp vĩnh viễn** — một phần đáng kể của chênh áp không bao giờ được phục hồi. Bơm hoặc quạt phải làm việc nhiều hơn để bù, **mỗi giờ, suốt vòng đời hệ thống**.

Với ống lớn chạy liên tục, khoản điện năng này có thể **vượt chênh lệch giá** giữa orifice và một đồng hồ điện từ (vốn gần như không gây tổn thất áp).

Vì vậy khi so sánh phương án, hãy tính:
- Giá thiết bị + phụ kiện (tấm, mặt bích, ống xung, manifold, cảm biến chênh áp)
- Công lắp đặt
- **Điện năng bù tổn thất áp trong suốt vòng đời**
- Bảo trì (thay tấm, vệ sinh ống xung)

Với ống nhỏ và lưu lượng thấp, orifice vẫn rẻ nhất. Với ống lớn chạy 24/7, kết luận có thể ngược lại ([xem bài cách chọn](/cach-chon-cam-bien-luu-luong/)).

---

## So sánh: khi nào chọn chênh áp

### Nên chọn khi

- **Ống rất lớn** — chi phí không tăng nhanh theo cỡ.
- **Nhà máy đã chuẩn hóa trên orifice** — có sẵn tấm dự phòng, thợ quen thao tác.
- **Lưu lượng khá ổn định** — không cần dải đo rộng.
- **Môi chất khắc nghiệt** — nhiệt độ rất cao, áp suất rất cao.
- **Cần thiết bị có thể tự chế tạo hoặc mua từ nhiều nguồn** — không phụ thuộc một hãng.
- **Ngân sách đầu tư hạn chế** và hệ chịu được tổn thất áp.

### Không nên chọn khi

- **Lưu lượng biến động rộng** — dải đo không đủ.
- **Hệ đã yếu áp suất** — không chịu được thêm tổn thất.
- **Lưu lượng lớn chạy liên tục** — chi phí điện bù tổn thất áp lớn.
- **Môi chất bẩn, có cặn** — tắc ống xung, mòn mép lỗ.
- **Không có người bảo trì ống xung định kỳ.**
- **Cần độ chính xác cao** — có công nghệ tốt hơn.
- **Đường ống chật** — không đủ đoạn ống thẳng.

---

## Sai lầm thường gặp

1. **Lắp tấm orifice ngược chiều** — mép sắc phải hướng về phía dòng tới.
2. **Không kiểm tra và thay tấm định kỳ** — mép mòn làm đọc thấp dần.
3. **Ống xung không đối xứng** — khác chiều dài, khác độ dốc, khác nhiệt độ.
4. **Bọt khí trong ống xung khi đo chất lỏng** — sai số lớn.
5. **Nước ngưng trong ống xung khi đo khí** — sai số lớn.
6. **Hai bình ngưng không cân nhau khi đo hơi** — sai số rất lớn.
7. **Thao tác van manifold sai thứ tự** — hỏng màng cảm biến chênh áp.
8. **Chọn beta không phù hợp** — hoặc tổn thất áp quá lớn, hoặc chênh áp quá nhỏ.
9. **Bỏ qua yêu cầu đoạn ống thẳng** — nhóm nhạy nhất.
10. **Không tính điện năng bù tổn thất áp** vào so sánh chi phí.
11. **Vận hành ở đáy dải đo** — nơi sai số bị khuếch đại bởi phép căn bậc hai.
12. **Đo khí hoặc hơi mà không bù áp suất và nhiệt độ.**

---

## Cam kết tại HOANTRANTDH

- ✅ **Tính toán và so sánh trung thực** giữa orifice và các công nghệ khác, có tính tổn thất áp suốt vòng đời.
- ✅ Tư vấn **chọn tỷ số beta** cân bằng giữa chênh áp đo được và tổn thất áp chấp nhận được.
- ✅ Cung cấp đồng bộ **tấm orifice, cụm van manifold và [cảm biến chênh áp](/cam-bien-chenh-ap/)**.
- ✅ Hướng dẫn **bố trí ống xung đúng** theo môi chất — nơi phần lớn sai số của hệ chênh áp phát sinh.

---

<a name="bao-gia"></a>
## Nhận tính toán & báo giá

Gửi cho chúng tôi: **môi chất (lỏng, khí, hơi) · đường kính trong của ống · dải lưu lượng nhỏ nhất và lớn nhất · áp suất và nhiệt độ làm việc · áp suất khả dụng của hệ (chịu được bao nhiêu tổn thất) · sơ đồ đoạn ống thẳng · có sẵn cảm biến chênh áp chưa.**

**→ [Liên hệ nhận tư vấn hệ chênh áp](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đo lưu lượng bằng chênh áp hoạt động thế nào?**
Một vật cản làm dòng **thu hẹp lại**, khiến vận tốc tăng và áp suất giảm. Đo **chênh lệch áp suất trước và tại chỗ thu hẹp** rồi suy ra lưu lượng.

**Vì sao dải đo của orifice hẹp?**
Vì **lưu lượng tỷ lệ với căn bậc hai của chênh áp**. Ở nửa dải đo, chênh áp chỉ còn một phần tư; ở một phần ba dải đo, chỉ còn một phần chín — quá nhỏ để đo chính xác.

**Tỷ số beta là gì?**
Là **tỷ số giữa đường kính lỗ orifice và đường kính trong ống**. Beta nhỏ cho chênh áp lớn dễ đo nhưng tổn thất áp cao; beta lớn thì ngược lại.

**Lắp tấm orifice có phân biệt chiều không?**
**Có.** **Mép sắc phải hướng về phía dòng chảy tới**. Lắp ngược gây sai số đáng kể. Nhà sản xuất luôn đánh dấu chiều trên tay cầm của tấm.

**Vì sao orifice đọc thấp dần theo năm?**
Vì **mép vào của lỗ bị mài mòn tròn đi**. Toàn bộ tính toán tiêu chuẩn giả định mép sắc, nên khi mép mòn thiết bị đọc thấp hơn thực tế.

**Ống xung nên bố trí thế nào?**
Với **chất lỏng**: cảm biến đặt **thấp hơn** điểm trích, ống dốc xuống, không có bọt khí. Với **khí**: cảm biến đặt **cao hơn**, ống dốc lên, không có nước ngưng. Với **hơi**: cần bình ngưng cân bằng ở cả hai phía.

**Venturi có gì hơn tấm orifice?**
**Tổn thất áp thấp hơn nhiều** và chịu môi chất có cặn tốt hơn. Đổi lại đắt hơn, dài hơn và khó thay thế hơn.

**Khi nào nên dùng ống pitot?**
Khi **ống rất lớn** và **tổn thất áp là vấn đề** — ví dụ ống gió HVAC hoặc ống khói. Nên dùng loại **pitot trung bình** (nhiều lỗ) để có độ chính xác tốt hơn pitot đơn giản.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /don-vi-luu-luong-quy-doi/, /luu-luong-ke-vortex/, /luu-luong-ke-coriolis/, /lap-dat-cam-bien-luu-luong/, /hieu-chuan-cam-bien-luu-luong/, /do-luu-luong-hoi-nuoc/, /cach-chon-cam-bien-luu-luong/, /cam-bien-chenh-ap/, /lien-he/. -->
