svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="800" height="400">
  <rect width="800" height="400" fill="#1a1a17"/>
  
  <rect x="40" y="40" width="720" height="40" fill="#25241f" rx="6"/>
  <text x="60" y="65" fill="#a9a79f" font-family="monospace" font-size="12">OPENAI CREATIVE ANALYSIS LOGS</text>
  <text x="740" y="65" fill="#4caf50" font-family="monospace" font-size="12" text-anchor="end">Status: LIVE</text>

  <text x="60" y="110" fill="#696861" font-family="monospace" font-size="11">AD_ID</text>
  <text x="180" y="110" fill="#696861" font-family="monospace" font-size="11">AI_DETECTED_HOOK</text>
  <text x="460" y="110" fill="#696861" font-family="monospace" font-size="11">EMOTION_TAG</text>
  <text x="600" y="110" fill="#696861" font-family="monospace" font-size="11">WIN_RATE</text>
  
  <rect x="40" y="130" width="720" height="50" fill="#25241f" rx="4"/>
  <text x="60" y="160" fill="#e4472f" font-family="monospace" font-size="13">#VID_082</text>
  <rect x="180" y="140" width="250" height="30" fill="#121210" rx="4"/>
  <text x="190" y="160" fill="#f0eee8" font-family="sans-serif" font-size="13">"3 sai lầm khiến bạn mất tiền..."</text>
  <rect x="460" y="142" width="100" height="26" fill="#e4472f" fill-opacity="0.2" rx="13"/>
  <text x="510" y="160" fill="#e4472f" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">FEAR</text>
  <text x="600" y="160" fill="#4caf50" font-family="monospace" font-size="14" font-weight="bold">+24.5%</text>

  <rect x="40" y="190" width="720" height="50" fill="#25241f" rx="4"/>
  <text x="60" y="220" fill="#e4472f" font-family="monospace" font-size="13">#IMG_105</text>
  <rect x="180" y="200" width="250" height="30" fill="#121210" rx="4"/>
  <text x="190" y="220" fill="#f0eee8" font-family="sans-serif" font-size="13">"Bí mật đằng sau doanh thu..."</text>
  <rect x="460" y="202" width="100" height="26" fill="#2196f3" fill-opacity="0.2" rx="13"/>
  <text x="510" y="220" fill="#2196f3" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">CURIOSITY</text>
  <text x="600" y="220" fill="#4caf50" font-family="monospace" font-size="14" font-weight="bold">+18.2%</text>

  <rect x="40" y="250" width="720" height="50" fill="#25241f" rx="4"/>
  <text x="60" y="280" fill="#e4472f" font-family="monospace" font-size="13">#VID_011</text>
  <rect x="180" y="260" width="250" height="30" fill="#121210" rx="4"/>
  <text x="190" y="280" fill="#f0eee8" font-family="sans-serif" font-size="13">"Sản phẩm này sẽ giúp bạn..."</text>
  <rect x="460" y="262" width="100" height="26" fill="#9e9e9e" fill-opacity="0.2" rx="13"/>
  <text x="510" y="280" fill="#9e9e9e" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">LOGICAL</text>
  <text x="600" y="280" fill="#e4472f" font-family="monospace" font-size="14" font-weight="bold">-5.4%</text>

  <rect x="520" y="200" width="260" height="150" fill="#121210" rx="8" stroke="#333" stroke-width="1" />
  <circle cx="540" cy="220" r="5" fill="#ff5f56"/>
  <circle cx="555" cy="220" r="5" fill="#ffbd2e"/>
  <circle cx="570" cy="220" r="5" fill="#27c93f"/>
  <text x="540" y="250" fill="#e4472f" font-family="monospace" font-size="11">import</text>
  <text x="590" y="250" fill="#f0eee8" font-family="monospace" font-size="11">openai, pandas</text>
  <text x="540" y="280" fill="#a9a79f" font-family="monospace" font-size="11">def analyze_hook(text):</text>
  <text x="550" y="300" fill="#f0eee8" font-family="monospace" font-size="11">res = openai.ChatCompletion...</text>
  <text x="550" y="320" fill="#f0eee8" font-family="monospace" font-size="11">return res.json()["hook_type"]</text>

  <g opacity="0.06" transform="translate(400, 200) rotate(-20)">
    <text x="0" y="0" fill="#888" font-family="sans-serif" font-weight="900" font-size="80" text-anchor="middle" letter-spacing="8">PHẠM PHONG</text>
  </g>
  <g opacity="0.4">
    <text x="776" y="376" fill="#888" font-family="monospace" font-weight="600" font-size="14" text-anchor="end">© Phạm Phong</text>
  </g>
</svg>'''

with open('Screenshots/mockup_ai_creative.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
