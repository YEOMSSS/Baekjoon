# nonlocal variable

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-26 - 530. 브루트 포스 - 재귀 250616 ~ 250620]]

원문 사본: [[Obsidian/원본 - Python README]]

밖 함수에서 선언된 variable의 값을 함수 내에서 변경하고 싶다면 함수가 시작할 때 global variable을 한번 써주면 된다.

## 보충 설명과 예시

중첩 함수에서 바깥 함수의 변수를 수정할 때 `nonlocal`을 선언한다.
```python
def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
```
