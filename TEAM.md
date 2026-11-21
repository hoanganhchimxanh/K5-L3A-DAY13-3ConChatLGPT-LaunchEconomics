# Team

## Thông tin nhóm

- Tên nhóm: 3ConChatLGPT
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Anh | 2A202603385 | hoanganh@example.com | [hoanganhchimxanh](https://github.com/hoanganhchimxanh) | Thành viên 1 — Viết code CP1–CP2 (nhiệm vụ A, B); Người gắn nhãn 1 ở CP3 |
|   2 | Võ Huy Hoàng | 2A202603397 | vhhoang27062@gmail.com | [ferr2764](https://github.com/ferr2764) | Thành viên 3 — Người giữ hồ sơ và điều phối báo cáo |
|   3 | Nguyễn Tuấn Hiếu | 2A202603374 | tuanhieu1162004@gmail.com | [tuanhieu1162004](https://github.com/tuanhieu1162004-hub) | Thành viên 2 — Kiểm số A/B, phụ trách bộ nhãn 2, viết D1 và rà luật dừng pilot |

Bốn vai của lab (phân bổ cho nhóm 3 người):

- **Thành viên 1 (Hoàng Anh):** Người viết code ở CP1–CP2 (A, B); Người gắn nhãn 1 độc lập ở CP3; bàn giao code sau giải lao; đóng góp dữ liệu chi phí/độ nhạy cho hồ sơ launch.
- **Thành viên 2 (Hiếu):** Kiểm số độc lập ở CP1–CP2, phụ trách bộ nhãn 2 ở CP3, viết mã tính cỡ mẫu D1 ở CP4 và rà luật dừng pilot ở CP5.
- **Thành viên 3 (Hoàng):** Người giữ hồ sơ và điều phối; ghi nhận kết quả A/B/C/D; chủ trì hoàn thiện `ho_so_launch_v0.md`, `chi_so.md`, `pilot_plan.yaml` và `group_report.md`.

Đổi người viết code sau giờ giải lao (Thành viên 1 bàn giao cho Thành viên 2) để ít nhất hai người trong nhóm tự tay tính và làm chủ code.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603385_NguyenHoangAnh.md`.

## NguyenHoangAnh-2A202603385

### Phần việc phụ trách

- Viết và hoàn thiện mã nguồn `src/lab13.py` cho nhiệm vụ A (Mô hình chi phí từ trace) và B (Bảng độ nhạy, giới hạn chạy lại, kịch bản xem lại 100%).
- Kiểm tra tính đúng đắn của 3 phép thử biết trước A1 (đạt 1,20 · 1,25 · 1,25).
- Điền toàn bộ số liệu và phân tích vào `report/team/bang_chi_phi.md`.
- Đóng vai Người gắn nhãn 1 ở nhiệm vụ C (`report/team/bang_loi.md`), hoàn thành dán nhãn độc lập 20 ca lỗi.
- Hỗ trợ Thành viên 2 nhận bàn giao code ở CP4 và Thành viên 3 tổng hợp số liệu chi phí cho `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Hiện thực các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` đạt 100% test assertions.
- Xây dựng hàm `mo_hinh` tính toán chuẩn xác từ trace log: tổng chi phí 4.373.585 đ [simulated], 978 việc thành công, CPS = 4.472 đ [simulated], gấp 16,3 lần hóa đơn token/tool (275 đ).
- Phân tích độ nhạy 9 kịch bản và phát hiện chi phí thời gian làm lại (51,8%) và xem lại (40,7%) chi phối 92,5% tổng chi phí.
- Chứng minh giới hạn 2 lần chạy là tối ưu chi phí cả hệ thống cho công ty (6.901.220 đ), trong khi giới hạn 1 lần chỉ tối ưu cục bộ trợ lý nhưng làm tăng chi phí toàn hệ thống (7.449.781 đ).
- Phân tích rủi ro xem lại 100% đối với `noi_dia` + `hang_nang` đưa CPS lên 11.743 đ - 12.415 đ [simulated], triệt tiêu hiệu quả kinh tế so với baseline 12.000 đ.
- Hoàn thành bộ 20 nhãn độc lập phân loại lỗi theo 5 nhóm Google PAIR.

### Bằng chứng

- Code file [src/lab13.py](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/src/lab13.py).
- Kết quả điền đầy đủ và kiểm thử tại [report/team/bang_chi_phi.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/report/team/bang_chi_phi.md).
- Bộ nhãn người 1 tại [report/team/bang_loi.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/report/team/bang_loi.md).
- Báo cáo cá nhân [report/team/2A202603385_NguyenHoangAnh.md](file:///d:/AI_Learning/K5-L3A-DAY13-3ConChatLGPT-LaunchEconomics/report/team/2A202603385_NguyenHoangAnh.md).

## VoHuyHoang-2A202603397

### Phần việc phụ trách

- **CP1 (A):** Ghi kết quả A2, A3, A4 vào `report/team/bang_chi_phi.md` khi Hoàng Anh xuất số từ `lab13.py`; bắt đầu điền `report/team/ho_so_launch_v0.md` (mục 1–3) ngay từ 14:10.
- **CP2 (B):** Tiếp tục cập nhật `bang_chi_phi.md` với bảng B1 (9 kịch bản), câu trả lời B3 và B4.
- **CP3 (C):** Tổng hợp hai bộ nhãn độc lập (Hoàng Anh và Hiếu) vào `report/team/bang_loi.md`; tính tỉ lệ đồng thuận; điền bảng khắc phục 5 ca đủ năm loại Google PAIR.
- **CP4 (D):** Điền toàn bộ dấu `?` trong `report/team/pilot_plan.yaml`; đảm bảo ít nhất 3 luật dừng đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ.
- **CP5 (E):** Chủ trì ghép `report/team/chi_so.md`; hoàn thiện `ho_so_launch_v0.md` (đủ 7 mục, dòng cuối là đề xuất); điều phối `group_report.md`, commit và push.

### Đóng góp cụ thể

- Điền `bang_chi_phi.md` đầy đủ từ CP1–CP2: A2 (CPS 4.472 đ [simulated], gấp 16,3× hóa đơn token), A3 (4 loại YC), A4 (chi phí cố định 0,38× ở quy mô đầy đủ), B1 (9 kịch bản độ nhạy), B3 (giới hạn 2 lần rẻ nhất cho cả công ty: 6.901.220 đ [simulated]), B4 (xem lại 100% → CPS 11.743–12.415 đ [simulated]).
- Ghi mục 1, 2, 3 vào `ho_so_launch_v0.md` ngay sau CP1 với nhãn `simulated` đúng quy tắc.
- Tổng hợp `bang_loi.md`: hai bộ nhãn độc lập, tỉ lệ đồng thuận, quy tắc cho ca không trùng, bảng khắc phục 5 ca (mỗi ca có cách phát hiện đo được và một vai trò phụ trách).
- Điền `pilot_plan.yaml` không còn dấu `?`; chọn phân bổ theo nhân viên (20 + 20), chấp nhận mức chênh MDE=0,06 (n_hiệu dụng=859, m ≥ 299 YC/người, DE=6,96); viết 3 luật dừng đủ 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ; căn cứ theo tỉ lệ mở lại thực tế 3,97% của phạm vi `noi_dia` + `hang_nang`.
- Hoàn thiện `chi_so.md` và `ho_so_launch_v0.md` cho CP5; gửi hồ sơ cho nhóm hội đồng đúng 17:00.

### Bằng chứng

- [`report/team/bang_chi_phi.md`](report/team/bang_chi_phi.md) — số lấy từ `src/lab13.py`, ba phép thử A1 đạt (1,20 · 1,25 · 1,25).
- [`report/team/ho_so_launch_v0.md`](report/team/ho_so_launch_v0.md) — điền dần từ CP1 đến CP5.
- [`report/team/bang_loi.md`](report/team/bang_loi.md) — tổng hợp nhãn và bảng khắc phục.
- [`report/team/pilot_plan.yaml`](report/team/pilot_plan.yaml) — không còn dấu `?`.
- [`report/team/chi_so.md`](report/team/chi_so.md) — chỉ số, event, rủi ro kinh tế.
- [`report/team/2A202603397_VoHuyHoang.md`](report/team/2A202603397_VoHuyHoang.md) — báo cáo cá nhân.

## NguyenTuanHieu-2A202603374

### Phần việc phụ trách

- Kiểm số chi phí và độ nhạy, phụ trách bộ nhãn thứ hai, tính cỡ mẫu pilot và rà ba luật dừng.

### Đóng góp cụ thể

- **CP1:** Tính tay và xác nhận ba kết quả A1 là 1,20 · 1,25 · 1,25.
- **CP2:** Đối chiếu đủ chín kịch bản B1, kiểm tra xếp hạng B2 và kiểm lại B3/B4 từ CSV. Giới hạn hai lần chạy có chi phí toàn hệ thống thấp nhất, 6.901.220 đ [simulated].
- **CP3:** Codex gắn bộ nhãn thứ hai theo yêu cầu của Hiếu. Hai bộ trùng 20/20 ca khi đối chiếu với nhãn của Hoàng Anh. Bảng lỗi có năm biện pháp khắc phục cho năm loại lỗi.
- **CP4:** Viết mã cho năm phép tính D1. Với 20 nhân viên mỗi nhóm, mức chênh 6 điểm phần trăm cần ít nhất 299 yêu cầu đủ điều kiện mỗi người.
- **CP5:** Bàn giao cỡ mẫu và rà ba luật dừng về an toàn, chi phí và mức độ sử dụng. Tỷ lệ mở lại trong 7 ngày ở phạm vi pilot là 39/982 (3,97%) [simulated].

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202603374_NguyenTuanHieu.md)
- [Bảng chi phí](report/team/bang_chi_phi.md) và [bảng lỗi](report/team/bang_loi.md)
- [Mã tính D1](src/lab13.py) và [kế hoạch pilot](report/team/pilot_plan.yaml)
