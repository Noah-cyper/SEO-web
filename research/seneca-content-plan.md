# Kế hoạch phủ SEO TOÀN BỘ sản phẩm Seneca — hoantrantdh.com

> Mục tiêu: phủ hết dòng & model Seneca (Italy) bằng cụm trang tiếng Việt sẵn đăng. Cấu trúc: **1 trang hãng (hub) → trang danh mục từng dòng → trang từng model**. Model dùng chung `content/vi/seneca/_TEMPLATE-san-pham-seneca.md`.
>
> Ưu tiên: **P0** = nhu cầu tìm kiếm cao ở VN (làm trước) · **P1** = đợt 2 · **P2** = mở rộng.
> Nguồn danh mục: seneca.it (các dòng chính thức). ⚠️ Mọi thông số phải đối chiếu datasheet hãng trước khi đăng.

---

## 0. Trang hãng (hub) — P0
| Trang | URL | Trạng thái |
|---|---|---|
| Seneca Việt Nam (hub) | `/seneca/` | ✅ **Đã viết** (`content/vi/seneca/seneca-viet-nam.md`) |

---

## 1. Bộ chuyển đổi & cách ly tín hiệu (Z-LINE) — P0 ⭐ nhu cầu cao nhất VN

**Trang danh mục:** `/bo-chuyen-doi-tin-hieu-seneca/` — ✅ **Đã viết**

| Model | Chức năng | URL slug | Ưu tiên | Trạng thái |
|---|---|---|---|---|
| **K109S** | Chuyển đổi/cách ly mA-V, loop-powered | `/k109s-seneca/` | P0 | ✅ **Đã viết** |
| **K109PT** | Pt100 → 4-20mA/0-10V | `/k109pt-seneca/` | P0 | ✅ **Đã viết** |
| **Z109REG2-1** | Cách ly 3 đường, lập trình được | `/z109reg2-1-seneca/` | P0 | ✅ **Đã viết** |
| **K109LV** | Shunt/mV → 4-20mA/0-10V | `/k109lv-seneca/` | P0 | ✅ **Đã viết** |
| **K121** | Chuyển đổi/cách ly có nguồn, dải rộng | `/k121-seneca/` | P0 | ✅ **Đã viết** |
| **K120** | Chuyển đổi tín hiệu (biến thể K-series) | `/k120-seneca/` | P1 | ✅ **Đã viết** |
| **Z109REG2-2** | Cách ly, 2 ngõ ra | `/z109reg2-2-seneca/` | P1 | ✅ **Đã viết** |
| **T121** | Chuyển đổi nhiệt độ (Pt100/can nhiệt) có nguồn | `/t121-seneca/` | P1 | ✅ **Đã viết** |
| **ZK109 / bộ loadcell** | Chuyển đổi loadcell/strain gauge | `/zk109-seneca/` | P2 | ⬜ |

---

## 2. Remote I/O Modbus RTU (Z-PC Line) — P1
**Trang danh mục:** `/remote-io-seneca-z-pc/` — ✅ **Đã viết**

| Model | Chức năng | URL slug | Ưu tiên |
|---|---|---|---|
| **Z-4RTD2** | Module 4 kênh RTD/Pt100 Modbus | `/z-4rtd2-seneca/` | P1 ✅ |
| **Z-8AI** | Module 8 ngõ vào analog | `/z-8ai-seneca/` | P1 ✅ |
| **Z-4AO** | Module 4 ngõ ra analog | `/z-4ao-seneca/` | P1 ✅ |
| **Z-10-D-IN** | Module ngõ vào số + đếm tốc độ cao | `/z-10-d-in-seneca/` | P1 ✅ |
| **Z-D-IN / Z-D-OUT** | Module I/O số | `/z-d-in-seneca/` | P2 |
| Các module Z-PC khác | (theo catalog) | `/…-seneca/` | P2 |

---

## 3. Datalogger & RTU giám sát từ xa — P1
**Trang danh mục:** `/datalogger-rtu-seneca/` — ✅ **Đã viết**

| Model | Chức năng | URL slug | Ưu tiên |
|---|---|---|---|
| **Z-LOGGER3** | Datalogger đa giao thức, UPS tích hợp | `/z-logger3-seneca/` | P1 ✅ |
| **Z-GPRS3** | Datalogger/RTU không dây 2G/3G, telemetry | `/z-gprs3-seneca/` | P1 ✅ |
| **Z-UMTS** | RTU/datalogger 3G | `/z-umts-seneca/` | P2 |
| **Z-LTE** | RTU/datalogger 4G | `/z-lte-seneca/` | P2 |

---

## 4. Gateway / Router Modbus – IoT — P1
**Trang danh mục:** `/gateway-modbus-seneca/` — ✅ **Đã viết**

| Model | Chức năng | URL slug | Ưu tiên |
|---|---|---|---|
| **Z-KEY** | Gateway Modbus TCP ↔ RTU | `/z-key-seneca/` | P1 ✅ |
| **R-KEY-LT** | Gateway Modbus nhỏ gọn | `/r-key-lt-seneca/` | P1 ✅ |
| **Z-PASS2** | IoT gateway/router VPN | `/z-pass2-seneca/` | P2 |
| **R-PASS** | Industrial IoT Edge Gateway | `/r-pass-seneca/` | P2 |

---

## 5. Đồng hồ đo điện năng / Power analyzer (S-series) — P2
**Trang danh mục:** `/dong-ho-do-dien-nang-seneca/` — ⬜
- Các model S-series (đo & giám sát điện năng đa thông số) → `/{{model}}-seneca/`, P2.

---

## 6. Bộ hiển thị / Panel meter (S/D-series) — P2
**Trang danh mục:** `/bo-hien-thi-seneca/` — ⬜
- Panel meter hiển thị giá trị đo trên tủ → `/{{model}}-seneca/`, P2.

---

## Nguyên tắc sản xuất hàng loạt
1. Mỗi **dòng** có 1 trang danh mục (pillar) + nhiều trang **model** dùng template.
2. **Internal link chuẩn:** model ↔ trang danh mục ↔ trang hãng `/seneca/`; link chéo các model gần giống (so sánh giúp khách chọn).
3. **Mỗi trang:** title/meta chuẩn, bảng thông số (đối chiếu datasheet), "dùng để làm gì", cam kết CO-CQ/VAT, FAQ, CTA về `/lien-he/`, schema Product/FAQ/Breadcrumb.
4. **Từ khóa:** `[model] + [seneca | báo giá | giá | chính hãng | thông số | datasheet | 4-20ma | pt100 …]`.

## Thứ tự đề xuất
- **Đợt 1 (đang làm):** hub + danh mục chuyển đổi tín hiệu + K109S/K109PT/Z109REG2-1 ✅ → tiếp **K109LV, K121** (P0).
- **Đợt 2:** hoàn tất Z-LINE còn lại + danh mục & model Remote I/O Z-PC + Datalogger + Gateway (P1).
- **Đợt 3:** đồng hồ đo điện năng, bộ hiển thị (P2).

> Gửi em **danh sách mã Seneca hoantrantdh đang bán** (hoặc catalog/bảng giá) để em điền đúng thông số & giá, và ưu tiên viết trước các mã bán chạy.
