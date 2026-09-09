<!--
LOẠI TRANG : Bài kiến thức kỹ thuật (chuỗi biến tần — tầng 1) — Thông tin
URL SLUG   : /phan-loai-bien-tan/
TỪ KHÓA    : phân loại biến tần | các loại biến tần | biến tần 1 pha 3 pha | biến tần chuyên dụng | biến tần theo điện áp
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 4/30 trong chuỗi biến tần.
-->

TITLE TAG   : Phân Loại Biến Tần – Các Loại Biến Tần Và Cách Chọn Đúng Nhóm
META (156)  : Phân loại biến tần theo nguồn cấp (1 pha/3 pha), điện áp, loại tải, chế độ điều khiển V/f–vector và biến tần chuyên dụng cho bơm, quạt, thang máy. Hướng dẫn chọn đúng nhóm.
H1          : Phân Loại Biến Tần – Có Những Loại Nào Và Chọn Ra Sao?

---

## Vì sao cần phân loại biến tần?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Khi tìm mua biến tần, bạn sẽ gặp hàng loạt thuật ngữ: biến tần 1 pha, biến tần 3 pha, biến tần vector, biến tần chuyên dụng cho bơm, biến tần trung thế… Nếu không biết cách phân nhóm, rất dễ mua nhầm — hoặc mua thừa tính năng không dùng đến, hoặc mua thiếu và phải đổi lại.

Thực tế, biến tần được phân loại theo **nhiều tiêu chí song song**. Một sản phẩm cụ thể sẽ mang đồng thời nhiều nhãn: ví dụ "biến tần **3 pha 380V**, dòng **vector không cảm biến**, chuyên dụng cho **bơm quạt**". Hiểu từng trục phân loại giúp bạn đọc catalogue nhanh và chọn chính xác.

> **Chưa biết nên chọn nhóm nào?** Gửi **nguồn điện hiện có · công suất động cơ · loại tải** → [Nhận tư vấn chọn loại](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vf-ratio.svg)


Đây là bài **4/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Trục 1: Phân loại theo nguồn cấp và điện áp

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)


Đây là tiêu chí **bắt buộc phải đúng** — chọn sai thì thiết bị không dùng được.

| Loại | Nguồn vào | Ngõ ra | Dùng khi |
|---|---|---|---|
| **1 pha vào – 3 pha ra 220V** | 1 pha 220V | 3 pha 220V | Nhà xưởng nhỏ, hộ gia đình chỉ có điện 1 pha |
| **3 pha vào – 3 pha ra 220V** | 3 pha 220V | 3 pha 220V | Động cơ 220V/3 pha (ít gặp ở VN) |
| **3 pha vào – 3 pha ra 380V** | 3 pha 380V | 3 pha 380V | **Phổ biến nhất trong công nghiệp VN** |
| **3 pha 480V / 690V** | 3 pha cao hơn | Tương ứng | Nhà máy dùng lưới đặc thù, công suất lớn |
| **Trung thế (3kV–11kV)** | Trung thế | Trung thế | Động cơ rất lớn, nhà máy xi măng, thép |

**Lưu ý cực kỳ quan trọng với loại 1 pha vào:** biến tần này nhận điện 1 pha 220V nhưng **xuất ra 3 pha 220V**, không phải 380V. Nghĩa là **động cơ phải đấu tam giác ở 220V** mới dùng được. Nhiều người mua về rồi mới phát hiện động cơ của mình là loại 380V và không đấu lại được. [Xem chi tiết →](/bien-tan-1-pha-ra-3-pha/)

Ngoài ra, loại 1 pha vào thường **giới hạn công suất** (phổ biến đến khoảng 2,2 kW, một số dòng lên cao hơn), vì dòng phía 1 pha tăng rất nhanh theo công suất.

---

## Trục 2: Phân loại theo chế độ điều khiển

Đây là trục quyết định **chất lượng điều khiển** và giá thành.

**V/f vô hướng (scalar).** Giữ tỉ số điện áp/tần số không đổi. Đơn giản, ổn định, cài nhanh, **chạy được nhiều động cơ song song**. Mô-men khởi động ở mức vừa phải. Phù hợp bơm, quạt, tải nhẹ.

**Vector không cảm biến (sensorless vector).** Biến tần dựng mô hình động cơ để ước lượng và điều khiển mô-men. Cho **mô-men khởi động cao** ngay ở tốc độ rất thấp và **giữ tốc độ ổn định khi tải biến động**. Cần cài đúng thông số động cơ (auto-tuning). Phù hợp băng tải, máy ép, trộn, nâng hạ.

**Vector có phản hồi (closed-loop, encoder).** Thêm encoder gắn trên trục để đo tốc độ thực. Cho độ chính xác cao nhất, giữ được mô-men ở tốc độ gần bằng 0. Dùng cho thang máy, cầu trục, máy công cụ chính xác.

**Điều khiển mô-men trực tiếp / servo.** Các dòng cao cấp cho ứng dụng đòi hỏi đáp ứng cực nhanh.

[Xem so sánh V/f và vector chi tiết →](/che-do-dieu-khien-vf-vector/)

---

## Trục 3: Phân loại theo đặc tính tải

Đây là trục hay bị bỏ qua nhất nhưng ảnh hưởng trực tiếp tới việc **chọn công suất**.

| Nhóm tải | Đặc tính | Ví dụ | Yêu cầu biến tần |
|---|---|---|---|
| **Mô-men giảm theo bậc hai** | Mô-men ∝ n², công suất ∝ n³ | Bơm ly tâm, quạt | Dòng **tiêu chuẩn**, chọn đúng công suất là đủ |
| **Mô-men không đổi** | Mô-men gần như cố định ở mọi tốc độ | Băng tải, máy nén piston, máy ép | Cần **khả năng quá tải tốt**, nên chọn dư 1 cấp |
| **Công suất không đổi** | Mô-men giảm khi tốc độ tăng | Máy quấn, máy tiện | Cần dải điều chỉnh rộng |
| **Tải va đập / xung** | Mô-men thay đổi đột ngột | Máy nghiền, máy cán | Cần quá tải cao, chế độ vector |

Nhiều catalogue ghi rõ hai mức công suất cho cùng một model: một cho **tải nhẹ (bơm/quạt)** và một cho **tải nặng (mô-men không đổi)**. Đọc nhầm cột là nguyên nhân phổ biến khiến biến tần chạy được vài tháng rồi liên tục báo quá tải. [Xem cách chọn theo tải →](/chon-cong-suat-bien-tan/)

---

## Trục 4: Phân loại theo mức độ chuyên dụng

**Biến tần đa dụng (general purpose).** Dùng được cho hầu hết ứng dụng thông thường. Đây là nhóm chiếm phần lớn thị trường và thường là lựa chọn đúng cho nhà máy phổ thông.

**Biến tần chuyên dụng cho bơm/quạt (HVAC, pump & fan).** Tích hợp sẵn **PID**, chức năng **luân phiên nhiều bơm**, chống búa nước, chế độ ngủ khi nhu cầu thấp, chống tắc bơm. Nếu bạn làm trạm bơm, dòng này tiết kiệm rất nhiều công lập trình. [Xem chi tiết →](/bien-tan-cho-bom-nuoc/)

**Biến tần chuyên dụng nâng hạ (crane, hoist).** Có logic điều khiển phanh cơ, chống trôi tải, mô-men khởi động rất cao.

**Biến tần chuyên dụng thang máy.** Đáp ứng yêu cầu êm ái và an toàn đặc thù.

**Biến tần chuyên ngành khác.** Dệt, đùn nhựa, máy nén khí, máy công cụ — mỗi ngành có yêu cầu riêng về dải tốc độ và độ chính xác.

**Nguyên tắc thực dụng:** chỉ chọn dòng chuyên dụng khi bạn **thực sự dùng đến tính năng đặc thù** của nó. Với đa số ứng dụng, biến tần đa dụng cấu hình đúng là đủ và dễ tìm phụ tùng hơn.

---

## Trục 5: Phân loại theo hình thức lắp đặt và bảo vệ

**Lắp trong tủ (IP20).** Phổ biến nhất, giá tốt, nhưng **bắt buộc phải đặt trong tủ điện** có thông gió. [Xem cách lắp tủ →](/lap-bien-tan-trong-tu-dien/)

**Lắp ngoài trời / chống bụi nước (IP54, IP55, IP65).** Vỏ kín, dùng khi không có tủ hoặc môi trường bụi ẩm nặng. Giá cao hơn, tản nhiệt khó hơn nên thường giới hạn công suất.

**Dạng module lắp tủ lớn.** Với công suất rất lớn, biến tần được thiết kế dạng module ghép trong tủ chuyên dụng.

Ngoài ra còn phân theo **phương thức làm mát**: quạt gió (phổ biến) hoặc làm mát bằng nước (công suất rất lớn, môi trường đặc biệt).

---

## Ứng dụng: chọn nhóm nào cho từng bài toán?

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bom.svg)


| Bài toán thực tế | Nhóm biến tần nên chọn |
|---|---|
| Bơm nước sinh hoạt, giữ áp | 3 pha 380V · V/f hoặc chuyên dụng bơm · có PID |
| Quạt hút bụi, thông gió nhà xưởng | 3 pha 380V · V/f · dòng tiêu chuẩn |
| Băng tải sản xuất | 3 pha 380V · **vector** · quá tải tốt |
| Máy trộn, máy nghiền | 3 pha 380V · **vector** · chọn dư công suất |
| Máy nhỏ trong xưởng chỉ có điện 1 pha | **1 pha vào – 3 pha ra 220V** |
| Cầu trục, nâng hạ | Chuyên dụng nâng hạ · vector · logic phanh |
| Trạm bơm nhiều bơm luân phiên | Chuyên dụng bơm · PID · luân phiên |
| Máy nén khí | Đa dụng hoặc chuyên dụng · vector |

---

## So sánh: đa dụng hay chuyên dụng?

| Tiêu chí | **Biến tần đa dụng** | **Biến tần chuyên dụng** |
|---|---|---|
| Giá | Thường tốt hơn | Cao hơn |
| Tính năng đặc thù | Phải tự cấu hình | **Có sẵn, cài nhanh** |
| Thời gian lắp đặt | Lâu hơn nếu cần logic phức tạp | **Nhanh** |
| Tính linh hoạt | **Dùng được nhiều loại máy** | Bó hẹp trong ứng dụng |
| Phụ tùng thay thế | **Dễ tìm, nhiều nguồn** | Hẹp hơn |
| Phù hợp | Đa số nhà máy | Trạm bơm, nâng hạ, thang máy |

**Lời khuyên:** nếu chỉ có một hai máy và nhân sự kỹ thuật quen cấu hình, **biến tần đa dụng** thường là lựa chọn kinh tế và linh hoạt hơn. Nếu bạn làm **trạm bơm nhiều bơm** hoặc **hệ nâng hạ**, dòng chuyên dụng tiết kiệm rất nhiều thời gian và rủi ro lập trình.

---

## Sai lầm thường gặp khi chọn nhóm

1. **Mua biến tần 1 pha vào nhưng động cơ là 380V.** Loại này xuất ra 3 pha **220V** — phải kiểm tra động cơ có đấu tam giác 220V được không.
2. **Đọc nhầm cột công suất tải nhẹ/tải nặng.** Băng tải mà chọn theo cột bơm–quạt sẽ liên tục báo quá tải.
3. **Mua dòng chuyên dụng nhưng không dùng tính năng.** Trả thêm tiền cho chức năng không bao giờ bật.
4. **Chọn V/f cho tải cần mô-men khởi động cao.** Máy ì, không khởi động nổi khi có tải.
5. **Chọn IP20 rồi treo ngoài trời.** Bụi và ẩm sẽ phá hỏng thiết bị trong thời gian ngắn.
6. **Bỏ qua nhiệt độ môi trường và độ cao lắp đặt.** Cả hai đều làm giảm công suất khả dụng (derating).

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **đúng nhóm biến tần** theo nguồn điện, loại tải và môi trường lắp đặt.
- ✅ Kiểm tra tương thích động cơ trước khi báo giá — tránh mua rồi phải đổi.
- ✅ Hàng **chính hãng**, CO/CQ, hoá đơn VAT.
- ✅ Hỗ trợ cài đặt và nghiệm thu tại hiện trường.

---

<a name="bao-gia"></a>
## Nhận tư vấn chọn loại biến tần

Gửi: **nguồn điện hiện có (1 pha 220V / 3 pha 380V) · thông số trên nhãn động cơ · loại tải · môi trường lắp · tính năng cần (PID, Modbus, luân phiên bơm…).**

**→ [Liên hệ tư vấn chọn biến tần](/lien-he/)**

---

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-parts.svg)


## Câu hỏi thường gặp (FAQ)

**Có bao nhiêu loại biến tần?**
Phân theo nhiều trục: **nguồn cấp/điện áp**, **chế độ điều khiển** (V/f, vector), **đặc tính tải**, **mức chuyên dụng** và **cấp bảo vệ vỏ**. Một sản phẩm mang nhiều nhãn cùng lúc.

**Biến tần 1 pha và 3 pha khác nhau thế nào?**
Khác ở **nguồn vào**. Loại 1 pha vào nhận 220V một pha nhưng **xuất ra 3 pha 220V** — động cơ phải đấu được ở 220V.

**Nên chọn V/f hay vector?**
**V/f** cho bơm, quạt, tải nhẹ. **Vector** khi cần mô-men khởi động cao hoặc giữ tốc độ ổn định lúc tải thay đổi.

**Biến tần chuyên dụng cho bơm có gì khác?**
Tích hợp sẵn **PID, luân phiên nhiều bơm, chế độ ngủ, chống búa nước** — giảm nhiều công cấu hình so với dòng đa dụng.

**Vì sao catalogue ghi hai mức công suất cho một model?**
Vì phân theo **tải nhẹ (bơm/quạt)** và **tải nặng (mô-men không đổi)**. Phải đọc đúng cột ứng với loại tải của bạn.

**Lắp biến tần ngoài trời được không?**
Chỉ khi dùng loại có **cấp bảo vệ phù hợp (IP54 trở lên)**. Loại IP20 thông thường **bắt buộc đặt trong tủ điện**.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /cach-chon-bien-tan/, /che-do-dieu-khien-vf-vector/, /bien-tan-1-pha-ra-3-pha/, /lien-he/. -->
