# global variable

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-27 - 520. 브루트 포스 - 순열 250614 ~ 250615]]

원문 사본: [[Obsidian/원본 - Python README]]

밖에서 선언된 variable의 값을 함수 내에서 변경하고 싶다면 함수가 시작할 때 global variable을 한번 써주면 된다.

## 보충 설명과 예시

전역 변수를 수정할 때만 `global`이 필요하며, 매개변수 전달이 더 안전한 경우가 많다.
```python
count = 0
def inc():
    global count
    count += 1
```
