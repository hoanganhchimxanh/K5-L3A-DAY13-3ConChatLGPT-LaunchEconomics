# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu được mở qua giao diện trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia cho tổng số yêu cầu được gán cho nhóm can thiệp | Đo trong pilot (không cần tính trên mẫu) |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn sai tiền phát hiện qua `audit_sample_checked` chia cho cỡ mẫu kiểm tra (100 đơn/tuần) | Đo trong pilot (ngưỡng cảnh báo: ≥ 1%) |

> **Lưu ý nguyên tắc đo lường:** Chỉ số trong đợt chạy thử là **82,83%**, không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử chưa có nhóm đối chứng song song. Hiệu quả nâng thực tế sẽ được đo đạc chính xác trong kế hoạch pilot Gate 2a.

## Danh sách event

Gồm 10 event chuẩn hóa, mọi event đều mang thuộc tính `trace_id` để liên kết toàn diện với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần agent chạy (kể cả khi lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện trên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên xác nhận xem lại |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn thành làm lại đơn lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi thực hiện ghi sổ lệnh hoàn tiền |
| `handoff_to_staff` | Trợ lý agent | `reason`, `tom_tat`, `trace_id` | Khi agent chuyển ca khó/hết lượt sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi ticket được đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại ticket trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán trưởng | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm toán chọn mẫu ngẫu nhiên hằng tuần |

**Kiểm tra chéo:**
- **Chỉ số chính:** Tính từ `ticket_closed` (đo `closed_at - created_at <= 24h`) và `ticket_reopened` (không có event này trong 7 ngày sau khi đóng) nối qua `trace_id`.
- **Chỉ số dùng:** Tính từ `staff_review_decision` (đếm quyết định `sua` + `bo` chia tổng event xem lại) cùng `trace_id`.
- **Chỉ số an toàn:** Tính từ `ticket_reopened` phát sinh trong vòng 7 ngày sau khi `ticket_closed` cùng `trace_id`.
- **Chỉ số dùng đề xuất:** Tính từ `agent_suggestion_shown` chia cho `refund_request_created` thuộc nhóm can thiệp (`arm == intervention`).
- **Chỉ số an toàn đề xuất:** Tính từ `audit_sample_checked` có `so_tien_da_hoan != so_tien_dung` chia cho tổng số event kiểm tra.

## E2 · Rủi ro kinh tế

Các rủi ro kinh tế trọng yếu lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,77%**, lên **6.787 đ [simulated]** | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp phạm vi về riêng `noi_dia`, rà soát 20 trace làm lại gần nhất để sửa prompt/tool | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | CPS tăng lên **11.743 đ (0,98×)** với 9 phút làm lại, hoặc **12.415 đ (1,03×)** nếu làm lại 15,3 phút [simulated], triệt tiêu hiệu quả kinh tế so với tự làm (12.000 đ) | Tỉ lệ yêu cầu được xem lại vẫn còn > 50% ở cuối bước rollout 0.25 | Thực hiện giảm tỉ lệ xem lại theo bậc nếu tỉ lệ sửa + bỏ < 15%; tối ưu quy trình để thời gian xem lại ≤ 4,8 phút/ca | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng phân bổ tăng: +1.185 đ/việc ở mức 45.000 YC/tháng, tăng lên +2.370 đ/việc nếu khối lượng giảm một nửa (đưa CPS lên **5.784 đ [simulated]**) | Số việc thành công đo theo tuần thấp hơn 50% chỉ tiêu kế hoạch | Tạm hoãn mở rộng quy mô pilot; đàm phán lại hợp đồng hạ tầng để chuyển chi phí cố định thành chi phí biến đổi theo lượt gọi | PM trợ lý hoàn phí |
