<!--
LOẠI TRANG : Bài ứng dụng (chuỗi biến tần — tầng 6) — Thông tin → Thương mại
URL SLUG   : /bien-tan-cho-cau-truc-palang/
TỪ KHÓA    : biến tần cho cầu trục | biến tần palăng | biến tần nâng hạ | tải thế năng | chống đung đưa cầu trục
INTENT     : Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 33/50 trong chuỗi biến tần.
-->

TITLE TAG   : Biến Tần Cho Cầu Trục & Palăng – Nâng Hạ An Toàn, Chống Trôi Tải
META (155)  : Ứng dụng biến tần cho cầu trục, palăng, tời: vì sao bắt buộc có điện trở xả và encoder, cách phối hợp phanh cơ, chống trôi tải và giảm đung đưa khi di chuyển.

H1          : Biến Tần Cho Cầu Trục Và Palăng

---

## Nâng hạ là ứng dụng khắt khe nhất của biến tần

Trong tất cả các ứng dụng của biến tần, **nâng hạ là nhóm khắt khe nhất** — không phải vì kỹ thuật phức tạp hơn, mà vì **hậu quả của một sai sót là tai nạn**, không chỉ là hỏng thiết bị.

Cầu trục, palăng, tời, thang nâng đều thuộc nhóm **tải thế năng (overhauling load)**. Đặc điểm phân biệt chúng với mọi loại tải khác:

> Với băng tải, bơm, quạt — tải luôn **cản trở** chuyển động. Với tải nâng hạ, trọng lực **cản trở khi nâng nhưng lại thúc đẩy khi hạ**.

Điều đó tạo ra hai tình huống hoàn toàn khác nhau trong cùng một thiết bị:

- **Khi nâng:** động cơ phải sinh mô-men lớn để thắng trọng lượng tải. Đây là chế độ động cơ bình thường.
- **Khi hạ:** trọng lực kéo tải xuống, **có xu hướng làm động cơ quay nhanh hơn tần số đặt**. Động cơ trở thành máy phát và bơm năng lượng ngược về biến tần — **liên tục trong suốt quá trình hạ**, không chỉ trong khoảnh khắc dừng.

Và một yêu cầu thứ ba không có ở bất kỳ ứng dụng nào khác: **giữ tải đứng yên ở tốc độ bằng 0** mà không để nó trôi xuống.

Ba đặc điểm này quyết định toàn bộ cấu hình thiết bị.

> **Đang cần biến tần cho cầu trục hoặc palăng?** Gửi **tải trọng · chiều cao nâng · công suất động cơ** → [Nhận tư vấn cấu hình](#bao-gia).

Đây là bài **33/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: bốn góc phần tư và năng lượng dội về

Một hệ truyền động có thể làm việc ở **bốn góc phần tư**, phân biệt theo chiều quay và chiều mô-men:

| Góc phần tư | Chiều quay | Chiều mô-men | Tình huống cầu trục |
|---|---|---|---|
| **I** | Thuận | Cùng chiều quay | **Nâng tải lên** |
| **II** | Thuận | Ngược chiều quay | Hãm khi đang nâng |
| **III** | Ngược | Cùng chiều quay | Hạ tải nhẹ, cần kéo xuống |
| **IV** | Ngược | Ngược chiều quay | **Hạ tải nặng — hãm liên tục** |

Với bơm và quạt, hệ chỉ làm việc ở góc phần tư I và thỉnh thoảng vào II khi dừng. Với cầu trục, hệ **thường xuyên làm việc ở góc phần tư IV** — và đó là nơi năng lượng dội về.

Lượng năng lượng đó không nhỏ và không thoáng qua. Hạ một tải nặng từ độ cao lớn nghĩa là **toàn bộ thế năng của tải chuyển thành điện năng** chảy về tụ DC bus, trong suốt thời gian hạ. Tụ không có khả năng chứa lượng đó, nên nếu không có đường thoát, điện áp DC bus dâng lên và biến tần **cắt vì quá áp** — đúng vào lúc tải đang lơ lửng.

Vì vậy với cầu trục, **bộ hãm và điện trở xả không phải tùy chọn mà là bắt buộc**. Đây là điểm khác biệt căn bản so với các ứng dụng đã bàn trong chuỗi bài này ([xem bài lỗi quá áp](/loi-qua-ap-thap-ap-bien-tan/)).

### Vì sao cần encoder

Yêu cầu "giữ tải đứng yên mà không trôi" đòi hỏi **mô-men đầy đủ ở tốc độ bằng 0**.

Chế độ sensorless vector **ước lượng** tốc độ rotor từ dòng và áp. Ước lượng đó rất tốt ở dải tốc độ làm việc, nhưng **mất độ tin cậy khi tần số tiến về 0** — vì ở đó tín hiệu điện gần như không còn thông tin về tốc độ.

Với cầu trục, đó chính là thời điểm nguy hiểm nhất: khoảnh khắc chuyển giao giữa phanh cơ và mô-men điện. Nếu biến tần không biết chắc trục đang đứng yên hay đang bắt đầu trôi, nó không thể bù đúng.

Lắp **encoder** trên trục và dùng **vector vòng kín** giải quyết việc này: tốc độ được **đo thật**, biến tần biết chính xác trục đang ở đâu và giữ được mô-men ngay cả ở 0 Hz ([xem so sánh chế độ điều khiển](/che-do-dieu-khien-vf-vector/)).

---

## Cấu tạo hệ nâng hạ: những thành phần bắt buộc

| Thành phần | Bắt buộc? | Vai trò |
|---|---|---|
| **Biến tần loại nâng hạ (hoisting)** | **Có** | Có sẵn logic phối hợp phanh, chống trôi |
| **Bộ hãm (braking unit)** | **Có** | Dẫn năng lượng dội về ra điện trở |
| **Điện trở xả đủ công suất** | **Có** | Tính theo tải và **thời gian hạ**, không chỉ theo công suất |
| **Encoder + card PG** | **Rất nên** | Mô-men giữ ở tốc độ 0 |
| **Phanh cơ (phanh điện từ)** | **Có** | Giữ tải khi mất điện — **không thể thay bằng điện tử** |
| **Công tắc hành trình trên/dưới** | **Có** | Giới hạn vật lý |
| **Chức năng STO** | **Rất nên** | Dừng an toàn ([xem bài STO](/safe-torque-off-bien-tan/)) |
| **Chống quá tải (load cell hoặc theo dòng)** | **Có** | Không cho nâng quá tải trọng |

**Về điện trở xả — điểm hay tính sai nhất.** Với máy ly tâm, điện trở xả chỉ làm việc trong vài giây lúc dừng. Với cầu trục, nó làm việc **suốt thời gian hạ tải**, có thể là hàng chục giây, lặp lại nhiều lần mỗi giờ.

Vì vậy phải tính theo **chu kỳ làm việc (duty cycle)**: bao nhiêu phần trăm thời gian điện trở đang chịu tải. Chọn điện trở đúng giá trị ohm nhưng **thiếu công suất chịu nhiệt** là lỗi phổ biến, và hậu quả là điện trở nóng đỏ, cháy, hoặc bộ hãm hỏng ([xem chi tiết](/cai-tang-giam-toc-bien-tan/)).

Điện trở xả cầu trục phải đặt ở **vị trí thoáng, cách xa vật liệu dễ cháy**, và tính tới việc nó ở trên cao trong nhà xưởng nóng.

**Về phanh cơ.** Đây là điểm an toàn tuyệt đối không được thỏa hiệp. Phanh điện từ giữ tải khi **mất điện** — tình huống mà biến tần hoàn toàn bất lực. Không có cấu hình điện tử nào thay thế được.

### Logic phối hợp phanh — nơi tai nạn xảy ra

Trình tự đóng/mở phanh phối hợp với mô-men điện là phần tinh tế nhất, và cũng là nơi hay xảy ra sự cố "tải tụt một đoạn rồi mới dừng".

**Trình tự đúng khi bắt đầu nâng:**
1. Biến tần nhận lệnh chạy, **xây dựng từ thông** trong động cơ.
2. Biến tần **sinh đủ mô-men giữ** để đỡ được tải.
3. **Chỉ khi đó mới nhả phanh cơ.**
4. Bắt đầu tăng tốc.

**Trình tự đúng khi dừng:**
1. Giảm tốc về 0.
2. **Giữ mô-men** ở tốc độ 0 trong một khoảng thời gian.
3. **Đóng phanh cơ.**
4. **Chỉ sau khi phanh đã đóng chắc** mới cắt mô-men điện.

Nếu nhả phanh **trước khi** có đủ mô-men, tải sẽ tụt xuống một đoạn — đây chính là hiện tượng "giật tụt" mà nhiều hệ gặp phải. Nếu cắt mô-men **trước khi** phanh đóng, cũng vậy.

Các thông số điều chỉnh trình tự này (thời gian trễ nhả phanh, thời gian trễ đóng phanh, ngưỡng mô-men nhả phanh) có trong biến tần loại nâng hạ và **phải được cài đúng, kiểm chứng bằng thử nghiệm với tải thật**.

---

## Ứng dụng: các cơ cấu và yêu cầu khác nhau

Một cầu trục thường có **ba cơ cấu độc lập**, và yêu cầu của chúng không giống nhau:

**1. Cơ cấu nâng hạ (hoist).** Khắt khe nhất. Cần đủ: điện trở xả, encoder, phanh cơ, chống quá tải, logic phanh. Đây là nơi mọi yêu cầu ở trên áp dụng đầy đủ.

**2. Cơ cấu di chuyển xe con (trolley).** Tải mô-men không đổi, không có thành phần thế năng. Yêu cầu chính là **khởi động và dừng êm để tải không đung đưa**. Đường cong chữ S rất hiệu quả ở đây.

**3. Cơ cấu di chuyển cầu (bridge/long travel).** Tương tự trolley nhưng khối lượng lớn hơn, quán tính lớn hơn. Cần thời gian tăng/giảm tốc dài hơn.

**Vấn đề đung đưa tải (sway).** Khi xe con tăng tốc hoặc dừng đột ngột, tải treo trên cáp sẽ đung đưa như con lắc. Điều này gây mất thời gian chờ ổn định, và nguy hiểm khi làm việc gần người hoặc thiết bị.

Biến tần giải quyết bằng hai mức:
- **Cơ bản:** kéo dài thời gian tăng/giảm tốc và dùng S-curve. Đơn giản, miễn phí, hiệu quả rõ rệt.
- **Nâng cao:** một số biến tần chuyên dụng có **chức năng chống đung đưa (anti-sway)** tính toán theo chiều dài cáp.

**Chức năng nâng tốc độ cao khi tải nhẹ.** Nhiều biến tần nâng hạ có chức năng cho phép chạy nhanh hơn định mức khi cảm nhận tải nhẹ, giúp tăng năng suất. Chỉ dùng khi **nhà sản xuất cơ cấu cho phép** — vượt tốc độ thiết kế của hộp số và tang cuốn là nguy hiểm.

---

## So sánh: điện trở xả hay hoàn năng lượng về lưới?

Với cầu trục hạ tải thường xuyên, lượng năng lượng dội về có thể đáng kể. Có hai cách xử lý:

| Tiêu chí | **Điện trở xả** | **Hoàn năng lượng (AFE)** |
|---|---|---|
| Nguyên lý | Đốt thành nhiệt | **Trả điện về lưới** |
| Chi phí đầu tư | **Thấp** | Cao |
| Tiết kiệm điện | Không | **Có** |
| Toả nhiệt trong nhà xưởng | **Nhiều** | Ít |
| Không gian lắp đặt | Cần chỗ thoáng cho điện trở | Gọn hơn |
| Độ phức tạp | Thấp | Cao hơn |
| Phù hợp | **Đa số cầu trục** | Hạ tải nặng, liên tục, nhiều giờ/ngày |

Với **đa số cầu trục nhà xưởng** — dùng gián đoạn, tải vừa — điện trở xả là lựa chọn hợp lý và kinh tế. Phương án hoàn năng lượng chỉ đáng cân nhắc với các cơ cấu **hạ tải nặng liên tục nhiều giờ mỗi ngày**, ví dụ cẩu cảng hoặc thang nâng cao tầng chạy suốt ca ([xem bài chuyên sâu](/bien-tan-hoan-nang-luong/)).

---

## Sai lầm thường gặp

1. **Không lắp điện trở xả** cho cơ cấu nâng hạ — lỗi quá áp mỗi lần hạ tải.
2. **Chọn điện trở đúng ohm nhưng thiếu công suất chịu nhiệt** — không tính chu kỳ làm việc khi hạ.
3. **Dùng sensorless vector thay vì vector có encoder** cho cơ cấu nâng — không giữ được mô-men ở 0 Hz.
4. **Cài sai trình tự phanh** — tải tụt một đoạn khi bắt đầu nâng hoặc khi dừng.
5. **Coi phanh điện tử thay được phanh cơ** — mất điện là mất tải.
6. **Đặt điện trở xả ở nơi kín, gần vật liệu dễ cháy.**
7. **Dùng biến tần đa năng thông thường** thay vì loại có chức năng nâng hạ.
8. **Bỏ qua chống quá tải** — nâng vượt tải trọng thiết kế.
9. **Không thử nghiệm với tải thật** ở đủ các mức trước khi bàn giao.
10. **Bật chức năng chạy nhanh khi tải nhẹ** mà nhà sản xuất cơ cấu không cho phép.
11. **Không có công tắc hành trình** hoặc lắp nhưng không kiểm tra định kỳ.
12. **Đặt thời gian tăng/giảm tốc quá ngắn** cho xe con — tải đung đưa mạnh.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **biến tần loại nâng hạ** có sẵn logic phối hợp phanh và chống trôi tải.
- ✅ **Tính chọn điện trở xả và bộ hãm theo chu kỳ làm việc thực tế**, không chỉ theo công suất động cơ.
- ✅ Tư vấn **encoder và card PG** cho cơ cấu nâng cần mô-men giữ ở tốc độ 0.
- ✅ Hỗ trợ **cài đặt trình tự phanh và quy trình thử nghiệm với tải** trước khi đưa vào sử dụng.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá hệ nâng hạ

Gửi cho chúng tôi: **tải trọng nâng · chiều cao nâng · công suất động cơ từng cơ cấu (nâng, xe con, cầu) · tần suất và thời gian hạ tải mỗi giờ · có sẵn encoder chưa · yêu cầu an toàn của nhà máy.**

**→ [Liên hệ nhận tư vấn cầu trục](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Vì sao cầu trục bắt buộc phải có điện trở xả?**
Vì khi hạ tải, **trọng lực kéo động cơ quay**, biến động cơ thành máy phát bơm năng lượng ngược về DC bus **liên tục trong suốt quá trình hạ**. Không có đường thoát thì biến tần sẽ cắt vì quá áp.

**Tính điện trở xả cho cầu trục thế nào?**
Theo **giá trị ohm khuyến nghị của hãng** và **công suất chịu nhiệt tính theo chu kỳ làm việc** — bao nhiêu phần trăm thời gian điện trở đang chịu tải khi hạ, không chỉ theo công suất động cơ.

**Cầu trục có cần encoder không?**
Cơ cấu **nâng hạ rất nên có**, vì cần **mô-men giữ ở tốc độ 0**. Sensorless vector không đảm bảo được điều này một cách tin cậy.

**Biến tần có thay được phanh cơ không?**
**Không.** Phanh điện từ giữ tải khi **mất điện** — tình huống biến tần hoàn toàn bất lực. Đây là yêu cầu an toàn không thỏa hiệp.

**Vì sao tải bị tụt một đoạn khi bắt đầu nâng?**
Do **nhả phanh cơ trước khi biến tần sinh đủ mô-men giữ**. Cần cài lại trình tự: xây từ thông → đủ mô-men → mới nhả phanh.

**Làm sao giảm đung đưa tải khi di chuyển?**
**Kéo dài thời gian tăng/giảm tốc và bật đường cong chữ S.** Một số biến tần chuyên dụng còn có chức năng chống đung đưa tính theo chiều dài cáp.

**Có nên dùng biến tần đa năng cho cầu trục không?**
Không nên. **Biến tần loại nâng hạ** có sẵn logic phối hợp phanh, chống trôi tải và các bảo vệ chuyên biệt mà loại đa năng không có.

**Khi nào nên dùng hoàn năng lượng thay điện trở xả?**
Khi cơ cấu **hạ tải nặng liên tục nhiều giờ mỗi ngày** — ví dụ cẩu cảng, thang nâng cao tầng chạy suốt ca. Với cầu trục nhà xưởng dùng gián đoạn, điện trở xả kinh tế hơn.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /che-do-dieu-khien-vf-vector/, /cai-tang-giam-toc-bien-tan/, /loi-qua-ap-thap-ap-bien-tan/, /safe-torque-off-bien-tan/, /bien-tan-hoan-nang-luong/, /lien-he/. -->
