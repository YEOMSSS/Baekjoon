# reversed(list)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

슬라이싱을 더 이상 남용해선 안 된다.  
읽기만 해도 되며, list를 만들 필요가 없다면 [::-1]로 복사할 필요가 없다.  
그냥 reversed로 iterator반환하는 것이 가장 효율적이다.

## 보충 설명과 예시

`reversed`는 새 리스트를 만들지 않고 역순 iterator를 돌려준다.
```python
for value in reversed([1, 2, 3]):
    print(value)
```
