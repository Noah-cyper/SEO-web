<!--
LOẠI TRANG : Bài kiến thức kỹ thuật (chuỗi biến tần — tầng 1) — Thông tin
URL SLUG   : /nguyen-ly-hoat-dong-bien-tan/
TỪ KHÓA    : nguyên lý hoạt động biến tần | pwm biến tần | luật v/f | tần số và tốc độ động cơ | biến tần ac dc ac
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 3/30 trong chuỗi biến tần.
-->

TITLE TAG   : Nguyên Lý Hoạt Động Của Biến Tần – PWM, Luật V/f Giải Thích Dễ Hiểu
META (156)  : Nguyên lý hoạt động của biến tần: quá trình AC-DC-AC, kỹ thuật PWM tạo sóng, luật V/f giữ mô-men, quan hệ tần số và tốc độ động cơ, vùng suy giảm từ thông và hãm tái sinh.
H1          : Nguyên Lý Hoạt Động Của Biến Tần (PWM & Luật V/f)

---

## Vấn đề cần giải quyết: vì sao không thể "vặn nhỏ" điện lưới?

Để hiểu biến tần, trước hết phải hiểu **vì sao không thể điều khiển tốc độ động cơ bằng cách giảm điện áp đơn thuần**.

Tốc độ quay của động cơ không đồng bộ 3 pha được quyết định bởi **tần số** của nguồn cấp, theo công thức tốc độ đồng bộ:

> **n = 120 × f / p**
> (n: vòng/phút · f: tần số Hz · p: số cực của động cơ)

Ví dụ động cơ 4 cực chạy ở 50 Hz sẽ có tốc độ đồng bộ **1500 vòng/phút** (thực tế thấp hơn một chút do độ trượt).

Điểm mấu chốt: **điện áp không nằm trong công thức này**. Nếu bạn chỉ giảm điện áp mà giữ nguyên tần số, động cơ **không chạy chậm lại đáng kể** — nó chỉ **yếu đi**: mô-men giảm mạnh, dòng tăng, động cơ nóng và có thể cháy.

Vậy muốn đổi tốc độ thì phải **đổi tần số**. Nhưng lưới điện có tần số cố định 50 Hz. Đây chính là bài toán mà biến tần sinh ra để giải.

> **Cần tư vấn chọn chế độ điều khiển đúng cho máy của bạn?** Gửi **loại tải · yêu cầu mô-men khởi động · dải tốc độ cần** → [Nhận tư vấn](#bao-gia).

Bài này là bài **3/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý ba bước: AC → DC → AC

Biến tần không "sửa" tần số lưới — nó **phá bỏ hoàn toàn rồi tạo lại**.

**Bước 1 — Chỉnh lưu (AC → DC).** Điện xoay chiều 50 Hz từ lưới đi qua cầu diode, thành điện một chiều còn nhấp nhô. Đến đây, **thông tin về tần số 50 Hz đã bị xoá bỏ hoàn toàn** — đây chính là ý nghĩa của bước này.

**Bước 2 — Lọc phẳng (DC bus).** Các tụ điện dung lượng lớn san phẳng phần nhấp nhô, tạo ra một nguồn một chiều ổn định. DC bus đóng vai trò như một "hồ chứa năng lượng" mà khối nghịch lưu có thể lấy ra tuỳ ý.

**Bước 3 — Nghịch lưu (DC → AC).** Sáu van **IGBT** đóng/cắt theo thứ tự và thời lượng được tính toán để tạo ra ba pha điện xoay chiều mới — với **tần số và điện áp hoàn toàn do biến tần quyết định**.

Vì tần số đầu ra được tạo mới từ nguồn một chiều, biến tần có thể xuất ra **bất kỳ tần số nào** trong dải cho phép: 5 Hz, 30 Hz, 50 Hz, thậm chí 60–120 Hz nếu động cơ và cơ khí chịu được.

---

## Kỹ thuật PWM: tạo sóng sin bằng các xung vuông

Đây là phần khiến nhiều người bối rối: IGBT chỉ có hai trạng thái **đóng** hoặc **cắt**, vậy làm sao tạo ra được sóng hình sin mượt mà?

Câu trả lời là **PWM — điều chế độ rộng xung (Pulse Width Modulation)**.

Thay vì tạo ra điện áp hình sin thật, biến tần phát ra **một chuỗi xung vuông có biên độ không đổi nhưng độ rộng thay đổi**. Ở đoạn mà sóng sin cần giá trị lớn, các xung được làm **rộng** ra; ở đoạn cần giá trị nhỏ, xung **hẹp** lại.

Điều kỳ diệu nằm ở chỗ: **cuộn dây động cơ có tính cảm kháng** — nó không phản ứng kịp với từng xung riêng lẻ mà chỉ "cảm nhận" **giá trị trung bình** của chuỗi xung. Kết quả là **dòng điện chạy trong động cơ gần như hình sin**, dù điện áp đặt vào là các xung vuông.

Số lần IGBT đóng cắt trong một giây gọi là **tần số sóng mang (carrier frequency)**. Đây là thông số có sự đánh đổi rõ rệt:

| Tần số sóng mang | Ưu điểm | Nhược điểm |
|---|---|---|
| **Cao** | Động cơ chạy êm, ít tiếng rít, dòng gần sin hơn | IGBT **nóng hơn**, **nhiễu EMC mạnh hơn**, hạn chế chiều dài cáp |
| **Thấp** | IGBT mát, nhiễu ít, chạy được cáp dài | Động cơ **kêu rít** rõ, dòng méo hơn |

Trong thực tế, khi biến tần hay báo quá nhiệt hoặc gây nhiễu cảm biến, **giảm tần số sóng mang** là một trong những biện pháp xử lý đầu tiên. [Xem chống nhiễu EMC →](/chong-nhieu-emc-cho-bien-tan/)

---

## Luật V/f: quy tắc quan trọng nhất cần hiểu

Đây là nguyên lý mà mọi người dùng biến tần nên nắm, vì nó giải thích rất nhiều hiện tượng thực tế.

**Vấn đề:** từ thông trong động cơ tỉ lệ thuận với **điện áp** và tỉ lệ nghịch với **tần số**, tức tỉ lệ với **U/f**. Nếu bạn giảm tần số xuống 25 Hz mà giữ nguyên điện áp 380V, tỉ số U/f **tăng gấp đôi** → từ thông tăng vọt → lõi thép động cơ **bão hoà từ** → dòng từ hoá tăng đột biến → động cơ nóng dữ dội và có thể cháy.

**Giải pháp:** biến tần **giảm điện áp đồng thời với tần số**, giữ tỉ số **U/f không đổi**. Ví dụ với động cơ 380V/50 Hz:

| Tần số đặt | Điện áp ra (xấp xỉ) | Tỉ số U/f | Mô-men khả dụng |
|---|---|---|---|
| 50 Hz | 380 V | 7,6 | 100% |
| 40 Hz | 304 V | 7,6 | ~100% |
| 25 Hz | 190 V | 7,6 | ~100% |
| 10 Hz | 76 V | 7,6 | Giảm (cần bù) |

Nhờ giữ U/f không đổi, **mô-men của động cơ được duy trì gần như nguyên vẹn** trên toàn dải tốc độ. Đây là lý do biến tần có thể cho động cơ chạy chậm mà vẫn kéo được tải.

**Hai vùng làm việc cần phân biệt:**

- **Vùng dưới 50 Hz — vùng mô-men không đổi.** U và f tăng cùng nhau, mô-men giữ nguyên, công suất tăng dần theo tốc độ.
- **Vùng trên 50 Hz — vùng suy giảm từ thông.** Điện áp **không thể tăng quá điện áp lưới**, nên khi f tiếp tục tăng thì U đứng yên → tỉ số U/f giảm → **mô-men giảm dần**. Công suất gần như không đổi.

Hệ quả thực tế rất quan trọng: **chạy vượt 50 Hz thì tốc độ tăng nhưng mô-men giảm**. Với quạt hay bơm cần thêm lưu lượng thì đôi khi chấp nhận được; với băng tải hay máy ép cần mô-men thì phải hết sức thận trọng.

**Vấn đề mô-men ở tần số rất thấp:** khi f nhỏ (dưới ~5–10 Hz), điện áp ra rất thấp và phần điện áp rơi trên điện trở cuộn dây chiếm tỉ lệ đáng kể, làm mô-men suy giảm. Các biến tần có thông số **bù mô-men (torque boost)** để tăng thêm điện áp ở vùng này. Cài quá tay sẽ khiến động cơ nóng khi chạy không tải.

---

## Ứng dụng: từ nguyên lý đến vận hành thực tế

Hiểu nguyên lý giúp lý giải nhiều hiện tượng thường gặp:

**Vì sao động cơ kêu rít khi chạy biến tần?** Do tần số sóng mang PWM nằm trong dải nghe được. Tăng tần số sóng mang sẽ êm hơn, đổi lại IGBT nóng hơn.

**Vì sao chạy chậm lâu thì động cơ nóng?** Vì quạt làm mát gắn trên trục động cơ **quay chậm theo**, khả năng tản nhiệt giảm mạnh trong khi dòng vẫn lớn. Với ứng dụng chạy chậm kéo dài, cần **quạt cưỡng bức riêng**.

**Vì sao giảm tốc nhanh lại báo quá áp?** Khi giảm tốc, động cơ trở thành **máy phát**, đẩy năng lượng ngược về DC bus làm điện áp tăng vọt. Giải pháp: kéo dài thời gian giảm tốc, hoặc lắp **điện trở hãm** để đốt bớt năng lượng. [Xem xử lý lỗi quá áp →](/loi-qua-ap-thap-ap-bien-tan/)

**Vì sao tăng tốc nhanh lại báo quá dòng?** Vì mô-men cần để tăng tốc tỉ lệ với gia tốc. Rút ngắn thời gian tăng tốc quá mức đòi hỏi mô-men vượt khả năng, biến tần bảo vệ bằng cách báo lỗi. [Xem xử lý lỗi quá dòng →](/loi-qua-dong-bien-tan/)

**Vì sao biến tần tiết kiệm điện với bơm/quạt?** Vì loại tải này có **công suất tỉ lệ với lũy thừa ba của tốc độ**. Giảm tốc 20% đưa công suất về khoảng 51%. [Xem chi tiết →](/bien-tan-tiet-kiem-dien/)

---

## So sánh: điều khiển V/f và điều khiển vector

Luật V/f mô tả ở trên là **phương pháp điều khiển vô hướng (scalar)** — đơn giản, ổn định, nhưng không "biết" động cơ đang thực sự chịu tải ra sao.

**Điều khiển vector** đi xa hơn: biến tần dựng **mô hình toán học của động cơ**, tách dòng điện thành hai thành phần — một tạo từ thông, một tạo mô-men — rồi điều khiển độc lập từng thành phần. Nhờ đó nó phản ứng nhanh khi tải thay đổi và cho **mô-men khởi động cao ngay ở tốc độ rất thấp**.

| Tiêu chí | **V/f (vô hướng)** | **Vector** |
|---|---|---|
| Độ phức tạp cài đặt | Đơn giản | Cần **auto-tuning** thông số động cơ |
| Mô-men ở tốc độ thấp | Trung bình | **Cao** |
| Giữ tốc độ khi tải đổi | Kém hơn | **Tốt** |
| Chạy nhiều động cơ song song | **Được** | Thường không |
| Phù hợp | Bơm, quạt, tải nhẹ | Băng tải, nâng hạ, máy ép, máy công cụ |

**Nguyên tắc chọn:** nếu tải là bơm hoặc quạt, V/f thường là đủ và đơn giản hơn. Nếu tải cần **giật khởi động mạnh** hoặc **giữ tốc độ ổn định khi tải biến động**, hãy dùng vector. [Xem so sánh chi tiết →](/che-do-dieu-khien-vf-vector/)

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn chọn **chế độ điều khiển đúng loại tải** — tránh mua thừa tính năng.
- ✅ Hỗ trợ cài đặt thông số động cơ, auto-tuning và bù mô-men.
- ✅ Biến tần **chính hãng**, CO/CQ, hoá đơn VAT.
- ✅ Hỗ trợ xử lý nhiễu, chọn cáp và phương án hãm khi cần.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi: **loại tải · công suất và dòng động cơ · dải tốc độ cần · yêu cầu mô-men khởi động · thời gian tăng/giảm tốc mong muốn.**

**→ [Liên hệ tư vấn biến tần](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Nguyên lý hoạt động của biến tần là gì?**
Biến tần thực hiện ba bước: **chỉnh lưu AC→DC**, **lọc phẳng ở DC bus**, rồi **nghịch lưu DC→AC** bằng IGBT theo kỹ thuật **PWM** với tần số do biến tần quyết định.

**Vì sao đổi tần số lại đổi được tốc độ động cơ?**
Vì tốc độ đồng bộ tuân theo **n = 120 × f / p** — tỉ lệ thuận với tần số. Điện áp không quyết định tốc độ.

**Luật V/f nghĩa là gì?**
Là quy tắc **giữ tỉ số điện áp trên tần số không đổi** khi thay đổi tốc độ, để từ thông ổn định và **mô-men được duy trì**.

**Chạy biến tần trên 50 Hz có được không?**
Được về mặt tần số, nhưng vào **vùng suy giảm từ thông** — **mô-men giảm dần**. Phải kiểm tra động cơ và cơ khí có chịu được tốc độ cao hơn không.

**PWM là gì?**
Là kỹ thuật **điều chế độ rộng xung**: tạo chuỗi xung vuông có độ rộng thay đổi, nhờ tính cảm kháng của cuộn dây mà dòng trong động cơ gần như hình sin.

**Vì sao chạy tần số thấp lâu thì động cơ nóng?**
Vì **quạt làm mát gắn trên trục quay chậm theo**, tản nhiệt kém trong khi dòng vẫn lớn. Cần quạt cưỡng bức riêng nếu chạy chậm kéo dài.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /cau-tao-bien-tan/, /che-do-dieu-khien-vf-vector/, /bien-tan-tiet-kiem-dien/, /lien-he/. -->
