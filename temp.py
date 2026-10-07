import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

real_data_start = html.find('<section id="real-data"')
real_data_end = html.find('<!-- 05 BUILDING THE SYSTEM -->')
real_data_html = html[real_data_start:real_data_end].strip()

footer_start = html.find('</main>')

new_system_html = '''    <!-- 05 BUILDING THE SYSTEM -->
    <section class="section" id="system">
      <div class="shell">
        <header class="section-heading reveal">
          <h2>Hệ thống tôi đã xây</h2>
          <p>Không nói lý thuyết. Dưới đây là 2 công cụ cốt lõi tôi tự xây dựng bằng Python và Automation để loại bỏ việc thủ công và tối ưu chi phí cho doanh nghiệp.</p>
        </header>

        <div class="cases-grid reveal">
          <div class="case-card">
            <div>
              <div class="case-meta">TOOL 01 &mdash; DATA ENGINEERING</div>
              <h3 class="case-title" style="margin-bottom: 12px; font-size: 1.6rem;">Growth Dashboard v2.0</h3>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 8px;"><strong>Vấn đề:</strong> Phải tải số liệu từ FB Ads, TikTok, và KiotViet bằng tay mỗi ngày để tính CIR.</p>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 16px;"><strong>Giải pháp:</strong> Code script Python lấy Data tự động qua API, làm sạch dữ liệu và đẩy lên Looker Studio.</p>
              <p style="color: var(--accent); font-weight: 700; font-size: 1rem;">Tiết kiệm: ~10h làm báo cáo/tuần.</p>
            </div>
            <div class="proof-gallery">
              <img src="Screenshots/mockup_dashboard.svg" alt="Growth Dashboard" loading="lazy" style="height: 100%; object-fit: cover;">
            </div>
          </div>
          <div class="case-card">
            <div>
              <div class="case-meta">TOOL 02 &mdash; WORKFLOW AUTOMATION</div>
              <h3 class="case-title" style="margin-bottom: 12px; font-size: 1.6rem;">Zalo ZNS Lead Routing</h3>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 8px;"><strong>Vấn đề:</strong> Khách để lại số điện thoại nhưng Sales gọi chậm, dẫn đến rớt đơn.</p>
              <p style="color: var(--muted); font-size: 1rem; margin-bottom: 16px;"><strong>Giải pháp:</strong> Dùng n8n bắt form từ FB, chia Lead thẳng về Google Sheets của Sales và tự động gửi tin nhắn chào mừng Zalo ZNS trong 5 giây.</p>
              <p style="color: var(--accent); font-weight: 700; font-size: 1rem;">Kết quả: Tăng 25% tỷ lệ kết nối thành công.</p>
            </div>
            <div class="proof-gallery">
              <img src="Screenshots/mockup_automation.svg" alt="Zalo Automation" loading="lazy" style="height: 100%; object-fit: cover;">
            </div>
          </div>
        </div>
      </div>
    </section>'''

new_contact_html = '''    <!-- 07 CLOSING -->
    <section class="section punchline" id="contact" style="border-bottom: none;">
      <div class="shell text-center reveal">
        <div class="capability-list" style="margin-bottom: 48px; justify-content: center;">
          <div class="cap-item">Performance Marketing</div>
          <div class="cap-item">Data &amp; Analytics</div>
          <div class="cap-item">Automation</div>
        </div>
        
        <blockquote>
          <span class="quiet">Marketing giúp tôi hiểu khách hàng.</span><br>
          <span class="quiet">Engineering giúp tôi tiếp cận họ tốt hơn.</span><br>
          <span class="loud">Đây là lý do tôi kết hợp cả hai.</span>
        </blockquote>

        <div class="contact-box reveal">
          <h3>Bạn đang có một bài toán Marketing?</h3>
          <p>Tôi không bắt đầu bằng việc bán một gói dịch vụ.<br>Tôi bắt đầu bằng việc hiểu bài toán.</p>
          <a class="button" href="mailto:phongpdt.work@gmail.com?subject=Trao%20đổi%20về%20bài%20toán%20Marketing">Bắt đầu trò chuyện</a>
        </div>
      </div>
    </section>

  </main>'''

new_html = html[:real_data_start] + new_system_html + '\n\n    <!-- 06 REAL DATA -->\n    ' + real_data_html + '\n\n' + new_contact_html + html[footer_start+7:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

