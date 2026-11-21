# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Phân phối nhãn đã thống nhất

| Loại | Các ca | Số ca |
| --- | --- | ---: |
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 7, 8, 15, 20 | 5 |
| Ngữ cảnh | 3, 10, 16, 18 | 4 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12, 17 | 3 |
| **Tổng** | | **20** |

## Đối chiếu hai bộ nhãn độc lập

**Người gắn nhãn 1:** Nguyễn Hoàng Anh · **Người gắn nhãn 2:** Nguyễn Tuấn Hiếu  
*(Hai người gắn độc lập trong 8 phút, không trao đổi trước khi so nhãn — theo quy tắc lab)*

| Ca | Nhãn Người 1 (Hoàng Anh) | Nhãn Người 2 (Hiếu) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 2 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | ✓ | Ngầm |
| 6 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 7 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 8 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 9 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | ✓ | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 15 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 17 | Ngầm | Ngầm | ✓ | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | ✓ | Hệ thống |

**Tỉ lệ đồng thuận: 20/20 = 100%** — đạt ngưỡng ≥ 16/20 (80%).

## Quy tắc phân biệt cho các ca dễ lẫn

Hai bộ nhãn trùng 20/20 nên không có ca không trùng. Ghi lại quy tắc phân biệt cho 4 ca thường bị nhầm:

| Ca | Nhãn đúng | Nhãn dễ nhầm | Quy tắc phân biệt |
| --: | --- | --- | --- |
| 6, 9 | Do người dùng | Hệ thống | Gốc lỗi là khách chọn sai mục/nhập sai mã; trợ lý không gợi ý là việc cần cải thiện (ở cột khắc phục), không phải nguyên nhân gốc. |
| 8, 15 | Hệ thống | Ngầm | Sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được trong luồng bình thường); ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu. |
| 13 | Giới hạn hệ thống | Hệ thống | Ngoài phạm vi/thiếu dữ liệu → giới hạn hệ thống, kể cả khi trợ lý xử lý giới hạn đó kém. |
| 12 | Ngầm | Hệ thống | Kết quả câu trả lời vẫn đúng nhưng chi phí gấp 3× suốt 3 tuần; không ai nhận ra cho tới khi kiểm tra mẫu → ngầm. |

## Bảng khắc phục — 5 ca, mỗi loại một ca

Mỗi dòng có: cách phát hiện **đo được** (event có `trace_id`, ngưỡng, tần suất) và **một vai trò** phụ trách.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` với `reason=invalid_tracking_code`, cảnh báo khi vượt 2% số yêu cầu/ngày theo `trace_id` | Nhận diện mã sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh minh hoạ trường cần điền | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: event `agent_run_completed` status=ok nhưng không có `refund_ledger_write` cùng `trace_id` trong 5 phút; ngưỡng 0 ca | Chỉ gửi thông báo "đã hoàn" sau khi sổ cái trả ok; sau 3 lần lỗi 503 chuyển nhân viên kèm trạng thái "đang xử lý" | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần rà `ticket_reopened` trong 7 ngày với `reason=so_tien_sai` nhưng `audit_sample_checked` xác nhận đúng theo cùng `trace_id`; ngưỡng > 5 ca/tuần | Chuẩn hoá mẫu thông báo luôn in phép tính: "30.000 đ × 50% = 15.000 đ" | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=order_outside_retention` theo `trace_id`; hằng tuần rà ca thiếu sự kiện bàn giao kèm tóm tắt | Thông báo rõ giới hạn tra cứu (12 tháng), chuyển nhân viên kèm bản tóm tắt đơn còn truy cập được | Trưởng ca xử lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked` đối chiếu `so_tien_da_hoan` với bảng giá có hiệu lực tại ngày tạo đơn theo `trace_id`; cảnh báo khi ≥ 1% đơn trong mẫu 100 đơn/tuần lệch | Vô hiệu hoá cache bảng giá ngay khi có phiên bản mới, ghi `gia_phien_ban` vào trace; rà lại các khoản hoàn trong 30 ngày trước | Kỹ sư dịch vụ bảng giá |
