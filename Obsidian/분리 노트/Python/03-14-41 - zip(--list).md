# zip(\*list)

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/03-14 - 710. 그리디 알고리즘 250901 ~ 260106]]

원문 사본: [[Obsidian/원본 - Python README]]

list의 원소들이 열 기준으로 묶인다.

## 보충 설명과 예시

여러 iterable을 같은 인덱스끼리 묶는다.
```python
for name, score in zip(['A', 'B'], [90, 80]):
    print(name, score)
```
