import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '  <!-- Contact Modal -->'
end_marker = '  <script>'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_modal = '''  <!-- Contact Modal -->
  <div id="contact-modal" class="lightbox" aria-hidden="true">
    <div class="lightbox-overlay contact-close" tabindex="-1"></div>
    <div class="lightbox-content" style="background: var(--paper); padding: 48px 32px; border-radius: 12px; width: 90%; max-width: 400px; display: flex; flex-direction: column; text-align: center; position: relative;">
      <button class="lightbox-close contact-close" aria-label="Đóng" style="color: var(--muted); top: 12px; right: 20px; font-size: 2.2rem; z-index: 10;">&times;</button>
      <h3 style="margin-top: 0; font-size: 1.6rem; margin-bottom: 32px; color: var(--ink);">Bắt đầu trò chuyện</h3>
      <div style="display: flex; flex-direction: column; gap: 16px; width: 100%;">
        <a href="mailto:phongpdt.work@gmail.com?subject=Trao đổi về bài toán Marketing" class="button" style="width: 100%; justify-content: center;">Qua Email</a>
        <a href="https://zalo.me/0705157813" target="_blank" class="button" style="width: 100%; justify-content: center; background: #0068ff; border-color: #0068ff; color: #fff;">Qua Zalo: 0705157813</a>
        <a href="tel:0813467885" class="button" style="width: 100%; justify-content: center; background: #2f3640; border-color: #2f3640; color: #fff;">Gọi trực tiếp: 0813467885</a>
      </div>
    </div>
  </div>

'''
html = html[:start_idx] + new_modal + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
