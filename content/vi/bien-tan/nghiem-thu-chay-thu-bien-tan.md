<!--
LOẠI TRANG : Bài quy trình (chuỗi biến tần — tầng 9) — Thông tin → Thương mại
URL SLUG   : /nghiem-thu-chay-thu-bien-tan/
TỪ KHÓA    : nghiệm thu biến tần | chạy thử biến tần | commissioning biến tần | biên bản nghiệm thu tủ điện | checklist chạy thử
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 47/50 trong chuỗi biến tần.
-->

TITLE TAG   : Nghiệm Thu & Chạy Thử Hệ Biến Tần – Checklist 5 Giai Đoạn
META (156)  : Quy trình nghiệm thu hệ biến tần: kiểm tra nguội, cấp nguồn không tải, chạy không tải, chạy có tải và thử tình huống bất thường. Kèm checklist và hồ sơ bàn giao.

H1          : Nghiệm Thu Và Chạy Thử Hệ Biến Tần

---

## Bàn giao không phải là bấm Run rồi thấy máy quay

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-tu-dien-bien-tan.svg)


Rất nhiều hệ biến tần được "nghiệm thu" theo cách sau: đấu xong, bấm chạy, thấy động cơ quay đúng chiều, ký biên bản, xong.

Vài tuần hoặc vài tháng sau, các vấn đề bắt đầu xuất hiện: máy báo lỗi khi tải nặng, tủ quá nhiệt vào mùa hè, dừng khẩn không hoạt động đúng, không ai biết thông số đã cài là gì.

Tất cả những thứ đó **đều phát hiện được trong một buổi nghiệm thu làm đúng** — với chi phí gần bằng không, so với chi phí xử lý sau này khi máy đang chạy sản xuất.

Nghiệm thu tốt có ba mục đích:

1. **Phát hiện lỗi lắp đặt** khi còn dễ sửa và chưa gây hư hỏng.
2. **Xác nhận hệ đạt yêu cầu** ở điều kiện vận hành thực tế, không chỉ ở điều kiện thuận lợi.
3. **Tạo ra bộ hồ sơ gốc** — các con số ban đầu để so sánh về sau, và bảng thông số để khôi phục khi cần.

Mục đích thứ ba hay bị xem nhẹ nhưng có giá trị lâu dài nhất. Một hồ sơ nghiệm thu đầy đủ biến việc thay một biến tần hỏng từ **hai ngày dò lại** thành **hai mươi phút**.

Bài này đưa ra quy trình theo **năm giai đoạn**, mỗi giai đoạn có checklist cụ thể.

> **Cần checklist nghiệm thu cho dự án của bạn?** Gửi **số lượng biến tần · loại máy** → [Nhận mẫu biên bản](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-pwm.svg)


Đây là bài **47/50** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: nghiệm thu theo thứ tự tăng dần rủi ro

Nguyên tắc xuyên suốt: **kiểm tra ở trạng thái an toàn nhất trước, rồi mới tăng dần mức độ**. Không bao giờ nhảy bước.

Thứ tự đúng:

**Giai đoạn 1 — Kiểm tra nguội.** Không có điện. Kiểm tra bằng mắt và bằng đồng hồ.

**Giai đoạn 2 — Cấp nguồn, chưa nối động cơ.** Có điện vào biến tần nhưng đầu ra chưa nối gì. Nếu có lỗi lắp đặt phía nguồn, nó lộ ra ở đây mà không hại gì tới động cơ.

**Giai đoạn 3 — Chạy không tải.** Động cơ nối vào nhưng đã tháo khớp nối với tải. Kiểm tra được chiều quay, độ rung, tiếng động cơ mà không có rủi ro cho cơ khí.

**Giai đoạn 4 — Chạy có tải.** Điều kiện vận hành thật, ở nhiều mức tải khác nhau.

**Giai đoạn 5 — Thử tình huống bất thường.** Dừng khẩn, mất pha, mất truyền thông, kẹt tải.

Lý do của thứ tự này rất thực tế: nếu có một lỗi đấu nối nghiêm trọng, phát hiện nó ở giai đoạn 2 chỉ tốn công sửa dây; phát hiện ở giai đoạn 4 có thể đã hỏng động cơ và hỏng biến tần.

---

## Cấu tạo checklist: năm giai đoạn chi tiết

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-nghiem-thu.svg)


### Giai đoạn 1 — Kiểm tra nguội (không có điện)

- [ ] **Xác nhận đã cách ly nguồn và khoá điện (LOTO).**
- [ ] **Đo xác nhận không còn điện** trên các cực, kể cả tụ DC bus.
- [ ] **Đối chiếu model biến tần** với thiết kế và với công suất động cơ.
- [ ] **Kiểm tra bố trí trong tủ** — khoảng cách thoáng theo khuyến nghị hãng ([xem bố trí tủ](/lap-bien-tan-trong-tu-dien/)).
- [ ] **Kiểm tra cáp động lực** — đúng tiết diện, đúng loại, không bị kẹp hay trầy.
- [ ] **Kiểm tra thứ tự pha đầu vào và đầu ra**, đúng nhãn.
- [ ] **Siết lại toàn bộ cực đấu động lực** theo lực siết khuyến nghị.
- [ ] **Kiểm tra nối đất** — vỏ biến tần, vỏ động cơ, tấm nền tủ, lớp bọc cáp.
- [ ] **Kiểm tra kẹp tiếp đất 360°** cho lớp bọc cáp động cơ.
- [ ] **Kiểm tra cáp điều khiển** — đi tách khỏi cáp động lực ([xem chống nhiễu](/chong-nhieu-emc-cho-bien-tan/)).
- [ ] **Đo cách điện động cơ** (đã tháo cáp khỏi biến tần).
- [ ] **Đo điện trở ba pha cuộn dây** — phải cân nhau.
- [ ] **Kiểm tra cách đấu trong hộp cực động cơ** — sao hay tam giác.
- [ ] **Quay trục bằng tay** — không kẹt, không tiếng lạ.
- [ ] **Kiểm tra aptomat, contactor, RCCB** — đúng loại, đúng dòng ([xem chọn aptomat](/chon-cap-aptomat-cho-bien-tan/)).
- [ ] **Kiểm tra cuộn kháng, điện trở xả** — đúng thông số, lắp đúng vị trí, đủ thoáng.
- [ ] **Kiểm tra nhãn tất cả đầu dây.**

### Giai đoạn 2 — Cấp nguồn, chưa nối động cơ

- [ ] **Đo điện áp ba pha ngay tại cực biến tần** — cân bằng, đúng cấp.
- [ ] **Cấp nguồn, quan sát biến tần lên nguồn bình thường.**
- [ ] **Kiểm tra không có mã lỗi** ngay khi khởi động.
- [ ] **Kiểm tra quạt làm mát biến tần chạy.**
- [ ] **Reset về mặc định** nếu là thiết bị cũ hoặc không rõ lịch sử.
- [ ] **Khai báo thông số động cơ** theo nhãn thực tế ([xem cài đặt](/cai-dat-thong-so-bien-tan/)).
- [ ] **Đặt giới hạn tần số trên và dưới** theo yêu cầu công nghệ.
- [ ] **Đặt thời gian tăng/giảm tốc** ban đầu (rộng rãi).
- [ ] **Chọn chế độ điều khiển** phù hợp tải.
- [ ] **Cấu hình nguồn lệnh và nguồn đặt tần số.**
- [ ] **Kiểm tra tín hiệu đầu vào số** — bấm từng nút, xác nhận biến tần nhận.
- [ ] **Kiểm tra tín hiệu analog** — thay đổi giá trị, xác nhận biến tần đọc đúng thang.
- [ ] **Kiểm tra truyền thông** — đọc được thanh ghi trạng thái ([xem điều khiển bằng PLC](/dieu-khien-bien-tan-bang-plc/)).

### Giai đoạn 3 — Chạy không tải (đã tháo khớp nối)

- [ ] **Chạy ở tần số thấp** — xác nhận **chiều quay đúng**.
- [ ] **Chạy auto-tune** nếu dùng chế độ vector.
- [ ] **Tăng dần tần số lên định mức**, quan sát dòng và tiếng động cơ.
- [ ] **Kiểm tra độ rung** ở toàn dải tần số.
- [ ] **Ghi nhận các vùng tần số gây cộng hưởng** — khai vào skip frequency.
- [ ] **Thử dừng theo dốc và chạy trớn.**
- [ ] **Đo dòng ba pha khi không tải** — phải cân nhau.
- [ ] **Kiểm tra phản hồi tần số** hiển thị đúng giá trị đặt.

### Giai đoạn 4 — Chạy có tải

- [ ] **Nối lại khớp nối, kiểm tra đồng tâm.**
- [ ] **Khởi động ở tần số thấp**, tăng dần.
- [ ] **Đo dòng ba pha ở nhiều mức tải** — nhẹ, trung bình, **nặng nhất thực tế**.
- [ ] **So dòng với dòng định mức** của cả biến tần và động cơ.
- [ ] **Thử khởi động ở điều kiện xấu nhất** — băng đầy hàng, máy trộn đầy liệu.
- [ ] **Rút ngắn dần thời gian tăng tốc** tới ngưỡng chấp nhận được.
- [ ] **Điều chỉnh PID** nếu chạy vòng kín, thử với nhiễu loạn thật ([xem cài PID](/dieu-khien-pid-bang-bien-tan/)).
- [ ] **Chạy liên tục vài giờ**, đo **nhiệt độ tản nhiệt và nhiệt độ trong tủ**.
- [ ] **Đo nhiệt độ động cơ** sau khi chạy ổn định.
- [ ] **Kiểm tra tiếng ồn và độ rung** ở điều kiện làm việc.
- [ ] **Đo điện năng tiêu thụ** để so với số liệu trước khi lắp (với dự án retrofit).
- [ ] **Kiểm tra không có thiết bị nào khác bị nhiễu** khi biến tần chạy.

### Giai đoạn 5 — Thử tình huống bất thường

Đây là giai đoạn hay bị bỏ qua nhất, và là giai đoạn có giá trị cao nhất:

- [ ] **Thử dừng khẩn** — xác nhận máy dừng đúng như thiết kế.
- [ ] **Thử STO nếu có** — từng kênh riêng biệt, và thử đứt dây ([xem bài STO](/safe-torque-off-bien-tan/)).
- [ ] **Đo thời gian chạy trớn** của tải sau khi cắt mô-men.
- [ ] **Thử mất truyền thông** — rút cáp, xác nhận biến tần dừng an toàn theo cấu hình.
- [ ] **Thử mất tín hiệu analog** — xác nhận hành vi đúng thiết kế.
- [ ] **Thử mất pha đầu vào** (nếu an toàn và được phép) — xác nhận biến tần báo lỗi đúng.
- [ ] **Thử tình huống kẹt tải** (nếu an toàn) — xác nhận giới hạn mô-men hoạt động.
- [ ] **Thử mất điện và khôi phục** — xác nhận máy **không tự khởi động lại** nếu không được phép.
- [ ] **Thử công tắc hành trình** với hệ nâng hạ hoặc di chuyển.
- [ ] **Thử RCCB** — bấm nút test, xác nhận tác động.
- [ ] **Kiểm tra cảnh báo và tín hiệu về PLC/HMI** hiển thị đúng.

Điểm về **tự khởi động lại sau mất điện** đặc biệt quan trọng về an toàn: nếu máy tự chạy lại khi có điện mà không có ai chủ động cho phép, đó là tình huống nguy hiểm — có thể có người đang thao tác trên máy.

---

## Ứng dụng: hồ sơ bàn giao

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-retrofit.svg)


Nghiệm thu chưa xong khi chưa có hồ sơ. Bộ hồ sơ tối thiểu gồm:

**1. Biên bản nghiệm thu** — các hạng mục đã kiểm tra, kết quả, người thực hiện, ngày.

**2. Bảng thông số đã cài** — đầy đủ các thông số đã thay đổi so với mặc định. **In hai bản**: một dán trong tủ, một lưu hồ sơ. Nếu biến tần có chức năng sao lưu thông số ra bàn phím hoặc file, hãy dùng và lưu lại.

**3. Số liệu đo thực tế:**
- Dòng ba pha ở các mức tải.
- Điện áp nguồn tại cực biến tần.
- Nhiệt độ tản nhiệt và nhiệt độ trong tủ ở điều kiện nóng nhất.
- Điện năng tiêu thụ (nếu có).
- Kết quả đo cách điện động cơ.
- Thời gian chạy trớn của tải.

**4. Sơ đồ đấu nối thực tế** — nếu khác thiết kế thì phải cập nhật, không giữ bản cũ.

**5. Ảnh chụp** — bên trong tủ sau khi hoàn thành, nhãn động cơ, màn hình biến tần hiển thị các thông số chính.

**6. Danh sách vật tư đã lắp** — model biến tần, số serial, cuộn kháng, điện trở xả, aptomat, RCCB.

**7. Hướng dẫn vận hành cơ bản** — cách chạy, dừng, đổi tốc độ, đọc mã lỗi, khi nào gọi bảo trì.

**8. Kết quả thử các chức năng an toàn** — dừng khẩn, STO, công tắc hành trình.

### Giá trị của bộ hồ sơ này về sau

- **Khi biến tần hỏng phải thay:** có bảng thông số nghĩa là cài lại trong vài chục phút thay vì dò lại từ đầu ([xem bài sửa hay thay](/sua-hay-thay-bien-tan/)).
- **Khi máy bắt đầu có vấn đề:** so dòng hiện tại với dòng ban đầu ở cùng chế độ — chênh lệch là dấu hiệu sớm của hỏng hóc cơ khí.
- **Khi tranh luận về hiệu quả dự án:** có số liệu trước và sau, không phải cảm tính.
- **Khi có người mới tiếp quản:** không phải bắt đầu từ con số không.
- **Khi kiểm toán năng lượng:** có cơ sở dữ liệu sẵn.

Bộ hồ sơ này nên được **cập nhật mỗi kỳ bảo trì**, không phải làm một lần rồi để đó ([xem bài bảo trì](/bao-tri-bien-tan-dinh-ky/)).

---

## So sánh: nghiệm thu đầy đủ và nghiệm thu qua loa

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-hang.svg)


| Hạng mục | **Qua loa** | **Đầy đủ** |
|---|---|---|
| Thời gian | Vài chục phút | Vài giờ đến một ngày |
| Kiểm tra nguội | Bỏ qua | **Đầy đủ** |
| Đo cách điện động cơ | Không | **Có** |
| Chạy thử có tải nặng nhất | Không | **Có** |
| Đo nhiệt độ tủ | Không | **Có** |
| Thử tình huống bất thường | Không | **Có** |
| Bảng thông số lưu lại | Không | **Có, hai bản** |
| Số liệu gốc để so sánh | Không | **Có** |
| Sự cố trong 6 tháng đầu | **Nhiều** | Ít |
| Thời gian thay biến tần hỏng | Hàng ngày | **Vài chục phút** |
| Chứng minh hiệu quả dự án | Không được | **Được** |

Chênh lệch chi phí giữa hai cột chỉ là **vài giờ công**. Chênh lệch giá trị thì lớn hơn rất nhiều lần.

---

## Sai lầm thường gặp

1. **Nhảy thẳng sang chạy có tải** mà không qua các giai đoạn trước.
2. **Không đo cách điện động cơ** trước khi đấu vào biến tần.
3. **Chỉ chạy thử không tải** rồi ký nghiệm thu.
4. **Không thử ở tải nặng nhất thực tế** — vấn đề lộ ra sau khi bàn giao.
5. **Không đo nhiệt độ tủ** vào thời điểm nóng nhất — lỗi quá nhiệt xuất hiện vào mùa hè.
6. **Bỏ qua giai đoạn thử tình huống bất thường** — chức năng an toàn có thể không hoạt động mà không ai biết.
7. **Không thử tự khởi động lại sau mất điện** — rủi ro an toàn nghiêm trọng.
8. **Không lưu bảng thông số** — tốn hàng ngày khi phải thay thiết bị.
9. **Không ghi số liệu gốc** — không có cơ sở so sánh và chứng minh hiệu quả.
10. **Không cập nhật sơ đồ khi đấu khác thiết kế.**
11. **Không đào tạo người vận hành** trước khi bàn giao.
12. **Không thử nút test của RCCB.**

---

## Cam kết tại HOANTRANTDH

- ✅ Cung cấp **mẫu checklist nghiệm thu 5 giai đoạn** phù hợp với dự án của bạn.
- ✅ Hỗ trợ **cài đặt và ghi bảng thông số** để bàn giao cùng thiết bị.
- ✅ Hướng dẫn **quy trình đo và ghi số liệu gốc** phục vụ so sánh về sau.
- ✅ Hỗ trợ **chẩn đoán từ xa qua Zalo** khi gặp vướng mắc trong quá trình chạy thử.

---

<a name="bao-gia"></a>
## Nhận mẫu biên bản & hỗ trợ nghiệm thu

Gửi cho chúng tôi: **số lượng và model biến tần · loại máy và tải · có chức năng an toàn nào (STO, dừng khẩn, công tắc hành trình) · có PID hoặc truyền thông không · yêu cầu hồ sơ của chủ đầu tư.**

**→ [Liên hệ nhận hỗ trợ nghiệm thu](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Nghiệm thu hệ biến tần gồm mấy giai đoạn?**
**Năm giai đoạn**: kiểm tra nguội, cấp nguồn chưa nối động cơ, chạy không tải, chạy có tải, và thử tình huống bất thường — theo thứ tự **tăng dần mức rủi ro**.

**Vì sao phải cấp nguồn khi chưa nối động cơ?**
Để **lỗi lắp đặt phía nguồn lộ ra mà không gây hại cho động cơ**. Nếu có sự cố đấu nối, phát hiện ở bước này chỉ tốn công sửa dây.

**Có bắt buộc chạy thử ở tải nặng nhất không?**
**Có.** Rất nhiều vấn đề — thiếu mô-men, quá dòng, quá nhiệt — chỉ lộ ra ở điều kiện tải nặng, không xuất hiện khi chạy không tải.

**Giai đoạn nào hay bị bỏ qua nhất?**
**Thử tình huống bất thường**: dừng khẩn, mất truyền thông, mất pha, kẹt tải, tự khởi động lại sau mất điện. Đây cũng là giai đoạn có giá trị cao nhất.

**Vì sao phải đo nhiệt độ tủ khi nghiệm thu?**
Vì lỗi quá nhiệt thường **chỉ xuất hiện vào mùa nóng**, hàng tháng sau khi bàn giao. Đo ở thời điểm nóng nhất trong ngày giúp phát hiện sớm ([xem bài lỗi OH](/loi-qua-nhiet-qua-tai-bien-tan/)).

**Hồ sơ bàn giao cần có gì?**
Biên bản nghiệm thu, **bảng thông số đã cài (hai bản)**, số liệu đo thực tế, sơ đồ đấu nối cập nhật, ảnh chụp, danh sách vật tư, hướng dẫn vận hành và kết quả thử chức năng an toàn.

**Vì sao bảng thông số quan trọng đến vậy?**
Vì khi biến tần hỏng phải thay, có bảng thông số nghĩa là **cài lại trong vài chục phút** thay vì dò lại từ đầu mất hàng ngày.

**Có cần thử máy tự khởi động lại sau mất điện không?**
**Rất cần.** Máy tự chạy lại khi có điện mà không ai chủ động cho phép là tình huống nguy hiểm — có thể có người đang thao tác trên máy.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /lap-bien-tan-trong-tu-dien/, /chong-nhieu-emc-cho-bien-tan/, /chon-cap-aptomat-cho-bien-tan/, /cai-dat-thong-so-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /dieu-khien-pid-bang-bien-tan/, /safe-torque-off-bien-tan/, /bao-tri-bien-tan-dinh-ky/, /sua-hay-thay-bien-tan/, /loi-qua-nhiet-qua-tai-bien-tan/, /lien-he/. -->
