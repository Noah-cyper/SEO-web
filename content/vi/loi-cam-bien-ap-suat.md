<!--
LOẠI TRANG : Blog kỹ thuật (how-to) — Thông tin + thương mại
URL SLUG   : /loi-cam-bien-ap-suat/
TỪ KHÓA    : lỗi cảm biến | lỗi cảm biến áp suất | cảm biến áp suất không lên tín hiệu | cảm biến áp suất sai số | khắc phục lỗi transmitter | 4-20ma không ổn định
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. Quy trình chẩn đoán chung; luôn đối chiếu datasheet của model cụ thể.
-->

TITLE TAG   : Lỗi Cảm Biến Áp Suất Thường Gặp Và Cách Khắc Phục
META (156)  : Lỗi cảm biến áp suất hay gặp: mất tín hiệu, số nhảy loạn, sai số, đứng yên. Quy trình chẩn đoán theo thứ tự và cách khắc phục từ nguồn, dây tới đầu dò.
H1          : Lỗi Cảm Biến Áp Suất – Chẩn Đoán Và Khắc Phục

---

## Nhận diện nhanh các nhóm lỗi cảm biến

<!--IMG:rep-->
![Lỗi cảm biến áp suất và cách chẩn đoán](assets/diagrams/rep-pressure.svg)


Phần lớn **lỗi cảm biến** áp suất trong nhà máy rơi vào bốn nhóm, và mỗi nhóm có hướng chẩn đoán khác hẳn nhau:

| Nhóm | Biểu hiện | Khả năng cao là |
|---|---|---|
| **Lỗi cảm biến mất tín hiệu** | PLC đọc 0mA hoặc dưới 4mA | Nguồn, đứt dây, hỏng cảm biến |
| **Lỗi cảm biến bão hòa tín hiệu** | Luôn ở 20mA hoặc trên 20mA | Quá áp, hỏng màng, ngắn mạch |
| **Lỗi cảm biến nhảy số** | Giá trị dao động liên tục | Nhiễu, tiếp đất, xung áp |
| **Lỗi cảm biến sai số ổn định** | Đọc lệch một lượng cố định | Trôi zero, cần hiệu chỉnh |

Khoanh đúng nhóm lỗi cảm biến trước khi động tay vào là cách tiết kiệm thời gian nhất. Rất nhiều trường hợp thay cảm biến mới rồi vẫn **lỗi cảm biến** như cũ — vì nguyên nhân nằm ở dây hoặc ở lắp đặt.

> **Cần thay cảm biến hoặc tư vấn chọn model bền hơn?** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-pressure.svg)


---

## Quy trình chẩn đoán lỗi cảm biến theo thứ tự

| Bước | Việc kiểm tra | Nếu bất thường thì |
|---|---|---|
| 1 | Đo điện áp nguồn tại chân cảm biến | Kiểm tra nguồn 24VDC, sụt áp trên dây |
| 2 | Đo dòng vòng 4-20mA bằng đồng hồ | Xác định lỗi ở cảm biến hay ở PLC |
| 3 | So giá trị với đồng hồ cơ cùng điểm đo | Biết lệch bao nhiêu, lệch theo hướng nào |
| 4 | Kiểm tra đường dẫn áp, van chặn | Loại trừ nghẹt, van đóng |
| 5 | Xem cấu hình thang đo trong PLC | Loại trừ khai báo sai |
| 6 | Tháo, kiểm tra màng và đầu nối | Đến bước này mới nghi cảm biến hỏng |

Nguyên tắc vàng: **luôn đo dòng vòng trước khi tháo cảm biến**. Nếu dòng đo tại vòng đúng mà PLC đọc sai, thì **lỗi cảm biến** thực ra không tồn tại — vấn đề nằm ở module analog hoặc khai báo. Xem [kết nối PLC với cảm biến 4-20mA](/ket-noi-plc-cam-bien-4-20ma/).

---

## Lỗi cảm biến không lên tín hiệu

| Nguyên nhân | Cách kiểm tra | Cách xử lý |
|---|---|---|
| Mất nguồn 24VDC | Đo áp tại chân cảm biến | Kiểm tra CB, nguồn, cầu chì |
| Sụt áp do dây quá dài, tiết diện nhỏ | Đo áp khi có tải | Tăng tiết diện hoặc đưa nguồn lại gần |
| Đứt dây, lỏng đầu cos | Đo thông mạch | Bấm lại đầu cos, thay đoạn dây |
| Đấu ngược cực | Đối chiếu sơ đồ | Đấu lại — xem [đấu dây 4-20mA](/dau-day-cam-bien-ap-suat-4-20ma/) |
| Hỏng module analog PLC | Thử kênh khác | Thay module, xem [lỗi ngõ vào ra PLC](/loi-ngo-vao-ra-plc/) |
| Cảm biến hỏng thật | Sau khi loại trừ 5 mục trên | Thay thiết bị |

Thứ tự bảng này chính là thứ tự nên kiểm tra khi gặp lỗi cảm biến. Kinh nghiệm thực tế: **lỗi cảm biến** kiểu mất tín hiệu phần lớn nằm ở **hai dòng đầu**, không phải ở thiết bị.

---

## Lỗi cảm biến cho số nhảy loạn

| Nguyên nhân | Dấu hiệu nhận biết | Cách xử lý |
|---|---|---|
| Nhiễu điện từ | Nhảy mạnh khi biến tần chạy | Tách máng cáp, dùng cáp có lưới — xem [lỗi PLC do nhiễu](/loi-plc-do-nhieu/) |
| Vòng lặp tiếp đất | Nhảy khi chạm vỏ tủ | Chỉ tiếp đất một điểm, cách ly tín hiệu |
| Xung áp trong đường ống | Nhảy theo nhịp bơm | Lắp bộ giảm chấn trên đường dẫn áp |
| Bọt khí trong ống dẫn áp | Nhảy thất thường, khó lặp lại | Xả khí đường dẫn áp |
| Nguồn kém chất lượng | Nhảy cùng lúc nhiều kênh | Thay nguồn ổn định hơn |

Với nhóm lỗi cảm biến do nhiễu, giải pháp bền nhất là **cách ly tín hiệu** bằng [bộ chuyển đổi tín hiệu](/bo-chuyen-doi-tin-hieu-seneca/) — rẻ hơn nhiều so với đi lại toàn bộ tuyến cáp, và xử lý dứt điểm cả vòng lặp tiếp đất.

---

## Lỗi cảm biến kiểu sai số và trôi theo thời gian

| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Lệch một lượng cố định | Trôi zero | Hiệu chỉnh zero khi đã xả hết áp |
| Lệch tăng dần theo giá trị đo | Trôi span | Hiệu chỉnh span bằng nguồn áp chuẩn |
| Sai số đổi theo nhiệt độ | Không bù nhiệt hoặc lắp gần nguồn nhiệt | Đổi model có bù nhiệt, che chắn nhiệt |
| Đọc thấp dần theo tháng | Đường dẫn áp bám cặn dần | Vệ sinh, cân nhắc bản màng ngăn |
| Kim/số đứng yên hoàn toàn | Nghẹt lỗ dẫn áp | Thông đường dẫn, dùng [bản dạng màng](/dong-ho-ap-suat-dang-mang/) |

Hiện tượng cuối cùng nguy hiểm nhất: **áp suất thật vẫn tăng nhưng thiết bị báo không đổi**. Với môi chất bẩn, nhớt hoặc dễ kết tinh, đây không phải **lỗi cảm biến** ngẫu nhiên mà là hệ quả của việc chọn sai loại ngay từ đầu.

---

## Lỗi cảm biến nào nên thay thay vì tiếp tục sửa?

- **Lỗi cảm biến do màng biến dạng vì quá áp** — không hiệu chỉnh lại được, phải thay.
- **Sai số vượt ngưỡng cho phép sau hiệu chỉnh** — thiết bị đã hết tuổi thọ hữu ích.
- **Vỏ nứt, nước vào bên trong** — dễ tái phát dù có sấy khô.
- **Model đã ngừng sản xuất, không còn phụ tùng** — xem [thiết bị công nghiệp khó tìm](/thiet-bi-cong-nghiep-kho-tim/).
- **Lỗi lặp lại nhiều lần cùng một vị trí** — dấu hiệu chọn sai loại cho môi chất, nên đổi sang bản phù hợp hơn.

Điểm cuối đáng lưu tâm: nếu cùng một điểm đo hỏng ba lần trong một năm, vấn đề không phải chất lượng thiết bị mà là **chọn sai model**. Xem [cách chọn cảm biến áp suất](/cam-bien-ap-suat/).

---

## Phòng ngừa lỗi cảm biến từ khâu lắp đặt

| Biện pháp | Ngăn được lỗi cảm biến nào |
|---|---|
| Chọn thang đo để áp làm việc ở 1/3–2/3 thang | Quá áp, trôi span |
| Lắp van chặn trước cảm biến | Tháo kiểm tra không phải dừng hệ thống |
| Dùng ống siphon với môi chất nóng | Hỏng do nhiệt — xem [đồng hồ áp suất lò hơi](/dong-ho-ap-suat-lo-hoi/) |
| Tách máng cáp tín hiệu và động lực | Nhiễu, số nhảy loạn |
| Bố trí đường dẫn áp có thể xả khí | Bọt khí gây đọc sai |
| Hiệu chỉnh và ghi nhật ký định kỳ | Phát hiện trôi trước khi thành sự cố |

---

<a name="bao-gia"></a>
## Nhận tư vấn khắc phục lỗi cảm biến áp suất

Gửi cho chúng tôi: **model cảm biến hiện có (ảnh tem) · biểu hiện lỗi · môi chất và điều kiện lắp đặt · đã kiểm tra được những gì.**

Chúng tôi hỗ trợ khoanh vùng nguyên nhân, và nếu cần thay thì đề xuất model phù hợp hơn với chính điều kiện đang gây lỗi — kèm CO/CQ và hóa đơn VAT.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-pressure.svg)

## Câu hỏi thường gặp (FAQ)

**Cảm biến báo 0mA nghĩa là gì?**
Dòng dưới 4mA thường là **mất nguồn hoặc đứt dây**, không phải hỏng cảm biến. Kiểm tra nguồn 24VDC và thông mạch trước khi nghi thiết bị.

**Cảm biến luôn báo 20mA là lỗi gì?**
Thường do **quá áp** hoặc màng đã hỏng; cũng có thể do ngắn mạch trên đường tín hiệu. Xả áp về 0 rồi đo lại để phân biệt.

**Số đọc nhảy loạn khi biến tần chạy, xử lý thế nào?**
Đây là nhiễu điện từ. Tách máng cáp tín hiệu khỏi cáp động lực, dùng cáp có lưới chống nhiễu, và cách ly tín hiệu bằng bộ chuyển đổi nếu vẫn chưa dứt.

**Có tự hiệu chỉnh zero được không?**
Nhiều model cho phép hiệu chỉnh zero khi đã xả hết áp. Hiệu chỉnh span thì cần nguồn áp chuẩn, nên thực hiện tại đơn vị có thiết bị chuẩn.

**Cùng một vị trí hỏng nhiều lần thì sao?**
Đó là dấu hiệu chọn sai model cho môi chất hoặc điều kiện lắp đặt. Gửi mô tả điều kiện thực tế, chúng tôi đề xuất bản phù hợp hơn thay vì thay đi thay lại cùng một loại.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-ap-suat/, /dau-day-cam-bien-ap-suat-4-20ma/, /loi-plc-do-nhieu/, /bo-chuyen-doi-tin-hieu-seneca/, /lien-he/. -->
