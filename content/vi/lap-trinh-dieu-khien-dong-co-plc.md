<!--
LOẠI TRANG : Blog kỹ thuật (hướng dẫn lập trình) + Thương mại
URL SLUG   : /lap-trinh-dieu-khien-dong-co-plc/
TỪ KHÓA    : lập trình plc điều khiển động cơ | plc điều khiển motor | mạch start stop plc | đảo chiều động cơ plc | plc contactor biến tần
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Lập Trình PLC Điều Khiển Động Cơ: Start/Stop & Đảo Chiều
META (150)  : Hướng dẫn lập trình PLC điều khiển động cơ: mạch start/stop có tự giữ, đảo chiều quay, khóa liên động và điều khiển tốc độ qua biến tần, kèm lưu ý an toàn.
H1          : Lập Trình PLC Điều Khiển Động Cơ: Start/Stop, Đảo Chiều

---

## Lập trình PLC điều khiển động cơ như thế nào?

<!--IMG:rep-->
![PLC điều khiển động cơ qua contactor/biến tần](assets/diagrams/dieu-khien-dong-co-plc.svg)


**Lập trình PLC điều khiển động cơ** là bài toán cơ bản và phổ biến nhất trong tự động hóa. PLC nhận lệnh từ **nút nhấn/cảm biến**, xử lý logic rồi điều khiển **contactor (đóng/cắt)** hoặc **biến tần (điều chỉnh tốc độ)** để chạy động cơ. Nắm vững phần này là nền tảng cho hầu hết máy móc.

> **Cần hỗ trợ lập trình điều khiển động cơ?** Gửi **yêu cầu** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## 1. Mạch Start/Stop có tự giữ

<!--IMG:prin-->
![Ví dụ chương trình Ladder](assets/diagrams/ladder-co-ban.svg)


Logic cơ bản:

- Nhấn **Start** → ngõ ra động cơ (Y0) bật.
- **Tiếp điểm tự giữ Y0** song song với Start → giữ chạy dù nhả nút.
- Nhấn **Stop** (tiếp điểm thường đóng) → cắt mạch, Y0 tắt.

Đây chính là mạch seal-in đã nêu trong [lập trình PLC Ladder cơ bản](/lap-trinh-ladder-plc/).

## 2. Đảo chiều quay (thuận/nghịch)

Dùng **hai ngõ ra** (Y0 chạy thuận, Y1 chạy nghịch), điều khiển hai contactor. Bắt buộc có **khóa liên động (interlock)**: mỗi ngõ ra dùng **tiếp điểm thường đóng của ngõ kia** để **không bao giờ bật đồng thời** (tránh ngắn mạch pha). Nên thêm **thời gian trễ** khi chuyển chiều.

## 3. Bảo vệ và khóa liên động

<!--IMG:app-->
![PLC điều khiển động cơ](assets/diagrams/dieu-khien-dong-co-plc.svg)


- Đưa tín hiệu **rơ le nhiệt/quá tải** vào PLC để **dừng khi sự cố**.
- **Khóa liên động** thuận–nghịch, dừng khẩn (E-Stop) đấu cứng độc lập.
- Dùng **relay trung gian** bảo vệ ngõ ra khi tải lớn.

## 4. Điều khiển tốc độ qua biến tần

Khi cần **thay đổi tốc độ**, PLC điều khiển **biến tần** — qua tiếp điểm/analog hoặc **Modbus**. Xem chi tiết: [kết nối PLC với biến tần](/ket-noi-plc-bien-tan/).

---

## Lưu ý an toàn

- **Nút dừng khẩn (E-Stop)** phải cắt trực tiếp mạch động lực, không chỉ qua PLC.
- Tuân thủ **an toàn điện (LOTO)** khi lắp đặt, bảo trì.
- Kiểm tra kỹ **khóa liên động** trước khi chạy thử.

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **loại động cơ · yêu cầu (thuận/nghịch/tốc độ) · hãng PLC.** Chúng tôi hỗ trợ lập trình và **báo giá PLC/biến tần/contactor**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Mạch Start/Stop động cơ trên PLC hoạt động thế nào?**
Nhấn Start bật ngõ ra động cơ, **tiếp điểm tự giữ** duy trì chạy dù nhả nút; nhấn Stop (thường đóng) cắt mạch để dừng.

**Vì sao cần khóa liên động khi đảo chiều động cơ?**
Để **không bao giờ bật đồng thời** hai contactor thuận–nghịch, tránh **ngắn mạch pha**. Mỗi ngõ ra dùng tiếp điểm thường đóng của ngõ kia và nên thêm trễ khi chuyển chiều.

**PLC điều khiển tốc độ động cơ bằng cách nào?**
Qua **biến tần** — dùng tiếp điểm/analog hoặc **Modbus** để đặt tần số. Xem [kết nối PLC với biến tần](/ket-noi-plc-bien-tan/).

**Có thể điều khiển nhiều động cơ bằng một PLC không?**
Có, miễn đủ **ngõ ra và dòng điều khiển**; mỗi động cơ một mạch logic riêng (start/stop, bảo vệ), dùng **relay trung gian** cho tải lớn.

**Điều khiển sao/tam giác (Y/Δ) bằng PLC thế nào?**
Dùng **ba contactor** (chính, sao, tam giác) với **timer** chuyển từ sao sang tam giác sau vài giây khởi động, kèm **khóa liên động** giữa contactor sao và tam giác để tránh sự cố.

**Nút dừng khẩn (E-Stop) có nên đi qua PLC không?**
Không nên chỉ qua PLC. E-Stop phải **cắt trực tiếp mạch động lực** theo tiêu chuẩn an toàn; PLC chỉ đọc trạng thái để dừng logic — như vậy hệ vẫn **dừng được ngay cả khi PLC lỗi**.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lập trình PLC điều khiển động cơ) + Article.
     INTERNAL LINK RA: /lap-trinh-ladder-plc/, /ket-noi-plc-bien-tan/, /plc-la-gi/, /lien-he/. -->
