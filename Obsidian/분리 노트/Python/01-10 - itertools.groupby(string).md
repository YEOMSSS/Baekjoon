# itertools.groupby(string)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

groupby는 연속으로 같은 값들을 묶어주는 함수다.

    for ch, group in groupby(string):
    print(ch, list(group))

## 보충 설명과 예시

`groupby`는 정렬된(또는 이미 연속한) 같은 값의 묶음을 만든다.
```python
from itertools import groupby
print([(k, len(list(g))) for k, g in groupby('aaabbc')])
```
