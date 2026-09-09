<!--
LOẠI TRANG : Bài kỹ thuật điện (chuỗi biến tần — tầng 8) — Thông tin → Thương mại
URL SLUG   : /bien-tan-chay-tren-may-phat-dien/
TỪ KHÓA    : biến tần chạy máy phát | biến tần và máy phát điện | chọn công suất máy phát cho biến tần | biến tần và ups | tải phi tuyến máy phát
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 43/50 trong chuỗi biến tần.
-->

TITLE TAG   : Biến Tần Chạy Trên Máy Phát Điện – Chọn Công Suất Và Lưu Ý
META (156)  : Vì sao biến tần chạy trên máy phát hay lỗi thấp áp, quá áp? Cách tính hệ số dự phòng công suất máy phát, xử lý sóng hài, năng lượng hãm và trình tự khởi động.

H1          : Biến Tần Chạy Trên Máy Phát Điện

---

## Lưới điện và máy phát không giống nhau

Trong tính toán thông thường, ta coi lưới điện là một **nguồn lý tưởng**: điện áp không đổi, tần số không đổi, cấp được bao nhiêu dòng cũng được. Giả định này gần đúng vì công suất của lưới lớn hơn tải rất nhiều lần.

Với **máy phát điện**, giả định đó sụp đổ. Máy phát là một nguồn có công suất **hữu hạn và tương đối gần với tải**, nên:

- **Điện áp sụt** khi tải tăng đột ngột, và cần thời gian để bộ điều áp (AVR) đưa về mức đặt.
- **Tần số dao động** khi tải thay đổi, vì động cơ sơ cấp cần thời gian để bộ điều tốc phản ứng.
- **Trở kháng nguồn cao hơn nhiều** so với lưới, nên dòng méo gây méo áp mạnh hơn.
- **Không hấp thụ được năng lượng dội ngược** — đây là điểm khác biệt nguy hiểm nhất.

Kết quả là một hệ chạy hoàn hảo trên lưới có thể **liên tục báo lỗi khi chuyển sang máy phát**: thấp áp khi khởi động, quá áp khi dừng, mất kết nối truyền thông, thiết bị điện tử khác trong hệ hoạt động bất thường.

Bài này giải thích cơ chế và đưa ra các nguyên tắc thiết kế cụ thể.

> **Hệ của bạn cần chạy được trên máy phát?** Gửi **công suất máy phát · tổng công suất biến tần · loại tải** → [Nhận tư vấn](#bao-gia).

Đây là bài **43/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: bốn xung đột giữa biến tần và máy phát

### 1. Sóng hài gây méo áp nặng hơn

Biến tần hút dòng theo xung nhọn, sinh sóng hài ([xem bài sóng hài](/song-hai-thd-bien-tan/)). Dòng méo này chảy qua **trở kháng của nguồn** và tạo ra sụt áp méo, làm méo luôn điện áp.

Trở kháng của máy phát **cao hơn nhiều so với lưới** — đó là bản chất của một nguồn công suất nhỏ. Cùng một dòng hài, mức méo áp trên máy phát sẽ **lớn hơn đáng kể** so với khi chạy lưới.

Hệ quả dây chuyền:
- **Điện áp méo** ảnh hưởng mọi thiết bị khác cùng chạy trên máy phát.
- **Bộ điều áp AVR** của máy phát đo điện áp méo và có thể điều chỉnh sai.
- **Cuộn dây máy phát nóng thêm** do dòng hài.
- Trường hợp nặng, máy phát có thể **mất ổn định điện áp**.

### 2. Không hấp thụ được năng lượng dội ngược

Đây là điểm khác biệt căn bản và nguy hiểm nhất.

Khi biến tần hãm động cơ, năng lượng dội về DC bus. Nếu vượt khả năng tiêu tán, biến tần báo quá áp ([xem bài lỗi quá áp](/loi-qua-ap-thap-ap-bien-tan/)).

Trên **lưới điện**, ngay cả khi năng lượng có đẩy ngược ra (với biến tần AFE), lưới là một "hồ chứa" khổng lồ hấp thụ được ngay.

Trên **máy phát**, không có hồ chứa nào. Năng lượng đẩy ngược sẽ **làm máy phát quay nhanh hơn** — hiện tượng gọi là **reverse power**. Hậu quả:
- **Tần số tăng** vượt ngưỡng.
- **Điện áp tăng** theo.
- Máy phát có thể **cắt bảo vệ** hoặc hư hỏng.

Vì vậy nguyên tắc quan trọng: **khi chạy trên máy phát, tuyệt đối không dùng biến tần AFE hoàn năng lượng** trừ khi hệ được thiết kế riêng cho việc đó. Với các tải có hãm, **phải dùng điện trở xả** để tiêu tán tại chỗ ([xem bài AFE](/bien-tan-hoan-nang-luong/)).

### 3. Sụt áp và dao động tần số khi tải thay đổi

Khi biến tần khởi động một động cơ lớn, dòng tăng nhanh. Máy phát **sụt áp tức thời** trước khi AVR kịp bù, và **tần số tụt** trước khi bộ điều tốc kịp tăng nhiên liệu.

Biến tần đo thấy DC bus tụt và **báo lỗi thấp áp** — dù thực ra nguồn vẫn "còn khỏe", chỉ là đang trong giai đoạn quá độ.

Ngược lại, khi tải giảm đột ngột (biến tần dừng), máy phát **vọt tốc độ và điện áp** trước khi điều chỉnh về, có thể gây lỗi quá áp.

### 4. Tần số không ổn định ảnh hưởng đồng bộ

Với hệ có nhiều biến tần cần đồng bộ, dao động tần số nguồn làm phức tạp thêm việc giữ đồng bộ ([xem bài đồng bộ](/dong-bo-nhieu-bien-tan/)).

---

## Cấu tạo giải pháp: thiết kế cho hệ chạy máy phát

### Chọn công suất máy phát — nguyên tắc dự phòng

Đây là quyết định quan trọng nhất. Nguyên tắc chung: **máy phát cấp cho tải biến tần phải có công suất lớn hơn đáng kể so với tổng công suất biến tần** — lớn hơn nhiều so với hệ số dự phòng thông thường dùng cho tải tuyến tính.

Lý do gồm ba phần cộng lại:

1. **Bù cho sóng hài** — dòng méo làm cuộn dây máy phát nóng hơn so với cùng một dòng hiệu dụng hình sin.
2. **Bù cho sụt áp quá độ** — cần biên để điện áp không tụt quá ngưỡng khi tải thay đổi.
3. **Bù cho dòng khởi động** — dù biến tần đã giảm dòng khởi động rất nhiều so với chạy trực tiếp, vẫn có đỉnh dòng.

Hệ số dự phòng cụ thể phụ thuộc vào:
- **Tỷ lệ tải phi tuyến** trên tổng tải máy phát — càng cao càng cần dự phòng nhiều.
- **Có cuộn kháng đầu vào hay không** — có thì giảm được yêu cầu dự phòng.
- **Loại máy phát** — một số dòng được thiết kế cho tải phi tuyến, chịu tốt hơn.
- **Đặc tính tải** — tải có hãm nhiều cần cân nhắc thêm.

**Cách làm đúng:** cung cấp cho nhà sản xuất máy phát thông tin về **tỷ lệ tải phi tuyến và loại thiết bị**, để họ tính chọn máy phù hợp. Đây không phải phép nhân đơn giản, và nhà sản xuất có dữ liệu về khả năng chịu tải phi tuyến của từng dòng máy.

### Các biện pháp kỹ thuật bắt buộc

| Biện pháp | Vì sao cần |
|---|---|
| **Cuộn kháng đầu vào cho mọi biến tần** | Giảm sóng hài — quan trọng hơn nhiều khi chạy máy phát |
| **Điện trở xả cho tải có hãm** | Máy phát **không hấp thụ được** năng lượng dội ngược |
| **Không dùng biến tần AFE** | Trả điện về máy phát gây reverse power |
| **Kéo dài thời gian tăng tốc** | Giảm sốc tải cho máy phát |
| **Khởi động tuần tự, không đồng thời** | Tránh dồn tải một lúc |
| **Nới rộng ngưỡng bảo vệ thấp áp/quá áp** (trong giới hạn cho phép) | Chịu được quá độ của máy phát |
| **Bật chức năng bù sụt áp thoáng qua** nếu biến tần có | Vượt qua các cú sụt ngắn |
| **Kiểm tra lại cấu hình truyền thông** | Dao động nguồn dễ gây rớt kết nối |

**Về khởi động tuần tự.** Đây là biện pháp không tốn tiền và hiệu quả nhất. Nếu hệ có nhiều biến tần, đừng để chúng khởi động cùng lúc khi máy phát vào. Dùng [PLC](/dieu-khien-bien-tan-bang-plc/) hoặc rơ-le thời gian để **khởi động lần lượt, cách nhau vài giây**, bắt đầu từ máy công suất lớn nhất.

**Về nới ngưỡng bảo vệ.** Cần thận trọng: chỉ nới trong giới hạn mà nhà sản xuất biến tần cho phép. Nới quá tay đồng nghĩa với việc để IGBT làm việc trong điều kiện điện áp không phù hợp ([xem bài lỗi thấp áp](/loi-qua-ap-thap-ap-bien-tan/)).

### Trình tự chuyển nguồn lưới ↔ máy phát

Đây là tình huống hay gây sự cố nhất:

1. **Mất lưới** → biến tần báo thấp áp và dừng (bình thường).
2. **Máy phát khởi động và ổn định** — mất một khoảng thời gian.
3. **Bộ chuyển nguồn (ATS) chuyển sang máy phát.**
4. **Chờ máy phát ổn định điện áp và tần số** trước khi cho tải vào.
5. **Khởi động tuần tự các biến tần.**

Lỗi phổ biến: bước 4 bị bỏ qua, tải được đóng ngay khi ATS chuyển, khiến máy phát phải gánh toàn bộ tải trong lúc chưa ổn định.

Cần lưu ý thêm về **cấu hình tự khởi động lại của biến tần**: nếu biến tần được đặt tự chạy lại khi có điện, tất cả sẽ cùng khởi động một lúc — đúng điều cần tránh. Với hệ chạy máy phát, nên **tắt tự khởi động lại** và điều khiển trình tự từ PLC.

---

## Ứng dụng: các tình huống thực tế

**Nhà máy có máy phát dự phòng cho toàn bộ sản xuất.** Cần tính toán kỹ nhất. Nên **phân loại tải theo mức ưu tiên** và chỉ cấp cho nhóm thiết yếu khi chạy máy phát, giảm yêu cầu công suất máy phát.

**Hệ bơm cứu hỏa, bơm thoát nước khẩn cấp.** Đây là ứng dụng mà việc chạy được trên máy phát là **bắt buộc theo thiết kế**. Cần thử nghiệm thực tế định kỳ, không chỉ tính toán.

**Công trường, khai thác mỏ, khu vực chưa có lưới.** Máy phát là nguồn chính, không phải dự phòng. Cần dự phòng công suất rộng rãi hơn và cuộn kháng đầu vào là bắt buộc.

**Tàu biển, giàn khoan.** Lưới điện độc lập hoàn toàn, công suất hữu hạn. Yêu cầu về chất lượng điện thường rất nghiêm ngặt, và bộ lọc sóng hài thường là bắt buộc.

**Hệ có UPS.** Một số hệ đặt biến tần sau UPS. Cần lưu ý: **UPS cũng là nguồn công suất hữu hạn** với các vấn đề tương tự máy phát, thậm chí nhạy hơn với tải phi tuyến. Phải kiểm tra UPS có được thiết kế cho tải phi tuyến hay không, và **tuyệt đối không đưa tải có hãm vào sau UPS** nếu không có điện trở xả.

### Kiểm chứng bằng thử nghiệm thực tế

Đây là phần không thể bỏ qua. Tính toán trên giấy không thay thế được thử nghiệm:

1. **Chạy thử toàn hệ trên máy phát** ở tải nặng nhất dự kiến.
2. **Đo điện áp và tần số máy phát** trong lúc khởi động từng biến tần.
3. **Đo THD áp** khi chạy trên máy phát và so với khi chạy lưới.
4. **Thử tình huống dừng đồng loạt** — xem có gây quá áp không.
5. **Thử chuyển nguồn lưới → máy phát và ngược lại** nhiều lần.
6. **Ghi lại toàn bộ số liệu** vào hồ sơ nghiệm thu ([xem bài nghiệm thu](/nghiem-thu-chay-thu-bien-tan/)).
7. **Lặp lại thử nghiệm định kỳ**, vì tải nhà máy thay đổi theo thời gian.

---

## So sánh: chạy trên lưới và chạy trên máy phát

| Tiêu chí | **Lưới điện** | **Máy phát** |
|---|---|---|
| Công suất nguồn | Rất lớn | **Hữu hạn, gần với tải** |
| Trở kháng nguồn | Thấp | **Cao** |
| Ổn định điện áp khi tải đổi | Tốt | **Sụt/vọt tạm thời** |
| Ổn định tần số | Rất ổn định | **Dao động** |
| Mức méo áp do sóng hài | Thấp | **Cao hơn nhiều** |
| Hấp thụ năng lượng dội ngược | Được | **Không được** |
| Dùng biến tần AFE | Được | **Không nên** |
| Yêu cầu cuộn kháng đầu vào | Nên có | **Bắt buộc** |
| Yêu cầu điện trở xả | Khi cần dừng nhanh | **Bắt buộc với tải có hãm** |
| Khởi động nhiều máy cùng lúc | Được | **Phải tuần tự** |
| Hệ số dự phòng công suất | Thông thường | **Cao hơn đáng kể** |

---

## Sai lầm thường gặp

1. **Chọn công suất máy phát bằng tổng công suất biến tần** — không tính dự phòng cho tải phi tuyến.
2. **Dùng biến tần AFE trên máy phát** — trả điện về gây reverse power, nguy hiểm cho máy phát.
3. **Không lắp cuộn kháng đầu vào** — méo áp nặng, ảnh hưởng cả các thiết bị khác.
4. **Bỏ điện trở xả** cho tải có hãm khi chạy máy phát.
5. **Để tất cả biến tần tự khởi động lại cùng lúc** khi máy phát vào.
6. **Đóng tải ngay khi ATS chuyển** mà không chờ máy phát ổn định.
7. **Không thử nghiệm thực tế**, chỉ tính toán trên giấy.
8. **Nới ngưỡng bảo vệ quá giới hạn cho phép** để hết báo lỗi.
9. **Không phân loại tải ưu tiên** — bắt máy phát gánh toàn bộ.
10. **Đưa tải có hãm vào sau UPS** mà không có điện trở xả.
11. **Không thử lại định kỳ** dù tải nhà máy đã thay đổi nhiều.
12. **Không thông báo tỷ lệ tải phi tuyến** cho nhà sản xuất máy phát khi tính chọn.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **yêu cầu dự phòng công suất máy phát** dựa trên tỷ lệ tải phi tuyến thực tế.
- ✅ Cảnh báo rõ các **cấu hình không được dùng** trên máy phát — đặc biệt là biến tần AFE.
- ✅ Tính chọn **cuộn kháng đầu vào và điện trở xả** cho hệ chạy máy phát.
- ✅ Hỗ trợ **quy trình khởi động tuần tự** và checklist thử nghiệm thực tế.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **công suất máy phát (hiện có hoặc dự kiến) · tổng công suất và số lượng biến tần · tỷ lệ tải phi tuyến trên tổng tải máy phát · tải có hãm không · máy phát là nguồn chính hay dự phòng · có UPS trong hệ không.**

**→ [Liên hệ nhận tư vấn hệ máy phát](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Biến tần chạy được trên máy phát điện không?**
**Được**, nhưng cần thiết kế đúng: dự phòng công suất máy phát rộng rãi, lắp cuộn kháng đầu vào, có điện trở xả cho tải có hãm và khởi động tuần tự.

**Chọn công suất máy phát cho tải biến tần thế nào?**
Phải **lớn hơn đáng kể** tổng công suất biến tần, vì cần bù cho sóng hài, sụt áp quá độ và dòng khởi động. Nên cung cấp **tỷ lệ tải phi tuyến** cho nhà sản xuất máy phát để họ tính chọn.

**Vì sao biến tần báo thấp áp khi chạy máy phát?**
Vì khi tải tăng đột ngột, máy phát **sụt áp tạm thời** trước khi bộ điều áp kịp bù. Biến tần đo thấy DC bus tụt và cắt bảo vệ.

**Có được dùng biến tần hoàn năng lượng (AFE) trên máy phát không?**
**Không nên.** Máy phát **không hấp thụ được năng lượng dội ngược**; điện trả về làm máy quay nhanh hơn, gây tăng tần số và điện áp, có thể hư hỏng.

**Tải có hãm chạy trên máy phát thì làm sao?**
**Bắt buộc dùng điện trở xả** để tiêu tán năng lượng tại chỗ, không để nó đẩy ngược về máy phát.

**Vì sao phải khởi động các biến tần tuần tự?**
Để **tránh dồn toàn bộ tải lên máy phát cùng một lúc**, gây sụt áp và tụt tần số vượt ngưỡng. Nên khởi động lần lượt, bắt đầu từ máy công suất lớn nhất.

**Có nên nới ngưỡng bảo vệ thấp áp để hết báo lỗi không?**
Chỉ **trong giới hạn nhà sản xuất cho phép**. Nới quá tay khiến IGBT làm việc ở điện áp không phù hợp, tăng nguy cơ hỏng thiết bị.

**Đặt biến tần sau UPS có được không?**
Cần kiểm tra kỹ. **UPS cũng là nguồn công suất hữu hạn** với các vấn đề tương tự máy phát, và thường nhạy hơn với tải phi tuyến. Tuyệt đối không đưa tải có hãm vào sau UPS nếu không có điện trở xả.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /song-hai-thd-bien-tan/, /loi-qua-ap-thap-ap-bien-tan/, /bien-tan-hoan-nang-luong/, /dong-bo-nhieu-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /nghiem-thu-chay-thu-bien-tan/, /lien-he/. -->
