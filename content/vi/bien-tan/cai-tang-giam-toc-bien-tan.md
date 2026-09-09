<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 4) — Thông tin
URL SLUG   : /cai-tang-giam-toc-bien-tan/
TỪ KHÓA    : thời gian tăng tốc biến tần | thời gian giảm tốc biến tần | điện trở xả biến tần | đường cong chữ S | lỗi khi giảm tốc
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 19/30 trong chuỗi biến tần.
-->

TITLE TAG   : Cài Thời Gian Tăng Giảm Tốc Biến Tần – Cách Chọn Đúng Và Chống Lỗi
META (156)  : Cách đặt thời gian tăng giảm tốc cho biến tần theo quán tính tải, xử lý lỗi quá dòng khi tăng tốc và quá áp khi giảm tốc, khi nào cần điện trở xả.

H1          : Cài Thời Gian Tăng Giảm Tốc Cho Biến Tần

---

## Hai con số quyết định biến tần chạy êm hay báo lỗi

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Trong toàn bộ bảng thông số của biến tần, **thời gian tăng tốc** và **thời gian giảm tốc** là hai con số gây ra nhiều sự cố nhất — và cũng là hai con số dễ sửa nhất.

Định nghĩa của chúng rất cụ thể:

- **Thời gian tăng tốc** là thời gian biến tần đưa tần số **từ 0 lên tần số định mức** (thường 50Hz).
- **Thời gian giảm tốc** là thời gian đưa tần số **từ tần số định mức về 0**.

Lưu ý quan trọng: đó là thời gian tính theo **toàn dải**, không phải theo quãng thực tế. Nếu đặt tăng tốc 20 giây và bạn chỉ chạy từ 0 lên 25Hz, thời gian thực tế chỉ khoảng 10 giây.

Hai con số này ảnh hưởng trực tiếp tới:

- **Dòng khởi động** — tăng tốc càng nhanh, dòng càng lớn.
- **Điện áp DC bus khi dừng** — giảm tốc càng nhanh, năng lượng dội về càng nhiều.
- **Ứng suất cơ khí** — dây curoa, xích, khớp nối, hộp số.
- **Chất lượng sản phẩm** — chai đổ trên băng tải, vật liệu văng, nước va trong đường ống.
- **Năng suất** — chu kỳ máy dài hay ngắn.

> **Máy hay báo lỗi khi khởi động hoặc khi dừng?** Gửi **mã lỗi · model biến tần · mô tả tải** → [Nhận tư vấn xử lý](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vf-ratio.svg)


Đây là bài **19/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: quán tính, mô-men và năng lượng dội về

### Khi tăng tốc

Để thay đổi tốc độ của một khối lượng đang quay, cần một **mô-men gia tốc** cộng thêm ngoài mô-men để thắng tải. Mô-men gia tốc tỷ lệ thuận với **quán tính của hệ** và tỷ lệ nghịch với **thời gian tăng tốc**.

Mô-men do động cơ sinh ra lại tỷ lệ với **dòng điện**. Vì vậy:

> Rút ngắn thời gian tăng tốc → cần mô-men lớn hơn → dòng lớn hơn → dễ chạm ngưỡng bảo vệ quá dòng.

Đó là lý do một máy có bánh đà lớn, hoặc một quạt ly tâm có cánh nặng, thường **không thể** khởi động trong vài giây dù biến tần đủ công suất. Vấn đề không nằm ở công suất mà ở quán tính.

### Khi giảm tốc

Đây là phần nhiều người bỏ qua. Khi biến tần giảm tần số nhanh hơn tốc độ mà tải tự chậm lại, **động cơ trở thành máy phát**. Năng lượng động năng của khối quay chảy ngược qua IGBT về **tụ DC bus**.

Tụ DC bus không có chỗ nào để xả năng lượng đó — biến tần thông thường không trả điện ngược lên lưới. Kết quả là **điện áp DC bus dâng lên**, và khi vượt ngưỡng, biến tần **báo lỗi quá áp và cắt** ([xem chi tiết lỗi quá áp](/loi-qua-ap-thap-ap-bien-tan/)).

Năng lượng này tỷ lệ với **quán tính** và với **bình phương tốc độ**. Nghĩa là dừng một khối quay nhanh từ tốc độ cao tạo ra lượng năng lượng lớn hơn rất nhiều so với cảm giác trực giác.

### Đường cong tuyến tính và đường cong chữ S

Mặc định, biến tần tăng tần số theo **đường thẳng** — tốc độ thay đổi đều. Điều đó tạo ra **hai điểm gãy**: lúc bắt đầu và lúc kết thúc, gia tốc đổi đột ngột, gây giật.

**Đường cong chữ S (S-curve)** làm mềm hai điểm gãy đó: bắt đầu chậm, giữa nhanh, cuối chậm lại. Đánh đổi là **tổng thời gian dài hơn** so với đường thẳng cùng cài đặt.

S-curve rất đáng dùng khi:
- Băng tải chở vật dễ đổ, dễ trượt.
- Thang nâng, cầu trục — liên quan trải nghiệm và an toàn.
- Hệ có dây curoa hoặc xích dễ trượt/giãn.
- Máy có khớp nối mềm hay hộp số cần bảo vệ.

---

## Cấu tạo bộ thông số liên quan

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-thongso.svg)


Ngoài hai thông số chính, có một nhóm thông số phụ đi kèm mà hiểu đúng sẽ giải quyết được phần lớn tình huống:

| Thông số | Ý nghĩa | Khi nào dùng |
|---|---|---|
| **Thời gian tăng tốc 1** | Từ 0 → tần số định mức | Luôn dùng |
| **Thời gian giảm tốc 1** | Từ tần số định mức → 0 | Luôn dùng |
| **Thời gian tăng/giảm tốc 2, 3, 4** | Bộ thời gian dự phòng | Chuyển bằng chân DI hoặc theo ngưỡng tần số — dùng khi một máy có nhiều chế độ |
| **Đường cong chữ S (S-curve)** | Làm mềm điểm bắt đầu/kết thúc | Tải dễ đổ, cầu trục, thang nâng |
| **Kiểu dừng (Stop mode)** | Giảm tốc theo dốc hay **chạy trớn tự do** | Chạy trớn khi không cần dừng nhanh |
| **Hãm DC khi dừng** | Bơm dòng một chiều để giữ trục | Cần dừng dứt điểm, chống trôi |
| **Chống quá áp khi giảm tốc** | Biến tần tự kéo dài thời gian dừng | Bật khi hay lỗi quá áp, chưa muốn lắp điện trở xả |
| **Điện trở xả / bộ hãm** | Đốt năng lượng dội về thành nhiệt | Bắt buộc khi phải dừng nhanh tải quán tính lớn |
| **Tần số điểm chuyển thời gian** | Đổi bộ thời gian theo ngưỡng tần số | Máy cần dốc khác nhau ở vùng tốc độ thấp/cao |

---

## Ứng dụng: chọn thời gian theo loại tải

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bangtai.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)

Không có con số đúng cho mọi máy. Nhưng có **thứ tự ưu tiên rõ ràng** theo loại tải:

**Quạt ly tâm cỡ lớn.** Quán tính cánh quạt rất lớn, nhưng mô-men cản ở tốc độ thấp lại nhỏ. Nên đặt **thời gian tăng tốc dài**. Khi dừng, thường **không cần dừng nhanh** — cho chạy trớn tự do là giải pháp đơn giản và rẻ nhất, tránh hoàn toàn lỗi quá áp ([xem bài quạt hút](/bien-tan-cho-quat-hut/)).

**Bơm ly tâm.** Cần lưu ý **nước va (water hammer)**. Tăng tốc và giảm tốc quá nhanh gây xung áp lực trong đường ống, hại van và mối nối. Đặt thời gian vừa phải, ưu tiên êm hơn nhanh ([xem bài bơm nước](/bien-tan-cho-bom-nuoc/)).

**Băng tải.** Tùy vật liệu chuyên chở. Vật rời, chai lọ, sản phẩm đứng → cần S-curve và thời gian dài hơn. Vật cố định, thùng nặng → có thể ngắn hơn. Đây là ứng dụng mà S-curve mang lại hiệu quả thấy rõ nhất.

**Máy có bánh đà, máy nghiền, máy ly tâm.** Quán tính rất lớn. Tăng tốc dài, và khi cần dừng nhanh thì **gần như chắc chắn phải có điện trở xả**.

**Cầu trục, thang nâng, tời.** Tải thế năng. Khi hạ, tải tự kéo động cơ quay — năng lượng dội về liên tục, không chỉ lúc dừng. Đây là ứng dụng **bắt buộc có bộ hãm và điện trở xả**, không phải tùy chọn.

**Máy công cụ, trục chính.** Cần dừng nhanh và chính xác. Thường dùng vector kèm hãm DC và điện trở xả.

### Quy trình dò giá trị tối ưu

1. Bắt đầu với giá trị **rộng rãi** — ví dụ dài gấp 2–3 lần dự đoán.
2. Chạy thử, quan sát **dòng khi tăng tốc** trên màn hình biến tần.
3. **Rút ngắn dần** cho tới khi dòng chạm gần ngưỡng bảo vệ hoặc biến tần bắt đầu báo lỗi.
4. **Lùi lại một bậc** để có biên an toàn.
5. Làm tương tự với giảm tốc, quan sát **điện áp DC bus**.
6. Nếu không rút ngắn được tới mức yêu cầu của quy trình sản xuất → cân nhắc **điện trở xả** (khi dừng) hoặc **biến tần lớn hơn một cấp** (khi tăng tốc).
7. Chạy thử ở **điều kiện tải nặng nhất** — không chỉ chạy không tải.
8. Ghi lại giá trị cuối cùng vào hồ sơ máy ([xem bài cài đặt thông số](/cai-dat-thong-so-bien-tan/)).

---

## So sánh các cách xử lý lỗi khi giảm tốc

Khi biến tần báo quá áp lúc dừng, có bốn hướng xử lý. Chúng khác nhau về chi phí và về việc có đạt được yêu cầu công nghệ hay không:

| Cách xử lý | Chi phí | Dừng nhanh được? | Phù hợp với |
|---|---|---|---|
| **Kéo dài thời gian giảm tốc** | Miễn phí | Không | Quạt, bơm, máy không yêu cầu chu kỳ |
| **Chuyển sang chạy trớn tự do** | Miễn phí | Không | Quạt lớn, máy không cần dừng dứt điểm |
| **Bật chống quá áp (tự kéo dài)** | Miễn phí | Không đoán trước được | Khi thời gian dừng không quan trọng |
| **Lắp điện trở xả + bộ hãm** | Trung bình | **Có** | Cầu trục, máy ly tâm, máy công cụ, máy có chu kỳ ngắn |

**Cảnh báo về chức năng chống quá áp tự động:** nó hoạt động bằng cách **tự ý kéo dài thời gian dừng** khi thấy DC bus tăng cao. Máy sẽ không báo lỗi nữa, nhưng thời gian dừng trở nên **không xác định**. Với dây chuyền cần đồng bộ, điều này có thể tệ hơn cả việc báo lỗi. Trong trường hợp đó phải dùng điện trở xả.

**Về điện trở xả:** chọn theo **giá trị điện trở (Ω)** và **công suất (W)** mà hãng khuyến nghị cho từng model. Điện trở xả **rất nóng khi làm việc** — lắp ở nơi thoáng, tránh xa dây dẫn và vật liệu dễ cháy, không đặt trong tủ kín cùng biến tần nếu không có thông gió đủ ([xem bố trí tủ](/lap-bien-tan-trong-tu-dien/)).

---

## Sai lầm thường gặp

1. **Đặt thời gian tăng tốc quá ngắn để máy nhanh hơn** rồi liên tục [lỗi quá dòng](/loi-qua-dong-bien-tan/).
2. **Đặt giảm tốc ngắn cho tải quán tính lớn** mà không có điện trở xả.
3. **Nhầm rằng thời gian đó tính theo quãng thực tế**, không phải toàn dải 0–50Hz.
4. **Bật chống quá áp tự động cho dây chuyền cần đồng bộ** — thời gian dừng trở nên bất định.
5. **Không dùng S-curve** cho băng tải chở vật dễ đổ.
6. **Lắp điện trở xả trong tủ kín** không thông gió — quá nhiệt, nguy cơ cháy.
7. **Chỉ chạy thử không tải** rồi chốt thông số, đến khi tải nặng thì báo lỗi.
8. **Tăng công suất biến tần** để xử lý lỗi quá áp khi dừng — sai hướng, vì vấn đề là năng lượng dội về chứ không phải thiếu công suất.
9. **Quên rằng cầu trục cần hãm liên tục khi hạ tải**, chỉ tính năng lượng lúc dừng.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **thời gian tăng/giảm tốc theo loại tải thực tế**, không đưa con số chung chung.
- ✅ Tính chọn **điện trở xả và bộ hãm** đúng giá trị và công suất theo model biến tần.
- ✅ Hỗ trợ **xử lý lỗi quá dòng khi khởi động, quá áp khi dừng** từ xa qua Zalo.
- ✅ Cung cấp đồng bộ [biến tần](/bien-tan-la-gi/), điện trở xả, cuộn kháng và phụ kiện tủ.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **model biến tần · công suất động cơ · loại tải và mô tả quán tính (có bánh đà, cánh quạt lớn, tải nâng hạ không) · thời gian dừng yêu cầu · mã lỗi đang gặp.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Thời gian tăng tốc biến tần tính như thế nào?**
Là thời gian đưa tần số **từ 0 lên tần số định mức** (thường 50Hz). Nếu chỉ chạy tới nửa dải thì thời gian thực tế cũng chỉ khoảng một nửa.

**Đặt thời gian tăng tốc bao nhiêu là hợp lý?**
Không có con số chung. Hãy bắt đầu **rộng rãi**, rút ngắn dần trong khi quan sát dòng, rồi lùi lại một bậc để có biên an toàn.

**Vì sao biến tần báo lỗi quá dòng khi khởi động?**
Vì thời gian tăng tốc **quá ngắn so với quán tính tải**, khiến động cơ cần mô-men lớn, kéo theo dòng lớn vượt ngưỡng bảo vệ.

**Vì sao biến tần báo lỗi quá áp khi dừng?**
Vì khi giảm tốc nhanh, động cơ **trở thành máy phát**, đẩy năng lượng ngược về tụ DC bus làm điện áp dâng vượt ngưỡng.

**Khi nào cần điện trở xả?**
Khi **bắt buộc phải dừng nhanh** tải có quán tính lớn, hoặc với **tải nâng hạ** như cầu trục, thang nâng — nơi năng lượng dội về xuất hiện liên tục khi hạ tải.

**Đường cong chữ S dùng khi nào?**
Khi cần **khởi động và dừng êm**: băng tải chở vật dễ đổ, cầu trục, thang nâng, hệ có dây curoa dễ trượt.

**Chức năng chống quá áp tự động có nên bật không?**
Chỉ nên bật khi **thời gian dừng không quan trọng**, vì nó tự kéo dài thời gian giảm tốc khiến thời gian dừng trở nên không xác định.

**Chạy trớn tự do khác dừng theo dốc thế nào?**
**Chạy trớn** là biến tần ngắt đầu ra, để tải tự dừng theo ma sát — không sinh năng lượng dội về. **Dừng theo dốc** là biến tần chủ động giảm tần số, dừng nhanh hơn nhưng có thể gây quá áp.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /cai-dat-thong-so-bien-tan/, /loi-qua-dong-bien-tan/, /loi-qua-ap-thap-ap-bien-tan/, /bien-tan-cho-bom-nuoc/, /bien-tan-cho-quat-hut/, /lap-bien-tan-trong-tu-dien/, /lien-he/. -->
