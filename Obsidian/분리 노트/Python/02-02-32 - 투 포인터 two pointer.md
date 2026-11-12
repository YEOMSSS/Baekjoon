# 투 포인터 two pointer

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/02-02 - 560. 브루트 포스 - 기타 260226 ~ 260301]]

원문 사본: [[Obsidian/원본 - Python README]]

투포인터 문제는 start를 for문으로 관리하는 편이 좋다.  
아, 슬라이딩 윈도우일 때만 가능한 거긴 함. 한쪽만 미는 경우니까.

그냥 투포인터인 경우는 i가 j보다 커질 수 있다.

## 보충 설명과 예시

정렬된 배열에서 합 조건을 찾을 때 양끝 포인터를 좁혀 간다.
```python
a, target = [1, 2, 4, 7, 11], 9
l, r = 0, len(a) - 1
while l < r:
    if a[l] + a[r] < target: l += 1
    elif a[l] + a[r] > target: r -= 1
    else: print(l, r); break
```
