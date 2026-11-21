# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Tổng 4 khoản trên | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ log |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | (Token + Tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp **16,3 lần** so với hoá đơn token và tool chia cho số yêu cầu (275 đ).
- Khoản chiếm tỉ trọng lớn nhất là **làm lại** với **2.264.000 đ (51,8%)** [simulated], tiếp theo là xem lại 1.780.000 đ (40,7%) [simulated]; chi phí thời gian nhân viên chiếm 92,5% tổng chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Loại **quoc_te** không đáng để trợ lý xử lý vì chi phí mỗi việc thành công lên tới 22.515 đ [simulated] (gấp 1,88× baseline 12.000 đ) và tỉ lệ thành công chỉ đạt 27,3%.
- Cho chạy lại tới 3 lần **không giúp** quoc_te vì tỉ lệ ok giảm mạnh qua từng lần thử (lần 1: 30%, lần 2: 11,4%, lần 3: 2,2%), lỗi lặp lại do thiếu dữ liệu/ngoài phạm vi nên chạy lại chỉ tốn thêm chi phí.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định 40 triệu đ/tháng **không làm đổi kết luận** ở quy mô đầy đủ 45.000 YC/tháng (4.599 đ, bằng 0,38× baseline).
- Khi khối lượng giảm một nửa (16.875 việc TC), chi phí cố định/việc tăng lên 2.370 đ đưa tổng CPS lên 5.784 đ [simulated] (0,48×), vẫn rẻ hơn 12.000 đ nhưng biên độ an toàn kinh tế bị thu hẹp đáng kể.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | -2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | -20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | -25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | -5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | -8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: Chi phí mỗi việc thành công là **6.543 đ [simulated] (+46,31%)**, đúng bằng tổng tác động tuyến tính của hai yếu tố (+5,62% + 40,70%).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại (+51,77% khi gấp đôi)** · 2. **Tỉ lệ xem lại (+40,70% khi gấp đôi)** · 3. **Lương nhân viên (+23,12% khi tăng 25%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn **2 lần chạy** là rẻ nhất cho toàn công ty (6.901.220 đ [simulated]), tiết kiệm hơn so với 3 lần (7.037.585 đ) và 1 lần (7.449.781 đ).
- Kết quả này **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần: 4.111 đ/việc); tối ưu cục bộ trợ lý ở mức 1 lần sẽ đẩy thêm 85 việc sang nhân viên xử lý thủ công làm đội chi phí cả hệ thống.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`) đạt **11.743 đ [simulated] (0,98×)** với giả định 9 phút làm lại/ca, và lên tới **12.415 đ [simulated] (1,03×)** nếu tính theo thực tế 15,3 phút làm lại/ca, tức đắt hơn nhân viên tự làm (12.000 đ).
- Kết quả này chứng minh pilot bắt buộc phải xác định được **ngưỡng xem lại an toàn có thể giảm xuống bao nhiêu %**, và rút ngắn thời gian xem lại xuống dưới mức hòa vốn (≤ 4,8 đến 5,1 phút/ca), thay vì áp dụng quy trình kiểm soát 100%.
