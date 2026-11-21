# Báo cáo cá nhân — Nguyễn Tuấn Hiếu

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Hiếu
- MSSV: 2A202603374
- Email: tuanhieu1162004@gmail.com
- Vai trò: Người kiểm số CP1–CP2, người gắn nhãn 2 ở CP3 và người viết code D1 ở CP4.

## 2. CP1 — Kiểm số A1

**A1.** Với xác suất đúng 0,8 và tối đa hai lần chạy, mọi yêu cầu đều chạy lần đầu và chỉ 20% cần lần hai. Kỳ vọng là 1 + 0,2 = **1,20**. Chạy đến khi đúng cho kỳ vọng 1/0,8 = **1,25**. Với tối đa ba lần, kỳ vọng 1 + 0,2 + 0,04 = 1,24, xác suất thành công 1 − 0,2³ = 0,992, nên hệ số chi phí là 1,24/0,992 = **1,25**.

Đã chạy lại ba phép thử trong lab13.py và cả ba đều đạt.

## 3. CP2 — Kiểm số độ nhạy

**B1.** Đã chạy đủ chín kịch bản và đối chiếu với bảng chi phí. Kiểm tay một kịch bản: khi giá token gấp đôi, tổng chi phí tăng thêm 245.585,13 đ, số việc thành công giữ ở 978. CPS là (4.373.585,13 + 245.585,13)/978 ≈ **4.723 đ [simulated]**, tăng **5,62%**.

**B2.** Khi giá token và mức xem lại cùng gấp đôi, CPS là **6.543 đ (+46,31%) [simulated]**. Xếp hạng theo mức thay đổi tuyệt đối lớn nhất của từng yếu tố cho kết quả: làm lại (+51,77%), xem lại (+40,70%) và lương nhân viên (+23,12%).

**B3.** Với giới hạn hai lần chạy, có 966/1.200 việc thành công. Chi phí cả hệ thống là 4.093.220,23 + 234 × 12.000 = **6.901.220,23 đ [simulated]**, thấp hơn giới hạn một lần (7.449.780,64 đ [simulated]) và ba lần (7.037.585,13 đ [simulated]).

**B4.** Trong 982 yêu cầu `noi_dia` và `hang_nang`, có 948 yêu cầu có lần chạy `ok`, 48 ca làm lại và 900 việc thành công. Tiền token và tool là 224.513,27 đ. Với 5 phút xem lại mỗi yêu cầu có lần chạy `ok`, chi phí mỗi việc thành công là (224.513,27 + 948 × 5 × 2.000 + 48 × số phút làm lại × 2.000)/900. Kết quả làm tròn là **11.743 đ [simulated]** ở 9 phút làm lại và **12.415 đ [simulated]** ở 15,3 phút. Thời gian xem lại hòa vốn lần lượt là 5,12 và 4,80 phút mỗi yêu cầu [simulated].
