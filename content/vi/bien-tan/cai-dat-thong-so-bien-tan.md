<!--
LOẠI TRANG : Bài hướng dẫn kỹ thuật (chuỗi biến tần — tầng 4) — Thông tin
URL SLUG   : /cai-dat-thong-so-bien-tan/
TỪ KHÓA    : cài đặt biến tần | thông số biến tần | reset biến tần về mặc định | cài tần số biến tần | auto tune biến tần
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 18/30 trong chuỗi biến tần.
-->

TITLE TAG   : Cài Đặt Thông Số Biến Tần – 12 Thông Số Cơ Bản Cần Cài Đầu Tiên
META (156)  : Hướng dẫn cài đặt biến tần từ đầu: reset về mặc định, khai báo động cơ, chọn nguồn lệnh, đặt tần số, tăng giảm tốc và auto-tune. Kèm bảng thông số và lỗi hay gặp.

H1          : Cài Đặt Thông Số Biến Tần Từ Đầu

---

## Vì sao phải cài đặt thông số trước khi chạy?

Biến tần xuất xưởng với một bộ **thông số mặc định của nhà sản xuất**. Bộ thông số đó được đặt cho một động cơ giả định "trung bình", một cách điều khiển giả định và một kiểu tải giả định. Hệ thống thực tế của bạn gần như chắc chắn khác.

Chạy biến tần với thông số mặc định thường dẫn tới một trong các kết quả sau:

- **Lỗi quá dòng ngay khi khởi động** vì thời gian tăng tốc mặc định quá ngắn so với quán tính tải.
- **Bảo vệ quá tải không hoạt động đúng** vì biến tần đang bảo vệ theo dòng của một động cơ khác.
- **Nút Run trên bàn phím không chạy được** vì nguồn lệnh mặc định là đầu vào số, hoặc ngược lại — chân điều khiển đã đấu mà biến tần vẫn chỉ nhận lệnh từ bàn phím.
- **Động cơ yếu, rung, kêu** vì tỷ số V/f không phù hợp.
- **Tần số không lên quá 50Hz** dù ứng dụng cần cao hơn, hoặc ngược lại — chạy vọt lên tần số nguy hiểm cho tải.

Việc cài đặt không phức tạp. Với **khoảng 10–12 thông số**, hầu hết ứng dụng công nghiệp phổ thông đã chạy đúng và an toàn. Phần còn lại trong quyển sách hướng dẫn dày cộp chỉ cần đến khi có yêu cầu đặc biệt.

> **Vừa mua biến tần và chưa biết bắt đầu từ đâu?** Gửi **model biến tần · nhãn động cơ · mô tả tải** → [Nhận bộ thông số gợi ý](#bao-gia).

Đây là bài **18/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Nguyên lý: hiểu cách biến tần tổ chức thông số

Mọi biến tần, dù của hãng nào, đều tổ chức thông số theo cùng một logic. Nắm được logic này thì đọc tài liệu hãng nào cũng nhanh.

**Nhóm thông số được đánh mã** dạng chữ + số (P0-xx, F0-xx, b0-xx, Pr.xx… tùy hãng), chia thành các khối chức năng:

- **Khối cơ bản** — nguồn lệnh, nguồn đặt tần số, tần số giới hạn, thời gian tăng/giảm tốc.
- **Khối động cơ** — công suất, điện áp, dòng, tần số, tốc độ định mức, số cực.
- **Khối V/f và điều khiển** — chọn kiểu điều khiển, đường cong V/f, mô-men khởi động.
- **Khối đầu vào/ra số (DI/DO)** — gán chức năng cho từng chân.
- **Khối đầu vào/ra tương tự (AI/AO)** — chọn 0–10V hay 4–20mA, hiệu chỉnh thang.
- **Khối bảo vệ** — quá tải, quá nhiệt, mất pha, xử lý khi có lỗi.
- **Khối truyền thông** — địa chỉ Modbus, tốc độ baud, định dạng khung.
- **Khối ứng dụng** — PID, đa cấp tốc độ, chức năng bơm/quạt.

**Ba khái niệm cần phân biệt:**

1. **Nguồn lệnh chạy/dừng** — biến tần nhận lệnh Run/Stop từ đâu: bàn phím, chân điều khiển, hay truyền thông.
2. **Nguồn đặt tần số** — giá trị tần số lấy từ đâu: biến trở trên bàn phím, đầu vào analog, truyền thông, hay giá trị cố định trong thông số.
3. **Chế độ điều khiển** — V/f hay vector ([xem so sánh chi tiết](/che-do-dieu-khien-vf-vector/)).

Ba thứ này **độc lập với nhau**. Rất nhiều ca "biến tần không chạy" chỉ là do cài đúng một cái mà quên cái còn lại — ví dụ cài nguồn lệnh là chân điều khiển nhưng vẫn để nguồn đặt tần số là bàn phím, rồi thắc mắc vì sao vặn biến trở ngoài không ăn.

---

## Cấu tạo bộ thông số: 12 thông số cơ bản

Đây là danh sách theo **thứ tự nên cài**. Mã thông số khác nhau giữa các hãng, nhưng ý nghĩa thì giống nhau — hãy tra tên tiếng Anh trong sách hướng dẫn của bạn.

| # | Thông số | Tên thường gặp | Ghi chú khi đặt |
|---|---|---|---|
| 0 | **Reset về mặc định** | Restore factory / Parameter init | **Luôn làm đầu tiên** với máy cũ hoặc máy không rõ lịch sử |
| 1 | Công suất động cơ | Motor rated power | Lấy từ **nhãn động cơ**, không phải nhãn biến tần |
| 2 | Điện áp động cơ | Motor rated voltage | 380V / 220V theo đấu nối thực tế |
| 3 | Dòng định mức động cơ | Motor rated current | Quyết định ngưỡng bảo vệ quá tải |
| 4 | Tần số định mức | Motor rated frequency | Thường 50Hz |
| 5 | Tốc độ định mức | Motor rated speed | rpm trên nhãn, dùng để tính trượt |
| 6 | Nguồn lệnh chạy/dừng | Run command source | Bàn phím · chân DI · truyền thông |
| 7 | Nguồn đặt tần số | Frequency source | Bàn phím · AI · truyền thông · đa cấp |
| 8 | Tần số lớn nhất | Max frequency | Giới hạn cứng — đặt theo giới hạn cơ khí của tải |
| 9 | Tần số trên / dưới | Upper / lower limit | Chặn vùng tốc độ không được phép |
| 10 | Thời gian tăng tốc | Acceleration time | [Xem bài chuyên sâu](/cai-tang-giam-toc-bien-tan/) |
| 11 | Thời gian giảm tốc | Deceleration time | Quá ngắn → lỗi quá áp |
| 12 | Chế độ điều khiển | Control mode | V/f cho tải đơn giản; vector khi cần mô-men thấp tốc |

Sau 12 thông số này, tùy ứng dụng mà bổ sung:

- **Gán chức năng chân DI** nếu điều khiển bằng nút ngoài hoặc [PLC](/dieu-khien-bien-tan-bang-plc/).
- **Cấu hình AI** (0–10V hay 4–20mA) nếu đặt tần số bằng tín hiệu analog ([xem đấu điều khiển](/dau-dieu-khien-bien-tan/)).
- **Thông số PID** nếu chạy vòng kín ([xem điều khiển PID](/dieu-khien-pid-bang-bien-tan/)).
- **Thông số truyền thông** nếu điều khiển qua Modbus.

---

## Ứng dụng: quy trình cài đặt 8 bước

**Bước 1 — Ngắt kết nối cơ khí nếu có thể.** Với thiết bị mới hoặc động cơ chưa rõ, nên tháo khớp nối để chạy thử không tải trước. Nếu không tháo được thì ít nhất phải đảm bảo tải quay được an toàn theo cả hai chiều.

**Bước 2 — Reset về mặc định.** Bắt buộc với biến tần cũ, biến tần mua lại, hoặc máy đã có người khác cài. Bước này loại bỏ toàn bộ thông số lạ mà bạn không biết tồn tại. Sau khi reset, biến tần thường yêu cầu tắt nguồn và bật lại.

**Bước 3 — Khai báo động cơ.** Đọc **nhãn động cơ** và nhập chính xác: công suất, điện áp, dòng, tần số, tốc độ. Đây là bước quan trọng nhất về mặt bảo vệ — biến tần dựa vào các con số này để tính ngưỡng quá tải và mô hình động cơ.

Lưu ý: nếu động cơ đấu sao hay tam giác khác nhau thì điện áp và dòng khai báo cũng khác. Hãy khai theo **cách đấu thực tế trong hộp cực**.

**Bước 4 — Chọn nguồn lệnh và nguồn đặt tần số.** Quyết định trước bạn sẽ vận hành bằng gì:

- Chạy thử bằng bàn phím → cả hai đặt là "bàn phím".
- Nút Start/Stop ngoài + biến trở → nguồn lệnh là DI, nguồn tần số là AI.
- Điều khiển từ PLC qua Modbus → cả hai đặt là "truyền thông".

**Bước 5 — Đặt giới hạn tần số.** Tần số lớn nhất phải phù hợp giới hạn cơ khí. Chạy vượt tần số định mức nghĩa là **vượt tốc độ thiết kế của tải** — nguy hiểm với quạt, bơm ly tâm và hộp số. Tần số nhỏ nhất nên đặt đủ cao để động cơ còn quạt mát được chính nó, trừ khi có quạt cưỡng bức.

**Bước 6 — Đặt thời gian tăng/giảm tốc.** Bắt đầu với giá trị **rộng rãi** (dài hơn cần thiết), chạy thử, rồi rút ngắn dần cho đến khi gần chạm ngưỡng báo lỗi thì lùi lại một chút.

**Bước 7 — Chạy auto-tune nếu dùng chế độ vector.** Auto-tune để biến tần đo các tham số điện của động cơ (điện trở stator, điện cảm…). Có hai kiểu:

- **Tĩnh (static)** — động cơ không quay, làm được khi tải đã lắp.
- **Động (rotating)** — động cơ quay tự do, cho kết quả chính xác hơn nhưng **phải tháo tải**.

Với chế độ V/f đơn giản, thường không cần auto-tune.

**Bước 8 — Chạy thử và ghi lại.** Chạy từ tần số thấp lên cao, quan sát dòng, tiếng động cơ, độ rung. Sau khi chạy ổn định, **ghi lại toàn bộ thông số đã thay đổi** vào một bảng lưu cùng hồ sơ máy, hoặc dùng chức năng sao lưu thông số của bàn phím nếu có.

Bước 8 hay bị bỏ qua nhất, và là bước tốn kém nhất khi cần làm lại: một năm sau, khi biến tần hỏng và phải thay mới, không ai nhớ đã cài gì.

---

## So sánh: chạy mặc định, cài cơ bản và cài đầy đủ

| Mức độ | Việc phải làm | Phù hợp với | Rủi ro còn lại |
|---|---|---|---|
| **Chạy mặc định** | Không cài gì, cấp nguồn và bấm Run | Chỉ để kiểm tra biến tần còn sống | Bảo vệ sai, dễ lỗi quá dòng/quá áp, không dùng được chân ngoài |
| **Cài cơ bản (12 thông số)** | Reset, khai báo động cơ, nguồn lệnh, giới hạn, tăng/giảm tốc | **Đa số ứng dụng bơm, quạt, băng tải** | Chưa tối ưu tiết kiệm điện, chưa có PID |
| **Cài đầy đủ** | Thêm DI/DO, AI/AO, PID, truyền thông, đa cấp tốc độ, tiết kiệm năng lượng | Dây chuyền có PLC/SCADA, hệ vòng kín | Cần thời gian và hiểu hệ thống |

Với phần lớn khách hàng, **mức "cài cơ bản" là điểm dừng hợp lý**: an toàn, chạy đúng, và không phát sinh thời gian không cần thiết. Chỉ leo lên mức đầy đủ khi ứng dụng thực sự yêu cầu — ví dụ [bơm giữ áp](/bien-tan-cho-bom-nuoc/) cần PID, hay dây chuyền cần đồng bộ nhiều biến tần.

---

## Sai lầm thường gặp

1. **Không reset về mặc định** khi dùng biến tần cũ — thông số lạ còn sót gây hành vi khó hiểu.
2. **Khai báo dòng động cơ theo nhãn biến tần.** Bảo vệ quá tải mất tác dụng hoàn toàn nếu biến tần lớn hơn động cơ nhiều.
3. **Nhầm nguồn lệnh với nguồn đặt tần số** — cài một cái quên cái kia.
4. **Đặt tần số lớn nhất quá cao** mà không kiểm tra giới hạn cơ khí của tải.
5. **Đặt tần số nhỏ nhất quá thấp** khiến động cơ chạy lâu ở tốc độ thấp, tự làm mát kém, nóng dần.
6. **Chạy auto-tune động khi tải vẫn lắp** — nguy hiểm và kết quả sai.
7. **Rút ngắn thời gian tăng tốc quá mức** để "máy nhanh hơn" rồi liên tục bị [lỗi quá dòng](/loi-qua-dong-bien-tan/).
8. **Không ghi lại thông số** — mất toàn bộ khi thay máy.
9. **Cài thông số khi động cơ đang chạy** — một số thông số chỉ nhận khi dừng, dẫn tới tưởng đã cài mà thực ra chưa.
10. **Khóa thông số rồi quên mã khóa.** Nhiều biến tần có thông số khóa ghi; hãy lưu lại mã đã đặt.

---

## Cam kết tại HOANTRANTDH

- ✅ **Cài đặt sẵn thông số cơ bản** theo nhãn động cơ khách gửi trước khi giao hàng.
- ✅ Hỗ trợ **hướng dẫn cài đặt từ xa** qua Zalo, có hình ảnh và video minh họa.
- ✅ Cung cấp **bảng thông số đã cài** để khách lưu hồ sơ máy.
- ✅ Hỗ trợ tích hợp với [PLC](/plc-la-gi/), HMI và hệ giám sát sẵn có.

---

<a name="bao-gia"></a>
## Nhận hỗ trợ cài đặt & báo giá

Gửi cho chúng tôi: **ảnh nhãn động cơ · model biến tần · mô tả tải (bơm, quạt, băng tải, máy…) · cách vận hành mong muốn (bàn phím, nút ngoài, biến trở, PLC).**

**→ [Liên hệ nhận hỗ trợ cài đặt](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cài đặt biến tần cần bao nhiêu thông số?**
Khoảng **10–12 thông số cơ bản** là đủ cho đa số ứng dụng: khai báo động cơ, nguồn lệnh, nguồn đặt tần số, giới hạn tần số và thời gian tăng/giảm tốc.

**Có nên reset biến tần về mặc định trước khi cài không?**
**Nên**, đặc biệt với biến tần cũ hoặc không rõ lịch sử. Reset loại bỏ các thông số lạ mà bạn không biết đang tồn tại.

**Khai báo dòng động cơ theo nhãn nào?**
Theo **nhãn động cơ**, đúng với cách đấu sao hay tam giác thực tế — không lấy theo nhãn biến tần.

**Auto-tune có bắt buộc không?**
Không bắt buộc với chế độ **V/f**. Với chế độ **vector**, auto-tune giúp mô-men thấp tốc và độ chính xác tốt hơn rõ rệt.

**Vì sao bấm Run trên bàn phím mà biến tần không chạy?**
Thường do **nguồn lệnh đang đặt là chân điều khiển hoặc truyền thông**. Đổi nguồn lệnh sang bàn phím, hoặc cấp đúng tín hiệu vào chân DI.

**Vì sao vặn biến trở ngoài mà tần số không đổi?**
Vì **nguồn đặt tần số** chưa được chuyển sang đầu vào analog, hoặc kiểu tín hiệu AI chưa khớp (0–10V so với 4–20mA).

**Đặt tần số lớn nhất bao nhiêu là an toàn?**
Theo **giới hạn cơ khí của tải**, không theo mong muốn chạy nhanh. Vượt tần số định mức là vượt tốc độ thiết kế của bơm, quạt hoặc hộp số.

**Làm sao lưu lại thông số đã cài?**
Dùng **chức năng sao lưu của bàn phím** nếu có, đồng thời ghi tay vào bảng và lưu cùng hồ sơ máy để dùng khi thay thiết bị.

<!-- SCHEMA: HowTo + FAQPage + BreadcrumbList. INTERNAL LINK: /bien-tan-la-gi/, /che-do-dieu-khien-vf-vector/, /cai-tang-giam-toc-bien-tan/, /dau-dieu-khien-bien-tan/, /dieu-khien-bien-tan-bang-plc/, /dieu-khien-pid-bang-bien-tan/, /bien-tan-cho-bom-nuoc/, /loi-qua-dong-bien-tan/, /plc-la-gi/, /lien-he/. -->
