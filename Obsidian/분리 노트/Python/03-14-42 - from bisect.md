# from bisect

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/03-14 - 710. 그리디 알고리즘 250901 ~ 260106]]

원문 사본: [[Obsidian/원본 - Python README]]

bisect는 이진탐색으로 들어갈 위치를 찾아주는 모듈이다.  
bisect_right(a, x), bisect_left(a, x). 각각 정렬된 a에서 x가 들어갈 수 있는 위치를 찾는다.  
right는 들어갈 수 있는 가장 오른쪽 인덱스를, left는 들어갈 수 있는 가장 왼쪽 인덱스를 반환한다.

left는 x가 존재할 경우 그 값의 인덱스 자체를 반환하는 느낌이고,  
right는 x보다 큰 값이 나타나기 시작하는 인덱스가 어딘지 찾는 느낌이라고 보면 된다.

    a = [1, 3, 3, 5]
    bisect.bisect_left(a, 3) # 1, [1, |3, 3, 5]
    bisect.bisect_right(a, 3) # 3, [1, 3, 3, |5]

insort_left(a, x), insort_right(a, x)는 a에서 x로 각각 left, right한 위치에 x를 삽입까지 해준다.

## 보충 설명과 예시

정렬된 리스트에서 삽입 위치를 이분 탐색으로 찾는다.
```python
from bisect import bisect_left
a = [1, 3, 3, 5]
print(bisect_left(a, 3))  # 1
```
