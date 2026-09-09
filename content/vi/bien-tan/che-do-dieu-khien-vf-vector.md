<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 4) — Thông tin
URL SLUG   : /che-do-dieu-khien-vf-vector/
TỪ KHÓA    : v/f và vector | điều khiển vector biến tần | sensorless vector | chế độ điều khiển biến tần | mô men khởi động
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 20/30 trong chuỗi biến tần.
-->

TITLE TAG   : V/f Hay Vector? Chọn Chế Độ Điều Khiển Biến Tần Đúng Ứng Dụng
META (156)  : So sánh V/f, sensorless vector và vector có encoder: khác nhau ở đâu, mô-men thấp tốc ra sao, khi nào bắt buộc dùng vector và cách cài đúng.

H1          : Chế Độ Điều Khiển Biến Tần: V/f Và Vector

---

## Cùng một biến tần, hai cách điều khiển khác hẳn nhau

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Khi cài đặt biến tần, có một thông số quyết định gần như toàn bộ chất lượng vận hành: **chế độ điều khiển (control mode)**. Cùng một biến tần, cùng một động cơ, đổi thông số này là hành vi của hệ thay đổi rõ rệt.

Các chế độ phổ biến trên biến tần công nghiệp hiện nay:

- **V/f (Volts per Hertz)** — điều khiển vô hướng, đơn giản nhất.
- **Sensorless Vector Control (SVC)** — điều khiển vector không cần encoder.
- **Vector có phản hồi (Closed-loop Vector / FVC)** — vector kèm encoder.
- **Điều khiển mô-men (Torque control)** — điều khiển trực tiếp lực kéo thay vì tốc độ.

Chọn sai chế độ dẫn tới hai kiểu lãng phí trái ngược nhau: hoặc **máy không đủ mô-men khi khởi động** vì để V/f cho tải nặng, hoặc **tốn thời gian auto-tune và phức tạp hóa hệ thống** vì dùng vector cho một cái quạt hút.

Bài này giải thích sự khác nhau ở mức nguyên lý đủ để chọn đúng, và đưa ra tiêu chí quyết định cụ thể.

> **Không chắc nên để V/f hay vector?** Gửi **mô tả tải · nhãn động cơ · model biến tần** → [Nhận tư vấn chế độ điều khiển](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vf-ratio.svg)


Đây là bài **20/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: hai cách nhìn về động cơ

### Chế độ V/f — giữ tỷ số điện áp trên tần số

Ý tưởng của V/f xuất phát từ một thực tế vật lý: **từ thông trong động cơ tỷ lệ với điện áp chia cho tần số**. Muốn động cơ giữ được khả năng sinh mô-men khi đổi tốc độ, phải giữ cho từ thông không đổi — tức là **giữ tỷ số V/f không đổi**.

Vì vậy biến tần chạy V/f làm một việc rất đơn giản: khi tăng tần số, tăng điện áp theo cùng tỷ lệ. Ví dụ với động cơ 380V/50Hz, ở 25Hz biến tần cấp khoảng 190V.

Đặc điểm quan trọng: **biến tần không biết động cơ đang chịu tải bao nhiêu**. Nó cứ cấp điện áp theo bảng đã định, và động cơ tự xoay xở. Đây là điều khiển **vòng hở, vô hướng** — không đo, không phản hồi, không mô hình hóa.

Hệ quả:

- Rất **ổn định và khó sai**, chạy được với hầu hết động cơ, kể cả nhiều động cơ song song.
- Không cần biết chính xác tham số động cơ, không cần auto-tune.
- Nhưng **mô-men ở tốc độ rất thấp yếu**, vì ở tần số thấp phần điện áp bị "ăn" bởi điện trở cuộn dây trở nên đáng kể so với tổng điện áp cấp.
- **Độ chính xác tốc độ kém** khi tải thay đổi — tải nặng lên thì động cơ trượt nhiều hơn, tốc độ thực tụt xuống.

Để bù phần mô-men yếu ở tốc độ thấp, biến tần có thông số **torque boost (bù mô-men)** — nâng thêm điện áp ở vùng tần số thấp. Đặt boost quá cao gây **nóng động cơ** khi chạy không tải, nên đây là một sự đánh đổi phải cân.

Ngoài đường V/f tuyến tính, biến tần còn có các **đường cong V/f dạng bình phương** dành riêng cho bơm và quạt — giảm điện áp mạnh hơn ở tốc độ thấp để tiết kiệm điện, tận dụng đặc tính mô-men cản của tải ly tâm ([xem bài tiết kiệm điện](/bien-tan-tiet-kiem-dien/)).

### Chế độ vector — mô hình hóa và tách dòng

Điều khiển vector tiếp cận theo hướng hoàn toàn khác. Biến tần **xây dựng một mô hình toán của động cơ** trong bộ vi xử lý, và dựa vào đó tách dòng stator thành hai thành phần:

- **Thành phần tạo từ thông** (giữ cho động cơ được "kích thích").
- **Thành phần tạo mô-men** (thực sự sinh lực kéo).

Tách được hai thành phần này, biến tần có thể **điều khiển mô-men gần như trực tiếp và tức thời**, giống như điều khiển một động cơ một chiều — vốn là loại có đặc tính mô-men lý tưởng.

Để mô hình chạy đúng, biến tần cần biết các **tham số điện thực của động cơ**: điện trở stator, điện trở rotor, điện cảm rò, dòng không tải. Đó chính là lý do phải chạy **auto-tune** ([xem quy trình cài đặt](/cai-dat-thong-so-bien-tan/)).

Kết quả đạt được:

- **Mô-men khởi động lớn ngay ở tần số rất thấp** — đây là ưu điểm quyết định.
- **Giữ tốc độ ổn định khi tải thay đổi**, vì biến tần liên tục ước lượng và bù.
- **Đáp ứng nhanh** với biến động tải đột ngột.
- Có thể **giới hạn mô-men** để bảo vệ cơ khí.

Đổi lại: cần auto-tune, cần khai báo động cơ chính xác, và **về nguyên tắc chỉ điều khiển một động cơ trên một biến tần** — vì mô hình được xây cho một động cơ cụ thể.

### Vector có encoder

Sensorless vector **ước lượng** tốc độ rotor từ dòng và áp. Ước lượng đó rất tốt trong phần lớn dải làm việc, nhưng **kém dần khi tần số tiến về 0**, vì ở đó tín hiệu điện gần như không còn thông tin về tốc độ.

Lắp **encoder** trên trục động cơ và đưa xung về biến tần thì tốc độ không còn phải ước lượng nữa — nó được **đo thật**. Nhờ đó đạt được:

- **Mô-men đầy đủ ở tốc độ bằng 0** (giữ trục đứng yên mà vẫn có lực).
- Độ chính xác tốc độ cao nhất.
- Điều khiển mô-men thực sự tin cậy.

Đây là yêu cầu bắt buộc với cầu trục, thang nâng, máy cuốn/xả liệu và các hệ đồng bộ nhiều trục.

---

## Cấu tạo bộ thông số theo từng chế độ

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-thongso.svg)


| Nhóm thông số | V/f | Sensorless vector | Vector có encoder |
|---|---|---|---|
| Khai báo động cơ cơ bản | Cần, mức vừa | **Cần chính xác** | **Cần chính xác** |
| Auto-tune | Không cần | **Nên chạy** | **Bắt buộc** |
| Đường cong V/f | **Có, chọn được** | Không dùng | Không dùng |
| Torque boost | **Có** | Không cần | Không cần |
| Giới hạn mô-men | Hạn chế | **Có** | **Có** |
| Card encoder (PG card) | Không | Không | **Bắt buộc** |
| Hệ số ổn định tốc độ / bù trượt | Bù trượt đơn giản | Vòng điều khiển tốc độ | Vòng tốc độ + vòng dòng |
| Nhiều động cơ song song | **Được** | Không nên | Không |

Một lưu ý thực tế: nhiều biến tần đặt mặc định là **V/f**. Nếu bạn mua biến tần cho một máy cần mô-men khởi động lớn mà không đổi chế độ, máy sẽ ì ạch dù thiết bị hoàn toàn đủ khả năng — chỉ vì một thông số chưa đổi.

---

## Ứng dụng: chọn chế độ theo loại máy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bangtai.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vf-vector.svg)

**Dùng V/f khi:**

- Tải là **bơm ly tâm hoặc quạt** — mô-men cản tăng theo bình phương tốc độ, ở tốc độ thấp gần như không cần mô-men ([xem bài quạt hút](/bien-tan-cho-quat-hut/)).
- **Một biến tần kéo nhiều động cơ** song song.
- Máy đơn giản, chỉ cần đổi tốc độ, không yêu cầu chính xác.
- Cần **độ tin cậy cao và cài đặt nhanh**, ít phụ thuộc tham số.
- Không tháo được tải để auto-tune và động cơ không rõ thông số.

**Dùng sensorless vector khi:**

- **Băng tải chở nặng**, cần khởi động có tải.
- **Máy trộn, máy nhào, máy nghiền** — mô-men cản lớn ngay từ đầu.
- **Máy ép, máy đùn** — tải thay đổi mạnh trong chu kỳ.
- Cần **giữ tốc độ ổn định** khi tải biến động.
- Cần **giới hạn mô-men** để bảo vệ cơ cấu.
- Máy công cụ, trục chính tốc độ thấp.

**Dùng vector có encoder khi:**

- **Cầu trục, thang nâng, tời** — cần mô-men giữ ở tốc độ 0.
- **Máy cuốn/xả liệu** cần điều khiển sức căng.
- **Hệ nhiều trục cần đồng bộ** chính xác.
- Yêu cầu **điều khiển mô-men thay vì tốc độ**.
- Định vị chính xác.

### Tình huống thực tế hay gặp

Một khách hàng lắp biến tần cho **máy trộn** và thấy máy không khởi động nổi khi trong thùng còn nguyên liệu, dù biến tần cùng công suất động cơ. Lỗi báo quá dòng, hoặc động cơ ù mà không quay.

Phản xạ thường thấy là **đổi biến tần lớn hơn**. Nhưng nguyên nhân thật là chế độ đang để **V/f**, vốn yếu mô-men ở tần số thấp — đúng vùng mà máy trộn cần lực nhất. Chuyển sang **sensorless vector và chạy auto-tune** giải quyết được, không tốn thêm thiết bị.

Ngược lại, một khách khác lắp biến tần cho **quạt hút bụi** và cố chạy vector, mất công auto-tune, gặp trục trặc vì hệ có hai quạt chung một biến tần. Ở đây **V/f với đường cong bình phương** mới là lựa chọn đúng — đơn giản hơn và tiết kiệm điện hơn.

---

## So sánh trực tiếp ba chế độ

| Tiêu chí | **V/f** | **Sensorless Vector** | **Vector + Encoder** |
|---|---|---|---|
| Nguyên lý | Giữ tỷ số V/f | Mô hình động cơ, ước lượng tốc độ | Mô hình động cơ, đo tốc độ thật |
| Mô-men ở tần số rất thấp | Yếu | **Mạnh** | **Mạnh, kể cả ở 0 Hz** |
| Độ chính xác tốc độ | Thấp | Khá | **Cao nhất** |
| Đáp ứng khi tải thay đổi | Chậm | Nhanh | **Nhanh nhất** |
| Cần auto-tune | Không | Nên | **Bắt buộc** |
| Cần phần cứng thêm | Không | Không | **Card encoder + encoder** |
| Nhiều động cơ song song | **Được** | Không nên | Không |
| Độ phức tạp cài đặt | **Thấp nhất** | Trung bình | Cao |
| Chi phí tổng | **Thấp nhất** | Thấp | Cao |
| Phù hợp | Bơm, quạt, tải nhẹ | Băng tải, máy trộn, máy ép | Cầu trục, cuốn liệu, đồng bộ |

**Nguyên tắc chọn ngắn gọn:** tải ly tâm (bơm, quạt) → **V/f**; tải cần mô-men khi khởi động → **sensorless vector**; tải nâng hạ hoặc cần giữ trục ở tốc độ 0 → **vector có encoder**.

---

## Sai lầm thường gặp

1. **Để mặc định V/f cho tải nặng** rồi kết luận biến tần thiếu công suất.
2. **Tăng torque boost quá cao** để bù mô-men — động cơ nóng khi chạy nhẹ tải.
3. **Chạy vector cho nhiều động cơ song song** — mô hình sai, hoạt động bất thường.
4. **Chọn vector nhưng bỏ qua auto-tune** — mất gần hết ưu điểm.
5. **Chạy auto-tune động khi tải còn lắp** — nguy hiểm và kết quả sai lệch.
6. **Dùng vector cho quạt và bơm** — phức tạp không cần thiết, mất luôn lợi ích của đường cong V/f bình phương.
7. **Kỳ vọng sensorless vector giữ mô-men ở đúng 0 Hz** — cần encoder mới làm được tin cậy.
8. **Khai báo nhãn động cơ sai** rồi dùng vector — mô hình xây trên số liệu sai thì kết quả cũng sai.
9. **Đổi động cơ nhưng không auto-tune lại** trong khi vẫn để chế độ vector.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **chọn chế độ điều khiển theo loại tải thật**, không mặc định một công thức.
- ✅ Hỗ trợ **quy trình auto-tune an toàn**, kể cả khi không tháo được tải.
- ✅ Tư vấn **encoder và card PG** khi ứng dụng thực sự cần vector vòng kín.
- ✅ Cài sẵn thông số theo nhãn động cơ khách gửi trước khi giao [biến tần](/bien-tan-la-gi/).

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **ảnh nhãn động cơ · model biến tần · mô tả tải (loại máy, có khởi động khi có tải không) · yêu cầu về độ chính xác tốc độ hoặc mô-men giữ.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**V/f và vector khác nhau thế nào?**
**V/f** giữ tỷ số điện áp/tần số cố định, đơn giản và ổn định nhưng yếu mô-men ở tốc độ thấp. **Vector** dựng mô hình động cơ để tách dòng tạo từ thông và dòng tạo mô-men, nhờ đó có mô-men mạnh ngay ở tần số rất thấp.

**Khi nào bắt buộc dùng vector?**
Khi cần **mô-men lớn lúc khởi động có tải** (máy trộn, máy nghiền, băng tải nặng), cần giữ tốc độ ổn định khi tải thay đổi, hoặc cần giới hạn mô-men.

**Sensorless vector có giữ được mô-men ở 0 Hz không?**
Không tin cậy. Muốn có **mô-men giữ ở tốc độ 0**, cần **vector có encoder**.

**Chạy vector có bắt buộc auto-tune không?**
Với vector vòng kín thì **bắt buộc**. Với sensorless vector thì rất nên chạy, vì không auto-tune sẽ mất phần lớn ưu điểm.

**Một biến tần kéo nhiều động cơ thì chọn chế độ nào?**
**V/f**. Chế độ vector xây mô hình cho một động cơ cụ thể nên không phù hợp khi chạy song song nhiều động cơ.

**Bơm và quạt nên để chế độ gì?**
**V/f**, và nên chọn **đường cong V/f dạng bình phương** để tiết kiệm điện, vì mô-men cản của tải ly tâm giảm mạnh ở tốc độ thấp.

**Torque boost là gì, đặt bao nhiêu?**
Là chức năng **nâng thêm điện áp ở tần số thấp** để bù mô-men trong chế độ V/f. Đặt vừa đủ để khởi động được — quá cao sẽ làm **động cơ nóng khi chạy nhẹ tải**.

**Đổi động cơ khác có cần cài lại không?**
Có. Phải **khai báo lại nhãn động cơ** và **chạy lại auto-tune** nếu đang dùng chế độ vector.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /cai-dat-thong-so-bien-tan/, /bien-tan-tiet-kiem-dien/, /bien-tan-cho-quat-hut/, /lien-he/. -->
