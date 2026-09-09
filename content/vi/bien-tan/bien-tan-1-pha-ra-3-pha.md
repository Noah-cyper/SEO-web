<!--
LOẠI TRANG : Bài hướng dẫn (chuỗi biến tần — tầng 2) — Thông tin + thương mại
URL SLUG   : /bien-tan-1-pha-ra-3-pha/
TỪ KHÓA    : biến tần 1 pha ra 3 pha | biến tần 220v ra 380v | chạy động cơ 3 pha bằng điện 1 pha | biến tần 1 pha | đấu tam giác 220v
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 9/30 trong chuỗi biến tần.
-->

TITLE TAG   : Biến Tần 1 Pha Ra 3 Pha – Chạy Động Cơ 3 Pha Bằng Điện 220V
META (156)  : Biến tần 1 pha ra 3 pha: nguyên lý, giới hạn công suất, cách kiểm tra động cơ đấu tam giác 220V, chọn aptomat và những hiểu lầm về việc "biến 220V thành 380V". Hướng dẫn đầy đủ.
H1          : Biến Tần 1 Pha Ra 3 Pha – Hướng Dẫn Đầy Đủ

---

## Bài toán: nhà xưởng chỉ có điện 1 pha

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan-1p3p.svg)


Đây là tình huống rất phổ biến với xưởng nhỏ, hộ kinh doanh, cơ sở gia công tại nhà: bạn có một **máy dùng động cơ 3 pha** — máy tiện, máy cưa, máy bơm, máy trộn — nhưng nơi lắp **chỉ có điện 1 pha 220V**.

Xin cấp điện 3 pha thì tốn kém và mất thời gian. Vậy giải pháp là gì?

Câu trả lời là **biến tần 1 pha vào – 3 pha ra**. Nhưng trước khi mua, có một điều **cực kỳ quan trọng** mà rất nhiều người hiểu sai và dẫn tới mua nhầm.

> **Muốn kiểm tra động cơ có dùng được không?** Gửi **ảnh nhãn động cơ · ảnh hộp đấu dây** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-pwm.svg)


Đây là bài **9/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Hiểu lầm lớn nhất: "biến 220V thành 380V"

**Biến tần 1 pha vào KHÔNG tạo ra điện 3 pha 380V.**

Nó nhận **1 pha 220V** và xuất ra **3 pha 220V**. Đây là điểm mà rất nhiều người mua nhầm.

Lý do nằm ở nguyên lý hoạt động. Biến tần chỉnh lưu điện vào thành một chiều, rồi nghịch lưu ngược lại thành xoay chiều. Nhưng **điện áp một chiều thu được từ nguồn 220V một pha không đủ cao** để tạo ra 380V ba pha ở đầu ra. Muốn có 380V ra thì phải có nguồn vào tương ứng.

**Hệ quả bắt buộc:** động cơ 3 pha của bạn **phải đấu được ở 220V**, tức phải **đấu tam giác (Δ)**.

| Nhãn động cơ | Có dùng được với biến tần 1 pha vào? |
|---|---|
| **220/380V (Δ/Y)** | ✅ **Được** — đấu tam giác ở 220V |
| **220V (Δ) đơn thuần** | ✅ Được |
| **380/660V (Δ/Y)** | ❌ **Không** — điện áp thấp nhất là 380V |
| **380V (Y) đơn thuần** | ❌ Không |

Vì vậy, việc đầu tiên phải làm là **mở hộp đấu dây động cơ và đọc nhãn**. [Xem hướng dẫn đọc nhãn →](/bien-tan-va-dong-co-3-pha/)

---

## Nguyên lý: biến tần 1 pha vào hoạt động thế nào?

Nguyên lý cơ bản giống mọi biến tần khác — **AC → DC → AC** — chỉ khác ở phía đầu vào:

**Bước 1 — Chỉnh lưu 1 pha.** Cầu 4 diode biến điện 1 pha 220V thành một chiều. Do chỉ có một pha nên dạng sóng sau chỉnh lưu **nhấp nhô mạnh hơn** so với chỉnh lưu 3 pha.

**Bước 2 — Lọc phẳng.** Tụ DC bus phải làm việc nặng hơn để san phẳng. Đây là lý do biến tần 1 pha vào thường có **dung lượng tụ lớn hơn** so với loại 3 pha cùng công suất.

**Bước 3 — Nghịch lưu 3 pha.** Sáu IGBT tạo ra ba pha 220V với tần số thay đổi được — hoàn toàn giống loại 3 pha vào.

Điểm cần lưu ý về mặt điện: với cùng một công suất, **dòng phía 1 pha lớn hơn nhiều** so với phía 3 pha. Đây là lý do dẫn tới giới hạn công suất ở phần tiếp theo. [Xem nguyên lý chi tiết →](/nguyen-ly-hoat-dong-bien-tan/)

---

## Cấu tạo bài toán: giới hạn công suất và dòng đầu vào

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-dauday.svg)


Đây là điểm kỹ thuật quan trọng thứ hai sau vấn đề điện áp.

Vì toàn bộ công suất phải đi qua **một pha duy nhất**, dòng điện phía nguồn tăng rất nhanh theo công suất. Hệ quả:

**1. Giới hạn công suất.** Biến tần 1 pha vào phổ biến ở dải **0,4 – 2,2 kW**; một số dòng lên tới khoảng 3,7 kW hoặc hơn. Vượt mức đó thì hiếm và rất đắt — lúc này xin cấp điện 3 pha thường hợp lý hơn.

**2. Aptomat và dây dẫn phải tính theo dòng 1 pha.** Đây là chỗ hay bị làm sai. Ví dụ minh hoạ cho biến tần khoảng 2,2 kW:

| Phía | Đặc điểm |
|---|---|
| **Đầu vào 1 pha 220V** | Dòng **lớn** — phải chọn aptomat và dây theo dòng này |
| **Đầu ra 3 pha 220V** | Dòng chia cho 3 pha — nhỏ hơn |

Chọn aptomat theo dòng động cơ (phía ra) thay vì theo dòng đầu vào là lỗi phổ biến, dẫn tới **aptomat nhảy liên tục** hoặc dây nóng. Hãy tra **dòng đầu vào định mức** trong catalogue của model đang dùng. [Xem hướng dẫn chọn cáp & aptomat →](/chon-cap-aptomat-cho-bien-tan/)

**3. Chất lượng nguồn.** Vì dòng lớn trên một pha, hệ thống dễ bị **sụt áp** khi khởi động — nhất là ở khu vực điện yếu hoặc dây dẫn từ công tơ vào xưởng nhỏ và dài. Sụt áp có thể khiến biến tần báo **lỗi thấp áp (LV)**. [Xem xử lý lỗi thấp áp →](/loi-qua-ap-thap-ap-bien-tan/)

---

## Ứng dụng: các trường hợp phù hợp

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bom.svg)


- **Xưởng gỗ, cơ khí nhỏ tại nhà:** máy cưa, máy bào, máy tiện mini dùng động cơ 3 pha.
- **Máy bơm nước gia đình/trang trại:** bơm 3 pha công suất nhỏ.
- **Máy trộn, máy nghiền nhỏ** trong cơ sở chế biến.
- **Máy nông nghiệp:** máy xay, máy ép, quạt thông gió chuồng trại.
- **Thiết bị nhập khẩu dùng động cơ 3 pha** trong khi nơi lắp chỉ có 1 pha.
- **Sửa chữa, chạy thử động cơ 3 pha** tại xưởng chỉ có điện 1 pha.

Ngoài việc "chạy được", bạn còn có luôn các lợi ích của biến tần: **điều chỉnh tốc độ, khởi động êm, bảo vệ động cơ**. Với máy gia công, khả năng đổi tốc độ thường quan trọng không kém việc chạy được.

---

## Hướng dẫn triển khai từng bước

**Bước 1 — Kiểm tra động cơ.** Đọc nhãn: có ghi 220V (hoặc 220/380V) không? Mở hộp đấu dây xem có đủ 6 đầu và thanh đồng để đổi cách đấu không.

**Bước 2 — Đổi động cơ sang đấu tam giác.** Cắt điện hoàn toàn. Làm theo sơ đồ in trong nắp hộp đấu dây. Nếu không chắc, nhờ thợ điện.

**Bước 3 — Lấy dòng định mức ở chế độ tam giác 220V.** Đây là con số dùng để chọn biến tần (thường là con số **lớn hơn** trên nhãn).

**Bước 4 — Chọn biến tần.** Dòng định mức đầu ra của biến tần ≥ dòng động cơ ở chế độ tam giác. Với tải nặng, chọn dư một cấp. [Xem cách chọn công suất →](/chon-cong-suat-bien-tan/)

**Bước 5 — Chọn aptomat và dây theo dòng ĐẦU VÀO 1 pha.** Tra catalogue, không suy từ dòng động cơ.

**Bước 6 — Đấu nối.** Nguồn 1 pha vào các chân **L/N** (hoặc R/S tuỳ hãng), động cơ vào **U/V/W**, **nối đất PE bắt buộc**. [Xem sơ đồ đấu dây →](/so-do-dau-day-bien-tan/)

**Bước 7 — Cài thông số động cơ.** Nhập điện áp **220V**, dòng ở chế độ tam giác, tần số, tốc độ. [Xem hướng dẫn cài đặt →](/cai-dat-thong-so-bien-tan/)

**Bước 8 — Chạy thử không tải rồi có tải.** Kiểm tra chiều quay, đo dòng thực tế, theo dõi nhiệt độ động cơ.

---

## So sánh: biến tần 1 pha và các giải pháp khác

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-saobam.svg)


| Giải pháp | Ưu điểm | Nhược điểm |
|---|---|---|
| **Biến tần 1 pha vào** | Chạy được ngay, **có điều chỉnh tốc độ**, khởi động êm, bảo vệ động cơ | Giới hạn công suất, cần động cơ đấu Δ 220V |
| **Xin cấp điện 3 pha** | Không giới hạn công suất, dùng được mọi động cơ | **Tốn kém, thủ tục lâu**, phải kéo dây |
| **Tụ ngậm (tụ đề)** | Rẻ nhất | **Mô-men yếu**, động cơ nóng, không đổi được tốc độ, hại động cơ |
| **Đổi sang động cơ 1 pha** | Đơn giản về điện | Phải thay động cơ, mô-men và hiệu suất kém hơn, khó tìm công suất lớn |
| **Máy biến áp 1→3 pha** | Có 3 pha thật | Cồng kềnh, đắt, không đổi được tốc độ |

**Kết luận thực dụng:** với công suất **dưới khoảng 2,2 kW**, biến tần 1 pha vào gần như luôn là giải pháp tốt nhất — vừa giải quyết vấn đề nguồn, vừa được thêm điều chỉnh tốc độ và bảo vệ động cơ.

Cách dùng **tụ ngậm** tuy rẻ nhưng nên tránh: động cơ chạy lệch pha, mô-men yếu, nóng và giảm tuổi thọ rõ rệt.

Với công suất **lớn hơn 3–4 kW**, nên tính đến phương án **xin cấp điện 3 pha** vì chi phí biến tần 1 pha vào ở dải này rất cao và dòng đầu vào quá lớn.

---

## Những lưu ý và sai lầm cần tránh

1. **Mua biến tần 1 pha rồi mới phát hiện động cơ chỉ đấu được 380V.** Luôn kiểm tra nhãn **trước khi mua**.
2. **Quên đổi động cơ sang đấu tam giác.** Cấp 220V vào động cơ đang đấu sao 380V → động cơ yếu, không kéo nổi tải.
3. **Chọn aptomat theo dòng động cơ thay vì dòng đầu vào 1 pha.** Aptomat sẽ nhảy liên tục.
4. **Dây nguồn quá nhỏ hoặc quá dài** → sụt áp → báo lỗi thấp áp khi khởi động.
5. **Cài thông số động cơ là 380V** trong khi thực tế chạy 220V → bảo vệ sai, có thể hỏng động cơ.
6. **Kỳ vọng công suất lớn.** Đừng cố ép biến tần 1 pha chạy động cơ vượt dải khuyến nghị.
7. **Bỏ qua nối đất.** Với thiết bị điện tử công suất, nối đất là bắt buộc cả về an toàn lẫn chống nhiễu.

---

## Cam kết tại HOANTRANTDH

- ✅ **Kiểm tra nhãn động cơ trước** — xác nhận đấu tam giác 220V được rồi mới báo giá.
- ✅ Tư vấn **chọn aptomat và dây theo dòng đầu vào 1 pha** đúng chuẩn.
- ✅ Nói rõ khi công suất vượt ngưỡng hợp lý và nên xin điện 3 pha.
- ✅ Biến tần chính hãng, CO/CQ, hoá đơn VAT; hướng dẫn cài đặt cụ thể.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi: **ảnh nhãn động cơ · ảnh hộp đấu dây · loại máy · chiều dài dây từ công tơ tới nơi lắp.**

**→ [Liên hệ tư vấn biến tần 1 pha ra 3 pha](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Biến tần 1 pha có biến 220V thành 380V không?**
**Không.** Loại 1 pha vào xuất ra **3 pha 220V**. Động cơ phải **đấu tam giác 220V** mới dùng được.

**Động cơ 380/660V có dùng được biến tần 1 pha không?**
**Không** — điện áp thấp nhất của động cơ này là 380V, trong khi biến tần chỉ ra 220V.

**Biến tần 1 pha chạy được tối đa bao nhiêu kW?**
Phổ biến **0,4 – 2,2 kW**, một số dòng cao hơn. Vượt ngưỡng này thì nên cân nhắc xin điện 3 pha.

**Chọn aptomat cho biến tần 1 pha thế nào?**
Theo **dòng đầu vào 1 pha** ghi trong catalogue, **không** theo dòng động cơ ở đầu ra.

**Dùng tụ ngậm thay biến tần được không?**
Được về mặt chạy máy, nhưng **mô-men yếu, động cơ nóng, không đổi được tốc độ** và giảm tuổi thọ. Không khuyến khích.

**Vì sao khởi động hay báo lỗi thấp áp?**
Thường do **sụt áp nguồn** vì dòng 1 pha lớn, dây nhỏ hoặc dài. Cần nâng tiết diện dây và kiểm tra chất lượng nguồn.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /bien-tan-va-dong-co-3-pha/, /chon-cap-aptomat-cho-bien-tan/, /so-do-dau-day-bien-tan/, /lien-he/. -->
