# if x is None

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

None을 검사할 때는 == None보다 is None을 더 많이 사용한다.

## 보충 설명과 예시

`None`은 싱글턴이므로 값 비교에는 `==`보다 `is`가 자연스럽다.
```python
answer = None
if answer is None:
    answer = 0
```
