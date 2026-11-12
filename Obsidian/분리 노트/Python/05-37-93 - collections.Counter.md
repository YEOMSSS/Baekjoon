# collections.Counter

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-37 - 201. 자료구조 1 (연습) 250515 ~ 250517]]

원문 사본: [[Obsidian/원본 - Python README]]

Counter(list) 의 형태로 list 안의 요소가 등장한 횟수를 {요소 : 횟수} 의 형태로 저장한다.  
딕셔너리처럼 작동함.

## 보충 설명과 예시

빈도 집계는 `Counter`가 가장 짧고 명확하다.
```python
from collections import Counter
counts = Counter('aabca')
print(counts.most_common(1))  # [('a', 3)]
```
