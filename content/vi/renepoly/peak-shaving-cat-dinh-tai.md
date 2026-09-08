<!--
LOẠI TRANG : Bài giải pháp (pillar) — Thông tin + thương mại
URL SLUG   : /peak-shaving-cat-dinh-tai/
TỪ KHÓA    : peak shaving | cắt đỉnh phụ tải | giảm tiền điện giờ cao điểm | load shifting | dịch tải bằng pin
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Ví dụ tính toán mang tính minh hoạ, cần áp số liệu thực tế.
-->

TITLE TAG   : Peak Shaving Là Gì? Cắt Đỉnh Phụ Tải Giảm Tiền Điện Bằng BESS
META (156)  : Peak shaving là gì? Cách dùng hệ lưu trữ BESS để cắt đỉnh phụ tải, giảm tiền điện giờ cao điểm và phí công suất. Phân biệt peak shaving và load shifting, cách tính kW/kWh cần thiết.
H1          : Peak Shaving – Cắt Đỉnh Phụ Tải Để Giảm Tiền Điện

---

## Peak shaving là gì?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bess-cabinet.svg)


**Peak shaving** (cắt đỉnh phụ tải) là kỹ thuật **giảm công suất tiêu thụ cực đại** của một cơ sở bằng cách dùng nguồn dự trữ bù vào đúng những khoảnh khắc phụ tải vọt lên cao nhất.

Hãy hình dung biểu đồ công suất của nhà máy trong một ngày. Phần lớn thời gian, đường tải nằm ở mức trung bình. Nhưng vào một vài khung giờ — thường là khi nhiều máy khởi động cùng lúc, hoặc ca sản xuất cao điểm — đường tải vọt lên tạo thành những **đỉnh nhọn**. Chính những đỉnh này gây tốn kém bất tương xứng, vì hai lý do:

1. **Giá điện giờ cao điểm** đắt hơn đáng kể so với giờ bình thường và thấp điểm.
2. **Phí công suất** ở nhiều biểu giá được tính theo **công suất cực đại đăng ký hoặc đo được** — nghĩa là chỉ vài phút đỉnh trong tháng cũng có thể quyết định chi phí của cả kỳ.

Peak shaving dùng hệ **BESS** để **xả điện ra đúng lúc đỉnh xuất hiện**, kéo đường tải nhìn từ phía lưới xuống dưới một ngưỡng đặt trước.

> **Muốn biết nhà máy mình tiết kiệm được bao nhiêu?** Gửi **hoá đơn điện 3–6 tháng · biểu đồ phụ tải nếu có** → [Nhận tính toán sơ bộ miễn phí](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-peakshaving.svg)


---

## Nguyên lý hoạt động

Cơ chế rất trực tiếp:

1. **EMS đặt một ngưỡng công suất** (ví dụ 300 kW) — đây là mức mà bạn không muốn vượt qua khi nhìn từ đồng hồ điện lực.
2. **Đo liên tục công suất tức thời** của toàn cơ sở.
3. Khi công suất tiến gần ngưỡng, EMS **lệnh cho PCS xả** đúng phần chênh lệch. Nếu tải là 380 kW và ngưỡng là 300 kW, BESS xả 80 kW.
4. Kết quả: **đồng hồ điện lực chỉ ghi nhận 300 kW**, phần 80 kW còn lại đến từ pin.
5. Khi qua giờ cao điểm, EMS **nạp lại** pin bằng điện giá rẻ hoặc điện mặt trời dư.

Điểm tinh tế nằm ở chỗ hệ phải **dự đoán và phản ứng đủ nhanh**. Nếu chờ đến khi vượt ngưỡng mới xả thì đỉnh đã được ghi nhận rồi. Vì vậy EMS tốt sẽ theo dõi xu hướng tải và bắt đầu xả **trước khi** chạm ngưỡng. [Tìm hiểu EMS →](/ems-quan-ly-nang-luong-renepoly/)

---

## Phân biệt peak shaving và load shifting

Hai khái niệm thường bị nhầm, nhưng mục tiêu khác nhau:

| | **Peak shaving** | **Load shifting** |
|---|---|---|
| Mục tiêu | Giảm **công suất cực đại** (kW) | Giảm **chi phí năng lượng** (kWh) |
| Cách làm | Xả đúng lúc đỉnh nhọn | Nạp giờ rẻ, xả giờ đắt trong thời gian dài |
| Tiết kiệm từ | **Phí công suất** + giá giờ cao điểm | **Chênh lệch giá** theo khung giờ |
| Yêu cầu thiết bị | Thiên về **công suất (kW)** | Thiên về **dung lượng (kWh)** |
| Thời lượng xả | Ngắn, tập trung | Dài, đều |

Trong thực tế, **một hệ BESS thường làm cả hai** — EMS điều phối để tối ưu tổng lợi ích. Nhưng khi chọn cấu hình, bạn cần biết mục tiêu nào là chính, vì nó quyết định tỷ lệ giữa kW và kWh.

---

## Cách tính công suất và dung lượng cần thiết

Đây là phần quan trọng nhất và cũng hay bị làm sai nhất. Quy trình bốn bước:

**Bước 1 — Đo biểu đồ phụ tải.** Cần dữ liệu công suất theo thời gian, tối thiểu một tuần, lý tưởng là một tháng. Có thể lấy từ công tơ điện tử của điện lực hoặc lắp đồng hồ đo riêng như [đồng hồ đo điện năng Seneca](/dong-ho-do-dien-nang-seneca/).

**Bước 2 — Xác định ngưỡng mong muốn.** Nhìn biểu đồ, chọn mức ngưỡng hợp lý. Đây là bài toán đánh đổi: ngưỡng càng thấp thì tiết kiệm càng nhiều nhưng thiết bị càng lớn và đắt.

**Bước 3 — Tính công suất (kW).** Lấy **đỉnh cao nhất trừ ngưỡng**. Ví dụ đỉnh 380 kW, ngưỡng 300 kW → cần PCS ít nhất **80 kW**.

**Bước 4 — Tính dung lượng (kWh).** Tính **diện tích phần nằm trên ngưỡng** — tức công suất bù nhân thời gian. Nếu phải bù trung bình 60 kW trong 2 giờ → cần khoảng **120 kWh**.

**Bước 5 — Cộng dự phòng.** Thêm khoảng **10–20%** cho hiệu suất vòng (nạp vào không lấy ra được 100%), giới hạn độ sâu xả (DoD) và suy giảm dung lượng theo năm. Vậy 120 kWh thành khoảng **140–145 kWh**.

Ví dụ minh hoạ: một tủ **100 kW / 215 kWh** như [EGS215](/egs215-renepoly/) sẽ dư sức cho bài toán trên, và còn dư dung lượng để làm thêm load shifting. [Xem hướng dẫn tính chi tiết →](/tinh-cong-suat-dung-luong-bess/)

---

## Ứng dụng thực tế theo ngành

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-factory-bess.svg)


- **Cơ khí, đúc, nhựa:** máy ép, lò nung khởi động tạo đỉnh rất nhọn — đối tượng lý tưởng của peak shaving.
- **Dệt may, thực phẩm:** ca sản xuất cao điểm kéo dài, phù hợp kết hợp cả peak shaving và load shifting.
- **Kho lạnh:** máy nén chạy theo chu kỳ, tạo đỉnh lặp lại đều đặn.
- **Trung tâm thương mại, toà nhà:** hệ điều hoà tạo đỉnh vào buổi trưa và chiều.
- **Trạm sạc xe điện:** đỉnh xuất hiện khi nhiều xe sạc cùng lúc — BESS giúp **tránh phải nâng cấp trạm biến áp**. [Xem chi tiết →](/bess-cho-tram-sac-xe-dien/)

---

## So sánh các nguồn hoàn vốn khi đầu tư

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/compare-roi-bess.svg)


Nhiều chủ đầu tư chỉ tính riêng chênh lệch giá điện rồi kết luận "lâu hoàn vốn". Thực tế nên cộng đủ các nguồn giá trị:

| Nguồn giá trị | Mô tả |
|---|---|
| **Chênh lệch giá theo giờ** | Nạp thấp điểm, xả cao điểm |
| **Giảm phí công suất** | Hạ mức công suất cực đại ghi nhận |
| **Tăng tự dùng điện mặt trời** | Bớt phải mua điện lưới buổi tối |
| **Tránh thiệt hại dừng sản xuất** | Giá trị lớn với dây chuyền tự động |
| **Trì hoãn nâng cấp hạ tầng** | Không phải nâng máy biến áp/đường dây |
| **Giá trị môi trường** | Hỗ trợ mục tiêu ESG, giảm phát thải |

Khi cộng đủ, bài toán thường khả quan hơn nhiều so với chỉ nhìn một chiều. Điều kiện là phải **tính trên số liệu thật của chính cơ sở đó** — không dùng con số trung bình ngành.

---

## Những sai lầm thường gặp

1. **Chọn dung lượng lớn nhưng công suất nhỏ.** Có nhiều kWh mà PCS yếu thì không cắt nổi đỉnh.
2. **Đặt ngưỡng quá thấp.** Tham tiết kiệm dẫn đến phải mua thiết bị lớn, kéo dài thời gian hoàn vốn.
3. **Không đo phụ tải thật.** Thiết kế theo công suất lắp đặt thay vì công suất thực tế thường dẫn tới thừa rất nhiều.
4. **Bỏ qua tổn hao và DoD.** Dung lượng danh định không phải dung lượng dùng được.
5. **Cấu hình EMS sai biểu giá.** Thiết bị tốt nhưng khai báo sai khung giờ thì hiệu quả giảm mạnh.

---

## Nhận biết nhà máy nào phù hợp với peak shaving

Không phải cơ sở nào cũng thu được lợi ích như nhau. Yếu tố quyết định là **hình dạng biểu đồ phụ tải**, chứ không phải quy mô tiêu thụ.

**Rất phù hợp — đỉnh nhọn, ngắn, lặp lại đều đặn.** Nhà máy có vài đợt tải vọt lên trong ngày rồi trở về mức nền. Ví dụ điển hình: xưởng cơ khí có máy ép khởi động theo chu kỳ, cơ sở đúc có lò nung, kho lạnh có máy nén chạy ngắt quãng. Ở đây, chỉ cần một hệ BESS công suất vừa phải cũng cắt được phần đỉnh đắt đỏ.

**Phù hợp vừa — đỉnh rộng, kéo dài vài giờ.** Nhà máy dệt may, chế biến thực phẩm chạy ca liên tục. Cắt đỉnh vẫn có tác dụng nhưng cần **nhiều kWh hơn**, nên bài toán nghiêng về dịch tải hơn là cắt đỉnh thuần tuý.

**Ít phù hợp — tải phẳng gần như không đổi.** Cơ sở chạy 24/7 với mức tải ổn định, chênh lệch giữa cao và thấp không nhiều. Ở đây giá trị của peak shaving thấp; lợi ích chủ yếu đến từ **chênh lệch giá theo giờ** và **dự phòng chống mất điện**.

**Cách tự đánh giá nhanh:** lấy **công suất đỉnh chia cho công suất trung bình**. Tỷ số này càng lớn thì tiềm năng cắt đỉnh càng cao. Nếu đỉnh gấp rưỡi trở lên so với trung bình, rất đáng để phân tích kỹ. Nếu tỷ số gần bằng 1 (tải phẳng), nên cân nhắc mục tiêu khác cho khoản đầu tư.

---

## Đo đạc và kiểm chứng hiệu quả sau khi lắp

Một dự án nghiêm túc không kết thúc ở việc lắp xong thiết bị. Cần có cách **chứng minh hiệu quả bằng số liệu**, vừa để đánh giá đầu tư, vừa để tinh chỉnh vận hành.

**Trước khi lắp — thiết lập mốc so sánh (baseline):**
- Ghi lại **công suất đỉnh hằng tháng** trong ít nhất 6 tháng gần nhất.
- Ghi lại **cơ cấu tiền điện** theo từng khung giờ.
- Lưu **biểu đồ phụ tải** điển hình của ngày làm việc và ngày nghỉ.

**Sau khi lắp — theo dõi các chỉ số:**

| Chỉ số | Cách đo | Kỳ vọng |
|---|---|---|
| Công suất đỉnh ghi nhận | Từ công tơ điện lực | Giảm xuống dưới ngưỡng đặt |
| Sản lượng xả của BESS | Từ EMS | Tương ứng phần đỉnh đã cắt |
| Tiền điện theo khung giờ | Từ hoá đơn | Giảm ở khung cao điểm |
| Số lần vượt ngưỡng | Từ EMS | Tiến về 0 |
| Hiệu suất vòng thực tế | Từ EMS | Ổn định qua các tháng |

**Lưu ý khi so sánh:** cần loại trừ các yếu tố gây nhiễu như **thay đổi sản lượng sản xuất**, **thêm/bớt thiết bị**, hoặc **thay đổi biểu giá điện**. Cách tốt nhất là so sánh **cùng kỳ năm trước** và chuẩn hoá theo sản lượng.

Nếu sau vài tháng kết quả thấp hơn kỳ vọng, nguyên nhân thường nằm ở **cấu hình EMS** (ngưỡng đặt chưa tối ưu, khai báo sai khung giờ) chứ không phải ở thiết bị. Đây là lý do nên dành 1–3 tháng đầu để **tinh chỉnh** thay vì cài một lần rồi để yên. [Tìm hiểu EMS →](/ems-quan-ly-nang-luong-renepoly/)

---

## Cam kết tại HOANTRANTDH

- ✅ **Phân tích hoá đơn và biểu đồ phụ tải miễn phí** trước khi báo giá.
- ✅ Đề xuất cấu hình **kW/kWh tối ưu**, không bán thừa.
- ✅ Phân phối [Renepoly](/renepoly/): tủ, container, PCS, EMS.
- ✅ Hỗ trợ đo đếm để **chứng minh hiệu quả thực tế** sau lắp đặt.

---

<a name="bao-gia"></a>
## Nhận tính toán & báo giá

Gửi: **hoá đơn điện 3–6 tháng · biểu đồ phụ tải (nếu có) · công suất đăng ký · đã có điện mặt trời chưa.**

**→ [Liên hệ tư vấn giải pháp cắt đỉnh phụ tải](/lien-he/)**

---

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-sizing.svg)


## Câu hỏi thường gặp (FAQ)

**Peak shaving tiết kiệm được bao nhiêu?**
Phụ thuộc **hình dạng đỉnh tải**, chênh lệch giá theo khung giờ và mức phí công suất áp dụng. Cần tính trên số liệu thật của từng cơ sở.

**Peak shaving khác load shifting thế nào?**
Peak shaving nhắm vào **công suất cực đại (kW)**; load shifting nhắm vào **chi phí năng lượng (kWh)** bằng cách dịch tiêu thụ sang giờ rẻ.

**Cần thiết bị gì để làm peak shaving?**
Một hệ **BESS** gồm pin + **PCS** + **EMS**, cộng với thiết bị đo công suất để EMS biết khi nào cần xả.

**Có làm peak shaving mà không cần pin không?**
Có thể giảm đỉnh bằng cách **dịch lịch chạy máy** hoặc cắt bớt tải không thiết yếu, nhưng cách này ảnh hưởng sản xuất. BESS cho phép giảm đỉnh **mà không đổi quy trình**.

**Bao lâu thì hoàn vốn?**
Tuỳ mức chênh giá, phí công suất và các giá trị cộng thêm. Nên tính đầy đủ các nguồn hoàn vốn, không chỉ chênh lệch giá điện.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /renepoly/, /tinh-cong-suat-dung-luong-bess/, /bess-cho-nha-may-khu-cong-nghiep/, /ems-quan-ly-nang-luong-renepoly/, /lien-he/. -->
