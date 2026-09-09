<!--
LOẠI TRANG : Bài kỹ thuật nâng cao (chuỗi biến tần — tầng 7) — Thông tin → Thương mại
URL SLUG   : /safe-torque-off-bien-tan/
TỪ KHÓA    : safe torque off | sto biến tần | an toàn chức năng biến tần | dừng khẩn cấp biến tần | sto và loto
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 39/50 trong chuỗi biến tần.
-->

TITLE TAG   : Safe Torque Off (STO) Trên Biến Tần – Nguyên Lý Và Cách Dùng Đúng
META (156)  : STO là gì, khác gì với dừng thường và với khoá điện LOTO? Nguyên lý cắt xung IGBT, cách đấu nối, các sai lầm nguy hiểm và khi nào STO không đủ an toàn.

H1          : Safe Torque Off (STO) Trên Biến Tần

---

## Dừng máy và dừng an toàn không phải một

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-tu-dien-bien-tan.svg)


Khi ai đó bấm nút dừng khẩn trên một máy có biến tần, điều gì thực sự xảy ra?

Với cách đấu thông thường, tín hiệu dừng đi vào **chân điều khiển của biến tần**. Biến tần đọc tín hiệu, phần mềm xử lý, rồi ra lệnh cắt đầu ra. Máy dừng.

Vấn đề nằm ở chỗ: **toàn bộ chuỗi đó đi qua phần mềm và vi xử lý**. Nếu vi xử lý treo, nếu phần mềm lỗi, nếu một linh kiện trên đường tín hiệu hỏng — lệnh dừng có thể không được thực thi. Máy vẫn quay trong khi người vận hành tin rằng nó đã dừng.

Với một máy có thể gây thương tích, đó là mức độ tin cậy không chấp nhận được.

**Safe Torque Off (STO)** là chức năng giải quyết đúng vấn đề này. Nó **cắt trực tiếp tín hiệu kích IGBT bằng phần cứng**, không thông qua vi xử lý. Không có xung kích thì IGBT không dẫn; không dẫn thì không có điện ra động cơ; không có điện thì **động cơ không thể sinh mô-men**.

Đây là ý nghĩa của cái tên: **"cắt mô-men an toàn"** — đảm bảo bằng phần cứng rằng động cơ không sinh ra lực xoắn.

> **Máy của bạn có cần chức năng STO?** Gửi **loại máy · yêu cầu an toàn · model biến tần** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-sto.svg)


Đây là bài **39/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: cắt ở đâu và vì sao đáng tin cậy

Nhớ lại cấu trúc biến tần: khối nghịch lưu gồm các **IGBT** đóng cắt theo lệnh từ **mạch driver**, mà mạch driver nhận lệnh từ **vi xử lý** ([xem cấu tạo biến tần](/cau-tao-bien-tan/)).

Chuỗi điều khiển bình thường:

**Vi xử lý → Mạch driver → IGBT → Động cơ**

STO chèn một **cổng phần cứng** vào giữa mạch driver và IGBT (hoặc cắt nguồn cấp cho mạch driver). Khi tín hiệu STO được kích hoạt, cổng này **chặn xung kích lại**, bất kể vi xử lý đang ra lệnh gì.

Ba đặc điểm khiến STO đáng tin cậy hơn dừng thường:

**1. Không phụ thuộc phần mềm.** Vi xử lý có treo, có chạy sai, có bị nhiễu — xung kích vẫn bị chặn.

**2. Hai kênh độc lập.** Hầu hết biến tần có **hai đầu vào STO riêng biệt**, mỗi kênh cắt được một cách độc lập. Muốn động cơ chạy được thì cả hai kênh đều phải cho phép. Một kênh hỏng thì kênh kia vẫn đảm bảo an toàn.

**3. Giám sát chéo.** Biến tần theo dõi trạng thái hai kênh. Nếu chúng **không khớp nhau** — một kênh báo cho phép, kênh kia báo cấm — biến tần hiểu là có lỗi trong mạch an toàn và báo lỗi thay vì cho chạy tiếp.

### Ba điều STO KHÔNG làm

Đây là phần quan trọng nhất của bài, vì hiểu sai ở đây dẫn tới tai nạn thật:

**1. STO không dừng ngay lập tức.** Nó chỉ **cắt mô-men**. Động cơ và tải sau đó **chạy trớn tự do** cho tới khi ma sát làm chúng dừng. Với một khối quay có quán tính lớn, quá trình đó có thể kéo dài. Nếu ứng dụng cần dừng **nhanh**, STO một mình không đủ — cần kết hợp với phanh cơ hoặc dùng chức năng dừng an toàn cấp cao hơn.

**2. STO không giữ tải nâng hạ.** Cắt mô-men trên một cầu trục đang giữ tải nghĩa là **tải rơi tự do**. Với ứng dụng nâng hạ, STO **phải luôn đi kèm phanh cơ** đóng đồng thời ([xem bài cầu trục](/bien-tan-cho-cau-truc-palang/)).

**3. STO không cách ly nguồn điện.** Đây là điểm nguy hiểm nhất khi hiểu sai. Khi STO đang kích hoạt:

- **Nguồn ba pha vẫn vào biến tần.**
- **Tụ DC bus vẫn tích điện ở mức nguy hiểm.**
- **Các cực đấu động lực vẫn có điện.**
- Với động cơ nam châm vĩnh cửu, **cực động cơ vẫn có back-EMF nếu trục còn quay** ([xem bài động cơ PM](/bien-tan-cho-dong-co-nam-cham-vinh-cuu/)).

Nghĩa là: **STO tuyệt đối không thay thế cho khoá điện (LOTO) khi bảo trì.** Ai mở tủ sửa chữa dựa vào việc "đã bấm STO rồi" là đang đối mặt với nguy cơ điện giật thật sự.

---

## Cấu tạo và thông số: những gì cần biết khi chọn và đấu

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-sto.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-loto-sto.svg)

| Hạng mục | Nội dung | Ghi chú |
|---|---|---|
| **Số kênh STO** | Thường **2 kênh độc lập** | Cả hai phải cho phép thì mới chạy |
| **Kiểu tín hiệu** | Thường 24VDC | Có điện = cho phép chạy |
| **Logic an toàn** | **Mất tín hiệu = kích hoạt STO** | Đứt dây cũng dẫn tới trạng thái an toàn |
| **Thời gian phản hồi** | Tính bằng mili-giây | Tra tài liệu của model |
| **Giám sát chéo hai kênh** | Có/không, thời gian cho phép lệch | Lệch quá lâu → báo lỗi |
| **Cách reset** | Thủ công hoặc tự động | **Nên chọn thủ công** |
| **Phản hồi trạng thái** | Đầu ra báo STO đang kích hoạt | Đưa về PLC/HMI để giám sát |
| **Hồ sơ chứng nhận** | Đi kèm thiết bị | Cần cho hồ sơ an toàn của máy |

**Về logic "mất tín hiệu = an toàn".** Đây là nguyên tắc thiết kế quan trọng và cần được giữ đúng khi đấu nối: **có điện 24V nghĩa là cho phép chạy, mất điện nghĩa là cấm**. Nhờ vậy, mọi sự cố trên đường dây — đứt dây, tuột giắc, hỏng tiếp điểm — đều đưa hệ về trạng thái an toàn, chứ không phải trạng thái chạy.

Đấu ngược logic này (có điện = cấm) là một sai lầm nghiêm trọng, vì khi đó **đứt dây sẽ khiến máy chạy được** trong khi mạch an toàn tưởng đang bảo vệ.

**Về reset thủ công.** Sau khi tình huống nguy hiểm được giải quyết và STO được nhả, câu hỏi là: máy có tự khởi động lại không?

Với hầu hết ứng dụng, câu trả lời phải là **không**. Máy tự chạy lại ngay khi ai đó xoay nút dừng khẩn về vị trí cũ là tình huống nguy hiểm — có thể vẫn còn người đang ở trong vùng máy. **Reset thủ công** (phải bấm một nút riêng để cho phép chạy lại) là cấu hình đúng cho đa số trường hợp.

**Về nguồn tín hiệu STO.** Hai kênh STO thường được điều khiển từ một **rơ-le an toàn** hoặc **bộ điều khiển an toàn**, chứ không đấu thẳng từ nút dừng khẩn. Thiết bị này đảm nhận việc giám sát, chống dính tiếp điểm và quản lý reset.

---

## Ứng dụng: khi nào STO đáng giá

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-cautruc.svg)


**Máy có cửa che chắn hoặc rào bảo vệ.** Khi cửa mở, máy phải không thể sinh mô-men. STO phối hợp với công tắc an toàn cửa là cấu hình kinh điển.

**Máy cần người thao tác gần vùng chuyển động.** Nạp liệu, lấy sản phẩm, điều chỉnh — mỗi lần vào vùng máy cần đảm bảo chắc chắn.

**Máy có chu kỳ dừng thường xuyên.** Đây là nơi STO thể hiện lợi ích thực dụng nhất, và đáng nói riêng — xem phần dưới.

**Cầu trục, palăng, thang nâng.** Luôn kèm phanh cơ.

**Robot và máy tự động** làm việc chung không gian với người.

**Dây chuyền có nhiều điểm dừng khẩn.** STO cho phép tích hợp gọn gàng vào mạch an toàn chung.

### Lợi ích thực dụng: bớt được contactor

Trước khi có STO, cách đảm bảo an toàn cho máy có biến tần là lắp một **contactor giữa biến tần và động cơ**, cắt vật lý đường điện khi cần an toàn.

Cách này hoạt động, nhưng có ba nhược điểm:

- **Contactor là chi tiết cơ khí** — tiếp điểm mòn, dính, cần thay theo tuổi thọ đóng cắt.
- **Đóng cắt dưới tải** làm hại cả contactor lẫn biến tần.
- **Chiếm không gian tủ** và cần thêm dây, thêm bảo vệ.

Với máy có chu kỳ dừng thường xuyên — dừng vài chục lần mỗi ca — contactor mòn rất nhanh. STO thay thế bằng một chức năng điện tử **không có bộ phận chuyển động, không mòn**, phản hồi nhanh hơn và không chiếm chỗ.

Đây là lý do thực dụng khiến STO ngày càng phổ biến, bên cạnh lý do an toàn thuần túy.

### Quy trình kiểm tra khi đưa vào vận hành

STO là chức năng an toàn, nên **phải được kiểm chứng bằng thử nghiệm thực tế**, không được tin vào cấu hình trên giấy:

1. **Cho máy chạy ở tốc độ làm việc.**
2. **Kích hoạt STO** (bấm dừng khẩn, mở cửa che chắn).
3. **Xác nhận động cơ mất mô-men ngay** — trục chuyển sang chạy trớn.
4. **Xác nhận máy không tự chạy lại** khi nhả STO.
5. **Thử reset thủ công** — máy chỉ chạy khi bấm nút cho phép.
6. **Thử từng kênh riêng biệt** — ngắt một kênh, xác nhận biến tần vẫn vào trạng thái an toàn và báo lỗi lệch kênh.
7. **Thử đứt dây** — rút một dây tín hiệu, xác nhận hệ vào trạng thái an toàn.
8. **Đo thời gian chạy trớn** của tải sau khi STO kích hoạt — con số này quyết định vùng an toàn và thời gian trễ mở cửa.
9. **Ghi lại toàn bộ kết quả** vào hồ sơ nghiệm thu ([xem bài nghiệm thu](/nghiem-thu-chay-thu-bien-tan/)).

Bước 8 hay bị bỏ qua nhưng rất quan trọng: nếu tải chạy trớn lâu, cửa che chắn **không được mở ngay** khi STO kích hoạt mà phải có khoá giữ cho tới khi máy thực sự dừng.

STO cũng nên được **kiểm tra định kỳ**, cùng lịch bảo trì chung ([xem bài bảo trì](/bao-tri-bien-tan-dinh-ky/)).

---

## So sánh: STO, dừng thường và LOTO

| Tiêu chí | **Dừng thường (qua chân DI)** | **STO** | **Khoá điện LOTO** |
|---|---|---|---|
| Đường tác động | Qua phần mềm | **Phần cứng, cắt xung IGBT** | Cắt nguồn vật lý |
| Phụ thuộc vi xử lý | **Có** | Không | Không |
| Số kênh | 1 | **2, giám sát chéo** | — |
| Cách ly nguồn | Không | **Không** | **Có** |
| Tụ DC bus | Còn điện | **Còn điện** | Xả sau khi chờ |
| Dùng khi vận hành | Có | **Có** | Chậm, bất tiện |
| Dùng khi bảo trì | **Không đủ** | **Không đủ** | **Bắt buộc** |
| Tốc độ tác động | Chậm hơn | **Nhanh** | Chậm |
| Có bộ phận mòn | Không | **Không** | Có |

**Nguyên tắc ghi nhớ:** STO là công cụ **an toàn khi vận hành**; LOTO là quy trình **an toàn khi bảo trì**. Chúng không thay thế nhau và không loại trừ nhau — một máy đầy đủ cần cả hai ([xem bài an toàn điện](/an-toan-dien-voi-bien-tan/)).

---

## Sai lầm thường gặp

1. **Coi STO là đã cách ly nguồn** rồi mở tủ sửa chữa — nguy cơ điện giật thật sự.
2. **Dùng STO một mình cho ứng dụng nâng hạ** — cắt mô-men làm tải rơi tự do.
3. **Kỳ vọng STO dừng máy ngay** — nó chỉ cắt mô-men, tải vẫn chạy trớn.
4. **Đấu ngược logic** — có điện thành cấm chạy, khiến đứt dây lại cho máy chạy.
5. **Chỉ đấu một kênh** rồi nối tắt kênh còn lại cho "đỡ rắc rối".
6. **Nối tắt STO để chạy thử** rồi quên tháo ra.
7. **Đặt reset tự động** cho máy có người thao tác gần vùng chuyển động.
8. **Không thử nghiệm thực tế** sau khi đấu nối, chỉ tin vào cấu hình.
9. **Không đo thời gian chạy trớn** — mở cửa che chắn khi máy còn quay.
10. **Không kiểm tra STO định kỳ** — chức năng an toàn cũng có thể hỏng âm thầm.
11. **Không đưa phản hồi trạng thái STO về PLC/HMI** — không biết hệ đang ở trạng thái nào.
12. **Đấu thẳng nút dừng khẩn vào STO** mà không qua rơ-le an toàn.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **biến tần có sẵn chức năng STO** phù hợp yêu cầu máy của bạn.
- ✅ Hỗ trợ **sơ đồ đấu nối hai kênh đúng logic an toàn** và chọn rơ-le an toàn phù hợp.
- ✅ Cung cấp **quy trình kiểm tra nghiệm thu STO** để đưa vào hồ sơ máy.
- ✅ Nói rõ **giới hạn của STO** — không thay thế LOTO, không giữ được tải nâng hạ.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá

Gửi cho chúng tôi: **loại máy và mức độ nguy hiểm · có cửa che chắn hay rào bảo vệ không · số lần dừng mỗi ca · máy có tải nâng hạ không · quán tính tải (thời gian chạy trớn) · model biến tần hiện có · yêu cầu an toàn của nhà máy.**

**→ [Liên hệ nhận tư vấn an toàn máy](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Safe Torque Off (STO) là gì?**
Là chức năng **cắt tín hiệu kích IGBT bằng phần cứng**, không qua vi xử lý, đảm bảo động cơ **không thể sinh mô-men** kể cả khi phần mềm biến tần lỗi hoặc treo.

**STO có dừng máy ngay lập tức không?**
**Không.** STO chỉ cắt mô-men; động cơ và tải sau đó **chạy trớn tự do** cho tới khi ma sát làm dừng. Cần dừng nhanh thì phải kết hợp phanh cơ.

**STO có thay được khoá điện LOTO khi bảo trì không?**
**Tuyệt đối không.** Khi STO kích hoạt, **nguồn ba pha vẫn vào biến tần và tụ DC bus vẫn tích điện nguy hiểm**. Bảo trì bắt buộc phải cách ly nguồn và chờ tụ xả.

**Vì sao STO có hai kênh?**
Để **một kênh hỏng thì kênh kia vẫn đảm bảo an toàn**. Biến tần còn giám sát chéo hai kênh và báo lỗi nếu chúng không khớp nhau.

**Đấu STO theo logic nào là đúng?**
**Có điện 24V = cho phép chạy, mất điện = kích hoạt STO.** Nhờ vậy đứt dây hay tuột giắc cũng đưa hệ về trạng thái an toàn.

**Nên đặt reset tự động hay thủ công?**
**Thủ công** cho đa số trường hợp — máy không được tự chạy lại ngay khi nhả nút dừng khẩn, vì có thể vẫn còn người trong vùng máy.

**Dùng STO cho cầu trục có an toàn không?**
Chỉ khi **kết hợp phanh cơ đóng đồng thời**. STO một mình cắt mô-men sẽ làm **tải rơi tự do**.

**STO thay được contactor giữa biến tần và động cơ không?**
Trong nhiều trường hợp có, và đó là lợi ích thực dụng lớn: **không có bộ phận cơ khí mòn**, phản hồi nhanh hơn, tiết kiệm không gian tủ. Cần đối chiếu với yêu cầu an toàn cụ thể của máy.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /cau-tao-bien-tan/, /bien-tan-cho-cau-truc-palang/, /bien-tan-cho-dong-co-nam-cham-vinh-cuu/, /an-toan-dien-voi-bien-tan/, /nghiem-thu-chay-thu-bien-tan/, /bao-tri-bien-tan-dinh-ky/, /lien-he/. -->
