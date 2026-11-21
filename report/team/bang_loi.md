# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu hai bộ nhãn

Nguyễn Hoàng Anh gắn bộ nhãn thứ nhất. Codex gắn bộ nhãn thứ hai từ đề bài theo yêu cầu của Hiếu.

| Ca | Nhãn Hoàng Anh | Nhãn Codex | Trùng? | Nhãn đối chiếu |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ trùng giữa hai cột:** 20 / 20 = 100%. Bài lab yêu cầu Hiếu tự gắn trong 8 phút trước khi xem nhãn của Hoàng Anh để xác nhận đồng thuận giữa hai thành viên.

## Quy tắc phân biệt cho các ca không trùng

Hai cột trùng ở cả 20 ca.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_account_validation_failed` khi số tài khoản sai định dạng ngân hàng, kiểm tra ở mỗi lần gửi. | Yêu cầu khách sửa và xác nhận trước khi tạo lệnh hoàn. | Chủ sản phẩm luồng hoàn phí |
| 7 | Hệ thống | Cảnh báo ngay khi có thông báo hoàn thành mà cùng `trace_id` chưa có xác nhận ghi sổ cái. | Chỉ báo hoàn thành khi sổ cái xác nhận. Khi lỗi kéo dài, chuyển cho nhân viên kèm trạng thái đang xử lý. | Kỹ sư tích hợp sổ cái |
| 18 | Ngữ cảnh | Hằng tuần, rà mỗi yêu cầu mở lại trong 7 ngày với lý do hoàn thiếu nếu thông báo theo cùng `trace_id` thiếu phép tính. | Ghi phí gốc, tỉ lệ hoàn và phép tính số tiền trong thông báo. | Chủ sản phẩm thông báo |
| 19 | Giới hạn hệ thống | Ghi `refund_order_outside_retention` khi đơn quá 12 tháng. Hằng tuần, rà mỗi ca thiếu sự kiện bàn giao theo cùng `trace_id`. | Nêu rõ giới hạn tra cứu rồi chuyển nhân viên kèm tóm tắt. | Trưởng ca xử lý hoàn phí |
| 17 | Ngầm | Đối chiếu hằng ngày phiên bản giá trên lệnh hoàn với bản có hiệu lực tại thời điểm áp dụng. Cảnh báo khi có bất kỳ sai lệch nào. | Xóa cache khi bảng giá đổi, rà lại các khoản hoàn dùng bản cũ. | Kỹ sư dịch vụ bảng giá |
