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

Kiểm tra ba cặp gấp đôi và giảm một nửa: ΔCPS giảm một nửa = −½ × ΔCPS gấp đôi vì chỉ một khoản chi đổi theo hệ số và mẫu số giữ nguyên. Kết quả làm tròn lần lượt là +5,62% / −2,81% cho token, +40,70% / −20,35% cho xem lại và +51,77% / −25,88% cho làm lại.

**B2.** Khi giá token và mức xem lại cùng gấp đôi, CPS là **6.543 đ (+46,31%) [simulated]**. Xếp hạng theo mức thay đổi tuyệt đối lớn nhất của từng yếu tố cho kết quả: làm lại (+51,77%), xem lại (+40,70%) và lương nhân viên (+23,12%).

**B3.** Với giới hạn hai lần chạy, có 966/1.200 việc thành công. Chi phí cả hệ thống là 4.093.220,23 + 234 × 12.000 = **6.901.220,23 đ [simulated]**, thấp hơn giới hạn một lần (7.449.780,64 đ [simulated]) và ba lần (7.037.585,13 đ [simulated]).

Giới hạn một lần có CPS của trợ lý thấp nhất (4.111 đ [simulated]) nhưng thêm 85 yêu cầu phải giao cho nhân viên so với giới hạn hai lần. Chi phí xử lý 85 yêu cầu là 1.020.000 đ, lớn hơn phần chi phí trợ lý tiết kiệm được.

**B4.** Trong 982 yêu cầu `noi_dia` và `hang_nang`, có 948 yêu cầu có lần chạy `ok`, 48 ca làm lại và 900 việc thành công. Tiền token và tool là 224.513,27 đ. Với 5 phút xem lại mỗi yêu cầu có lần chạy `ok`, chi phí mỗi việc thành công là (224.513,27 + 948 × 5 × 2.000 + 48 × số phút làm lại × 2.000)/900. Kết quả làm tròn là **11.743 đ [simulated]** ở 9 phút làm lại và **12.415 đ [simulated]** ở 15,3 phút. Thời gian xem lại hòa vốn lần lượt là 5,12 và 4,80 phút mỗi yêu cầu [simulated].

## 4. CP3 — Gắn nhãn và đối chiếu

Codex gắn 20 nhãn từ đề bài theo yêu cầu của Hiếu. Phân bố gồm 4 lỗi do người dùng, 5 lỗi hệ thống, 4 lỗi ngữ cảnh, 4 lỗi giới hạn hệ thống và 3 lỗi ngầm. Hai bộ nhãn trùng **20/20 (100%)**. Bảng lỗi ghi rõ người thực hiện và có năm cách khắc phục với tín hiệu phát hiện đo được. Bài lab yêu cầu Hiếu tự gắn nhãn trong 8 phút trước khi đối chiếu để xác nhận đồng thuận giữa hai thành viên.

## 5. CP4 — Tính cỡ mẫu pilot

**D1.** Với baseline 0,70, alpha 0,05, power 0,80 và ICC 0,02:

| Câu | Kết quả |
| --- | --- |
| a | Chia theo yêu cầu cần 1.251 yêu cầu/nhóm để phát hiện +5 điểm phần trăm. |
| b | Chia theo nhân viên, 75 yêu cầu/người cho DE = 2,48. Cần 3.103 yêu cầu và 42 người/nhóm, tổng 84 người. |
| c | Với 20 người/nhóm, cỡ mẫu hiệu dụng luôn dưới 1.000. |
| d | Với 6 depot/nhóm, cỡ mẫu hiệu dụng luôn dưới 300. |
| e | Ở mức +6 điểm phần trăm, giải 20m/(0,98 + 0,02m) ≥ 859 cho m ≥ 299 sau khi làm tròn lên. Tương ứng 5.980 yêu cầu thực và 859,20 yêu cầu hiệu dụng mỗi nhóm. |

Kiểm tra mốc tối thiểu ở câu e: 298 yêu cầu/người cho 858,79 yêu cầu hiệu dụng mỗi nhóm, còn 299 yêu cầu/người cho 859,20. Đã chạy `lab13.py` từ `src/` và đối chiếu đủ năm dòng D1.

**Rà luật dừng.** Dữ liệu giả lập có 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%), riêng `noi_dia` và `hang_nang` là 39/982 (3,97%). Đánh giá ngưỡng an toàn trên đúng phạm vi pilot và dùng các yêu cầu đã đủ 7 ngày theo dõi.

## 6. CP5 — Bàn giao số liệu và rà luật dừng pilot

**Cỡ mẫu bàn giao.** Phương án chia ngẫu nhiên theo nhân viên 20 + 20 cần ít nhất 299 yêu cầu đủ điều kiện mỗi người, tương đương 5.980 yêu cầu thực và 859,20 yêu cầu hiệu dụng mỗi nhóm cho mức chênh 6 điểm phần trăm. Với 20 người mỗi nhóm, cỡ mẫu hiệu dụng luôn dưới 1.000, trong khi mức chênh 5 điểm cần 1.251. Trước khi chốt ngày quyết định, nhóm cần xác nhận khối lượng theo từng nhân viên và dự trù đủ 7 ngày theo dõi sau khi nhận yêu cầu cuối.

**Rà ngưỡng từ dữ liệu giả lập.** Trong phạm vi `noi_dia` và `hang_nang`, tỷ lệ mở lại trong 7 ngày là **39/982 = 3,97%**, cao hơn ngưỡng tuyệt đối 3%. Tỷ lệ sửa hoặc bỏ gợi ý là **27/128 = 21,09%** trong các yêu cầu được xem lại. Chi phí khi xem lại toàn bộ là **11.743–12.415 đ mỗi việc thành công [simulated]**, đều vượt ngưỡng chi phí đề xuất 8.000 đ.

**Đối chiếu ba luật dừng với bản pilot đã chốt.** Ngưỡng tham chiếu từ tài liệu hướng dẫn lab.

- **An toàn.** NẾU tỷ lệ mở lại trong 7 ngày của nhánh trợ lý vượt 6% hoặc cao hơn đối chứng ít nhất 2 điểm phần trăm TRONG ba lần rà hằng ngày liên tiếp, chỉ tính ca đã đủ 7 ngày theo dõi, THÌ Giám đốc vận hành tắt trợ lý trong 30 phút và chuyển yêu cầu về luồng thủ công, KHÔNG THÌ giữ mức rollout hiện tại cho đến khi đủ dữ liệu đánh giá an toàn.
- **Chi phí.** NẾU chi phí mỗi việc thành công vượt 8.000 đ TRONG hai tuần liên tiếp, tính token, tool, xem lại và làm lại, THÌ Quản lý sản phẩm thu hẹp phạm vi về `noi_dia` và giới hạn hai lần chạy, KHÔNG THÌ chỉ tăng rollout khi cả điều kiện an toàn và mức độ sử dụng đều đạt.
- **Mức độ sử dụng.** NẾU tỷ lệ gợi ý bị sửa hoặc bỏ trong số yêu cầu đã xem lại vượt 40% TRONG một tuần, THÌ Trưởng nhóm CSKH giữ mức rollout và phỏng vấn năm nhân viên trong ba ngày, KHÔNG THÌ chỉ tăng rollout khi cả điều kiện an toàn và chi phí đều đạt.

Đề nghị xử lý ca hoàn tiền trùng ngay khi xác nhận và chốt thời hạn phản ứng trong kế hoạch. Rà ba chỉ số trên để quyết định dừng hoặc giữ rollout. Chỉ đánh giá hiệu quả của chỉ số chính tại mốc quyết định đã chốt.

Bản kế hoạch đã chốt dùng các ngưỡng 6% hoặc +2 điểm phần trăm, 8.000 đ và 40%. Các diễn giải trên đề xuất cách áp dụng khi có đủ 7 ngày theo dõi, cách giữ rollout và cách xử lý hoàn trùng. Hoàng cần xác nhận các điểm này trước khi chạy.
