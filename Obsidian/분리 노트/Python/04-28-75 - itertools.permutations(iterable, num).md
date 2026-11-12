# itertools.permutations(iterable, num)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-28 - 510. 브루트 포스 (N과 M) 250611 ~ 250614]]

원문 사본: [[Obsidian/원본 - Python README]]

iterable에서 서로 다른 요소 중 num개를 선택하는 **순열**을 중복 없이 **튜플** 형태로 생성한다.

## 보충 설명과 예시

순서가 중요하면 순열을 사용한다.
```python
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))
```
