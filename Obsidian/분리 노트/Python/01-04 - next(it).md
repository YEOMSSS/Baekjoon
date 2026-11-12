# next(it)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

```python
it = map(int, input().split())

# next로 iterator의 0번value 꺼내기
prev = next(it)
count = 1

# 남은 iterator로 for문 돌리기
for h in it:
    if prev <= h:
        count += 1
    prev = h
```
