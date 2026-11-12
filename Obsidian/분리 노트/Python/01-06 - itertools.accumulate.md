# itertools.accumulate

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

```python
from itertools import accumulate

durations = [5, 2, 10]
acc_d = list(accumulate(durations))
# 결과: [5, 7, 17] (차례대로 5, 5+2, 5+2+10)
```
