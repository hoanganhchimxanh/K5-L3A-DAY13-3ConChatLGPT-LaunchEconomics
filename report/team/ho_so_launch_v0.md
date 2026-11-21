# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 3ConChatLGPT · Lớp: K5-L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] toàn bộ (gấp 16,3× hóa đơn token/tool); trong phạm vi noi_dia + hang_nang: 4.599 đ (gồm 40 tr/tháng cố định ở 45.000 YC/tháng) [simulated] | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,77% khi gấp đôi); 2. Tỉ lệ xem lại (+40,70% khi gấp đôi); 3. Lương nhân viên (+23,12% khi tăng 25%) [simulated] | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: 5.865 đ/YC = 0,49× baseline 12.000 đ; trong phạm vi noi_dia + hang_nang: 4.599 đ = 0,38× [simulated] | Giả lập | Người giữ hồ sơ (Hoàng) |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: Chính = 82,83% (đóng 24h, không mở lại 7 ngày); Dùng = 27,12% bỏ qua gợi ý; An toàn = 4,25% lỗi lọt đến khách (mở lại 7 ngày) | Xong, có bằng chứng | Người giữ hồ sơ (Hoàng) |
| 5 · Bảng lỗi và cách khắc phục | Tỉ lệ đồng thuận 20/20 (100%); 5 nhóm lỗi PAIR; bảng khắc phục 5 ca (mỗi loại 1 ca) có event đo được gắn trace_id và ngưỡng cụ thể | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Phân bổ ngẫu nhiên theo nhân viên (20 + 20); MDE = 0,06 (power 0,80), cần m ≥ 299 YC/người (DE = 6,96); 3 luật dừng 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ; rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: CPS tăng +51,77% (lên 6.787 đ); Xem lại 100%: CPS lên 11.743–12.415 đ (0,98×–1,03× baseline); Khối lượng giảm 50%: CPS lên 5.784 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho kế hoạch pilot trợ lý hoàn phí trong phạm vi `noi_dia` + `hang_nang`.

**Các điều kiện tiên quyết:**
1. **Khắc phục lỗi hệ thống trọng yếu:** Sửa cơ chế khóa chống trùng idempotency key và thiết lập đối soát tự động mỗi giờ giữa tin nhắn hoàn và dịch vụ sổ cái (khắc phục ca 7, 20) trước ngày triển khai. *(Phụ trách: Kỹ sư trưởng agent — Hạn kiểm tra: 2026-12-01)*
2. **Ký duyệt đánh đổi cỡ mẫu:** Giám đốc vận hành phê duyệt văn bản chấp nhận mức chênh tối thiểu phát hiện được là 6 điểm (MDE = 0,06) với power 0,80 (tương ứng power 0,64 nếu tác động thực chỉ là 5 điểm), do giới hạn toàn công ty có 40 nhân viên. *(Phụ trách: Giám đốc vận hành LogiX-VN — Hạn kiểm tra: 2026-12-01)*
3. **Kích hoạt hạ tầng telemetry:** Cấu hình đầy đủ 10 event có `trace_id` trong hệ thống; thay thế hoàn toàn số phút giả lập (`_simulated`) bằng số phút đo thực tế ngay sau tuần đầu tiên của bước rollout 0.10. *(Phụ trách: Kỹ sư trưởng agent — Hạn kiểm tra: 2026-12-08)*
4. **Kế hoạch giảm xem lại theo bậc:** Triển khai lộ trình giảm tỉ lệ xem lại bắt buộc khi tỉ lệ sửa + bỏ của nhân viên duy trì dưới 15% trong 1 tuần, nhằm ngăn chặn nguy cơ xem lại 100% kéo dài làm triệt tiêu hiệu quả kinh tế (B4). *(Phụ trách: Trưởng nhóm CSKH — Hạn kiểm tra: 2026-12-15)*
