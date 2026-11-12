# collections.Counter()

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/02-02 - 560. 브루트 포스 - 기타 260226 ~ 260301]]

원문 사본: [[Obsidian/원본 - Python README]]

이 친구가 아주 대단한 놈이었다. 딕셔너리를 상속받았구나...  
dict와 달리 존재하지 않는 key를 입력해도 에러가 안 난다. 그냥 0을 반환함.

```python
counts = Counter()
for val in some_data:
    counts[val] += 1
```

이런 짓거리가 가능하다는거다.  
심지어 hashMap이라 in연산도 O(1)이다... 미친거임?
