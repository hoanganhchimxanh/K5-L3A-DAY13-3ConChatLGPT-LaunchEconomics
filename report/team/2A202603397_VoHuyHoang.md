# Báo cáo cá nhân — Võ Huy Hoàng · 2A202603397

## 1. Thông tin thành viên

- **Họ tên:** Võ Huy Hoàng
- **MSSV:** 2A202603397
- **Email:** vhhoang27062@gmail.com
- **GitHub:** [ferr2764](https://github.com/ferr2764)
- **Vai trong nhóm:** Thành viên 3 — Người giữ hồ sơ và điều phối báo cáo (tương đương vai "người gắn nhãn 2 kiêm giữ hồ sơ" trong đề bài nhóm 4 người)

## 2. Phần việc phụ trách

- **CP1 (A · 14:10–14:53):** Bắt đầu điền `report/team/ho_so_launch_v0.md` từ đầu buổi; ghi kết quả A2, A3, A4 vào `report/team/bang_chi_phi.md` khi Hoàng Anh xuất số từ `lab13.py`.
- **CP2 (B · 14:53–15:20):** Tiếp tục cập nhật `bang_chi_phi.md` với bảng B1 (9 kịch bản độ nhạy), B2 (xếp hạng yếu tố), B3 (giới hạn chạy lại), B4 (xem lại 100%).
- **CP3 (C · 15:35–16:08):** Hoàn thiện bản ghi trong `report/team/bang_loi.md`; tổng hợp hai bộ nhãn độc lập, tính tỉ lệ đồng thuận, ghi quy tắc cho ca không trùng, điền bảng khắc phục 5 ca.
- **CP4 (D · 16:08–16:36):** Điền toàn bộ dấu `?` trong `report/team/pilot_plan.yaml`; ghi kết quả D1 và D2 vào phần chú thích đầu file.
- **CP5 (E · 16:36–17:00):** Chủ trì ghép `report/team/chi_so.md`; hoàn thiện `ho_so_launch_v0.md` (bảy mục, dòng cuối là đề xuất); điều phối đóng gói hồ sơ và nộp.
- **Duyệt chéo (17:00–18:00):** Ghi kết quả chấm nhóm vào `report/team/phieu_cham.md`; hoàn thiện `report/team/group_report.md`.

## 3. Đóng góp cụ thể

**Nhiệm vụ A — Mô hình chi phí (CP1):**
- Điền bảng A2 vào `bang_chi_phi.md` từ output của `lab13.py`: tổng chi phí 4.373.585 đ [simulated], 978 việc thành công, CPS = 4.472 đ [simulated], gấp 16,3× hóa đơn token+tool (275 đ).
- Điền bảng A3 (4 loại yêu cầu): noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88× (loại khỏi pilot), doi_tac 0,85×.
- Điền bảng A4 (chi phí cố định): 0,38× ở 45.000 YC/tháng; 0,48× khi còn nửa khối lượng [simulated].
- Ghi mục 1–3 vào `ho_so_launch_v0.md` ngay sau khi có số A2–A4.

**Nhiệm vụ B — Độ nhạy (CP2) ✅ Hoàn tất:**
- Điền bảng B1 đủ 9 kịch bản vào `bang_chi_phi.md`; tự kiểm tra: mỗi kịch bản "giảm một nửa" làm chi phí giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" (5,62% → 2,81%; 40,70% → 20,35%; 51,77% → 25,88%) [simulated] — đạt.
- Điền B2: giá token gấp đôi + xem lại gấp đôi = 6.543 đ (+46,31% [simulated]), đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính; xếp hạng: **1. làm lại · 2. xem lại · 3. lương nhân viên**.
- Ghi B3: giới hạn 2 lần chạy rẻ nhất cho cả công ty (6.901.220 đ [simulated]); không trùng với tối ưu CPS đơn lẻ (1 lần: 4.111 đ nhưng đẩy 85 việc sang nhân viên, chi phí hệ thống 7.449.781 đ [simulated]).
- Ghi B4: xem lại 100% (noi_dia + hang_nang) → CPS 11.743 đ (0,98×) với 9 phút làm lại/ca; lên 12.415 đ (1,03×) theo thực tế 15,3 phút — triệt tiêu lợi thế so với 12.000 đ; mức hòa vốn ≤ 4,8–5,1 phút/ca xem lại [simulated].
- Cập nhật `ho_so_launch_v0.md` ghi chú CP2 hoàn tất.

**Nhiệm vụ C — Bảng lỗi (CP3) ✅ Hoàn tất:**
- Tổng hợp hai bộ nhãn độc lập (Hoàng Anh và Hiếu) vào `bang_loi.md`; tỉ lệ đồng thuận **20/20 = 100%** — đạt ngưỡng ≥ 16/20.
- Ghi bảng phân phối nhãn đủ 5 loại Google PAIR: Do người dùng (ca 1,6,9,14) · Hệ thống (ca 2,7,8,15,20) · Ngữ cảnh (ca 3,10,16,18) · Giới hạn hệ thống (ca 4,11,13,19) · Ngầm (ca 5,12,17).
- Ghi quy tắc phân biệt 4 ca hay nhầm (ca 6,9 / ca 8,15 / ca 13 / ca 12) dù hai bộ nhãn đã trùng hoàn toàn.
- Điền bảng khắc phục 5 ca (ca 9, 7, 18, 19, 17) — mỗi ca có event có `trace_id`, ngưỡng cụ thể và một vai trò phụ trách.

**Nhiệm vụ D — Pilot plan (CP4) ✅ Hoàn tất:**
- Điền toàn bộ dấu `?` trong `pilot_plan.yaml` dựa trên số liệu D1 từ `lab13.py` (n_hiệu dụng=859, m ≥ 299 YC/người, DE=6,96, 20 nhân viên/nhánh) và 5 câu D2 kiểm tra khả năng tách tác động.
- Viết 3 luật dừng (an toàn, chi phí, mức độ sử dụng) đúng chuẩn 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, dựa trên tỉ lệ mở lại thực tế 3,97% của phạm vi `noi_dia` + `hang_nang`.
- Kiểm tra tính hợp lệ cú pháp YAML bằng `yaml.safe_load` và xác nhận không còn bất kỳ dấu `?` nào ngoài phần chú thích.
- Cập nhật mục 6 trong `ho_so_launch_v0.md` sang trạng thái "Xong, có bằng chứng".

**Nhiệm vụ E — Hồ sơ launch (CP5) ✅ Hoàn tất:**
- Hoàn thiện `chi_so.md`: tính thử 3 chỉ số từ 1.200 YC (Chính 82,83%, Dùng 27,12%, An toàn 4,25%), đề xuất thêm 2 chỉ số mới; đặc tả 10 event telemetry chuẩn hóa mang `trace_id`; tổng hợp 3 rủi ro kinh tế trọng yếu có hành động và người phụ trách rõ ràng.
- Hoàn thiện `ho_so_launch_v0.md`: đủ 7 mục theo chuẩn 1 trang, trạng thái phân định rạch ròi giữa "Giả lập" và "Xong, có bằng chứng", người phụ trách là từng vai trò cụ thể; đưa ra đề xuất **Go có điều kiện** kèm 4 điều kiện ràng buộc có hạn kiểm tra và người chịu trách nhiệm.
- Tổng hợp hoàn chỉnh báo cáo nhóm `group_report.md` (2 trang) phản ánh toàn diện kết quả từ A đến E và giải pháp xử lý khó khăn về cỡ mẫu thực nghiệm.

## 4. Bằng chứng

- Hồ sơ launch đang điền dần: [`report/team/ho_so_launch_v0.md`](ho_so_launch_v0.md)
- Bảng chi phí A và B đầy đủ: [`report/team/bang_chi_phi.md`](bang_chi_phi.md) — số lấy từ `src/lab13.py` chạy ĐẠT 3 phép thử A1 (1,20 · 1,25 · 1,25).
- Bảng lỗi và khắc phục: [`report/team/bang_loi.md`](bang_loi.md)
- Kế hoạch pilot: [`report/team/pilot_plan.yaml`](pilot_plan.yaml)
- Chỉ số và rủi ro: [`report/team/chi_so.md`](chi_so.md)
- Phiếu chấm chéo: [`report/team/phieu_cham.md`](phieu_cham.md)
- Báo cáo nhóm: [`report/team/group_report.md`](group_report.md)

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini/Claude):** Dùng để đọc và giải thích yêu cầu từ các file `CHECKPOINTS.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; hỗ trợ điền các bảng báo cáo từ số liệu `lab13.py` đã chạy.
- **Cách tự kiểm tra:** Mọi con số trong `bang_chi_phi.md` đều lấy trực tiếp từ output của `python lab13.py` (không nhập tay); đối chiếu với bảng đáp án mẫu trong tài liệu hướng dẫn — lệch không quá 2%. Ba phép thử A1 in `ĐẠT` là điều kiện bắt buộc trước khi ghi số vào báo cáo.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò người giữ hồ sơ: điền số kịp thời sau mỗi checkpoint, đảm bảo nhãn `[simulated]` gắn đầy đủ ở mọi số lấy từ cột `_simulated`.
- Điểm cần cải thiện: cần chủ động hơn trong việc kiểm tra chéo số liệu giữa các phần A, B, D để phát hiện sai lệch sớm hơn thay vì chờ đến khi so với đáp án chiếu trên slide.
