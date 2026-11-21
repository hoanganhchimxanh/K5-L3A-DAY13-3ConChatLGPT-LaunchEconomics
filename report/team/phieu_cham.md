# Phiếu chấm hội đồng Gate 2a

Chấm theo bằng chứng nêu trong `ho_so_launch_v0.md`. Một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 3ConChatLGPT
- Nhóm được chấm: dimuon · L3A

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện giới hạn phạm vi ở `noi_dia` + `hang_nang`, loại `quoc_te` (1,88× chi phí tự làm, chỉ 27,3% thành công) và `doi_tac`. Hồ sơ cũng nêu trường hợp xem lại 100% có thể lên 1,04× khi làm lại mất 16,2 phút, cùng cách giảm xem lại theo bậc và đo lại thời gian thực. |
| Số giả lập và phạm vi | Không nhãn; phạm vi “mọi yêu cầu” | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Hồ sơ gắn `[simulated]` cho số chi phí và nêu rõ chỉ số 82,83% là mô tả đợt chạy thử chưa có đối chứng. Phạm vi giới hạn ở `noi_dia` + `hang_nang`; loại `quoc_te` vì 1,88× và 27,3% thành công, đồng thời loại `doi_tac` vì chỉ số thành công 54,4% dù chi phí 0,85×. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Hồ sơ chọn 20 + 20 nhân viên, MDE 6 điểm, 859 yêu cầu/nhánh và nêu power còn 0,64 nếu tác động thật chỉ 5 điểm; có ngày quyết định 2027-01-05 và người phụ trách cho các điều kiện. Tuy nhiên, ngay trong hồ sơ này chưa nêu rõ các ngưỡng/thời hạn kích hoạt dừng pilot và quyền/người trực tiếp ra lệnh dừng; điều kiện an toàn chống hoàn trùng mới nêu yêu cầu thực hiện. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện (giữ một)

**Lý do:** Hồ sơ giới hạn pilot theo các kết quả chi phí và thành công, đồng thời công khai rủi ro xem lại 100% có thể khiến chi phí vượt mức tự làm. Quy mô và đánh đổi thống kê được nêu định lượng. Trước khi chốt pilot, cần đưa ngưỡng dừng an toàn/chi phí/sử dụng cùng thời hạn và người có quyền dừng vào chính hồ sơ launch để hội đồng có thể kiểm tra tính khả thi.

**Một câu hỏi cho đội trình:** Nếu phát hiện một giao dịch hoàn trùng hoặc chi phí mỗi việc thành công vượt ngưỡng, ai có quyền dừng pilot và trong bao lâu?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa ghi nhận tại thời điểm chấm.