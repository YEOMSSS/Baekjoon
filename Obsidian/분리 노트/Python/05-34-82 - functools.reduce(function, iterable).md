# functools.reduce(function, iterable)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-34 - 301. 수학 1 (연습) 250522 ~ 250524]]

원문 사본: [[Obsidian/원본 - Python README]]

iterable의 처음 두 요소부터 시작해서 하나씩 function을 누적해 적용한다.  
만약 iterable의 길이가 1이라면 함수를 호출하지 않고 하나뿐인 요소를 그대로 반환한다.

## 보충 설명과 예시

`reduce`는 누적 연산을 함수로 표현할 때 쓴다.
```python
from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3]))
```
