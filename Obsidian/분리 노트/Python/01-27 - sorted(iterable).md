# sorted(iterable)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

sorted는 iterable을 받아서 list형으로 반환한다.  
sorted()는 list.sort()와 동일한 사용방식을 가지나, iterable에 사용할 수 있다.  
원본을 정렬하는 sort()와 달리 값을 반환한다. 값은 list형태로 반환된다.

    words = ["apple", "fig", "pear", "banana", "kiwi"]
    sorted_words = sorted(words, key=lambda x: (len(x), x))
    print(sorted_words)
    # 출력: ['fig', 'kiwi', 'pear', 'apple', 'banana']

## 보충 설명과 예시

`sorted()`는 원본을 건드리지 않고 새 리스트를 준다.
```python
a = [3, 1, 2]
print(sorted(a), a)
```
