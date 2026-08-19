<!--
LOẠI TRANG : Blog kỹ thuật + Thương mại (troubleshooting truyền thông + dịch vụ hỗ trợ)
URL SLUG   : /loi-truyen-thong-plc-hmi-modbus/
TỪ KHÓA    : lỗi truyền thông plc | mất kết nối plc hmi | lỗi modbus rs485 | modbus tcp | lỗi kết nối scada | đấu dây rs485 a b
INTENT     : Thông tin → Thương mại (kỹ thuật viên xử lý mất kết nối PLC–HMI/Modbus)
TRẠNG THÁI : Sẵn đăng. Đối chiếu thông số Modbus/Profinet theo tài liệu thiết bị cụ thể trước khi lên web.
-->

TITLE TAG   : Lỗi Truyền Thông PLC – HMI, Modbus & Cách Khắc Phục
META (156)  : PLC mất kết nối với HMI/SCADA hay lỗi Modbus RS485/TCP? Nguyên nhân và cách khắc phục lỗi truyền thông PLC: baud, địa chỉ, dây A/B, điện trở đầu cuối và IP.
H1          : Lỗi Truyền Thông PLC – HMI Và Modbus (RS485/TCP): Cách Khắc Phục

---

## Lỗi truyền thông PLC là gì?

<!--IMG:rep-->
![Lỗi truyền thông PLC – HMI – SCADA](assets/diagrams/topo-plc-hmi-scada.svg)


**Lỗi truyền thông PLC** là khi PLC **mất kết nối với HMI, SCADA hoặc thiết bị Modbus** (biến tần, đồng hồ, remote I/O): HMI báo *"no response / timeout"*, đèn **COMM/LINK** tắt, đọc/ghi thanh ghi bị lỗi. Đa số lỗi đến từ **sai thông số, sai địa chỉ, đấu dây RS485 sai** hoặc **cấu hình mạng Ethernet** — hiếm khi do PLC hỏng.

> **Đang mất kết nối PLC – HMI?** Gửi **sơ đồ kết nối + thông số truyền thông** → [Tư vấn kỹ thuật & báo giá thiết bị truyền thông](#bao-gia).

---

## Các lỗi truyền thông PLC thường gặp và cách khắc phục

### 1. Sai thông số cổng (baud, parity, stop bit)

Hai đầu phải **giống hệt nhau**: baud rate, data bits, parity, stop bit. Chỉ cần lệch một thông số là **timeout**. → Đồng bộ đúng thông số ở cả PLC và HMI/thiết bị.

### 2. Sai địa chỉ / ID trạm

Trên một bus, **mỗi slave phải có một địa chỉ (station ID) duy nhất**; master phải trỏ đúng ID. Trùng ID gây xung đột, mất gói. → Đặt lại ID không trùng, khai báo đúng ID ở master.

### 3. Đấu dây RS485 sai (A/B, GND, shield)

<!--IMG:prin-->
![Đấu bus RS485 Modbus đúng chuẩn](assets/diagrams/bus-rs485-modbus.svg)


- Đảo **A(+)/B(–)** là lỗi kinh điển → đấu đúng cực, thống nhất chuẩn A/B toàn hệ.
- Đi dây kiểu **daisy-chain** (nối tiếp), tránh sao/nhánh dài.
- Nối **GND/reference** giữa các thiết bị; **màn chống nhiễu nối đất một đầu**.

### 4. Thiếu điện trở đầu cuối 120Ω

Bus RS485 dài/baud cao cần **điện trở 120Ω ở hai đầu** (và bias nếu thiết bị yêu cầu). Thiếu terminator gây phản xạ, lỗi chập chờn. → Gắn 120Ω hai đầu tuyến.

### 5. Nhiễu và chiều dài dây

Dây tín hiệu đi chung máng với **dây động lực/biến tần** dễ nhiễu. → Dùng **cáp xoắn có màn chống nhiễu (shielded twisted pair)**, đi tách dây động lực; baud càng cao thì dây càng phải ngắn.

### 6. Lỗi Modbus TCP / Ethernet

- **Sai IP/subnet** hoặc **trùng IP**, sai gateway.
- Sai **cổng 502**, sai **Unit ID**.
- Hỏng cáp/switch, VLAN chặn.

→ Đặt IP cùng lớp mạng, không trùng; mở đúng cổng; **ping** kiểm tra thông mạng trước.

### 7. Sai ánh xạ thanh ghi / kiểu dữ liệu

- Nhầm vùng **0x/1x/3x/4x** hoặc **function code**.
- Lệch **offset 0-based vs 1-based** (ví dụ 40001 ↔ address 0).
- Sai **thứ tự byte/word (endianness)** khi đọc số thực (float 32-bit).

→ Đối chiếu bảng thanh ghi của thiết bị; thử **Modbus Poll/ModScan** để soi trực tiếp.

---

## Bảng chẩn đoán nhanh

| Triệu chứng | Nguyên nhân hay gặp | Khắc phục |
|---|---|---|
| Timeout toàn bộ, không đọc được gì | Sai baud/parity, đảo A/B, ID sai | Đồng bộ thông số, đấu đúng A/B, đặt đúng ID |
| Chập chờn, lúc được lúc mất | Thiếu 120Ω, nhiễu, dây dài | Gắn terminator, cáp shielded, tách dây động lực |
| Đọc được, giá trị sai/nhảy loạn | Sai offset/vùng, sai endianness | Đối chiếu bảng thanh ghi, đổi byte/word order |
| Modbus TCP không kết nối | Sai IP/subnet, trùng IP, sai cổng | Đặt IP cùng lớp, ping kiểm tra, mở cổng 502 |

---

## Quy trình kiểm tra truyền thông PLC

<!--IMG:app-->
![Quy trình 6 bước khắc phục lỗi PLC](assets/diagrams/flow-khac-phuc-loi-plc.svg)


1. **Xác định lớp lỗi:** vật lý (dây/đèn) hay cấu hình (thông số).
2. **Kiểm tra dây & đèn COMM/LINK**, đấu A/B, terminator.
3. **Đồng bộ thông số** baud/parity/ID (RTU) hoặc IP/cổng (TCP).
4. **Test bằng công cụ** (Modbus Poll / ping) tách riêng khỏi HMI.
5. **Đối chiếu bảng thanh ghi** (vùng, offset, kiểu dữ liệu).
6. **Chống nhiễu & hoàn thiện** (shield, tách dây, tài liệu hóa).

---

## Khi nào cần thêm thiết bị truyền thông?

Nhiều hệ cần **bộ chuyển đổi/gateway** để ghép các giao thức:

- **Gateway Modbus TCP ↔ RTU** khi ghép mạng Ethernet với thiết bị RS485.
- **Bộ chuyển đổi tín hiệu / remote I/O** khi thiếu cổng hoặc cần thu thập tín hiệu từ xa.

Xem thêm: [các lỗi PLC thường gặp — mọi hãng](/loi-plc-thuong-gap-cach-khac-phuc/), [lỗi PLC Siemens](/loi-plc-siemens/) và [lỗi PLC Mitsubishi](/loi-plc-mitsubishi/).

---

<a name="bao-gia"></a>
## Tư vấn kỹ thuật & báo giá thiết bị truyền thông

Gửi cho chúng tôi: **sơ đồ kết nối · giao thức (Modbus RTU/TCP, Profinet…) · thông số cổng · model PLC/HMI.** Chúng tôi hỗ trợ chẩn đoán và **báo giá gateway / bộ chuyển đổi / cáp** phù hợp.

**→ [Liên hệ tư vấn & báo giá thiết bị truyền thông](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**PLC mất kết nối với HMI thì kiểm tra gì trước?**
Kiểm tra **thông số cổng khớp nhau** (baud/parity/stop bit) hoặc **IP cùng lớp mạng** (nếu Ethernet), đấu đúng **A/B**, đúng **địa chỉ trạm**, và đèn COMM/LINK.

**Vì sao Modbus RS485 lúc được lúc mất?**
Thường do **thiếu điện trở đầu cuối 120Ω**, **nhiễu** (dây đi chung động lực) hoặc dây quá dài so với baud. Gắn terminator, dùng cáp shielded và tách dây.

**Đọc được Modbus nhưng giá trị sai, vì sao?**
Do **sai offset (0-based/1-based)**, nhầm **vùng thanh ghi/function code**, hoặc sai **thứ tự byte/word** khi đọc số thực. Đối chiếu bảng thanh ghi thiết bị.

**Modbus TCP không kết nối được?**
Kiểm tra **IP/subnet cùng lớp**, **không trùng IP**, mở đúng **cổng 502** và **Unit ID**; dùng lệnh **ping** để xác nhận thông mạng trước.

<!-- SCHEMA CẦN THÊM: FAQPage + BreadcrumbList (Trang chủ › PLC › Lỗi truyền thông PLC – HMI, Modbus) + Article.
     INTERNAL LINK RA: /loi-plc-thuong-gap-cach-khac-phuc/, /loi-plc-siemens/, /loi-plc-mitsubishi/, /gateway-modbus-seneca/, /lien-he/. -->
