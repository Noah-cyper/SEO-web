<!--
LOẠI TRANG : Bài xử lý sự cố (chuỗi biến tần — tầng 5) — Thông tin
URL SLUG   : /loi-qua-nhiet-qua-tai-bien-tan/
TỪ KHÓA    : lỗi quá nhiệt biến tần | lỗi quá tải biến tần | biến tần báo oh | biến tần báo ol | biến tần nóng
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 28/30 trong chuỗi biến tần.
-->

TITLE TAG   : Lỗi Quá Nhiệt (OH) Và Quá Tải (OL) Biến Tần – Cách Xử Lý
META (156)  : Biến tần báo OH khi trời nóng hoặc OL khi tải nặng? Nguyên nhân quá nhiệt do quạt, bụi, tủ kín; quá tải do chọn sai công suất và cơ khí. Kèm cách phòng ngừa.

H1          : Lỗi Quá Nhiệt Và Quá Tải Trên Biến Tần

---

## Hai lỗi cùng nói về nhiệt, nhưng nhiệt ở hai nơi khác nhau

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan-loi.svg)


**Quá nhiệt (OH, OH1, OH2)** và **quá tải (OL, OL1, OL2)** thường bị gộp chung, nhưng chúng bảo vệ hai đối tượng khác nhau:

- **Quá nhiệt (OH)** — biến tần đo **nhiệt độ tấm tản nhiệt và IGBT của chính nó**. Đây là bảo vệ cho **biến tần**.
- **Quá tải (OL)** — biến tần tính toán **nhiệt tích lũy trong động cơ** dựa trên dòng và thời gian. Đây là bảo vệ cho **động cơ** (và một biến thể khác bảo vệ cho chính biến tần).

Nhiều dòng máy phân biệt rõ: **OL1 cho động cơ, OL2 cho biến tần**. Đọc đúng ký hiệu giúp khoanh vùng nhanh hơn nhiều.

Điểm chung của cả hai: chúng thường **không xuất hiện đột ngột** mà **tăng dần theo thời gian** — vài tháng, vài mùa. Đó là lý do chúng thường bị coi là "máy chạy lâu nên yếu đi", trong khi nguyên nhân thật thường rất cụ thể và xử lý được.

> **Biến tần nóng bất thường hoặc hay báo OH/OL?** Gửi **mã lỗi · môi trường lắp đặt · ảnh tủ** → [Nhận hỗ trợ chẩn đoán](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-loi.svg)


Đây là bài **28/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: nhiệt sinh ra từ đâu

### Nhiệt trong biến tần

Biến tần có hiệu suất cao, nhưng phần tổn hao vẫn tạo ra một lượng nhiệt đáng kể, tập trung ở:

- **IGBT** — tổn hao khi dẫn và tổn hao khi đóng cắt.
- **Diode chỉnh lưu.**
- **Tụ DC bus** và các phần tử thụ động.

Toàn bộ nhiệt đó được dẫn ra **tấm tản nhiệt (heatsink)** và thổi đi bằng **quạt làm mát**. Chuỗi tản nhiệt này chỉ hoạt động khi ba điều kiện được thỏa mãn:

1. **Quạt còn chạy tốt.**
2. **Khe tản nhiệt không bị bít.**
3. **Không khí xung quanh đủ mát và lưu thông được.**

Chỉ cần một trong ba điều kiện hỏng là nhiệt độ tăng dần cho tới ngưỡng cắt.

Một yếu tố quan trọng ít người để ý: **tần số sóng mang**. Sóng mang càng cao, IGBT đóng cắt càng nhiều lần mỗi giây, **tổn hao đóng cắt càng lớn** và biến tần càng nóng. Nhiều trường hợp quá nhiệt được giải quyết chỉ bằng cách hạ sóng mang xuống — đổi lại động cơ kêu to hơn một chút.

### Derating — công suất giảm theo điều kiện

Thông số công suất ghi trên nhãn biến tần chỉ đúng trong **điều kiện tiêu chuẩn**: nhiệt độ môi trường trong khoảng cho phép, độ cao lắp đặt dưới mức quy định, tần số sóng mang mặc định.

Khi điều kiện xấu hơn, biến tần **phải giảm công suất cho phép (derating)**:

- **Nhiệt độ môi trường cao hơn tiêu chuẩn** → giảm dòng cho phép.
- **Lắp ở độ cao lớn** → không khí loãng, tản nhiệt kém → giảm dòng.
- **Tần số sóng mang cao hơn mặc định** → giảm dòng.
- **Lắp trong tủ kín không thông gió** → nhiệt độ trong tủ cao hơn ngoài trời đáng kể.

Bỏ qua derating là lý do khiến nhiều hệ **chạy tốt vào mùa mát nhưng báo OH liên tục vào mùa nóng** — thiết bị không hỏng, chỉ là đã chọn sát quá so với điều kiện thực tế ([xem cách chọn công suất](/chon-cong-suat-bien-tan/)).

### Nhiệt trong động cơ

Bảo vệ quá tải động cơ (OL) hoạt động theo mô hình nhiệt: biến tần theo dõi **dòng vượt định mức bao nhiêu và trong bao lâu**, tích lũy lại, và cắt khi đạt ngưỡng.

Vì mô hình dựa trên **dòng định mức động cơ đã khai báo**, nên nếu khai sai — hoặc dùng biến tần lớn hơn động cơ nhiều mà không khai đúng — thì bảo vệ này **hoàn toàn mất tác dụng**.

Một đặc thù quan trọng: động cơ tự làm mát bằng **quạt gắn trên trục**. Khi chạy ở tốc độ thấp kéo dài, quạt quay chậm, **khả năng tản nhiệt giảm mạnh** trong khi dòng có thể vẫn cao. Đây là lý do động cơ chạy lâu ở tần số thấp dễ nóng, và là lý do phải đặt tần số nhỏ nhất hợp lý ([xem cài đặt thông số](/cai-dat-thong-so-bien-tan/)).

---

## Cấu tạo chẩn đoán: bảng tra hai lỗi

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-baotri.svg)


### Lỗi quá nhiệt (OH)

| Dấu hiệu | Nguyên nhân | Xử lý |
|---|---|---|
| Chỉ báo lỗi vào **buổi chiều nóng, mùa hè** | Nhiệt độ môi trường vượt điều kiện | Thông gió tủ, quạt hút, điều hòa tủ; xem lại derating |
| **Nặng dần theo tháng** | **Khe tản nhiệt bám bụi** | Vệ sinh khe tản nhiệt bằng khí nén khô |
| Quạt không quay hoặc quay yếu, kêu | **Quạt làm mát hỏng** | Thay quạt — vật tư rẻ, thay được tại chỗ |
| Tủ kín, không có lỗ thoáng | Nhiệt tích trong tủ | Bổ sung quạt hút + lọc gió [xem bố trí tủ](/lap-bien-tan-trong-tu-dien/) |
| Nhiều biến tần xếp sát nhau | Không đủ khoảng cách | Bố trí lại theo khuyến nghị hãng |
| Xuất hiện sau khi ai đó "chỉnh cho êm" | **Tần số sóng mang bị tăng** | Hạ sóng mang về mặc định |
| Lắp ở khu vực nhiều bụi (xưởng gỗ, xi măng) | Bụi bít khe và bám cánh quạt | Lọc gió tủ + lịch vệ sinh định kỳ |
| Lắp trên cao, gần mái tôn | Nhiệt bức xạ | Dời tủ hoặc che chắn, thông gió cưỡng bức |

### Lỗi quá tải (OL)

| Dấu hiệu | Nguyên nhân | Xử lý |
|---|---|---|
| Báo lỗi khi **tải nặng hơn bình thường** | Tải thực vượt thiết kế | Giảm tải, hoặc nâng cấp công suất |
| Báo lỗi **ngày càng thường xuyên** | **Cơ khí xuống cấp** — vòng bi, dây curoa, lệch tâm | Kiểm tra, bảo dưỡng cơ khí |
| Báo lỗi khi chạy **tần số thấp kéo dài** | Động cơ tự làm mát kém | Nâng tần số nhỏ nhất, hoặc lắp **quạt cưỡng bức** cho động cơ |
| Báo lỗi sau khi **đổi động cơ** | Chưa khai lại thông số | Khai lại nhãn động cơ, auto-tune lại |
| Không bao giờ báo OL dù động cơ nóng | **Khai sai dòng định mức** (theo biến tần) | Khai lại theo **nhãn động cơ** |
| Báo lỗi ngay từ khi mới lắp | Chọn thiếu công suất, hoặc sai loại tải | Xem lại tính chọn |
| Dòng ba pha lệch nhau | Mất pha đầu ra, cuộn dây có vấn đề | Đo ampe kìm ba pha, kiểm tra cách điện |
| Chỉ báo khi khởi động, không báo khi chạy | Mô-men khởi động thiếu | Đổi sang vector, kéo dài tăng tốc [xem →](/loi-qua-dong-bien-tan/) |

---

## Ứng dụng: phòng ngừa thay vì chữa cháy

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-suachua.svg)


Cả OH và OL đều thuộc nhóm lỗi **hoàn toàn phòng ngừa được**. Danh sách dưới đây là những việc rẻ và hiệu quả nhất:

**Về nhiệt của biến tần:**

1. **Vệ sinh khe tản nhiệt định kỳ** bằng khí nén khô — công việc mười phút, hiệu quả rất lớn ở môi trường bụi.
2. **Kiểm tra quạt làm mát mỗi kỳ bảo trì.** Nghe tiếng, cảm nhận luồng gió. Quạt là chi tiết cơ khí, chắc chắn sẽ hỏng trước phần điện tử.
3. **Lắp lọc gió cho tủ** và thay lưới lọc theo lịch.
4. **Đo nhiệt độ trong tủ vào ngày nóng nhất** — con số này quan trọng hơn nhiệt độ ngoài trời.
5. **Giữ khoảng cách lắp đặt** theo khuyến nghị hãng, không xếp sát nhau.
6. **Không tăng tần số sóng mang** trừ khi thực sự cần, và biết rằng đánh đổi là nhiệt.
7. **Chọn công suất có tính tới derating** khi lắp ở nơi nóng hoặc tủ kín.

**Về quá tải động cơ:**

1. **Khai đúng dòng định mức động cơ** — điều kiện tiên quyết để bảo vệ hoạt động.
2. **Không chọn biến tần lớn hơn động cơ quá nhiều** mà không khai đúng thông số.
3. **Đặt tần số nhỏ nhất hợp lý**, hoặc lắp **quạt cưỡng bức** nếu buộc phải chạy chậm kéo dài.
4. **Bảo dưỡng cơ khí định kỳ** — vòng bi, độ căng dây curoa, đồng tâm khớp nối.
5. **Theo dõi xu hướng dòng theo thời gian.** Dòng tăng dần ở cùng một chế độ là **dấu hiệu sớm** của hỏng hóc cơ khí, xuất hiện trước khi máy dừng.

Điểm cuối cùng đáng được nhấn mạnh: rất nhiều sự cố dừng máy đột xuất **đã phát tín hiệu từ trước** dưới dạng dòng tăng dần. Chỉ cần ghi lại dòng làm việc mỗi tuần là đủ để phát hiện ([xem lịch bảo trì](/bao-tri-bien-tan-dinh-ky/)).

---

## So sánh hai lỗi

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)


| Tiêu chí | **Quá nhiệt (OH)** | **Quá tải (OL)** |
|---|---|---|
| Bảo vệ ai | **Biến tần** (IGBT, tản nhiệt) | **Động cơ** (OL1) hoặc biến tần (OL2) |
| Đo cái gì | Nhiệt độ tấm tản nhiệt | Dòng tích lũy theo thời gian |
| Nguyên nhân số một | **Quạt hỏng, khe tản nhiệt bám bụi** | **Tải thực vượt thiết kế**, cơ khí xuống cấp |
| Liên quan môi trường | **Rất mạnh** — nhiệt độ, bụi, độ cao | Yếu |
| Liên quan cài đặt | Tần số sóng mang | **Khai báo dòng động cơ** |
| Xuất hiện theo mùa | **Rõ rệt** | Không rõ |
| Giải pháp rẻ nhất | Vệ sinh + thay quạt | Bảo dưỡng cơ khí, khai đúng thông số |
| Phòng ngừa | Lọc gió, thông gió tủ, vệ sinh định kỳ | Theo dõi xu hướng dòng, bảo dưỡng cơ khí |

---

## Sai lầm thường gặp

1. **Bỏ qua vệ sinh khe tản nhiệt** trong môi trường nhiều bụi.
2. **Không kiểm tra quạt làm mát** cho tới khi máy dừng.
3. **Lắp biến tần trong tủ kín** hoàn toàn không thông gió.
4. **Xếp nhiều biến tần sát nhau** để tiết kiệm không gian tủ.
5. **Tăng tần số sóng mang cho động cơ êm** rồi báo OH vào mùa nóng.
6. **Không tính derating** khi lắp ở nơi nóng hoặc trên cao.
7. **Khai dòng động cơ theo nhãn biến tần** — bảo vệ quá tải mất tác dụng hoàn toàn.
8. **Chạy động cơ ở tần số rất thấp kéo dài** mà không có quạt cưỡng bức.
9. **Nâng ngưỡng bảo vệ quá tải** để hết báo lỗi — động cơ có thể cháy.
10. **Bỏ qua xu hướng dòng tăng dần** — mất cơ hội phát hiện sớm hỏng hóc cơ khí.
11. **Mở cửa tủ để cho mát** — bụi và ẩm vào, vấn đề nặng hơn về lâu dài.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **chọn công suất có tính derating** theo môi trường lắp đặt thực tế.
- ✅ Hỗ trợ **phương án thông gió và lọc gió tủ điện** cho môi trường bụi.
- ✅ Cung cấp **quạt làm mát thay thế** và hướng dẫn vệ sinh, bảo dưỡng.
- ✅ Hỗ trợ **rà soát thông số bảo vệ** để đảm bảo động cơ được bảo vệ đúng.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ chẩn đoán & báo giá

Gửi cho chúng tôi: **mã lỗi · model biến tần · nhiệt độ môi trường và trong tủ · ảnh tủ điện và cách bố trí · công suất động cơ và loại tải · tần số làm việc thường xuyên · lỗi xuất hiện theo mùa hay liên tục.**

**→ [Liên hệ hỗ trợ xử lý lỗi OH/OL](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lỗi OH trên biến tần là gì?**
Là lỗi **quá nhiệt tấm tản nhiệt của chính biến tần**. Nguyên nhân phổ biến nhất là **quạt làm mát hỏng** và **khe tản nhiệt bám bụi**.

**Lỗi OL khác OH thế nào?**
**OL là quá tải** — biến tần tính nhiệt tích lũy trong **động cơ** theo dòng và thời gian. **OH là quá nhiệt của bản thân biến tần**.

**Vì sao biến tần chỉ báo lỗi vào mùa nóng?**
Vì thông số công suất chỉ đúng trong **điều kiện nhiệt độ tiêu chuẩn**. Khi môi trường nóng hơn, biến tần phải **giảm công suất cho phép (derating)** — nếu chọn sát quá thì mùa nóng sẽ chạm ngưỡng.

**Có nên tăng tần số sóng mang để động cơ chạy êm không?**
Cân nhắc. Sóng mang cao làm **IGBT nóng hơn** và tăng nhiễu. Nếu đang gặp lỗi OH, hạ sóng mang thường là biện pháp miễn phí hiệu quả.

**Vì sao biến tần không bao giờ báo quá tải dù động cơ rất nóng?**
Gần như chắc chắn do **khai sai dòng định mức động cơ** — thường là khai theo nhãn biến tần thay vì nhãn động cơ.

**Chạy động cơ ở tần số thấp lâu có sao không?**
Có. Quạt làm mát gắn trên trục quay chậm nên **động cơ tản nhiệt kém**. Cần đặt tần số nhỏ nhất hợp lý hoặc lắp **quạt cưỡng bức**.

**Quạt làm mát biến tần có thay được không?**
Có. Đây là **vật tư tiêu hao** giá rẻ, thay được tại chỗ, và nên nằm trong lịch bảo trì định kỳ.

**Làm sao phát hiện sớm quá tải trước khi máy dừng?**
**Ghi lại dòng làm việc theo thời gian**. Dòng tăng dần ở cùng một chế độ vận hành là dấu hiệu sớm của hỏng hóc cơ khí.

<!-- SCHEMA: FAQPage + BreadcrumbList + Article. INTERNAL LINK: /bien-tan-la-gi/, /loi-bien-tan-thuong-gap/, /loi-qua-dong-bien-tan/, /chon-cong-suat-bien-tan/, /cai-dat-thong-so-bien-tan/, /lap-bien-tan-trong-tu-dien/, /bao-tri-bien-tan-dinh-ky/, /lien-he/. -->
