# f-string

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

`binum = f"{a[-4:]:0>4}{b[-4:]:0>4}{c[-4:]:0>4}"`
0은 채울 문자, >는 우측 정렬, 4는 전체 길이(width)  
int형은 우측정렬이 기본이고, str형은 좌측정렬이 기본이다.

## 보충 설명과 예시

값의 자릿수·정렬을 문자열 안에서 바로 지정할 수 있다.
```python
score = 7
print(f"{score:03d}")  # 007
```
