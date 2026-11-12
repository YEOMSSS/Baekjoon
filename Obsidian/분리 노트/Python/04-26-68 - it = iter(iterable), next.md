# it = iter(iterable), next

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-26 - 530. 브루트 포스 - 재귀 250616 ~ 250620]]

원문 사본: [[Obsidian/원본 - Python README]]

189_1248 문제 참고

## 보충 설명과 예시

iterator는 `next`로 하나씩 꺼내고, 남은 값은 그대로 순회할 수 있다.
```python
it = iter([3, 5, 7])
first = next(it)
print(first, list(it))
```
