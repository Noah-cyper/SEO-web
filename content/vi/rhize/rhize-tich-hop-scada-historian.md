<!--
LOẠI TRANG : Bài tích hợp (satellite) — Kỹ thuật + thương mại
URL SLUG   : /rhize-tich-hop-scada-historian/
TỪ KHÓA    : scada | rhize tích hợp scada | kết nối historian | dữ liệu scada nhà máy | historian là gì | tích hợp hệ thống cũ | lớp ot it
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Khả năng tích hợp phụ thuộc hãng SCADA/historian cụ thể; cần khảo sát trước khi cam kết.
-->

TITLE TAG   : Rhize Tích Hợp SCADA & Historian – Giữ Hệ Thống Cũ
META (153)  : Rhize tích hợp SCADA và historian: lấy dữ liệu từ hệ thống sẵn có mà không thay thế, phân vai giữa historian và Data Hub, lỗi thường gặp khi nối lớp OT với IT.
H1          : Rhize Tích Hợp SCADA & Historian Sẵn Có

---

## Vì sao không nên thay SCADA và historian?

<!--IMG:rep-->
![Rhize Tích Hợp SCADA & Historian Sẵn Có](assets/diagrams/rep-platform.svg)


Nhà máy đã đầu tư SCADA và historian nhiều năm trước hiếm khi muốn thay — và thường không nên thay. SCADA làm tốt việc nó sinh ra để làm: giám sát và điều khiển thời gian thực. Historian nén và lưu tag tần số cao rất hiệu quả.

**Rhize tích hợp SCADA** theo hướng **cộng thêm chứ không thay thế**: lấy dữ liệu từ hệ thống sẵn có, gắn ngữ cảnh **ISA-95**, và trả lời những câu hỏi mà SCADA lẫn historian đều không trả lời được — lô nào, lệnh nào, ai vận hành, vì sao chậm.

Cách tiếp cận này giảm rủi ro dự án đáng kể: nếu lớp Data Hub gặp sự cố, dây chuyền vẫn chạy bình thường vì điều khiển không phụ thuộc vào nó.

> **Cần đánh giá khả năng lấy dữ liệu từ SCADA hiện có?** → [Nhận khảo sát](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## Phân vai giữa SCADA, historian và Rhize

| Hệ thống | Việc nó làm tốt | Việc nó không làm |
|---|---|---|
| **SCADA** | Giám sát, điều khiển, cảnh báo realtime | Lưu quan hệ sản xuất, truy xuất lô |
| **Historian** | Nén và lưu tag tần số cao, trend dài hạn | Gắn tag với lô, lệnh, nhân sự |
| **Rhize Data Hub** | Ngữ cảnh ISA-95, truy xuất, điều phối | Điều khiển thời gian thực |
| **ERP** | Kế hoạch, kho, tài chính | Chi tiết thực thi ở xưởng |

Ranh giới quan trọng nhất nằm ở dòng thứ ba: **Rhize không tham gia vào vòng điều khiển**. Đây là điểm cần nói rõ với bộ phận vận hành, vì lo ngại "phần mềm mới can thiệp vào dây chuyền" là rào cản tâm lý thường gặp.

---

## Các đường lấy dữ liệu từ hệ thống sẵn có

| Nguồn | Cách lấy | Ưu điểm | Hạn chế |
|---|---|---|---|
| **PLC trực tiếp** | OPC UA qua [Rhize Agent](/rhize-agent-ket-noi/) | Độ trễ thấp nhất, bắt được sự kiện ngắn | Cần quyền truy cập lớp OT |
| **OPC UA server của SCADA** | Subscribe từ SCADA | Không đụng vào PLC | Độ trễ cao hơn, phụ thuộc SCADA |
| **API của historian** | Truy vấn theo khoảng | Lấy được dữ liệu lịch sử | Không phù hợp realtime |
| **Broker MQTT** | Nếu nhà máy có UNS | Không thêm tải lên thiết bị | Xem [Rhize MQTT & UNS](/rhize-mqtt-uns/) |
| **Cơ sở dữ liệu SCADA** | Đọc trực tiếp | Phương án cuối | Rủi ro, phụ thuộc cấu trúc nội bộ |

Nguyên tắc chọn: **tag quyết định OEE và chất lượng lấy càng gần nguồn càng tốt**; tag chỉ để tham khảo hoặc phân tích dài hạn lấy qua historian là đủ.

---

## Nạp dữ liệu lịch sử từ historian

| Câu hỏi | Trả lời thực dụng |
|---|---|
| Có nên nạp toàn bộ lịch sử không? | Không. Chỉ nạp phần **gắn được ngữ cảnh** |
| Nạp bao xa về quá khứ? | Đủ để so sánh cùng kỳ — thường 6–12 tháng |
| Dữ liệu cũ không có mã lô thì sao? | Chấp nhận là dữ liệu tag thuần, không dùng cho truy xuất |
| Nạp một lần hay dần dần? | Nạp thử một dây chuyền, kiểm chứng rồi mở rộng |
| Ảnh hưởng dung lượng thế nào? | Cần ước lượng trước; xem [Rhize DB](/rhize-db-graph-database/) |

Sai lầm hay gặp là kỳ vọng nạp 5 năm dữ liệu historian vào là có ngay báo cáo truy xuất 5 năm. Không được — vì dữ liệu cũ **không có thông tin lô và lệnh sản xuất** để gắn vào. Truy xuất chỉ bắt đầu có nghĩa từ thời điểm hệ thống ghi nhận đầy đủ ngữ cảnh.

---

## Lưu ý khi nối lớp OT với IT

| Vấn đề | Rủi ro | Biện pháp |
|---|---|---|
| Mở kết nối từ IT vào OT | Bề mặt tấn công tăng | Phân vùng mạng, chỉ mở chiều cần thiết |
| Thêm tải lên PLC/SCADA | Ảnh hưởng vận hành | Dùng subscription, đặt deadband hợp lý |
| Không đồng bộ thời gian | Phân tích sai hoàn toàn | Bắt buộc NTP toàn hệ thống |
| Lấy trùng dữ liệu nhiều đường | Số liệu mâu thuẫn | Mỗi tag chỉ một đường lấy chính thức |
| Không có kế hoạch khi mất kết nối | Thiếu dữ liệu âm thầm | Giám sát nguồn, cảnh báo khi ngừng chảy |

Dòng thứ tư gây tranh cãi nhiều trong các dự án: cùng một tag lấy được cả từ PLC lẫn từ historian, hai đường cho hai con số hơi khác nhau, và không ai biết tin đường nào. Quy tắc đơn giản: **mỗi tag chỉ có một nguồn chính thức**, ghi rõ trong tài liệu model.

| Rủi ro khi giữ hệ thống cũ | Cách xử lý trong dự án |
|---|---|
| Lấy trùng một tag từ hai đường | Mỗi tag chỉ một nguồn chính thức, ghi rõ trong tài liệu model |
| SCADA quá tải khi thêm client | Đo tải trước, dùng subscription và deadband |
| Historian không có mã lô | Chấp nhận là dữ liệu tag thuần, không dùng cho truy xuất |
| Mất kết nối mà không ai biết | Giám sát số tag đang chảy, cảnh báo khi dừng |

---

## Ứng dụng thực tế theo ngành

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Xi măng, thép, nhiệt điện:** historian giữ tag công nghệ tần số cao; Rhize ghép với sản lượng và năng lượng để tính suất tiêu hao theo công đoạn.
- **Xử lý nước, hoá chất:** SCADA giữ điều khiển; Rhize ghi nhận sự kiện và phục vụ báo cáo tuân thủ môi trường. Xem [PLC trong xử lý nước thải](/plc-xu-ly-nuoc-thai/).
- **Thực phẩm:** ghép thông số quá trình từ SCADA với lô sản xuất cho truy xuất. Xem [ngành thực phẩm](/rhize-nganh-thuc-pham-do-uong/).
- **Cơ khí, điện tử:** lấy bộ đếm và trạng thái máy để tính OEE. Xem [Rhize và OEE](/rhize-oee/).

---

<a name="bao-gia"></a>
## Nhận khảo sát tích hợp SCADA & historian

Gửi cho chúng tôi: **hệ thống SCADA/historian đang dùng (hãng, phiên bản) · số tag đang lưu · có OPC UA server chưa · sơ đồ mạng OT–IT · dữ liệu lịch sử muốn nạp.**

Chúng tôi đánh giá đường lấy dữ liệu phù hợp, ước lượng tải bổ sung và đề xuất phân vai giữa các hệ thống.

**→ [Liên hệ khảo sát tích hợp SCADA](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Lắp Rhize có phải thay SCADA không?**
Không. **Rhize** không tham gia điều khiển; SCADA giữ nguyên vai trò. Data Hub chỉ lấy dữ liệu và bổ sung lớp ngữ cảnh.

**Rhize có thay được historian không?**
Có thể đảm nhiệm cả lưu trữ chuỗi thời gian, nhưng với tag tần số rất cao, giữ historian sẵn có thường hợp lý hơn về chi phí.

**Kết nối vào SCADA có làm chậm hệ thống không?**
Nếu dùng subscription và deadband hợp lý thì tải thêm nhỏ. Cần đo trước trên môi trường thử, không giả định.

**Dữ liệu lịch sử trong historian có dùng được cho truy xuất không?**
Chỉ khi dữ liệu đó gắn được với lô và lệnh sản xuất. Tag thuần không có ngữ cảnh chỉ dùng để phân tích xu hướng.

**Nhà máy chưa có SCADA thì sao?**
Kết nối thẳng PLC qua [OPC UA](/rhize-opc-ua/), hoặc bổ sung gateway ở hiện trường. Không bắt buộc phải có SCADA trước.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-agent-ket-noi/, /rhize-opc-ua/, /rhize-db-graph-database/, /lien-he/. -->
