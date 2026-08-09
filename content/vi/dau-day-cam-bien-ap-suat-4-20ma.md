<!--
LOẠI TRANG : Blog kỹ thuật how-to (top-funnel + kéo về sản phẩm)
URL SLUG   : /dau-day-cam-bien-ap-suat-4-20ma/
TỪ KHÓA    : đấu dây cảm biến áp suất | cảm biến áp suất 4-20ma 2 dây 3 dây | cách đấu cảm biến áp suất | sơ đồ đấu dây 4-20ma
INTENT     : Thông tin (kỹ thuật) → Thương mại
TRẠNG THÁI : Sẵn đăng. Rà kỹ thuật với người có chuyên môn trước khi lên web.
-->

TITLE TAG   : Cách Đấu Dây Cảm Biến Áp Suất 4-20mA (2 Dây, 3 Dây) – Hướng Dẫn
META (155)  : Hướng dẫn đấu dây cảm biến áp suất 4-20mA loại 2 dây, 3 dây và 4 dây: sơ đồ, nguồn 24VDC, cách đọc tín hiệu về PLC và lỗi thường gặp khi đấu sai.
H1          : Cách Đấu Dây Cảm Biến Áp Suất 4-20mA (2 Dây, 3 Dây, 4 Dây)

---

## Tín hiệu 4-20mA và loại đấu dây

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/wiring-4-20ma-2wire.svg)


Cảm biến áp suất công nghiệp phổ biến nhất dùng tín hiệu **4-20mA** (4mA = mức thấp nhất, 20mA = cao nhất). Có 3 kiểu đấu dây:

| Loại | Số dây | Nguồn | Đặc điểm |
|---|---|---|---|
| **2 dây (loop-powered)** | 2 | Nguồn nằm trên vòng dòng | Phổ biến nhất, đi xa, ít dây |
| **3 dây** | 3 | Nguồn + tín hiệu chung mass | Khi cần công suất/tín hiệu riêng |
| **4 dây** | 4 | Nguồn riêng, tín hiệu riêng | Cách ly rõ nguồn và tín hiệu |

> ⚠️ **Luôn đối chiếu sơ đồ trên nhãn/datasheet của cảm biến** — ký hiệu chân có thể khác nhau giữa các hãng.

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/wiring-4-20ma-3wire.svg)


---

## 1. Đấu dây cảm biến 2 dây (loop-powered) — phổ biến nhất

Nguyên tắc: **nguồn 24VDC – cảm biến – ngõ vào analog của PLC** nối tiếp thành một vòng (loop), dòng 4-20mA chạy trong vòng đó.

- Cực **+** nguồn 24VDC → chân **+** (supply) của cảm biến.
- Chân **–/out** của cảm biến → chân **AI+ (analog input)** của PLC.
- Chân **AI–** của PLC → cực **–** nguồn 24VDC.

Cả nguồn và tín hiệu dùng chung một vòng dây → tiết kiệm dây, chống nhiễu tốt khi đi xa.

---

## 2. Đấu dây 3 dây

- Dây 1: **+24VDC** cấp nguồn cảm biến.
- Dây 2: **0V (GND)** chung.
- Dây 3: **tín hiệu 4-20mA (OUT)** về AI của PLC (AI– nối GND chung).

---

## 3. Đấu dây 4 dây

Nguồn cấp (2 dây) và tín hiệu ra (2 dây) **tách riêng** — dùng khi cần cách ly rõ ràng giữa nguồn và tín hiệu.

---

## Đọc 4-20mA khi PLC chỉ nhận điện áp (0-10V)?

Nếu ngõ vào PLC chỉ nhận **áp (0-10V)** mà cảm biến ra **dòng (4-20mA)**, có 2 cách:

1. Mắc **điện trở 250Ω** trên vòng dòng để quy 4-20mA → 1-5V (rồi đọc áp).
2. **Khuyên dùng:** dùng **bộ chuyển đổi tín hiệu** như [K109S (Seneca)](/k109s-seneca/) để chuyển 4-20mA ↔ 0-10V có **cách ly chống nhiễu** — sạch và ổn định hơn.

---

## Lỗi thường gặp khi đấu sai

- **Không lên tín hiệu / báo 0mA:** ngược cực nguồn, đứt vòng, thiếu nguồn 24VDC.
- **Nhiễu, giá trị nhảy:** đi dây tín hiệu chung máng với dây động lực; thiếu cách ly → dùng bộ chuyển đổi cách ly.
- **Luôn ~4mA hoặc ~20mA cứng:** sai dải đo hoặc cảm biến quá/thiếu áp, hoặc đấu nhầm chân.

---

## Cần cảm biến / bộ chuyển đổi phù hợp?

- Xem [cách chọn cảm biến áp suất](/cam-bien-ap-suat/).
- Cần chuyển/cách ly 4-20mA ↔ 0-10V: [bộ chuyển đổi tín hiệu Seneca](/bo-chuyen-doi-tin-hieu-seneca/).

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/signal-chain.svg)

## Câu hỏi thường gặp (FAQ)

**Cảm biến áp suất 2 dây và 3 dây khác gì nhau?**
Loại 2 dây (loop-powered) dùng chung một vòng cho cả nguồn và tín hiệu, tiết kiệm dây, đi xa tốt. Loại 3 dây tách nguồn và tín hiệu (chung mass).

**Đấu cảm biến 4-20mA cần nguồn bao nhiêu?**
Thường là **24VDC**. Kiểm tra dải nguồn trên datasheet của cảm biến.

**PLC chỉ nhận 0-10V thì đọc 4-20mA thế nào?**
Dùng điện trở 250Ω (được 1-5V) hoặc tốt hơn là bộ chuyển đổi tín hiệu có cách ly (vd K109S) để chuyển 4-20mA sang 0-10V.

**Vì sao tín hiệu bị nhiễu, nhảy số?**
Thường do đi dây tín hiệu chung với dây động lực hoặc thiếu cách ly — nên tách dây và dùng bộ chuyển đổi cách ly.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-ap-suat/, /k109s-seneca/, /bo-chuyen-doi-tin-hieu-seneca/, /lien-he/. -->
