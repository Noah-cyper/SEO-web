<!--
LOẠI TRANG : Bài hướng dẫn (chuỗi biến tần — tầng 2) — Thông tin + thương mại
URL SLUG   : /chon-cong-suat-bien-tan/
TỪ KHÓA    : chọn công suất biến tần | tính công suất biến tần | dòng định mức biến tần | derating biến tần | biến tần bao nhiêu kw
INTENT     : Thông tin → thương mại
TRẠNG THÁI : Sẵn đăng. Bài 8/30. Ví dụ tính toán minh hoạ.
-->

TITLE TAG   : Chọn Công Suất Biến Tần – Tính Theo Dòng, Loại Tải Và Derating
META (156)  : Cách chọn công suất biến tần chuẩn: vì sao phải chọn theo dòng (A) chứ không chỉ kW, phân biệt tải nhẹ và tải nặng, hệ số derating theo nhiệt độ, độ cao và ví dụ tính cụ thể.
H1          : Chọn Công Suất Biến Tần – Tính Đúng Ngay Từ Đầu

---

## Sai lầm phổ biến nhất: chọn theo kW

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bien-tan.svg)


Câu hỏi thường gặp nhất khi mua biến tần là: *"Động cơ 7,5 kW thì mua biến tần 7,5 kW đúng không?"*

Câu trả lời: **chưa chắc**. Và đây chính là sai lầm gây ra phần lớn các ca biến tần liên tục báo quá tải hoặc chết sớm.

Lý do rất đơn giản: **kW là công suất cơ ở đầu trục động cơ**, còn thứ mà biến tần thực sự phải chịu là **dòng điện chạy qua các van IGBT**. Hai động cơ cùng 7,5 kW nhưng khác hãng, khác số cực, khác hiệu suất và hệ số công suất có thể có **dòng định mức chênh nhau đáng kể**.

Nguyên tắc đúng:

> **Dòng định mức của biến tần phải lớn hơn hoặc bằng dòng định mức của động cơ**, xét ở đúng cột tải tương ứng.

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-affinity.svg)


> **Cần tính giúp công suất cho máy của bạn?** Gửi **ảnh nhãn động cơ · loại tải · nhiệt độ tủ** → [Nhận tính toán](#bao-gia).

Đây là bài **8/30** trong [chuỗi bài biến tần](/bien-tan-la-gi/).

---

## Cấu tạo bài toán: ba con số cần đối chiếu

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-vfd-sizing.svg)


Khi mở catalogue biến tần, bạn sẽ thấy mỗi model có nhiều dòng số. Ba con số quan trọng nhất:

| Thông số trong catalogue | Ý nghĩa | Cách dùng |
|---|---|---|
| **Công suất động cơ áp dụng (kW)** | Gợi ý sơ bộ | Chỉ dùng để khoanh vùng |
| **Dòng định mức đầu ra (A)** | Dòng biến tần chịu liên tục | **So sánh với dòng động cơ** |
| **Khả năng quá tải** | VD 150% trong 60 giây | Quyết định chịu được khởi động nặng không |

Nhiều catalogue còn tách thành **hai cột**:
- **ND / Tải nhẹ (Normal Duty)** — cho bơm, quạt. Quá tải thường thấp hơn (VD 120%/60s).
- **HD / Tải nặng (Heavy Duty)** — cho băng tải, máy ép. Quá tải cao hơn (VD 150%/60s), nhưng **dòng định mức thấp hơn** trên cùng một model.

Nghĩa là **cùng một biến tần** có thể được gọi là "11 kW" khi dùng cho bơm quạt, nhưng chỉ "7,5 kW" khi dùng cho băng tải. Đọc nhầm cột là lỗi kinh điển.

---

## Quy trình 5 bước tính công suất

### Bước 1 — Lấy dòng định mức của động cơ

Đọc trên nhãn động cơ, **chọn đúng giá trị ứng với cách đấu** mà bạn sẽ dùng. Nhãn ghi kiểu "220/380V — 20/11,6A" nghĩa là: đấu tam giác 220V thì 20A, đấu sao 380V thì 11,6A.

Nếu chạy biến tần 3 pha 380V → động cơ đấu sao → lấy **11,6A**. [Xem hướng dẫn đọc nhãn →](/bien-tan-va-dong-co-3-pha/)

### Bước 2 — Xác định nhóm tải

| Nhóm | Ví dụ | Cột catalogue dùng |
|---|---|---|
| Bậc ba (nhẹ) | Bơm ly tâm, quạt | **ND / tải nhẹ** |
| Mô-men không đổi | Băng tải, máy trộn, máy nén piston | **HD / tải nặng** |
| Va đập | Máy nghiền, máy cán | **HD** + dư thêm |

### Bước 3 — Tra dòng biến tần ở đúng cột

Tìm model có **dòng định mức ≥ dòng động cơ** ở cột tương ứng nhóm tải.

### Bước 4 — Áp hệ số dự phòng theo điều kiện

| Điều kiện | Hệ số nên cộng thêm |
|---|---|
| Tải nhóm mô-men không đổi | Dư **1 cấp** |
| Tải va đập, khởi động nặng | Dư **1 cấp** trở lên |
| Khởi động nhiều lần/giờ | Dư 1 cấp |
| Chạy tần số thấp kéo dài với tải nặng | Cân nhắc dư |
| Nhiều động cơ chạy chung 1 biến tần | Cộng dòng các động cơ **rồi dư thêm** |

### Bước 5 — Áp hệ số derating theo môi trường

Đây là bước hay bị quên. Catalogue công bố dòng định mức ở **điều kiện chuẩn** (thường 40 °C, độ cao dưới 1000 m). Vượt điều kiện đó, khả năng chịu tải **giảm xuống**:

| Yếu tố | Ảnh hưởng |
|---|---|
| **Nhiệt độ môi trường vượt chuẩn** | Giảm dòng cho phép theo mỗi độ tăng |
| **Độ cao trên 1000 m** | Không khí loãng, tản nhiệt kém → giảm dòng |
| **Tần số sóng mang đặt cao** | IGBT nóng hơn → giảm dòng cho phép |
| **Lắp sát nhau nhiều biến tần trong tủ** | Nhiệt cộng hưởng → cần khoảng cách và thông gió |

Hệ số cụ thể **khác nhau theo từng hãng và model** — phải tra bảng derating trong tài liệu kỹ thuật của model đang chọn.

---

## Ví dụ minh hoạ

### Ví dụ 1 — Bơm ly tâm

- Động cơ: **7,5 kW, 380V, 15,5A** (đấu sao)
- Tải: bơm ly tâm → **nhóm tải nhẹ**
- Nhiệt độ tủ: khoảng 40 °C, có quạt thông gió
- **Chọn:** biến tần có dòng định mức **cột ND ≥ 15,5A** → thường là model ghi 7,5 kW
- **Kết luận:** chọn đúng cấp là đủ, không cần dư

### Ví dụ 2 — Băng tải

- Động cơ: **7,5 kW, 380V, 15,5A**
- Tải: băng tải → **mô-men không đổi**, khởi động có tải
- **Chọn:** tra ở **cột HD**. Model "7,5 kW ND" có thể chỉ còn khoảng 5,5 kW ở cột HD → **phải lên model cao hơn một cấp** (11 kW ND / 7,5 kW HD)
- **Kết luận:** cùng một động cơ nhưng vì tải nặng nên phải mua biến tần lớn hơn một cấp

### Ví dụ 3 — Tủ nóng

- Động cơ: **15 kW, 380V, 30A**, tải quạt
- Nhiệt độ trong tủ đo được khoảng **50 °C** (vượt chuẩn 40 °C)
- **Chọn:** phải áp hệ số derating → dòng khả dụng của biến tần giảm → **chọn model có dòng cao hơn**, hoặc **cải thiện thông gió tủ** để đưa nhiệt độ về mức chuẩn

Ví dụ 3 cho thấy một điều quan trọng: **nhiều khi giải pháp rẻ hơn là cải thiện tủ điện chứ không phải mua biến tần to hơn**. [Xem hướng dẫn lắp tủ →](/lap-bien-tan-trong-tu-dien/)

---

## Ứng dụng: các tình huống đặc biệt

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-vfd-bangtai.svg)


**Một biến tần chạy nhiều động cơ.** Chỉ làm được với chế độ **V/f** (không dùng vector). Phải **cộng dòng của tất cả động cơ** rồi cộng thêm dự phòng. Ngoài ra mỗi động cơ **cần rơ-le nhiệt riêng**, vì bảo vệ quá tải của biến tần chỉ nhìn thấy tổng dòng, không biết động cơ nào đang quá tải.

**Động cơ nhỏ hơn nhiều so với biến tần.** Nếu biến tần quá lớn so với động cơ, cảm biến dòng khó đo chính xác ở mức thấp, chế độ vector hoạt động kém và bảo vệ quá tải không nhạy. Nên tránh chênh lệch quá 2 cấp.

**Thay biến tần cũ đã hỏng.** Đừng mua theo đúng model cũ một cách máy móc — hãy kiểm tra lại: động cơ có còn nguyên không, tải có thay đổi không, biến tần cũ có bị chọn thiếu ngay từ đầu (nên mới hỏng) không.

**Máy đã có sẵn nhưng hay báo quá tải.** Trước khi kết luận thiếu công suất, hãy kiểm tra: thời gian tăng tốc quá ngắn, cơ khí bị kẹt, cài sai thông số động cơ. Nhiều trường hợp là do cấu hình chứ không phải phần cứng. [Xem xử lý lỗi quá tải →](/loi-qua-nhiet-qua-tai-bien-tan/)

---

## So sánh: chọn vừa đủ hay chọn dư?

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-vfd-tai.svg)


| Tiêu chí | **Chọn vừa đủ** | **Chọn dư 1 cấp** |
|---|---|---|
| Chi phí đầu tư | Thấp hơn | Cao hơn |
| Khả năng chịu khởi động nặng | Hạn chế | **Tốt** |
| Biên an toàn khi tủ nóng | Ít | **Nhiều** |
| Hiệu suất khi chạy tải thấp | Tốt hơn | Kém hơn một chút |
| Rủi ro báo quá tải | Cao hơn | **Thấp** |
| Khả năng nâng cấp tải sau này | Hạn chế | **Linh hoạt** |

**Nguyên tắc:** với **bơm quạt trong tủ mát**, chọn vừa đủ là hợp lý và tiết kiệm. Với **tải nặng, môi trường nóng bụi, hoặc khởi động nhiều**, dư một cấp gần như luôn đáng giá — chi phí chênh lệch nhỏ hơn nhiều so với thiệt hại khi dừng máy.

Ngược lại, **dư quá nhiều (2–3 cấp) không phải là tốt hơn**: tốn tiền, chiếm chỗ, và điều khiển kém chính xác ở tải thấp.

---

## Kiểm chứng lại lựa chọn sau khi lắp

Chọn công suất trên giấy chỉ là bước đầu. Sau khi lắp xong, hãy dành mười phút để xác nhận lựa chọn là đúng — việc này rẻ hơn rất nhiều so với phát hiện sai vào mùa cao điểm.

**Bốn phép đo cần làm trong tuần đầu vận hành:**

1. **Đo dòng thực tế khi chạy ở chế độ nặng nhất** bằng ampe kìm, so với dòng định mức biến tần. Nếu dòng làm việc thường xuyên nằm gần sát ngưỡng, bạn đang không còn biên dự phòng nào cho ngày nóng hoặc khi tải nặng hơn.
2. **Đo dòng lúc khởi động.** Đây là thời điểm dòng cao nhất. Nếu biến tần chạm ngưỡng ngay ở bước này, hoặc là thời gian tăng tốc quá ngắn, hoặc là công suất chọn thiếu thật.
3. **Đọc nhiệt độ tản nhiệt** trên màn hình biến tần sau khi máy chạy ổn định vài giờ, vào **thời điểm nóng nhất trong ngày**. Nhiệt độ cao ngay từ đầu mùa mát là dấu hiệu sẽ có sự cố khi vào mùa nóng.
4. **Kiểm tra dòng ba pha có cân nhau không.** Lệch đáng kể cho thấy vấn đề ở đấu nối hoặc ở động cơ, không phải ở việc chọn công suất.

**Ghi lại các con số này vào hồ sơ máy.** Chúng trở thành mốc so sánh: sáu tháng sau, nếu dòng ở cùng chế độ vận hành đã tăng lên đáng kể, đó là dấu hiệu sớm của hỏng hóc cơ khí — vòng bi mòn, dây curoa quá căng, khớp nối lệch tâm — chứ không phải biến tần yếu đi.

Một lưu ý cuối: nếu sau khi đo bạn phát hiện đã chọn thiếu, **đừng cố xoay xở bằng cách nâng ngưỡng bảo vệ**. Đó là cách nhanh nhất để hỏng cả biến tần lẫn động cơ. Hãy đổi lên một cấp công suất, hoặc xem lại xem tải có vấn đề cơ khí gì không.

---

## Sai lầm thường gặp

1. **Chỉ so kW mà không so dòng (A).**
2. **Đọc nhầm cột tải nhẹ / tải nặng.**
3. **Quên derating khi tủ nóng hoặc lắp ở vùng cao.**
4. **Lấy dòng ở cách đấu sai** (lấy dòng tam giác 220V trong khi thực tế đấu sao 380V).
5. **Chạy nhiều động cơ mà chỉ cộng kW, không cộng dòng và không lắp rơ-le nhiệt riêng.**
6. **Chọn theo công suất máy bơm ghi trên catalogue máy**, thay vì theo nhãn động cơ thực tế đang lắp.
7. **Giả định biến tần lớn hơn thì luôn tốt hơn.**

---

## Cam kết tại HOANTRANTDH

- ✅ **Tính công suất theo dòng và loại tải thật**, không bán theo cảm tính.
- ✅ Kiểm tra điều kiện tủ điện để tư vấn derating hợp lý.
- ✅ Nói rõ khi nào **nên cải thiện thông gió tủ** thay vì mua biến tần lớn hơn.
- ✅ Hàng chính hãng, CO/CQ, hoá đơn VAT; hỗ trợ cài đặt và nghiệm thu.

---

<a name="bao-gia"></a>
## Nhận tính toán & báo giá

Gửi: **ảnh nhãn động cơ (rõ dòng và điện áp) · loại tải · số lần khởi động mỗi giờ · nhiệt độ trong tủ · độ cao lắp đặt.**

**→ [Liên hệ nhận tư vấn chọn công suất](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Động cơ 7,5 kW thì mua biến tần 7,5 kW được không?**
Chỉ khi tải là **bơm/quạt** và dòng biến tần ở cột tải nhẹ ≥ dòng động cơ. Với **băng tải hoặc tải nặng**, thường phải lên **một cấp**.

**Vì sao phải chọn theo dòng chứ không theo kW?**
Vì biến tần chịu **dòng điện**, mà cùng một mức kW thì dòng có thể khác nhau giữa các động cơ.

**Cột ND và HD trong catalogue nghĩa là gì?**
**ND (Normal Duty)** cho tải nhẹ như bơm quạt; **HD (Heavy Duty)** cho tải nặng, có khả năng quá tải cao hơn nhưng dòng định mức thấp hơn trên cùng model.

**Derating là gì?**
Là việc **giảm dòng cho phép** khi điều kiện vận hành khắc nghiệt hơn chuẩn — nhiệt độ cao, độ cao lớn, tần số sóng mang cao.

**Một biến tần chạy được mấy động cơ?**
Được, nhưng phải dùng **chế độ V/f**, **cộng dòng tất cả động cơ** cộng dự phòng, và **mỗi động cơ cần rơ-le nhiệt riêng**.

**Chọn biến tần lớn hơn nhiều có sao không?**
Tốn chi phí và **điều khiển kém chính xác ở tải thấp**; bảo vệ quá tải cũng kém nhạy. Không nên chênh quá 2 cấp.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cach-chon-bien-tan/, /bien-tan-va-dong-co-3-pha/, /lap-bien-tan-trong-tu-dien/, /loi-qua-nhiet-qua-tai-bien-tan/, /lien-he/. -->
