# bit_count(), bit_length()

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

2진수로 바꿨을 때 1의 개수를 세주는 n.bit_count()  
2진수로 바꿀 때 필요한 비트의 개수를 알려주는 n.bit_length()

## 보충 설명과 예시

비트마스크에서 켜진 비트 수와 필요한 비트 수를 바로 구할 수 있다.
```python
n = 0b10110
print(n.bit_count(), n.bit_length())  # 3 5
```
