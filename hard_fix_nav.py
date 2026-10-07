import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix desktop nav
html = re.sub(
    r'<nav class="desktop-nav" aria-label=".*?">.*?</nav>',
    '''<nav class="desktop-nav" aria-label="Điều hướng chính">
          <a href="#how-i-think">Tư duy</a>
          <a href="#case-studies">Case Studies</a>
          <a href="#system">Hệ thống</a>
          <a href="#real-data">Thực tế</a>
        </nav>''',
    html,
    flags=re.DOTALL
)

# Fix mobile nav
html = re.sub(
    r'<nav class="mobile-menu" id="mobile-menu" aria-label=".*?">.*?</nav>',
    '''<nav class="mobile-menu" id="mobile-menu" aria-label="Điều hướng di động">
      <a href="#how-i-think">Tư duy</a>
      <a href="#case-studies">Case Studies</a>
      <a href="#system">Hệ thống</a>
      <a href="#real-data">Thực tế</a>
    </nav>''',
    html,
    flags=re.DOTALL
)

# Fix footer email
html = re.sub(
    r'<a href="mailto:phongpdt.work@gmail.com">phongpdt.work@gmail.com</a>',
    '<a href="https://mail.google.com/mail/?view=cm&fs=1&to=phongpdt.work@gmail.com&su=Trao%20đổi%20về%20bài%20toán%20Marketing" target="_blank" rel="noopener noreferrer" style="text-decoration: underline; text-underline-offset: 4px; color: var(--ink);">phongpdt.work@gmail.com</a>',
    html
)

# Fix header email
html = re.sub(
    r'<a class="wordmark" href="mailto:phongpdt.work@gmail.com" aria-label=".*?">phongpdt.work@gmail.com</a>',
    '<a class="wordmark" href="https://mail.google.com/mail/?view=cm&fs=1&to=phongpdt.work@gmail.com&su=Trao%20đổi%20về%20bài%20toán%20Marketing" target="_blank" rel="noopener noreferrer" aria-label="Gửi email cho Phong PDT">phongpdt.work@gmail.com</a>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Regex replace applied.")
