<!--
LOẠI TRANG : Bài công nghệ — chuỗi cảm biến lưu lượng — tầng 2
URL SLUG   : /cam-bien-luu-luong-sieu-am/
TỪ KHÓA    : cảm biến lưu lượng siêu âm | đồng hồ siêu âm kẹp ngoài | clamp on flow meter | transit time | doppler
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng. Bài 7/20 trong chuỗi cảm biến lưu lượng.
-->

TITLE TAG   : Cảm Biến Lưu Lượng Siêu Âm – Kẹp Ngoài Ống, Không Cần Cắt Ống
META (156)  : Cảm biến siêu âm đo lưu lượng không cần cắt ống. Phân biệt transit-time và Doppler, điều kiện để đo chính xác, cách lắp đầu dò và các lỗi hay gặp.

H1          : Cảm Biến Lưu Lượng Siêu Âm

---

## Công nghệ duy nhất đo được mà không đụng vào đường ống

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-sieu-am-clamp.svg)


Mọi công nghệ đo lưu lượng khác đều đòi hỏi một điều: **cắt đường ống ra và lắp thiết bị vào**. Với một dây chuyền đang sản xuất, điều đó nghĩa là dừng máy, xả nước, cắt, hàn, thử áp — một dự án nhỏ.

**Cảm biến siêu âm kẹp ngoài (clamp-on)** là ngoại lệ. Hai đầu dò kẹp bên ngoài thành ống, sóng âm xuyên qua thành ống vào môi chất và trở ra. Toàn bộ quá trình lắp đặt mất chưa tới một giờ, **không đụng vào đường ống, không dừng sản xuất, không một giọt nước chảy ra**.

Từ đặc điểm này sinh ra hai nhóm ứng dụng mà siêu âm gần như không có đối thủ:

**1. Đo trên hệ đang chạy không được dừng.** Đường ống cấp nước chính, hệ làm mát của lò, đường ống trong nhà máy hoạt động liên tục.

**2. Đo tạm thời để khảo sát.** Một thiết bị xách tay có thể đo hôm nay ở điểm A, mai ở điểm B, tuần sau ở nhà máy khác. Rất giá trị cho kiểm toán năng lượng, kiểm tra chéo đồng hồ khác, và chẩn đoán sự cố.

Đổi lại, siêu âm có những điều kiện riêng — và hiểu chúng là điều kiện để dùng thành công.

> **Cần đo lưu lượng mà không được cắt ống?** Gửi **vật liệu và đường kính ống · môi chất** → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-transit-time.svg)


Đây là bài **7/20** trong [chuỗi cảm biến lưu lượng](/cam-bien-luu-luong-la-gi/).

---

## Nguyên lý: hai công nghệ rất khác nhau dưới cùng một tên

Điều gây nhầm lẫn nhất về siêu âm là **có hai nguyên lý hoàn toàn khác nhau** cùng được gọi là "đồng hồ siêu âm", và chúng phù hợp với **hai loại môi chất trái ngược nhau**.

### Transit-time — chênh lệch thời gian truyền

Đây là loại phổ biến hơn và chính xác hơn.

Hai đầu dò đặt lệch nhau trên ống, mỗi đầu vừa phát vừa thu. Sóng âm được truyền theo hai chiều:

- **Chiều xuôi dòng:** sóng được dòng chảy "đẩy đi", nên tới đích **nhanh hơn**.
- **Chiều ngược dòng:** sóng phải "bơi ngược", nên tới đích **chậm hơn**.

**Chênh lệch giữa hai thời gian truyền tỷ lệ với vận tốc dòng chảy.** Biết vận tốc và tiết diện ống thì tính ra lưu lượng.

Điểm quan trọng: chênh lệch này **cực kỳ nhỏ** — cỡ phần tỷ giây. Điều đó giải thích vì sao thiết bị cần điện tử chính xác cao, và vì sao **mọi yếu tố gây nhiễu đường truyền sóng đều ảnh hưởng tới kết quả**.

**Yêu cầu của transit-time:** môi chất phải **tương đối sạch và trong**, để sóng âm truyền qua được. Quá nhiều bọt khí hoặc hạt rắn sẽ **tán xạ và hấp thụ sóng**, khiến tín hiệu quá yếu.

### Doppler — phản xạ từ hạt lơ lửng

Loại này hoạt động theo nguyên lý ngược lại.

Một đầu dò phát sóng âm vào dòng chảy. Sóng gặp **các hạt rắn hoặc bọt khí đang trôi theo dòng** và phản xạ trở lại. Do các hạt đang chuyển động, **tần số sóng phản xạ bị dịch đi** — đây là hiệu ứng Doppler quen thuộc.

Độ dịch tần tỷ lệ với vận tốc của các hạt, tức là vận tốc dòng chảy.

**Yêu cầu của Doppler — ngược hẳn với transit-time:** môi chất **phải có hạt lơ lửng hoặc bọt khí** để phản xạ sóng. Đo nước quá sạch thì **không có gì phản xạ** và thiết bị không hoạt động.

### Chọn loại nào

| Môi chất | Loại phù hợp |
|---|---|
| **Nước sạch, nước đã xử lý** | **Transit-time** |
| **Nước làm mát, nước tuần hoàn** | Transit-time |
| **Dầu sạch, dung môi** | Transit-time |
| **Nước thải có cặn** | **Doppler** |
| **Bùn loãng** | Doppler |
| **Chất lỏng có nhiều bọt khí** | Doppler |
| **Nước rất sạch (không có hạt)** | **Không dùng được Doppler** |

**Về độ chính xác:** transit-time **chính xác hơn đáng kể** so với Doppler. Doppler thường chỉ dùng khi transit-time không hoạt động được — tức là khi môi chất quá bẩn.

Lưu ý cho môi chất bẩn nói chung: nếu chất lỏng **dẫn điện**, [đồng hồ điện từ](/dong-ho-luu-luong-dien-tu/) thường là lựa chọn tốt hơn cả hai loại siêu âm — chính xác hơn và ổn định hơn. Siêu âm chỉ thắng khi **không được cắt ống**.

---

## Cấu tạo và thông số: điều gì quyết định độ chính xác

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-flow-lapdat.svg)


Với siêu âm kẹp ngoài, **chất lượng lắp đặt quyết định kết quả nhiều hơn chất lượng thiết bị**. Đây là điểm khác biệt lớn nhất so với các công nghệ lắp trong ống.

### Thông tin phải khai báo chính xác

Thiết bị không "nhìn thấy" bên trong ống — nó tính toán dựa trên các con số bạn nhập vào. Nhập sai là kết quả sai, không có cách nào phát hiện tự động.

| Thông tin | Vì sao quan trọng |
|---|---|
| **Đường kính ngoài ống** | Đo thực tế bằng thước dây, không lấy theo danh nghĩa |
| **Độ dày thành ống** | **Quan trọng nhất và hay sai nhất** — nên đo bằng máy đo độ dày siêu âm |
| **Vật liệu ống** | Tốc độ truyền âm mỗi vật liệu khác nhau |
| **Vật liệu và độ dày lớp lót** | Nếu ống có lót |
| **Loại môi chất** | Tốc độ truyền âm trong môi chất |
| **Nhiệt độ môi chất** | Ảnh hưởng tốc độ truyền âm |

**Về độ dày thành ống:** ống thép sau nhiều năm sử dụng có thể mỏng đi do ăn mòn, hoặc dày lên do đóng cặn bên trong. Lấy theo bảng tra danh nghĩa có thể sai đáng kể. **Máy đo độ dày siêu âm** là công cụ nên có khi triển khai loại kẹp ngoài.

### Cách bố trí đầu dò

Có ba kiểu lắp, khác nhau về số lần sóng đi qua ống:

**Kiểu Z (1 lần truyền).** Hai đầu dò đặt **đối diện nhau ở hai phía ống**. Sóng đi thẳng qua một lần.
- Tín hiệu **mạnh nhất** — dùng khi môi chất khó truyền âm, ống lớn, ống bị đóng cặn.
- Độ chính xác thấp hơn vì quãng đường đo ngắn.

**Kiểu V (2 lần truyền).** Hai đầu dò đặt **cùng một phía ống**. Sóng đi qua, phản xạ ở thành đối diện, quay lại.
- **Kiểu phổ biến nhất** — cân bằng giữa tín hiệu và độ chính xác.
- Dễ lắp vì chỉ cần tiếp cận một phía ống.

**Kiểu W (4 lần truyền).** Sóng phản xạ hai lần.
- **Chính xác nhất** — quãng đường đo dài nhất.
- Tín hiệu yếu nhất, chỉ dùng cho **ống nhỏ và môi chất sạch**.

Nguyên tắc: **bắt đầu bằng kiểu V**. Nếu tín hiệu yếu thì chuyển sang Z; nếu ống nhỏ và tín hiệu rất mạnh thì thử W để tăng độ chính xác.

### Chất tiếp âm (couplant)

Giữa mặt đầu dò và thành ống **không được có không khí** — không khí gần như chặn hoàn toàn sóng siêu âm. Vì vậy phải bôi một lớp **gel hoặc mỡ tiếp âm**.

Đây là chi tiết nhỏ nhưng là **nguyên nhân số một khiến thiết bị không bắt được tín hiệu** khi lắp lần đầu.

Với lắp cố định lâu dài, gel thường sẽ khô đi theo thời gian. Cần dùng loại chuyên dụng cho lắp cố định, hoặc kiểm tra và bôi lại định kỳ — nếu không, thiết bị sẽ **mất tín hiệu sau vài tháng** mà không ai hiểu vì sao.

### Chuẩn bị bề mặt ống

Tại hai vị trí đặt đầu dò, bề mặt ống phải:
- **Sạch sơn bong, gỉ, bụi bẩn.**
- **Nhẵn** — mài nhẹ nếu cần.
- **Không có mối hàn, nhãn dán, vết lõm.**

Bỏ qua bước này là nguyên nhân phổ biến thứ hai của việc không bắt được tín hiệu.

---

## Ứng dụng: khi nào siêu âm là lựa chọn đúng

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-flow-nuoc.svg)



<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/comp-flow-clamp-inline.svg)

### Rất phù hợp

- **Đường ống đang vận hành không được dừng** — lý do hàng đầu.
- **Kiểm toán năng lượng, khảo sát hiện trạng** — thiết bị xách tay đo nhiều điểm.
- **Kiểm tra chéo một đồng hồ khác** đang bị nghi ngờ sai.
- **Ống rất lớn** — chi phí siêu âm gần như không tăng theo cỡ ống, trong khi đồng hồ inline tăng rất nhanh.
- **Môi chất ăn mòn mạnh** — không có bộ phận nào tiếp xúc môi chất.
- **Cần đo nhưng ngân sách chỉ cho phép thuê thiết bị** thay vì mua lắp cố định.
- **Chất lỏng không dẫn điện** (dầu sạch) — nơi điện từ không dùng được.

### Không phù hợp

- **Ống nhựa mỏng hoặc ống có lớp lót dày** — sóng bị suy giảm mạnh.
- **Ống bê tông, ống có lớp bọc cách nhiệt không tháo được.**
- **Môi chất có rất nhiều bọt khí** — transit-time mất tín hiệu.
- **Nước quá sạch** — Doppler không có gì để phản xạ.
- **Ống bị đóng cặn dày bên trong** — làm sai tiết diện thực và cản sóng.
- **Yêu cầu độ chính xác cao cho mua bán** — nên dùng loại lắp trong ống.
- **Ống không đầy** — như mọi công nghệ khác.

### Lắp tạm hay lắp cố định

| | **Xách tay / tạm thời** | **Lắp cố định** |
|---|---|---|
| Mục đích | Khảo sát, kiểm tra, chẩn đoán | Giám sát liên tục |
| Đầu dò | Kẹp bằng dây đai, tháo được | Kẹp cố định, bọc bảo vệ |
| Couplant | Gel thường | **Loại chuyên dụng lâu dài** |
| Nguồn | Pin | Nguồn cố định |
| Chi phí | Một thiết bị dùng nhiều điểm | Mỗi điểm một bộ |
| Rủi ro chính | — | **Khô couplant, lệch đầu dò theo thời gian** |

**Lời khuyên thực dụng:** nếu chỉ cần biết lưu lượng ở vài điểm trong vài ngày, **thuê hoặc mua một thiết bị xách tay** là phương án kinh tế nhất. Chỉ lắp cố định khi thực sự cần giám sát liên tục.

### Quy trình lắp đặt

1. **Chọn vị trí** có đủ đoạn ống thẳng — siêu âm cần đoạn thẳng đáng kể ([xem bài lắp đặt](/lap-dat-cam-bien-luu-luong/)).
2. **Đảm bảo ống luôn đầy** — ưu tiên đoạn nằm ngang hoặc đi lên.
3. **Đo đường kính ngoài** bằng thước dây quấn quanh ống.
4. **Đo độ dày thành ống** bằng máy đo siêu âm.
5. **Nhập đầy đủ thông số** vào thiết bị: kích thước, vật liệu, lót, môi chất, nhiệt độ.
6. **Thiết bị tính ra khoảng cách đặt hai đầu dò** — đây là con số phải theo đúng.
7. **Làm sạch và mài nhẵn** hai vị trí đặt đầu dò.
8. **Bôi couplant**, đặt đầu dò, kẹp chắc.
9. **Kiểm tra cường độ tín hiệu** trên màn hình — nếu yếu, chỉnh vị trí hoặc đổi kiểu lắp.
10. **Đối chiếu với một nguồn tham chiếu** nếu có — đồng hồ khác, mức bể thay đổi, hoặc lưu lượng bơm đã biết.

Bước 10 rất đáng làm: nó là cách duy nhất phát hiện lỗi nhập sai thông số ống, vì thiết bị vẫn hiển thị một con số trông hoàn toàn hợp lý.

---

## So sánh với các công nghệ khác

| Tiêu chí | **Siêu âm kẹp ngoài** | Điện từ | Coriolis | Tuabin |
|---|---|---|---|---|
| Cắt ống để lắp | **Không** | Có | Có | Có |
| Dừng sản xuất | **Không** | Có | Có | Có |
| Tiếp xúc môi chất | **Không** | Có | Có | Có |
| Độ chính xác | Trung bình | Cao | **Rất cao** | Cao |
| Tổn thất áp | **Không** | **Không** | Có | Có |
| Đo được môi chất không dẫn điện | **Có** | Không | Có | Có |
| Nhạy với bọt khí | **Cao** | Trung bình | Trung bình | Cao |
| Phụ thuộc chất lượng lắp đặt | **Rất cao** | Thấp | Thấp | Trung bình |
| Di chuyển sang điểm khác | **Được** | Không | Không | Không |
| Chi phí theo cỡ ống lớn | **Gần như không tăng** | Tăng nhanh | **Tăng rất nhanh** | Tăng |

**Kết luận:** siêu âm không phải công nghệ chính xác nhất, nhưng nó giải được một bài toán mà các công nghệ khác không giải được — **đo mà không đụng vào ống**. Khi đó là ràng buộc chính, siêu âm là lựa chọn gần như duy nhất.

Khi có thể cắt ống và môi chất dẫn điện, hãy cân nhắc [đồng hồ điện từ](/dong-ho-luu-luong-dien-tu/) — chính xác hơn và ít phụ thuộc vào tay nghề lắp đặt hơn nhiều.

---

## Sai lầm thường gặp

1. **Quên bôi couplant** — không bắt được tín hiệu, nguyên nhân số một khi lắp lần đầu.
2. **Nhập độ dày thành ống theo bảng tra** thay vì đo thực tế — sai số đáng kể.
3. **Không làm sạch, mài nhẵn bề mặt ống** tại vị trí đầu dò.
4. **Đặt đầu dò lên mối hàn hoặc chỗ móp.**
5. **Dùng Doppler cho nước quá sạch** — không có hạt để phản xạ.
6. **Dùng transit-time cho môi chất nhiều bọt** — mất tín hiệu.
7. **Đặt sai khoảng cách giữa hai đầu dò** so với giá trị thiết bị tính ra.
8. **Không đối chiếu với nguồn tham chiếu** sau khi lắp — không phát hiện được lỗi nhập liệu.
9. **Lắp ở đoạn ống có thể không đầy.**
10. **Lắp cố định mà dùng gel thường** — khô sau vài tháng, mất tín hiệu.
11. **Bỏ qua yêu cầu đoạn ống thẳng** vì nghĩ "kẹp ngoài thì lắp đâu cũng được".
12. **Không tính lớp cặn bám trong ống** làm thay đổi tiết diện thực.

---

## Cam kết tại HOANTRANTDH

- ✅ Tư vấn **chọn đúng loại transit-time hay Doppler** theo độ sạch của môi chất.
- ✅ Hướng dẫn **đo và nhập thông số ống chính xác** — yếu tố quyết định kết quả.
- ✅ Tư vấn trung thực khi **đồng hồ điện từ là lựa chọn tốt hơn** nếu bạn có thể cắt ống.
- ✅ Cung cấp cả **thiết bị xách tay để khảo sát** và bộ lắp cố định cho giám sát liên tục.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá cảm biến siêu âm

Gửi cho chúng tôi: **vật liệu, đường kính ngoài và độ dày ống · ống có lớp lót hoặc bọc cách nhiệt không · môi chất và độ sạch (có cặn, có bọt không) · dải lưu lượng · nhiệt độ môi chất · cần đo tạm thời hay lắp cố định · ảnh chụp đoạn ống dự kiến lắp.**

**→ [Liên hệ nhận tư vấn](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cảm biến siêu âm đo lưu lượng thế nào?**
Hai nguyên lý: **transit-time** đo chênh lệch thời gian sóng âm truyền xuôi và ngược dòng; **Doppler** đo độ dịch tần của sóng phản xạ từ các hạt lơ lửng.

**Transit-time và Doppler dùng cho môi chất nào?**
**Transit-time** cho môi chất **tương đối sạch**; **Doppler** cho môi chất **có hạt hoặc bọt khí** để phản xạ. Yêu cầu của chúng ngược nhau.

**Có thật là không cần cắt ống không?**
**Đúng** với loại kẹp ngoài (clamp-on). Đầu dò kẹp bên ngoài thành ống, sóng xuyên qua thành ống. Không dừng sản xuất, không xả nước.

**Vì sao thiết bị không bắt được tín hiệu?**
Ba nguyên nhân phổ biến nhất: **quên bôi couplant**, **bề mặt ống chưa làm sạch và mài nhẵn**, hoặc **đặt sai khoảng cách giữa hai đầu dò**.

**Thông số nào hay nhập sai nhất?**
**Độ dày thành ống.** Ống cũ có thể mỏng đi do ăn mòn hoặc dày lên do đóng cặn — nên đo bằng máy đo độ dày siêu âm thay vì lấy theo bảng tra.

**Kiểu lắp V, Z, W khác nhau thế nào?**
**Z** (1 lần truyền) cho tín hiệu mạnh nhất, dùng khi khó truyền âm. **V** (2 lần) là kiểu phổ biến nhất, cân bằng. **W** (4 lần) chính xác nhất nhưng tín hiệu yếu, chỉ cho ống nhỏ và môi chất sạch.

**Siêu âm có chính xác bằng đồng hồ điện từ không?**
**Thường là không.** Siêu âm kẹp ngoài phụ thuộc rất nhiều vào chất lượng lắp đặt và thông tin ống. Nếu cắt ống được và môi chất dẫn điện, điện từ chính xác và ổn định hơn.

**Lắp cố định có vấn đề gì cần lưu ý?**
**Couplant khô theo thời gian** khiến thiết bị mất tín hiệu sau vài tháng. Cần dùng loại chuyên dụng cho lắp cố định và kiểm tra định kỳ.

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /cam-bien-luu-luong-la-gi/, /nguyen-ly-do-luu-luong/, /dong-ho-luu-luong-dien-tu/, /lap-dat-cam-bien-luu-luong/, /loi-cam-bien-luu-luong/, /cach-chon-cam-bien-luu-luong/, /lien-he/. -->
