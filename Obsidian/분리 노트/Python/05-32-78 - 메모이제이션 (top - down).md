# 메모이제이션 (top - down)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-32 - 400. 다이나믹 프로그래밍 1 250524 ~ 250601]]

원문 사본: [[Obsidian/원본 - Python README]]

재귀하며 중복계산은 딕셔너리에 저장하고, 한번 한 계산은 재사용한다.

    import sys
    sys.setrecursionlimit(10**6)
    재귀 깊이를 늘리는 코드. 파이썬은 1000번이 제한이기 때문에 반필수다.
    다만 이걸 사용하면 보통 메모리가 초과된다.

## 보충 설명과 예시

재귀 상태의 답을 저장하면 같은 부분문제를 반복하지 않는다.
```python
memo = {}
def solve(x):
    if x not in memo: memo[x] = x * x
    return memo[x]
```
