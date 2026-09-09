<!--
LOẠI TRANG : Bài xử lý sự cố (chuỗi biến tần — tầng 5) — Thông tin
URL SLUG   : /loi-qua-ap-thap-ap-bien-tan/
TỪ KHÓA    : lỗi quá áp biến tần | lỗi thấp áp biến tần | biến tần báo ov | biến tần báo lv | mất pha đầu vào biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 27/30 trong chuỗi biến tần.
-->

TITLE TAG   : Lỗi Quá Áp (OV) Và Thấp Áp (LV) Biến Tần – Nguyên Nhân, Cách Xử Lý
META (156)  : Biến tần báo OV khi dừng hoặc LV khi khởi động? Giải thích DC bus, phân biệt hai lỗi, cách xử lý mất pha, sụt áp lưới và khi nào cần điện trở xả.

H1          : Lỗi Quá Áp Và Thấp Áp Trên Biến Tần

---

## Hai lỗi trái ngược, cùng nói về một thứ: DC bus

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan-loi.svg)


Quá áp (**OV, OU**) và thấp áp (**LV, UV, LU**) là hai mã lỗi đối lập nhau, nhưng cả hai đều báo về **điện áp trên tụ DC bus** — trái tim của biến tần.

Nhắc lại nguyên lý: biến tần chỉnh lưu điện lưới xoay chiều thành một chiều, lưu trên **dàn tụ DC bus**, rồi nghịch lưu ra xoay chiều tần số thay đổi. Toàn bộ năng lượng đi qua điểm này ([xem nguyên lý hoạt động](/nguyen-ly-hoat-dong-bien-tan/)).

Biến tần giám sát điện áp DC bus rất chặt, vì:

- **Quá cao** → tụ và IGBT có thể bị đánh thủng.
- **Quá thấp** → mạch điều khiển không hoạt động tin cậy, IGBT đóng cắt không đủ nhanh, dễ hỏng.

Hai lỗi này có nguyên nhân rất khác nhau, nhưng đều **hiếm khi là do biến tần hỏng**. Chúng gần như luôn phản ánh một vấn đề bên ngoài: cách vận hành, tải, hoặc chất lượng nguồn điện.

> **Biến tần báo OV hoặc LV lặp lại?** Gửi **mã lỗi · lỗi xảy ra khi nào · tình trạng lưới** → [Nhận hỗ trợ chẩn đoán](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-loi.svg)


Đây là bài **27/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: điện áp DC bus dâng và tụt vì đâu

### Vì sao DC bus dâng cao (quá áp)

Có ba nguồn làm DC bus dâng lên:

**1. Năng lượng dội về từ động cơ (nguyên nhân số một).** Khi biến tần giảm tần số nhanh hơn tốc độ mà tải tự chậm lại, động cơ **trở thành máy phát**. Động năng của khối quay chuyển thành điện năng, chảy ngược qua IGBT về tụ DC bus.

Biến tần thông thường **không trả điện ngược lên lưới**. Năng lượng đó không có chỗ đi, nên tích lại trên tụ và làm điện áp dâng lên tới ngưỡng cắt.

**2. Tải kéo động cơ quay.** Không cần giảm tốc, chỉ cần tải chủ động kéo:
- **Cầu trục, thang nâng khi hạ tải** — trọng lực kéo động cơ quay nhanh hơn tần số đặt.
- **Băng tải nghiêng xuống** có tải nặng.
- **Quạt bị gió thổi** hoặc bơm bị dòng nước đẩy.

Trong các trường hợp này, năng lượng dội về **xuất hiện liên tục** chứ không chỉ lúc dừng.

**3. Điện áp lưới quá cao.** Lưới vượt ngưỡng cho phép, hoặc có **xung áp** do đóng cắt tụ bù, do tải lớn gần đó ngừng đột ngột, do sét lan truyền.

### Vì sao DC bus tụt thấp (thấp áp)

**1. Mất một pha đầu vào (nguyên nhân số một).** Cầu chì đứt, tiếp điểm contactor cháy, cực đấu lỏng, đứt cáp. Chỉnh lưu còn hai pha vẫn tạo được điện áp một chiều, nhưng **thấp hơn và nhấp nhô mạnh** — biến tần báo thấp áp, đôi khi kèm mã mất pha riêng.

**2. Sụt áp lưới.** Lưới yếu, cuối đường dây, hoặc có tải lớn khác khởi động trực tiếp gần đó kéo tụt điện áp trong vài giây.

**3. Tiếp xúc lỏng.** Cực đấu không siết đủ lực, contactor rỗ tiếp điểm, aptomat mòn. Đây là nguyên nhân của rất nhiều lỗi LV **ngẫu nhiên, không quy luật**, và cũng là nguyên nhân dễ bỏ sót nhất.

**4. Cáp cấp nguồn quá nhỏ hoặc quá dài** — sụt áp trên đường dây khi mang tải ([xem chọn cáp](/chon-cap-aptomat-cho-bien-tan/)).

**5. Điện trở nạp (soft-charge) hoặc contactor nội bộ hỏng.** Nhiều biến tần có mạch hạn dòng nạp tụ khi cấp nguồn. Nếu mạch này hỏng, DC bus không lên đủ.

**6. Tụ DC bus đã già.** Sau nhiều năm, tụ mất dần điện dung, không giữ được điện áp khi tải nặng.

---

## Cấu tạo chẩn đoán: xác định lỗi theo thời điểm

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-dauday.svg)


### Quá áp (OV) — bảng tra

| Xảy ra khi | Nguyên nhân | Cách xử lý |
|---|---|---|
| **Khi giảm tốc / dừng** | Năng lượng dội về từ quán tính | **Kéo dài thời gian giảm tốc**; hoặc chuyển sang chạy trớn tự do |
| **Khi dừng, nhưng bắt buộc phải dừng nhanh** | Quán tính lớn | **Lắp điện trở xả và bộ hãm** |
| **Khi hạ tải (cầu trục, thang nâng)** | Tải thế năng kéo động cơ | **Bắt buộc có bộ hãm + điện trở xả** |
| **Khi chạy ổn định** | Lưới cao, hoặc tải kéo động cơ | Đo điện áp lưới; kiểm tra chiều tác động của tải |
| **Ngẫu nhiên, kèm thiết bị khác bị ảnh hưởng** | **Xung áp do đóng cắt tụ bù** | Lắp **cuộn kháng đầu vào** [xem chi tiết](/cuon-khang-loc-nhieu-bien-tan/) |
| **Chỉ vào ban đêm, giờ thấp điểm** | Điện áp lưới dâng khi non tải | Đo và ghi nhật ký điện áp; xem xét cuộn kháng vào |

### Thấp áp (LV) — bảng tra

| Xảy ra khi | Nguyên nhân | Cách xử lý |
|---|---|---|
| **Ngay khi cấp nguồn** | Mất pha, cầu chì đứt, mạch nạp hỏng | Đo điện áp **cả ba pha ngay tại cực biến tần** |
| **Khi khởi động động cơ** | Sụt áp do dòng khởi động; cáp nhỏ | Kiểm tra tiết diện cáp, kéo dài thời gian tăng tốc |
| **Khi tải nặng** | Lưới yếu, cáp nhỏ, tụ già | Đo sụt áp khi mang tải |
| **Ngẫu nhiên, không quy luật** | **Tiếp xúc lỏng**, contactor rỗ | **Siết lại toàn bộ cực đấu**, kiểm tra contactor |
| **Khi thiết bị lớn khác khởi động** | Sụt áp lưới chung | Khởi động mềm cho tải kia, hoặc tách nguồn |
| **Kèm biến tần chạy yếu, nóng** | **Tụ DC bus đã già** | Kiểm tra tụ, cân nhắc [sửa hay thay](/sua-hay-thay-bien-tan/) |
| **Xuất hiện tăng dần theo tháng** | Tụ suy giảm, tiếp xúc oxy hóa | Đưa vào [lịch bảo trì](/bao-tri-bien-tan-dinh-ky/) |

### Bốn phép đo cần làm

1. **Đo điện áp ba pha ngay tại cực đấu của biến tần** (không phải tại tủ tổng). Chênh lệch giữa hai điểm cho biết sụt áp trên đường dây và tiếp xúc.
2. **Đo cả khi không tải và khi mang tải nặng nhất.** Sụt áp chỉ lộ ra khi có tải.
3. **Đo điện áp DC bus** nếu biến tần có hiển thị — so với giá trị lý thuyết.
4. **Ghi nhật ký điện áp theo giờ trong vài ngày** nếu lỗi xảy ra theo chu kỳ thời gian.

---

## Ứng dụng: xử lý theo tình huống thực tế

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-suachua.svg)


**Máy ly tâm, máy nghiền báo OV mỗi lần dừng.** Quán tính rất lớn. Nếu quy trình không yêu cầu dừng nhanh, kéo dài thời gian giảm tốc là đủ. Nếu bắt buộc dừng trong thời gian xác định, **phải có điện trở xả** — không có cách miễn phí nào thay thế ([xem bài tăng giảm tốc](/cai-tang-giam-toc-bien-tan/)).

**Quạt hút lớn báo OV khi dừng.** Giải pháp đơn giản nhất là **chuyển sang chạy trớn tự do**. Quạt không cần dừng dứt điểm ([xem bài quạt](/bien-tan-cho-quat-hut/)).

**Cầu trục báo OV khi hạ hàng.** Đây không phải chuyện chỉnh thông số. Tải thế năng sinh năng lượng dội về **liên tục trong suốt quá trình hạ**. Bắt buộc phải có **bộ hãm và điện trở xả đủ công suất**, tính theo thời gian hạ và khối lượng tải.

**Cả xưởng báo OV cùng lúc vào một thời điểm nhất định trong ngày.** Dấu hiệu rất điển hình của **tụ bù đóng cắt**. Mỗi lần dàn tụ bù đóng, một xung áp lan khắp lưới nội bộ. Xử lý bằng **cuộn kháng đầu vào** cho từng biến tần, và xem lại chế độ vận hành của tủ bù.

**Biến tần báo LV mỗi sáng khi khởi động ca.** Thường do **sụt áp lưới giờ cao điểm** khi cả xưởng cùng khởi động, hoặc do **tiếp xúc oxy hóa qua đêm ẩm**. Đo điện áp tại cực biến tần vào đúng thời điểm đó, và siết lại toàn bộ cực đấu.

**Biến tần báo LV ngẫu nhiên vài lần một tuần.** Ưu tiên số một: **siết lại tất cả cực đấu động lực và kiểm tra contactor**. Đây là nguyên nhân rất phổ biến và rất rẻ để loại trừ.

---

## So sánh hai lỗi

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)


| Tiêu chí | **Quá áp (OV)** | **Thấp áp (LV)** |
|---|---|---|
| DC bus | Vượt ngưỡng trên | Dưới ngưỡng dưới |
| Thời điểm điển hình | **Khi giảm tốc, khi hạ tải** | **Khi cấp nguồn, khi tải nặng** |
| Nguyên nhân số một | Năng lượng dội về từ quán tính | **Mất pha đầu vào** |
| Liên quan tới lưới | Lưới cao, xung từ tụ bù | Lưới yếu, sụt áp |
| Giải pháp miễn phí | Kéo dài giảm tốc, chạy trớn | Siết cực đấu |
| Giải pháp phần cứng | **Điện trở xả + bộ hãm** | Nâng tiết diện cáp, sửa nguồn |
| Phòng ngừa từ lưới | **Cuộn kháng đầu vào** | Ổn áp, cải tạo lưới, cáp đủ lớn |
| Có phải do biến tần hỏng? | Hiếm khi | Đôi khi (tụ già, mạch nạp) |

---

## Sai lầm thường gặp

1. **Xử lý OV bằng cách mua biến tần lớn hơn** — sai hướng hoàn toàn, vì vấn đề là năng lượng dội về chứ không phải thiếu công suất.
2. **Bật chống quá áp tự động cho dây chuyền cần đồng bộ** — hết báo lỗi nhưng thời gian dừng trở nên không xác định.
3. **Bỏ qua bộ hãm cho cầu trục** — không có cách nào chỉnh thông số thay thế được.
4. **Chỉ đo điện áp ở tủ tổng** khi chẩn đoán LV, không đo tại cực biến tần.
5. **Chỉ đo khi không tải** — sụt áp không lộ ra.
6. **Không siết lại cực đấu định kỳ** — nguồn gốc của rất nhiều lỗi LV ngẫu nhiên.
7. **Bỏ qua tụ bù đóng cắt** khi cả xưởng cùng báo OV theo giờ.
8. **Lắp điện trở xả trong tủ kín** không thông gió ([xem bố trí tủ](/lap-bien-tan-trong-tu-dien/)).
9. **Hạ ngưỡng bảo vệ thấp áp** để chạy tiếp trên lưới yếu — IGBT làm việc trong điều kiện nguy hiểm.
10. **Không thay tụ DC bus theo tuổi thọ** trên máy chạy liên tục nhiều năm.

---

## Cam kết tại HOANTRANTDH

- ✅ Hỗ trợ **phân biệt lỗi do lưới, do tải hay do biến tần** trước khi đề xuất mua thiết bị.
- ✅ Tính chọn **điện trở xả và bộ hãm** đúng giá trị, công suất theo model và chu kỳ làm việc.
- ✅ Tư vấn **cuộn kháng đầu vào** cho xưởng có tụ bù đóng cắt hoặc lưới nhiều xung.
- ✅ Cung cấp đồng bộ [biến tần](/bien-tan-la-gi/), cuộn kháng, điện trở xả và phụ kiện tủ điện.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ chẩn đoán & báo giá

Gửi cho chúng tôi: **mã lỗi · model biến tần · lỗi xảy ra khi nào (dừng / khởi động / chạy / theo giờ trong ngày) · loại tải và quán tính · điện áp đo được tại cực biến tần · xưởng có tụ bù đóng cắt không.**

**→ [Liên hệ hỗ trợ xử lý lỗi OV/LV](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lỗi OV trên biến tần là gì?**
Là lỗi **quá áp trên tụ DC bus**. Nguyên nhân phổ biến nhất là **năng lượng dội về từ động cơ** khi giảm tốc quá nhanh hoặc khi tải kéo động cơ quay.

**Lỗi LV trên biến tần là gì?**
Là lỗi **thấp áp trên DC bus**. Nguyên nhân hàng đầu là **mất một pha đầu vào**, sau đó là sụt áp lưới và tiếp xúc lỏng.

**Biến tần báo OV mỗi khi dừng, xử lý thế nào?**
Trước hết **kéo dài thời gian giảm tốc**, hoặc chuyển sang **chạy trớn tự do** nếu không cần dừng nhanh. Nếu buộc phải dừng nhanh thì cần **điện trở xả**.

**Cầu trục hạ tải báo OV liên tục thì sao?**
Đây là **tải thế năng**, năng lượng dội về xuất hiện suốt quá trình hạ. **Bắt buộc phải có bộ hãm và điện trở xả**, không thể xử lý bằng thông số.

**Vì sao cả xưởng báo OV vào cùng một thời điểm mỗi ngày?**
Dấu hiệu điển hình của **tụ bù đóng cắt** tạo xung áp trên lưới nội bộ. Xử lý bằng **cuộn kháng đầu vào** và xem lại vận hành tủ bù.

**Biến tần báo LV ngẫu nhiên phải kiểm tra gì đầu tiên?**
**Siết lại toàn bộ cực đấu động lực** và kiểm tra contactor, aptomat. Tiếp xúc lỏng là nguyên nhân rất phổ biến của lỗi LV không theo quy luật.

**Đo điện áp ở đâu để chẩn đoán LV?**
**Ngay tại cực đấu của biến tần**, không phải tại tủ tổng, và phải đo **cả khi đang mang tải nặng nhất** thì sụt áp mới lộ ra.

**Có nên hạ ngưỡng bảo vệ thấp áp để chạy trên lưới yếu không?**
Không nên. Điều đó khiến IGBT làm việc trong điều kiện điện áp không đủ, **tăng nguy cơ hỏng thiết bị**. Nên xử lý ở phía nguồn hoặc cáp.

<!-- SCHEMA: FAQPage + BreadcrumbList + Article. INTERNAL LINK: /bien-tan-la-gi/, /nguyen-ly-hoat-dong-bien-tan/, /loi-bien-tan-thuong-gap/, /cai-tang-giam-toc-bien-tan/, /cuon-khang-loc-nhieu-bien-tan/, /chon-cap-aptomat-cho-bien-tan/, /lap-bien-tan-trong-tu-dien/, /bien-tan-cho-quat-hut/, /bao-tri-bien-tan-dinh-ky/, /sua-hay-thay-bien-tan/, /lien-he/. -->
