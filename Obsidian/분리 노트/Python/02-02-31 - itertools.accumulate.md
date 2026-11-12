# itertools.accumulate

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/02-02 - 560. 브루트 포스 - 기타 260226 ~ 260301]]

원문 사본: [[Obsidian/원본 - Python README]]

누적합을 자동으로 구해준다. C기반이라 루프도는것보다 빠름.

```python
# initial=0을 주면 자동으로 맨 앞에 0이 붙는다.
A = list(accumulate(map(int, input().split()), initial=0))
```
