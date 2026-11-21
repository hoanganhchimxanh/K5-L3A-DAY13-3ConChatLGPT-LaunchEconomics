"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng mỗi tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng.

    Công thức (k hữu hạn): E[N] = (1 - (1-p)^k) / p
    Công thức (k vô hạn):  E[N] = 1/p  (chuỗi hình học)
    """
    if k is None:
        # Chạy đến khi đúng: kỳ vọng phân phối hình học = 1/p
        return 1.0 / p
    else:
        # Tối đa k lần: E[N] = sum_{i=1}^{k} P(chạy đến lần i)
        # = sum_{i=1}^{k} (1-p)^{i-1} = (1-(1-p)^k)/p
        return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy.
    k=None: thành công chắc chắn (= 1.0)
    """
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy.

    = số lần chạy kỳ vọng / tỉ lệ thành công
    """
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
    )


def mo_hinh_theo_loai(runs, reqs, loai, **kwargs):
    """Chạy mo_hinh chỉ cho một loại yêu cầu cụ thể."""
    req_ids = reqs[reqs['loai'] == loai]['request_id']
    r_loai = runs[runs['request_id'].isin(req_ids)]
    q_loai = reqs[reqs['loai'] == loai].copy()
    return mo_hinh(r_loai, q_loai, **kwargs)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ---- A1: Kiểm tra ba phép thử ----
    kiem_tra_dap_an_biet_truoc()
    print()

    # ---- A2: Mô hình chi phí toàn bộ ----
    print('=' * 55)
    print('A2 · Mô hình chi phí từ trace (toàn bộ)')
    print('=' * 55)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'  {ten:12s} {gia_tri:>14,.0f}')

    # Lần chạy attempt > 1 (chi phí phát sinh khi chạy lại)
    runs_lai = runs[runs['attempt'] > 1]
    cp_lai_token = (runs_lai['tokens_in'] / 1000 * GIA_VAO + runs_lai['tokens_out'] / 1000 * GIA_RA).sum()
    cp_lai_tool = (runs_lai['tool_calls'] * GIA_TOOL).sum()
    cp_lam_lai_phan = cp_lai_token + cp_lai_tool
    print(f'  {"lam_lai_phan":12s} {cp_lam_lai_phan:>14,.0f}  (token+tool của attempt>1)')

    hoa_don_token_tool = (ket_qua['token'] + ket_qua['tool']) / len(reqs)
    print(f'\n  Hoá đơn token+tool chia số yêu cầu: {hoa_don_token_tool:,.0f} đ')
    print(f'  Chi phí mỗi việc thành công (cps):  {ket_qua["cps"]:,.0f} đ')
    print(f'  cps gấp hóa đơn: {ket_qua["cps"] / hoa_don_token_tool:.2f} lần')
    print()

    # ---- A3: Tách theo loại yêu cầu ----
    print('=' * 55)
    print('A3 · Chi phí tách theo loại yêu cầu')
    print('=' * 55)
    print(f'  {"Loại":<12} {"Số YC":>7} {"Thành công":>12} {"Tỉ lệ TC":>10} {"Lần chạy/YC":>13} {"CPS (đ)":>12} {"So 12.000":>10}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        kq = mo_hinh_theo_loai(runs, reqs, loai)
        q_l = reqs[reqs['loai'] == loai]
        r_l = runs[runs['request_id'].isin(q_l['request_id'])]
        n = len(q_l)
        tc = kq['thanh_cong']
        ti_le = tc / n
        lan_chay = len(r_l) / n
        cps = kq['cps']
        print(f'  {loai:<12} {n:>7} {tc:>12} {ti_le:>10.1%} {lan_chay:>13.2f} {cps:>12,.0f} {cps/BASELINE:>10.2f}x')
    print()

    # ---- A4: Chi phí cố định (phạm vi noi_dia + hang_nang) ----
    print('=' * 55)
    print('A4 · Chi phí cố định (noi_dia + hang_nang)')
    print('=' * 55)
    kq_nd = mo_hinh_theo_loai(runs, reqs, 'noi_dia')
    kq_hn = mo_hinh_theo_loai(runs, reqs, 'hang_nang')
    # Tỉ lệ noi_dia+hang_nang trong tổng
    n_nd_hn = len(reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])])
    n_total = len(reqs)
    ty_le_nd_hn = n_nd_hn / n_total

    for khoi_luong, nhan in [(45_000, '45.000/tháng'), (22_500, 'Nửa khối lượng')]:
        # Số việc thành công mỗi tháng (tỉ lệ từ sample)
        ti_le_tc_nd = kq_nd['thanh_cong'] / len(reqs[reqs['loai'] == 'noi_dia'])
        ti_le_tc_hn = kq_hn['thanh_cong'] / len(reqs[reqs['loai'] == 'hang_nang'])
        # Ước lượng tỉ lệ nd+hn trong tổng
        n_nd = len(reqs[reqs['loai'] == 'noi_dia'])
        n_hn = len(reqs[reqs['loai'] == 'hang_nang'])
        ty_le_nd = n_nd / n_total
        ty_le_hn = n_hn / n_total
        viec_tc = khoi_luong * (ty_le_nd * ti_le_tc_nd + ty_le_hn * ti_le_tc_hn)
        cp_co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_tc
        # CPS biến đổi trung bình (trọng số)
        kq_nd_cps = kq_nd['cps']
        kq_hn_cps = kq_hn['cps']
        cps_trung_binh = (kq_nd_cps * ti_le_tc_nd * ty_le_nd + kq_hn_cps * ti_le_tc_hn * ty_le_hn) / \
                         (ti_le_tc_nd * ty_le_nd + ti_le_tc_hn * ty_le_hn)
        cps_tong = cps_trung_binh + cp_co_dinh_moi_viec
        print(f'  {nhan}: việc TC/tháng={viec_tc:,.0f} | CP cố định/việc={cp_co_dinh_moi_viec:,.0f} đ | CPS+CĐ={cps_tong:,.0f} đ ({cps_tong/BASELINE:.2f}x)')
    print()

    # ---- B1: Độ nhạy – đổi từng yếu tố ----
    print('=' * 55)
    print('B1 · Bảng độ nhạy – đổi từng yếu tố')
    print('=' * 55)
    base = mo_hinh(runs, reqs)
    base_cps = base['cps']

    scenarios = [
        ('Giá token gấp đôi',        dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa',    dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi',    dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi',    dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%',  dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần',        dict(max_lan_chay=1)),
    ]

    print(f'  {"Kịch bản":<35} {"CPS (đ)":>12} {"Thay đổi (%)":>14}')
    print(f'  {"Cơ sở (baseline)":<35} {base_cps:>12,.0f} {"0.00%":>14}')
    b1_by_factor = {}
    for ten, kwargs in scenarios:
        kq = mo_hinh(runs, reqs, **kwargs)
        pct = (kq['cps'] - base_cps) / base_cps * 100
        print(f'  {ten:<35} {kq["cps"]:>12,.0f} {pct:>+13.2f}%')
        # Các kịch bản của cùng một yếu tố dùng cùng tham số đầu tiên.
        factor = next(iter(kwargs))
        if factor not in b1_by_factor or abs(pct) > abs(b1_by_factor[factor][1]):
            b1_by_factor[factor] = (ten, pct)
    print()

    # ---- B2: Đổi một cặp + xếp hạng ----
    print('=' * 55)
    print('B2 · Đổi một cặp + xếp hạng yếu tố ảnh hưởng')
    print('=' * 55)
    kq_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    pct_cap = (kq_cap['cps'] - base_cps) / base_cps * 100
    print(f'  Giá token gấp đôi + xem lại gấp đôi: CPS={kq_cap["cps"]:,.0f} đ ({pct_cap:+.2f}%)')

    # Xếp hạng từng yếu tố theo kịch bản có thay đổi tuyệt đối lớn nhất.
    ranking = sorted(b1_by_factor.values(), key=lambda result: abs(result[1]), reverse=True)
    print(f'  Xếp hạng ba yếu tố ảnh hưởng mạnh nhất:')
    for i, (ten, pct) in enumerate(ranking[:3], 1):
        print(f'    {i}. {ten}: {pct:+.2f}%')
    print()

    # ---- B3: Giới hạn chạy lại có thật sự rẻ hơn ----
    print('=' * 55)
    print('B3 · Giới hạn số lần chạy')
    print('=' * 55)
    print(f'  {"Giới hạn":<10} {"Tổng CP trợ lý":>16} {"YC không TC":>13} {"CP cả hệ thống":>16} {"CPS":>12}')
    for lim in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=lim)
        q_lim = reqs.copy()
        q_lim.loc[q_lim['so_lan_chay'] > lim, 'ket_qua'] = 'chuyen_nhan_vien'
        yc_khong_tc = (q_lim['ket_qua'] != 'thanh_cong').sum()
        cp_nv_xu_ly = yc_khong_tc * BASELINE  # nhân viên xử lý phần không thành công
        cp_he_thong = kq['tong'] + cp_nv_xu_ly
        print(f'  {lim} lần{"":<5} {kq["tong"]:>16,.0f} {yc_khong_tc:>13,} {cp_he_thong:>16,.0f} {kq["cps"]:>12,.0f}')
    print()

    # ---- B4: Xem lại 100% (noi_dia + hang_nang) ----
    print('=' * 55)
    print('B4 · Nếu xem lại 100% (noi_dia + hang_nang)')
    print('=' * 55)
    q_nd_hn = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    r_nd_hn = runs[runs['request_id'].isin(q_nd_hn['request_id'])]
    
    # 1. Yêu cầu có ít nhất một lần chạy status = ok
    req_co_ok = r_nd_hn[r_nd_hn['status'] == 'ok']['request_id'].unique()
    so_yc_xem_lai = len(set(req_co_ok).intersection(set(q_nd_hn['request_id'])))
    # Giả định đề bài: mỗi yêu cầu xem lại 5 phút -> 5 * 2.000 = 10.000 đ
    cp_xem_lai_100 = so_yc_xem_lai * 5 * LUONG_PHUT
    
    # 2. Số ca làm lại
    so_ca_lam_lai = (q_nd_hn['ket_qua'] == 'lam_lai').sum()
    cp_lam_lai_9m = so_ca_lam_lai * 9 * LUONG_PHUT
    cp_lam_lai_15m3 = so_ca_lam_lai * 15.3 * LUONG_PHUT
    
    # 3. Token + tool của mọi lần chạy thuộc 982 yêu cầu
    cp_token_tool_nd_hn = (r_nd_hn['tokens_in'] / 1000 * GIA_VAO + 
                           r_nd_hn['tokens_out'] / 1000 * GIA_RA + 
                           r_nd_hn['tool_calls'] * GIA_TOOL).sum()
    
    # 4. Số việc thành công
    so_tc_nd_hn = (q_nd_hn['ket_qua'] == 'thanh_cong').sum()
    
    tong_9m = cp_token_tool_nd_hn + cp_xem_lai_100 + cp_lam_lai_9m
    cps_9m = tong_9m / so_tc_nd_hn
    
    tong_15m3 = cp_token_tool_nd_hn + cp_xem_lai_100 + cp_lam_lai_15m3
    cps_15m3 = tong_15m3 / so_tc_nd_hn
    
    print(f'  Số yêu cầu xem lại (có lần ok): {so_yc_xem_lai}')
    print(f'  Số việc thành công: {so_tc_nd_hn}')
    print(f'  Với 9 phút làm lại/ca:   CPS = {cps_9m:,.0f} đ ({cps_9m/BASELINE:.2f}x so với {BASELINE:,} đ)')
    print(f'  Với 15.3 phút làm lại/ca: CPS = {cps_15m3:,.0f} đ ({cps_15m3/BASELINE:.2f}x so với {BASELINE:,} đ)')
    print()

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
