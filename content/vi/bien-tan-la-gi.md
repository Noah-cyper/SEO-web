<!--
LOẠI TRANG : Bài trụ (pillar) — Thông tin + thương mại
URL SLUG   : /bien-tan-la-gi/
TỪ KHÓA    : biến tần | biến tần là gì | cách chọn biến tần | inverter | công suất biến tần | biến tần điều khiển động cơ
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. Bảng chọn viết theo nguyên tắc; công suất và mã đặt hàng tra catalog hãng trước khi báo giá.
-->

TITLE TAG   : Biến Tần Là Gì? Nguyên Lý, Cách Chọn Và Ứng Dụng
META (151)  : Biến tần là gì, nguyên lý hoạt động, cách chọn đúng công suất và loại tải, tiết kiệm điện được bao nhiêu. Kèm lỗi thường gặp và tư vấn chọn mã, báo giá.
H1          : Biến Tần Là Gì? Nguyên Lý Và Cách Chọn Đúng

---

## Biến tần là gì?

<!--IMG:rep-->
![Biến tần là gì](assets/diagrams/rep-controller.svg)


**Biến tần** (inverter, VFD — Variable Frequency Drive) là thiết bị thay đổi **tần số và điện áp** cấp cho động cơ, nhờ đó điều chỉnh được **tốc độ quay** của động cơ xoay chiều.

Trước khi có **biến tần**, muốn giảm lưu lượng bơm thì phải khóa bớt van — động cơ vẫn chạy hết công suất, phần năng lượng thừa biến thành nhiệt và tiếng ồn. Với **biến tần**, động cơ chỉ chạy đúng tốc độ cần thiết.

Ba lý do nhà máy lắp **biến tần**:

- **Tiết kiệm điện** với tải bơm và quạt — nhóm tải chiếm tỷ trọng điện lớn nhất ở hầu hết nhà máy.
- **Khởi động mềm**, giảm dòng khởi động và sốc cơ khí lên khớp nối, dây curoa, hộp số.
- **Điều khiển chính xác** tốc độ theo tín hiệu từ [PLC](/plc-la-gi/) hoặc cảm biến quá trình.

> **Cần chọn biến tần cho một động cơ cụ thể?** Gửi **công suất · loại tải · điện áp lưới · yêu cầu điều khiển** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-energy.svg)


---

## Nguyên lý hoạt động của biến tần

| Khối | Việc thực hiện | Ảnh hưởng tới lựa chọn |
|---|---|---|
| **Chỉnh lưu** | Đổi AC lưới thành DC | Quyết định điện áp vào 1 pha hay 3 pha |
| **Tụ DC bus** | Lọc, tích năng lượng | Tuổi thọ tụ quyết định tuổi thọ biến tần |
| **Nghịch lưu (IGBT)** | Tạo lại AC với tần số thay đổi | Tần số sóng mang ảnh hưởng tiếng ồn, nhiễu |
| **Mạch điều khiển** | Thuật toán V/f, vector | Quyết định khả năng giữ mô-men ở tốc độ thấp |
| **Điện trở xả** | Tiêu tán năng lượng khi hãm | Cần cho tải quán tính lớn, hạ tải |

Hiểu khối thứ hai giúp tránh một sai lầm phổ biến: **biến tần để lâu không dùng sẽ hỏng tụ**. Thiết bị dự phòng nên được cấp điện định kỳ theo khuyến cáo của hãng thay vì cất kho nhiều năm.

---

## Cách chọn biến tần theo loại tải

| Loại tải | Đặc điểm mô-men | Lưu ý khi chọn biến tần |
|---|---|---|
| **Bơm ly tâm, quạt** | Mô-men thay đổi theo bình phương tốc độ | Tiết kiệm điện rõ nhất, chọn chế độ tải nhẹ |
| **Băng tải** | Mô-men không đổi | Cần mô-men khởi động đủ, xem [điều khiển băng tải](/plc-dieu-khien-bang-tai/) |
| **Máy nén khí** | Mô-men không đổi, tải nặng | Chọn dòng chịu quá tải cao |
| **Máy khuấy, máy trộn** | Mô-men lớn ở tốc độ thấp | Cần điều khiển vector, không dùng V/f đơn thuần |
| **Cẩu trục, nâng hạ** | Có giai đoạn hãm tái sinh | Bắt buộc có điện trở xả hoặc bộ hãm |
| **Máy công cụ** | Yêu cầu độ chính xác cao | Cân nhắc điều khiển vòng kín có encoder |

Nguyên tắc chọn công suất: **chọn theo dòng định mức của động cơ, không chọn theo kW ghi trên nhãn**. Hai động cơ cùng kW nhưng khác số cực, khác hiệu suất thì dòng khác nhau — chọn theo kW dễ bị thiếu dòng khi tải nặng.

---

## Biến tần tiết kiệm điện được bao nhiêu?

| Ứng dụng | Mức tiết kiệm điển hình | Điều kiện để đạt được |
|---|---|---|
| Bơm cấp nước theo nhu cầu | Cao | Tải thay đổi nhiều trong ngày |
| Quạt hút, quạt thổi lò | Cao | Trước đây điều tiết bằng lá chắn gió |
| Băng tải chạy liên tục đầy tải | Thấp | Không có dư địa giảm tốc |
| Máy nén khí tải nền | Trung bình | Nhu cầu khí dao động |
| Bơm chạy 100% suốt ngày | Gần như không | Không giảm tốc được |

⚠️ Cần nói thẳng: **biến tần chỉ tiết kiệm điện khi tải thực sự thay đổi**. Với động cơ chạy đủ tải liên tục, lắp **biến tần** chủ yếu để khởi động mềm và bảo vệ cơ khí, không phải để giảm hóa đơn điện. Con số tiết kiệm cụ thể phải tính từ biểu đồ phụ tải thực tế của nhà máy.

---

## Ghép biến tần vào hệ thống điều khiển

| Cách điều khiển | Phù hợp khi | Ghi chú |
|---|---|---|
| **Chiết áp / nút trên mặt biến tần** | Máy đơn lẻ, chỉnh tay | Đơn giản nhất |
| **Tín hiệu 4-20mA / 0-10V từ PLC** | Điều khiển theo quá trình | Xem [kết nối PLC – biến tần](/ket-noi-plc-bien-tan/) |
| **Modbus RTU / Ethernet** | Nhiều biến tần, cần đọc trạng thái | Đọc được dòng, tần số, mã lỗi |
| **Vòng kín PID** | Giữ áp suất, lưu lượng ổn định | Kết hợp [cảm biến áp suất](/cam-bien-ap-suat/) |
| **Điều khiển đa bơm luân phiên** | Trạm bơm cấp nước | Xem [PLC cho hệ thống bơm](/plc-he-thong-bom/) |

Nếu **biến tần** đặt xa tủ điều khiển hoặc môi trường nhiễu mạnh, nên đưa tín hiệu analog qua [bộ chuyển đổi cách ly](/bo-chuyen-doi-tin-hieu-seneca/) thay vì kéo dây trực tiếp.

---

## Lỗi thường gặp và cách xử lý

| Mã lỗi / hiện tượng | Nguyên nhân thường gặp | Hướng xử lý |
|---|---|---|
| Quá dòng (OC) khi khởi động | Thời gian tăng tốc quá ngắn, tải kẹt | Kéo dài thời gian tăng tốc, kiểm tra cơ khí |
| Quá áp (OV) khi dừng | Năng lượng hãm dội về DC bus | Kéo dài thời gian giảm tốc, lắp điện trở xả |
| Quá nhiệt (OH) | Quạt tủ hỏng, lọc bụi tắc | Vệ sinh, kiểm tra thông gió tủ |
| Động cơ rung, kêu ở tốc độ thấp | Cài V/f không phù hợp | Chuyển sang điều khiển vector, chỉnh boost |
| Nhiễu lên tín hiệu cảm biến | Cáp động lực đi chung máng tín hiệu | Tách máng, dùng cáp có lưới, lắp lọc EMC |
| Biến tần dự phòng bật lên là lỗi | Tụ DC khô do cất kho lâu | Cấp điện định kỳ theo khuyến cáo hãng |

Hai dòng cuối bảng là nguyên nhân của rất nhiều sự cố bị quy nhầm cho "hàng kém chất lượng". Cả hai đều phòng được bằng thi công và bảo trì đúng.

---

## Ứng dụng biến tần tại nhà máy Việt Nam

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-control.svg)


- **Cấp nước, xử lý nước thải:** giữ áp suất đường ống ổn định, luân phiên bơm. Xem [PLC xử lý nước thải](/plc-xu-ly-nuoc-thai/).
- **Thực phẩm – đồ uống:** điều chỉnh tốc độ băng tải theo nhịp dây chuyền.
- **Dệt may:** đồng bộ tốc độ nhiều cụm máy.
- **Xi măng, thép:** quạt lò, băng tải liệu — nhóm tải tiêu thụ điện lớn nhất.
- **HVAC tòa nhà, nhà xưởng:** quạt AHU, bơm nước lạnh. Xem [PLC trong HVAC](/plc-trong-hvac/).

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá biến tần

Gửi cho chúng tôi: **công suất và dòng định mức động cơ · loại tải · điện áp lưới (1 pha/3 pha) · cách điều khiển mong muốn · môi trường lắp đặt (bụi, ẩm, nhiệt độ).**

Chúng tôi tư vấn chọn dòng phù hợp, kiểm tra nhu cầu điện trở xả và phụ kiện đi kèm, gửi báo giá kèm catalog.

**→ [Liên hệ báo giá biến tần](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Chọn biến tần theo kW hay theo dòng điện?**
Theo **dòng định mức của động cơ**. Cùng một mức kW, động cơ khác số cực hoặc khác hiệu suất sẽ có dòng khác nhau; chọn theo kW dễ bị thiếu dòng khi tải nặng.

**Có nên chọn biến tần công suất lớn hơn cho chắc?**
Lớn hơn một cấp là hợp lý với tải nặng hoặc khởi động khó. Lớn quá nhiều thì lãng phí và khả năng bảo vệ quá tải kém chính xác hơn.

**Biến tần dùng cho động cơ 1 pha được không?**
Phần lớn biến tần công nghiệp cấp nguồn cho **động cơ 3 pha**; nhiều dòng nhận điện vào 1 pha nhưng ngõ ra vẫn là 3 pha. Cần xác nhận rõ điện áp vào và ra khi chọn mã.

**Lắp biến tần có gây nhiễu cho thiết bị khác không?**
Có thể, nhất là với tín hiệu analog và truyền thông. Phòng ngừa bằng cách tách máng cáp động lực và tín hiệu, dùng cáp có lưới chống nhiễu, tiếp đất đúng và lắp lọc EMC khi cần.

**Có hỗ trợ chọn mã và báo giá nhanh không?**
Có. Gửi thông số động cơ và mô tả tải, đội kỹ thuật sẽ đề xuất dòng phù hợp kèm báo giá, hàng có CO/CQ và hóa đơn VAT.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /plc-la-gi/, /ket-noi-plc-bien-tan/, /plc-he-thong-bom/, /bo-chuyen-doi-tin-hieu-seneca/, /lien-he/. -->
