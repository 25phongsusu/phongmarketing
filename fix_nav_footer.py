import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation
old_desktop_nav = '''<nav class="desktop-nav" aria-label="Điều hướng chính">
          <a href="#how-i-think">Tư duy</a>
          <a href="#case-studies">Dự án</a>
          <a href="#system">Hệ thống</a>
        </nav>'''
new_desktop_nav = '''<nav class="desktop-nav" aria-label="Điều hướng chính">
          <a href="#how-i-think">Tư duy</a>
          <a href="#case-studies">Case Studies</a>
          <a href="#system">Hệ thống</a>
          <a href="#real-data">Số liệu thực tế</a>
        </nav>'''

old_mobile_nav = '''<nav class="mobile-menu" id="mobile-menu" aria-label="Điều hướng di động">
      <a href="#how-i-think">Tư duy</a>
      <a href="#case-studies">Dự án</a>
      <a href="#system">Hệ thống</a>
    </nav>'''
new_mobile_nav = '''<nav class="mobile-menu" id="mobile-menu" aria-label="Điều hướng di động">
      <a href="#how-i-think">Tư duy</a>
      <a href="#case-studies">Case Studies</a>
      <a href="#system">Hệ thống</a>
      <a href="#real-data">Số liệu thực tế</a>
    </nav>'''

html = html.replace(old_desktop_nav, new_desktop_nav)
html = html.replace(old_mobile_nav, new_mobile_nav)

# 2. Update Footer Email Link
# The user wants "thực hiện gửi mail" which might just mean opening the mailto with a pre-filled subject, 
# or maybe they want it to explicitly open Gmail. I'll use the Gmail web intent for reliability, 
# as some users don't have default mail apps set up on Windows.
old_footer = '<a href="mailto:phongpdt.work@gmail.com">phongpdt.work@gmail.com</a>'
new_footer = '<a href="https://mail.google.com/mail/?view=cm&fs=1&to=phongpdt.work@gmail.com&su=Trao%20đổi%20về%20bài%20toán%20Marketing" target="_blank" rel="noopener noreferrer" style="text-decoration: underline; text-underline-offset: 4px; color: var(--ink);">phongpdt.work@gmail.com</a>'
html = html.replace(old_footer, new_footer)

# Also update the header email link just in case
old_header_email = '<a class="wordmark" href="mailto:phongpdt.work@gmail.com" aria-label="Gửi email cho Phong PDT">phongpdt.work@gmail.com</a>'
new_header_email = '<a class="wordmark" href="https://mail.google.com/mail/?view=cm&fs=1&to=phongpdt.work@gmail.com&su=Trao%20đổi%20về%20bài%20toán%20Marketing" target="_blank" rel="noopener noreferrer" aria-label="Gửi email cho Phong PDT">phongpdt.work@gmail.com</a>'
html = html.replace(old_header_email, new_header_email)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated nav and email links")
