<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 3) — Thông tin
URL SLUG   : /cuon-khang-loc-nhieu-bien-tan/
TỪ KHÓA    : cuộn kháng biến tần | cuộn kháng đầu vào | cuộn kháng đầu ra | lọc dU/dt | lọc sin biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 17/30 trong chuỗi biến tần.
-->

TITLE TAG   : Cuộn Kháng Biến Tần – Đầu Vào, Đầu Ra, Lọc dU/dt Và Lọc Sin
META (155)  : Cuộn kháng biến tần là gì, khi nào cần đầu vào, khi nào cần đầu ra? Phân biệt cuộn kháng, lọc dU/dt, lọc sin, lọc EMC và cách chọn theo chiều dài cáp.

H1          : Cuộn Kháng Biến Tần: Đầu Vào, Đầu Ra Và Các Loại Lọc

---

## Cuộn kháng biến tần là gì và vì sao cần đến nó?

**Cuộn kháng (reactor)** là một cuộn dây quấn trên lõi sắt, mắc nối tiếp trên đường điện của biến tần. Nguyên lý rất đơn giản: cuộn dây **cản trở sự thay đổi đột ngột của dòng điện**. Dòng càng thay đổi nhanh, cuộn kháng cản càng mạnh.

Chính đặc tính đó khiến cuộn kháng trở thành phụ kiện quan trọng của biến tần. Biến tần là thiết bị **tạo ra rất nhiều thay đổi đột ngột**: chỉnh lưu nạp tụ theo từng xung dòng nhọn ở đầu vào, và IGBT đóng cắt hàng nghìn lần mỗi giây ở đầu ra. Cuộn kháng làm mềm những thay đổi đó.

Có hai vị trí lắp, giải quyết hai vấn đề hoàn toàn khác nhau:

- **Cuộn kháng đầu vào (AC line reactor / DC link reactor)** — đặt giữa lưới điện và biến tần. Bảo vệ **biến tần khỏi lưới** và bảo vệ **lưới khỏi biến tần**.
- **Cuộn kháng đầu ra (output reactor)** — đặt giữa biến tần và động cơ. Bảo vệ **động cơ và cáp** khỏi xung áp dốc của biến tần.

Rất nhiều sự cố "không hiểu tại sao" trong tủ biến tần — cầu chì đứt lặp lại, tụ DC bus phồng sớm, động cơ cháy cách điện sau vài tháng, cảm biến nhiễu — có gốc rễ ở việc thiếu cuộn kháng đúng chỗ.

> **Không chắc hệ của bạn có cần cuộn kháng?** Gửi **model biến tần · công suất · chiều dài cáp động cơ · tình trạng lưới** → [Nhận tư vấn](#bao-gia).

Đây là bài **17/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: biến tần làm gì với dòng điện?

Để hiểu vì sao cần cuộn kháng, phải nhìn vào hai đầu của biến tần.

### Ở đầu vào: dòng không hình sin

Khối chỉnh lưu của biến tần chỉ dẫn dòng khi **điện áp lưới cao hơn điện áp trên tụ DC bus**. Nghĩa là trong mỗi nửa chu kỳ, dòng không chảy đều mà chỉ chảy trong một khoảng rất ngắn ở đỉnh — dưới dạng một **xung dòng nhọn và cao**.

Hệ quả:

- **Dòng đỉnh lớn hơn nhiều so với dòng hiệu dụng** — gây ứng suất cho diode chỉnh lưu, tụ và cầu chì.
- **Sóng hài bậc lẻ (5, 7, 11, 13…)** bơm ngược lên lưới, làm méo dạng sóng điện áp, gây nóng máy biến áp và tụ bù.
- **Nhạy với xung áp từ lưới** — sét lan truyền, đóng cắt tụ bù, khởi động tải lớn gần đó đều có thể gây quá áp DC bus.

### Ở đầu ra: xung áp dốc và hiện tượng phản xạ sóng

Biến tần không cấp cho động cơ một điện áp hình sin. Nó cấp một **chuỗi xung vuông** với biên độ bằng điện áp DC bus, độ rộng thay đổi theo quy luật PWM. Sườn của mỗi xung rất dốc — điện áp tăng hàng trăm volt trong thời gian cực ngắn ([xem nguyên lý PWM](/nguyen-ly-hoat-dong-bien-tan/)).

Khi những xung dốc đó chạy trên một sợi cáp dài, xuất hiện **hiện tượng phản xạ sóng (reflected wave)**: xung đi đến đầu động cơ, gặp trở kháng không khớp, dội ngược lại và cộng với xung tới. Kết quả là **điện áp tại đầu cực động cơ có thể vọt lên gần gấp đôi** điện áp DC bus.

Cách điện của động cơ chịu ứng suất đó liên tục, hàng nghìn lần mỗi giây. Với động cơ tiêu chuẩn cũ, không được thiết kế cho biến tần, cách điện suy giảm dần và **cháy cuộn dây sau vài tháng đến vài năm** — thường bị chẩn đoán nhầm là "động cơ kém chất lượng".

Ngoài ra, cáp động cơ dài mang xung dốc còn hoạt động như **ăng-ten phát nhiễu** ([xem bài chống nhiễu EMC](/chong-nhieu-emc-cho-bien-tan/)) và làm tăng **dòng rò cao tần** qua điện dung ký sinh, khiến RCCB nhảy vô cớ.

---

## Cấu tạo và thông số: đọc nhãn cuộn kháng như thế nào

Cuộn kháng ba pha gồm **lõi sắt từ** ghép từ các lá thép kỹ thuật điện, **ba cuộn dây** quấn trên ba trụ, đầu ra bằng các cực bắt vít, tất cả đặt trong khung kim loại có lỗ bắt vào tấm nền tủ.

Các thông số cần đọc khi chọn mua:

| Thông số | Ý nghĩa | Lưu ý khi chọn |
|---|---|---|
| **Dòng định mức (A)** | Dòng làm việc liên tục | Phải **≥ dòng định mức biến tần**, không phải dòng động cơ |
| **Điện cảm (mH)** | Giá trị cản dòng biến thiên | Quyết định độ sụt áp và hiệu quả |
| **% sụt áp (impedance)** | Thường 2% · 3% · 4% | Đầu vào phổ biến **3–4%**; đầu ra thường **1–2%** |
| **Điện áp làm việc** | 220V / 380–480V | Khớp với cấp điện áp hệ thống |
| **Tần số** | 50/60Hz (đầu vào); cao hơn (đầu ra) | Cuộn kháng đầu ra phải chịu được tần số sóng mang |
| **Cấp cách điện / nhiệt độ** | H, F… | Cuộn kháng nóng khi làm việc — cần chỗ thoáng |
| **Kiểu lắp** | Đứng / nằm | Ảnh hưởng bố trí trong tủ |

**Hai lỗi chọn sai phổ biến nhất:**

1. **Chọn theo công suất động cơ thay vì dòng biến tần.** Nếu biến tần được chọn dư (thường gặp khi [chọn công suất biến tần](/chon-cong-suat-bien-tan/) có dự phòng), cuộn kháng phải theo biến tần.
2. **Dùng cuộn kháng đầu vào lắp ở đầu ra.** Cuộn kháng đầu vào chỉ thiết kế cho 50/60Hz. Đặt nó ở đầu ra, nơi có tần số sóng mang hàng kilohertz, lõi sẽ **nóng bất thường và có thể cháy**. Hai loại **không thay thế cho nhau**.

### Bốn thiết bị hay bị gọi nhầm là "cuộn kháng"

- **Cuộn kháng đầu vào (AC reactor)** — cuộn dây nối tiếp phía lưới.
- **Cuộn kháng DC (DC link choke)** — lắp trên mạch một chiều, nhiều biến tần công suất lớn đã tích hợp sẵn; hiệu quả giảm sóng hài tương đương nhưng không chống được xung áp từ lưới tốt bằng AC reactor.
- **Lọc dU/dt** — cuộn kháng kết hợp thêm mạch RC, làm **giảm độ dốc sườn xung** mạnh hơn cuộn kháng đầu ra thông thường.
- **Lọc sin (sine wave filter)** — mạch LC, biến đầu ra PWM thành **điện áp gần hình sin thật sự**. Đắt nhất, hiệu quả nhất, nhưng làm giảm điện áp đầu ra và không dùng được ở mọi chế độ điều khiển.

---

## Ứng dụng: khi nào thực sự cần lắp?

### Cần cuộn kháng đầu vào khi

- **Lưới điện yếu, dao động, hay có xung** — khu công nghiệp cũ, cuối đường dây, gần trạm hàn.
- **Có tụ bù đóng cắt** trong xưởng. Mỗi lần tụ bù đóng tạo một xung áp; đây là nguyên nhân rất phổ biến gây hỏng biến tần mà chủ đầu tư không biết.
- **Nhiều biến tần chung một máy biến áp** — sóng hài cộng dồn.
- **Máy biến áp nguồn có công suất rất lớn** so với biến tần (trở kháng nguồn thấp → dòng xung nạp tụ rất cao).
- **Cầu chì đầu vào đứt lặp lại**, diode chỉnh lưu hỏng nhiều lần.
- **Biến tần báo lỗi quá áp DC bus** không rõ nguyên nhân ([xem bài lỗi quá áp](/loi-qua-ap-thap-ap-bien-tan/)).
- Có yêu cầu **giới hạn sóng hài (THD)** theo hợp đồng đấu nối hoặc tiêu chuẩn nội bộ.

### Cần cuộn kháng đầu ra / lọc dU/dt khi

- **Cáp động cơ dài.** Đây là tiêu chí quan trọng nhất. Cáp càng dài, phản xạ sóng càng nghiêm trọng và dòng rò càng lớn.
- **Động cơ cũ, không phải loại inverter-duty**, cách điện không được thiết kế cho xung PWM.
- **Một biến tần kéo nhiều động cơ song song** — tổng chiều dài cáp cộng dồn, và không có bảo vệ nhiệt riêng từng động cơ.
- **Động cơ đặt ở môi trường ẩm, bụi, hóa chất** — cách điện đã yếu sẵn.
- **RCCB nhảy liên tục** dù không có chạm chập thật.
- **Nhiễu bức xạ mạnh** ảnh hưởng thiết bị xung quanh.
- **Động cơ kêu rít, nóng bất thường** dù tải không nặng.

### Cần lọc sin khi

- Cáp động cơ **rất dài** (bơm chìm giếng sâu, băng tải dài, quạt trên mái nhà xưởng lớn).
- Động cơ **không thể thay thế** và có giá trị cao (động cơ đặc chủng, động cơ phòng nổ).
- Yêu cầu **động cơ chạy êm tuyệt đối** — ứng dụng gần khu dân cư, phòng thí nghiệm.
- Có **máy biến áp cách ly** ở đầu ra biến tần.

### Trường hợp thường KHÔNG cần

- Cáp động cơ **ngắn**, chạy trong cùng tủ hoặc gần tủ.
- Động cơ **mới, loại inverter-duty**.
- Lưới điện **ổn định**, không có tụ bù đóng cắt.
- Biến tần công suất nhỏ, ứng dụng đơn giản như [bơm nước](/bien-tan-cho-bom-nuoc/) đặt sát tủ.

Nói cách khác: cuộn kháng không phải phụ kiện bắt buộc trong mọi trường hợp, nhưng khi cần mà không có thì cái giá phải trả là **hỏng động cơ hoặc hỏng biến tần** — đắt hơn nhiều lần giá cuộn kháng.

---

## So sánh các loại lọc: chọn cái nào?

| Tiêu chí | **Cuộn kháng đầu vào** | **Cuộn kháng đầu ra** | **Lọc dU/dt** | **Lọc sin** | **Lọc EMC** |
|---|---|---|---|---|---|
| Vị trí | Lưới → biến tần | Biến tần → động cơ | Biến tần → động cơ | Biến tần → động cơ | Lưới → biến tần |
| Giải quyết | Sóng hài, xung áp lưới, dòng đỉnh | Phản xạ sóng, dòng rò, nhiễu | Độ dốc sườn xung | Toàn bộ méo dạng đầu ra | Nhiễu dẫn EMC |
| Bảo vệ | Biến tần & lưới | Động cơ & cáp | Cách điện động cơ | Động cơ, cáp, môi trường | Thiết bị dùng chung nguồn |
| Chiều dài cáp phù hợp | Không liên quan | Trung bình | Dài | Rất dài | Không liên quan |
| Chi phí tương đối | Thấp | Thấp | Trung bình | **Cao nhất** | Trung bình |
| Sụt áp gây ra | Nhỏ (2–4%) | Nhỏ | Trung bình | **Đáng kể** | Không đáng kể |
| Hạn chế | Sụt áp nhẹ | Không xử lý triệt để cáp rất dài | Không tạo sóng sin | Hạn chế với vector/servo | Có thể **tăng dòng rò** |

**Nguyên tắc chọn theo thứ tự chi phí tăng dần:** cuộn kháng đầu ra → lọc dU/dt → lọc sin. Chỉ leo lên bậc cao hơn khi bậc dưới không đủ, hoặc khi giá trị động cơ đủ lớn để không được phép thử sai.

Cần lưu ý: **lọc EMC và cuộn kháng không thay thế nhau.** Lọc EMC chặn nhiễu dẫn quay về lưới; cuộn kháng đầu ra xử lý vấn đề trên đường tới động cơ. Một hệ thống khó tính có thể cần cả hai.

---

## Lắp đặt đúng cách

Mua đúng thiết bị mà lắp sai thì hiệu quả giảm rất nhiều:

1. **Đặt cuộn kháng càng gần biến tần càng tốt.** Dây nối dài làm giảm tác dụng và tự nó trở thành nguồn nhiễu.
2. **Chừa khoảng thoáng.** Cuộn kháng sinh nhiệt đáng kể. Không kẹp sát vào biến tần hay chèn giữa các thiết bị khác; tuân thủ khoảng cách tối thiểu của nhà sản xuất ([xem bố trí tủ](/lap-bien-tan-trong-tu-dien/)).
3. **Đặt ở vị trí thấp và thoáng trong tủ**, tránh nằm ngay dưới các thiết bị nhạy nhiệt.
4. **Bắt chắc vào tấm nền kim loại**, tiếp đất khung cuộn kháng.
5. **Siết đúng lực các cực đấu.** Cực lỏng phát nhiệt, oxy hóa, dẫn đến sự cố sau vài tháng.
6. **Kiểm tra tiết diện cáp** — dòng qua cuộn kháng bằng dòng biến tần ([xem chọn cáp và aptomat](/chon-cap-aptomat-cho-bien-tan/)).
7. **Ghi nhãn rõ ràng** đầu vào và đầu ra, tránh người sau đấu ngược.
8. **Sau khi lắp cuộn kháng đầu ra, kiểm tra lại thông số biến tần** — một số dòng cần khai báo hoặc cần chạy lại auto-tune ([xem cài đặt thông số](/cai-dat-thong-so-bien-tan/)).

---

## Sai lầm thường gặp

1. **Lấy cuộn kháng đầu vào lắp ra đầu ra** — nóng, cháy, hỏng cả cuộn kháng lẫn biến tần.
2. **Chọn dòng theo động cơ thay vì theo biến tần.**
3. **Bỏ qua cuộn kháng đầu ra khi cáp rất dài** rồi đổ lỗi cho chất lượng động cơ khi nó cháy.
4. **Đặt cuộn kháng xa biến tần** vì tủ chật.
5. **Nhét cuộn kháng vào góc kín** không có đối lưu không khí.
6. **Mua lọc sin cho mọi trường hợp** — tốn tiền không cần thiết, và có thể xung đột với chế độ điều khiển vector.
7. **Lắp lọc sin nhưng vẫn để tần số sóng mang thấp** — lọc sin thường yêu cầu sóng mang tối thiểu theo khuyến nghị hãng.
8. **Không xét lại sụt áp** sau khi lắp lọc sin, khiến động cơ thiếu mô-men ở tốc độ định mức.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **có thực sự cần cuộn kháng hay không** dựa trên chiều dài cáp, tình trạng lưới và loại động cơ — không bán thừa.
- ✅ Chọn đúng **dòng định mức và % trở kháng** theo biến tần thực tế.
- ✅ Hỗ trợ **bố trí trong tủ** đảm bảo tản nhiệt và giảm nhiễu.
- ✅ Cung cấp đồng bộ [biến tần](/bien-tan-la-gi/), cuộn kháng, lọc EMC và phụ kiện tủ điện.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá cuộn kháng

Gửi cho chúng tôi: **model và công suất biến tần · dòng định mức · chiều dài cáp động cơ · loại động cơ (mới/cũ, inverter-duty hay không) · tình trạng lưới (có tụ bù đóng cắt không) · vấn đề đang gặp.**

**→ [Liên hệ nhận tư vấn cuộn kháng](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cuộn kháng biến tần là gì?**
Là cuộn dây mắc nối tiếp trên đường điện của biến tần, có tác dụng **cản trở sự thay đổi đột ngột của dòng điện**, qua đó giảm sóng hài, giảm xung áp và giảm nhiễu.

**Khi nào cần cuộn kháng đầu vào?**
Khi lưới yếu hoặc hay có xung, **có tụ bù đóng cắt**, nhiều biến tần chung một máy biến áp, cầu chì đầu vào hay đứt, hoặc biến tần hay báo lỗi quá áp DC bus.

**Khi nào cần cuộn kháng đầu ra?**
Chủ yếu khi **cáp động cơ dài**, động cơ cũ không phải loại inverter-duty, một biến tần kéo nhiều động cơ, hoặc RCCB nhảy do dòng rò cao tần.

**Cuộn kháng đầu vào và đầu ra có dùng thay nhau được không?**
**Không.** Cuộn kháng đầu vào chỉ thiết kế cho tần số lưới 50/60Hz; lắp ở đầu ra nơi có tần số sóng mang cao sẽ khiến nó nóng bất thường và có thể cháy.

**Lọc dU/dt khác lọc sin thế nào?**
Lọc dU/dt chỉ **làm mềm sườn xung**, đầu ra vẫn là dạng xung. Lọc sin biến đầu ra thành **điện áp gần hình sin thật**, hiệu quả cao hơn nhưng đắt hơn và gây sụt áp đáng kể.

**Chọn dòng cuộn kháng theo động cơ hay theo biến tần?**
Theo **dòng định mức của biến tần**, vì dòng thực tế chạy qua cuộn kháng do biến tần quyết định.

**Có cuộn kháng rồi có cần lọc EMC nữa không?**
Có thể vẫn cần. Hai thiết bị giải quyết hai vấn đề khác nhau: cuộn kháng đầu ra xử lý phía động cơ, **lọc EMC chặn nhiễu dẫn quay về lưới**.

**Lắp cuộn kháng có làm giảm hiệu suất không?**
Có sụt áp nhỏ (thường 2–4% với cuộn kháng đầu vào) và tổn hao nhiệt nhất định, nhưng **đổi lại là tuổi thọ biến tần và động cơ tăng lên đáng kể**.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /nguyen-ly-hoat-dong-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /lap-bien-tan-trong-tu-dien/, /chon-cap-aptomat-cho-bien-tan/, /chon-cong-suat-bien-tan/, /cai-dat-thong-so-bien-tan/, /loi-qua-ap-thap-ap-bien-tan/, /bien-tan-cho-bom-nuoc/, /lien-he/. -->
