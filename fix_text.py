import os

files = {
    'mockup_dashboard.svg': [
        ('Last updated: Just now', 'Cập nhật: Vừa xong'),
        ('Total Doanh Thu', 'Tổng Doanh Thu'),
        ('Doanh Thu vs Spend (30 Days)', 'Doanh Thu vs Chi Phí (30 Ngày)'),
        ('T ng Chi PhA-', 'Tổng Chi Phí'),
        ('Tng NgAn SAch', 'Tăng Ngân Sách'),
        ('PHM PHONG', 'PHẠM PHONG'),
        ('Ac Phm Phong', '© Phạm Phong')
    ],
    'mockup_ab_test.svg': [
        ('M U C', 'MẪU CŨ'),
        ('M U MsI', 'MẪU MỚI'),
        ('NASU RA  GIA? &amp; I?U KI+N', 'NÊU RÕ GIÁ &amp; ĐIỀU KIỆN'),
        ('Tin nh_n thu v?:', 'Tin nhắn thu về:'),
        ('?n hAng ch	:', 'Đơn hàng chốt:'),
        ('T l ch	:', 'Tỷ lệ chốt:'),
        ('L OC KHA?CH', 'LỌC KHÁCH'),
        ('PHM PHONG', 'PHẠM PHONG'),
        ('Ac Phm Phong', '© Phạm Phong')
    ],
    'mockup_testing_matrix.svg': [
        ('PHASE 1: INSIGHT', 'GĐ 1: INSIGHT'),
        ('PHASE 2: VISUAL (Current)', 'GĐ 2: HÌNH ẢNH (Hiện tại)'),
        ('PHASE 3: SCALE', 'GĐ 3: VÍT ADS'),
        ('Insight A: Tit kim', 'Insight A: Tiết kiệm'),
        ('WINNER', 'THẮNG'),
        ('KILLED', 'ĐÃ TẮT'),
        ('TESTING...', 'ĐANG TEST...'),
        ('Winning Combo', 'Mẫu Win'),
        ('LOCKED', 'ĐÃ CHỐT'),
        ('nh: Feedback', 'Ảnh: Feedback'),
        ('QUY TRAONH TH NGHI+M', 'QUY TRÌNH THỬ NGHIỆM'),
        ('PHM PHONG', 'PHẠM PHONG'),
        ('Ac Phm Phong', '© Phạm Phong')
    ]
}

for f, rules in files.items():
    filepath = 'Screenshots/' + f
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try regex fix for mangled text
    import re
    # Fix mockup_ab_test
    content = re.sub(r'M.U C.. \(CONTENT CHUNG CHUNG\)', 'MẪU CŨ (CONTENT CHUNG CHUNG)', content)
    content = re.sub(r'M.U M.sI \(.*?\)', 'MẪU MỚI (NÊU RÕ GIÁ &amp; ĐIỀU KIỆN)', content)
    content = re.sub(r'Tin nh.*n thu v.*?:', 'Tin nhắn thu về:', content)
    content = re.sub(r'.*n hAng ch.*t:', 'Đơn hàng chốt:', content)
    content = re.sub(r'T. l. ch.*t:', 'Tỷ lệ chốt:', content)
    content = re.sub(r'L.OC KHA.CH T. CONTENT', 'LỌC KHÁCH TỪ CONTENT', content)
    
    # Fix testing matrix
    content = re.sub(r'QUY TRAONH TH. NGHI.M.*', 'QUY TRÌNH THỬ NGHIỆM (LOW BUDGET)</text>', content)
    content = re.sub(r'Insight A: Ti.*t ki.*m', 'Insight A: Tiết kiệm', content)
    content = re.sub(r'.nh: Feedback', 'Ảnh: Feedback', content)
    
    # Fix dashboard
    content = re.sub(r'T. ng Chi PhA-', 'Tổng Chi Phí', content)
    content = re.sub(r'T.ng NgA.n SA.ch', 'Tăng Ngân Sách', content)

    # Fix watermarks
    content = re.sub(r'PH.M PHONG', 'PHẠM PHONG', content)
    content = re.sub(r'Ac Ph.m Phong', '© Phạm Phong', content)

    # Apply static rules
    for old, new in rules:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
