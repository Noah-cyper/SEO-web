<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật — Thông tin + thương mại
URL SLUG   : /tinh-cong-suat-dung-luong-bess/
TỪ KHÓA    : tính công suất bess | tính dung lượng pin lưu trữ | c-rate | kw hay kwh | chọn dung lượng bess
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Ví dụ minh hoạ, cần áp số liệu đo thực tế của từng dự án.
-->

TITLE TAG   : Cách Tính Công Suất & Dung Lượng BESS – kW, kWh Và C-rate
META (156)  : Hướng dẫn tính công suất (kW) và dung lượng (kWh) cho hệ lưu trữ BESS: phân biệt kW và kWh, ý nghĩa C-rate, quy trình 6 bước có ví dụ và các sai lầm thường gặp khi chọn cấu hình.
H1          : Cách Tính Công Suất & Dung Lượng Cho Hệ Lưu Trữ BESS

---

## Hai con số quan trọng nhất: kW và kWh

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bess-cabinet.svg)


Sai lầm phổ biến nhất khi mua hệ lưu trữ là **nhầm lẫn giữa công suất và dung lượng**. Đây là hai đại lượng hoàn toàn khác nhau và phục vụ hai mục đích khác nhau.

Hãy dùng một hình ảnh dễ hiểu — **một bình nước có vòi**:

- **Dung lượng (kWh)** = **kích thước bình nước**. Nó cho biết bạn chứa được **bao nhiêu** năng lượng, tức xả được **bao lâu**.
- **Công suất (kW)** = **độ lớn của vòi**. Nó cho biết bạn lấy ra được **nhanh cỡ nào** tại một thời điểm.

Một bình rất lớn nhưng vòi bé thì không thể chữa cháy. Ngược lại, vòi rất to nhưng bình bé thì chỉ xịt được vài giây. **Hệ BESS cũng vậy — phải cân đối cả hai.**

> **Muốn biết nhà máy mình cần cấu hình nào?** Gửi **hoá đơn điện · biểu đồ phụ tải** → [Nhận tính toán sơ bộ](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-peakshaving.svg)


---

## C-rate: chỉ số nối hai con số lại với nhau

**C-rate** là tỷ lệ giữa công suất và dung lượng:

> **C-rate = Công suất (kW) ÷ Dung lượng (kWh)**

Ý nghĩa thực tế: C-rate cho biết hệ **xả hết dung lượng trong bao lâu** ở công suất định mức.

| C-rate | Thời gian xả hết | Phù hợp với |
|---|---|---|
| **0,25C** | ~4 giờ | Dịch tải dài, lưu trữ nhiều giờ |
| **0,5C** | ~2 giờ | **Phổ biến nhất** — cắt đỉnh tiêu chuẩn |
| **1C** | ~1 giờ | Đỉnh nhọn, phản ứng nhanh |
| **2C** | ~30 phút | Trạm sạc, điều tần, đỉnh rất ngắn |

Ví dụ: một tủ **100 kW / 215 kWh** như [EGS215](/egs215-renepoly/) có C-rate ≈ **0,47C** — tức xả hết trong khoảng **2 giờ**. Đây là cấu hình cân bằng, phù hợp với bài toán cắt đỉnh phổ biến nhất của nhà máy Việt Nam.

Ngược lại, một [trạm sạc xe điện](/bess-cho-tram-sac-xe-dien/) cần xả rất mạnh trong thời gian ngắn, nên thường cần **C-rate cao hơn**.

---

## Quy trình 6 bước để tính đúng

### Bước 1 — Đo biểu đồ phụ tải thực tế

Đây là bước không thể bỏ qua. Cần dữ liệu **công suất theo thời gian**, tối thiểu một tuần, lý tưởng là một tháng để bắt được cả biến động theo ngày trong tuần.

Nguồn dữ liệu: công tơ điện tử của điện lực, hoặc lắp đồng hồ đo riêng như [đồng hồ đo điện năng Seneca](/dong-ho-do-dien-nang-seneca/) có truyền thông Modbus.

**Đừng thiết kế theo công suất lắp đặt** (tổng công suất danh định của tất cả thiết bị) — con số này luôn lớn hơn nhiều so với thực tế, dẫn tới đầu tư thừa.

### Bước 2 — Xác định mục tiêu và ngưỡng

Bạn muốn gì?

- **Cắt đỉnh:** chọn một **ngưỡng công suất** không muốn vượt qua.
- **Dịch tải:** xác định **lượng kWh** muốn chuyển từ giờ đắt sang giờ rẻ.
- **Dự phòng:** xác định **tải quan trọng (kW)** và **thời gian cần cầm cự (giờ)**.
- **Tăng tự dùng PV:** xác định **lượng điện dư mỗi ngày** muốn giữ lại.

Ngưỡng càng thấp thì tiết kiệm càng nhiều nhưng thiết bị càng lớn — đây là bài toán đánh đổi cần cân nhắc kỹ.

### Bước 3 — Tính công suất cần (kW)

> **Công suất = Đỉnh cao nhất − Ngưỡng mong muốn**

Ví dụ: đỉnh 380 kW, ngưỡng 300 kW → cần **80 kW**.

Với mục tiêu dự phòng, công suất phải **đủ gánh toàn bộ tải quan trọng** cùng lúc.

### Bước 4 — Tính dung lượng cần (kWh)

> **Dung lượng = Công suất bù trung bình × Thời gian**

Cần tính **diện tích phần nằm trên ngưỡng** trong biểu đồ, không phải nhân đỉnh cao nhất với thời gian (sẽ thừa rất nhiều).

Ví dụ: bù trung bình 60 kW trong 2 giờ → **120 kWh**.

### Bước 5 — Cộng hệ số dự phòng

Dung lượng danh định **không phải dung lượng dùng được**. Cần cộng thêm cho:

- **Hiệu suất vòng (round-trip):** nạp vào 100 phần không lấy ra được đủ 100 phần.
- **Giới hạn độ sâu xả (DoD):** thường không xả cạn 100% để bảo vệ tuổi thọ.
- **Suy giảm dung lượng theo năm:** pin cuối vòng đời có dung lượng thấp hơn lúc mới.

Thực tế nên cộng khoảng **10–20%**. Với ví dụ trên: 120 kWh → khoảng **135–145 kWh**.

### Bước 6 — Kiểm tra C-rate và chọn cấu hình

Tính C-rate = kW ÷ kWh, xem có hợp lý không, rồi đối chiếu với các model có sẵn.

Ví dụ: 80 kW / 140 kWh ≈ 0,57C → nằm trong vùng phổ biến. Một tủ **100 kW / 215 kWh** sẽ dư sức, đồng thời còn dung lượng để làm thêm dịch tải.

---

## Ví dụ tổng hợp theo ba tình huống

**Tình huống A — Nhà máy cắt đỉnh.**
Đỉnh 380 kW, ngưỡng 300 kW, kéo dài 2 giờ, bù trung bình 60 kW.
→ Cần ≈ **80 kW / 140 kWh** (0,57C). Một [tủ EGS215](/egs215-renepoly/) là phù hợp.

**Tình huống B — Tăng tự dùng điện mặt trời.**
Điện dư 150 kWh/ngày, muốn giữ lại 120 kWh, tải tối khoảng 60 kW.
→ Cần ≈ **60 kW / 140 kWh** (0,43C). Cấu hình thiên về dung lượng. [Xem chi tiết →](/dien-mat-troi-ket-hop-luu-tru/)

**Tình huống C — Trạm sạc xe điện.**
Đỉnh 360 kW, lưới chỉ 150 kW, cần bù 210 kW trong 45 phút, có 2 đợt/ngày.
→ Cần ≈ **210 kW / 300 kWh** (0,7C) — thiên về công suất. [Xem chi tiết →](/bess-cho-tram-sac-xe-dien/)

Ba tình huống, ba cấu hình khác hẳn nhau — dù dung lượng có thể tương đương. **Đó chính là lý do không thể mua BESS theo kiểu "cứ chọn con số kWh cho đẹp".**

---

## So sánh: khi nào ưu tiên kW, khi nào ưu tiên kWh?

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/compare-roi-bess.svg)


| Tình huống | Ưu tiên | Lý do |
|---|---|---|
| Đỉnh **rất cao nhưng ngắn** | **kW (công suất)** | Cần xả mạnh trong thời gian ngắn |
| Đỉnh **vừa nhưng kéo dài** | **kWh (dung lượng)** | Cần cầm cự lâu |
| Dịch tải theo giá điện | **kWh** | Chuyển nhiều năng lượng qua khung giờ |
| Dự phòng mất điện | **Cả hai** | Đủ gánh tải và đủ lâu |
| Tăng tự dùng PV | **kWh** | Hấp thụ hết lượng dư ban ngày |
| Trạm sạc, điều tần | **kW** | Phản ứng nhanh, công suất lớn |

---

## Năm sai lầm thường gặp

1. **Thiết kế theo công suất lắp đặt thay vì phụ tải thực đo.** Đây là nguyên nhân số một của việc đầu tư thừa.
2. **Chỉ nhìn kWh mà bỏ qua kW.** Mua nhiều dung lượng nhưng PCS yếu thì không cắt nổi đỉnh.
3. **Quên hệ số dự phòng.** Dùng thẳng dung lượng danh định dẫn tới thiếu hụt trong thực tế.
4. **Đặt ngưỡng quá thấp.** Tham tiết kiệm khiến thiết bị phình to, kéo dài thời gian hoàn vốn.
5. **Không tính khả năng mở rộng.** Nếu sản xuất sẽ mở rộng, nên chừa sẵn mặt bằng và hạ tầng đấu nối.

---

## Hiểu về dung lượng danh định và dung lượng khả dụng

Đây là chỗ khiến nhiều người bất ngờ khi hệ đi vào vận hành: **con số kWh ghi trên nhãn không phải con số bạn dùng được**.

Ba yếu tố làm giảm dung lượng thực tế:

**1. Giới hạn độ sâu xả (DoD).** Hệ thường không xả cạn 100% để bảo vệ tuổi thọ pin. Nếu DoD được giới hạn ở 90%, thì 215 kWh danh định chỉ còn khoảng 193 kWh khả dụng.

**2. Hiệu suất vòng (round-trip efficiency).** Năng lượng mất mát khi đi qua PCS hai lần và qua điện trở trong của pin. Nghĩa là để lấy ra được 100 kWh, bạn phải nạp vào nhiều hơn 100 kWh.

**3. Suy giảm dung lượng theo năm.** Pin ở năm thứ 8 có dung lượng thấp hơn lúc mới đáng kể. Nếu chỉ thiết kế vừa khít cho hiện tại, vài năm sau hệ sẽ không còn đáp ứng đủ.

**Cách xử lý thực tế:** khi tính, hãy dùng **dung lượng khả dụng ở cuối vòng đời thiết kế**, chứ không phải dung lượng danh định lúc mới. Đó là lý do khuyến nghị cộng thêm **10–20% dự phòng** — con số này chính là để bù cho ba yếu tố trên.

Ví dụ minh hoạ cách nghĩ đúng:

> Cần **120 kWh thực dùng** ở năm cuối vòng đời
> → Cộng dự phòng cho DoD, tổn hao và suy giảm
> → Chọn hệ có dung lượng danh định khoảng **140–150 kWh** trở lên

Nếu làm ngược lại — thấy cần 120 kWh rồi mua đúng 120 kWh danh định — hệ sẽ **thiếu ngay từ năm đầu** và càng thiếu về sau.

---

## Trường hợp đặc biệt: thiết kế cho dự phòng mất điện

Bài toán dự phòng khác với cắt đỉnh và cần cách tính riêng.

**Bước 1 — Xác định tải thiết yếu (kW).** Đây là tổng công suất của những thiết bị **bắt buộc phải có điện**: hệ điều khiển, máy chủ, kho lạnh, thiết bị an toàn. Đừng gộp cả nhà máy vào đây — sẽ đội quy mô lên rất nhiều.

**Bước 2 — Xác định thời gian cần cầm cự (giờ).** Thực tế cần trả lời: sự cố mất điện tại khu vực của bạn thường kéo dài bao lâu? Nếu chỉ vài phút đến vài chục phút, quy mô cần thiết nhỏ hơn nhiều so với việc thiết kế cho vài giờ.

**Bước 3 — Nhân ra kWh, rồi cộng dự phòng.**

**Bước 4 — Kiểm tra công suất PCS.** PCS phải **đủ gánh toàn bộ tải thiết yếu cùng lúc**, kể cả dòng khởi động của động cơ. Đây là điểm hay bị bỏ sót: động cơ khi khởi động có thể rút dòng lớn hơn nhiều so với lúc chạy ổn định.

**Bước 5 — Quyết định mức dự trữ SOC.** Nếu hệ vừa cắt đỉnh vừa dự phòng, EMS phải luôn **giữ lại một phần SOC** không dùng cho mục đích kinh tế. Phần giữ lại này trực tiếp làm giảm dung lượng dành cho việc tiết kiệm tiền điện — cần cân đối rõ ràng.

**Một lưu ý về kết hợp:** nếu cơ sở đã có máy phát diesel, có thể thiết kế BESS chỉ để **giữ điện trong vài phút đầu** cho tới khi máy phát khởi động và ổn định. Cách này giảm đáng kể quy mô pin cần thiết mà vẫn đạt mục tiêu không gián đoạn. [Tìm hiểu cách phối hợp →](/microgrid-la-gi/)

---

## Cam kết tại HOANTRANTDH

- ✅ **Phân tích hoá đơn và biểu đồ phụ tải miễn phí** trước khi báo giá.
- ✅ Tính toán **kW/kWh/C-rate** theo số liệu thật, đề xuất cấu hình tối ưu — không bán thừa.
- ✅ Phân phối [Renepoly](/renepoly/): [tủ BESS](/tu-luu-tru-nang-luong-renepoly/), [container](/container-luu-tru-nang-luong-renepoly/), PCS, EMS.
- ✅ Hỗ trợ lắp đo đếm để **chứng minh hiệu quả thực tế** sau khi vận hành.

---

<a name="bao-gia"></a>
## Nhận tính toán & báo giá

Gửi: **hoá đơn điện 3–6 tháng · biểu đồ phụ tải (nếu có) · công suất đăng ký · mục tiêu (cắt đỉnh / dịch tải / dự phòng / tự dùng PV) · kế hoạch mở rộng.**

**→ [Liên hệ nhận tính toán cấu hình BESS](/lien-he/)**

---

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-sizing.svg)



<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-factory-bess.svg)

## Câu hỏi thường gặp (FAQ)

**kW và kWh khác nhau thế nào?**
**kW** là **công suất** — lấy ra được nhanh cỡ nào. **kWh** là **dung lượng** — chứa được bao nhiêu, xả được bao lâu.

**C-rate 0.5C nghĩa là gì?**
Nghĩa là hệ **xả hết dung lượng trong khoảng 2 giờ** ở công suất định mức. Ví dụ 100 kW với 200 kWh.

**Nên chọn C-rate nào?**
Tuỳ bài toán: cắt đỉnh tiêu chuẩn thường **0,5C**; trạm sạc hoặc điều tần cần **cao hơn**; dịch tải dài giờ cần **thấp hơn**.

**Vì sao phải cộng thêm 10–20% dự phòng?**
Vì có **tổn hao hiệu suất vòng**, **giới hạn độ sâu xả (DoD)** và **suy giảm dung lượng theo năm** — dung lượng danh định không phải dung lượng dùng được.

**Có cần đo phụ tải trước không?**
**Rất nên.** Thiết kế theo cảm tính hoặc theo công suất lắp đặt gần như luôn dẫn tới thừa hoặc thiếu.

**Sau này mở rộng được không?**
Được, nếu thiết kế theo hướng module hoá — thêm tủ hoặc thêm rack. Nên chừa sẵn mặt bằng và hạ tầng đấu nối ngay từ đầu.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /renepoly/, /peak-shaving-cat-dinh-tai/, /bess-cho-nha-may-khu-cong-nghiep/, /egs215-renepoly/, /lien-he/. -->
