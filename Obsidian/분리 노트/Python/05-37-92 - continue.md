# continue

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-37 - 201. 자료구조 1 (연습) 250515 ~ 250517]]

원문 사본: [[Obsidian/원본 - Python README]]

그 자리에서 현재 반복을 멈추고, 다음 반복을 진행한다.

## 보충 설명과 예시

`continue`는 현재 반복의 나머지를 건너뛴다.
```python
for x in range(5):
    if x % 2 == 0: continue
    print(x)
```
