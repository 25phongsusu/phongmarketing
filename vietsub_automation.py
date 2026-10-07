filepath = 'Screenshots/mockup_automation.svg'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('Trigger Event', 'Bắt sự kiện'),
    ('Data Parsing', 'Xử lý Dữ liệu'),
    ('Format &amp; Filter', 'Định dạng &amp; Lọc'),
    ('Update Tracking', 'Cập nhật File'),
    ('Auto Follow-up', 'Gửi tin Tự động'),
    ('Workflow Active', 'Workflow: Đang chạy')
]
for old, new in replacements:
    content = content.replace(old, new)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
