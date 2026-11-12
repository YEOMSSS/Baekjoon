# import heapq

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/03-14 - 710. 그리디 알고리즘 250901 ~ 260106]]

원문 사본: [[Obsidian/원본 - Python README]]

파이썬에서 최소 힙과 최대 힙을 사용할 수 있게 하는 모듈이다.  
힙 전용 자료구조가 있는 것이 아니므로 `max_heap = []` 로 둔 리스트를 힙 규칙으로 관리한다.  
파이썬의 heapq는 최소 힙만 다루므로 최대 힙을 사용하고 싶다면 -를 붙여 쓰면 된다.

    최대 힙을 사용하는 경우
    max_heap = []
    heapq.heappush(max_heap, -value) # 힙에 value를 push한다.
    print(-heapq.heappop(max_heap)) # 힙의 최댓값을 pop한다.

## 보충 설명과 예시

`heapq`는 최소 힙이므로 최대 힙은 부호를 반전해 표현한다.
```python
import heapq
h = []
heapq.heappush(h, -7)
print(-heapq.heappop(h))  # 7
```
