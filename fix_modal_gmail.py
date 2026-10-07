with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_href = 'href="mailto:phongpdt.work@gmail.com?subject=Trao đổi về bài toán Marketing"'
new_href = 'href="https://mail.google.com/mail/?view=cm&fs=1&to=phongpdt.work@gmail.com&su=Trao%20đổi%20về%20bài%20toán%20Marketing" target="_blank"'

html = html.replace(old_href, new_href)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
