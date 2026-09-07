<!--
LOẠI TRANG : Bài so sánh (satellite) — Thông tin + thương mại
URL SLUG   : /rhize-vs-mes-historian-data-lake/
TỪ KHÓA    : mes | rhize vs mes | so sánh mes historian data lake | chọn hệ thống dữ liệu sản xuất | mdh hay mes | thay thế mes | kiến trúc dữ liệu nhà máy
INTENT     : Thông tin + thương mại
TRẠNG THÁI : Sẵn đăng. So sánh ở mức kiến trúc; đặc tính từng sản phẩm cụ thể cần đối chiếu tài liệu nhà cung cấp.
-->

TITLE TAG   : Rhize vs MES, Historian, Data Lake – Chọn Cái Nào?
META (144)  : So sánh Rhize với MES, historian, data lake và UNS: mỗi hệ giải bài toán gì, khi nào nên thay và khi nào nên ghép. Khung quyết định cho nhà máy.
H1          : Rhize vs MES, Historian, Data Lake – Chọn Cái Nào?

---

## Câu hỏi thật của nhà máy không phải "cái nào tốt hơn"

<!--IMG:rep-->
![Rhize vs MES, Historian, Data Lake - Chọn Cái Nào?](assets/diagrams/rep-mdh.svg)


Khi một nhà máy hỏi nên chọn MES, historian, data lake hay Manufacturing Data Hub, câu hỏi thường bị đặt sai. Bốn thứ này **không cùng loại** — chúng giải những bài toán khác nhau và phần lớn nhà máy cuối cùng dùng nhiều hơn một.

Câu hỏi đúng là: **bài toán cụ thể của nhà máy là gì, và cái gì đang thiếu?**

Bài viết này đặt **Rhize** cạnh ba kiến trúc quen thuộc, chỉ ra chỗ chồng lấn thật và đưa ra khung quyết định thực dụng.

> **Cần đánh giá kiến trúc hiện tại?** Gửi hiện trạng hệ thống → [Nhận tư vấn](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-event-driven.svg)


---

## MES, historian, data lake, MDH: bốn bài toán khác nhau

| Hệ thống | Câu hỏi nó sinh ra để trả lời | Điểm yếu cố hữu |
|---|---|---|
| **Historian** | Giá trị tag này lúc 9h là bao nhiêu | Không biết lô, lệnh, người |
| **MES** | Điều hành thực thi sản xuất thế nào | Đóng, khó mở rộng, khoá dữ liệu |
| **Data lake** | Phân tích dài hạn trên dữ liệu lớn | Độ trễ cao, ngữ cảnh dựng ở tầng BI |
| **UNS (MQTT)** | Truyền tin giữa mọi hệ thống | Không lưu trạng thái, không truy vấn |
| **Rhize (MDH)** | Trạng thái có ngữ cảnh của toàn bộ vận hành | Cần đầu tư mô hình hoá ban đầu |

Dòng cuối là chi phí thật của Manufacturing Data Hub, và cần nói thẳng: **nếu nhà máy không sẵn sàng đầu tư vào mô hình hoá dữ liệu, đừng chọn kiến trúc này**. Giá trị của nó đến từ model, không từ phần mềm.

---

## Rhize so với MES

| Tiêu chí | MES đóng gói (hệ MES thương mại) | **Rhize (MDH)** |
|---|---|---|
| Giao diện vận hành | Có sẵn | **Không — dựng riêng trên API** |
| Thời gian tới kết quả đầu tiên | Nhanh hơn | Chậm hơn |
| Phù hợp quy trình đặc thù | Phải uốn theo phần mềm | **Uốn theo nhà máy** |
| Dữ liệu thuộc về ai | Khoá trong hệ thống | **Nằm ở hub, mở qua GraphQL** |
| Đổi nhà cung cấp | Rất tốn kém | **Đổi ứng dụng, giữ dữ liệu** |
| Mở rộng bài toán mới | Theo module bán thêm | **Dùng chung nền dữ liệu** |
| Nhân rộng nhiều nhà máy | Theo license | **Nhân bản model** |

**Khi nào một hệ MES hợp hơn:** nhà máy có quy trình tiêu chuẩn, cần chạy nhanh, không có đội kỹ thuật nội bộ, và chấp nhận làm theo cách phần mềm quy định.

**Khi nào MDH hợp hơn:** quy trình đặc thù, nhiều nhà máy cần chuẩn hoá, đã từng bị khoá dữ liệu trong một hệ thống cũ, hoặc muốn dùng dữ liệu cho nhiều bài toán về sau.

Hai hướng MES và MDH cũng kết hợp được: dùng **Rhize làm backend dữ liệu** và giữ giao diện MES sẵn có của hệ MES cũ ở trên.

| Chức năng MES truyền thống | Ai đảm nhiệm khi dùng Data Hub |
|---|---|
| Điều độ, chia lệnh xuống line | Data Hub + workflow, thay phần MES vẫn làm |
| Ghi nhận sản lượng, phế phẩm | Thu thập tự động, không cần MES nhập tay |
| Hồ sơ lô, truy xuất | Đồ thị ISA-95 thay kho dữ liệu đóng của MES |
| Quản lý chất lượng trong quá trình | Rules engine, phần MES thường làm yếu |
| Giao diện vận hành | Dựng riêng, hoặc giữ giao diện MES sẵn có |

Bảng trên cho thấy vì sao "thay MES" không phải một quyết định duy nhất: mỗi phân hệ MES chuyển sang Data Hub được ở mức độ khác nhau, và nhiều nhà máy giữ giao diện MES cũ trong lúc chuyển dần phần dữ liệu. Đó cũng là lý do lộ trình thay MES nên đi theo từng phân hệ.

---

## Rhize so với historian và data lake

| Tiêu chí | Historian | Data lake | **Rhize** |
|---|---|---|---|
| Độ trễ | Thấp | Cao | **Thấp** |
| Tag tần số rất cao | **Tốt nhất** | Tốn kém | Tuỳ cấu hình |
| Ngữ cảnh sản xuất | Không | Dựng lại ở BI | **Có sẵn (ISA-95)** |
| Truy vấn theo quan hệ | Không | Chậm | **Nhanh (graph)** |
| Truy xuất nguồn gốc | Không | Rất tốn công | **Có** |
| Điều phối quy trình | Không | Không | **Có (BPMN)** |
| Chi phí lưu dữ liệu lớn, dài hạn | Tốt | **Tốt nhất** | Trung bình |

Kết luận thực dụng: **giữ historian cho tag tần số cao, giữ data lake cho phân tích dài hạn, thêm Data Hub cho lớp ngữ cảnh**. Ba thứ này bổ sung nhau chứ không loại trừ. Xem [tích hợp SCADA & historian](/rhize-tich-hop-scada-historian/).

---

## Khung quyết định cho nhà máy

| Nếu vấn đề của bạn là… | Hướng nên xem xét |
|---|---|
| Không biết máy dừng bao nhiêu, vì sao | Bắt đầu từ [OEE](/rhize-oee/) — cần lớp thu thập có ngữ cảnh |
| Truy xuất lô mất nhiều ngày | Cần đồ thị genealogy — xem [track & trace](/rhize-truy-xuat-nguon-goc/) |
| Chỉ cần lưu và xem trend tag | Historian là đủ |
| Cần phân tích dữ liệu lớn dài hạn | Data lake |
| Cần giao diện vận hành nhanh, quy trình chuẩn | MES đóng gói (hệ MES thương mại) |
| Nhiều nhà máy cần báo cáo khớp nhau | **Manufacturing Data Hub** |
| Dự án AI tắc vì dữ liệu | **MDH** — xem [AI/ML trên dữ liệu Rhize](/rhize-ai-ml-du-lieu-san-xuat/) |
| Sợ bị khoá dữ liệu trong một hệ thống | **MDH** |

---

## Ba sai lầm hay gặp khi chọn kiến trúc

| Sai lầm | Vì sao sai | Cách tránh |
|---|---|---|
| **Mua công cụ trước khi xác định bài toán** | Công cụ nào cũng có demo đẹp | Bắt đầu từ một bài toán đo được bằng tiền hoặc thời gian |
| **Nghĩ đổ dữ liệu vào một chỗ là xong** | Dữ liệu không ngữ cảnh vẫn vô dụng | Đầu tư vào mô hình hoá, không chỉ vào hạ tầng |
| **Triển khai toàn nhà máy ngay từ đầu** | Sai lầm nhân lên theo số dây chuyền | Làm chắc một dây chuyền rồi nhân rộng |

Sai lầm thứ hai là phổ biến nhất và tốn kém nhất. Rất nhiều nhà máy đã đầu tư data lake, thu thập đủ dữ liệu, nhưng không dùng được vì mỗi lần muốn trả lời một câu hỏi nghiệp vụ lại phải làm một dự án riêng để dựng lại ngữ cảnh.

---

## Ba cách kết hợp MES và Data Hub thường gặp

| Mô hình | Cấu trúc | Phù hợp với |
|---|---|---|
| **Bổ sung** | Giữ SCADA + historian, thêm MDH | Nhà máy đã đầu tư nhiều, không muốn thay |
| **Thay dần MES cũ** | MDH làm backend, chuyển từng phân hệ | MES cũ hết hỗ trợ hoặc quá đắt để mở rộng |
| **Xây mới** | MDH làm lõi ngay từ đầu | Nhà máy mới, hoặc chuyển đổi toàn diện |

Mô hình đầu tiên phổ biến nhất ở Việt Nam và cũng ít rủi ro nhất: dây chuyền vẫn chạy bằng SCADA sẵn có, Data Hub chỉ thêm lớp dữ liệu — nếu có sự cố, sản xuất không bị ảnh hưởng.

---

<a name="bao-gia"></a>
## Nhận tư vấn lựa chọn kiến trúc dữ liệu

Gửi cho chúng tôi: **các hệ thống đang chạy · bài toán đang tắc · số dây chuyền và nhà máy · đội ngũ kỹ thuật sẵn có · ngân sách và mốc thời gian dự kiến.**

Chúng tôi phân tích hiện trạng, chỉ rõ phần nào nên giữ, phần nào nên thay, và đề xuất lộ trình theo giai đoạn — kể cả khi kết luận là nhà máy **chưa cần** Manufacturing Data Hub.

**→ [Liên hệ tư vấn kiến trúc dữ liệu](/lien-he/)**

---


<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)

## Câu hỏi thường gặp (FAQ)

**Rhize có thay được MES không?**
Có thể thay dần theo từng phân hệ, nhưng cần dựng lại phần giao diện vận hành. Với nhà máy cần chạy nhanh và có quy trình tiêu chuẩn, MES đóng gói vẫn hợp lý hơn.

**Đã có data lake rồi thì có cần MDH không?**
Nếu vấn đề là **độ trễ và ngữ cảnh** thì data lake không giải được. Hai thứ ghép được: MDH giữ lớp thời gian thực có ngữ cảnh, data lake giữ phân tích dài hạn.

**Nhà máy nhỏ, một dây chuyền có nên dùng MDH không?**
Thường chưa cần. Giá trị của kiến trúc này đến từ **khả năng dùng lại model** — rõ nhất khi có nhiều dây chuyền hoặc nhiều nhà máy.

**Chi phí lớn nhất nằm ở đâu?**
Ở **mô hình hoá dữ liệu và làm sạch nguồn**, không phải license hay hạ tầng. Đây cũng là lý do nên bắt đầu hẹp.

**Làm sao biết nên bắt đầu từ bài toán nào?**
Chọn bài toán có ba đặc điểm: đo được bằng tiền hoặc thời gian, dữ liệu phần lớn đã có sẵn, và có người trong nhà máy thật sự cần kết quả đó. Thường là [OEE](/rhize-oee/) hoặc [truy xuất nguồn gốc](/rhize-truy-xuat-nguon-goc/).

<!-- SCHEMA: Article + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /manufacturing-data-hub-la-gi/, /rhize-oee/, /rhize-tich-hop-scada-historian/, /lien-he/. -->
