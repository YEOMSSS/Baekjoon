# map과 lambda

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/02-04 - 551. 브루트 포스 - 문제 (연습) 260205 ~ 260216]]

원문 사본: [[Obsidian/원본 - Python README]]

result = list(map(lambda x, y: abs(x - y), [2, 9, 4], [4, 8, 2]))  
결과는 [abs(2-4), abs(9-8), abs(4-2)] -> [2, 1, 2]  
map의 함수에 2개 이상 넣으면 각 리스트에서 같은 인덱스의 요소를 하나씩 꺼내와서 인수로 전달한다.

## 보충 설명과 예시

`map`은 각 원소에 같은 변환을 적용할 때 간결하다.
```python
print(list(map(lambda x: x * x, [1, 2, 3])))
```
