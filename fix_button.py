with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<button class="button" id="btn-open-contact">', '<a class="button" id="btn-open-contact" href="javascript:void(0)">')
html = html.replace('Bắt đầu trò chuyện</button>', 'Bắt đầu trò chuyện</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
