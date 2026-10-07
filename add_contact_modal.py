import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the contact button
old_button = '<a class="button" href="mailto:phongpdt.work@gmail.com?subject=Trao%20đổi%20về%20bài%20toán%20Marketing">Bắt đầu trò chuyện</a>'
new_button = '<button class="button" id="btn-open-contact">Bắt đầu trò chuyện</button>'
html = html.replace(old_button, new_button)

# 2. Add Modal HTML before <script>
modal_html = '''  <!-- Contact Modal -->
  <div id="contact-modal" class="lightbox" aria-hidden="true">
    <div class="lightbox-overlay contact-close" tabindex="-1"></div>
    <div class="lightbox-content" style="background: var(--paper); padding: 40px; border-radius: 12px; width: 90%; max-width: 400px; text-align: center; position: relative;">
      <button class="lightbox-close contact-close" aria-label="Đóng" style="color: var(--ink); top: 16px; right: 16px; font-size: 2rem;">&times;</button>
      <h3 style="margin-top: 0; font-size: 1.6rem; margin-bottom: 24px; color: var(--ink);">Bắt đầu trò chuyện</h3>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <a href="mailto:phongpdt.work@gmail.com?subject=Trao đổi về bài toán Marketing" class="button" style="width: 100%; justify-content: center;">Qua Email</a>
        <a href="https://zalo.me/0705157813" target="_blank" class="button" style="width: 100%; justify-content: center; background: #0068ff; border-color: #0068ff;">Qua Zalo: 0705157813</a>
        <a href="tel:0813467885" class="button" style="width: 100%; justify-content: center; background: #2f3640; border-color: #2f3640;">Gọi trực tiếp: 0813467885</a>
      </div>
    </div>
  </div>

  <script>'''
html = html.replace('  <script>', modal_html)

# 3. Add JS logic
js_logic = '''
    // Contact Modal Logic
    const contactModal = document.getElementById('contact-modal');
    const btnOpenContact = document.getElementById('btn-open-contact');
    
    if(btnOpenContact) {
      btnOpenContact.addEventListener('click', () => {
        contactModal.classList.add('is-open');
        document.body.classList.add('menu-open');
      });
    }

    document.querySelectorAll('.contact-close').forEach(el => {
      el.addEventListener('click', () => {
        contactModal.classList.remove('is-open');
        if (!document.getElementById('lightbox').classList.contains('is-open') && !document.querySelector('.mobile-menu').classList.contains('is-open')) {
          document.body.classList.remove('menu-open');
        }
      });
    });
'''
html = html.replace('// Lightbox Logic', js_logic + '\n    // Lightbox Logic')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
