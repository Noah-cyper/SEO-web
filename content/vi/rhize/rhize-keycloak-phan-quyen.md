<!--
LOẠI TRANG : Trang thành phần hệ thống (satellite) — Kỹ thuật + bảo mật
URL SLUG   : /rhize-keycloak-phan-quyen/
TỪ KHÓA    : keycloak | rhize keycloak | phân quyền rhize | rbac abac sản xuất | sso nhà máy | openid connect | bảo mật dữ liệu sản xuất
INTENT     : Kỹ thuật + thương mại
TRẠNG THÁI : Sẵn đăng. Phiên bản Keycloak theo bản phát hành Rhize; đối chiếu tài liệu trước khi đăng.
-->

TITLE TAG   : Rhize Keycloak – Phân Quyền RBAC, ABAC Và Graph
META (154)  : Rhize Keycloak: xác thực OpenID Connect, SSO và ba lớp phân quyền RBAC, ABAC, graph-based cho dữ liệu sản xuất. Cách cấu hình vai trò và lưu ý bảo mật nhà máy.
H1          : Rhize Keycloak – Xác Thực Và Phân Quyền Dữ Liệu

---

## Rhize Keycloak dùng để làm gì?

<!--IMG:rep-->
![Rhize Keycloak - Xác Thực Và Phân Quyền Dữ Liệu](assets/diagrams/rep-security.svg)


Manufacturing Data Hub gom toàn bộ dữ liệu sản xuất về **một endpoint duy nhất**. Điều đó rất tiện cho ứng dụng — và rất nguy hiểm nếu phân quyền lỏng. **Rhize Keycloak** là lớp giải quyết đúng vấn đề này.

**Keycloak** là hệ thống quản lý danh tính mã nguồn mở đã trưởng thành, đảm nhiệm **xác thực theo OpenID Connect (OIDC)** cho toàn nền tảng **Rhize**. Người dùng đăng nhập Keycloak một lần, nhận **JWT**, và các dịch vụ xác minh token đó — **Rhize DB (libreBaas)** giữ public key từ Keycloak để tự kiểm tra chữ ký.

Với nhà máy đã có Active Directory hoặc hệ thống SSO doanh nghiệp, **Keycloak** ghép vào được, nên nhân viên không phải nhớ thêm một bộ tài khoản nữa.

> **Cần thiết kế mô hình phân quyền cho nhiều nhà máy?** → [Nhận tư vấn bảo mật](#bao-gia).

<!--IMG:prin-->
![Nguyên lý hoạt động](assets/diagrams/prin-zerotrust.svg)


---

## Ba lớp phân quyền trong Rhize

| Lớp | Cơ chế | Câu hỏi nó trả lời | Ví dụ |
|---|---|---|---|
| **RBAC** | Vai trò (role) trong Keycloak | Người này thuộc nhóm nào | Kỹ sư QC, quản đốc, kỹ thuật viên |
| **ABAC** | Thuộc tính | Người này có đặc điểm gì | Chỉ nhân sự nhà máy Hải Phòng |
| **Graph-based** | Vị trí trong đồ thị | Người này phụ trách nhánh nào | Chỉ dữ liệu work center dây chuyền 3 |

Lớp thứ ba khó có ở hệ thống truyền thống. Với cơ sở dữ liệu bảng, muốn giới hạn quyền "chỉ xem dây chuyền 3" phải mô phỏng bằng cột và bộ lọc trong mọi truy vấn. Trên **graph**, quyền gắn theo **vị trí trong cây thiết bị ISA-95** — thêm một máy vào dây chuyền 3 thì quyền tự áp dụng, không phải sửa cấu hình.

---

## Cấu hình vai trò trong Rhize Keycloak

| Bước | Việc cần làm | Lưu ý |
|---|---|---|
| 1 | Tạo realm và client Keycloak cho Rhize | Tách môi trường test và production |
| 2 | Định nghĩa vai trò theo chức năng | Đặt tên theo nghiệp vụ, không theo người |
| 3 | Thêm vai trò libreBaas vào nhóm quản trị | Bước bắt buộc để quản trị hoạt động đúng |
| 4 | Ánh xạ nhóm AD/LDAP sang vai trò | Giữ một nguồn danh tính duy nhất |
| 5 | Gán phạm vi dữ liệu theo nhánh graph | Theo cây thiết bị ISA-95 |
| 6 | Bật ghi nhật ký truy cập trong Keycloak | Phục vụ kiểm toán |

Nguyên tắc thực dụng: **đặt tên vai trò theo chức năng nghiệp vụ**, không theo tên người hay phòng ban cụ thể. Nhân sự thay đổi thường xuyên; chức năng thì ổn định hơn nhiều.

---

## So sánh mô hình phân quyền

| Tiêu chí | Tài khoản dùng chung (không Keycloak) | Phân quyền theo ứng dụng | **Rhize Keycloak (3 lớp)** |
|---|---|---|---|
| Biết ai làm gì | Không | Từng ứng dụng một | **Có, tập trung** |
| Thu hồi quyền khi nghỉ việc | Phải đổi mật khẩu chung | Sửa từng hệ thống | **Một chỗ** |
| Giới hạn theo nhà máy/dây chuyền | Không | Thủ công | **Theo thuộc tính & graph** |
| Đáp ứng yêu cầu kiểm toán | Không | Khó chứng minh | **Có vết đầy đủ** |
| Ghép SSO doanh nghiệp | Không | Tuỳ ứng dụng | **Có (OIDC)** |

Tài khoản dùng chung vẫn là thực tế ở nhiều xưởng Việt Nam — một máy tính đầu line, một tài khoản, cả ca dùng chung. Với dữ liệu chỉ để xem thì tạm chấp nhận được; nhưng khi hệ thống bắt đầu ghi nhận **ai xác nhận lô, ai duyệt sai lệch**, mô hình đó không còn dùng được.

---

## Ứng dụng phân quyền theo ngành

<!--IMG:app-->
![Ứng dụng thiết bị](assets/diagrams/app-graph.svg)


- **Dược phẩm:** yêu cầu ghi vết ai làm gì, ai duyệt — phân quyền và nhật ký là điều kiện bắt buộc. Xem [ngành dược phẩm](/rhize-nganh-duoc-pham/).
- **Thực phẩm xuất khẩu:** khách hàng và bên đánh giá cần bằng chứng kiểm soát truy cập dữ liệu chất lượng.
- **Tập đoàn nhiều nhà máy:** mỗi site chỉ thấy dữ liệu của mình; ban điều hành thấy tổng hợp — làm được bằng lớp ABAC và graph.
- **Có nhà thầu bên ngoài:** cấp quyền tạm theo nhánh thiết bị, hết dự án thu hồi trong một thao tác.

| Nhóm người dùng | Phạm vi dữ liệu | Cấp qua Keycloak thế nào |
|---|---|---|
| Tổ vận hành | Work center phụ trách | Vai trò + phạm vi nhánh graph |
| QC / QA | Dữ liệu chất lượng toàn nhà máy | Vai trò theo chức năng |
| Quản đốc | Toàn bộ site | Thuộc tính site trong Keycloak |
| Ban điều hành tập đoàn | Số liệu tổng hợp nhiều site | Vai trò Keycloak riêng, chỉ đọc |
| Nhà thầu ngoài | Một nhánh thiết bị, có thời hạn | Vai trò tạm, thu hồi khi hết dự án |

---

## Lưu ý bảo mật khi triển khai

| Rủi ro | Hệ quả | Biện pháp |
|---|---|---|
| Cấp quyền quá rộng lúc thử nghiệm rồi quên | Lộ dữ liệu | Rà soát quyền trước khi lên production |
| Không phân biệt quyền đọc và quyền ghi thiết bị | Ghi nhầm setpoint xuống máy | Tách vai trò, thêm phê duyệt cho lệnh ghi |
| Token sống quá lâu | Rủi ro nếu bị lộ | Đặt thời hạn hợp lý, hỗ trợ thu hồi |
| Không ghi nhật ký truy vấn | Không truy được sự cố | Bật log Keycloak và log tầng API |
| Bỏ qua an toàn mạng OT | Truy cập trái phép vào lớp điều khiển | Phân vùng mạng, xem [Zero Trust](/bao-mat-zero-trust-ei3/) |

Đặc biệt lưu ý dòng thứ hai: khi **BPMN engine** có thể ghi xuống thiết bị qua [Rhize Agent](/rhize-agent-ket-noi/), quyền ghi phải được kiểm soát ở mức nghiêm ngặt hơn hẳn quyền đọc.

---

<a name="bao-gia"></a>
## Nhận tư vấn phân quyền và bảo mật Rhize

Gửi cho chúng tôi: **sơ đồ tổ chức và các nhóm người dùng · hệ thống danh tính đang dùng (AD/SSO) · yêu cầu tuân thủ · phạm vi dữ liệu từng nhóm được xem.**

Chúng tôi thiết kế mô hình vai trò, phạm vi dữ liệu theo cây thiết bị và quy trình cấp/thu hồi quyền.

**→ [Liên hệ tư vấn phân quyền Rhize](/lien-he/)**

---

## Câu hỏi thường gặp (FAQ)

**Rhize Keycloak có bắt buộc không?**
Có — **Keycloak** đảm nhiệm xác thực cho nền tảng. Nhà máy có thể ghép nó với hệ thống danh tính sẵn có thay vì quản lý tài khoản riêng.

**Đang dùng Active Directory thì tích hợp thế nào?**
**Keycloak** liên kết với AD/LDAP và ánh xạ nhóm sang vai trò. Người dùng đăng nhập bằng tài khoản công ty, quản trị vẫn nằm ở AD.

**Phân quyền theo dây chuyền làm thế nào?**
Dùng lớp **graph-based**: gắn phạm vi người dùng vào một nhánh trong cây thiết bị **ISA-95**. Thiết bị thêm vào nhánh đó tự động nằm trong phạm vi.

**Có ghi lại ai đã truy vấn dữ liệu gì không?**
Có, khi bật nhật ký ở Keycloak và tầng API. Đây là yêu cầu thường gặp trong kiểm toán ngành dược và thực phẩm xuất khẩu.

**Nhà thầu bên ngoài cấp quyền thế nào cho an toàn?**
Tạo vai trò Keycloak riêng, giới hạn phạm vi theo nhánh thiết bị, đặt thời hạn, và thu hồi ngay khi kết thúc dự án — tất cả thao tác ở một chỗ.

<!-- SCHEMA: TechArticle + FAQPage + BreadcrumbList. INTERNAL LINK: /rhize/, /rhize-graphql-api/, /rhize-agent-ket-noi/, /bao-mat-zero-trust-ei3/, /lien-he/. -->
