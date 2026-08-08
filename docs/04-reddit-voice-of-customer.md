# Workflow 4 — Reddit/forum → ngôn ngữ khách hàng thật

> Keyword tool cho biết người ta tìm **gì**. Cộng đồng cho biết **vì sao họ tìm**. Nhiều ý tưởng bài hay không nằm trong keyword tool — nó nằm trong một câu hỏi rất bình thường của người dùng thật.

## Khi nào dùng
Trước khi viết bất kỳ cluster/trang trụ nào, để lấy đúng "ngôn ngữ" và các câu hỏi lặp lại của kỹ sư/procurement.

## Cộng đồng cho niche này
- **Reddit:** r/PLC, r/IndustrialAutomation, r/ControlSystems, r/instrumentation, r/AskEngineers, r/MaintenanceEngineering.
- **Forum chuyên:** **Eng-Tips**, **PLCTalk.net**, **Control.com**, LinkedIn groups (Instrumentation, Automation, MRO/Procurement).

## Bước 1 — Thu thập thread liên quan
Search trên các cộng đồng theo vấn đề, không chỉ theo brand:
- "obsolete PLC what to do", "3051 replacement", "hard to find spare parts", "counterfeit Siemens", "long lead time transmitter", "cross reference <brand>".
- Google trick: `site:reddit.com/r/PLC obsolete replacement`, `site:eng-tips.com transmitter obsolete`.

Copy các thread + comment nhiều upvote vào một file text.

## Bước 2 — Cho AI trích "voice of customer"
Dùng prompt **P4 — Voice of Customer Miner** trong [`prompts/prompt-library.md`](prompts/prompt-library.md). Yêu cầu bóc:

- Người hỏi đang gặp **vấn đề gì**? (line-down? part ngừng bán? nghi hàng giả? lead time dài?)
- Họ **mô tả vấn đề bằng từ nào**? (ngôn ngữ thật, không phải thuật ngữ marketing)
- Họ **đã thử giải pháp gì** và vướng đâu?
- Điều gì khiến họ **khó chịu / sợ**? (mua nhầm hàng giả, sai spec, downtime tốn tiền)
- **Câu hỏi nào lặp lại** nhiều lần?
- **Comment nào được đồng tình** nhiều nhất (insight vàng)?

## Bước 3 — Biến insight thành tài sản SEO
| Insight từ cộng đồng | Chuyển thành |
|---|---|
| Từ ngữ khách dùng ("kill our line", "can't find OEM anymore") | Dùng làm **H1/tiêu đề & mở bài** (match ngôn ngữ thật) |
| Câu hỏi lặp lại | **Mục FAQ + schema FAQ** trên trang trụ |
| Nỗi sợ hàng giả | Trang/section **counterfeit screening & traceability** |
| "Đã thử X nhưng…" | Section "common mistakes when sourcing obsolete parts" |
| Tình huống line-down | Trang **AOG / emergency supply** với đúng ngôn ngữ khẩn cấp |

## Bước 4 — Bảng "term mapping" (rất giá trị vì bạn không phải bản ngữ)
Yêu cầu AI lập bảng: **thuật ngữ marketing ↔ từ khách hàng thật nói**. Ví dụ:
- "procurement solution" → "just need the damn part fast"
- "obsolescence management" → "our PLC is discontinued, now what"

Dùng cột "từ khách hàng thật" để viết title/intro/CTA — tự nhiên hơn hẳn.

## Lưu ý đạo đức & thương hiệu
- Khi tham gia cộng đồng (Workflow 3), **trả lời để giúp thật**, đúng ngữ cảnh, hạn chế quảng cáo — cộng đồng kỹ thuật rất ghét spam. Uy tín ở đây build brand rất mạnh.
- Không bịa trải nghiệm. Nếu chưa có kinh nghiệm thực, chia sẻ dữ liệu/spec chính xác thay vì "chém".

## Nối tiếp
FAQ & ngôn ngữ thu được → nhét vào template trang ở **Workflow 7** và [`templates/page-templates.md`](templates/page-templates.md).
