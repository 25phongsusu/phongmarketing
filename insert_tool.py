import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update header text
html = html.replace('2 công cụ cốt lõi', '3 hệ thống cốt lõi')

# Find where Tool 2 ends
tool2_end_marker = 'Screenshots/mockup_automation.svg" alt="Zalo Automation" loading="lazy" style="height: 100%; object-fit: cover;">\n            </div>\n          </div>'
tool2_end_idx = html.find(tool2_end_marker)

if tool2_end_idx != -1:
    insert_idx = tool2_end_idx + len(tool2_end_marker)
    tool3_html = '''
          <div class="case-card">
            <div>
              <div class="case-meta">TOOL 03 &mdash; AI &amp; CONTENT ANALYTICS</div>
              <h3 class="case-title" style="margin-bottom: 12px; font-size: 1.6rem;">AI Creative Analyst</h3>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 8px;"><strong>Vấn đề:</strong> Chạy hàng trăm mẫu quảng cáo nhưng không rõ vì sao mẫu đó "win" (do Hook, hay tiêu đề?).</p>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 16px;"><strong>Giải pháp:</strong> Dùng Python kéo Data Ads &rarr; gọi API OpenAI bóc tách tự động Hook, Cảm xúc &rarr; đổ về Google Sheets.</p>
              <p style="color: var(--accent); font-weight: 700; font-size: 1rem;">Kết quả: Tìm ra "công thức nội dung" có tỷ lệ chuyển đổi cao nhất.</p>
            </div>
            <div class="proof-gallery">
              <img src="Screenshots/mockup_ai_creative.svg" alt="AI Creative Analyst" loading="lazy" style="height: 100%; object-fit: cover;">
            </div>
          </div>'''
    
    html = html[:insert_idx] + tool3_html + html[insert_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Failed to find Tool 2 marker")
