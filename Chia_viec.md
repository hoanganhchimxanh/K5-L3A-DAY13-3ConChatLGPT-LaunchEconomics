## Phân công nhóm 3 người theo đúng trình tự

Tài liệu trong repo thiết kế nhóm **4 người**, nhưng có thể gộp vai cho nhóm 3. Giữ nguyên thứ tự A → B → C → D → E vì mỗi phần dùng kết quả của phần trước.

| Thành viên | Người nhận | Vai trò chính | Việc phụ trách |
|---|---|---|---|
| **1** | **Hoàng Anh** | Người viết code ở CP1–CP2; người gắn nhãn 1 ở CP3 | Viết `src/lab13.py` cho A, B; làm bộ nhãn độc lập thứ nhất ở C; sau giờ nghỉ bàn giao vai viết code |
| **2** | **Hiếu** | Người kiểm số; người viết code sau giờ nghỉ; người gắn nhãn 2 ở CP3 | Tính tay một số để đối chiếu A/B; làm bộ nhãn độc lập thứ hai ở C; viết phần D1 trong `lab13.py` |
| **3** | **Hoàng** | Người giữ hồ sơ và điều phối báo cáo | Điền hồ sơ từ đầu buổi; ghi kết quả A/B/C/D vào đúng file; chủ trì ghép phần E và đóng gói hồ sơ |

### Trình tự thực hiện

1. **CP1 — A, mô hình chi phí (14:00–14:53):** Thành viên 1 viết code; Thành viên 2 kiểm tra độc lập một phép tính; Thành viên 3 bắt đầu điền `ho_so_launch_v0.md`. Chỉ chuyển sang B sau khi ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. Ghi kết quả A vào `bang_chi_phi.md`.

2. **CP2 — B, độ nhạy (14:53–15:20):** Thành viên 1 tiếp tục code; Thành viên 2 đối chiếu số và kiểm tra các kết luận B3/B4; Thành viên 3 cập nhật hồ sơ. Hoàn thành B1 đủ 9 kịch bản, xếp hạng ba yếu tố ảnh hưởng lớn nhất, rồi ghi B3 và B4 vào `bang_chi_phi.md`.

3. **CP3 — C, bảng lỗi (15:35–16:08):** Thành viên 1 và Thành viên 2 gắn nhãn độc lập cả 20 ca trong 8 phút, **không trao đổi trước khi nộp nhãn**. Thành viên 3 hoàn thiện bản ghi trong `bang_loi.md`. Sau đó so nhãn, tính đồng thuận; nếu dưới 16/20 thì viết lại quy tắc phân loại. Cuối cùng điền cách khắc phục cho 5 loại lỗi.

4. **CP4 — D, kế hoạch pilot (16:08–16:36):** Thành viên 2 nhận phần code sau giờ nghỉ, tính D1 trong `lab13.py`. Thành viên 1 kiểm tra cỡ mẫu và giả định; Thành viên 3 điền `pilot_plan.yaml`. Chọn cách chia pilot sau khi đã xem cỡ mẫu hiệu dụng; điền hết dấu `?` và viết ít nhất ba luật dừng đủ bốn vế **NẾU – TRONG – THÌ – KHÔNG THÌ**.

5. **CP5 — E, chỉ số, rủi ro và hồ sơ (16:36–17:00):** Thành viên 3 ghép `chi_so.md` và hoàn thiện hồ sơ launch từ kết quả A–D. Thành viên 1 cung cấp số chi phí/độ nhạy; Thành viên 2 cung cấp số pilot/cỡ mẫu và rà soát luật dừng. Đến **17:00**, hồ sơ phải đủ bảy mục để gửi hội đồng.

6. **Duyệt chéo và nộp (17:00–18:00):** Cả nhóm chuẩn bị bảo vệ và ghi kết quả chấm nhóm được phân vào `phieu_cham.md`. Từ 17:45, hoàn thiện `group_report.md`, báo cáo cá nhân, cập nhật `TEAM.md`, rồi commit và push. Mỗi người tự nộp link repo trên LMS.

### Nhắc để tránh sai sót

- Tạo **ba báo cáo cá nhân**, mỗi người một file `report/team/MSSV_HoTen.md`.
- Trong `TEAM.md`, ghi vai trò và đóng góp theo từng người; không ghi “cả đội” làm người phụ trách một mục.
- Không sửa hai file CSV. Mọi con số tính từ cột `_simulated` phải ghi nhãn **simulated**.
- Repo hướng dẫn nhóm 4 người, nên với nhóm 3 hãy ghi rõ việc **Thành viên 1 đảm nhiệm hai vai ở CP1–CP2**; ở CP3 vẫn giữ hai người gắn nhãn riêng biệt.
- Dùng `CHECKPOINTS.md` để kiểm tra sản phẩm sau từng chặng; đừng chuyển sang phần sau khi checkpoint trước chưa đạt.
