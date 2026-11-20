import requests

CLIENT_ID = "4a42aa8a2c68e657d91c2824"
CLIENT_SECRET = "sacs_R8vxQnQNgg--NU9J53bSKKNwDoLlFWVokuNbauRG1ag"
HANDLE = "marigold2003"

url = f"https://solved.ac/api/v4/users/{HANDLE}?lang=ko"
headers = {
    "x-client-id": CLIENT_ID,
    "x-client-secret": CLIENT_SECRET,
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("에러 발생:", response.status_code, response.text)
    exit()

data = response.json()

TIERS = [
    ("Unrated", "#2D2D2D"),
    ("Bronze V", "#AD5600"),
    ("Bronze IV", "#AD5600"),
    ("Bronze III", "#AD5600"),
    ("Bronze II", "#AD5600"),
    ("Bronze I", "#AD5600"),
    ("Silver V", "#435F7A"),
    ("Silver IV", "#435F7A"),
    ("Silver III", "#435F7A"),
    ("Silver II", "#435F7A"),
    ("Silver I", "#435F7A"),
    ("Gold V", "#EC9A00"),
    ("Gold IV", "#EC9A00"),
    ("Gold III", "#EC9A00"),
    ("Gold II", "#EC9A00"),
    ("Gold I", "#EC9A00"),
    ("Platinum V", "#27E2A4"),
    ("Platinum IV", "#27E2A4"),
    ("Platinum III", "#27E2A4"),
    ("Platinum II", "#27E2A4"),
    ("Platinum I", "#27E2A4"),
    ("Diamond V", "#00B4FC"),
    ("Diamond IV", "#00B4FC"),
    ("Diamond III", "#00B4FC"),
    ("Diamond II", "#00B4FC"),
    ("Diamond I", "#00B4FC"),
    ("Ruby V", "#FF0062"),
    ("Ruby IV", "#FF0062"),
    ("Ruby III", "#FF0062"),
    ("Ruby II", "#FF0062"),
    ("Ruby I", "#FF0062"),
    ("Master", "#B491FF"),
]

tier_num = data.get("tier") or 0
tier_name, color = (
    TIERS[tier_num] if 0 <= tier_num < len(TIERS) else ("Unknown", "#17CE3A")
)
rating = data.get("rating", 0)
current_streak = data.get("currentStreak", 0)
max_streak = data.get("maxStreak", 0)

svg_content = f"""<svg width="420" height="160" viewBox="0 0 420 160" fill="none" xmlns="http://w3.org">
  <rect x="2" y="2" width="416" height="156" rx="12" fill="#0D1117" stroke="{color}" stroke-width="2.5"/>
  
  <text x="24" y="42" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold">{HANDLE}</text>
  <text x="396" y="42" fill="{color}" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="bold" text-anchor="end">{tier_name}</text>
  
  <line x1="24" y1="60" x2="396" y2="60" stroke="#30363D" stroke-width="1"/>
  
  <text x="24" y="92" fill="#8B949E" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="bold">RATING</text>
  <text x="24" y="122" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold">{rating:,}</text>
  
  <text x="175" y="92" fill="#8B949E" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="bold">CURRENT STREAK</text>
  <text x="175" y="122" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold">{current_streak} days</text>
  
  <text x="315" y="92" fill="#8B949E" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="bold">MAX STREAK</text>
  <text x="315" y="122" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold">{max_streak} days</text>
</svg>
"""

with open("card.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("✅ 완료! card.svg 파일이 생성되었습니다!")
