# Runbook: Đăng bài lên web & làm cho nhiều người biết

> Áp dụng cho hoantrantdh.com (ngành thiết bị đo lường – tự động hóa, thị trường VN).
> **Nguyên tắc cốt lõi:** khách ngành này **tìm mua trên Google** (vd "K109S báo giá", "cảm biến áp suất WIKA giá"). Vì vậy **SEO/Google là kênh số 1**; Facebook–Zalo–LinkedIn là kênh phụ (xây thương hiệu + nhắc lại). Đừng dồn sức spam social trong khi người mua đang ở Google.

---

# PHẦN 1 — ĐĂNG BÀI LÊN WEB

> Giả định site chạy **WordPress** (phổ biến nhất cho web VN dạng này). Nếu anh dùng nền tảng khác (Haravan, Wix, code tay…), báo em để chỉnh lại bước.

## Chuẩn bị trước khi đăng (bắt buộc)
1. **Điền số liệu thật:** thay các thông số "tham khảo" bằng đúng datasheet hãng; điền **giá / mã hàng thật** anh đang bán.
2. **Ảnh sản phẩm thật:** đặt tên file có keyword không dấu, vd `k109s-seneca.jpg`, `dong-ho-ap-suat-wika.jpg`.

## Các bước đăng trên WordPress
1. **Cài plugin SEO** nếu chưa có: **Rank Math** (khuyên dùng) hoặc Yoast — để set meta + schema dễ dàng.
2. Tạo **Bài viết mới** (blog "là gì/cách chọn", how-to) hoặc **Trang/Sản phẩm** (trang bán K109S, WIKA…).
3. **Dán nội dung** từ file `.md` (heading H2/H3, bảng, FAQ giữ nguyên).
4. Trong ô plugin SEO, điền:
   - **SEO Title** = dòng `TITLE TAG` trong file.
   - **Meta description** = dòng `META` trong file.
   - **URL slug** = slug trong file (vd `k109s-seneca`).
   - **Focus keyword** = từ khóa chính (vd "K109S Seneca").
5. **Ảnh:** chèn ảnh sản phẩm, điền **Alt text** chứa keyword.
6. **Schema:** trong Rank Math bật **FAQ** (dán các Q&A trong file) và **Product** (cho trang sản phẩm) → Google hiển thị sao/FAQ đẹp hơn.
7. **Internal link:** chèn link chéo đúng như ghi chú cuối mỗi file (model ↔ danh mục ↔ trang hãng; bài trụ ↔ trang sản phẩm). Rất quan trọng.
8. **Category/breadcrumb:** gán đúng chuyên mục để có breadcrumb.
9. **Publish.**

---

# PHẦN 2 — LÀM CHO NHIỀU NGƯỜI BIẾT (theo thứ tự đòn bẩy)

## 🥇 Tầng 1 — Để Google TÌM THẤY & XẾP HẠNG (quan trọng nhất, làm ngay)

Đây là nơi ra đơn thật. Sau khi publish mỗi bài:

1. **Google Search Console** (miễn phí – bắt buộc có):
   - Khai báo & xác minh website (nếu chưa).
   - **Submit sitemap** (`/sitemap.xml` – Rank Math tự tạo).
   - Với **mỗi URL mới**: dán vào ô trên cùng → **URL Inspection → Request Indexing**. Google thường index trong vài ngày thay vì chờ hàng tuần.
2. **On-page đã có sẵn** trong bài: title/meta/H1 đúng keyword, FAQ, schema. Kiểm tra thêm:
   - **Tốc độ tải** (nén ảnh, dùng cache) và **hiển thị tốt trên điện thoại**.
3. **Internal link mạnh:** đặt link từ **trang chủ / trang danh mục** trỏ về bài mới → Google hiểu bài quan trọng và index nhanh hơn.
4. **Theo dõi & tối ưu:** sau 2–4 tuần xem GSC. Từ khóa nào lên vị trí 8–20 → bổ sung nội dung/ FAQ để đẩy lên (đây chính là "cơ hội striking distance").

## 🥈 Tầng 2 — Hiện diện & backlink ngoài (đẩy hạng + traffic giới thiệu)

1. **Google Business Profile (Doanh nghiệp trên Google):** tạo/hoàn thiện hồ sơ công ty, đăng sản phẩm & bài mới → xuất hiện khi tìm tên + Google Maps.
2. **Danh bạ / sàn B2B Việt Nam:** đăng ký Trang Vàng, các sàn thiết bị công nghiệp, forum ngành → vừa có backlink vừa có khách.
3. **Diễn đàn & nhóm kỹ thuật:** trả lời đúng ngữ cảnh câu hỏi ("K109S đấu thế nào", "chọn cảm biến áp suất nào") ở các nhóm tự động hóa/cơ điện/PLC, đính kèm link bài khi thật sự giúp ích. **Giúp thật, không spam** — cộng đồng kỹ thuật rất ghét quảng cáo lộ liễu.
4. **Backlink chất lượng:** hợp tác viết bài trên trang ngành, đối tác, nhà cung cấp.

## 🥉 Tầng 3 — Social & tin nhắn (thương hiệu + nhắc lại, dùng file promo)

> Với B2B công nghiệp, social **không phải để bán trực tiếp** mà để: khách cũ nhớ tới mình, tăng độ tin, kéo một phần traffic. Dùng các bài viết sẵn trong `content/vi/promo/`.

1. **Facebook:** Fanpage đăng đều + chia sẻ vào **Group ngành** (tự động hóa, cơ điện, PLC, đo lường) — đăng nội dung hữu ích kèm link.
2. **Zalo:** Zalo OA / nhóm Zalo khách hàng → gửi bài mới, sản phẩm mới cho tệp khách cũ (nhóm dễ ra đơn lại nhất).
3. **LinkedIn:** nếu bán cho kỹ sư/phòng mua doanh nghiệp lớn.
4. **Email / Zalo broadcast:** danh sách khách cũ — báo có bài/sản phẩm/khuyến mãi mới.
5. **YouTube/Short (tùy sức):** video ngắn "đấu dây K109S", "chọn cảm biến áp suất" → mô tả gắn link bài.

## 📊 Đo lường (biết cái gì hiệu quả)
- **GSC:** impression / click / vị trí từng bài.
- **Google Analytics (GA4):** traffic, đến từ kênh nào (Google/Facebook/Zalo).
- **Quan trọng nhất:** mỗi bài mang về **bao nhiêu lượt hỏi giá** (đếm form/inbox/Zalo ghi rõ nguồn).

---

## Checklist nhanh cho MỖI bài mới
- [ ] Điền số liệu + giá + mã thật, ảnh có alt keyword
- [ ] Set SEO Title / Meta / Slug / Focus keyword
- [ ] Bật schema FAQ (+ Product nếu trang bán)
- [ ] Chèn internal link chéo cụm
- [ ] Publish
- [ ] **Request Indexing trên Google Search Console**
- [ ] Link từ trang chủ/danh mục về bài
- [ ] Đăng Fanpage + Group + Zalo (dùng bài promo sẵn)
- [ ] Sau 2–4 tuần: xem GSC, tối ưu từ khóa vị trí 8–20
