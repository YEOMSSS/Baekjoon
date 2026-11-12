# enumerate(iterable)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/05-33 - 303. 수학 1 (참고) 250524 ~ 250524]]

원문 사본: [[Obsidian/원본 - Python README]]

`for index, value in enumerate(iterable)` index와 value에 iterable의 인덱스와 값이 들어간다.

## 보충 설명과 예시

인덱스와 값을 함께 순회할 때 쓴다.
```python
for i, value in enumerate(['a', 'b']):
    print(i, value)
```
