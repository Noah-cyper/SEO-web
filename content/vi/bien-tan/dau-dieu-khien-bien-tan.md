<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 3) — Thông tin
URL SLUG   : /dau-dieu-khien-bien-tan/
TỪ KHÓA    : đấu điều khiển biến tần | mạch điều khiển biến tần | chân di ai ao biến tần | npn pnp biến tần | đấu biến trở biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 13/30. Ký hiệu chân khác nhau theo hãng — đối chiếu tài liệu model.
-->

TITLE TAG   : Đấu Mạch Điều Khiển Biến Tần – DI, AI, AO, Relay Và RS485
META (156)  : Hướng dẫn đấu mạch điều khiển biến tần: chân DI chạy/dừng, chọn NPN hay PNP, đấu biến trở và cảm biến 4-20mA vào AI, ngõ ra AO và relay, cùng cách chống nhiễu cho cáp tín hiệu.
H1          : Đấu Mạch Điều Khiển Biến Tần (DI, AI, AO, Relay)

---

## Mạch điều khiển: nơi quyết định cách bạn vận hành máy

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Nếu mạch động lực trả lời câu hỏi *"điện đi đâu"*, thì mạch điều khiển trả lời câu hỏi *"ai ra lệnh và ra lệnh thế nào"*.

Đây là phần **linh hoạt nhất** của biến tần và cũng là nơi quyết định trải nghiệm vận hành: bạn muốn nhấn nút tại tủ, vặn biến trở, hay để PLC điều khiển hoàn toàn tự động?

Đây cũng là phần **dễ hỏng nhất do đấu sai** — cấp nhầm 220V vào chân điều khiển 24V là tai nạn xảy ra thường xuyên và thường phá hỏng bo mạch điều khiển.

> **Cần hỗ trợ thiết kế mạch điều khiển?** Gửi **model biến tần · cách muốn vận hành · thiết bị hiện có** → [Nhận hỗ trợ](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-pwm.svg)


Đây là bài **13/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Cấu tạo: các nhóm chân điều khiển

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-dieukhien.svg)


| Nhóm | Ký hiệu thường gặp | Chức năng |
|---|---|---|
| **Ngõ vào số (DI)** | X1–X6, S1–S6, DI1–DI6, FWD, REV | Nhận lệnh chạy, dừng, đảo chiều, chọn cấp tốc độ, reset lỗi |
| **Chân chung DI** | COM, SC, CM, DCM | Điểm chung cho các ngõ vào số |
| **Nguồn 24V nội** | +24V, PLC, P24 | Cấp nguồn cho tiếp điểm khô |
| **Ngõ vào analog (AI)** | AI1, AI2, VI, CI, AVI, ACI | Nhận tín hiệu đặt tần số (0–10V hoặc 4–20mA) |
| **Nguồn cho biến trở** | +10V, VR, VCC | Cấp nguồn cho biến trở ngoài |
| **Chân chung analog** | GND, ACM, AGND | Mát riêng cho tín hiệu analog |
| **Ngõ ra analog (AO)** | AO, FM, AM | Phản hồi tần số, dòng ra đồng hồ |
| **Ngõ ra relay** | TA/TB/TC, RA/RB/RC | Báo lỗi, báo đang chạy |
| **Ngõ ra transistor** | Y1, DO | Báo trạng thái tốc độ thấp/cao |
| **Truyền thông** | A+/B−, 485+/485− | RS485 Modbus |

> ⚠️ **Ký hiệu khác nhau đáng kể giữa các hãng.** Bài này trình bày nguyên tắc chung — luôn đối chiếu **tài liệu của model bạn đang dùng**.

---

## Ngõ vào số (DI): NPN hay PNP?

Đây là điểm gây nhầm lẫn nhiều nhất khi đấu mạch điều khiển.

**Khái niệm:** ngõ vào số nhận tín hiệu khi có dòng chạy qua. Nhưng dòng có thể chạy theo hai chiều tuỳ cách đấu:

**Chế độ NPN (sink).** Ngõ vào được kích hoạt khi **nối xuống chân COM (0V)**. Đây là kiểu phổ biến ở các thiết bị châu Á.

**Chế độ PNP (source).** Ngõ vào được kích hoạt khi **nối lên +24V**. Phổ biến ở thiết bị châu Âu.

Hầu hết biến tần có **cầu nối (jumper) hoặc công tắc gạt** để chọn chế độ. **Đặt sai chế độ thì nút nhấn sẽ không có tác dụng**, hoặc tệ hơn là ngõ vào luôn ở trạng thái tích cực khiến động cơ tự chạy khi cấp nguồn.

**Cách kiểm tra nhanh:** xem trong tài liệu vị trí jumper (thường ghi NPN/PNP hoặc SINK/SOURCE), xác nhận đúng kiểu thiết bị bạn nối vào — đặc biệt khi nối với **ngõ ra của PLC**, vì PLC cũng có kiểu NPN/PNP riêng.

---

## Các cách ra lệnh chạy/dừng

### Cách 1 — Hai dây (chạy/dừng bằng công tắc duy trì)

Dùng **một công tắc duy trì** nối chân FWD (chạy thuận) với COM. Đóng công tắc → chạy; mở → dừng.

Ưu điểm: đơn giản nhất. Nhược điểm: **nếu mất điện rồi có lại, máy tự chạy** khi công tắc vẫn đóng — nguy hiểm với một số ứng dụng. Cần cân nhắc kỹ về an toàn.

### Cách 2 — Ba dây (nút nhấn Start/Stop tự giữ)

Dùng **nút nhấn nhả** cho Start và Stop, biến tần tự giữ trạng thái bên trong (cấu hình qua thông số). Đây là cách **an toàn hơn** vì sau khi mất điện, máy không tự khởi động lại — phải nhấn Start lại.

Đây là cấu hình được khuyến nghị cho hầu hết máy công nghiệp.

### Cách 3 — Đảo chiều

Dùng thêm chân **REV (chạy nghịch)**. Lưu ý cần cấu hình **thời gian trễ khi đảo chiều** để động cơ dừng hẳn trước khi quay ngược, tránh dòng đảo chiều lớn.

### Cách 4 — Chọn cấp tốc độ cố định (multi-speed)

Kết hợp nhiều chân DI để chọn các cấp tần số đã cài sẵn. Ví dụ 3 chân DI cho tối đa 8 cấp tốc độ. Hữu ích cho băng tải nhiều tốc độ mà không cần biến trở hay PLC.

### Cách 5 — Reset lỗi từ xa

Một chân DI cấu hình làm **Reset** cho phép xoá lỗi mà không phải đến tận biến tần bấm nút.

---

## Ngõ vào analog (AI): đặt tần số

### Đấu biến trở (chỉnh tay)

Cấu hình cổ điển, dùng biến trở khoảng vài kΩ (theo khuyến nghị của hãng):

- Chân **+10V** của biến tần → một đầu biến trở
- Chân **AI** → đầu giữa (con chạy) của biến trở
- Chân **GND/ACM** → đầu còn lại

Vặn biến trở là đổi điện áp vào AI (0–10V), biến tần quy đổi thành tần số theo dải đã cài. Cần cài **tần số ứng với 0V và ứng với 10V** trong thông số.

### Đấu tín hiệu 4–20mA từ cảm biến

Dùng khi muốn biến tần chạy theo một đại lượng đo được (áp suất, lưu lượng, mức). Nối cảm biến vào chân AI được cấu hình ở **chế độ dòng** — thường phải gạt **jumper V/I** sang I hoặc đổi thông số.

Ưu điểm của 4–20mA so với 0–10V: **chống nhiễu tốt hơn nhiều** và **phát hiện được đứt dây** (dòng bằng 0 nghĩa là mất tín hiệu, khác với mức 4mA hợp lệ). Với khoảng cách xa, luôn ưu tiên 4–20mA. [Xem thêm về tín hiệu 4-20mA →](/ket-noi-plc-cam-bien-4-20ma/)

Kết hợp AI dạng dòng với **PID tích hợp** cho phép biến tần tự điều chỉnh tốc độ để giữ đại lượng đo ở mức đặt. [Xem chi tiết →](/dieu-khien-pid-bang-bien-tan/)

---

## Ngõ ra: AO, relay và transistor

**Ngõ ra analog (AO).** Xuất tín hiệu 0–10V hoặc 4–20mA tỉ lệ với tần số, dòng hoặc công suất. Dùng để đưa lên đồng hồ hiển thị, PLC hoặc hệ giám sát. Có thể ghép với [bộ hiển thị](/bo-hien-thi-seneca/) để xem tại tủ.

**Ngõ ra relay (tiếp điểm khô).** Thường có 3 chân: chung (TC), thường mở (TA), thường đóng (TB). Cấu hình phổ biến:
- **Báo lỗi** — nối đèn/còi cảnh báo hoặc báo về PLC
- **Báo đang chạy** — cho hệ giám sát biết trạng thái
- **Báo đạt tần số** — dùng cho khoá liên động

**Ngõ ra transistor.** Tương tự relay nhưng đóng cắt nhanh hơn, dòng nhỏ hơn, thường dùng báo trạng thái về PLC.

**Lưu ý về tải relay:** kiểm tra dòng và điện áp cho phép của tiếp điểm. Nếu cần đóng cắt tải lớn, dùng relay trung gian thay vì đấu thẳng.

---

## Ứng dụng: các cấu hình mạch điều khiển thực tế

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-plc.svg)


| Nhu cầu vận hành | Cấu hình đấu nối |
|---|---|
| **Đơn giản nhất** | Chạy/dừng và chỉnh tốc độ bằng bàn phím biến tần |
| **Vận hành tại tủ** | Nút Start/Stop → DI (3 dây) · biến trở → AI · đèn báo lỗi ← relay |
| **Đảo chiều** | Thêm nút REV → DI, cài trễ đảo chiều |
| **Nhiều cấp tốc độ cố định** | Công tắc chọn → nhiều DI · cài tần số từng cấp |
| **Tự động theo áp suất** | Cảm biến 4-20mA → AI · bật PID |
| **Điều khiển từ PLC (dây)** | PLC DO → DI · PLC AO → AI · relay biến tần → PLC DI |
| **Điều khiển từ PLC (truyền thông)** | RS485 Modbus — ít dây, nhiều dữ liệu |
| **Giám sát tại tủ** | AO → đồng hồ hiển thị tần số |

**Khi nào chọn dây, khi nào chọn truyền thông?** Nếu chỉ cần chạy/dừng và đặt một giá trị tần số, đấu dây đơn giản và tin cậy. Nếu cần **đọc nhiều thông số** (dòng, công suất, mã lỗi, trạng thái) hoặc điều khiển **nhiều biến tần**, thì **Modbus tiết kiệm dây và linh hoạt hơn nhiều**. [Xem chi tiết →](/dieu-khien-bien-tan-bang-plc/)

---

## Chống nhiễu cho mạch điều khiển

Đây là phần quyết định mạch điều khiển có chạy ổn định hay không. Biến tần phát nhiễu tần số cao rất mạnh, và **cáp tín hiệu là nạn nhân đầu tiên**.

**Quy tắc bắt buộc:**

1. **Cáp tín hiệu phải đi riêng máng** với cáp động lực. Nếu buộc phải cắt nhau, cắt **vuông góc**, không đi song song.
2. **Dùng cáp có lớp bọc chống nhiễu (shielded)** cho tín hiệu analog và truyền thông.
3. **Lớp bọc chỉ nối đất một đầu** — thường là đầu phía tủ điện. Nối cả hai đầu có thể tạo vòng đất gây nhiễu ngược.
4. **Giữ cáp tín hiệu càng ngắn càng tốt.**
5. **Dùng 4–20mA thay vì 0–10V** khi khoảng cách xa.
6. **Không đấu chung mát analog (ACM) với mát số (COM)** nếu tài liệu tách riêng chúng.
7. Với truyền thông RS485, dùng **cáp xoắn đôi có bọc** và lắp **điện trở đầu cuối 120Ω** ở hai đầu tuyến.

Nếu đã làm đúng các điểm trên mà vẫn nhiễu, cần xét đến lọc EMC, cuộn kháng và kiểm tra lại nối đất. [Xem chi tiết →](/chong-nhieu-emc-cho-bien-tan/)

---

## So sánh: các phương thức điều khiển

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vf-vector.svg)


| Phương thức | Ưu điểm | Nhược điểm | Phù hợp |
|---|---|---|---|
| **Bàn phím biến tần** | Không cần đấu gì thêm | Phải đến tận máy | Máy đơn giản, ít thao tác |
| **Nút nhấn + biến trở** | Trực quan, rẻ, dễ hiểu | Cố định tại tủ, ít dữ liệu | Xưởng nhỏ, vận hành thủ công |
| **Cảm biến + PID** | **Tự động hoàn toàn** | Cần cảm biến, phải chỉnh PID | Bơm giữ áp, quạt theo nhiệt |
| **PLC qua dây** | Tin cậy, đơn giản về giao thức | Nhiều dây, ít dữ liệu | Ít biến tần, logic đơn giản |
| **PLC qua Modbus** | **Ít dây, nhiều dữ liệu**, dễ mở rộng | Cần cấu hình truyền thông, nhạy nhiễu | Nhiều biến tần, cần giám sát |

---

## Sai lầm thường gặp

1. **Cấp 220V vào chân điều khiển 24V.** Hỏng bo mạch điều khiển ngay.
2. **Đặt sai jumper NPN/PNP.** Nút nhấn không tác dụng hoặc máy tự chạy.
3. **Đi chung cáp tín hiệu với cáp động lực.** Tín hiệu nhảy loạn, mất truyền thông.
4. **Dùng cấu hình 2 dây cho máy nguy hiểm.** Máy tự chạy lại khi có điện trở lại.
5. **Quên gạt jumper V/I** khi dùng cảm biến 4–20mA.
6. **Nối lớp bọc cáp ở cả hai đầu** tạo vòng đất.
7. **Đấu tải lớn trực tiếp vào relay biến tần** vượt dòng cho phép.
8. **Không cài lại thông số nguồn lệnh.** Đấu dây đúng nhưng biến tần vẫn nhận lệnh từ bàn phím vì chưa đổi thông số. [Xem hướng dẫn cài đặt →](/cai-dat-thong-so-bien-tan/)

---

## Cam kết tại HOANTRANTDH

- ✅ Cung cấp **sơ đồ chân điều khiển theo đúng model** bạn mua.
- ✅ Tư vấn thiết kế mạch điều khiển phù hợp cách vận hành thực tế.
- ✅ Hỗ trợ **cài thông số nguồn lệnh, dải AI, cấu hình relay** khi lắp đặt.
- ✅ Hỗ trợ ghép biến tần với [PLC](/plc-la-gi/) và cảm biến sẵn có.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ kỹ thuật & báo giá

Gửi: **model biến tần · cách muốn vận hành (nút nhấn/biến trở/cảm biến/PLC) · thiết bị hiện có · khoảng cách từ tủ tới nơi đặt nút.**

**→ [Liên hệ hỗ trợ đấu mạch điều khiển](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Chân DI của biến tần dùng để làm gì?**
Nhận **lệnh số**: chạy, dừng, đảo chiều, chọn cấp tốc độ, reset lỗi.

**NPN và PNP khác nhau thế nào?**
**NPN (sink)** kích hoạt khi nối xuống **COM (0V)**; **PNP (source)** kích hoạt khi nối lên **+24V**. Chọn sai thì nút nhấn không tác dụng.

**Đấu biến trở vào biến tần thế nào?**
**+10V** → một đầu biến trở, **AI** → con chạy giữa, **GND/ACM** → đầu còn lại. Sau đó cài dải tần số ứng với 0V và 10V.

**Nên dùng 0–10V hay 4–20mA?**
**4–20mA** khi khoảng cách xa hoặc môi trường nhiễu, vì chống nhiễu tốt hơn và **phát hiện được đứt dây**.

**Vì sao đấu dây xong mà nhấn nút không chạy?**
Thường do **chưa đổi thông số nguồn lệnh** từ bàn phím sang terminal, hoặc **đặt sai jumper NPN/PNP**.

**Cáp điều khiển đi chung máng với cáp động lực được không?**
**Không nên.** Phải đi riêng máng; nếu cắt nhau thì cắt **vuông góc** để giảm nhiễu.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /so-do-dau-day-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /dieu-khien-pid-bang-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /lien-he/. -->
