# 로컬에서만 사용 (백준 제출용 아님)
import re, requests
from bs4 import BeautifulSoup

URL = "http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national"  # 문제 출처 아카이브
html = requests.get(URL, timeout=30).text
soup = BeautifulSoup(html, "html.parser")

pairs = []  # (번호, 이름, "타입1 타입2")
for i, dex in enumerate(soup.select(".infocard")):
    no = int(dex.select_one(".infocard-lg-data .text-muted").text.strip("#"))
    name = dex.select_one(".ent-name").text.strip()
    types = " ".join([t.text.strip() for t in dex.select(".aside .itype")])
    if 1 <= no <= 718:
        pairs.append((no, name, types))

# 여기서부터는 '출력 포맷'만 바꾸면 다양한 언어로 생성 가능
print("POKE = {")
for no, name, types in pairs:
    print(f'    {no}: ("{name}", "{types}"),')
print("}")
