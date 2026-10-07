import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '  <!-- Contact Modal -->'
end_marker = '  <script>'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers")
    sys.exit(1)

new_modal = '''  <!-- High-End Contact Modal -->
  <style>
    .contact-modal-shell {
      background: var(--paper);
      padding: 8px;
      border-radius: 2rem;
      width: 90%;
      max-width: 420px;
      position: relative;
      box-shadow: 0 40px 80px -20px rgba(0,0,0,0.5);
      border: 1px solid rgba(128,128,128,0.1);
      transform: translateY(20px);
      opacity: 0;
      transition: all 0.6s cubic-bezier(0.32,0.72,0,1);
    }
    .lightbox.is-open .contact-modal-shell {
      transform: translateY(0);
      opacity: 1;
    }
    .contact-modal-core {
      background: var(--paper);
      border-radius: calc(2rem - 8px);
      padding: 48px 32px;
      display: flex;
      flex-direction: column;
      text-align: center;
      border: 1px solid rgba(128,128,128,0.05);
    }
    .contact-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      border-radius: 999px;
      background: rgba(128,128,128,0.04);
      border: 1px solid rgba(128,128,128,0.08);
      text-decoration: none;
      color: var(--ink);
      transition: all 0.4s cubic-bezier(0.32,0.72,0,1);
      cursor: pointer;
    }
    .contact-btn:hover {
      background: var(--ink);
      color: var(--paper);
      transform: scale(0.98);
      border-color: var(--ink);
    }
    .contact-btn-icon {
      width: 44px;
      height: 44px;
      flex-shrink: 0;
      border-radius: 50%;
      background: var(--paper);
      color: var(--ink);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.05);
      border: 1px solid rgba(128,128,128,0.1);
      transition: all 0.4s cubic-bezier(0.32,0.72,0,1);
      font-size: 1.2rem;
    }
    .contact-btn:hover .contact-btn-icon {
      transform: scale(1.05);
    }
    .contact-btn-text {
      text-align: left;
      margin-left: 16px;
      flex-grow: 1;
    }
    .contact-btn-title {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 2px;
    }
    .contact-btn-sub {
      font-size: 0.75rem;
      color: var(--muted);
      font-family: monospace;
      letter-spacing: 0.05em;
    }
    .contact-btn-arrow {
      width: 36px;
      height: 36px;
      flex-shrink: 0;
      border-radius: 50%;
      border: 1px solid rgba(128,128,128,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      transition: all 0.4s cubic-bezier(0.32,0.72,0,1);
    }
    .contact-btn:hover .contact-btn-arrow {
      background: var(--paper);
      color: var(--ink);
      border-color: var(--paper);
      transform: translate(2px, -2px);
    }
    .contact-close-btn {
      position: absolute;
      top: 24px;
      right: 24px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(128,128,128,0.1);
      color: var(--ink);
      border: none;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: all 0.3s ease;
      padding: 0;
    }
    .contact-close-btn:hover {
      background: var(--ink);
      color: var(--paper);
      transform: rotate(90deg);
    }
  </style>

  <div id="contact-modal" class="lightbox" aria-hidden="true">
    <div class="lightbox-overlay contact-close" tabindex="-1"></div>
    <div class="contact-modal-shell">
      <div class="contact-modal-core">
        <button class="contact-close-btn contact-close" aria-label="Đóng">✕</button>
        
        <div style="display: inline-block; padding: 6px 16px; border-radius: 999px; border: 1px solid rgba(128,128,128,0.2); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; color: var(--muted); margin: 0 auto 24px auto;">
          Kết nối
        </div>

        <h3 style="margin: 0 0 40px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.04em; color: var(--ink); line-height: 1.1;">
          Bắt đầu<br><span style="color: var(--muted); font-weight: 400;">trò chuyện.</span>
        </h3>

        <div style="display: flex; flex-direction: column; gap: 12px; width: 100%;">
          
          <!-- Email -->
          <a href="mailto:phongpdt.work@gmail.com?subject=Trao đổi về bài toán Marketing" class="contact-btn">
            <div class="contact-btn-icon">@</div>
            <div class="contact-btn-text">
              <div class="contact-btn-title">Gửi Email</div>
              <div class="contact-btn-sub">phongpdt.work</div>
            </div>
            <div class="contact-btn-arrow">↗</div>
          </a>

          <!-- Zalo -->
          <a href="https://zalo.me/0705157813" target="_blank" class="contact-btn">
            <div class="contact-btn-icon" style="color: #0068ff; font-weight: 900;">Z</div>
            <div class="contact-btn-text">
              <div class="contact-btn-title">Nhắn Zalo</div>
              <div class="contact-btn-sub">0705.157.813</div>
            </div>
            <div class="contact-btn-arrow">↗</div>
          </a>

          <!-- Phone -->
          <a href="tel:0813467885" class="contact-btn">
            <div class="contact-btn-icon">✆</div>
            <div class="contact-btn-text">
              <div class="contact-btn-title">Gọi trực tiếp</div>
              <div class="contact-btn-sub">0813.467.885</div>
            </div>
            <div class="contact-btn-arrow">↗</div>
          </a>

        </div>
      </div>
    </div>
  </div>

'''

html = html[:start_idx] + new_modal + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
