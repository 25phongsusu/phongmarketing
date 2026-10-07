import glob, re

for filepath in glob.glob('Screenshots/mockup_*.svg'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already watermarked
    if 'PHẠM PHONG' in content:
        continue

    # Extract width and height
    w_match = re.search(r'width="(\d+)"', content)
    h_match = re.search(r'height="(\d+)"', content)
    
    if not w_match or not h_match:
        continue
        
    w = int(w_match.group(1))
    h = int(h_match.group(1))
    
    # Calculate center
    cx = w / 2
    cy = h / 2
    
    # Watermark XML
    watermark = f'''
  <!-- Watermark -->
  <g opacity="0.06" transform="translate({cx}, {cy}) rotate(-20)">
    <text x="0" y="0" fill="#888" font-family="sans-serif" font-weight="900" font-size="80" text-anchor="middle" letter-spacing="8">PHẠM PHONG</text>
  </g>
  <g opacity="0.4">
    <text x="{w - 24}" y="{h - 24}" fill="#888" font-family="monospace" font-weight="600" font-size="14" text-anchor="end">© Phạm Phong</text>
  </g>
</svg>'''

    # Replace </svg>
    content = content.replace('</svg>', watermark)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Watermarks added successfully!")
