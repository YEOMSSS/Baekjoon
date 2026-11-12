# range(start, end)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-28 - 510. 브루트 포스 (N과 M) 250611 ~ 250614]]

원문 사본: [[Obsidian/원본 - Python README]]

start부터 end-1까지의 수를 반환하는 iterable이다. 리스트가 아니다.  
range 타입으로, 숫자들을 미리 저장하는 것이 아니라 필요할 때 값을 생성하는 방식으로 동작한다.

## 보충 설명과 예시

`range`의 끝값은 포함하지 않는다.
```python
print(list(range(2, 5)))  # [2, 3, 4]
```
