<!--
LOẠI TRANG : Bài xử lý sự cố (chuỗi biến tần — tầng 5) — Thông tin
URL SLUG   : /loi-qua-dong-bien-tan/
TỪ KHÓA    : lỗi quá dòng biến tần | biến tần báo oc | lỗi oc biến tần | quá dòng khi tăng tốc | biến tần nhảy oc
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 26/30 trong chuỗi biến tần.
-->

TITLE TAG   : Lỗi Quá Dòng Biến Tần (OC) – Nguyên Nhân Và Cách Khắc Phục
META (156)  : Biến tần báo lỗi quá dòng OC khi tăng tốc, khi chạy hay ngay khi khởi động? Phân biệt ba tình huống, quy trình chẩn đoán và cách xử lý theo từng nguyên nhân.

H1          : Lỗi Quá Dòng Biến Tần (OC)

---

## Quá dòng là lỗi phổ biến nhất — và cũng dễ hiểu sai nhất

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan-loi.svg)


**Quá dòng (Over Current, ký hiệu OC, OC1/OC2/OC3, E.OC…)** là mã lỗi xuất hiện nhiều nhất trên biến tần công nghiệp. Nó có nghĩa là **dòng điện đầu ra vượt ngưỡng cho phép**, và biến tần cắt ngay lập tức để bảo vệ IGBT.

Cần phân biệt quá dòng với quá tải:

- **Quá dòng (OC)** là **tức thời**. Dòng vọt lên rất cao trong khoảnh khắc, biến tần cắt trong vài mili giây. Đây là bảo vệ phần cứng cho IGBT.
- **Quá tải (OL)** là **theo thời gian**. Dòng cao vừa phải nhưng kéo dài, biến tần tích lũy nhiệt và cắt sau vài giây đến vài phút. Đây là bảo vệ nhiệt cho động cơ ([xem bài quá tải](/loi-qua-nhiet-qua-tai-bien-tan/)).

Sai lầm hay gặp nhất là **đổ lỗi ngay cho biến tần thiếu công suất** và đi mua máy lớn hơn. Trong thực tế, nguyên nhân thường nằm ở **cài đặt, cơ khí hoặc đấu nối** — và biến tần lớn hơn không giải quyết được gì ngoài việc làm mất luôn khả năng bảo vệ.

> **Biến tần đang nhảy OC liên tục?** Gửi **mã lỗi · lỗi xảy ra khi nào · loại tải** → [Nhận hỗ trợ chẩn đoán](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-loi.svg)


Đây là bài **26/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: vì sao dòng vọt lên?

Dòng điện qua động cơ tỷ lệ với **mô-men mà động cơ đang phải sinh ra**. Mô-men đó gồm hai phần:

1. **Mô-men để thắng tải** — ma sát, trọng lực, lực cắt, trở lực đường ống…
2. **Mô-men để gia tốc** — thay đổi tốc độ của khối lượng quay.

Phần thứ hai tỷ lệ với **quán tính** và **tỷ lệ nghịch với thời gian tăng tốc**. Rút ngắn thời gian tăng tốc một nửa nghĩa là đòi hỏi mô-men gia tốc gấp đôi, kéo theo dòng tăng mạnh.

Ngoài ra còn có ba cơ chế khác gây dòng vọt:

**Từ thông không phù hợp.** Ở chế độ V/f, nếu **torque boost đặt quá cao**, biến tần cấp thừa điện áp ở tần số thấp, làm động cơ bị bão hòa từ và **hút dòng lớn dù không tải nặng**.

**Khởi động khi động cơ đang quay.** Nếu biến tần đóng đầu ra trong khi rotor vẫn quay (quạt đang quay theo gió, bơm đang bị nước đẩy ngược, băng tải trôi), tần số đầu ra và tốc độ rotor **không khớp nhau**, tạo ra dòng đột biến rất lớn.

**Chạm chập thật sự.** Chạm pha-pha hoặc pha-đất trên cáp hoặc trong động cơ. Đây là trường hợp duy nhất mà lỗi OC báo hiệu một hư hỏng vật lý cần sửa chữa ngay.

---

## Cấu tạo chẩn đoán: ba tình huống, ba nguyên nhân khác nhau

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-thongso.svg)


Điều quan trọng nhất khi xử lý lỗi OC là xác định **lỗi xảy ra vào lúc nào**. Ba tình huống dưới đây dẫn tới ba hướng xử lý hoàn toàn khác nhau.

### Tình huống 1 — OC khi tăng tốc (phổ biến nhất)

**Nguyên nhân theo thứ tự khả năng:**

1. **Thời gian tăng tốc quá ngắn** so với quán tính tải.
2. **Tải quá nặng khi khởi động** — máy trộn đầy nguyên liệu, băng tải chất đầy.
3. **Chế độ điều khiển không phù hợp** — để V/f cho tải cần mô-men lớn ở tốc độ thấp.
4. **Torque boost đặt quá cao.**
5. **Động cơ đang quay khi khởi động** (chưa bật flying start).
6. **Cơ khí kẹt** — vòng bi hỏng, lệch tâm, vật lạ.
7. **Biến tần thiếu công suất thật sự** — chỉ xét sau khi loại trừ hết các nguyên nhân trên.

**Xử lý theo thứ tự:**

- **Kéo dài thời gian tăng tốc** — miễn phí, thử ngay đầu tiên ([xem chi tiết](/cai-tang-giam-toc-bien-tan/)).
- Bật **đường cong chữ S** nếu tải cần khởi động mềm.
- Chuyển sang **sensorless vector và chạy auto-tune** nếu tải cần mô-men khởi động lớn ([xem so sánh chế độ](/che-do-dieu-khien-vf-vector/)).
- **Giảm torque boost** nếu đang để cao.
- Bật **flying start** với quạt và các tải có thể tự quay.
- Kiểm tra **cơ khí**: quay trục bằng tay, nghe tiếng vòng bi, kiểm tra khớp nối.
- Chỉ khi tất cả đều đúng mà vẫn thiếu mô-men → **tăng một cấp công suất** ([xem cách chọn](/chon-cong-suat-bien-tan/)).

### Tình huống 2 — OC khi đang chạy ổn định

Đây là tình huống đáng lo hơn, vì hệ đã chạy được rồi mà vẫn vọt dòng.

**Nguyên nhân:**

1. **Tải thay đổi đột ngột** — vật liệu vào máy không đều, kẹt cục bộ, vật lạ lọt vào.
2. **Cơ khí bắt đầu hỏng** — vòng bi mòn, dây curoa quá căng, khớp nối lệch tâm.
3. **Mất pha đầu ra** — một pha đứt hoặc cực lỏng khiến hai pha còn lại gánh toàn bộ.
4. **Cách điện động cơ suy giảm** — chớm chạm chập trong cuộn dây.
5. **Cáp động cơ dài gây dòng nạp điện dung**, nhất là khi tần số sóng mang cao.
6. **Nhiễu** gây đọc sai giá trị dòng.

**Xử lý:**

- **Đo dòng ba pha bằng ampe kìm** — ba pha lệch nhau đáng kể là dấu hiệu mất pha hoặc cuộn dây có vấn đề.
- **Siết lại toàn bộ cực đấu** (sau khi ngắt điện và chờ tụ xả hết).
- **Kiểm tra cơ khí** — độ căng dây curoa, đồng tâm khớp nối, vòng bi.
- **Đo cách điện động cơ** — nhớ **tháo cáp khỏi biến tần** trước khi megger.
- **Giảm tần số sóng mang** nếu cáp dài.
- Lắp **cuộn kháng đầu ra** nếu cáp dài ([xem chi tiết](/cuon-khang-loc-nhieu-bien-tan/)).

### Tình huống 3 — OC ngay khi vừa bấm Run, chưa kịp quay

Tình huống này thường nghiêm trọng và cần dừng lại kiểm tra kỹ trước khi thử lại.

**Nguyên nhân:**

1. **Chạm chập cáp động cơ** — cáp bị kẹp, dập, ẩm ướt.
2. **Chạm chập trong động cơ** — cuộn dây hỏng.
3. **Đấu sai** — chạm pha trong hộp cực, đấu sao/tam giác sai ([xem sơ đồ đấu dây](/so-do-dau-day-bien-tan/)).
4. **IGBT hỏng** trong biến tần.
5. **Tải kẹt cứng hoàn toàn.**

**Xử lý — làm theo đúng thứ tự an toàn:**

1. **Ngắt điện, chờ tụ xả hết, đo xác nhận.**
2. **Tháo cáp động cơ khỏi biến tần.**
3. **Đo cách điện và thông mạch cuộn dây động cơ** — ba pha phải cân nhau.
4. **Kiểm tra cáp** — cách điện giữa các pha và với đất.
5. **Quay trục bằng tay** — có kẹt không.
6. Nếu động cơ và cáp đều tốt, **chạy biến tần không nối động cơ** — vẫn báo OC thì khả năng cao **IGBT đã hỏng** ([xem bài sửa hay thay](/sua-hay-thay-bien-tan/)).

---

## Ứng dụng: bảng tra nhanh

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-suachua.svg)


| Lỗi OC xảy ra khi | Nguyên nhân hàng đầu | Việc làm đầu tiên |
|---|---|---|
| **Tăng tốc, tải nhẹ** | Thời gian tăng tốc quá ngắn | Kéo dài thời gian tăng tốc |
| **Tăng tốc, tải nặng** | Thiếu mô-men khởi động | Chuyển sang vector + auto-tune |
| **Tăng tốc quạt** | Cánh đang quay | Bật flying start |
| **Chạy ổn định, đột ngột** | Tải kẹt, vật lạ | Kiểm tra cơ khí và vật liệu vào máy |
| **Chạy ổn định, ngày càng thường xuyên** | Vòng bi mòn, cách điện suy giảm | Đo dòng 3 pha, kiểm tra cơ khí |
| **Ngay khi bấm Run** | Chạm chập hoặc IGBT hỏng | Tháo cáp, đo cách điện |
| **Chỉ khi chạy tần số cao** | Cáp dài, sóng mang cao | Giảm sóng mang, lắp cuộn kháng ra |
| **Sau khi đổi động cơ** | Chưa khai lại thông số | Khai lại nhãn động cơ, auto-tune lại |
| **Sau khi ai đó chỉnh máy** | Cài đặt bị đổi | So với bảng thông số đã lưu |

---

## So sánh: các hướng xử lý và chi phí

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)


| Hướng xử lý | Chi phí | Khi nào đúng | Rủi ro nếu làm sai chỗ |
|---|---|---|---|
| **Kéo dài thời gian tăng tốc** | Miễn phí | OC khi tăng tốc, không yêu cầu chu kỳ nhanh | Chu kỳ máy dài hơn |
| **Đổi sang vector + auto-tune** | Miễn phí | Tải cần mô-men lớn khi khởi động | Không dùng được nếu nhiều động cơ song song |
| **Bật flying start** | Miễn phí | Quạt, tải tự quay | Không có |
| **Giảm torque boost** | Miễn phí | Dòng cao ở tần số thấp khi tải nhẹ | Nếu giảm quá tay sẽ yếu mô-men |
| **Sửa cơ khí** | Thấp – trung bình | Trục nặng, vòng bi kêu | — |
| **Lắp cuộn kháng đầu ra** | Trung bình | Cáp dài | Không giải quyết được nếu nguyên nhân là cài đặt |
| **Tăng một cấp công suất biến tần** | Cao | Đã loại trừ hết các nguyên nhân trên | **Mất khả năng bảo vệ động cơ** nếu chọn quá lớn |
| **Thay biến tần** | Cao nhất | IGBT hỏng thật | Vô ích nếu lỗi nằm ở hệ thống |

Điểm cần nhấn mạnh ở dòng cuối bảng: **chọn biến tần lớn hơn nhiều so với động cơ làm bảo vệ quá tải mất tác dụng**. Biến tần sẽ không còn nhận ra động cơ đang quá tải, và động cơ có thể cháy trong khi biến tần vẫn "bình thường".

---

## Sai lầm thường gặp

1. **Mua biến tần lớn hơn ngay** khi gặp OC mà chưa kiểm tra cài đặt và cơ khí.
2. **Reset và chạy lại liên tục** — nếu có chạm chập thật, mỗi lần reset là một lần đánh vào IGBT.
3. **Tăng torque boost để khởi động khỏe hơn** — thường làm dòng cao hơn nữa.
4. **Bỏ qua bước quay trục bằng tay** — bước kiểm tra rẻ và nhanh nhất.
5. **Không đo dòng ba pha** khi lỗi xảy ra lúc chạy ổn định.
6. **Megger động cơ khi cáp còn nối vào biến tần** — hỏng mạch điện tử.
7. **Quên bật flying start** cho quạt và tải tự quay.
8. **Không khai lại thông số sau khi đổi động cơ.**
9. **Chỉ chạy thử không tải rồi kết luận đã sửa xong.**
10. **Nâng ngưỡng bảo vệ dòng** để hết báo lỗi.

---

## Cam kết tại HOANTRANTDH

- ✅ **Chẩn đoán theo tình huống** — hỏi rõ lỗi xảy ra khi nào trước khi đề xuất giải pháp.
- ✅ Ưu tiên các **biện pháp miễn phí về cài đặt** trước khi tư vấn thay thiết bị.
- ✅ Tư vấn **chọn đúng cấp công suất** — không bán máy lớn hơn mức cần thiết.
- ✅ Hỗ trợ kiểm tra **cơ khí, đấu nối và cách điện** cùng đội bảo trì tại chỗ.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ chẩn đoán & báo giá

Gửi cho chúng tôi: **mã lỗi chính xác · model biến tần · lỗi xảy ra khi nào (tăng tốc / chạy ổn định / ngay khi bấm Run) · công suất động cơ và loại tải · thời gian tăng tốc đang cài · có thay đổi gì gần đây không.**

**→ [Liên hệ hỗ trợ xử lý lỗi OC](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lỗi OC trên biến tần nghĩa là gì?**
Nghĩa là **dòng điện đầu ra vượt ngưỡng tức thời**, biến tần cắt ngay trong vài mili giây để bảo vệ IGBT.

**Lỗi OC và OL khác nhau thế nào?**
**OC là quá dòng tức thời** — dòng vọt rất cao trong khoảnh khắc. **OL là quá tải theo thời gian** — dòng cao vừa phải nhưng kéo dài, bảo vệ nhiệt cho động cơ.

**Biến tần báo OC khi tăng tốc, xử lý ra sao?**
Bắt đầu bằng cách **kéo dài thời gian tăng tốc**. Nếu vẫn lỗi và tải cần mô-men lớn khi khởi động thì chuyển sang **sensorless vector và chạy auto-tune**.

**Có phải cứ báo OC là biến tần thiếu công suất không?**
**Không.** Nguyên nhân phổ biến hơn nhiều là cài đặt (tăng tốc quá nhanh, chế độ sai, boost quá cao) và cơ khí (kẹt, vòng bi hỏng).

**Biến tần báo OC ngay khi bấm Run là bị gì?**
Thường là **chạm chập cáp hoặc động cơ**, đấu sai, tải kẹt cứng, hoặc **IGBT đã hỏng**. Cần ngắt điện, tháo cáp và đo cách điện trước khi thử lại.

**Vì sao quạt hay báo OC khi khởi động?**
Vì **cánh quạt đang quay** (có khi quay ngược) khi biến tần đóng đầu ra. Cần bật chức năng **flying start / speed search**.

**Có nên reset và chạy lại nhiều lần không?**
Không. Nếu có chạm chập thật, mỗi lần reset là một lần đánh dòng lớn vào IGBT và có thể làm hỏng hẳn thiết bị.

**Tăng biến tần lên một cấp có an toàn không?**
Chỉ khi đã loại trừ các nguyên nhân khác. Chọn biến tần **lớn hơn nhiều** so với động cơ sẽ làm **bảo vệ quá tải mất tác dụng**, khiến động cơ có thể cháy mà biến tần không báo gì.

<!-- SCHEMA: FAQPage + BreadcrumbList + Article. INTERNAL LINK: /bien-tan-la-gi/, /loi-bien-tan-thuong-gap/, /cai-tang-giam-toc-bien-tan/, /che-do-dieu-khien-vf-vector/, /chon-cong-suat-bien-tan/, /so-do-dau-day-bien-tan/, /cuon-khang-loc-nhieu-bien-tan/, /loi-qua-nhiet-qua-tai-bien-tan/, /sua-hay-thay-bien-tan/, /lien-he/. -->
