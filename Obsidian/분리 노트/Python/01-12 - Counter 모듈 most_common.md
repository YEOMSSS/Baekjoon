# Counter 모듈 most_common

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

dictionary 형태로 작동한다. most_common을 Counter에 사용하면 빈도순으로 출력된다.

    word_counter = Counter(words)
    print(word_counter.most_common(3))

    Counter({'python': 3, 'is': 3, 'amazing': 1, 'and': 1, 'fun.': 1, 'powerful.': 1})
    [('python', 3), ('is', 3), ('amazing', 1)]

## 보충 설명과 예시

빈도 집계는 `Counter`가 가장 짧고 명확하다.
```python
from collections import Counter
counts = Counter('aabca')
print(counts.most_common(1))  # [('a', 3)]
```
