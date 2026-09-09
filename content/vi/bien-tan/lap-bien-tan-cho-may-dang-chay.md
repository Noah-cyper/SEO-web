<!--
LOẠI TRANG : Bài dự án (chuỗi biến tần — tầng 9) — Thương mại
URL SLUG   : /lap-bien-tan-cho-may-dang-chay/
TỪ KHÓA    : lắp biến tần cho máy cũ | retrofit biến tần | cải tạo máy lắp biến tần | thay khởi động trực tiếp bằng biến tần | nâng cấp tủ điện
INTENT     : Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 46/50 trong chuỗi biến tần.
-->

TITLE TAG   : Lắp Biến Tần Cho Máy Đang Chạy – Quy Trình Retrofit Từ A Đến Z
META (156)  : Cải tạo máy đang chạy trực tiếp để lắp biến tần: khảo sát động cơ và cơ khí, kiểm tra cách điện, chọn thiết bị, kế hoạch dừng máy và nghiệm thu đo lại tiết kiệm.

H1          : Lắp Biến Tần Cho Máy Đang Chạy (Retrofit)

---

## Cải tạo khác với lắp mới

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-vfd-retrofit.svg)


Phần lớn bài viết về biến tần giả định bạn đang thiết kế một hệ thống mới: chọn động cơ, chọn biến tần, thiết kế tủ, đấu nối. Mọi thứ đều mới và đều do bạn quyết định.

Thực tế phổ biến hơn nhiều là **retrofit**: một cái máy đã chạy nhiều năm bằng cách đóng trực tiếp hoặc sao–tam giác, giờ cần lắp biến tần vào để tiết kiệm điện, để đổi tốc độ theo sản phẩm, hoặc để giảm hỏng hóc cơ khí.

Retrofit có những ràng buộc riêng mà lắp mới không có:

- **Động cơ đã có sẵn** — không được chọn, và có thể đã cũ.
- **Cơ khí đã có sẵn** — có thể đã xuống cấp mà không ai biết.
- **Tủ điện đã có sẵn** — thường không còn chỗ, không đủ thông gió.
- **Cáp đã đi sẵn** — có thể không đúng loại cần cho biến tần.
- **Máy đang chạy sản xuất** — thời gian dừng máy là chi phí thật.
- **Người vận hành đã quen cách cũ** — cần thời gian làm quen.

Bỏ qua các ràng buộc này là nguyên nhân của những dự án retrofit "lắp xong rồi hỏng" — thiết bị mới cháy trong tuần đầu, hoặc máy chạy nhưng không đạt được lợi ích mong đợi.

Bài này trình bày quy trình đầy đủ, theo thứ tự thực tế.

> **Đang có máy muốn cải tạo lắp biến tần?** Gửi **loại máy · nhãn động cơ · ảnh tủ điện** → [Nhận khảo sát và báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-affinity.svg)


Đây là bài **46/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: xác định máy có đáng retrofit không

Không phải máy nào cũng đáng lắp biến tần. Trước khi khảo sát kỹ thuật, hãy sàng lọc theo bốn câu hỏi:

**1. Máy có chạy non tải thường xuyên không?**

Đây là câu hỏi quan trọng nhất về mặt kinh tế. Dấu hiệu nhận biết non tải:
- **Van đang bị bóp** (bơm) hoặc **damper đang đóng bớt** (quạt) — dấu hiệu rõ ràng nhất.
- **Máy chạy tải/không tải theo chu kỳ** (máy nén khí).
- **Dòng đo được thấp hơn nhiều so với dòng định mức** động cơ.
- **Sản lượng thực tế thấp hơn công suất thiết kế.**

Máy luôn chạy đầy tải thì tiềm năng tiết kiệm rất thấp.

**2. Máy có chạy nhiều giờ không?**

Tiết kiệm mỗi giờ nhân với số giờ. Máy chạy 3 ca hoàn vốn nhanh hơn nhiều lần so với máy chạy vài giờ mỗi tuần.

**3. Tải thuộc loại nào?**

- **Tải ly tâm (bơm, quạt)** → tiềm năng tiết kiệm cao nhất, quy luật lập phương ([xem bài tiết kiệm điện](/bien-tan-tiet-kiem-dien/)).
- **Tải mô-men không đổi (băng tải, máy nén)** → tiết kiệm ít hơn, nhưng có thể có lý do khác.
- **Máy chạy cố định một tốc độ, luôn đầy tải** → cân nhắc **khởi động mềm** thay vì biến tần ([xem bài so sánh](/bien-tan-va-khoi-dong-mem/)).

**4. Có lý do ngoài tiết kiệm điện không?**

Nhiều dự án retrofit đáng làm dù tiết kiệm điện không nhiều:
- **Cần đổi tốc độ theo sản phẩm** — linh hoạt sản xuất.
- **Giảm hỏng hóc cơ khí** do khởi động sốc.
- **Giảm sản phẩm hỏng** do khởi động giật (băng tải).
- **Giữ áp suất, lưu lượng ổn định** — chất lượng sản phẩm.
- **Giảm dòng khởi động** — lưới yếu, không nâng được công suất trạm.
- **Tích hợp vào hệ giám sát tập trung.**

Nếu cả bốn câu trả lời đều không thuận, hãy nói thẳng với chủ đầu tư rằng máy đó không nên retrofit — và dành ngân sách cho máy khác.

---

## Cấu tạo quy trình: khảo sát trước khi báo giá

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-retrofit.svg)


Đây là phần quyết định dự án thành hay bại. Đừng báo giá dựa trên một dòng "động cơ 15kW".

### Khảo sát động cơ

- [ ] **Chụp ảnh nhãn động cơ** — công suất, điện áp, dòng, tần số, tốc độ, cách đấu, cấp cách điện, cấp bảo vệ.
- [ ] **Kiểm tra cách đấu thực tế trong hộp cực** — sao hay tam giác. Không tin vào nhãn, phải mở ra xem.
- [ ] **Đo cách điện cuộn dây** — đây là bước bắt buộc, xem phần dưới.
- [ ] **Đo điện trở ba pha cuộn dây** — phải cân nhau.
- [ ] **Đánh giá tuổi và tình trạng** — động cơ đã quấn lại chưa, quấn lại mấy lần.
- [ ] **Kiểm tra có phải loại inverter-duty không** — động cơ cũ thường không phải.
- [ ] **Xem có quạt làm mát gắn trục hay quạt cưỡng bức.**

**Về đo cách điện — bước không được bỏ qua.** Động cơ chạy trực tiếp từ lưới chỉ chịu điện áp hình sin 50Hz. Khi chuyển sang biến tần, nó phải chịu **chuỗi xung có sườn dốc, với đỉnh áp có thể cao hơn đáng kể** do hiện tượng phản xạ sóng ([xem bài cuộn kháng](/cuon-khang-loc-nhieu-bien-tan/)).

Một động cơ cũ có cách điện đã suy giảm — vẫn chạy tốt trên lưới — có thể **cháy trong vài ngày** sau khi chuyển sang biến tần. Và khi đó, biến tần sẽ bị đổ lỗi.

Vì vậy: **đo cách điện trước khi lắp, và ghi kết quả vào hồ sơ**. Nếu giá trị thấp, phải xử lý động cơ trước — sấy, quấn lại, hoặc thay mới.

Lưu ý an toàn: đo bằng megger **chỉ khi đã tháo cáp khỏi biến tần** (nếu đã lắp), nếu không sẽ phá hỏng mạch điện tử.

### Khảo sát cơ khí

- [ ] **Quay trục bằng tay** — có nặng, có kẹt, có tiếng lạ không.
- [ ] **Kiểm tra vòng bi** — tiếng ồn, độ rơ.
- [ ] **Kiểm tra khớp nối, dây curoa, xích** — độ căng, đồng tâm, mòn.
- [ ] **Kiểm tra hộp số** — dầu, tiếng ồn.
- [ ] **Kiểm tra tải** — van có kẹt không, đường ống có tắc không, băng có lệch không.

**Nguyên tắc:** đừng dùng biến tần để bù cho cơ khí kém. Một băng tải có con lăn kẹt sẽ vẫn kẹt sau khi lắp biến tần, chỉ khác là bây giờ biến tần sẽ báo quá dòng và bị đổ lỗi.

### Đo điện trước khi lắp

Đây là bước tạo ra **cơ sở so sánh** để chứng minh hiệu quả sau này:

- [ ] **Đo dòng ba pha** ở các chế độ vận hành thực tế, trong ít nhất một tuần.
- [ ] **Đo công suất tiêu thụ** nếu có thiết bị.
- [ ] **Ghi lại điều kiện vận hành** — van mở bao nhiêu, damper mở bao nhiêu, sản lượng bao nhiêu.
- [ ] **Ghi lại số giờ chạy mỗi ngày** và phân bố theo ca.
- [ ] **Đo điện áp nguồn** — có sụt áp, có mất pha không.

Bỏ qua bước này nghĩa là sau khi lắp xong, bạn **không có cách nào chứng minh đã tiết kiệm được bao nhiêu**.

### Khảo sát tủ điện và cáp

- [ ] **Đo không gian trống trong tủ** — biến tần cần chỗ và cần khoảng cách thoáng ([xem bố trí tủ](/lap-bien-tan-trong-tu-dien/)).
- [ ] **Đánh giá thông gió tủ** — có quạt hút, lọc gió không.
- [ ] **Đo nhiệt độ trong tủ** vào thời điểm nóng nhất trong ngày.
- [ ] **Kiểm tra tiết diện cáp động lực** — còn phù hợp không.
- [ ] **Đo chiều dài cáp động cơ** — quyết định có cần cuộn kháng đầu ra không.
- [ ] **Kiểm tra loại cáp** — có bọc chống nhiễu không.
- [ ] **Kiểm tra hệ thống nối đất** — điện trở, cách đấu.
- [ ] **Kiểm tra aptomat, contactor hiện có** — còn dùng được không ([xem chọn aptomat](/chon-cap-aptomat-cho-bien-tan/)).
- [ ] **Kiểm tra loại RCCB** — cần đổi sang loại B ([xem bài dòng rò](/dong-ro-noi-dat-bien-tan/)).
- [ ] **Xem có tụ bù trên tuyến không** — rủi ro cộng hưởng ([xem bài tụ bù](/he-so-cong-suat-tu-bu-bien-tan/)).

### Khảo sát cách vận hành

- [ ] **Ai vận hành máy, bằng gì** — nút bấm, công tắc, PLC.
- [ ] **Có cần giữ nguyên giao diện vận hành cũ không** — người vận hành đã quen.
- [ ] **Có cần chế độ chạy dự phòng** khi biến tần hỏng.
- [ ] **Có tích hợp vào hệ giám sát không.**

Điểm về **chế độ dự phòng** rất thực tế: nhiều nhà máy yêu cầu giữ khả năng **chuyển tay sang chạy trực tiếp** qua contactor nếu biến tần hỏng giữa ca. Điều này khả thi với động cơ không đồng bộ và cần được thiết kế vào tủ ngay từ đầu.

---

## Ứng dụng: triển khai và bàn giao

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-retrofit.svg)


### Chuẩn bị trước ngày dừng máy

Thời gian dừng máy là chi phí thật, nên mọi thứ có thể làm trước đều phải làm trước:

1. **Lắp sẵn biến tần và phụ kiện vào tủ** (nếu dùng tủ mới) hoặc **chuẩn bị panel lắp sẵn**.
2. **Cài sẵn toàn bộ thông số** theo nhãn động cơ đã khảo sát ([xem cài đặt thông số](/cai-dat-thong-so-bien-tan/)).
3. **Chuẩn bị đủ vật tư** — cáp, đầu cốt, ống ghen, nhãn.
4. **In sẵn bảng thông số** để dán trong tủ.
5. **Lập danh sách công việc theo trình tự** và phân công người.
6. **Chuẩn bị phương án quay lại trạng thái cũ** nếu có sự cố — giữ nguyên contactor cũ, đấu để chuyển lại được trong thời gian ngắn.

Điểm cuối cùng đặc biệt quan trọng với dây chuyền sản xuất: nếu retrofit gặp vấn đề, bạn phải **đưa máy trở lại chạy được trong vòng vài chục phút**, không phải vài ngày.

### Trong ngày lắp đặt

1. **Cách ly nguồn, khoá điện (LOTO), treo biển cảnh báo.**
2. **Đo xác nhận không còn điện** ([xem bài an toàn](/an-toan-dien-voi-bien-tan/)).
3. **Tháo đấu nối cũ**, giữ lại và ghi nhãn những gì có thể dùng lại.
4. **Đo cách điện động cơ lần cuối** trước khi đấu vào biến tần.
5. **Lắp biến tần, cuộn kháng, phụ kiện.**
6. **Đấu động lực** — đúng thứ tự pha, siết đúng lực ([xem sơ đồ đấu dây](/so-do-dau-day-bien-tan/)).
7. **Đấu điều khiển** — chân DI, AI, truyền thông.
8. **Kiểm tra nối đất** toàn bộ.
9. **Ghi nhãn tất cả đầu dây.**

### Chạy thử và nghiệm thu

1. **Cấp nguồn, chưa nối động cơ** — kiểm tra biến tần lên nguồn bình thường.
2. **Nối động cơ, chạy không tải** ở tần số thấp — kiểm tra chiều quay.
3. **Tăng dần tần số**, quan sát dòng, tiếng động cơ, độ rung.
4. **Chạy với tải thật** ở các mức khác nhau.
5. **Đo dòng ba pha** và so với dòng định mức.
6. **Đo nhiệt độ tủ** sau vài giờ chạy.
7. **Thử dừng khẩn** và các chức năng an toàn.
8. **Mở hoàn toàn van hoặc damper** — bước quyết định để đạt được tiết kiệm.
9. **Đo lại điện năng** ở cùng điều kiện sản lượng như trước khi lắp.
10. **Bàn giao hồ sơ**: bảng thông số, sơ đồ đấu nối, kết quả đo trước/sau, hướng dẫn vận hành ([xem bài nghiệm thu](/nghiem-thu-chay-thu-bien-tan/)).

**Bước 8 là bước hay bị quên nhất và tốn kém nhất khi quên.** Rất nhiều dự án retrofit không đạt tiết kiệm mong đợi chỉ vì van vẫn bị bóp như cũ. Biến tần khi đó chỉ đang bù cho một trở lực nhân tạo.

### Đào tạo người vận hành

Đừng bỏ qua phần này. Người vận hành cần biết:

- **Cách chạy, dừng, đổi tốc độ** bằng giao diện mới.
- **Ý nghĩa các thông số hiển thị** — tần số, dòng, đặc biệt là dòng.
- **Đọc mã lỗi cơ bản** và biết khi nào cần gọi bảo trì ([xem bài mã lỗi](/loi-bien-tan-thuong-gap/)).
- **Không được tự ý chỉnh thông số** — và ai được phép chỉnh.
- **An toàn**: không mở tủ khi máy đang chạy, chờ tụ xả trước khi thao tác.

---

## So sánh: các mức độ retrofit

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-roi.svg)


| Mức độ | Nội dung | Chi phí | Phù hợp |
|---|---|---|---|
| **Tối thiểu** | Lắp biến tần vào tủ cũ, giữ nguyên cáp và động cơ | **Thấp nhất** | Cáp ngắn, tủ còn chỗ, động cơ tốt |
| **Cơ bản** | + Cuộn kháng đầu vào, đổi RCCB loại B, cải tạo thông gió tủ | Trung bình | **Đa số trường hợp** |
| **Đầy đủ** | + Cuộn kháng đầu ra, cáp bọc chống nhiễu, cảm biến và PID | Cao | Cáp dài, cần giữ áp/lưu lượng |
| **Toàn diện** | + Tủ mới, động cơ inverter-duty, tích hợp PLC/giám sát | **Cao nhất** | Động cơ cũ yếu, dự án lớn |

**Lời khuyên chọn mức:** đừng chọn mức tối thiểu chỉ vì rẻ. Ba khoản trong mức "cơ bản" — cuộn kháng đầu vào, RCCB đúng loại, thông gió tủ — là các khoản nhỏ nhưng ngăn được phần lớn sự cố sau lắp đặt. Cắt chúng để tiết kiệm là tiết kiệm sai chỗ.

---

## Sai lầm thường gặp

1. **Không đo cách điện động cơ trước khi lắp** — động cơ cũ cháy sau vài ngày, biến tần bị đổ lỗi.
2. **Không kiểm tra cơ khí** — dùng biến tần để bù cho vòng bi hỏng, con lăn kẹt.
3. **Không đo điện trước khi lắp** — không có cơ sở chứng minh tiết kiệm.
4. **Quên mở van/damper sau khi lắp** — mất phần lớn lợi ích.
5. **Nhồi biến tần vào tủ cũ chật** — quá nhiệt vào mùa hè.
6. **Giữ nguyên RCCB loại cũ** — nhảy liên tục hoặc bảo vệ không tin cậy.
7. **Không xem lại tụ bù trên tuyến** — rủi ro cộng hưởng.
8. **Bỏ qua cuộn kháng đầu ra khi cáp dài** — hỏng cách điện động cơ.
9. **Không chuẩn bị phương án quay lại trạng thái cũ** — sự cố là dừng sản xuất dài.
10. **Không đào tạo người vận hành** — máy chạy sai hoặc bị chỉnh lung tung.
11. **Không ghi nhãn đầu dây và lưu bảng thông số** — khổ cho người sau.
12. **Retrofit máy luôn chạy đầy tải** — không hoàn vốn được.

---

## Cam kết tại HOANTRANTDH

- ✅ **Khảo sát trước khi báo giá** — không báo giá dựa trên một dòng công suất động cơ.
- ✅ **Tư vấn trung thực** về việc máy có đáng retrofit hay không, và có nên dùng khởi động mềm thay thế.
- ✅ **Cài sẵn thông số** theo nhãn động cơ trước khi giao, rút ngắn thời gian dừng máy.
- ✅ Hỗ trợ **đo trước – đo sau** để chứng minh hiệu quả bằng số liệu.

---

<a name="bao-gia"></a>
## Nhận khảo sát & báo giá retrofit

Gửi cho chúng tôi: **ảnh nhãn động cơ · ảnh tủ điện hiện tại (mở cửa) · loại máy và cách vận hành hiện nay · van/damper đang mở bao nhiêu phần · số giờ chạy mỗi ngày · chiều dài cáp tới động cơ · có tụ bù trên tuyến không · thời gian dừng máy cho phép.**

**→ [Liên hệ nhận khảo sát retrofit](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Máy đang chạy trực tiếp có lắp biến tần được không?**
**Được**, đây là dạng dự án phổ biến (retrofit). Nhưng phải khảo sát kỹ động cơ, cơ khí, tủ điện và cáp trước, vì các ràng buộc sẵn có quyết định phương án và chi phí.

**Vì sao phải đo cách điện động cơ trước khi lắp biến tần?**
Vì biến tần cấp **chuỗi xung có sườn dốc**, đỉnh áp cao hơn nhiều so với điện áp sin 50Hz. Động cơ cũ có cách điện suy giảm vẫn chạy tốt trên lưới nhưng **có thể cháy nhanh** khi chuyển sang biến tần.

**Có được dùng động cơ cũ không phải loại inverter-duty không?**
Được trong nhiều trường hợp, nhưng cần **đo cách điện** và cân nhắc lắp **cuộn kháng đầu ra hoặc lọc dU/dt** nếu cáp dài, để bảo vệ cách điện.

**Máy nào không nên retrofit?**
Máy **luôn chạy đầy tải**, **chạy rất ít giờ**, hoặc **chạy cố định một tốc độ mà chỉ cần khởi động êm** — trường hợp cuối nên dùng khởi động mềm.

**Bước nào hay bị quên nhất sau khi lắp?**
**Mở hoàn toàn van hoặc damper.** Giữ nguyên trạng thái bóp cũ khiến biến tần chỉ đang bù cho một trở lực nhân tạo, mất phần lớn lợi ích tiết kiệm.

**Có cần đo điện trước khi lắp không?**
**Rất cần.** Đó là cơ sở duy nhất để chứng minh mức tiết kiệm sau này. Nên đo dòng và công suất ở các chế độ thực tế trong ít nhất một tuần.

**Có giữ được khả năng chạy trực tiếp khi biến tần hỏng không?**
**Có**, với động cơ không đồng bộ — thiết kế tủ có contactor chuyển tay. Cần đưa vào yêu cầu ngay từ đầu. Lưu ý điều này **không làm được với động cơ nam châm vĩnh cửu**.

**Nên chọn mức retrofit nào?**
Thường là **mức cơ bản**: biến tần + cuộn kháng đầu vào + RCCB đúng loại + cải tạo thông gió tủ. Ba khoản phụ này nhỏ nhưng ngăn được phần lớn sự cố sau lắp đặt.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /bien-tan-tiet-kiem-dien/, /bien-tan-va-khoi-dong-mem/, /cuon-khang-loc-nhieu-bien-tan/, /lap-bien-tan-trong-tu-dien/, /chon-cap-aptomat-cho-bien-tan/, /dong-ro-noi-dat-bien-tan/, /he-so-cong-suat-tu-bu-bien-tan/, /cai-dat-thong-so-bien-tan/, /so-do-dau-day-bien-tan/, /an-toan-dien-voi-bien-tan/, /nghiem-thu-chay-thu-bien-tan/, /loi-bien-tan-thuong-gap/, /lien-he/. -->
