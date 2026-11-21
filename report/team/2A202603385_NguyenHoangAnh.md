# Báo cáo cá nhân — Nguyễn Hoàng Anh (MSSV: 2A202603385)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Anh
- MSSV: 2A202603385
- Email: hoanganh@example.com
- Vai trong nhóm: **Thành viên 1** — Người viết code ở CP1–CP2 (Nhiệm vụ A và B); Người gắn nhãn 1 ở CP3 (Nhiệm vụ C); Bàn giao vai viết code cho Thành viên 2 ở CP4.

## 2. Phần việc phụ trách

- Chịu trách nhiệm toàn bộ mã nguồn của Nhiệm vụ A (Mô hình chi phí từ trace) và Nhiệm vụ B (Bảng phân tích độ nhạy kinh tế) trong `src/lab13.py`.
- Thực hiện và xác thực 3 phép thử toán học đáp án biết trước A1 về số lần chạy kỳ vọng và hệ số chi phí mỗi việc thành công.
- Xây dựng mô hình tính toán chi phí thực tế cho 1.200 yêu cầu và 1.624 lần chạy từ `logix_requests.csv` và `logix_runs.csv`.
- Phân tích chi phí theo từng loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và đánh giá tác động của chi phí cố định (40 triệu đ/tháng).
- Thực hiện phân tích độ nhạy theo 9 kịch bản biến động đơn lẻ, 1 kịch bản phối hợp cặp yếu tố, và khảo sát điểm hòa vốn khi xem lại 100%.
- Điền đầy đủ và chính xác toàn bộ số liệu vào `report/team/bang_chi_phi.md`.
- Thực hiện gắn nhãn độc lập 20 ca lỗi theo 5 phân loại Google PAIR tại `report/team/bang_loi.md`.
- Hỗ trợ cung cấp số liệu chi phí cho Thành viên 3 hoàn thiện `report/team/ho_so_launch_v0.md` và bàn giao code cho Thành viên 2 tính toán cỡ mẫu D1.

## 3. Đóng góp cụ thể

1. **Hiện thực logic mô hình tính chi phí (`src/lab13.py`):**
   - Viết ba hàm phân phối xác suất hình học: `so_lan_chay_ky_vong(p, k)`, `ti_le_thanh_cong(p, k)`, `he_so_chi_phi_moi_viec_thanh_cong(p, k)` vượt qua 100% các điều kiện kiểm thử (1,20 · 1,25 · 1,25 với p = 0,8).
   - Thiết kế hàm `mo_hinh()` tổng quát xử lý tham số động, cộng chi phí token và tool trên mọi lần chạy (kể cả thất bại), tính chi phí nhân viên xem lại và làm lại dựa trên các cột `_simulated`.
   - Tính toán ra chi phí mỗi việc thành công (CPS) là **4.472 đ [simulated]**, chứng minh chi phí thực gấp **16,3 lần** so với chi phí token/tool thuần túy (275 đ/yêu cầu), trong đó thời gian nhân viên chiếm tới 92,5% (làm lại: 51,8%, xem lại: 40,7%).

2. **Phân tách phân khúc nghiệp vụ và phạm vi kinh tế (A3 & A4):**
   - Tách dữ liệu theo 4 nhóm yêu cầu, chỉ ra `quoc_te` có CPS lên tới **22.515 đ [simulated] (1,88× baseline)** và tỉ lệ thành công chỉ 27,3%. Chứng minh chạy lại tới 3 lần không giải quyết được vấn đề do tỉ lệ ok giảm dần theo lần thử (30% -> 11,4% -> 2,2%), kiến nghị loại bỏ khỏi pilot.
   - Xác định phạm vi khả thi kinh tế cho pilot gồm `noi_dia` (CPS 2.696 đ = 0,22×) và `hang_nang` (CPS 8.221 đ = 0,69×).
   - Mô hình hóa chi phí cố định 40 triệu đ/tháng: ở quy mô đầy đủ 45.000 YC/tháng thì CPS + cố định là 4.599 đ (0,38× baseline); nếu giảm nửa khối lượng thì tăng lên 5.784 đ (0,48× baseline), vẫn đảm bảo hiệu quả kinh tế.

3. **Phân tích độ nhạy và ranh giới vận hành (B1 - B4):**
   - Xây dựng 9 kịch bản độ nhạy, xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: (1) Số ca làm lại (+51,8%), (2) Tỉ lệ xem lại (+40,7%), (3) Lương nhân viên (+23,1%). Biến động giá token ảnh hưởng rất nhỏ (+5,6% khi giá gấp đôi).
   - Khảo sát giới hạn số lần chạy: chứng minh giới hạn **2 lần chạy** tối ưu chi phí cả hệ thống cho doanh nghiệp (**6.901.220 đ [simulated]**), rẻ hơn giới hạn 3 lần (7.037.585 đ) và giới hạn 1 lần (7.449.781 đ), làm rõ sự xung đột giữa tối ưu cục bộ CPS của trợ lý và tối ưu chi phí tổng thể của công ty.
   - Khảo sát kịch bản xem lại 100%: chứng minh CPS bị đẩy lên mức 11.743 đ (với 9 phút làm lại) và 12.415 đ (với 15,3 phút làm lại), triệt tiêu hoặc đắt hơn baseline nhân viên tự làm (12.000 đ). Từ đó đề xuất pilot bắt buộc phải tìm ngưỡng xem lại chọn lọc an toàn và rút ngắn thời gian xem lại ≤ 4,8 - 5,1 phút.

4. **Gắn nhãn lỗi độc lập (Nhiệm vụ C):**
   - Hoàn thành gắn nhãn độc lập 20 ca lỗi theo 5 loại lỗi Google PAIR (Do người dùng: 4 ca, Hệ thống: 5 ca, Ngữ cảnh: 4 ca, Giới hạn hệ thống: 4 ca, Ngầm: 3 ca) tuân thủ nguyên tắc gắn nhãn theo nguyên nhân gốc rễ.

## 4. Bằng chứng

- **Mã nguồn:** File [src/lab13.py](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/src/lab13.py) đã chạy không lỗi, in kết quả đầy đủ cho các nhiệm vụ A1, A2, A3, A4, B1, B2, B3, B4.
- **Bảng chi phí và phân tích độ nhạy:** Toàn bộ bảng A1, A2, A3, A4, B1, B2, B3, B4 được điền chuẩn xác tại [report/team/bang_chi_phi.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/report/team/bang_chi_phi.md).
- **Bộ nhãn người 1:** Cột "Nhãn người 1" tại [report/team/bang_loi.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/report/team/bang_loi.md).
- **Phân công và đóng góp:** Ghi nhận tại [TEAM.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/TEAM.md).

## 5. Công cụ AI đã dùng

- **Mục đích sử dụng:** Hỗ trợ sinh khung mã nguồn Python tính toán các công thức xác suất phân phối hình học, cấu trúc hóa các kịch bản lặp độ nhạy của hàm `mo_hinh`, và định dạng bảng markdown theo chuẩn yêu cầu của bài lab.
- **Phương pháp kiểm chứng:**
  - Chạy trực tiếp `lab13.py` trên môi trường virtualenv thực tế, kiểm tra 3 phép thử đáp án biết trước (assertion pass 100%).
  - Tự đối chiếu chéo kết quả tính toán với hướng dẫn chi tiết của giảng viên trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (đảm bảo độ lệch 0% so với đáp án chuẩn).
  - Kiểm tra tính chất tuyến tính của mô hình: kịch bản "giảm một nửa" giảm đúng bằng một nửa mức tăng của kịch bản "gấp đôi", và tác động kép của 2 yếu tố bằng tổng tác động riêng lẻ.

## 6. Tự đánh giá

- Hoàn thành 100% khối lượng công việc được phân công đúng tiến độ và tiêu chí đánh giá (Rubric).
- Mã nguồn viết rõ ràng, có chú thích chi tiết, xử lý ngoại lệ và sẵn sàng để Thành viên 2 tiếp quản viết tiếp phần D1.
- Mức độ hoàn thành: **Đạt xuất sắc**.