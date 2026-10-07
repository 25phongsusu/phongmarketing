with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_knt = '''<div style="display: inline-block; padding: 6px 16px; border-radius: 999px; border: 1px solid rgba(128,128,128,0.2); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; color: var(--muted); margin: 0 auto 24px auto;">
          Kết nối
        </div>'''
new_knt = '''<div style="display: inline-block; padding: 6px 16px; border-radius: 999px; border: 1px solid rgba(76, 175, 80, 0.4); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; color: #4caf50; background: rgba(76, 175, 80, 0.08); margin: 0 auto 24px auto;">
          Kết nối
        </div>'''

old_h3 = '''<h3 style="margin: 0 0 40px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.04em; color: var(--ink); line-height: 1.1;">
          Bắt đầu<br><span style="color: var(--muted); font-weight: 400;">trò chuyện.</span>
        </h3>'''
new_h3 = '''<h3 style="margin: 0 0 40px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.04em; color: var(--ink); line-height: 1.3;">
          <span style="background-color: #ff5c39; color: #121210; padding: 2px 8px; display: inline-block; transform: rotate(-2deg); margin-bottom: 4px;">Bắt đầu</span><br><span style="color: var(--muted); font-weight: 400;">trò chuyện.</span>
        </h3>'''

html = html.replace(old_knt, new_knt)
html = html.replace(old_h3, new_h3)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
