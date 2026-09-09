<!--
LOẠI TRANG : Bài kiến thức kỹ thuật (chuỗi biến tần — tầng 1) — Thông tin
URL SLUG   : /bien-tan-va-dong-co-3-pha/
TỪ KHÓA    : biến tần và động cơ 3 pha | đọc nhãn động cơ | đấu sao tam giác | động cơ chạy biến tần | tốc độ động cơ 3 pha
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 6/30 trong chuỗi biến tần.
-->

TITLE TAG   : Biến Tần Và Động Cơ 3 Pha – Đọc Nhãn, Đấu Sao/Tam Giác Đúng Cách
META (156)  : Biến tần làm việc với động cơ 3 pha thế nào? Hướng dẫn đọc nhãn động cơ, chọn đấu sao hay tam giác, kiểm tra động cơ có chạy được biến tần không và lưu ý khi chạy tốc độ thấp.
H1          : Biến Tần Và Động Cơ 3 Pha – Những Điều Phải Biết

---

## Vì sao phải hiểu động cơ trước khi lắp biến tần?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Biến tần không làm việc một mình — nó là **một nửa của cặp đôi biến tần + động cơ**. Rất nhiều sự cố mà người dùng đổ lỗi cho biến tần thực ra bắt nguồn từ việc **không hiểu động cơ đang dùng**: đấu nhầm sao/tam giác, cài sai thông số, hoặc chọn động cơ không phù hợp để chạy tần số thấp.

Bài này giúp bạn đọc được nhãn động cơ, quyết định cách đấu dây và đánh giá xem động cơ hiện có dùng được với biến tần hay không — trước khi bỏ tiền mua.

> **Cần kiểm tra động cơ có hợp với biến tần không?** Gửi **ảnh chụp nhãn động cơ · loại tải · dải tốc độ mong muốn** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vf-ratio.svg)


Đây là bài **6/30**, khép lại tầng nền tảng của [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: tần số quyết định tốc độ

Nhắc lại công thức nền tảng cho động cơ không đồng bộ 3 pha:

> **n = 120 × f / p** (tốc độ đồng bộ)

Trong đó **p** là **số cực** của động cơ. Đây là thông số cố định do cách quấn dây, **không thể thay đổi**.

| Số cực | Tốc độ đồng bộ ở 50 Hz | Tốc độ thực tế (có trượt) |
|---|---|---|
| 2 cực | 3000 v/p | ~2850–2900 v/p |
| 4 cực | 1500 v/p | ~1420–1450 v/p |
| 6 cực | 1000 v/p | ~940–960 v/p |
| 8 cực | 750 v/p | ~700–720 v/p |

Tốc độ thực tế luôn thấp hơn tốc độ đồng bộ một chút — chênh lệch này gọi là **độ trượt**, và nó là điều kiện để động cơ sinh ra mô-men.

Khi lắp biến tần, tốc độ tỉ lệ với tần số đặt. Ví dụ động cơ 4 cực (1450 v/p ở 50 Hz) chạy ở 30 Hz sẽ quay khoảng **870 v/p**. [Xem nguyên lý chi tiết →](/nguyen-ly-hoat-dong-bien-tan/)

---

## Cấu tạo thông tin: đọc nhãn động cơ

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-dauday.svg)


Nhãn (name plate) trên động cơ chứa mọi thông số bạn cần để cài biến tần. Đây là bước **bắt buộc** trước khi cấu hình.

| Thông số trên nhãn | Ký hiệu thường gặp | Dùng để làm gì |
|---|---|---|
| **Công suất** | kW hoặc HP | Chọn cấp biến tần (nhưng chưa đủ) |
| **Điện áp** | V — thường ghi **Δ/Y** (VD: 220/380V) | **Quyết định cách đấu dây** |
| **Dòng định mức** | A — cũng ghi 2 giá trị theo cách đấu | **Quan trọng nhất để chọn biến tần** |
| **Tần số** | Hz (50 hoặc 60) | Cài tần số cơ bản |
| **Tốc độ** | v/p (rpm) | Suy ra số cực, cài hiển thị |
| **Hệ số công suất** | cosφ | Cài cho chế độ vector |
| **Cấp cách điện** | B, F, H | Đánh giá khả năng chịu nhiệt |
| **Cấp bảo vệ** | IP55, IP54… | Môi trường lắp |
| **Chế độ làm việc** | S1, S2… | S1 = chạy liên tục |

**Điểm quan trọng nhất:** hãy chọn biến tần theo **dòng định mức (A)**, không chỉ theo kW. Hai động cơ cùng 5,5 kW nhưng khác hãng hoặc khác số cực có thể có dòng khác nhau. Nguyên tắc: **dòng định mức của biến tần phải ≥ dòng định mức của động cơ**. [Xem cách chọn công suất →](/chon-cong-suat-bien-tan/)

---

## Đấu sao (Y) hay tam giác (Δ)?

Đây là nơi gây nhầm lẫn nhiều nhất, và đấu sai có thể **cháy động cơ ngay lập tức**.

Trên nhãn động cơ thường ghi dạng **220/380V** kèm ký hiệu **Δ/Y**. Cách đọc:

- **220V — đấu tam giác (Δ):** dùng khi nguồn 3 pha có điện áp dây **220V**
- **380V — đấu sao (Y):** dùng khi nguồn 3 pha có điện áp dây **380V**

**Quy tắc vàng:** con số điện áp **nhỏ hơn** đi với **tam giác**, con số **lớn hơn** đi với **sao**.

Áp dụng vào thực tế:

| Biến tần của bạn | Điện áp ra | Động cơ 220/380V đấu thế nào |
|---|---|---|
| 3 pha vào 380V | 3 pha 380V | **Đấu sao (Y)** |
| 1 pha vào 220V | 3 pha **220V** | **Đấu tam giác (Δ)** |
| 3 pha vào 220V | 3 pha 220V | **Đấu tam giác (Δ)** |

Đây chính là lý do đã nói ở bài phân loại: mua biến tần **1 pha vào** thì phải kiểm tra động cơ có **đấu tam giác 220V được không**. Nếu động cơ chỉ ghi 380/660V thì không dùng được với loại này. [Xem chi tiết →](/bien-tan-1-pha-ra-3-pha/)

**Cách đổi cách đấu:** trong hộp đấu dây động cơ có 6 đầu (U1-V1-W1 và U2-V2-W2) cùng các thanh đồng nối tắt. Đổi vị trí thanh đồng là đổi giữa sao và tam giác. Luôn **cắt điện và làm theo sơ đồ in trong nắp hộp**.

---

## Ứng dụng: động cơ của tôi có chạy được biến tần không?

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bangtai.svg)


Không phải động cơ nào cũng phù hợp. Hãy kiểm tra theo danh sách sau:

**1. Động cơ có phải loại không đồng bộ 3 pha (rotor lồng sóc) không?**
Đây là loại phổ biến nhất và hợp nhất với biến tần. Động cơ 1 pha có tụ, động cơ vòng chập hoặc động cơ đồng bộ cần xử lý khác.

**2. Cách điện có còn tốt không?**
Biến tần phát ra xung PWM có **độ dốc điện áp cao**, gây ứng suất lên cách điện cuộn dây — mạnh hơn so với chạy trực tiếp từ lưới. Động cơ **đời cũ, cách điện đã lão hoá** dễ bị đánh thủng. Nên **đo điện trở cách điện (megger)** trước khi lắp.

**3. Có cần chạy tốc độ thấp kéo dài không?**
Đây là vấn đề quan trọng thường bị bỏ qua. Quạt làm mát của động cơ tiêu chuẩn **gắn trên chính trục động cơ** — khi chạy chậm, quạt cũng chậm, khả năng tản nhiệt giảm mạnh trong khi dòng vẫn lớn. Kết quả: **động cơ nóng dần và có thể cháy** dù biến tần không báo lỗi.

Giải pháp:
- Lắp **quạt cưỡng bức riêng** chạy độc lập với tốc độ động cơ
- Hoặc dùng **động cơ chuyên dụng cho biến tần (inverter duty)**
- Hoặc **giới hạn tần số tối thiểu** để động cơ không chạy quá chậm quá lâu

**4. Chiều dài cáp từ biến tần đến động cơ bao nhiêu?**
Cáp dài gây hiện tượng **phản xạ sóng**, làm điện áp tại đầu cực động cơ vọt lên cao hơn điện áp ra của biến tần — có thể đánh thủng cách điện. Với cáp dài, cần **giảm tần số sóng mang** hoặc lắp **cuộn kháng đầu ra (dU/dt filter)**. [Xem chi tiết →](/cuon-khang-loc-nhieu-bien-tan/)

**5. Có ổ bi chịu dòng rò không?**
Với động cơ công suất lớn chạy biến tần, có thể xuất hiện **dòng trục** làm rỗ ổ bi. Giải pháp là ổ bi cách điện hoặc vòng dẫn dòng trục — thường chỉ cần quan tâm ở công suất lớn.

---

## So sánh: động cơ thường và động cơ chuyên dụng cho biến tần

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vf-vector.svg)


| Tiêu chí | **Động cơ tiêu chuẩn** | **Động cơ inverter duty** |
|---|---|---|
| Cách điện | Tiêu chuẩn | **Tăng cường**, chịu xung PWM tốt hơn |
| Làm mát ở tốc độ thấp | Kém — quạt quay chậm theo | **Có quạt cưỡng bức** hoặc thiết kế tốt hơn |
| Dải tốc độ khả dụng | Hẹp hơn | **Rộng** |
| Xử lý dòng trục | Không có | Thường có ổ bi cách điện (công suất lớn) |
| Giá | Thấp hơn | Cao hơn |
| Phù hợp | Chạy quanh tốc độ định mức, giảm tốc vừa phải | **Chạy chậm kéo dài, dải rộng, tải nặng** |

**Nguyên tắc thực dụng:** với ứng dụng **bơm quạt giảm tốc vừa phải (không dưới ~30 Hz)**, động cơ tiêu chuẩn thường vẫn dùng tốt. Với ứng dụng **chạy rất chậm liên tục** hoặc **dải tốc độ rất rộng**, nên đầu tư động cơ chuyên dụng — rẻ hơn nhiều so với việc thay động cơ cháy giữa chừng.

---

## Những sai lầm phổ biến

1. **Đấu sai sao/tam giác.** Đấu tam giác 220V vào biến tần ra 380V sẽ cháy động cơ gần như tức thì.
2. **Chọn biến tần chỉ theo kW mà bỏ qua dòng (A).**
3. **Không cài thông số động cơ vào biến tần.** Chế độ vector và các bảo vệ quá tải dựa trên thông số này; bỏ trống thì bảo vệ không chính xác.
4. **Chạy tần số thấp kéo dài với động cơ tiêu chuẩn** mà không có quạt cưỡng bức.
5. **Lắp contactor giữa biến tần và động cơ rồi đóng cắt khi đang chạy.** Điều này gây quá áp/quá dòng và có thể hỏng IGBT. Nếu bắt buộc phải có contactor, phải **khoá liên động** để chỉ đóng cắt khi biến tần đã dừng.
6. **Đấu tụ bù vào phía sau biến tần.** Tuyệt đối không được — sẽ hỏng biến tần.
7. **Bỏ qua nối đất.** Nối đất kém vừa nguy hiểm vừa gây nhiễu. [Xem chi tiết →](/so-do-dau-day-bien-tan/)

---

## Cam kết tại HOANTRANTDH

- ✅ **Kiểm tra tương thích động cơ – biến tần** trước khi báo giá.
- ✅ Tư vấn cách đấu sao/tam giác đúng với điện áp ra của biến tần.
- ✅ Đề xuất giải pháp khi cần chạy tốc độ thấp kéo dài hoặc cáp dài.
- ✅ Biến tần chính hãng, CO/CQ, hoá đơn VAT; hỗ trợ cài đặt tại hiện trường.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi: **ảnh chụp nhãn động cơ · nguồn điện hiện có · loại tải · dải tốc độ cần chạy · chiều dài cáp từ tủ tới động cơ.**

**→ [Liên hệ tư vấn biến tần & động cơ](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Biến tần điều khiển tốc độ động cơ 3 pha bằng cách nào?**
Bằng cách **thay đổi tần số** cấp cho động cơ, theo công thức **n = 120 × f / p**, đồng thời giảm điện áp tương ứng để giữ tỉ số **V/f**.

**Động cơ ghi 220/380V thì đấu thế nào?**
Nguồn ra **380V → đấu sao (Y)**; nguồn ra **220V → đấu tam giác (Δ)**. Quy tắc: số điện áp nhỏ đi với tam giác.

**Động cơ cũ có chạy được biến tần không?**
Có thể, nhưng nên **đo điện trở cách điện** trước, vì xung PWM gây ứng suất lên cách điện mạnh hơn chạy trực tiếp từ lưới.

**Vì sao chạy chậm lâu thì động cơ nóng?**
Vì **quạt làm mát gắn trên trục quay chậm theo**. Cần **quạt cưỡng bức riêng**, dùng **động cơ inverter duty**, hoặc giới hạn tần số tối thiểu.

**Có được lắp contactor giữa biến tần và động cơ không?**
Nên tránh. Nếu bắt buộc, phải **khoá liên động** để chỉ đóng/cắt khi biến tần đã dừng — đóng cắt khi đang chạy có thể hỏng IGBT.

**Có được lắp tụ bù sau biến tần không?**
**Tuyệt đối không.** Tụ bù chỉ được lắp ở phía nguồn, không bao giờ lắp giữa biến tần và động cơ.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /nguyen-ly-hoat-dong-bien-tan/, /chon-cong-suat-bien-tan/, /so-do-dau-day-bien-tan/, /lien-he/. -->
