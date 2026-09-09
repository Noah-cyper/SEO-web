<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 3) — Thông tin
URL SLUG   : /chon-cap-aptomat-cho-bien-tan/
TỪ KHÓA    : chọn aptomat cho biến tần | chọn cáp cho biến tần | mccb biến tần | cáp bọc chống nhiễu | rccb biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 14/30. Luôn tuân thủ tiêu chuẩn lắp đặt và tài liệu hãng.
-->

TITLE TAG   : Chọn Cáp Và Aptomat Cho Biến Tần – Tính Đúng Theo Dòng Đầu Vào
META (156)  : Hướng dẫn chọn aptomat và cáp cho biến tần: vì sao phải tính theo dòng đầu vào chứ không phải dòng động cơ, chọn cáp bọc chống nhiễu, lưu ý về RCCB chống giật và cách đi cáp.
H1          : Chọn Cáp Và Aptomat Cho Biến Tần

---

## Sai lầm phổ biến: chọn theo dòng động cơ

Khi lắp biến tần, rất nhiều người chọn aptomat theo **dòng định mức của động cơ** — giống như khi đấu trực tiếp. Đây là cách làm **sai** và gây ra hai vấn đề trái ngược nhau:

- **Aptomat nhảy liên tục** (nếu chọn thiếu), đặc biệt lúc đóng điện
- **Không bảo vệ được cáp** (nếu chọn thừa)

Nguyên tắc đúng:

> **Aptomat và cáp phía nguồn phải chọn theo DÒNG ĐẦU VÀO CỦA BIẾN TẦN**, không phải theo dòng động cơ.

Vì sao? Vì biến tần là một tải điện tử, và **dòng ở phía vào khác với dòng ở phía ra**. Với biến tần 3 pha vào, dòng vào thường xấp xỉ dòng ra nhưng vẫn có chênh lệch. Với **biến tần 1 pha vào – 3 pha ra**, chênh lệch này rất lớn: toàn bộ công suất dồn vào một pha. [Xem chi tiết →](/bien-tan-1-pha-ra-3-pha/)

> **Cần tính giúp cáp và aptomat?** Gửi **model biến tần · công suất động cơ · chiều dài cáp** → [Nhận tư vấn](#bao-gia).

Đây là bài **14/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Cấu tạo bài toán: các thông số cần có

Trước khi tính, hãy thu thập:

| Thông số | Lấy ở đâu | Dùng để làm gì |
|---|---|---|
| **Dòng đầu vào định mức của biến tần** | **Catalogue biến tần** | Chọn aptomat và cáp phía nguồn |
| **Dòng đầu ra định mức** | Catalogue biến tần | Chọn cáp tới động cơ |
| **Dòng động cơ** | Nhãn động cơ | Kiểm tra tương thích |
| **Chiều dài cáp** | Đo thực tế | Kiểm tra sụt áp, xét cuộn kháng |
| **Nhiệt độ môi trường & cách lắp cáp** | Khảo sát | Hệ số hiệu chỉnh tiết diện cáp |
| **Khuyến nghị của hãng** | Tài liệu model | Nhiều hãng ghi sẵn cỡ aptomat/cáp |

**Mẹo tiết kiệm thời gian:** phần lớn hãng biến tần **đã ghi sẵn bảng khuyến nghị** cỡ aptomat, cầu chì và tiết diện cáp cho từng model trong tài liệu kỹ thuật. Hãy dùng bảng đó làm căn cứ chính, các nguyên tắc dưới đây để kiểm tra chéo.

---

## Chọn aptomat (MCCB/MCB)

### Nguyên tắc cơ bản

**Dòng định mức aptomat ≥ dòng đầu vào định mức của biến tần**, có cộng thêm biên dự phòng theo khuyến nghị của hãng.

### Vì sao cần biên dự phòng?

Vì lúc **đóng điện lần đầu**, biến tần hút một **dòng nạp tụ** lớn trong thời gian rất ngắn. Dù đã có mạch nạp mềm hạn chế, xung dòng này vẫn có thể làm nhảy aptomat nếu chọn quá sát.

### Chọn đường cong đặc tính

Aptomat có nhiều loại đường cong (B, C, D) phản ánh khả năng chịu dòng xung:

| Đường cong | Đặc điểm | Dùng cho |
|---|---|---|
| **B** | Nhạy nhất, cắt sớm | Tải thuần trở, chiếu sáng |
| **C** | Trung bình | **Phổ biến cho biến tần** |
| **D** | Chịu xung cao nhất | Tải có dòng khởi động rất lớn |

Với biến tần, **loại C** thường phù hợp. Nếu hay bị nhảy lúc đóng điện dù đã chọn đủ dòng, có thể cân nhắc loại D — nhưng phải đảm bảo vẫn bảo vệ được cáp.

### Cầu chì bán dẫn

Với biến tần công suất lớn, một số hãng khuyến nghị dùng thêm **cầu chì tác động nhanh (semiconductor fuse)** để bảo vệ IGBT khi ngắn mạch. Aptomat thông thường cắt chậm hơn tốc độ hỏng của bán dẫn. Đây là hạng mục nên làm theo đúng khuyến nghị của hãng.

---

## Vấn đề RCCB / RCD (chống giật)

Đây là điểm kỹ thuật quan trọng và hay gây bực bội khi lắp đặt.

**Hiện tượng:** lắp biến tần xong, **aptomat chống giật nhảy liên tục** dù không có sự cố gì.

**Nguyên nhân:** biến tần tạo ra **dòng rò tần số cao** qua điện dung ký sinh giữa cuộn dây động cơ và vỏ, cũng như qua tụ lọc EMC bên trong biến tần. Đây là **dòng rò bình thường về mặt kỹ thuật**, không phải sự cố — nhưng RCCB thông thường lại nhìn thấy nó và cắt.

**Các yếu tố làm dòng rò tăng:**
- Cáp tới động cơ **càng dài** thì dòng rò càng lớn
- **Tần số sóng mang càng cao** thì dòng rò càng lớn
- Có **lọc EMC** thì dòng rò tăng thêm
- Nhiều biến tần chung một RCCB thì dòng rò **cộng dồn**

**Hướng xử lý:**

1. Dùng **RCCB loại B** (hoặc loại được nhà sản xuất xác nhận phù hợp với bộ biến đổi tần số) thay vì loại AC thông thường — vì loại AC không phát hiện đúng dòng rò có thành phần một chiều và tần số cao.
2. Chọn **ngưỡng tác động phù hợp** theo tính toán, cân bằng giữa an toàn và khả năng vận hành.
3. **Mỗi biến tần một RCCB riêng** thay vì gộp chung nhiều máy.
4. **Giảm tần số sóng mang** để giảm dòng rò.
5. **Rút ngắn cáp động cơ** nếu có thể.
6. **Nối đất thật tốt** — nối đất kém làm dòng rò tìm đường khác và gây nhiễu. [Xem chi tiết →](/so-do-dau-day-bien-tan/)

> ⚠️ Việc lựa chọn thiết bị bảo vệ chống giật liên quan trực tiếp tới **an toàn tính mạng** và phải tuân thủ **quy định lắp đặt điện hiện hành**. Hãy làm việc với kỹ sư điện có chuyên môn, **không tự ý bỏ RCCB** chỉ vì nó hay nhảy.

---

## Chọn cáp động lực

### Cáp phía nguồn (từ aptomat tới biến tần)

Chọn theo **dòng đầu vào của biến tần**, có xét:
- **Hệ số hiệu chỉnh theo nhiệt độ** môi trường
- **Cách lắp đặt** (trong ống, trên máng, chôn ngầm — mỗi kiểu có khả năng tản nhiệt khác nhau)
- **Số mạch đi chung** trong cùng máng
- **Sụt áp** nếu tuyến cáp dài

### Cáp phía động cơ (từ biến tần tới động cơ)

Đây là đoạn cáp **đặc biệt** vì nó mang dòng có tần số cao và là nguồn phát nhiễu chính.

**Nên dùng cáp bọc chống nhiễu (shielded).** Lớp bọc kim loại bao quanh giúp giữ nhiễu bên trong thay vì phát ra môi trường xung quanh. Đây không phải chi tiết xa xỉ — với hệ có cảm biến hoặc truyền thông, cáp bọc thường là điều kiện để hệ chạy ổn định.

**Cách đấu lớp bọc rất quan trọng:** phải **kẹp tiếp đất 360°** bằng kẹp kim loại tại điểm vào tủ và tại hộp đấu dây động cơ. Nếu chỉ xoắn lớp bọc thành "đuôi chuột" rồi vặn ốc, hiệu quả chống nhiễu giảm rất nhiều.

**Kéo dây PE theo cùng cáp** tới động cơ, không dùng chung đất qua khung máy.

---

## Vấn đề chiều dài cáp động cơ

Đây là yếu tố kỹ thuật thường bị bỏ qua cho tới khi động cơ cháy.

**Hiện tượng phản xạ sóng:** xung PWM từ biến tần truyền theo cáp; khi gặp điểm có trở kháng khác (đầu cực động cơ), một phần sóng **phản xạ ngược lại** và cộng với sóng tới, làm **điện áp tại đầu cực động cơ vọt cao hơn** điện áp ra của biến tần. Cáp càng dài, hiện tượng càng rõ.

Hậu quả: **ứng suất lên cách điện động cơ tăng mạnh**, có thể đánh thủng cuộn dây theo thời gian.

**Giải pháp theo thứ tự ưu tiên:**

1. **Rút ngắn cáp** — đặt tủ gần động cơ nhất có thể.
2. **Giảm tần số sóng mang** — giảm số lần xung, giảm ứng suất.
3. **Lắp cuộn kháng đầu ra (output reactor)** hoặc **bộ lọc dU/dt** — làm mềm sườn xung.
4. **Dùng động cơ inverter duty** có cách điện tăng cường.

Giới hạn chiều dài cáp cho phép **khác nhau theo model** và có thể khác nhau giữa cáp bọc và cáp thường (cáp bọc có điện dung lớn hơn nên giới hạn thường ngắn hơn). Luôn tra tài liệu. [Xem chi tiết về cuộn kháng →](/cuon-khang-loc-nhieu-bien-tan/)

---

## Ứng dụng: quy tắc đi cáp trong tủ và ngoài tủ

Cách đi cáp ảnh hưởng trực tiếp tới độ ổn định của cả hệ thống:

**Trong tủ điện:**
- Tách **ba nhóm** riêng biệt: cáp động lực vào, cáp ra động cơ, cáp tín hiệu
- **Không bó chung** cáp động lực với cáp điều khiển
- Đi cáp **sát vách kim loại tiếp đất** giúp giảm phát xạ
- Nếu buộc phải cắt nhau, cắt **vuông góc**
- Cáp ra động cơ nên đi **ngắn nhất** trong tủ

**Ngoài tủ:**
- **Máng riêng** cho cáp động lực và cáp tín hiệu
- Nếu chung máng, dùng **vách ngăn kim loại**
- Giữ khoảng cách tối thiểu theo khuyến nghị của hãng
- Cáp tín hiệu tránh chạy song song dài với cáp động lực

[Xem hướng dẫn lắp tủ →](/lap-bien-tan-trong-tu-dien/)

---

## So sánh: cáp thường và cáp bọc chống nhiễu

| Tiêu chí | **Cáp thường** | **Cáp bọc chống nhiễu** |
|---|---|---|
| Giá | Thấp hơn | Cao hơn |
| Phát xạ nhiễu | **Cao** | **Thấp** |
| Ảnh hưởng tới cảm biến, truyền thông | Dễ gây sự cố | Ít |
| Điện dung ký sinh | Thấp hơn | Cao hơn → dòng rò lớn hơn |
| Chiều dài cho phép | Thường dài hơn | Có thể bị giới hạn ngắn hơn |
| Lắp đặt | Đơn giản | Cần **kẹp tiếp đất 360°** |
| Nên dùng khi | Tuyến rất ngắn, không có thiết bị nhạy gần đó | **Có cảm biến, PLC, truyền thông gần đó** — đa số trường hợp |

**Khuyến nghị thực tế:** với hầu hết nhà máy có PLC, cảm biến hoặc hệ giám sát, **cáp bọc là lựa chọn đúng**. Chi phí chênh lệch nhỏ hơn nhiều so với thời gian đi tìm nguyên nhân nhiễu.

---

## Sai lầm thường gặp

1. **Chọn aptomat theo dòng động cơ** thay vì dòng đầu vào biến tần.
2. **Chọn aptomat quá sát** → nhảy khi đóng điện do dòng nạp tụ.
3. **Dùng RCCB loại AC thông thường** → nhảy liên tục vì dòng rò tần số cao.
4. **Tự ý tháo bỏ RCCB** vì hay nhảy — nguy hiểm cho tính mạng.
5. **Dùng cáp thường cho tuyến dài** rồi bị nhiễu khắp hệ thống.
6. **Xoắn lớp bọc thành đuôi chuột** thay vì kẹp 360°.
7. **Bỏ qua giới hạn chiều dài cáp** → hỏng cách điện động cơ sau vài tháng.
8. **Quên hệ số hiệu chỉnh** khi nhiều cáp đi chung máng trong môi trường nóng.

---

## Cam kết tại HOANTRANTDH

- ✅ Tra **bảng khuyến nghị của hãng** cho đúng model bạn mua.
- ✅ Tư vấn chọn **aptomat, cầu chì, cáp và phương án RCCB** phù hợp thực tế.
- ✅ Cảnh báo sớm về **giới hạn chiều dài cáp** và nhu cầu cuộn kháng.
- ✅ Hỗ trợ kiểm tra phương án đi cáp và nối đất tại hiện trường.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi: **model biến tần (hoặc công suất động cơ) · chiều dài cáp tới động cơ · nhiệt độ môi trường · cách đi cáp · có PLC/cảm biến gần đó không.**

**→ [Liên hệ tư vấn chọn cáp & aptomat](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Chọn aptomat cho biến tần theo dòng nào?**
Theo **dòng đầu vào định mức của biến tần** ghi trong catalogue, **không** theo dòng động cơ.

**Vì sao aptomat hay nhảy khi đóng điện biến tần?**
Do **dòng nạp tụ** lúc khởi động. Cần chọn đủ dòng và dùng **đường cong C** (hoặc D nếu cần).

**Vì sao aptomat chống giật nhảy liên tục?**
Do **dòng rò tần số cao** từ biến tần. Cần dùng **RCCB loại B** hoặc loại được xác nhận phù hợp, mỗi biến tần một RCCB riêng, và nối đất tốt.

**Có bắt buộc dùng cáp bọc chống nhiễu không?**
Không bắt buộc về mặt vận hành, nhưng **rất nên** khi có cảm biến, PLC hoặc truyền thông gần đó.

**Cáp tới động cơ dài bao nhiêu là được?**
Tuỳ model — phải tra tài liệu. Cáp dài gây **phản xạ sóng** làm hỏng cách điện động cơ; cần cuộn kháng đầu ra hoặc giảm tần số sóng mang.

**Lớp bọc cáp nối đất thế nào cho đúng?**
**Kẹp tiếp đất 360°** bằng kẹp kim loại, không xoắn thành đuôi chuột rồi vặn ốc.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /so-do-dau-day-bien-tan/, /cuon-khang-loc-nhieu-bien-tan/, /lap-bien-tan-trong-tu-dien/, /bien-tan-1-pha-ra-3-pha/, /lien-he/. -->
