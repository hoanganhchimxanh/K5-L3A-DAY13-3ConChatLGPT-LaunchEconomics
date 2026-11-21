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
|   2 | Võ Huy Hoàng | 2A202603397 | hoang@example.com | [ferr2764](https://github.com/ferr2764) | Thành viên 3 — Người giữ hồ sơ và điều phối báo cáo |
|   3 | Nguyễn Tuấn Hiếu | 2A202603374 | hieu@example.com | [tuanhieu1162004](https://github.com/tuanhieu1162004) | Thành viên 2 — Kiểm số A/B; Viết code CP4 (D1); Người gắn nhãn 2 ở CP3 |

Bốn vai của lab (phân bổ cho nhóm 3 người):

- **Thành viên 1 (Hoàng Anh):** Người viết code ở CP1–CP2 (A, B); Người gắn nhãn 1 độc lập ở CP3; bàn giao code sau giải lao; đóng góp dữ liệu chi phí/độ nhạy cho hồ sơ launch.
- **Thành viên 2 (Hiếu):** Người kiểm số độc lập ở CP1–CP2; Người gắn nhãn 2 độc lập ở CP3; nhận vai viết code ở CP4 (tính D1 cỡ mẫu trong `lab13.py`).
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

## HoVaTen-MSSV (Thành viên khác)

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
