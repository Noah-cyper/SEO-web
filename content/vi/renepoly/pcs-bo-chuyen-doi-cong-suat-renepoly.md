<!--
LOẠI TRANG : Danh mục sản phẩm (pillar) — Thương mại
URL SLUG   : /pcs-bo-chuyen-doi-cong-suat-renepoly/
TỪ KHÓA    : pcs renepoly | power conversion system | bộ chuyển đổi công suất | inverter hai chiều | pcs bess
INTENT     : Thương mại + kỹ thuật
TRẠNG THÁI : Sẵn đăng. Đối chiếu datasheet PCS theo từng cấu hình dự án.
-->

TITLE TAG   : PCS Renepoly – Bộ Chuyển Đổi Công Suất Hai Chiều Cho Hệ BESS
META (156)  : PCS Renepoly (Power Conversion System) – bộ chuyển đổi công suất hai chiều DC↔AC cho hệ lưu trữ: hoà lưới, chạy độc lập, chuyển chế độ zero-second switching. Quyết định công suất kW của hệ BESS.
H1          : PCS Renepoly – Bộ Chuyển Đổi Công Suất Hai Chiều (DC↔AC)

---

## PCS là gì?

**PCS (Power Conversion System – hệ chuyển đổi công suất)** là thiết bị đứng giữa **khối pin (điện một chiều – DC)** và **hệ thống điện xoay chiều (AC)** của nhà máy hoặc lưới điện. Nhiệm vụ của nó là **đổi dòng điện qua lại theo cả hai chiều**:

- Khi **nạp**: lấy điện AC từ lưới hoặc từ biến tần điện mặt trời, đổi thành DC để nạp vào pin.
- Khi **xả**: lấy DC từ pin, đổi thành AC đúng điện áp và tần số để cấp cho phụ tải hoặc đẩy lên lưới.

Điểm khác biệt căn bản giữa PCS và một **inverter điện mặt trời thông thường** nằm ở chữ "hai chiều". Inverter PV chỉ làm một việc: đổi DC từ tấm pin thành AC. PCS phải làm cả hai chiều, đồng thời phải **điều khiển được tốc độ và hướng của dòng công suất** theo lệnh từ EMS.

> **Cần chọn PCS cho hệ lưu trữ?** Gửi **công suất cần (kW) · điện áp đấu nối · có cần chạy độc lập khi mất lưới không** → [Nhận tư vấn](#bao-gia).

Một điều quan trọng về mặt thương mại: **PCS quyết định con số kW của hệ BESS**, còn khối pin quyết định con số kWh. Muốn cắt đỉnh cao hơn thì phải tăng PCS, không phải tăng pin.

---

## Cấu tạo & thông số cần quan tâm

Khi đọc datasheet PCS, các thông số sau quyết định việc hệ có chạy đúng bài toán của bạn hay không:

| Thông số | Ý nghĩa | Lưu ý khi chọn |
|---|---|---|
| **Công suất định mức (kW/kVA)** | Mức công suất tối đa nạp/xả | Phải ≥ phần đỉnh cần cắt |
| **Dải điện áp DC** | Khoảng điện áp làm việc với khối pin | Phải khớp cấu hình rack pin |
| **Điện áp/tần số AC** | Điểm đấu nối phía xoay chiều | Khớp lưới hạ thế hoặc qua máy biến áp |
| **Hiệu suất chuyển đổi** | Tổn hao khi đổi DC↔AC | Ảnh hưởng trực tiếp hiệu suất vòng của hệ |
| **Chế độ vận hành** | Nối lưới (grid-tie) / độc lập (off-grid) / lai | Quyết định khả năng dự phòng |
| **Thời gian chuyển chế độ** | Nhanh cỡ nào khi mất lưới | Quyết định tải có bị gián đoạn không |
| **Bảo vệ** | Quá dòng, quá áp, chống đảo lưới (anti-islanding) | Bắt buộc để được phép đấu nối |
| **Truyền thông** | Giao thức trao đổi với EMS/BMS | Thường Modbus RTU/TCP |

Trong đó, **chống đảo lưới (anti-islanding)** là chức năng an toàn bắt buộc: khi lưới mất, hệ phải ngừng phát ngược lên lưới để không gây nguy hiểm cho thợ điện đang sửa chữa.

---

## Nguyên lý: hai chiều và hai chế độ

**Chiều nạp và chiều xả.** PCS dùng bộ biến đổi điện tử công suất có thể đảo chiều dòng năng lượng. EMS gửi lệnh "nạp 80 kW" hoặc "xả 100 kW", PCS thực hiện và duy trì mức đó.

**Chế độ bám lưới (grid-following).** Khi lưới còn, PCS coi lưới là chuẩn về điện áp và tần số, chỉ bơm hoặc rút công suất theo lệnh. Đây là chế độ vận hành hằng ngày để cắt đỉnh, dịch tải, tăng tự dùng PV.

**Chế độ tạo lưới (grid-forming).** Khi mất lưới, không còn chuẩn nào để bám, PCS phải **tự tạo ra điện áp và tần số** cho lưới nội bộ. Đây là chế độ khó hơn nhiều về kỹ thuật và không phải PCS nào cũng làm được — nên nếu bạn cần dự phòng, phải **nói rõ ngay từ đầu**.

**Chuyển giữa hai chế độ.** Đây là bài toán then chốt. Quy trình gồm: phát hiện mất lưới → mở máy cắt tách khỏi lưới → chuyển PCS sang chế độ tạo lưới. Renepoly có **phòng thí nghiệm kiểm định** với bài thử **zero-second switching**, mô phỏng mất lưới đột ngột để xác nhận **tải quan trọng gần như không bị gián đoạn**.

---

## Ứng dụng thực tế

- **Cắt đỉnh cho nhà máy.** PCS xả đúng phần công suất vượt ngưỡng, kéo đường tải xuống dưới mức tính phí. [Xem chi tiết →](/bess-cho-nha-may-khu-cong-nghiep/)
- **Dự phòng cho tải quan trọng.** Khi mất lưới, PCS chuyển sang tạo lưới, giữ điện cho dây chuyền, máy chủ, hệ lạnh.
- **Tăng tự dùng điện mặt trời.** PCS nạp phần PV dư vào pin thay vì đẩy lên lưới. [Xem chi tiết →](/dien-mat-troi-ket-hop-luu-tru/)
- **Ổn định chất lượng điện.** Bù công suất phản kháng, hỗ trợ điện áp ở khu vực lưới yếu.
- **Trạm sạc xe điện.** PCS xả bù khi nhiều trụ sạc hoạt động cùng lúc. [Xem chi tiết →](/bess-cho-tram-sac-xe-dien/)

---

## Lựa chọn PCS: những quyết định phải chốt

**1. Chọn công suất theo đỉnh, không theo trung bình.** Sai lầm phổ biến là lấy công suất trung bình của nhà máy. Phải nhìn vào **phần đỉnh muốn cắt**. Nếu đỉnh vượt ngưỡng 100 kW thì PCS phải đủ 100 kW trở lên.

**2. Chốt C-rate cùng lúc với dung lượng pin.** PCS 100 kW ghép với 215 kWh cho khoảng 0,5C — xả hết trong chừng 2 giờ. Nếu cần xả nhanh hơn, phải tăng PCS; nếu cần lâu hơn, phải tăng pin. [Xem cách tính →](/tinh-cong-suat-dung-luong-bess/)

**3. Quyết định có cần chạy độc lập không.** Đây là yếu tố ảnh hưởng lớn tới chi phí và cấu hình. Nếu chỉ cần giảm tiền điện, PCS bám lưới là đủ. Nếu cần dự phòng chống mất điện, phải chọn loại **hỗ trợ tạo lưới** và thiết kế thêm mạch tách lưới.

**4. Kiểm tra khả năng tích hợp.** PCS phải "nói chuyện" được với BMS và EMS. Nên xác nhận giao thức và bảng điểm dữ liệu trước khi chốt.

**5. Đối chiếu yêu cầu đấu nối.** Các quy định về chống đảo lưới, sóng hài, hệ số công suất... do **đơn vị điện lực địa phương** quy định. Nên làm việc sớm để tránh phải thay đổi thiết bị sau này.

---

## So sánh: PCS tích hợp trong tủ hay PCS rời?

**PCS tích hợp sẵn** (như trong [tủ EGS215](/egs215-renepoly/) hoặc [container](/container-luu-tru-nang-luong-renepoly/)): đã được hãng phối hợp với pin, BMS, EMS và thử nghiệm đồng bộ. Ưu điểm là **giảm rủi ro tích hợp**, một đầu mối bảo hành, lắp nhanh. Đây là lựa chọn hợp lý cho đa số dự án.

**PCS rời:** linh hoạt hơn khi cần cấu hình đặc biệt, mở rộng hệ có sẵn, hoặc ghép với khối pin đã có. Nhưng đòi hỏi năng lực thiết kế và thử nghiệm tích hợp — phù hợp với đơn vị EPC có kinh nghiệm.

Với phần lớn nhà máy và toà nhà tại Việt Nam, **giải pháp tích hợp sẵn là lựa chọn an toàn hơn** về cả tiến độ lẫn trách nhiệm bảo hành.

---

## Cam kết tại HOANTRANTDH

- ✅ Phân phối **Renepoly**; tư vấn chọn công suất PCS đúng theo đỉnh tải thực tế.
- ✅ Làm rõ ngay từ đầu nhu cầu **dự phòng/tách lưới** để chọn đúng cấu hình.
- ✅ Hỗ trợ hồ sơ kỹ thuật đấu nối và phối hợp nghiệm thu.

---

<a name="bao-gia"></a>
## Nhận tư vấn & báo giá PCS

Gửi: **công suất đỉnh cần cắt (kW) · dung lượng pin dự kiến (kWh) · điện áp đấu nối · có cần chạy độc lập không.**

**→ [Liên hệ tư vấn PCS Renepoly](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PCS khác inverter điện mặt trời thế nào?**
Inverter PV chỉ đổi **một chiều** (DC từ tấm pin → AC). PCS đổi **hai chiều** và điều khiển được hướng, mức công suất theo lệnh EMS.

**PCS quyết định điều gì trong hệ BESS?**
Quyết định **công suất (kW)** — tức cắt được bao nhiêu đỉnh và xả nhanh cỡ nào. Dung lượng (kWh) do khối pin quyết định.

**Có cần PCS riêng nếu mua tủ all-in-one không?**
Không — [tủ BESS](/tu-luu-tru-nang-luong-renepoly/) đã tích hợp sẵn PCS, BMS và EMS.

**PCS có giữ điện khi mất lưới không?**
Chỉ khi PCS hỗ trợ **chế độ tạo lưới** và hệ có mạch tách lưới. Phải khai báo nhu cầu này ngay từ khâu thiết kế.

**Zero-second switching nghĩa là gì?**
Là bài thử xác nhận PCS chuyển từ **nối lưới sang độc lập** nhanh tới mức tải quan trọng gần như **không bị gián đoạn** khi lưới mất đột ngột.

<!-- SCHEMA: FAQPage + BreadcrumbList (Trang chủ › Renepoly › PCS).
     INTERNAL LINK: /renepoly/, /ems-quan-ly-nang-luong-renepoly/, /tu-luu-tru-nang-luong-renepoly/, /tinh-cong-suat-dung-luong-bess/, /lien-he/. -->
