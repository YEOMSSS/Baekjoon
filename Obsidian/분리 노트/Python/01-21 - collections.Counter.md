# collections.Counter

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

iterable을 넣으면 딕셔너리 형태로 개수를 세 준다.

## 보충 설명과 예시

빈도 집계는 `Counter`가 가장 짧고 명확하다.
```python
from collections import Counter
counts = Counter('aabca')
print(counts.most_common(1))  # [('a', 3)]
```
