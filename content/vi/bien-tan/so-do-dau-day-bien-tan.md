<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 3) — Thông tin
URL SLUG   : /so-do-dau-day-bien-tan/
TỪ KHÓA    : sơ đồ đấu dây biến tần | cách đấu biến tần | đấu dây r s t u v w | nối đất biến tần | đấu điện biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 12/30. Luôn tuân thủ tài liệu của model đang dùng.
-->

TITLE TAG   : Sơ Đồ Đấu Dây Biến Tần – Hướng Dẫn Đấu Động Lực Và Nối Đất
META (156)  : Sơ đồ đấu dây biến tần chuẩn: đấu nguồn vào R/S/T, đầu ra U/V/W tới động cơ, nối đất PE, vị trí aptomat và cuộn kháng, cùng 8 lỗi đấu dây nguy hiểm cần tránh tuyệt đối.
H1          : Sơ Đồ Đấu Dây Biến Tần (Mạch Động Lực)

---

## Nguyên tắc an toàn trước khi bắt đầu

Đấu dây biến tần không phức tạp, nhưng có **vài lỗi có thể phá hỏng thiết bị ngay lập tức** hoặc gây nguy hiểm cho người. Trước khi thao tác:

- **Cắt điện hoàn toàn** và treo biển cảnh báo tại tủ.
- **Chờ đủ thời gian xả tụ** ghi trên nhãn biến tần (thường vài phút) — tụ DC bus vẫn giữ điện áp cao nguy hiểm sau khi ngắt nguồn.
- **Đo kiểm tra** bằng đồng hồ trước khi chạm vào đầu cốt, không tin vào đèn báo.
- Luôn làm theo **sơ đồ trong tài liệu của model cụ thể** — ký hiệu chân có thể khác nhau giữa các hãng.

> ⚠️ Bài này trình bày **nguyên tắc chung**. Với thiết bị thực tế, tài liệu của nhà sản xuất luôn là căn cứ cuối cùng.

> **Cần hỗ trợ đấu nối tại hiện trường?** Gửi **model biến tần · công suất động cơ · sơ đồ tủ hiện có** → [Nhận hỗ trợ kỹ thuật](#bao-gia).

Đây là bài **12/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/), mở đầu tầng lắp đặt.

---

## Cấu tạo hàng đầu cốt: các nhóm chân trên biến tần

Một biến tần điển hình có ba nhóm đầu nối:

| Nhóm | Ký hiệu thường gặp | Chức năng |
|---|---|---|
| **Nguồn vào** | R, S, T (hoặc L1, L2, L3) · L, N với loại 1 pha | Nhận điện lưới |
| **Ngõ ra động cơ** | **U, V, W** (hoặc T1, T2, T3) | Cấp điện cho động cơ |
| **Nối đất** | **PE** hoặc ký hiệu ⏚ | Bảo vệ và chống nhiễu |
| **DC bus** | P/+, N/− (hoặc P1, P2) | Đấu điện trở hãm, cuộn kháng DC |
| **Điện trở hãm** | P, B (hoặc B1, B2) | Đấu điện trở xả năng lượng khi hãm |
| **Điều khiển** | DI, AI, AO, COM, relay, RS485 | Mạch tín hiệu — xem bài riêng |

**Quy tắc quan trọng nhất cần khắc cốt ghi tâm:**

> **Nguồn lưới CHỈ được đấu vào R/S/T. Động cơ CHỈ được đấu vào U/V/W.**

Đấu ngược — tức cấp điện lưới vào U/V/W — sẽ **phá hỏng khối IGBT ngay lập tức**, và đây là hư hỏng **không được bảo hành** vì lỗi do người dùng. Đây là tai nạn phổ biến nhất khi lắp biến tần.

---

## Sơ đồ đấu dây mạch động lực

Thứ tự các thiết bị từ nguồn đến động cơ:

**Lưới điện → Aptomat (MCCB/MCB) → [Contactor nếu cần] → [Cuộn kháng AC nếu cần] → Biến tần (R/S/T) → Biến tần (U/V/W) → Động cơ**

Giải thích từng khâu:

**1. Aptomat (MCCB/MCB).** Bảo vệ ngắn mạch cho đoạn cáp và biến tần. Chọn theo **dòng đầu vào của biến tần** ghi trong catalogue, **không phải** theo dòng động cơ. [Xem hướng dẫn chọn →](/chon-cap-aptomat-cho-bien-tan/)

**2. Contactor (tuỳ chọn).** Chỉ dùng để **cách ly nguồn** khi bảo trì hoặc cho mạch an toàn. **Không dùng contactor để chạy/dừng máy hằng ngày** — hãy dùng lệnh chạy/dừng qua chân điều khiển.

**3. Cuộn kháng AC đầu vào (tuỳ chọn).** Giảm sóng hài, bảo vệ khi lưới không ổn định, kéo dài tuổi thọ tụ. [Xem chi tiết →](/cuon-khang-loc-nhieu-bien-tan/)

**4. Biến tần.** Nguồn vào R/S/T, ra U/V/W.

**5. Cáp tới động cơ.** Nên dùng **cáp bọc chống nhiễu**, đi riêng máng với cáp tín hiệu.

**6. Động cơ.** Đấu sao hay tam giác tuỳ điện áp ra của biến tần. [Xem hướng dẫn →](/bien-tan-va-dong-co-3-pha/)

---

## Nối đất — phần quan trọng nhất và hay bị làm ẩu nhất

Nối đất cho biến tần phục vụ **hai mục đích cùng lúc**: an toàn cho người và **thoát nhiễu tần số cao**. Làm ẩu ở đây gây ra cả rủi ro điện giật lẫn hàng loạt sự cố nhiễu khó tìm nguyên nhân.

**Nguyên tắc:**

1. **Chân PE của biến tần phải nối đất trực tiếp** với tiết diện dây đủ lớn theo tài liệu.
2. **Vỏ động cơ cũng phải nối đất**, tốt nhất là **kéo dây PE theo cùng cáp động lực** từ tủ tới động cơ.
3. **Dây nối đất càng ngắn càng tốt**, tránh vòng vèo — nhiễu tần số cao rất nhạy với chiều dài dây.
4. **Nối đất kiểu hình sao** về một điểm chung, tránh nối đất nối tiếp qua nhiều thiết bị.
5. **Lớp bọc (shield) của cáp động lực** phải được kẹp tiếp đất **360° bằng kẹp kim loại** tại đầu vào tủ, không xoắn thành đuôi chuột rồi vặn ốc — kiểu đuôi chuột làm mất phần lớn hiệu quả chống nhiễu.
6. **Không dùng chung điểm nối đất với thiết bị nhạy cảm** (PLC, cảm biến) nếu có thể tách được.

Rất nhiều ca "biến tần gây nhiễu cảm biến" hoặc "mất kết nối Modbus khi biến tần chạy" thực chất là **lỗi nối đất**, không phải lỗi thiết bị. [Xem chi tiết chống nhiễu →](/chong-nhieu-emc-cho-bien-tan/)

---

## Ứng dụng: các cấu hình đấu dây thường gặp

### Cấu hình 1 — Cơ bản nhất

Aptomat → biến tần → động cơ. Chạy/dừng bằng bàn phím trên biến tần, chỉnh tốc độ bằng phím lên/xuống. Phù hợp máy đơn giản, ít thao tác.

### Cấu hình 2 — Điều khiển tại tủ

Thêm **nút nhấn chạy/dừng** đấu vào chân DI và **biến trở** đấu vào chân AI để chỉnh tốc độ. Đây là cấu hình phổ biến nhất trong xưởng. [Xem đấu mạch điều khiển →](/dau-dieu-khien-bien-tan/)

### Cấu hình 3 — Điều khiển tự động theo cảm biến

Cảm biến 4-20mA (áp suất, lưu lượng) đấu vào chân AI, bật **PID** trong biến tần để tự điều chỉnh tốc độ. [Xem chi tiết →](/dieu-khien-pid-bang-bien-tan/)

### Cấu hình 4 — Điều khiển từ PLC

Nối **RS485/Modbus** từ PLC tới biến tần. PLC ra lệnh chạy/dừng và đặt tần số bằng lệnh truyền thông. [Xem chi tiết →](/dieu-khien-bien-tan-bang-plc/)

### Cấu hình 5 — Có điện trở hãm

Với tải quán tính lớn hoặc cần dừng nhanh, thêm **điện trở hãm** vào chân P/B. Điện trở này đốt bớt năng lượng do động cơ trả về khi giảm tốc, tránh lỗi quá áp. [Xem xử lý lỗi quá áp →](/loi-qua-ap-thap-ap-bien-tan/)

### Cấu hình 6 — Có bypass (chạy trực tiếp khi biến tần hỏng)

Với máy quan trọng, đôi khi cần mạch cho phép **chạy động cơ trực tiếp từ lưới** khi biến tần gặp sự cố. Mạch này bắt buộc phải có **khoá liên động cơ khí và điện** để **tuyệt đối không bao giờ** đóng điện lưới vào đầu ra U/V/W của biến tần.

---

## Tám lỗi đấu dây nguy hiểm cần tránh

**1. Đấu nguồn lưới vào U/V/W.** Hỏng IGBT ngay, không được bảo hành. Luôn kiểm tra ba lần trước khi đóng điện.

**2. Lắp tụ bù ở phía sau biến tần.** Tuyệt đối cấm. Tụ bù chỉ được lắp phía nguồn, trước biến tần.

**3. Đóng/cắt contactor giữa biến tần và động cơ khi đang chạy.** Gây quá áp và có thể hỏng IGBT. Nếu buộc phải có contactor ở đầu ra, phải khoá liên động để chỉ thao tác khi biến tần đã dừng.

**4. Không nối đất hoặc nối đất qua loa.** Vừa nguy hiểm vừa gây nhiễu khó chẩn đoán.

**5. Đi chung cáp động lực và cáp tín hiệu trong một máng.** Nhiễu sẽ làm sai tín hiệu analog và rớt truyền thông. Phải đi riêng, nếu cắt nhau thì cắt **vuông góc**.

**6. Xoắn lớp bọc cáp thành đuôi chuột.** Làm mất hiệu quả che chắn. Phải dùng **kẹp tiếp đất 360°**.

**7. Siết đầu cốt không đủ lực hoặc quá lực.** Lỏng gây phát nhiệt và cháy đầu cốt; quá chặt làm hỏng ren và nứt vỏ. Siết theo **lực quy định trong tài liệu**.

**8. Dùng cáp quá nhỏ hoặc quá dài mà không xử lý.** Cáp nhỏ gây sụt áp và nóng; cáp quá dài gây **phản xạ sóng** làm hỏng cách điện động cơ — cần cuộn kháng đầu ra hoặc giảm tần số sóng mang.

---

## So sánh: đấu trực tiếp và đấu qua biến tần

| Hạng mục | **Đấu trực tiếp (DOL)** | **Qua biến tần** |
|---|---|---|
| Thiết bị bảo vệ | Aptomat + rơ-le nhiệt | Aptomat theo dòng vào biến tần |
| Contactor | Dùng để chạy/dừng | **Chỉ để cách ly**, không chạy/dừng |
| Cáp tới động cơ | Cáp thường | Nên dùng **cáp bọc** |
| Nối đất | Theo quy định an toàn | **Quan trọng hơn** — thêm vai trò chống nhiễu |
| Đi cáp | Không đặc biệt | **Tách riêng cáp tín hiệu** |
| Đảo chiều quay | Đảo 2 pha ở dây | **Đổi bằng lệnh**, không đổi dây |
| Tụ bù | Có thể lắp | **Cấm lắp phía sau biến tần** |

Điểm cần nhớ: khi có biến tần, **đảo chiều quay không làm bằng cách hoán đổi dây** nữa mà bằng **lệnh đảo chiều** qua chân DI hoặc thông số. Nếu chạy thử thấy sai chiều, hãy đổi bằng cài đặt thay vì tráo dây U/V/W.

---

## Quy trình đấu dây và nghiệm thu

1. **Cắt điện, chờ xả tụ, đo kiểm tra.**
2. **Lắp biến tần vào tủ** đúng hướng, đủ khoảng cách thông gió. [Xem hướng dẫn →](/lap-bien-tan-trong-tu-dien/)
3. **Đấu nối đất PE trước tiên** — luôn là dây đầu tiên nối, cuối cùng tháo.
4. **Đấu nguồn vào R/S/T**, kiểm tra kỹ ký hiệu.
5. **Đấu đầu ra U/V/W tới động cơ**, kéo dây PE theo cùng cáp.
6. **Siết đầu cốt đúng lực**, kiểm tra lại từng chân.
7. **Đấu mạch điều khiển** (nếu có), đi riêng máng.
8. **Kiểm tra lại toàn bộ** — đặc biệt xác nhận không nhầm R/S/T với U/V/W.
9. **Đóng điện, chưa chạy động cơ.** Kiểm tra màn hình lên bình thường.
10. **Cài thông số động cơ** trước khi chạy. [Xem hướng dẫn →](/cai-dat-thong-so-bien-tan/)
11. **Chạy thử không tải ở tần số thấp**, kiểm tra chiều quay.
12. **Chạy có tải**, đo dòng thực tế, theo dõi nhiệt độ và tiếng động.

---

## Cam kết tại HOANTRANTDH

- ✅ Cung cấp **sơ đồ đấu dây theo đúng model** bạn mua.
- ✅ Hỗ trợ kỹ thuật khi đấu nối và nghiệm thu tại hiện trường.
- ✅ Tư vấn chọn **aptomat, cáp, cuộn kháng và phương án nối đất** phù hợp.
- ✅ Biến tần chính hãng, CO/CQ, hoá đơn VAT.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ kỹ thuật & báo giá

Gửi: **model biến tần · công suất động cơ · chiều dài cáp tới động cơ · cách muốn điều khiển · ảnh tủ điện hiện có.**

**→ [Liên hệ hỗ trợ đấu nối biến tần](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Đấu nguồn vào chân nào của biến tần?**
Vào **R/S/T** (hoặc L1/L2/L3). Động cơ đấu vào **U/V/W**. **Tuyệt đối không đấu ngược.**

**Đấu nhầm nguồn vào U/V/W thì sao?**
**Hỏng khối IGBT ngay lập tức** và thường không được bảo hành vì là lỗi người dùng.

**Có bắt buộc nối đất không?**
**Bắt buộc.** Vừa để an toàn cho người, vừa để **thoát nhiễu tần số cao**. Nối đất kém là nguyên nhân của rất nhiều sự cố nhiễu.

**Có được lắp contactor giữa biến tần và động cơ không?**
Nên tránh. Nếu buộc phải có, phải **khoá liên động** để chỉ đóng/cắt khi biến tần đã dừng hẳn.

**Muốn đảo chiều động cơ thì đổi dây phải không?**
**Không.** Với biến tần, hãy dùng **lệnh đảo chiều** qua chân DI hoặc thông số cài đặt.

**Cáp từ biến tần tới động cơ dài thì sao?**
Gây **phản xạ sóng** làm tăng điện áp tại đầu cực động cơ. Cần **giảm tần số sóng mang** hoặc lắp **cuộn kháng đầu ra**. [Xem chi tiết →](/cuon-khang-loc-nhieu-bien-tan/)

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /dau-dieu-khien-bien-tan/, /chon-cap-aptomat-cho-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /lien-he/. -->
