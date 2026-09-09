<!--
LOẠI TRANG : Bài kiến thức kỹ thuật (chuỗi biến tần — tầng 1) — Thông tin
URL SLUG   : /cau-tao-bien-tan/
TỪ KHÓA    : cấu tạo biến tần | các bộ phận của biến tần | igbt biến tần | tụ dc bus | mạch chỉnh lưu nghịch lưu
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 2/30 trong chuỗi biến tần.
-->

TITLE TAG   : Cấu Tạo Biến Tần – Các Bộ Phận Bên Trong Và Vai Trò Từng Khối
META (156)  : Cấu tạo biến tần gồm những gì? Phân tích chi tiết bộ chỉnh lưu, tụ DC bus, khối IGBT, vi điều khiển, mạch I/O và hệ tản nhiệt — bộ phận nào dễ hỏng và vì sao cần bảo trì.
H1          : Cấu Tạo Biến Tần – Bên Trong Có Những Gì?

---

## Vì sao nên hiểu cấu tạo biến tần?

Nhiều người vận hành coi biến tần là một "hộp đen": cắm điện vào, cài vài thông số, chạy được là xong. Cách nghĩ đó ổn cho tới khi máy báo lỗi lúc 2 giờ sáng.

Hiểu cấu tạo giúp bạn trả lời được những câu hỏi rất thực tế: **vì sao biến tần nóng thì hỏng nhanh?** **Vì sao phải chờ vài phút mới được mở nắp sau khi cắt điện?** **Vì sao bụi lại nguy hiểm đến vậy?** **Vì sao có biến tần dùng 10 năm, có cái 2 năm đã hỏng?** Tất cả đều nằm ở mấy khối linh kiện bên trong.

> **Cần tư vấn chọn biến tần bền cho môi trường nhà máy?** Gửi **công suất động cơ · loại tải · điều kiện tủ điện (nhiệt độ, bụi)** → [Nhận tư vấn](#bao-gia).

Bài này là bài **2/30** trong [chuỗi bài về biến tần](/bien-tan-la-gi/), tập trung mổ xẻ phần cứng.

---

## Nguyên lý xuyên suốt: AC → DC → AC

Trước khi đi vào từng khối, cần nắm dòng năng lượng đi qua biến tần theo ba chặng:

1. **Chỉnh lưu:** điện xoay chiều từ lưới → điện một chiều.
2. **Trung gian một chiều (DC bus):** lọc phẳng, tích trữ năng lượng.
3. **Nghịch lưu:** điện một chiều → điện xoay chiều với **tần số và điện áp do biến tần quyết định**.

Mọi bộ phận bên trong đều phục vụ một trong ba chặng này, hoặc phục vụ việc **điều khiển** và **làm mát** chúng. [Xem nguyên lý chi tiết →](/nguyen-ly-hoat-dong-bien-tan/)

---

## Các khối chính bên trong biến tần

| Khối | Linh kiện chính | Vai trò | Rủi ro hỏng |
|---|---|---|---|
| **Chỉnh lưu** | Cầu diode / SCR | Đổi AC → DC | Trung bình — hỏng khi sét, sốc điện |
| **Mạch nạp mềm** | Điện trở + relay/SCR | Nạp tụ từ từ khi bật nguồn | Relay dính, điện trở cháy |
| **DC bus** | Tụ điện phân dung lượng lớn | Lọc phẳng, tích trữ | **Cao — lão hoá theo nhiệt** |
| **Nghịch lưu** | Module **IGBT** + driver | Tạo AC tần số biến đổi | **Cao — sinh nhiệt lớn** |
| **Điều khiển** | Vi điều khiển / DSP | Thuật toán V/f, vector, PID, bảo vệ | Thấp |
| **Mạch I/O** | DI, AI, AO, relay, RS485 | Giao tiếp bên ngoài | Trung bình — hỏng do nhiễu, đấu sai |
| **Nguồn phụ** | SMPS | Cấp điện cho mạch điều khiển | Trung bình |
| **Tản nhiệt** | Lá nhôm + quạt | Thải nhiệt IGBT | **Cao — quạt kẹt, bụi bám** |
| **Bảo vệ** | Cảm biến dòng, nhiệt, áp | Phát hiện bất thường, báo lỗi | Thấp |

---

## Phân tích từng khối

### 1. Bộ chỉnh lưu — cửa vào

Thường là **cầu diode 6 xung** với biến tần 3 pha, hoặc cầu 4 diode với loại 1 pha. Nhiệm vụ đơn giản: chỉ cho dòng đi một chiều, biến AC thành DC còn gợn sóng.

Ở các dòng cao cấp có thể dùng **chỉnh lưu tích cực (active front end)** để giảm sóng hài và cho phép trả năng lượng về lưới khi hãm — nhưng loại này đắt và ít gặp ở nhà máy phổ thông.

### 2. Mạch nạp mềm — chi tiết nhỏ nhưng quan trọng

Khi vừa đóng điện, tụ DC bus đang rỗng nên hút một **dòng nạp rất lớn** — đủ để hỏng diode nếu không kiểm soát. Vì vậy có một **điện trở hạn dòng** mắc nối tiếp lúc khởi động, sau vài giây thì **relay hoặc SCR nối tắt** điện trở này.

Đây là lý do **không nên bật/tắt nguồn biến tần liên tục**. Mỗi lần đóng điện là một lần mạch nạp mềm làm việc; đóng cắt quá thường xuyên làm relay dính hoặc điện trở cháy. Muốn chạy/dừng thường xuyên, hãy dùng **lệnh chạy/dừng qua terminal**, giữ nguồn động lực luôn đóng.

### 3. Tụ DC bus — bộ phận có tuổi thọ hữu hạn

Đây là điểm quan trọng nhất cần nhớ. Tụ điện phân trong DC bus **lão hoá theo thời gian và nhiệt độ**: chất điện phân bay hơi dần, điện dung giảm, điện trở nội tăng. Quy luật chung trong ngành điện tử là **nhiệt độ càng cao, tuổi thọ tụ càng ngắn theo cấp số nhân**.

Hệ quả thực tế rất rõ: hai biến tần giống hệt nhau, một cái đặt trong tủ mát có quạt thông gió tốt, một cái đặt trong tủ kín cạnh lò nhiệt — tuổi thọ có thể chênh nhau gấp nhiều lần.

Tụ cũng là lý do của cảnh báo an toàn: **sau khi cắt điện, tụ vẫn giữ điện áp cao nguy hiểm trong vài phút**. Luôn chờ đúng thời gian ghi trên nhãn và **đo kiểm tra trước khi chạm vào**.

Dấu hiệu tụ xuống cấp: biến tần hay báo lỗi **quá áp/thấp áp DC bus** không rõ nguyên nhân, tụ phồng nắp, có vết rỉ chất điện phân.

### 4. Khối IGBT — trái tim và cũng là nguồn nhiệt

**IGBT (Insulated Gate Bipolar Transistor)** là van bán dẫn đóng/cắt hàng nghìn lần mỗi giây để tạo ra dạng sóng **PWM**. Mỗi lần đóng cắt đều sinh ra một lượng nhiệt nhỏ; nhân với tần số đóng cắt cao thì tổng nhiệt sinh ra rất đáng kể.

Có một đánh đổi kỹ thuật đáng biết: **tần số sóng mang (carrier frequency)** càng cao thì động cơ chạy càng êm và ít tiếng rít, nhưng **IGBT càng nóng** và **nhiễu điện từ phát ra càng mạnh**. Vì vậy khi biến tần hay báo quá nhiệt, một trong các cách xử lý là **giảm tần số sóng mang** — đổi lại chấp nhận tiếng ồn động cơ lớn hơn. [Xem xử lý lỗi quá nhiệt →](/loi-qua-nhiet-qua-tai-bien-tan/)

### 5. Vi điều khiển — phần "thông minh"

Chạy các thuật toán quyết định chất lượng điều khiển: **V/f vô hướng** (đơn giản) hay **vector** (mô-men khởi động cao, giữ tốc độ chính xác), bộ **PID** tích hợp, các lớp bảo vệ và ghi **lịch sử lỗi**.

Lịch sử lỗi là tính năng bị bỏ quên nhiều nhất nhưng cực kỳ hữu ích khi chẩn đoán: nó cho biết lỗi xảy ra lúc nào, ở tần số và dòng bao nhiêu. [Xem so sánh V/f và vector →](/che-do-dieu-khien-vf-vector/)

### 6. Mạch I/O — nơi giao tiếp

Gồm **ngõ vào số (DI)** cho lệnh chạy/dừng/đảo chiều, **ngõ vào analog (AI)** nhận 0–10V hoặc 4–20mA để đặt tần số, **ngõ ra analog (AO)** phản hồi, **relay** báo lỗi hoặc báo đang chạy, và cổng **RS485/Modbus** để nối [PLC](/plc-la-gi/).

Đây cũng là khối **dễ hỏng do đấu sai hoặc do nhiễu**. Cấp nhầm 220V vào chân điều khiển 24V là tai nạn phổ biến. [Xem cách đấu mạch điều khiển →](/dau-dieu-khien-bien-tan/)

### 7. Hệ tản nhiệt — nơi quyết định tuổi thọ

Gồm **lá nhôm tản nhiệt** và **quạt**. Nghe đơn giản nhưng đây là bộ phận liên quan trực tiếp tới phần lớn ca hỏng hóc thực tế: bụi bám kín khe tản nhiệt → nhiệt không thoát → IGBT và tụ nóng lên → tuổi thọ giảm nhanh, rồi báo lỗi quá nhiệt.

Vì vậy nội dung chính của bảo trì biến tần chỉ gói gọn trong hai việc: **giữ sạch và giữ mát**. [Xem quy trình bảo trì →](/bao-tri-bien-tan-dinh-ky/)

---

## Ứng dụng: hiểu cấu tạo giúp chẩn đoán nhanh hơn

Khi biết bên trong có gì, việc đọc mã lỗi trở nên logic thay vì đoán mò:

| Hiện tượng | Khối nghi ngờ | Hướng kiểm tra |
|---|---|---|
| Báo **quá nhiệt (OH)** | Tản nhiệt, quạt | Vệ sinh bụi, kiểm tra quạt, nhiệt độ tủ |
| Báo **quá áp DC (OV)** | DC bus, tải kéo | Kéo dài thời gian giảm tốc, xét điện trở hãm |
| Báo **thấp áp (LV)** | Nguồn vào, tụ, chỉnh lưu | Đo điện áp lưới, kiểm tra sụt áp, tuổi tụ |
| Báo **quá dòng (OC)** | IGBT, động cơ, cơ khí | Kiểm tra kẹt tải, cách điện động cơ, ACC |
| **Không lên nguồn** | Nguồn phụ, mạch nạp mềm | Kiểm tra cầu chì, relay nạp mềm |
| **Mất tín hiệu điều khiển** | Mạch I/O, nhiễu | Kiểm tra đấu dây, che chắn, nối đất |

[Xem chi tiết các lỗi thường gặp →](/loi-bien-tan-thuong-gap/)

---

## So sánh: vì sao biến tần cùng công suất lại chênh giá?

Nhiều khách hàng thắc mắc vì sao hai biến tần cùng ghi 7,5 kW mà giá chênh nhau đáng kể. Khác biệt thường nằm ở những chỗ không nhìn thấy:

**Chất lượng và dung lượng tụ DC bus.** Tụ tốt, chịu nhiệt cao, dung lượng dư dả sẽ bền hơn nhiều trong môi trường nóng.

**Module IGBT.** Dòng chịu đựng, khả năng quá tải ngắn hạn và chất lượng driver quyết định độ tin cậy khi tải nặng.

**Thiết kế tản nhiệt.** Diện tích lá nhôm, chất lượng quạt, đường dẫn gió — ảnh hưởng trực tiếp tuổi thọ.

**Thuật toán điều khiển.** Vector chất lượng cao cho mô-men khởi động tốt hơn hẳn V/f đơn giản.

**Khả năng quá tải.** Ví dụ 150% trong 60 giây so với 120% trong 30 giây là khác biệt lớn với tải nặng.

**Lớp phủ bảo vệ mạch.** Với môi trường ẩm, bụi kim loại hay hoá chất, mạch có phủ chống ẩm bền hơn nhiều.

**Hệ sinh thái hỗ trợ.** Tài liệu tiếng Việt, phần mềm, phụ tùng thay thế sau 5–10 năm. [Xem tiêu chí chọn hãng →](/so-sanh-cac-hang-bien-tan/)

Nói cách khác, **giá rẻ bất thường thường tương ứng với việc cắt giảm ở một trong những điểm trên** — và chỗ bị cắt giảm sẽ lộ ra sau vài năm vận hành trong môi trường nóng bụi của nhà máy Việt Nam.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn chọn biến tần **phù hợp môi trường lắp đặt**, không chỉ đúng công suất.
- ✅ Hàng **chính hãng**, CO/CQ, hoá đơn VAT, bảo hành rõ ràng.
- ✅ Hỗ trợ kiểm tra tủ điện, thông gió và phương án chống nhiễu.
- ✅ Hướng dẫn bảo trì để kéo dài tuổi thọ tụ và IGBT.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi: **công suất động cơ (kW) · dòng (A) · loại tải · nhiệt độ và độ bụi nơi lắp · có cần Modbus/PID không.**

**→ [Liên hệ tư vấn biến tần](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Biến tần gồm những bộ phận nào?**
Chính gồm **bộ chỉnh lưu, tụ DC bus, khối IGBT, vi điều khiển, mạch I/O, nguồn phụ và hệ tản nhiệt**.

**Bộ phận nào của biến tần dễ hỏng nhất?**
**Tụ DC bus** (lão hoá theo nhiệt) và **hệ tản nhiệt/quạt** (bụi bám). Cả hai đều xuống cấp nhanh khi tủ điện nóng và bẩn.

**Vì sao phải chờ vài phút mới được mở biến tần sau khi cắt điện?**
Vì **tụ DC bus vẫn tích điện áp cao** sau khi ngắt nguồn. Phải chờ đúng thời gian ghi trên nhãn và **đo kiểm tra** trước khi thao tác.

**Tần số sóng mang là gì và nên đặt bao nhiêu?**
Là tần số đóng cắt của IGBT. **Cao** thì động cơ êm hơn nhưng **IGBT nóng hơn và nhiễu mạnh hơn**; **thấp** thì mát hơn nhưng động cơ kêu. Cân bằng theo thực tế từng máy.

**Có nên bật/tắt nguồn biến tần thường xuyên không?**
Không nên. Mỗi lần đóng điện, **mạch nạp mềm** phải làm việc. Hãy giữ nguồn động lực và dùng **lệnh chạy/dừng qua terminal**.

**Biến tần cùng kW sao giá chênh nhiều?**
Khác nhau ở **chất lượng tụ, module IGBT, thiết kế tản nhiệt, khả năng quá tải, thuật toán điều khiển** và hệ thống hỗ trợ phụ tùng lâu dài.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /nguyen-ly-hoat-dong-bien-tan/, /bao-tri-bien-tan-dinh-ky/, /loi-bien-tan-thuong-gap/, /lien-he/. -->
