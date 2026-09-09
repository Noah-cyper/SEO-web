<!--
LOẠI TRANG : Bài kỹ thuật nâng cao (chuỗi biến tần — tầng 7) — Thông tin → Thương mại
URL SLUG   : /dong-bo-nhieu-bien-tan/
TỪ KHÓA    : đồng bộ nhiều biến tần | master slave biến tần | chia tải biến tần | điều khiển sức căng | nhiều động cơ một dây chuyền
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 37/50 trong chuỗi biến tần.
-->

TITLE TAG   : Đồng Bộ Nhiều Biến Tần – Master-Slave, Chia Tải Và Sức Căng
META (156)  : Cách cho nhiều biến tần chạy đồng bộ trên một dây chuyền: đồng bộ tốc độ, chia tải cơ khí cứng, điều khiển sức căng. So sánh analog, Modbus và fieldbus.

H1          : Đồng Bộ Nhiều Biến Tần Trên Một Dây Chuyền

---

## Ba bài toán khác nhau hay bị gộp làm một

Khi một dây chuyền có nhiều động cơ, câu hỏi "làm sao cho chúng chạy đồng bộ" thực ra che giấu **ba bài toán kỹ thuật khác nhau**, với ba lời giải khác nhau. Nhầm lẫn giữa chúng là nguyên nhân của rất nhiều hệ chạy không ổn định.

**Bài toán 1 — Đồng bộ tốc độ (speed following).** Các trục **không nối cứng với nhau về cơ khí**, nhưng cần chạy cùng một tốc độ. Ví dụ: nhiều đoạn băng tải nối tiếp, nhiều quạt trong một hệ thông gió. Nếu tốc độ lệch, hàng sẽ dồn ứ hoặc thưa ra.

**Bài toán 2 — Chia tải (load sharing).** Hai hoặc nhiều động cơ **nối cứng vào cùng một tải** — cùng một trục, cùng một hộp số, hoặc cùng một băng tải qua hai tang. Ở đây tốc độ **bắt buộc phải bằng nhau về mặt cơ khí**, nên vấn đề không phải tốc độ mà là **mô-men**: làm sao để hai động cơ gánh tải đều nhau thay vì một cái kéo, một cái bị kéo.

**Bài toán 3 — Điều khiển sức căng (tension control).** Vật liệu dạng cuộn — giấy, màng nhựa, vải, dây kim loại — đi qua nhiều trục. Ở đây các trục **cố tình chạy khác tốc độ**, và cái cần giữ không đổi là **sức căng của vật liệu**.

Ba bài toán này đòi hỏi ba cấu hình khác nhau. Bài này trình bày cả ba, cùng các cách kết nối và những cạm bẫy thực tế.

> **Dây chuyền của bạn cần đồng bộ mấy trục?** Gửi **sơ đồ dây chuyền · số động cơ · yêu cầu đồng bộ** → [Nhận tư vấn cấu hình](#bao-gia).

Đây là bài **37/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: vì sao cùng tần số chưa chắc cùng tốc độ

Một hiểu lầm phổ biến: "cấp cùng một tần số cho hai biến tần thì hai động cơ sẽ chạy cùng tốc độ".

Điều đó **không đúng với động cơ không đồng bộ**. Lý do là **độ trượt (slip)**: tốc độ thực của rotor luôn thấp hơn tốc độ từ trường quay, và **độ chênh lệch đó phụ thuộc vào tải**.

- Động cơ **tải nhẹ** → trượt ít → quay **nhanh hơn**.
- Động cơ **tải nặng** → trượt nhiều → quay **chậm hơn**.

Vậy nên hai động cơ cấp cùng 40 Hz nhưng chịu tải khác nhau sẽ quay ở hai tốc độ khác nhau. Sai lệch tuy nhỏ nhưng **tích lũy theo thời gian**, và với dây chuyền chạy liên tục nhiều giờ, nó đủ để gây dồn ứ hoặc căng đứt vật liệu.

Có ba cách xử lý, theo mức độ chính xác tăng dần:

**Mức 1 — Bù trượt (slip compensation).** Biến tần ước lượng tải và tự tăng nhẹ tần số để bù phần trượt. Đây là chức năng có sẵn trong hầu hết biến tần, chỉ cần bật và cài đúng thông số động cơ. Đủ cho nhiều ứng dụng đơn giản.

**Mức 2 — Chế độ vector.** Vector kiểm soát mô-men trực tiếp nên giữ tốc độ ổn định hơn nhiều khi tải thay đổi ([xem so sánh chế độ](/che-do-dieu-khien-vf-vector/)).

**Mức 3 — Vector có encoder.** Tốc độ được **đo thật** thay vì ước lượng. Đây là mức chính xác cao nhất, cần cho dây chuyền yêu cầu nghiêm ngặt.

### Nguyên lý chia tải: master điều khiển tốc độ, slave theo mô-men

Khi hai động cơ nối cứng vào cùng một tải, **không được để cả hai cùng điều khiển tốc độ**. Lý do rất trực quan: hai bộ điều khiển tốc độ cùng bám vào một trục sẽ "đánh nhau" — cái nào đặt cao hơn một chút sẽ kéo, cái kia bị kéo và chuyển sang chế độ hãm. Kết quả là một động cơ quá tải, một động cơ phát nhiệt, dòng dao động.

Cấu hình đúng là:

- **Master** chạy ở chế độ **điều khiển tốc độ** — nó quyết định trục quay nhanh bao nhiêu.
- **Slave** chạy ở chế độ **điều khiển mô-men** — nó không quan tâm tốc độ, chỉ sinh ra đúng lượng mô-men mà master yêu cầu.
- Master **gửi giá trị mô-men tham chiếu** cho slave, thường bằng tín hiệu analog hoặc qua truyền thông.

Với cấu hình này, hai động cơ gánh tải theo tỷ lệ đặt trước (thường 50/50, nhưng có thể lệch nếu hai động cơ khác công suất).

**Trường hợp không nối cứng** (ví dụ hai băng tải riêng biệt) thì ngược lại: cả hai đều điều khiển tốc độ, chỉ cần nhận cùng một lệnh tốc độ.

---

## Cấu tạo: các cách truyền lệnh giữa các biến tần

| Cách kết nối | Cách hoạt động | Ưu điểm | Hạn chế |
|---|---|---|---|
| **Analog song song** | Một tín hiệu 4–20mA cấp cho tất cả AI | Đơn giản, không lập trình | Không đọc ngược, sai số cộng dồn |
| **Analog nối tiếp (daisy)** | AO của máy trước → AI máy sau | Truyền được mô-men tham chiếu | Sai số tích lũy qua từng khâu |
| **Modbus RTU** | PLC ghi tần số cho từng biến tần | 2 dây, đọc được trạng thái | Chu kỳ cập nhật chậm hơn |
| **Fieldbus Ethernet** | Mạng công nghiệp tốc độ cao | **Nhanh, chính xác, chẩn đoán tốt** | Chi phí cao hơn |
| **Master–slave tích hợp** | Chức năng có sẵn trong hãng | Cài nhanh, tối ưu sẵn | Chỉ dùng được **trong cùng một hãng** |
| **Encoder chia sẻ** | Xung encoder master → card PG slave | Chính xác cao nhất | Cần phần cứng chuyên dụng |

**Về master–slave tích hợp.** Nhiều hãng biến tần có sẵn chức năng này với các thông số chuyên dụng: khai báo máy nào là master, máy nào là slave, tỷ lệ chia tải, độ dốc chia tải (droop). Nếu toàn bộ hệ dùng **cùng một hãng**, đây là cách nhanh và ổn định nhất. Nếu hệ trộn nhiều hãng, phải quay lại analog hoặc truyền thông ([xem bài truyền thông công nghiệp](/bien-tan-mang-truyen-thong-cong-nghiep/)).

**Về độ dốc chia tải (droop).** Đây là một kỹ thuật đơn giản mà hiệu quả cho chia tải: cấu hình biến tần **tự giảm nhẹ tần số khi mô-men tăng**. Động cơ nào đang gánh nhiều hơn sẽ tự chậm lại một chút, nhường bớt tải cho động cơ kia. Hệ tự cân bằng mà không cần truyền thông giữa hai máy.

Droop không chính xác bằng master–slave thật, nhưng rất đáng thử vì **chỉ cần cài một thông số** và không cần thêm dây nối nào.

### Thông số cần thống nhất giữa các biến tần

Đây là danh sách kiểm tra thường bị bỏ sót, và là nguyên nhân của nhiều hệ "đã đấu đúng mà vẫn không đồng bộ":

- **Tần số lớn nhất** phải giống nhau — nếu không, cùng một tín hiệu analog sẽ cho hai tốc độ khác nhau.
- **Thang tín hiệu analog** (0–10V hay 4–20mA, và điểm đầu/cuối thang) phải khớp.
- **Thời gian tăng/giảm tốc** phải giống nhau — nếu lệch, các trục sẽ mất đồng bộ trong lúc thay đổi tốc độ.
- **Chế độ điều khiển** nên giống nhau.
- **Bù trượt** bật ở tất cả, với thông số động cơ khai đúng cho từng máy.
- **Tỷ số truyền cơ khí** (hộp số, đường kính tang) phải được tính vào hệ số tỷ lệ.

Điểm thứ ba đặc biệt hay bị bỏ qua: hai băng tải có thể chạy đúng tốc độ khi ổn định, nhưng **dồn hàng mỗi lần khởi động** chỉ vì thời gian tăng tốc lệch nhau vài giây.

---

## Ứng dụng: ba bài toán và cấu hình tương ứng

### Đồng bộ tốc độ nhiều đoạn băng tải

Cấu hình: tất cả biến tần chạy **điều khiển tốc độ**, nhận cùng một lệnh.

- Nếu yêu cầu không quá nghiêm ngặt: **một tín hiệu analog 4–20mA cấp song song** cho tất cả.
- Nếu cần giám sát và điều chỉnh linh hoạt: **PLC ghi tần số qua Modbus** cho từng máy ([xem điều khiển bằng PLC](/dieu-khien-bien-tan-bang-plc/)).
- **Bật bù trượt** ở tất cả các máy.
- **Thống nhất thời gian tăng/giảm tốc.**
- Có thể đặt hệ số tỷ lệ nhẹ cho từng đoạn (ví dụ đoạn sau nhanh hơn đoạn trước một chút) để **tránh dồn hàng ở điểm chuyển tiếp**.

### Chia tải hai động cơ trên cùng một trục

Cấu hình: **master điều khiển tốc độ, slave điều khiển mô-men**.

- Master gửi mô-men tham chiếu cho slave qua **analog hoặc truyền thông**.
- Đặt **tỷ lệ chia tải** theo công suất từng động cơ.
- Bật **giới hạn mô-men** ở slave để tránh nó kéo quá mức nếu mất tín hiệu.
- Cấu hình xử lý khi **mất tín hiệu tham chiếu** — slave phải dừng an toàn, không được chạy tự do.
- Nếu không có truyền thông, thử **droop** trước — đơn giản hơn nhiều và thường đủ dùng.

**Kiểm chứng bắt buộc:** đo **dòng của cả hai động cơ** ở các mức tải khác nhau. Nếu dòng lệch nhau đáng kể, cấu hình chưa đúng — một động cơ đang gánh nhiều hơn phần của nó.

### Điều khiển sức căng vật liệu cuộn

Đây là bài toán khó nhất trong ba. Đặc thù: **đường kính cuộn thay đổi liên tục** khi vật liệu được cuốn vào hoặc xả ra, nên tốc độ quay phải thay đổi tương ứng để giữ tốc độ dài không đổi.

Ba cách tiếp cận:

**1. Điều khiển theo con lăn nhảy (dancer).** Một con lăn treo trên vật liệu, vị trí của nó phản ánh độ căng. PID điều chỉnh tốc độ để giữ con lăn ở vị trí giữa. Đơn giản và bền, phù hợp nhiều ứng dụng.

**2. Điều khiển theo cảm biến lực căng (load cell).** Đo trực tiếp lực căng, PID điều chỉnh. Chính xác hơn nhưng đắt hơn và nhạy với nhiễu.

**3. Điều khiển mô-men theo đường kính cuộn.** Biến tần tính đường kính hiện tại (từ tỷ số tốc độ giữa hai trục) và điều chỉnh mô-men tương ứng. Không cần cảm biến lực nhưng cần cấu hình kỹ.

Với hệ xả liệu, trục xả thường **luôn ở chế độ hãm** để tạo lực căng ngược — nghĩa là có năng lượng dội về liên tục, cần **điện trở xả** hoặc phương án hoàn năng lượng ([xem bài AFE](/bien-tan-hoan-nang-luong/)).

---

## So sánh: chọn cách kết nối nào

| Yêu cầu | Cách phù hợp |
|---|---|
| Vài băng tải, yêu cầu bình thường | **Analog song song** + bù trượt |
| Cần giám sát và đổi tốc độ linh hoạt | **Modbus RTU từ PLC** |
| Dây chuyền nhiều trục, yêu cầu cao | **Fieldbus Ethernet** |
| Cùng một hãng biến tần | **Master–slave tích hợp** |
| Chia tải đơn giản, ngại đi dây | **Droop** |
| Chia tải chính xác | **Master tốc độ + slave mô-men** |
| Độ chính xác cao nhất | **Vector có encoder + fieldbus** |
| Vật liệu cuộn | **Dancer hoặc load cell + PID** |

Nguyên tắc chọn: **bắt đầu từ phương án đơn giản nhất có thể đáp ứng yêu cầu**. Rất nhiều dây chuyền chạy tốt với analog song song và bù trượt; đầu tư fieldbus và encoder chỉ cần khi độ chính xác thực sự đòi hỏi.

---

## Sai lầm thường gặp

1. **Để cả hai biến tần cùng điều khiển tốc độ** khi hai động cơ nối cứng — chúng "đánh nhau", một cái quá tải.
2. **Nghĩ cùng tần số là cùng tốc độ** — quên độ trượt phụ thuộc tải.
3. **Không bật bù trượt** ở các máy chạy đồng bộ.
4. **Thời gian tăng/giảm tốc khác nhau** giữa các biến tần — mất đồng bộ mỗi lần khởi động.
5. **Tần số lớn nhất khác nhau** — cùng tín hiệu analog cho hai tốc độ khác nhau.
6. **Không tính tỷ số truyền cơ khí** vào hệ số tỷ lệ.
7. **Không kiểm tra dòng từng động cơ** sau khi cấu hình chia tải.
8. **Không cấu hình xử lý khi mất tín hiệu tham chiếu** cho slave.
9. **Dùng analog nối tiếp qua nhiều khâu** — sai số cộng dồn.
10. **Trộn nhiều hãng biến tần** rồi mong dùng được chức năng master–slave tích hợp.
11. **Quên điện trở xả cho trục xả liệu** — trục này hãm liên tục.
12. **Đầu tư fieldbus và encoder** cho ứng dụng mà analog đơn giản đã đủ.

---

## Cam kết tại HOANTRANTDH

- ✅ Phân tích rõ dây chuyền của bạn thuộc **bài toán nào trong ba** trước khi đề xuất cấu hình.
- ✅ Ưu tiên **phương án đơn giản nhất đáp ứng được yêu cầu** — không bán thừa fieldbus và encoder.
- ✅ Hỗ trợ **thống nhất thông số giữa các biến tần** và quy trình kiểm chứng bằng đo dòng.
- ✅ Cung cấp đồng bộ [biến tần](/bien-tan-la-gi/), encoder, card truyền thông và [PLC](/plc-la-gi/).

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **sơ đồ dây chuyền · số động cơ và công suất từng máy · các trục có nối cứng cơ khí với nhau không · yêu cầu độ chính xác đồng bộ · có vật liệu dạng cuộn không · hãng biến tần hiện có · đã có PLC chưa.**

**→ [Liên hệ nhận tư vấn đồng bộ](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cấp cùng một tần số thì hai động cơ có chạy cùng tốc độ không?**
**Không hẳn.** Động cơ không đồng bộ có **độ trượt phụ thuộc tải** — máy tải nặng quay chậm hơn máy tải nhẹ dù cùng tần số. Cần bật **bù trượt** hoặc dùng chế độ vector.

**Hai động cơ nối cùng một trục thì cấu hình thế nào?**
**Master điều khiển tốc độ, slave điều khiển mô-men.** Không được để cả hai cùng điều khiển tốc độ, vì chúng sẽ tranh nhau và một máy sẽ quá tải.

**Droop là gì và khi nào dùng?**
Là cấu hình cho biến tần **tự giảm nhẹ tần số khi mô-men tăng**, giúp hai động cơ tự cân bằng tải. Đơn giản, chỉ cần cài một thông số, không cần dây nối giữa hai máy — nên thử trước khi làm master–slave.

**Vì sao dây chuyền dồn hàng mỗi lần khởi động dù tốc độ chạy đúng?**
Thường do **thời gian tăng/giảm tốc khác nhau** giữa các biến tần. Phải thống nhất thông số này ở tất cả các máy.

**Có bắt buộc dùng encoder để đồng bộ không?**
Không. Nhiều dây chuyền chạy tốt với **bù trượt hoặc chế độ vector**. Encoder chỉ cần khi yêu cầu độ chính xác rất cao.

**Đồng bộ bằng analog hay Modbus tốt hơn?**
**Analog** đơn giản và nhanh, phù hợp vài trục yêu cầu bình thường. **Modbus** cho phép đọc ngược trạng thái và điều chỉnh linh hoạt từ PLC, phù hợp dây chuyền nhiều trục.

**Trộn nhiều hãng biến tần có đồng bộ được không?**
Được, nhưng phải dùng **analog hoặc truyền thông tiêu chuẩn** — chức năng master–slave tích hợp chỉ hoạt động trong cùng một hãng.

**Điều khiển sức căng vật liệu cuộn làm thế nào?**
Ba cách: **con lăn nhảy (dancer) + PID**, **cảm biến lực căng + PID**, hoặc **điều khiển mô-men theo đường kính cuộn**. Trục xả thường hãm liên tục nên cần điện trở xả.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /che-do-dieu-khien-vf-vector/, /dieu-khien-bien-tan-bang-plc/, /bien-tan-mang-truyen-thong-cong-nghiep/, /bien-tan-hoan-nang-luong/, /plc-la-gi/, /lien-he/. -->
