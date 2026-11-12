# Merge Sort

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/03-10 - 801. 분할 정복 (연습) 260115 ~ 260117]]

원문 사본: [[Obsidian/원본 - Python README]]

머지소트형으로 반갈내는 분할정복은 재귀깊이제한을 풀어줄 필요가 딱히 없다.  
깊이는 백만이 들어와도 20번이 안되걸랑. N logN의 힘

## 보충 설명과 예시

머지 소트는 두 정렬 구간을 병합하며 `O(N log N)`에 정렬한다.
```python
def merge(a, b):
    out = []
    while a and b:
        out.append((a if a[0] < b[0] else b).pop(0))
    return out + a + b
```
