# @lru_cache(maxsize=None)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/03-17 - 533. 브루트 포스 - 재귀 (참고) 250716 ~ 250716]]

원문 사본: [[Obsidian/원본 - Python README]]

재귀함수 def 바로 위에 이 한줄을 써주면 중복연산을 없애준다.  
한번 했던 계산을 캐시로 저장해 다시 안하고 불러오는 소중한 한 줄이다.  
@lru_cache는 "DP 테이블 없이 DP를 구현할 수 있는 방법"이다.  
Top-down 방식으로 상태만 정의하면 끝. 없이도 코드를 완성할 수 있어야 한다.

## 보충 설명과 예시

같은 상태를 다시 계산하는 재귀에는 메모이제이션을 붙인다.
```python
from functools import lru_cache
@lru_cache(None)
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
```
