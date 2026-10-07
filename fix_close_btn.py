with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('font-size: 2rem;">&times;</button>', 'font-size: 2rem; z-index: 10;">&times;</button>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
