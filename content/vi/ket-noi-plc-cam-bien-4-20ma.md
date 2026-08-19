<!--
LOẠI TRANG : Blog kỹ thuật (hướng dẫn) + Thương mại
URL SLUG   : /ket-noi-plc-cam-bien-4-20ma/
TỪ KHÓA    : kết nối plc với cảm biến 4-20ma | đấu cảm biến analog vào plc | ngõ vào analog plc | cảm biến 2 dây 3 dây plc | scale 4-20ma plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Kết Nối PLC Với Cảm Biến 4-20mA: Hướng Dẫn Đấu Dây
META (151)  : Hướng dẫn kết nối PLC với cảm biến 4-20mA: đấu 2 dây/3 dây/4 dây, chọn ngõ vào analog, scale giá trị và xử lý lỗi tín hiệu analog thường gặp.
H1          : Kết Nối PLC Với Cảm Biến 4-20mA: Đấu Dây Và Scale Tín Hiệu

---

## Kết nối PLC với cảm biến 4-20mA như thế nào?

<!--IMG:rep-->
![Kết nối PLC với cảm biến 4-20mA: đấu dây NPN/PNP và analog](assets/diagrams/io-sink-source.svg)


**Kết nối PLC với cảm biến 4-20mA** là công việc thường gặp khi đọc **áp suất, nhiệt độ, mức, lưu lượng**. Tín hiệu **4-20mA** chống nhiễu tốt và truyền xa. Việc cần làm gồm: **đấu đúng kiểu dây (2/3/4 dây), chọn đúng ngõ vào analog** và **scale giá trị** trong chương trình.

> **Cần hỗ trợ đấu cảm biến vào PLC?** Gửi **loại cảm biến + model PLC** → [Tư vấn kỹ thuật & báo giá](#bao-gia).

---

## Đấu dây theo loại cảm biến

### Cảm biến 2 dây (loop-powered)

Cảm biến lấy nguồn ngay trên vòng dòng: **nguồn 24V → cảm biến → ngõ vào AI của PLC → về 0V**. Đơn giản, ít dây.

### Cảm biến 3 dây / 4 dây

- **3 dây:** +24V, 0V (GND chung) và **OUT 4-20mA** vào AI.
- **4 dây:** nguồn riêng và tín hiệu ra riêng (cách ly hơn).

> Xác định đúng **loop cấp nguồn** và **chiều dòng** theo tài liệu cảm biến để không đấu sai.

### Ngõ vào dòng hay áp?

Chọn đúng **ngõ vào kiểu dòng (mA)** trên module analog; nếu module là kiểu áp (V), cần **điện trở shunt** hoặc bộ chuyển đổi phù hợp.

---

## Scale giá trị trong chương trình

<!--IMG:prin-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


PLC đọc analog thành **giá trị số (ví dụ 0–32000 hoặc 0–4000)**. Cần **scale tuyến tính** từ dải số này sang **đơn vị kỹ thuật** (bar, °C, %) theo dải cảm biến. Lưu ý:

- **4mA = giá trị đầu dải**, **20mA = giá trị cuối dải**.
- Kiểm tra **offset live-zero** (4mA), phát hiện **đứt dây khi < 4mA**.
- Đọc đúng **độ phân giải** module analog.

---

## Lỗi thường gặp và cách khắc phục

<!--IMG:app-->
![6 nhóm lỗi PLC thường gặp](assets/diagrams/app-nhom-loi-plc.svg)


- **Không đọc được (0mA):** đứt dây, sai loop nguồn, chọn nhầm ngõ áp/dòng → kiểm tra nguồn loop và kiểu ngõ vào.
- **Giá trị nhảy/nhiễu:** dây tín hiệu gần động lực → cáp shielded, tách dây, nối đất; xem [lỗi PLC do nhiễu](/loi-plc-do-nhieu/).
- **Sai đơn vị:** scale sai dải → kiểm tra lại công thức scale.

Xem thêm: [lỗi ngõ vào ra PLC (I/O)](/loi-ngo-vao-ra-plc/) và [đấu dây cảm biến áp suất 4-20mA](/dau-day-cam-bien-ap-suat-4-20ma/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá

Gửi cho chúng tôi: **loại cảm biến (2/3/4 dây) · dải đo · model PLC/module analog.** Chúng tôi hỗ trợ đấu nối và **báo giá cảm biến/module/bộ chuyển đổi**.

**→ [Liên hệ tư vấn & báo giá](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến 2 dây và 3 dây đấu vào PLC khác nhau thế nào?**
**2 dây** lấy nguồn trên vòng dòng (nguồn → cảm biến → AI → 0V); **3 dây** có +24V, 0V và dây OUT 4-20mA riêng vào ngõ vào analog.

**Vì sao PLC đọc analog nhưng giá trị sai đơn vị?**
Do **scale sai dải**: cần map 4mA = đầu dải, 20mA = cuối dải sang đơn vị kỹ thuật. Kiểm tra lại công thức và độ phân giải module.

**Làm sao phát hiện đứt dây cảm biến 4-20mA?**
Vì tín hiệu **live-zero (4mA)**, khi dòng **< 4mA (gần 0)** thường là **đứt dây/mất nguồn loop**. Có thể lập trình cảnh báo khi dưới ngưỡng.

**Nên dùng cảm biến 4-20mA hay 0-10V với PLC?**
**4-20mA** chống nhiễu tốt và **truyền xa** hơn, lại phát hiện được đứt dây (live-zero) nên được ưu tiên trong công nghiệp. **0-10V** đơn giản, phù hợp khoảng cách ngắn. Quan trọng là chọn đúng **kiểu ngõ vào (dòng hay áp)** trên module analog cho khớp loại tín hiệu.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Kết nối PLC với cảm biến 4-20mA) + Article.
     INTERNAL LINK RA: /loi-plc-do-nhieu/, /loi-ngo-vao-ra-plc/, /dau-day-cam-bien-ap-suat-4-20ma/, /lien-he/. -->
