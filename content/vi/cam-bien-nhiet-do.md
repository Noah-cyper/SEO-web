<!--
LOẠI TRANG : Bài trụ (pillar) — Thông tin + Thương mại
URL SLUG   : /cam-bien-nhiet-do/
TỪ KHÓA    : cảm biến nhiệt độ | cảm biến nhiệt độ là gì | pt100 | can nhiệt | cảm biến nhiệt độ pt100 | cách chọn cảm biến nhiệt độ
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Kiểm tra thông số theo datasheet trước khi lên web.
-->

TITLE TAG   : Cảm Biến Nhiệt Độ Là Gì? Pt100, Can Nhiệt – Cách Chọn & Báo Giá
META (157)  : Cảm biến nhiệt độ là gì, phân biệt Pt100 (RTD) và can nhiệt (thermocouple), nguyên lý và cách chọn đúng dải nhiệt – kiểu đấu dây – tín hiệu. Kèm ứng dụng và báo giá chính hãng.
H1          : Cảm Biến Nhiệt Độ Là Gì? Pt100, Can Nhiệt Và Cách Chọn Đúng

---

## Cảm biến nhiệt độ là gì?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-temp.svg)


**Cảm biến nhiệt độ** là thiết bị đo nhiệt độ và chuyển thành tín hiệu để đưa về bộ điều khiển, hiển thị hay SCADA. Hai loại phổ biến nhất trong công nghiệp là **Pt100 (RTD)** và **can nhiệt (thermocouple)**. Tín hiệu từ cảm biến thường được đưa qua **bộ chuyển đổi (transmitter)** để ra chuẩn **4-20mA/0-10V** trước khi vào PLC.

> **Cần báo giá?** Gửi **dải nhiệt độ · loại (Pt100/can nhiệt) · kiểu lắp** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/rtd-vs-tc.svg)


---

## Phân loại cảm biến nhiệt độ

| Loại | Đặc điểm | Dải nhiệt tiêu biểu | Chọn khi |
|---|---|---|---|
| **Pt100 (RTD)** | Chính xác, ổn định, tuyến tính tốt | ~ -200…+600°C | Cần **độ chính xác cao**, dải vừa |
| **Can nhiệt K/J/T/S…** (thermocouple) | Chịu **nhiệt rất cao**, bền, rẻ | tới ~1200°C+ (loại K, S) | Lò nung, nhiệt độ **rất cao** |
| **Cảm biến bán dẫn / IC** | Rẻ, dải hẹp | thấp | Ứng dụng dân dụng, dải nhỏ |

**Ghi nhớ nhanh:** cần **chính xác** → Pt100; cần **nhiệt độ cực cao** → can nhiệt.

---

## Nguyên lý

- **Pt100 (RTD):** điện trở thay đổi theo nhiệt độ (100Ω ở 0°C). Đo điện trở → suy ra nhiệt độ.
- **Can nhiệt:** hai kim loại khác nhau tạo ra điện áp (mV) theo chênh lệch nhiệt độ (hiệu ứng Seebeck).

Do tín hiệu gốc (điện trở / mV) yếu, thường dùng **bộ chuyển đổi nhiệt độ** như [K109PT (Seneca)](/k109pt-seneca/) để ra 4-20mA/0-10V.

---

## Cách chọn cảm biến nhiệt độ (5 bước)

1. **Dải nhiệt độ đo:** chọn Pt100 (dải vừa, chính xác) hay can nhiệt (rất cao).
2. **Độ chính xác cần thiết:** cao → Pt100.
3. **Kiểu đấu dây Pt100:** 2 / 3 / 4 dây (3–4 dây chính xác hơn, bù trừ điện trở dây).
4. **Kiểu lắp cơ khí:** que thẳng, có ren, có củ hành/đầu nối, chiều dài que, vật liệu vỏ (inox 304/316).
5. **Tín hiệu đầu ra:** cần transmitter tích hợp (ra 4-20mA) hay đưa tín hiệu gốc về bộ chuyển đổi riêng.

---

## Ứng dụng

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-temp.svg)


- Lò hơi, lò nung, nhiệt điện (can nhiệt cho nhiệt cao).
- Đo nhiệt đường ống, bồn chứa, máy móc (Pt100).
- Thực phẩm, dược, HVAC (Pt100 inox).

---

## Vì sao chọn tại HOANTRANTDH

- ✅ Chính hãng, CO/CQ, hóa đơn VAT.
- ✅ Tư vấn chọn **Pt100 hay can nhiệt**, kèm **bộ chuyển đổi** phù hợp.
- ✅ Cung cấp đồng bộ cảm biến + [bộ chuyển đổi nhiệt độ K109PT](/k109pt-seneca/) + hiển thị.

---

<a name="bao-gia"></a>
## Nhận báo giá & tư vấn

Gửi: **dải nhiệt độ · loại (Pt100/can nhiệt) · kiểu lắp & chiều dài que · tín hiệu ngõ ra · số lượng.**

**→ [Liên hệ báo giá cảm biến nhiệt độ](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Nên chọn Pt100 hay can nhiệt?**
Cần độ chính xác cao và dải nhiệt vừa → **Pt100**. Cần đo nhiệt độ rất cao (lò nung, tới hơn 1000°C) → **can nhiệt**.

**Pt100 đấu 2, 3 hay 4 dây khác gì nhau?**
Càng nhiều dây càng bù trừ được điện trở dây dẫn → chính xác hơn. 3 dây phổ biến trong công nghiệp; 4 dây cho phòng thí nghiệm/độ chính xác cao.

**Làm sao đưa Pt100 về PLC chỉ nhận 4-20mA?**
Dùng bộ chuyển đổi nhiệt độ (transmitter), ví dụ **K109PT** của Seneca: Pt100 → 4-20mA/0-10V.

**Cảm biến nhiệt độ có chính hãng, CO/CQ không?**
Có. Hàng chính hãng kèm CO/CQ và hóa đơn VAT.

<!-- SCHEMA: FAQPage + BreadcrumbList (Trang chủ › Cảm biến › Cảm biến nhiệt độ).
     INTERNAL LINK: /k109pt-seneca/, /cam-bien-ap-suat/, /bo-chuyen-doi-tin-hieu-seneca/, /lien-he/. -->
