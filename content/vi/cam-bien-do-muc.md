<!--
LOẠI TRANG : Bài trụ (pillar) — Thông tin + thương mại
URL SLUG   : /cam-bien-do-muc/
TỪ KHÓA    : cảm biến đo mức | đo mức nước | cảm biến siêu âm đo mức | cảm biến radar đo mức | công tắc báo mức | đo mức bồn chứa
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. Bảng công nghệ viết theo nguyên lý chọn; thông số cụ thể tra datasheet từng model trước khi báo giá.
-->

TITLE TAG   : Cảm Biến Đo Mức Là Gì? Các Loại Và Cách Chọn Đúng
META (152)  : Cảm biến đo mức là gì, có mấy loại (siêu âm, radar, thủy tĩnh, điện dung, phao) và cách chọn đúng theo môi chất, bồn chứa. Kèm ứng dụng thực tế và báo giá.
H1          : Cảm Biến Đo Mức Là Gì? Phân Loại Và Cách Chọn

---

## Cảm biến đo mức là gì?

<!--IMG:rep-->
![Cảm biến đo mức là gì](assets/diagrams/rep-level.svg)


**Cảm biến đo mức** là thiết bị xác định **chiều cao hoặc thể tích môi chất** trong bồn, bể, silo, kênh hở — rồi chuyển thành tín hiệu điện để PLC, SCADA hoặc bộ hiển thị đọc được.

Cần phân biệt hai nhóm ngay từ đầu, vì chọn nhầm nhóm là lỗi tốn kém nhất:

- **Cảm biến đo mức liên tục:** trả về giá trị mức theo thời gian thực (thường 4-20mA hoặc Modbus). Dùng khi cần biết *còn bao nhiêu*.
- **Công tắc báo mức (level switch):** chỉ đóng/ngắt tiếp điểm tại một điểm. Dùng khi chỉ cần biết *đầy hay cạn*.

Rất nhiều nhà máy mua cảm biến đo mức liên tục cho một bài toán chỉ cần chống tràn — trả gấp nhiều lần chi phí cần thiết. Ngược lại, dùng công tắc cho bài toán quản lý tồn kho thì không bao giờ đủ.

> **Cần chọn cảm biến đo mức cho bồn cụ thể?** Gửi **môi chất · chiều cao bồn · vật liệu bồn · nhiệt độ/áp suất** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-ultrasonic.svg)


---

## Các loại cảm biến đo mức thông dụng hiện nay

| Công nghệ | Nguyên lý | Mạnh ở đâu | Tránh dùng khi |
|---|---|---|---|
| **Siêu âm** | Đo thời gian sóng âm phản xạ | Không tiếp xúc, giá hợp lý | Nhiều bọt, hơi dày đặc, chân không |
| **Radar (sóng vi ba)** | Đo phản xạ sóng điện từ | Ổn định với hơi, bụi, nhiệt cao | Ngân sách rất hạn chế |
| **Radar dẫn sóng (GWR)** | Sóng chạy dọc que/cáp dẫn | Bồn hẹp, có vách ngăn, chất bám | Môi chất đóng cặn nặng lên que |
| **Thủy tĩnh (áp suất)** | Đo áp cột chất lỏng | Giếng sâu, hố bơm, nước thải | Chất lỏng đổi tỷ trọng liên tục |
| **Điện dung** | Đo thay đổi điện dung | Chất rắn, bột, hạt | Môi chất bám dính mạnh lên que |
| **Phao cơ / phao từ** | Phao nổi theo mực | Rẻ, đơn giản, tin cậy | Chất lỏng bẩn, dễ kẹt phao |

Bảng công nghệ cảm biến đo mức trên dùng để **loại trừ** chứ không phải để chọn ngay. Với phần lớn bồn nước sạch, **cảm biến đo mức siêu âm** là điểm khởi đầu hợp lý; khi môi trường có hơi, bụi hoặc nhiệt độ cao thì chuyển sang **radar**.

---

## Cách chọn cảm biến đo mức theo môi chất

| Môi chất | Công nghệ nên ưu tiên | Lý do |
|---|---|---|
| Nước sạch, nước cấp | Siêu âm hoặc thủy tĩnh | Bề mặt phẳng, ít bọt |
| Nước thải, bùn | Siêu âm hoặc thủy tĩnh vỏ chống ăn mòn | Không tiếp xúc hoặc vỏ chịu bẩn |
| Hóa chất ăn mòn | Radar, siêu âm đầu dò PVDF | Không tiếp xúc, vật liệu chịu hóa chất |
| Dầu, nhớt | Radar dẫn sóng | Ít bị ảnh hưởng bởi hằng số điện môi thấp |
| Xăng, dung môi dễ cháy | Thiết bị có chứng nhận phòng nổ | Yêu cầu an toàn bắt buộc |
| Bột, hạt, xi măng | Điện dung, radar | Bề mặt nghiêng, nhiều bụi |
| Thực phẩm, sữa | Đầu dò vệ sinh, đấu nối clamp | Yêu cầu vệ sinh, dễ tháo lắp |

Ba câu hỏi quyết định phần lớn lựa chọn **cảm biến đo mức**: môi chất **bám dính** không, có **bọt/hơi** không, và bồn có **vật cản** bên trong không. Trả lời được ba câu này là loại ngay được quá nửa số công nghệ.

---

## Chọn cảm biến đo mức theo dạng bồn chứa

| Kiểu bồn | Lưu ý khi lắp cảm biến đo mức | Sai lầm thường gặp |
|---|---|---|
| Bồn đứng, nắp phẳng | Lắp cảm biến đo mức cách thành ≥ khoảng chết cho phép | Lắp sát thành gây nhiễu phản xạ |
| Bồn có cánh khuấy | Tránh vùng xoáy, cân nhắc GWR | Đặt ngay trên cánh khuấy |
| Bồn nằm ngang | Cần bảng quy đổi mức → thể tích | Coi mức tỷ lệ thẳng với thể tích |
| Silo chất rắn | Đo tại điểm đại diện, tính góc nghỉ | Đo giữa đỉnh đống, sai số lớn |
| Hố bơm, giếng sâu | Thủy tĩnh thả chìm | Dùng siêu âm khi giếng hẹp, nhiều hơi |
| Kênh hở, mương | Siêu âm kết hợp máng đo lưu lượng | Bỏ qua bù nhiệt độ ngoài trời |

Với bồn nằm ngang, kết quả của cảm biến đo mức **không tỷ lệ tuyến tính** với thể tích. Nếu cần số lít chứ không phải số mm, phải có bảng quy đổi trong bộ hiển thị hoặc PLC — chi tiết này hay bị bỏ sót đến lúc nghiệm thu.

---

## Ngõ ra của cảm biến đo mức và cách ghép hệ thống

| Ngõ ra cảm biến đo mức | Dùng khi | Ghi chú đấu nối |
|---|---|---|
| **4-20mA (2 dây)** | Phổ biến nhất, nối thẳng PLC | Xem [đấu dây 4-20mA](/dau-day-cam-bien-ap-suat-4-20ma/) |
| **Relay** | Chống tràn, bảo vệ bơm | Cần rõ trạng thái an toàn khi mất điện |
| **Modbus RTU** | Nhiều điểm đo trên một bus | Xem [gateway Modbus](/gateway-modbus-seneca/) |
| **Hiển thị tại chỗ** | Vận hành đọc trực tiếp | Có thể dùng [bộ hiển thị](/bo-hien-thi-seneca/) |
| **IO-Link / số** | Hệ thống mới, cần chẩn đoán | Kiểm tra PLC có hỗ trợ không |

Nếu tín hiệu **cảm biến đo mức** phải đi xa hoặc qua khu vực nhiễu, nên dùng [bộ chuyển đổi tín hiệu cách ly](/bo-chuyen-doi-tin-hieu-seneca/) — rẻ hơn nhiều so với đi lại tuyến cáp.

---

## Ứng dụng cảm biến đo mức tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-level.svg)


- **Cấp nước, xử lý nước thải:** điều khiển bơm theo mức, chống chạy khô, cảnh báo tràn. Xem [PLC trong xử lý nước thải](/plc-xu-ly-nuoc-thai/).
- **Thực phẩm – đồ uống:** đo mức bồn chứa nguyên liệu, siro, dầu ăn với đầu dò vệ sinh.
- **Hóa chất, sơn:** đo mức bồn axit, dung môi bằng công nghệ không tiếp xúc.
- **Xi măng, thức ăn chăn nuôi:** đo mức silo bột, hạt bằng điện dung hoặc radar.
- **Xăng dầu:** đo mức bồn nhiên liệu, bắt buộc thiết bị đạt chuẩn phòng nổ.

Dải sản phẩm đo mức đang phân phối: [cảm biến siêu âm](/cam-bien-sieu-am-do-muc-flowline/), [cảm biến radar](/cam-bien-radar-do-muc-flowline/), [cảm biến thủy tĩnh](/cam-bien-ap-suat-thuy-tinh-flowline/), [công tắc báo mức](/cong-tac-bao-muc-flowline/).

---

## Lỗi thường gặp của cảm biến đo mức

| Hiện tượng | Nguyên nhân hay gặp | Cách xử lý |
|---|---|---|
| Giá trị nhảy loạn | Bọt, hơi, sóng mặt thoáng | Thêm ống lặng, đổi sang radar |
| Mức đứng yên khi bồn đang thay đổi | Đầu dò bám bẩn, kẹt phao | Vệ sinh, chuyển công nghệ không tiếp xúc |
| Sai số tăng dần theo nhiệt độ | Không bù nhiệt | Chọn model có bù nhiệt tự động |
| Không đo được vùng gần đầu dò | Khoảng chết (dead band) | Nâng vị trí lắp hoặc đổi model |
| Tín hiệu 4-20mA trôi | Nhiễu, chung điểm nối đất | Cách ly tín hiệu, đi cáp có lưới chống nhiễu |

Riêng lỗi đầu bảng của cảm biến đo mức — số nhảy loạn — chiếm phần lớn khiếu nại thực tế, và gần như luôn là **vấn đề lắp đặt hoặc chọn sai công nghệ**, không phải lỗi thiết bị.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá cảm biến đo mức

Gửi cho chúng tôi: **môi chất · chiều cao và kiểu bồn · vật liệu bồn · nhiệt độ và áp suất làm việc · ngõ ra cần (4-20mA/relay/Modbus) · có yêu cầu phòng nổ hay vệ sinh không.**

Chúng tôi chọn đúng công nghệ và model, gửi datasheet kèm báo giá — hàng chính hãng, có CO/CQ và hóa đơn VAT.

**→ [Liên hệ báo giá cảm biến đo mức](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến đo mức loại nào chính xác nhất?**
Radar thường cho độ ổn định cao nhất trong điều kiện khó (hơi, bụi, nhiệt). Nhưng "chính xác nhất" chỉ có nghĩa khi gắn với môi chất và kiểu bồn cụ thể — chọn đúng công nghệ quan trọng hơn chọn cấp chính xác cao.

**Đo mức nước sạch nên dùng loại nào?**
Siêu âm hoặc thủy tĩnh là hai lựa chọn phổ biến và kinh tế. Giếng sâu, hố bơm hẹp thì thủy tĩnh thả chìm thuận tiện hơn.

**Cảm biến đo mức có đo được chất rắn không?**
Có. Bột, hạt, xi măng thường dùng điện dung hoặc radar. Cần lưu ý bề mặt chất rắn nghiêng theo góc nghỉ nên vị trí lắp ảnh hưởng lớn tới kết quả.

**Chênh lệch giá giữa siêu âm và radar khoảng bao nhiêu?**
Radar thường cao hơn đáng kể. Nếu môi trường không có hơi, bụi hay nhiệt cao thì siêu âm đủ dùng; chỉ nên trả thêm cho radar khi thực sự cần độ ổn định đó.

**Có hàng chính hãng, CO/CQ không?**
Có. Thiết bị nhập chính hãng, kèm CO/CQ và hóa đơn VAT; hỗ trợ chọn mã và hướng dẫn lắp đặt.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-sieu-am-do-muc-flowline/, /cam-bien-radar-do-muc-flowline/, /cong-tac-bao-muc-flowline/, /dau-day-cam-bien-ap-suat-4-20ma/, /lien-he/. -->
