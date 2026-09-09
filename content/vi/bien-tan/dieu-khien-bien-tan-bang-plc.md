<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 4) — Thông tin
URL SLUG   : /dieu-khien-bien-tan-bang-plc/
TỪ KHÓA    : điều khiển biến tần bằng plc | biến tần modbus rtu | plc điều khiển biến tần rs485 | thanh ghi biến tần | đa cấp tốc độ
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 21/30 trong chuỗi biến tần.
-->

TITLE TAG   : Điều Khiển Biến Tần Bằng PLC – Modbus RTU, Analog Hay Đa Cấp Tốc Độ
META (156)  : Ba cách điều khiển biến tần từ PLC: đầu ra số đa cấp tốc độ, analog 4-20mA và Modbus RTU. So sánh ưu nhược, cách đấu, thanh ghi và lỗi truyền thông hay gặp.

H1          : Điều Khiển Biến Tần Bằng PLC

---

## Ba cách để PLC ra lệnh cho biến tần

Khi biến tần được đưa vào một dây chuyền tự động hóa, nó không còn được vận hành bằng bàn phím nữa mà nhận lệnh từ **PLC**. Có ba cách để làm việc đó, khác nhau về số dây, chi phí và mức thông tin trao đổi được:

1. **Qua đầu ra số của PLC (DO → DI biến tần)** — dùng các tổ hợp tín hiệu để chọn **đa cấp tốc độ** đã cài sẵn.
2. **Qua đầu ra analog của PLC (AO → AI biến tần)** — đặt tần số **liên tục** bằng tín hiệu 4–20mA hoặc 0–10V.
3. **Qua truyền thông Modbus RTU (RS485)** — PLC vừa ra lệnh vừa **đọc ngược trạng thái** của biến tần.

Nhiều hệ thực tế dùng **kết hợp**: Modbus để đọc/ghi thông số và giám sát, cộng thêm một đường dây cứng cho lệnh dừng khẩn — vì lệnh an toàn không nên phụ thuộc vào truyền thông.

Bài này trình bày cả ba cách, tiêu chí chọn và những lỗi hay gặp khi đấu nối cũng như khi cấu hình truyền thông.

> **Đang tích hợp biến tần vào hệ PLC?** Gửi **model biến tần · model PLC · số điểm cần điều khiển** → [Nhận tư vấn phương án](#bao-gia).

Đây là bài **21/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: PLC và biến tần "nói chuyện" bằng gì

### Cách 1 — Đầu ra số và đa cấp tốc độ

Biến tần có sẵn chức năng **đa cấp tốc độ (multi-speed)**: bạn cài trước một loạt giá trị tần số vào thông số, rồi gán vài chân đầu vào số làm **chân chọn cấp**. Tổ hợp trạng thái của các chân đó quyết định biến tần chạy ở cấp nào.

Với **2 chân chọn** có 4 tổ hợp, **3 chân chọn** có 8 tổ hợp, **4 chân** có 16. Cộng thêm một chân cho lệnh chạy/dừng và một chân đảo chiều.

PLC chỉ cần **đóng/mở các đầu ra số** — đơn giản, không cần module đặc biệt, không cần lập trình truyền thông.

Điểm quan trọng khi đấu: phải xác định biến tần dùng **kiểu NPN (sink) hay PNP (source)** và cấu hình cho khớp với đầu ra PLC. Đấu sai kiểu là nguyên nhân số một khiến "PLC xuất tín hiệu mà biến tần không nhận" ([xem chi tiết đấu điều khiển](/dau-dieu-khien-bien-tan/)).

### Cách 2 — Đầu ra analog

PLC có module đầu ra analog xuất tín hiệu **4–20mA** hoặc **0–10V**, nối vào chân AI của biến tần. Tần số biến tần thay đổi **liên tục theo giá trị tín hiệu**.

Đây là cách phù hợp khi tốc độ cần thay đổi mượt theo một đại lượng tính toán trong PLC — ví dụ PLC chạy vòng điều khiển và xuất kết quả ra biến tần.

**Nên ưu tiên 4–20mA hơn 0–10V** trên nhà máy vì: chống nhiễu tốt hơn, không bị sụt áp trên khoảng cách xa, và **phát hiện được đứt dây** (dòng bằng 0 là bất thường, trong khi 0V lại là một giá trị hợp lệ).

Hạn chế: một đường analog chỉ truyền được **một giá trị một chiều**. Vẫn cần thêm dây cứng cho lệnh chạy/dừng, và PLC không biết biến tần đang bị lỗi gì.

### Cách 3 — Modbus RTU trên RS485

Đây là cách được dùng nhiều nhất trong hệ hiện đại. Chỉ với **một đôi dây xoắn**, PLC có thể:

- Ghi lệnh **chạy / dừng / đảo chiều / reset lỗi**.
- Ghi **giá trị tần số đặt**.
- Đọc **tần số thực, dòng, điện áp, công suất, nhiệt độ, mã lỗi, trạng thái**.
- **Ghi và đọc thông số** cài đặt của biến tần.

Và quan trọng nhất: **một đường bus nối được nhiều biến tần** (thường tới hàng chục thiết bị), mỗi cái một địa chỉ. So với việc kéo hàng chục cặp dây analog và hàng trăm dây DI, khác biệt về công lắp đặt là rất lớn.

Modbus RTU hoạt động theo mô hình **master–slave**: PLC là master, các biến tần là slave. Master hỏi, slave trả lời — slave không bao giờ tự phát.

---

## Cấu tạo cấu hình Modbus: những gì phải khớp

Để hai thiết bị nói chuyện được, một loạt tham số phải **giống hệt nhau ở cả hai đầu**:

| Tham số | Ý nghĩa | Lưu ý |
|---|---|---|
| **Địa chỉ slave** | Số hiệu của biến tần trên bus | **Không được trùng** giữa các biến tần |
| **Tốc độ baud** | 9600 / 19200 / 38400… | Phải khớp master; baud cao thì cáp phải tốt |
| **Số bit dữ liệu** | Thường 8 | |
| **Parity** | None / Even / Odd | Nguồn sai cấu hình rất phổ biến |
| **Stop bit** | 1 hoặc 2 | Đi kèm với lựa chọn parity |
| **Nguồn lệnh** | Phải đặt là **truyền thông** | Quên bước này thì ghi lệnh không có tác dụng |
| **Nguồn đặt tần số** | Phải đặt là **truyền thông** | Độc lập với nguồn lệnh |
| **Xử lý khi mất truyền thông** | Dừng / giữ tốc độ / báo lỗi | Nên đặt là **dừng an toàn** |
| **Thời gian timeout** | Ngưỡng coi là mất kết nối | Đặt phù hợp chu kỳ quét của PLC |

Bên cạnh đó là phần **thanh ghi**. Mỗi hãng biến tần định nghĩa bản đồ thanh ghi riêng — địa chỉ để ghi lệnh chạy, địa chỉ để ghi tần số, địa chỉ để đọc dòng… đều khác nhau. **Bắt buộc phải tra tài liệu truyền thông của đúng model** đang dùng; không có bản đồ dùng chung cho mọi hãng.

Một điểm hay nhầm: **đơn vị của giá trị tần số**. Nhiều biến tần nhận tần số theo đơn vị 0,01Hz, nghĩa là muốn đặt 50Hz phải ghi số 5000. Có dòng lại nhận theo **phần trăm của tần số lớn nhất**. Ghi sai đơn vị dẫn tới động cơ chạy sai tốc độ hoàn toàn.

### Phần cứng RS485 cần đúng

- **Cáp xoắn đôi có bọc chống nhiễu** — không dùng cáp mạng thường.
- **Nối theo kiểu daisy-chain** (nối tiếp từ thiết bị này sang thiết bị kế), **không nối hình sao**.
- **Điện trở đầu cuối 120Ω ở hai đầu tuyến** — thiếu là nguyên nhân kinh điển gây rớt gói ngẫu nhiên.
- **Lớp bọc nối đất một đầu**, phía tủ.
- **Đi cáp tách khỏi cáp động lực**, cắt vuông góc nếu buộc phải cắt ([xem bài chống nhiễu](/chong-nhieu-emc-cho-bien-tan/)).
- Chú ý **đúng cực A/B (D+/D−)** — đảo là không có truyền thông.

---

## Ứng dụng: chọn cách nào cho hệ của bạn

| Tình huống | Nên chọn |
|---|---|
| Máy đơn, chỉ cần vài tốc độ cố định | **Đa cấp tốc độ qua DI** |
| Cần tốc độ thay đổi mượt theo tính toán của PLC | **Analog 4–20mA** |
| Nhiều biến tần trong một dây chuyền | **Modbus RTU** |
| Cần giám sát dòng, lỗi, trạng thái từ SCADA | **Modbus RTU** |
| Cần thay đổi thông số biến tần từ xa | **Modbus RTU** |
| Yêu cầu an toàn nghiêm ngặt cho lệnh dừng | **Dây cứng**, không qua truyền thông |
| Khoảng cách xa, môi trường nhiễu mạnh | **Modbus RTU** hoặc analog **4–20mA** |
| Hệ cũ, PLC không có cổng truyền thông | Đa cấp tốc độ hoặc analog |

**Phương án kết hợp được khuyến nghị cho dây chuyền thực tế:**

- **Modbus RTU** cho toàn bộ lệnh vận hành và giám sát.
- **Một chân DI dây cứng** cho lệnh dừng khẩn hoặc chân cho phép chạy (enable).
- Cấu hình biến tần **tự dừng khi mất truyền thông** quá thời gian timeout.

Cách này giữ được sự gọn gàng của truyền thông mà vẫn đảm bảo chức năng dừng không phụ thuộc vào phần mềm và đường bus.

### Trình tự tích hợp thực tế

1. **Đấu nguồn và động lực**, chạy thử biến tần bằng bàn phím trước ([xem sơ đồ đấu dây](/so-do-dau-day-bien-tan/)).
2. **Cài thông số động cơ** và giới hạn tần số ([xem quy trình cài đặt](/cai-dat-thong-so-bien-tan/)).
3. **Đặt địa chỉ và tham số truyền thông** cho từng biến tần, ghi vào bảng.
4. **Đấu RS485**, lắp điện trở đầu cuối, kiểm tra đúng cực.
5. **Thử đọc trước, ghi sau** — đọc một thanh ghi trạng thái để xác nhận đường truyền thông đã thông.
6. **Chuyển nguồn lệnh và nguồn tần số sang truyền thông.**
7. **Thử ghi tần số**, kiểm tra động cơ chạy đúng tốc độ mong muốn.
8. **Thử ngắt cáp truyền thông** để xác nhận biến tần dừng đúng như cấu hình.
9. Ghi lại toàn bộ **bảng địa chỉ, thanh ghi và tham số** vào hồ sơ hệ thống.

Bước 5 và bước 8 hay bị bỏ qua nhất, và cũng là hai bước tiết kiệm nhiều thời gian nhất về sau.

---

## So sánh ba phương án

| Tiêu chí | **DI đa cấp** | **Analog** | **Modbus RTU** |
|---|---|---|---|
| Số dây cho 1 biến tần | Nhiều (4–6 dây) | 2–4 dây | **2 dây, dùng chung** |
| Số dây cho 10 biến tần | Rất nhiều | Rất nhiều | **Vẫn 2 dây** |
| Tốc độ đặt được | Vài cấp cố định | **Liên tục** | **Liên tục** |
| Đọc ngược trạng thái | Không | Không | **Có, đầy đủ** |
| Đọc mã lỗi | Không | Không | **Có** |
| Ghi thông số từ xa | Không | Không | **Có** |
| Cần lập trình | Rất ít | Ít | Trung bình |
| Cần module PLC riêng | Không (dùng DO sẵn có) | **Có (module AO)** | Có (cổng RS485) |
| Chống nhiễu | Tốt | Khá (4–20mA) | Khá, cần cáp đúng chuẩn |
| Độ tin cậy khi sự cố | **Cao nhất** | Cao | Phụ thuộc cáp và cấu hình |
| Chi phí mở rộng | Tăng nhanh | Tăng nhanh | **Gần như không tăng** |

---

## Sai lầm thường gặp

1. **Quên chuyển nguồn lệnh và nguồn tần số sang "truyền thông"** — đấu đúng, cấu hình đúng, mà biến tần vẫn không nhận lệnh.
2. **Trùng địa chỉ slave** giữa hai biến tần trên cùng bus.
3. **Sai parity hoặc baud** ở một thiết bị trong tuyến.
4. **Thiếu điện trở đầu cuối 120Ω** — chạy được lúc đầu rồi rớt gói ngẫu nhiên khi tải nặng.
5. **Nối RS485 hình sao** thay vì daisy-chain.
6. **Đảo cực A/B**.
7. **Ghi sai đơn vị tần số** (quên hệ số 0,01Hz) khiến động cơ chạy sai tốc độ.
8. **Dùng truyền thông cho lệnh dừng khẩn** — vi phạm nguyên tắc an toàn.
9. **Không cấu hình xử lý khi mất truyền thông** — biến tần giữ nguyên tốc độ dù PLC đã mất kết nối.
10. **Đấu sai kiểu NPN/PNP** khi dùng đầu ra số của PLC.
11. **Đi cáp RS485 chung máng với cáp động cơ** — nhiễu, rớt kết nối khi biến tần chạy.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **chọn phương án điều khiển** phù hợp quy mô hệ thống, không mặc định bán thêm module.
- ✅ Hỗ trợ **bảng thanh ghi Modbus** theo đúng model biến tần khách đang dùng.
- ✅ Cài sẵn **địa chỉ và tham số truyền thông** trước khi giao hàng theo yêu cầu.
- ✅ Cung cấp đồng bộ [biến tần](/bien-tan-la-gi/), [PLC](/plc-la-gi/), cáp truyền thông và phụ kiện tủ điện.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **model biến tần · model PLC · số lượng biến tần trong hệ · khoảng cách đi cáp · yêu cầu giám sát (chỉ chạy/dừng hay cần đọc dòng, lỗi, năng lượng).**

**→ [Liên hệ nhận tư vấn tích hợp](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Điều khiển biến tần bằng PLC có mấy cách?**
Ba cách: **đầu ra số chọn đa cấp tốc độ**, **đầu ra analog 4–20mA/0–10V**, và **truyền thông Modbus RTU** qua RS485.

**Khi nào nên dùng Modbus thay vì analog?**
Khi có **nhiều biến tần**, cần **đọc ngược trạng thái và mã lỗi**, hoặc cần thay đổi thông số từ xa. Modbus chỉ dùng hai dây cho cả tuyến.

**Một tuyến RS485 nối được bao nhiêu biến tần?**
Tùy chuẩn và thiết bị, thường **tới hàng chục thiết bị** trên một tuyến, mỗi thiết bị một địa chỉ khác nhau.

**Vì sao PLC ghi lệnh mà biến tần không chạy?**
Phổ biến nhất là **chưa chuyển nguồn lệnh và nguồn đặt tần số sang "truyền thông"** trong thông số biến tần.

**Vì sao truyền thông chạy được lúc đầu rồi hay rớt?**
Thường do **thiếu điện trở đầu cuối 120Ω**, cáp không đúng chuẩn, hoặc cáp RS485 đi chung máng với cáp động lực.

**Ghi tần số 50Hz thì ghi số bao nhiêu?**
Tùy model. Nhiều biến tần dùng **đơn vị 0,01Hz** nên phải ghi 5000; một số dòng lại nhận theo **phần trăm tần số lớn nhất**. Phải tra tài liệu của đúng model.

**Có nên dùng truyền thông cho lệnh dừng khẩn không?**
**Không.** Lệnh dừng khẩn phải đi **dây cứng**, độc lập với phần mềm và đường bus.

**Mất kết nối PLC thì biến tần xử lý ra sao?**
Theo thông số bạn cài. Nên đặt là **dừng an toàn sau thời gian timeout**, và luôn kiểm chứng bằng cách rút thử cáp truyền thông khi nghiệm thu.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /dau-dieu-khien-bien-tan/, /so-do-dau-day-bien-tan/, /cai-dat-thong-so-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /plc-la-gi/, /lien-he/. -->
