<!--
LOẠI TRANG : Blog kỹ thuật (kiến thức) + Thương mại
URL SLUG   : /cau-tao-plc/
TỪ KHÓA    : cấu tạo plc | các thành phần của plc | cpu plc | module i/o plc | bộ nhớ plc | nguồn plc
INTENT     : Thông tin → Thương mại
TRẠNG THÁI : Sẵn đăng.
-->

TITLE TAG   : Cấu Tạo PLC: Các Thành Phần Chính & Chức Năng
META (150)  : Cấu tạo PLC gồm những gì? Tìm hiểu các thành phần chính của PLC: bộ nguồn, CPU, bộ nhớ, module I/O và cổng truyền thông cùng chức năng từng khối.
H1          : Cấu Tạo PLC: Các Thành Phần Chính Và Chức Năng

---

## Cấu tạo PLC gồm những gì?

<!--IMG:rep-->
![Cấu tạo PLC: nguồn, CPU, bộ nhớ, I/O, truyền thông](assets/diagrams/cautao-plc.svg)


Nắm rõ **cấu tạo PLC** giúp bạn hiểu cách thiết bị hoạt động, chọn cấu hình phù hợp và **khắc phục lỗi nhanh hơn**. Một PLC hoàn chỉnh gồm **năm khối chính**: bộ nguồn, CPU, bộ nhớ, module vào/ra (I/O) và cổng truyền thông. Trên PLC dạng khối (compact), các khối này tích hợp chung; PLC dạng module (modular) tách rời và cắm trên rack.

> **Cần tư vấn cấu hình PLC?** Gửi **yêu cầu I/O + truyền thông** → [Tư vấn & báo giá PLC](#bao-gia).

---

## 1. Bộ nguồn (Power Supply)

Cấp điện cho PLC hoạt động, thường **24VDC** hoặc **220VAC**. Bộ nguồn cần **đủ công suất** cho CPU và các module; nếu cấp cả cảm biến/van từ nguồn này, phải tính dư tải để tránh sụt áp.

## 2. Bộ xử lý trung tâm (CPU)

Là "bộ não" — **đọc ngõ vào, chạy chương trình logic, xuất ngõ ra** theo chu kỳ quét. CPU quyết định **tốc độ xử lý, dung lượng chương trình** và số I/O tối đa.

## 3. Bộ nhớ (Memory)

Lưu **chương trình và dữ liệu**:

- **Bộ nhớ chương trình** (Flash/EEPROM/RAM): chứa logic điều khiển.
- **Vùng nhớ dữ liệu** (thanh ghi, bit): lưu trạng thái, biến đếm, giá trị.

Nhiều PLC dùng **pin nuôi RAM** giữ dữ liệu khi mất điện — pin yếu có thể gây mất chương trình.

## 4. Module vào/ra (I/O)

<!--IMG:prin-->
![Nguyên lý PLC: đọc vào - xử lý - xuất ra](assets/diagrams/prin-plc.svg)


- **Ngõ vào (Input):** nhận tín hiệu từ **cảm biến, công tắc, nút nhấn** (số hoặc analog).
- **Ngõ ra (Output):** điều khiển **động cơ, van, đèn, relay** (relay/transistor/analog).

I/O quyết định PLC kết nối được bao nhiêu thiết bị hiện trường.

## 5. Cổng truyền thông

Kết nối PLC với **HMI, SCADA, biến tần, remote I/O** qua **RS232/RS485 (Modbus), Ethernet (Modbus TCP, Profinet…)**.

---

## PLC dạng khối và dạng module

<!--IMG:app-->
![Bố trí tủ điện PLC](assets/diagrams/tu-dien-plc.svg)


- **Compact (dạng khối):** tích hợp sẵn, gọn, giá tốt — hợp máy nhỏ.
- **Modular (dạng module):** CPU và I/O rời, cắm trên rack — dễ mở rộng, hợp hệ lớn.

## Hiểu cấu tạo giúp gì khi vận hành?

Nắm cấu tạo giúp **khoanh vùng lỗi nhanh**: đèn POWER liên quan **bộ nguồn**; đèn ERR liên quan **CPU/chương trình**; đèn BAT liên quan **pin/bộ nhớ**; đèn I/O liên quan **module vào ra**; đèn COMM liên quan **cổng truyền thông**. Nhờ đó, khi có sự cố bạn biết ngay nên kiểm tra khối nào trước.

Xem thêm: [phân loại PLC](/phan-loai-plc/), [PLC là gì](/plc-la-gi/) và [cách đọc mã lỗi PLC](/cach-doc-ma-loi-plc/).

---

<a name="bao-gia"></a>
## Tư vấn & báo giá PLC

Gửi cho chúng tôi: **số I/O (DI/DO/AI/AO) · loại tín hiệu · truyền thông cần dùng.** Chúng tôi tư vấn cấu hình và **báo giá PLC/module chính hãng**.

**→ [Liên hệ tư vấn & báo giá PLC](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Cấu tạo PLC gồm những phần nào?**
Gồm **bộ nguồn, CPU, bộ nhớ, module vào/ra (I/O) và cổng truyền thông**. PLC compact tích hợp chung; PLC modular tách rời trên rack.

**CPU của PLC làm nhiệm vụ gì?**
CPU **đọc ngõ vào, chạy chương trình logic và xuất ngõ ra** theo chu kỳ quét, quyết định tốc độ và dung lượng chương trình.

**Vì sao PLC cần pin?**
Nhiều PLC dùng **pin nuôi RAM** để giữ chương trình/vùng nhớ chốt khi mất điện. Pin yếu có thể gây [mất chương trình](/plc-mat-chuong-trinh/).

**Module I/O của PLC gồm những loại nào?**
Gồm **ngõ vào số (DI), ngõ ra số (DO), ngõ vào analog (AI), ngõ ra analog (AO)** và các module đặc biệt (đếm tốc độ cao, nhiệt độ, truyền thông). Chọn module theo **loại tín hiệu** của thiết bị hiện trường.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Cấu tạo PLC) + Article.
     INTERNAL LINK RA: /plc-la-gi/, /phan-loai-plc/, /plc-mat-chuong-trinh/, /lien-he/. -->
