# extend([a, b])

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-34 - 301. 수학 1 (연습) 250522 ~ 250524]]

원문 사본: [[Obsidian/원본 - Python README]]

리스트를 풀어서 요소별로 추가 (평탄화)  
append(a); append(b) 와 동일한 효과지만 한 번에 처리할 수 있다.

## 보충 설명과 예시

`extend`는 두 원소를 따로 append하는 효과를 낸다.
```python
a = [1]
a.extend([2, 3])
```
