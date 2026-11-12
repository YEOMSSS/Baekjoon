# itertools.combinations(iterable, num)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-28 - 510. 브루트 포스 (N과 M) 250611 ~ 250614]]

원문 사본: [[Obsidian/원본 - Python README]]

list에서 서로 다른 요소 중 num개를 선택하는 **조합**을 중복 없이 **튜플** 형태로 생성한다.  
`pairs = list(combinations(arr, 2))` 형태로 사용한다.  
`pairs = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i + 1, len(arr))]` 은  
`pairs = [(i, j) for i, j in combinations(arr, 2)]` 로 나타낼 수 있다.

## 보충 설명과 예시

순서가 중요하지 않은 선택에는 조합을 사용한다.
```python
from itertools import combinations
print(list(combinations([1, 2, 3], 2)))
```
