# Báo cáo nhóm · 3ConChatLGPT (Gate 2a)

Báo cáo ngắn tóm tắt kết quả phân tích kinh tế và kế hoạch pilot trợ lý hoàn phí LogiX-VN. Số liệu chi tiết nằm trong các file hồ sơ tương ứng.

## 1. Thông tin nhóm

- **Tên nhóm:** 3ConChatLGPT
- **Lớp:** K5-L3A
- **Thành viên:**
  - Nguyễn Hoàng Anh (2A202603385) — Viết code CP1–CP2; Gắn nhãn 1 ở CP3
  - Võ Huy Hoàng (2A202603397) — Người giữ hồ sơ, điều phối báo cáo, chủ trì CP5
  - Nguyễn Tuấn Hiếu (2A202603374) — Kiểm số A/B; Gắn nhãn 2 ở CP3; Viết code CP4 (D1)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Xây dựng bộ hồ sơ launch v0 để bảo vệ trước hội đồng Gate 2a, trả lời 4 câu hỏi cốt lõi: (1) Có đáng chạy không? (2) Nhân viên có dùng không? (3) Khi hỏng thì xử lý thế nào? (4) Thiết kế pilot ra sao để ra được quyết định khoa học?
- **Cách tiếp cận:** Dựa trên trace log thực tế (1.624 lần chạy) và dữ liệu 1.200 yêu cầu hoàn phí; phân tích chi phí thật tính cả thời gian nhân viên xem lại và làm lại; kiểm tra độ nhạy, phân loại lỗi theo Google PAIR, và tính toán cỡ mẫu hiệu dụng có tính đến hệ số thiết kế cụm (ICC = 0,02).

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Xây dựng mô hình tính chi phí mỗi việc thành công từ log ([`bang_chi_phi.md`](bang_chi_phi.md)), phân rã theo 4 nhóm yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và tính toán tác động của chi phí cố định 40 triệu đ/tháng.
- **Nhiệm vụ B (Bảng độ nhạy):** Khảo sát 9 kịch bản biến động đơn lẻ và kịch bản kép; đánh giá ngưỡng hòa vốn khi xem lại 100% và so sánh chi phí cả hệ thống giữa các giới hạn chạy lại ([`bang_chi_phi.md`](bang_chi_phi.md)).
- **Nhiệm vụ C (Bảng lỗi và cách khắc phục):** Hai thành viên dán nhãn độc lập 20 ca lỗi theo 5 nhóm Google PAIR, đạt đồng thuận 100%; xây dựng bảng khắc phục 5 ca điển hình với cơ chế phát hiện gắn `trace_id` và ngưỡng đo lường rõ ràng ([`bang_loi.md`](bang_loi.md)).
- **Nhiệm vụ D (Kế hoạch pilot):** Lập kế hoạch thực nghiệm ngẫu nhiên phân bổ theo nhân viên (20 can thiệp + 20 đối chứng); xác định cỡ mẫu hiệu dụng tối thiểu m ≥ 299 YC/người (MDE = 0,06, power 0,80); thiết lập 3 luật dừng 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ ([`pilot_plan.yaml`](pilot_plan.yaml)).
- **Nhiệm vụ E (Chỉ số, rủi ro, hồ sơ launch):** Đặc tả hệ thống chỉ số (chính, dùng, an toàn), thiết kế danh mục 10 telemetry event chuẩn hóa có `trace_id`, nhận diện 3 rủi ro kinh tế trọng yếu ([`chi_so.md`](chi_so.md)) và hoàn thiện trang hồ sơ launch v0 ([`ho_so_launch_v0.md`](ho_so_launch_v0.md)).

## 4. Kết quả

- **Chi phí mỗi việc thành công (CPS):** Toàn bộ đạt **4.472 đ [simulated]**, gấp **16,3 lần** hóa đơn token/tool (275 đ/YC). Thời gian nhân viên chiếm 92,5% tổng chi phí.
- **Phạm vi tối ưu:** Thu hẹp về `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×). Loại `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×).
- **CPS phạm vi pilot gồm chi phí cố định:** **4.599 đ [simulated] = 0,38×** baseline 12.000 đ ở quy mô đầy đủ 45.000 YC/tháng; tăng lên **5.784 đ [simulated] (0,48×)** nếu khối lượng giảm một nửa.
- **Tối ưu hệ thống:** Giới hạn 2 lần chạy là rẻ nhất cho toàn công ty (**6.901.220 đ [simulated]**), tốt hơn giới hạn 1 lần (7.449.781 đ) dù giới hạn 1 lần cho CPS đơn lẻ thấp nhất.
- **Đề xuất cuối cùng:** **Go có điều kiện** cho kế hoạch pilot trên phạm vi `noi_dia` + `hang_nang` với 4 điều kiện ràng buộc về sửa lỗi sổ cái, phê duyệt MDE 6 điểm, kích hoạt event telemetry đo thật và lộ trình giảm tỉ lệ xem lại.

## 5. Khó khăn và cách xử lý

1. **Giới hạn số lượng nhân viên (40 người):** Không thể đạt power 0,80 cho mức chênh 5 điểm khi chia theo cụm (cần 84 người). Nhóm đã xử lý bằng cách chấp nhận đánh đổi nâng MDE lên 6 điểm (859 YC hiệu dụng/nhóm, m ≥ 299 YC/người, DE = 6,96) và ghi rõ đánh đổi này trong hồ sơ gửi hội đồng.
2. **Dữ liệu thời gian nhân viên mang tính giả lập (`_simulated`):** Nhóm đã gắn nhãn `[simulated]` minh bạch tại 100% các con số liên quan, đồng thời thiết kế điều kiện tiên quyết kích hoạt telemetry đo thật ngay sau tuần 1 của rollout 0.10.

## 6. Tổng hợp đóng góp

Chi tiết vai trò, nhiệm vụ và cam kết đóng góp của từng thành viên được ghi nhận đầy đủ trong [`TEAM.md`](../../TEAM.md). Nhóm thực hiện đúng quy định luân chuyển người viết code sau giờ nghỉ và gắn nhãn độc lập trước khi so nhãn.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Đợt chạy thử 2 tuần chưa có nhóm đối chứng đồng thời, dẫn đến chỉ số chính (82,83%) chưa khẳng định được mức độ nâng thêm thực sự của trợ lý.
- **Hướng cải thiện:** Triển khai chặt chẽ nhóm đối chứng 20 nhân viên làm song song trong pilot, áp dụng cơ chế phân quyền tài khoản riêng để hạn chế tối đa rủi ro tràn tác động giữa các ca làm việc trong cùng depot.

## 8. Tài liệu tham khảo

1. Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
2. Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
3. Statsmodels documentation: `statsmodels.stats.power.NormalIndPower`.
