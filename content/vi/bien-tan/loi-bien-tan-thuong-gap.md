<!--
LOẠI TRANG : Bài xử lý sự cố (chuỗi biến tần — tầng 5) — Thông tin
URL SLUG   : /loi-bien-tan-thuong-gap/
TỪ KHÓA    : lỗi biến tần | mã lỗi biến tần | biến tần báo lỗi | biến tần không lên nguồn | cách khắc phục lỗi biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 25/30 trong chuỗi biến tần.
-->

TITLE TAG   : Lỗi Biến Tần Thường Gặp – Bảng Tra Mã Lỗi Và Cách Khắc Phục
META (156)  : Tổng hợp các nhóm lỗi biến tần phổ biến: quá dòng, quá áp, thấp áp, quá nhiệt, quá tải, mất pha, lỗi truyền thông. Kèm quy trình chẩn đoán 7 bước.

H1          : Lỗi Biến Tần Thường Gặp Và Cách Khắc Phục

---

## Mã lỗi là thông tin, không phải bản án

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan-loi.svg)


Khi biến tần dừng và hiện một mã lỗi, phản ứng thường thấy là nghĩ rằng thiết bị đã hỏng. Trong thực tế, **phần lớn mã lỗi không có nghĩa là biến tần hỏng**. Chúng là kết quả của cơ chế tự bảo vệ: biến tần phát hiện một điều kiện bất thường và **chủ động ngắt để tự bảo vệ mình và bảo vệ động cơ**.

Nói cách khác, mã lỗi là thiết bị đang **báo cho bạn biết có gì đó không ổn trong hệ thống** — có thể là tải, là cài đặt, là đấu nối, là nguồn điện, là môi trường. Nhiệm vụ của người vận hành là đọc đúng thông điệp đó.

Bài này tổng hợp các **nhóm lỗi lớn**, ý nghĩa và hướng xử lý, kèm quy trình chẩn đoán chung. Các lỗi quan trọng nhất được phân tích sâu trong các bài riêng của chuỗi.

> **Biến tần đang báo lỗi và chưa xử lý được?** Gửi **mã lỗi · model biến tần · thời điểm xảy ra** → [Nhận hỗ trợ chẩn đoán](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-vfd-loi.svg)


Đây là bài **25/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: biến tần tự bảo vệ như thế nào

Biến tần liên tục đo một loạt đại lượng và so với ngưỡng đã cài:

- **Dòng đầu ra** — bảo vệ IGBT và động cơ khỏi quá dòng tức thời và quá tải kéo dài.
- **Điện áp DC bus** — phát hiện quá áp (năng lượng dội về, lưới cao) và thấp áp (mất pha, sụt áp lưới).
- **Nhiệt độ tản nhiệt** — bảo vệ IGBT khỏi quá nhiệt.
- **Cân bằng pha đầu vào và đầu ra** — phát hiện mất pha, đứt dây.
- **Điện trở cách điện / dòng chạm đất** — phát hiện chạm vỏ.
- **Trạng thái truyền thông** — phát hiện mất kết nối với thiết bị điều khiển.

Khi một đại lượng vượt ngưỡng, biến tần **cắt đầu ra ngay** và ghi lại mã lỗi. Nhiều dòng còn lưu **lịch sử lỗi** kèm các thông số tại thời điểm xảy ra — dòng, tần số, điện áp DC bus, nhiệt độ. Đây là **nguồn thông tin quý nhất** để chẩn đoán, và cũng là nơi ít người nghĩ tới xem đầu tiên.

Một điểm cần nắm: **thời điểm xảy ra lỗi cho biết rất nhiều về nguyên nhân.**

| Lỗi xảy ra khi | Hướng nghi ngờ |
|---|---|
| **Khi tăng tốc** | Thời gian tăng tốc quá ngắn, tải nặng, mô-men khởi động không đủ |
| **Khi giảm tốc / dừng** | Năng lượng dội về, thiếu điện trở xả |
| **Khi chạy ổn định** | Tải bất thường, cơ khí kẹt, cài đặt sai, nhiệt độ |
| **Ngay khi cấp nguồn** | Nguồn điện, chạm chập, phần cứng |
| **Ngẫu nhiên, không quy luật** | Nhiễu, tiếp xúc lỏng, nguồn dao động |
| **Chỉ khi trời nóng / chiều muộn** | Tản nhiệt, quạt, bụi bẩn |

---

## Cấu tạo bảng tra: các nhóm lỗi chính

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-baotri.svg)


Mã lỗi khác nhau giữa các hãng (OC, E.OC1, Err05, F001…), nhưng **nhóm nghĩa thì giống nhau**. Hãy tra theo nhóm dưới đây rồi đối chiếu với sách hướng dẫn của model bạn đang dùng.

| Nhóm lỗi | Ký hiệu thường gặp | Ý nghĩa | Nguyên nhân phổ biến |
|---|---|---|---|
| **Quá dòng** | OC, OC1/2/3 | Dòng vượt ngưỡng tức thời | Tăng tốc quá nhanh, tải kẹt, chạm chập đầu ra, cài sai [chi tiết →](/loi-qua-dong-bien-tan/) |
| **Quá áp** | OV, OU | DC bus vượt ngưỡng | Giảm tốc quá nhanh, tải kéo động cơ, lưới cao [chi tiết →](/loi-qua-ap-thap-ap-bien-tan/) |
| **Thấp áp** | LV, UV, LU | DC bus dưới ngưỡng | Mất pha đầu vào, sụt áp lưới, tiếp xúc lỏng |
| **Quá nhiệt** | OH, OH1/2 | Tản nhiệt quá nóng | Quạt hỏng, bụi bám, tủ kín [chi tiết →](/loi-qua-nhiet-qua-tai-bien-tan/) |
| **Quá tải** | OL, OL1/2 | Dòng cao kéo dài | Tải nặng hơn thiết kế, chọn thiếu công suất |
| **Mất pha** | SPI, SPO, LF | Mất pha vào hoặc ra | Cầu chì đứt, cực lỏng, đứt cáp |
| **Chạm đất** | GF, GFF | Dòng rò lớn | Cách điện động cơ hỏng, cáp ẩm |
| **Lỗi truyền thông** | CE, CoF | Mất kết nối | Cáp RS485, sai cấu hình [chi tiết →](/dieu-khien-bien-tan-bang-plc/) |
| **Lỗi EEPROM / bộ nhớ** | EEP, Er.EEP | Lỗi lưu thông số | Mất nguồn khi đang ghi, phần cứng |
| **Lỗi bên ngoài** | EF, E.Ext | Tín hiệu lỗi từ chân DI | Thiết bị ngoài báo lỗi, chân cấu hình sai |
| **Lỗi CPU / phần cứng** | Er, Fn | Lỗi nội bộ | Nhiễu nặng hoặc hỏng board |
| **Lỗi auto-tune** | tUn, tE | Auto-tune thất bại | Khai báo động cơ sai, tải còn lắp |

---

## Ứng dụng: quy trình chẩn đoán 7 bước

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-suachua.svg)


Áp dụng được cho hầu hết mã lỗi:

**Bước 1 — Ghi lại đầy đủ thông tin trước khi reset.** Mã lỗi, thời điểm, biến tần đang làm gì (tăng tốc, chạy, dừng), tải ra sao, có gì thay đổi gần đây không. **Đừng vội bấm reset** — reset xóa mất bối cảnh.

**Bước 2 — Xem lịch sử lỗi trong biến tần.** Nhiều người bỏ qua bước này. Lịch sử cho biết lỗi lặp lại bao nhiêu lần, và các thông số tại thời điểm lỗi.

**Bước 3 — Xác định lỗi thuộc nhóm nào** theo bảng trên và tra sách hướng dẫn của đúng model.

**Bước 4 — Kiểm tra phần cơ khí trước phần điện.** Quay thử trục động cơ bằng tay (khi đã ngắt điện an toàn). Trục nặng, kẹt, có tiếng lạ — rất nhiều "lỗi biến tần" thực ra là **hỏng vòng bi, kẹt tải, lệch tâm khớp nối**.

**Bước 5 — Kiểm tra đấu nối và tiếp xúc.** Siết lại toàn bộ cực đấu động lực (khi đã ngắt điện và chờ tụ xả hết). Cực lỏng là nguyên nhân của rất nhiều lỗi ngẫu nhiên khó hiểu.

**Bước 6 — Kiểm tra thông số cài đặt.** Đặc biệt: thông số động cơ có khai đúng nhãn không, thời gian tăng/giảm tốc có hợp lý không, chế độ điều khiển có phù hợp tải không ([xem bài cài đặt](/cai-dat-thong-so-bien-tan/)).

**Bước 7 — Chạy thử không tải.** Tháo khớp nối, chạy biến tần với động cơ không tải. Nếu chạy êm không lỗi → **vấn đề ở tải hoặc cơ khí**, không phải biến tần. Nếu vẫn lỗi → khoanh vùng tiếp về phía động cơ hoặc biến tần.

### Ba bài kiểm tra an toàn phải nhớ

1. **Chờ tụ DC bus xả hết.** Sau khi ngắt nguồn, tụ vẫn còn tích điện ở mức nguy hiểm trong nhiều phút. Chờ đủ thời gian theo cảnh báo trên thân máy và **đo xác nhận** trước khi chạm vào cực đấu.
2. **Không megger (đo cách điện cao áp) khi biến tần còn đấu.** Sẽ phá hỏng mạch điện tử. Phải tháo cáp động cơ khỏi biến tần trước.
3. **Không đo điện trở đầu ra biến tần bằng đồng hồ ở thang cao áp.**

---

## So sánh: lỗi do hệ thống và lỗi do biến tần

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-sua-thay.svg)


Câu hỏi thực tế quan trọng nhất là: **có phải thay biến tần không?** Bảng dưới giúp phân biệt.

| Dấu hiệu | Nhiều khả năng do **hệ thống** | Nhiều khả năng do **biến tần** |
|---|---|---|
| Lỗi chỉ xuất hiện khi có tải | ✔ | |
| Chạy không tải vẫn lỗi | | ✔ |
| Lỗi xuất hiện sau khi đổi tải, đổi cài đặt | ✔ | |
| Lỗi xuất hiện dần theo thời gian, kèm tiếng ồn/quá nhiệt | | ✔ (tụ, quạt) |
| Không lên nguồn dù có điện vào | | ✔ |
| Có mùi khét, vết cháy, tụ phồng | | ✔ |
| Lỗi biến mất khi đổi sang biến tần khác cùng cấu hình | | ✔ |
| Lỗi vẫn còn khi đổi biến tần khác | ✔ | |
| Lỗi liên quan tới nhiễu, truyền thông | ✔ ([xem EMC](/chong-nhieu-emc-cho-bien-tan/)) | |

**Phép thử quyết định:** nếu thay tạm một biến tần khác cùng thông số mà lỗi biến mất → vấn đề ở biến tần cũ. Nếu lỗi vẫn còn → vấn đề ở hệ thống, và thay máy mới cũng không giải quyết được.

Khi đã xác định biến tần thực sự có vấn đề, bước tiếp theo là cân nhắc sửa hay thay ([xem bài phân tích](/sua-hay-thay-bien-tan/)).

---

## Sai lầm thường gặp

1. **Reset lỗi liên tục để chạy tiếp** mà không tìm nguyên nhân — nguy cơ hỏng thật.
2. **Không ghi lại mã lỗi và bối cảnh** trước khi reset.
3. **Bỏ qua lịch sử lỗi** lưu trong máy.
4. **Kết luận biến tần hỏng ngay** mà chưa kiểm tra cơ khí và đấu nối.
5. **Đo cách điện bằng megger khi biến tần còn đấu cáp** — phá hỏng thiết bị.
6. **Chạm vào cực đấu ngay sau khi ngắt nguồn** — tụ còn tích điện nguy hiểm.
7. **Tăng ngưỡng bảo vệ để hết báo lỗi** — vô hiệu hóa chính chức năng bảo vệ.
8. **Thay biến tần lớn hơn** để "chắc ăn" mà không biết nguyên nhân thật.
9. **Không kiểm tra lại sau khi sửa** — chỉ chạy không tải rồi bàn giao.
10. **Không lưu bảng thông số**, nên khi thay máy phải dò lại từ đầu.

---

## Cam kết tại HOANTRANTDH

- ✅ **Hỗ trợ chẩn đoán mã lỗi miễn phí** qua Zalo — gửi ảnh màn hình và mô tả, nhận hướng xử lý.
- ✅ Tư vấn trung thực **có cần thay biến tần hay không** — không đẩy khách mua thiết bị mới khi lỗi nằm ở hệ thống.
- ✅ Hỗ trợ **chuyển thông số sang máy mới** khi buộc phải thay.
- ✅ Cung cấp [biến tần](/bien-tan-la-gi/) thay thế, linh kiện và phụ kiện tủ điện.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ chẩn đoán & báo giá

Gửi cho chúng tôi: **mã lỗi hiển thị · model biến tần · lỗi xảy ra khi nào (khởi động/chạy/dừng) · công suất và loại tải · có thay đổi gì gần đây không · ảnh màn hình và ảnh tủ.**

**→ [Liên hệ hỗ trợ xử lý lỗi](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Biến tần báo lỗi có nghĩa là đã hỏng chưa?**
**Chưa chắc.** Phần lớn mã lỗi là biến tần **tự bảo vệ** khi phát hiện điều kiện bất thường từ tải, cài đặt, đấu nối hoặc nguồn điện.

**Nên làm gì đầu tiên khi biến tần báo lỗi?**
**Ghi lại mã lỗi và bối cảnh** trước khi reset, sau đó xem **lịch sử lỗi** lưu trong máy để biết lỗi lặp lại thế nào.

**Reset lỗi nhiều lần có sao không?**
Có. Reset liên tục để chạy tiếp mà không xử lý nguyên nhân có thể **làm hỏng thật** IGBT, động cơ hoặc cơ khí.

**Làm sao biết lỗi do biến tần hay do hệ thống?**
Phép thử rõ nhất: **chạy không tải**. Nếu êm thì vấn đề ở tải/cơ khí. Ngoài ra, thay tạm một biến tần khác cùng cấu hình — lỗi biến mất nghĩa là biến tần cũ có vấn đề.

**Có được đo cách điện động cơ khi biến tần còn đấu không?**
**Không.** Megger sẽ phá hỏng mạch điện tử. Phải **tháo cáp động cơ khỏi biến tần** trước khi đo.

**Sau khi ngắt điện bao lâu thì chạm được vào cực đấu?**
Phải **chờ tụ DC bus xả hết** theo cảnh báo trên thân máy và **đo xác nhận** bằng đồng hồ trước khi thao tác.

**Có nên tăng ngưỡng bảo vệ để hết báo lỗi không?**
Không. Đó là **vô hiệu hóa chức năng bảo vệ**, và hậu quả thường là hỏng IGBT hoặc cháy động cơ.

**Vì sao lỗi chỉ xảy ra vào buổi chiều nắng nóng?**
Gần như chắc chắn liên quan tới **tản nhiệt**: quạt yếu, khe tản nhiệt bám bụi, hoặc tủ điện thiếu thông gió.

<!-- SCHEMA: FAQPage + BreadcrumbList + Article. INTERNAL LINK: /bien-tan-la-gi/, /loi-qua-dong-bien-tan/, /loi-qua-ap-thap-ap-bien-tan/, /loi-qua-nhiet-qua-tai-bien-tan/, /cai-dat-thong-so-bien-tan/, /chong-nhieu-emc-cho-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /sua-hay-thay-bien-tan/, /lien-he/. -->
