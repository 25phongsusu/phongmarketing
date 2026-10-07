import glob

replacements = {
    'mockup_ab_test.svg': [
        ('Conv. Rate:', 'Tỷ lệ chốt:'),
        ('Sales:', 'Đơn hàng:'),
        ('Status: PAUSED', 'Trạng thái: ĐÃ TẮT'),
        ('Status: SCALING', 'Trạng thái: ĐANG SCALE')
    ],
    'mockup_dashboard.svg': [
        ('Total Spend', 'Tổng Chi Phí'),
        ('Revenue', 'Doanh Thu'),
        ('Scale up Ads', 'Tăng Ngân Sách'),
        ('Rev +45%', 'Doanh thu +45%')
    ],
    'mockup_automation.svg': [
        ('Data Formatter', 'Xử Lý Dữ Liệu'),
        ('New Lead', 'Có Lead Mới'),
        ('Clean data', 'Chuẩn Hóa'),
        ('Add row', 'Thêm Dòng Mới'),
        ('Send Template', 'Gửi Tin Chăm Sóc'),
        ('>Trigger<', '>Bắt Đầu<'),
        ('>Action<', '>Hành Động<'),
        ('>Success<', '>Thành Công<')
    ],
    'mockup_testing_matrix.svg': [
        ('TESTING PIPELINE', 'QUY TRÌNH THỬ NGHIỆM'),
        ('Phase 1: Concept', 'Giai đoạn 1: Thông điệp'),
        ('Phase 2: Visual', 'Giai đoạn 2: Hình ảnh'),
        ('Phase 3: Scale', 'Giai đoạn 3: Mở rộng'),
        ('Insight A (Pain point)', 'Insight A (Nỗi đau)'),
        ('Insight B (Desire)', 'Insight B (Mong muốn)'),
        ('Winner: Insight A', 'Mẫu Thắng: Insight A'),
        ('Video vs Image', 'Video vs Ảnh'),
        ('Winner: Video (CPL -30%)', 'Thắng: Video (CPL rẻ hơn 30%)'),
        ('Increase Budget +20%/day', 'Tăng ngân sách +20%/ngày'),
        ('Monitor CIR &lt; 15%', 'Kiểm soát CIR &lt; 15%'),
        ('Monitor CIR < 15%', 'Kiểm soát CIR < 15%')
    ]
}

for filename, rules in replacements.items():
    filepath = f'Screenshots/{filename}'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_txt, new_txt in rules:
            content = content.replace(old_txt, new_txt)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

