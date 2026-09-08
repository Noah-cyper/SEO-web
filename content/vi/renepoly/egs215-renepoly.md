<!--
LOẠI TRANG : Trang sản phẩm (model) — Thương mại
URL SLUG   : /egs215-renepoly/
TỪ KHÓA    : egs215 | egs215 renepoly | tủ lưu trữ 215kwh | bess 100kw 215kwh | tủ bess làm mát chất lỏng
INTENT     : Thương mại + kỹ thuật
TRẠNG THÁI : Sẵn đăng. Đối chiếu datasheet EGS215 bản mới nhất trước khi lên web.
-->

TITLE TAG   : EGS215 Renepoly – Tủ Lưu Trữ 100kW/215kWh Làm Mát Chất Lỏng, IP55
META (156)  : EGS215 Renepoly – tủ BESS tích hợp 100kW/215,04kWh: pin LFP, PCS, EMS, làm mát chất lỏng, PCCC trong một tủ IP55 ngoài trời. Hỗ trợ RS485/TCP, giám sát đám mây. Báo giá theo dự án.
H1          : EGS215 Renepoly – Tủ Lưu Trữ Năng Lượng 100kW / 215kWh

---

## EGS215 là gì?

<!--IMG:rep-->
![Hình đại diện](assets/diagrams/rep-bess-cabinet.svg)


**EGS215** là **tủ lưu trữ năng lượng tích hợp (all-in-one)** của **Renepoly**, cấu hình **100 kW / 215,04 kWh**, sử dụng **làm mát bằng chất lỏng** và đạt cấp bảo vệ **IP55** để lắp đặt ngoài trời.

Toàn bộ một hệ BESS hoàn chỉnh được đóng gói trong một tủ duy nhất: **khối pin LFP kèm BMS**, **PCS chuyển đổi công suất hai chiều**, **EMS điều phối**, **hệ làm mát chất lỏng** và **hệ phòng cháy chữa cháy**. Thiết bị được lắp ráp và chạy thử tại nhà máy, nên tại công trường chỉ cần đặt lên móng, đấu điện và cấu hình vận hành.

> **Cần báo giá EGS215?** Gửi **công suất đỉnh (kW) · số giờ cần bù · mặt bằng lắp đặt · đã có điện mặt trời chưa** → [Nhận tư vấn & báo giá](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-liquid-cooling.svg)


Với tỷ lệ **100 kW trên 215 kWh** (khoảng **0,5C**), EGS215 xả hết dung lượng trong chừng **2 giờ** ở công suất định mức. Đây là cấu hình cân bằng, phù hợp với bài toán phổ biến nhất của nhà máy Việt Nam: **cắt đỉnh phụ tải trong khung giờ cao điểm buổi chiều**.

---

## Thông số kỹ thuật (tham khảo)

<!--IMG:spec-->
![Cấu tạo & thông số](assets/diagrams/spec-cabinet-layout.svg)


| Hạng mục | Giá trị |
|---|---|
| **Công suất định mức** | **100 kW** |
| **Dung lượng** | **215,04 kWh** |
| **C-rate** | Khoảng **0,5C** (xả ~2 giờ ở công suất định mức) |
| **Hoá học pin** | **LFP (LiFePO₄)** — cell an toàn cao |
| **Quản lý nhiệt** | **Làm mát bằng chất lỏng** |
| **Cấp bảo vệ** | **IP55** — lắp ngoài trời |
| **EMS tích hợp** | Có — lập lịch thông minh, nhiều chế độ vận hành, cập nhật từ xa |
| **Truyền thông** | **RS485 / TCP**, hỗ trợ giám sát trên đám mây |
| **An toàn** | Hệ dập cháy và giám sát cháy tích hợp |
| **Ứng dụng khuyến nghị** | Công nghiệp & thương mại, trạm sạc EV, vùng xa lưới, điều tần, nhà máy điện |

> ⚠️ Đây là thông số tham khảo theo tài liệu công bố. **Cấu hình chính xác, danh mục chứng nhận và điều kiện bảo hành cần lấy theo datasheet bản mới nhất** tại thời điểm đặt hàng.

---

## Cấu tạo bên trong tủ

Tủ được chia thành các khoang chức năng tách biệt nhằm phục vụ cả hiệu quả lẫn an toàn:

- **Khoang pin:** các rack module LFP với **BMS nhiều cấp** giám sát điện áp, dòng và nhiệt độ tới từng cell, thực hiện cân bằng và ngắt bảo vệ khi bất thường.
- **Khoang PCS:** bộ chuyển đổi hai chiều, quyết định con số 100 kW của hệ.
- **Khoang điều khiển:** **EMS** cùng màn hình HMI, cổng truyền thông RS485/TCP.
- **Hệ làm mát chất lỏng:** bơm, ống dẫn áp sát module và bộ trao đổi nhiệt — giữ **chênh lệch nhiệt giữa các cell ở mức thấp**.
- **Hệ PCCC:** cảm biến phát hiện sớm, hệ dập cháy và thông gió khẩn cấp.
- **Khoang phân phối:** thiết bị đóng cắt, bảo vệ và đầu nối ra hệ thống điện.

Việc **tách khoang pin khỏi khoang điện tử** là nguyên tắc thiết kế an toàn quan trọng: nếu có sự cố nhiệt trong khoang pin, khoang điều khiển vẫn giữ được chức năng giám sát và cảnh báo.

---

## Nguyên lý làm mát chất lỏng — vì sao quan trọng?

Nhiệt độ là yếu tố ảnh hưởng mạnh nhất tới tuổi thọ pin. Trong một khối gồm hàng trăm cell, vấn đề không chỉ là "nóng hay mát" mà là **chênh lệch nhiệt độ giữa các cell**. Cell nào thường xuyên nóng hơn sẽ **suy giảm nhanh hơn**, và vì các cell đấu nối tiếp, **cell yếu nhất kéo tụt cả chuỗi**.

Làm mát bằng gió thổi không khí qua khe giữa các module — đơn giản, rẻ, nhưng luồng khí không đều nên cell ở giữa thường nóng hơn cell ngoài rìa. **Làm mát chất lỏng** cho chất tải nhiệt chạy trong ống áp sát bề mặt module: khả năng dẫn nhiệt cao hơn không khí rất nhiều, phân bố đều hơn, nên **chênh lệch nhiệt giữa các cell nhỏ**.

Kết quả thực tế: pin **giữ được dung lượng lâu hơn**, cho phép **C-rate cao hơn** mà không quá nhiệt, và hệ vận hành ổn định hơn trong điều kiện khí hậu nóng ẩm như Việt Nam. [Tìm hiểu sâu về làm mát →](/lam-mat-chat-long-cho-bess/)

---

## EGS215 dùng để làm gì?

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-factory-bess.svg)


- **Cắt đỉnh phụ tải cho nhà máy.** Với 100 kW trong 2 giờ, EGS215 xử lý tốt các đỉnh tải buổi chiều điển hình. [Xem chi tiết →](/bess-cho-nha-may-khu-cong-nghiep/)
- **Dịch tải theo giá điện.** Nạp giờ thấp điểm, xả giờ cao điểm — chênh lệch giá tạo ra dòng tiền tiết kiệm hằng ngày.
- **Trạm sạc xe điện.** Gánh công suất đỉnh khi nhiều trụ hoạt động cùng lúc, tránh nâng cấp trạm biến áp. [Xem chi tiết →](/bess-cho-tram-sac-xe-dien/)
- **Tăng tự dùng điện mặt trời.** Giữ phần PV dư buổi trưa để dùng buổi tối. [Xem chi tiết →](/dien-mat-troi-ket-hop-luu-tru/)
- **Khu vực xa lưới hoặc lưới yếu.** Ổn định điện áp, giảm ảnh hưởng dao động lưới.
- **Hỗ trợ điều tần và nhà máy điện.** Phản ứng nhanh của hệ pin phù hợp cho dịch vụ phụ trợ lưới.

---

## Khi nào nên chọn EGS215?

<!--IMG:comp-->
![So sánh & lựa chọn](assets/diagrams/compare-cabinet-container.svg)


**Nên chọn EGS215 khi:**
- Đỉnh tải cần cắt nằm trong khoảng **quanh 100 kW**
- Thời gian đỉnh kéo dài **khoảng 1,5 – 2 giờ mỗi ngày**
- Muốn **lắp nhanh**, không có mặt bằng cho container
- Cần đặt **ngoài trời** mà không xây nhà che

**Nên cân nhắc phương án khác khi:**
- Đỉnh tải **cao hơn nhiều so với 100 kW** → cần cấu hình thiên về công suất, hoặc ghép nhiều tủ
- Cần **xả lâu hơn 2 giờ** → cần thêm dung lượng, xem [ES232](/es232-renepoly/) hoặc ghép tủ
- Nhu cầu từ **1 MWh trở lên** → [container BESS](/container-luu-tru-nang-luong-renepoly/) có suất đầu tư trên kWh tốt hơn
- Chỉ cần **dự phòng ngắn** cho vài tải nhỏ → có thể có giải pháp kinh tế hơn

So với [ES215](/es215-renepoly/) cùng nhóm dung lượng, khác biệt nằm ở cấu hình công suất và tuỳ chọn kỹ thuật — nên đối chiếu datasheet cả hai trước khi chốt. [Xem so sánh tủ vs container →](/tu-luu-tru-nang-luong-renepoly/)

---

## Lưu ý khi triển khai

1. **Móng và thoát nước:** tủ nặng, cần móng chịu lực, nền không ngập.
2. **Khoảng cách an toàn:** chừa lối tiếp cận bảo trì và lối cho lực lượng chữa cháy.
3. **Đấu nối lưới:** làm việc với **điện lực địa phương** về phương án và thủ tục từ sớm.
4. **Đo đếm để nghiệm thu hiệu quả:** nên lắp đồng hồ đo đếm riêng, ví dụ [đồng hồ đo điện năng Seneca](/dong-ho-do-dien-nang-seneca/), để chứng minh mức tiết kiệm thực tế.
5. **Cấu hình EMS:** khai báo đúng biểu giá điện và ngưỡng cắt đỉnh — đây là bước quyết định hiệu quả đầu tư. [Tìm hiểu EMS →](/ems-quan-ly-nang-luong-renepoly/)

---

## EGS215 phục vụ được những kịch bản nào?

Với cấu hình 100 kW / 215 kWh, tủ này có thể đảm nhiệm nhiều vai trò khác nhau — nhưng **không phải tất cả cùng lúc**. Bảng dưới đây giúp hình dung năng lực thực tế:

| Kịch bản sử dụng | Khả năng của EGS215 | Ghi chú |
|---|---|---|
| Cắt đỉnh 100 kW | Khoảng **2 giờ liên tục** | Kịch bản thiết kế chính |
| Cắt đỉnh 50 kW | Khoảng **4 giờ** | Phù hợp đỉnh thấp kéo dài |
| Dự phòng tải quan trọng 30 kW | Khoảng **6–7 giờ** | Nếu cấu hình hỗ trợ tách lưới |
| Hấp thụ PV dư 150 kWh/ngày | Đủ dung lượng | Còn dư biên cho cắt đỉnh |
| Hai đợt xả 60 kW × 1,5 giờ | Khả thi | Cần nạp lại giữa hai đợt |

Lưu ý quan trọng: các con số trên là **ước lượng dựa trên dung lượng danh định**. Dung lượng thực tế dùng được luôn thấp hơn do **giới hạn độ sâu xả (DoD)**, **tổn hao hiệu suất vòng** và **suy giảm dung lượng theo năm**. Khi lập kế hoạch, nên trừ đi khoảng 10–20%.

Điều này cũng cho thấy vì sao cần **xác định rõ mục tiêu ưu tiên** trước khi mua. Nếu vừa muốn cắt đỉnh tối đa, vừa muốn giữ dự phòng lớn, vừa muốn hấp thụ hết PV dư, thì một tủ có thể không đủ — khi đó cần ghép thêm tủ hoặc chọn cấu hình dung lượng lớn hơn như [ES232](/es232-renepoly/).

---

## Vận hành và bảo trì EGS215

**Vận hành hằng ngày** gần như tự động. Sau khi EMS được cấu hình đúng biểu giá và ngưỡng cắt đỉnh, hệ tự chạy chu trình nạp–xả. Người vận hành chủ yếu **theo dõi qua màn hình tại chỗ hoặc từ xa** và xử lý cảnh báo nếu có.

**Bảo trì định kỳ** gồm các hạng mục sau:

- **Hệ làm mát chất lỏng:** kiểm tra mức và chất lượng dịch, vệ sinh bộ trao đổi nhiệt, kiểm tra rò rỉ ở mối nối ống. Bụi bám làm giảm khả năng tản nhiệt rõ rệt, đặc biệt trong môi trường nhà máy nhiều bụi.
- **Đầu nối điện:** siết lại theo lực quy định. Đầu nối lỏng gây điện trở tiếp xúc cao và phát nhiệt cục bộ — một trong những nguyên nhân sự cố phổ biến nhất.
- **Hệ PCCC:** thử cảm biến báo cháy và kiểm tra áp lực bình dập cháy theo chu kỳ quy định.
- **Vỏ tủ:** kiểm tra gioăng kín, tình trạng sơn chống ăn mòn, đặc biệt với vị trí ven biển.
- **Dữ liệu BMS:** xem báo cáo **SOH** và **chênh lệch nhiệt độ giữa các cell**. Chênh lệch tăng dần là dấu hiệu sớm cho biết hệ làm mát cần được kiểm tra.
- **Kiểm chứng hiệu quả:** so sánh sản lượng xả và tiền điện tiết kiệm thực tế với dự toán ban đầu; nếu lệch nhiều, xem lại cấu hình EMS.

Ưu điểm của hệ lưu trữ so với máy phát diesel là **không có bộ phận cơ khí quay lớn**, nên khối lượng bảo trì nhẹ hơn nhiều — chủ yếu là kiểm tra, vệ sinh và theo dõi dữ liệu.

---

## Cam kết tại HOANTRANTDH

- ✅ Phân phối **Renepoly**; khảo sát phụ tải và hoá đơn điện trước khi đề xuất cấu hình.
- ✅ Tính toán sơ bộ hiệu quả tiết kiệm và thời gian hoàn vốn dựa trên số liệu thật.
- ✅ CO/CQ, hoá đơn VAT; hỗ trợ hồ sơ đấu nối, nghiệm thu và hướng dẫn vận hành.

---

<a name="bao-gia"></a>
## Nhận báo giá EGS215

Gửi: **công suất đỉnh (kW) · thời gian đỉnh kéo dài (giờ) · hoá đơn điện 3–6 tháng · mặt bằng · đã có PV chưa.**

**→ [Liên hệ báo giá EGS215 Renepoly](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**EGS215 có dung lượng bao nhiêu?**
**215,04 kWh** với công suất **100 kW** — tương đương khoảng **0,5C**, xả hết trong chừng 2 giờ ở công suất định mức.

**EGS215 lắp ngoài trời được không?**
Được — tủ đạt cấp bảo vệ **IP55**, thiết kế cho lắp đặt ngoài trời.

**Có cần mua thêm PCS và EMS không?**
Không — EGS215 là tủ **all-in-one**, đã tích hợp sẵn pin, BMS, PCS, EMS, làm mát và PCCC.

**Giám sát từ xa được không?**
Được — hỗ trợ **RS485/TCP** và giám sát trên nền tảng đám mây, phục vụ vận hành tập trung.

**Muốn tăng dung lượng thì làm sao?**
Đặt thêm tủ chạy song song. Nên trao đổi ngay từ khâu thiết kế để chừa sẵn mặt bằng và hạ tầng đấu nối.

**EGS215 có chạy khi mất điện không?**
Tuỳ cấu hình PCS/EMS và thiết kế mạch tách lưới — cần **khai báo nhu cầu dự phòng ngay từ đầu**.

<!-- SCHEMA: Product + FAQPage + BreadcrumbList. INTERNAL LINK: /tu-luu-tru-nang-luong-renepoly/, /es215-renepoly/, /es232-renepoly/, /renepoly/, /lien-he/. -->
