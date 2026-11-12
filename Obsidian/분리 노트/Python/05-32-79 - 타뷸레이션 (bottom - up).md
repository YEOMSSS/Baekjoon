# 타뷸레이션 (bottom - up)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-32 - 400. 다이나믹 프로그래밍 1 250524 ~ 250601]]

원문 사본: [[Obsidian/원본 - Python README]]

작은 문제부터 dp배열에 차곡차곡 계산해 넣는다.

## 보충 설명과 예시

작은 상태부터 배열에 채우는 bottom-up 방식이다.
```python
dp = [0, 1]
for i in range(2, 6):
    dp.append(dp[-1] + dp[-2])
```
