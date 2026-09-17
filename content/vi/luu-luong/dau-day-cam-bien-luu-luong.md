<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật — chuỗi cảm biến lưu lượng — tầng 3
URL SLUG   : /dau-day-cam-bien-luu-luong/
TỪ KHÓA    : đấu dây cảm biến lưu lượng | tín hiệu 4-20ma | đầu ra xung | modbus lưu lượng | scale tín hiệu plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 14/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Đấu Dây Cảm Biến Lưu Lượng – 4-20mA, Xung, Modbus Và Scale
META (156)  : Cách đấu dây và chọn tín hiệu cho cảm biến lưu lượng: 4-20mA hai dây và bốn dây, đầu ra xung để đếm tổng, Modbus. Kèm cách scale trong PLC và lỗi hay gặp.

H1          : Đấu Dây Cảm Biến Lưu Lượng

---

## Đo đúng rồi vẫn có thể hiển thị sai

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-cam-bien-luu-luong.svg)


Một cảm biến lưu lượng lắp đúng vị trí, hiệu chuẩn tốt, vẫn có thể khiến hệ thống hiển thị con số sai — nếu phần đấu nối và quy đổi tín hiệu làm không đúng.

Ba lỗi kinh điển ở khâu này:

**1. Scale sai trong PLC.** Cảm biến xuất 4–20mA tương ứng 0–100 m³/h, nhưng PLC được lập trình quy đổi thành 0–50 m³/h. Con số hiển thị chỉ bằng một nửa thực tế, và không có gì báo lỗi.

**2. Dùng tín hiệu analog để tính tổng.** Lấy giá trị 4–20mA nhân với thời gian để cộng dồn. Sai số của từng lần đọc **tích lũy dần**, và sau một tháng tổng lệch đáng kể.

**3. Cấu hình sai đơn vị mỗi xung.** Thiết bị xuất một xung cho mỗi 10 lít, nhưng PLC đếm mỗi xung là 1 lít. Tổng sai gấp mười lần — và thường chỉ phát hiện khi có ai đó đối chiếu hóa đơn.

Cả ba đều không phải lỗi thiết bị và đều **phòng tránh được bằng một quy trình kiểm tra đơn giản**.

Bài này trình bày các kiểu tín hiệu, cách đấu nối, cách scale đúng, và quy trình kiểm chứng sau khi đấu.

> **Cần hỗ trợ đấu nối vào PLC hoặc bộ hiển thị?** Gửi **model thiết bị · hệ điều khiển đang dùng** → [Nhận hướng dẫn đấu nối](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-faraday.svg)


Đây là bài **14/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: bốn kiểu tín hiệu và mục đích của chúng

### 4–20mA — cho giá trị tức thời

Kiểu tín hiệu phổ biến nhất trong công nghiệp. Lưu lượng được biểu diễn bằng **dòng điện từ 4mA tới 20mA**.

**Vì sao là dòng chứ không phải áp:**
- **Không sụt theo khoảng cách** — dòng điện giữ nguyên trên cả tuyến dây dài.
- **Chống nhiễu tốt hơn** tín hiệu áp.
- **Phát hiện được đứt dây** — dòng bằng 0 là bất thường, trong khi 0V lại là một giá trị hợp lệ.

Điểm cuối cùng là lý do chuẩn này bắt đầu từ 4mA chứ không phải 0mA: **4mA là "sống và đang đọc giá trị nhỏ nhất", 0mA là "có sự cố"**.

**Hai kiểu đấu nối:**

**Loại hai dây (loop-powered).** Thiết bị **lấy nguồn từ chính vòng dòng điện** — chỉ cần hai sợi dây làm cả nhiệm vụ cấp nguồn lẫn truyền tín hiệu.
- Đơn giản nhất, ít dây nhất.
- Nhưng công suất tiêu thụ bị giới hạn nên **không phải thiết bị nào cũng làm được** — đồng hồ điện từ và Coriolis thường cần nguồn riêng.

**Loại bốn dây.** Hai dây cấp nguồn riêng (24VDC hoặc 220VAC), hai dây tín hiệu.
- Cần thêm dây nhưng không giới hạn công suất.
- Phổ biến với đồng hồ điện từ, Coriolis, thiết bị có màn hình lớn.

**Về nguồn cấp cho vòng dòng:** trong hệ hai dây, phải có **một nguồn duy nhất** cấp cho vòng — hoặc từ PLC (nếu module analog có cấp nguồn vòng), hoặc từ nguồn ngoài. **Cấp nguồn từ hai phía là lỗi đấu nối** và có thể hỏng thiết bị.

### Đầu ra xung — cho tổng tích lũy

Mỗi xung tương ứng với **một lượng thể tích cố định** đi qua: một xung = 1 lít, hoặc 10 lít, hoặc 1 m³ tùy cấu hình.

**Vì sao xung tốt hơn analog cho việc đếm tổng:**

Với analog, PLC phải **lấy mẫu định kỳ và nhân với thời gian** để cộng dồn. Mỗi lần lấy mẫu có sai số nhỏ, và các sai số này **tích lũy lại**. Nếu lưu lượng thay đổi nhanh giữa hai lần lấy mẫu, phần thay đổi đó bị bỏ sót hoàn toàn.

Với xung, mỗi xung **đại diện cho một lượng thể tích đã thực sự đi qua**. PLC chỉ việc đếm. **Không có sai số tích lũy**, và không bỏ sót gì kể cả khi lưu lượng biến động nhanh.

**Nguyên tắc:** nếu bạn cần **tổng chính xác** để tính chi phí hoặc mua bán, hãy dùng **đầu ra xung**, không dùng tích phân từ 4–20mA.

**Các kiểu đầu ra xung về mặt điện:**

| Kiểu | Đặc điểm |
|---|---|
| **Transistor NPN** | Kéo xuống mát khi có xung |
| **Transistor PNP** | Kéo lên nguồn dương khi có xung |
| **Tiếp điểm khô (relay/reed)** | Tần số thấp, dùng cho bộ đếm cơ |
| **Open collector** | Cần điện trở kéo lên phía nhận |
| **Namur** | Cho khu vực nguy hiểm cháy nổ |

**Phải khớp với đầu vào của PLC.** Đây là chỗ hay nhầm: PLC cấu hình cho đầu vào PNP mà thiết bị xuất NPN thì không nhận được xung nào — tương tự như vấn đề ở đầu vào số của biến tần ([xem bài đấu điều khiển biến tần](/dau-dieu-khien-bien-tan/)).

**Và phải kiểm tra tần số tối đa** mà đầu vào PLC đọc được. Đầu vào số thường có giới hạn tần số; nếu xung đến nhanh hơn, PLC **bỏ sót xung** và tổng thiếu.

### Modbus RTU — cho nhiều giá trị cùng lúc

Qua hai dây RS485, PLC đọc được cùng lúc:
- Lưu lượng tức thời
- Tổng tích lũy
- Nhiệt độ, áp suất (nếu thiết bị có)
- Khối lượng riêng (với Coriolis)
- Trạng thái và mã lỗi
- Các thông số cấu hình

**Ưu điểm:** một đường dây cho tất cả, **đọc được cả mã lỗi** — điều mà 4–20mA không làm được.

**Yêu cầu đấu nối:** cáp xoắn đôi có bọc, nối daisy-chain, **điện trở đầu cuối 120Ω ở hai đầu tuyến**, lớp bọc nối đất một đầu, và đi tách khỏi cáp động lực ([xem nguyên tắc tương tự ở bài biến tần](/dieu-khien-bien-tan-bang-plc/)).

**Lưu ý về tổng tích lũy đọc qua Modbus:** giá trị tổng là một con số lớn và có thể **tràn về 0** khi đạt giới hạn thanh ghi. Chương trình PLC cần xử lý tình huống này, nếu không sẽ có một lần nhảy âm trong dữ liệu.

### HART — 4–20mA kèm dữ liệu số

Tín hiệu số được điều chế chồng lên dòng 4–20mA. Vòng analog vẫn hoạt động bình thường, đồng thời truyền thêm dữ liệu.

**Ưu điểm:** cấu hình và chẩn đoán thiết bị từ xa mà **không phải đến tận nơi** — rất giá trị với thiết bị lắp ở vị trí khó tiếp cận.

### Tiếp điểm rơ-le — báo động ngưỡng

Đóng/mở khi lưu lượng vượt hoặc xuống dưới ngưỡng đặt. Dùng cho báo động, khóa liên động, hoặc dừng bơm khi mất dòng.

---

## Cấu tạo: scale tín hiệu đúng cách

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-dauday.svg)


Đây là khâu gây sai số nhiều nhất và cũng dễ kiểm tra nhất.

### Quy đổi 4–20mA sang giá trị kỹ thuật

Quan hệ là **tuyến tính**: 4mA ứng với giá trị đầu thang, 20mA ứng với giá trị cuối thang.

**Ba con số phải khớp nhau ở ba nơi:**

1. **Trên thiết bị** — thang đo đã cấu hình (ví dụ 0–100 m³/h ứng với 4–20mA).
2. **Trong PLC** — thông số scale của khối xử lý analog.
3. **Trên HMI/SCADA** — đơn vị và thang hiển thị.

Nếu ba nơi này không thống nhất, số hiển thị sai — và **không có cảnh báo nào**.

**Quy tắc thực hành:** khi nghiệm thu, hãy **ghi cả ba con số vào hồ sơ** và dán một bản trong tủ. Khi sau này có ai thay thiết bị hoặc sửa chương trình, họ có căn cứ đối chiếu.

### Kiểm chứng bằng phép thử ba điểm

Cách nhanh nhất để xác nhận scale đúng — làm được ngay tại tủ, không cần dòng chảy:

1. **Dùng chức năng mô phỏng đầu ra** của thiết bị (hầu hết thiết bị có), hoặc dùng bộ phát dòng chuẩn.
2. **Đặt 4mA** → PLC và HMI phải hiển thị **giá trị đầu thang**.
3. **Đặt 12mA** → phải hiển thị **đúng giữa thang**.
4. **Đặt 20mA** → phải hiển thị **giá trị cuối thang**.

Nếu cả ba điểm đều khớp, scale đúng. Nếu điểm giữa lệch, có thể chương trình đang áp dụng phép căn bậc hai không cần thiết (xem dưới).

Phép thử này mất năm phút và loại trừ được một trong những nguồn sai số phổ biến nhất.

### Bẫy: căn bậc hai với tín hiệu chênh áp

Đây là cái bẫy kinh điển khi dùng hệ đo chênh áp ([xem bài orifice](/luu-luong-ke-chenh-ap-orifice/)).

Với hệ orifice, **lưu lượng tỷ lệ với căn bậc hai của chênh áp**. Phép khai căn này phải được thực hiện **đúng một lần** — nhưng nó có thể được làm ở ba nơi:

- Trong **cảm biến chênh áp** (nếu bật chức năng khai căn).
- Trong **PLC**.
- Trong **phần mềm SCADA**.

**Nếu làm hai lần** → số sai hoàn toàn. **Nếu không làm lần nào** → cũng sai hoàn toàn.

Triệu chứng nhận biết: số hiển thị **đúng ở đầu thang và cuối thang nhưng sai ở giữa** — chính là điều mà phép thử ba điểm ở trên phát hiện ra.

**Quy tắc:** xác định rõ **khai căn được thực hiện ở đâu**, ghi vào hồ sơ, và đảm bảo các nơi còn lại đều tắt chức năng đó.

### Cấu hình đơn vị mỗi xung

Với đầu ra xung, phải thống nhất:

- **Một xung tương ứng bao nhiêu thể tích** — cấu hình trên thiết bị.
- **PLC cộng bao nhiêu cho mỗi xung** — trong chương trình.

Sai lệch ở đây làm tổng sai **theo bội số** (gấp 10, gấp 100 lần), không phải sai vài phần trăm. Đây là lỗi dễ phát hiện khi đối chiếu, nhưng thường chỉ được đối chiếu sau cả tháng.

**Kiểm chứng:** cho một lượng thể tích đã biết chạy qua (ví dụ bơm đầy một bể có dung tích biết trước) và so với số PLC cộng được.

---

## Ứng dụng: chọn tín hiệu theo mục đích

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-suachua.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-congnghe.svg)

| Mục đích | Tín hiệu nên dùng |
|---|---|
| **Hiển thị lưu lượng tức thời** | 4–20mA |
| **Phản hồi cho vòng điều khiển PID** | 4–20mA ([xem PID bằng biến tần](/dieu-khien-pid-bang-bien-tan/)) |
| **Đếm tổng để tính chi phí** | **Xung** |
| **Mua bán, giao nhận** | **Xung** + hiển thị tại chỗ |
| **Giám sát nhiều giá trị** | Modbus |
| **Cần đọc mã lỗi thiết bị** | **Modbus hoặc HART** |
| **Báo động ngưỡng, khóa liên động** | Tiếp điểm rơ-le |
| **Cấu hình thiết bị từ xa** | HART |
| **Thiết bị ở vị trí khó tiếp cận** | Modbus hoặc HART |

**Cấu hình phổ biến và hợp lý:** dùng **4–20mA cho giá trị tức thời** đưa vào điều khiển, **cộng thêm đầu ra xung cho tổng tích lũy**. Nhiều thiết bị có cả hai đầu ra cùng lúc — tận dụng được cả hai thế mạnh.

### Đi dây và chống nhiễu

Các nguyên tắc giống với mọi tín hiệu đo lường công nghiệp:

- **Cáp xoắn đôi có bọc chống nhiễu** cho tín hiệu analog và truyền thông.
- **Đi tách khỏi cáp động lực**; nếu buộc phải cắt nhau thì **cắt vuông góc**.
- **Lớp bọc nối đất một đầu**, phía tủ điện — nối hai đầu tạo vòng đất.
- **Không đi chung máng với cáp động cơ của biến tần** — đây là nguồn nhiễu mạnh nhất trong nhà máy ([xem bài chống nhiễu](/chong-nhieu-emc-cho-bien-tan/)).
- **Siết chắc đầu cốt** — tiếp xúc lỏng gây tín hiệu chập chờn khó chẩn đoán.
- **Ghi nhãn đầy đủ** hai đầu dây.

### Quy trình kiểm tra sau khi đấu nối

1. **Kiểm tra nguồn cấp** đúng điện áp và đúng cực.
2. **Đo dòng vòng 4–20mA** bằng đồng hồ — xác nhận nằm trong dải hợp lệ.
3. **Thử mô phỏng ba điểm** (4, 12, 20mA) và đối chiếu hiển thị ở PLC và HMI.
4. **Xác nhận vị trí khai căn** nếu là hệ chênh áp.
5. **Đếm xung thử** — cho một lượng thể tích đã biết đi qua và so với số PLC cộng.
6. **Thử ngắt dây tín hiệu** — PLC phải nhận biết được (dòng về 0).
7. **Thử báo động ngưỡng** nếu có.
8. **Chạy thử với dòng thật**, so với một nguồn tham chiếu nếu có.
9. **Ghi vào hồ sơ:** thang đo trên thiết bị, thông số scale trong PLC, đơn vị mỗi xung, vị trí khai căn.

Bước 9 là bước tốn ít thời gian nhất và tiết kiệm nhiều thời gian nhất về sau ([xem bài hiệu chuẩn](/hieu-chuan-cam-bien-luu-luong/)).

---

## So sánh các kiểu tín hiệu

| Tiêu chí | **4–20mA** | **Xung** | **Modbus** | **HART** |
|---|---|---|---|---|
| Giá trị tức thời | **Có** | Gián tiếp | **Có** | **Có** |
| Tổng tích lũy chính xác | Kém (tích lũy sai số) | **Tốt nhất** | **Tốt** | Tốt |
| Đọc nhiều giá trị | Không | Không | **Có** | **Có** |
| Đọc mã lỗi | Không | Không | **Có** | **Có** |
| Cấu hình từ xa | Không | Không | **Có** | **Có** |
| Số dây cho 1 thiết bị | 2–4 | 2–3 | 2 | 2–4 |
| Số dây cho 10 thiết bị | Nhiều | Nhiều | **Vẫn 2** | Nhiều |
| Chống nhiễu | **Tốt** | Tốt | Khá | Tốt |
| Phát hiện đứt dây | **Có** | Không trực tiếp | Có | **Có** |
| Đơn giản khi triển khai | **Nhất** | Đơn giản | Trung bình | Trung bình |

---

## Sai lầm thường gặp

1. **Scale trong PLC không khớp thang đo trên thiết bị** — số hiển thị sai mà không báo lỗi.
2. **Dùng tích phân 4–20mA để tính tổng** thay vì đầu ra xung — sai số tích lũy.
3. **Cấu hình sai đơn vị mỗi xung** — tổng sai theo bội số.
4. **Khai căn hai lần** hoặc **không khai căn lần nào** với hệ chênh áp.
5. **Đấu sai kiểu NPN/PNP** cho đầu ra xung — PLC không nhận được xung nào.
6. **Tần số xung vượt khả năng đọc của đầu vào PLC** — bỏ sót xung, tổng thiếu.
7. **Cấp nguồn vòng 4–20mA từ hai phía** — có thể hỏng thiết bị.
8. **Đi cáp tín hiệu chung máng với cáp động cơ biến tần** — nhiễu nặng.
9. **Nối lớp bọc cáp ở cả hai đầu** — tạo vòng đất.
10. **Không thử mô phỏng ba điểm** khi nghiệm thu.
11. **Không xử lý tình huống tổng tích lũy tràn về 0** khi đọc qua Modbus.
12. **Thiếu điện trở đầu cuối 120Ω** trên tuyến RS485.
13. **Không ghi thông số scale vào hồ sơ** — người sau không có căn cứ đối chiếu.

---

## Cam kết tại HOANTRANTDH

- ✅ **Cấu hình sẵn thang đo và đơn vị** theo yêu cầu trước khi giao thiết bị.
- ✅ Cung cấp **sơ đồ đấu nối cụ thể theo model** và theo hệ điều khiển khách đang dùng.
- ✅ Hướng dẫn **quy trình mô phỏng ba điểm** để kiểm chứng scale khi nghiệm thu.
- ✅ Hỗ trợ **bảng thanh ghi Modbus** và cấu hình truyền thông khi tích hợp vào [PLC](/plc-la-gi/).

---

<a name="bao-gia"></a>
## Nhận hướng dẫn đấu nối & báo giá

Gửi cho chúng tôi: **model cảm biến lưu lượng · hệ điều khiển đang dùng (PLC, bộ hiển thị, SCADA) · cần tín hiệu gì (tức thời, tổng, cả hai) · khoảng cách từ cảm biến tới tủ · môi trường đi cáp (có gần biến tần không) · nguồn cấp khả dụng tại vị trí lắp.**

**→ [Liên hệ nhận hỗ trợ đấu nối](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Nên dùng tín hiệu nào cho cảm biến lưu lượng?**
**4–20mA** cho giá trị tức thời và điều khiển; **đầu ra xung** cho tổng tích lũy; **Modbus** khi cần đọc nhiều giá trị và mã lỗi. Nhiều thiết bị có cả hai đầu ra cùng lúc.

**Vì sao không nên tính tổng từ tín hiệu 4–20mA?**
Vì PLC phải lấy mẫu định kỳ và nhân với thời gian, khiến **sai số tích lũy dần** và bỏ sót các biến động nhanh giữa hai lần lấy mẫu. **Đầu ra xung** không có vấn đề này.

**4–20mA hai dây và bốn dây khác nhau thế nào?**
**Hai dây (loop-powered)** lấy nguồn từ chính vòng dòng điện — đơn giản nhưng giới hạn công suất. **Bốn dây** có nguồn cấp riêng, dùng cho đồng hồ điện từ, Coriolis và thiết bị có màn hình lớn.

**Vì sao chuẩn bắt đầu từ 4mA chứ không phải 0mA?**
Để **phân biệt "giá trị nhỏ nhất" với "đứt dây"**. Dòng 4mA nghĩa là thiết bị đang sống và đọc giá trị đầu thang; dòng 0mA nghĩa là có sự cố.

**Làm sao kiểm tra scale đúng chưa?**
Dùng **chức năng mô phỏng ba điểm**: đặt 4mA, 12mA, 20mA và đối chiếu hiển thị ở PLC và HMI với giá trị đầu thang, giữa thang, cuối thang.

**Bẫy căn bậc hai với hệ chênh áp là gì?**
Phép khai căn phải làm **đúng một lần** — ở cảm biến, ở PLC hoặc ở SCADA. Làm **hai lần hoặc không lần nào** đều sai. Triệu chứng: đúng ở hai đầu thang nhưng sai ở giữa.

**Vì sao PLC không đếm được xung?**
Thường do **đấu sai kiểu NPN/PNP**, hoặc **tần số xung vượt khả năng đọc** của đầu vào số. Cần kiểm tra cả hai.

**Đi cáp tín hiệu cần lưu ý gì?**
**Cáp xoắn đôi có bọc**, **đi tách khỏi cáp động lực** (đặc biệt là cáp động cơ của biến tần), **lớp bọc nối đất một đầu** phía tủ.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /luu-luong-ke-chenh-ap-orifice/, /hieu-chuan-cam-bien-luu-luong/, /dau-dieu-khien-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /dieu-khien-pid-bang-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /plc-la-gi/, /lien-he/. -->
