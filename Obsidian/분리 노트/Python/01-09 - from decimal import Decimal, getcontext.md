# from decimal import Decimal, getcontext

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

Decimal = 10진수로 계산하는 숫자 타입. 2진수 연산인 float에서 생기는 오차를 막는다.  
getcontext().prec는 계산 중 유지할 유효숫자 수다.

## 보충 설명과 예시

금액처럼 10진수 오차를 피해야 할 때 `Decimal`을 쓴다.
```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```
