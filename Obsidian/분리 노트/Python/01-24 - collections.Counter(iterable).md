# collections.Counter(iterable)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

iterable의 개수를 각각 세서 dict의 형태로 반환한다.  
사실 Counter의 형태로 반환하는 거지만, dict와 같은 역할을 수행할 수 있다.

## 보충 설명과 예시

빈도 집계는 `Counter`가 가장 짧고 명확하다.
```python
from collections import Counter
counts = Counter('aabca')
print(counts.most_common(1))  # [('a', 3)]
```
