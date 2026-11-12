# string.replace('a', 'b')

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

string에서 a를 b로 바꿔주는 문자열 method.  
.replace는 무한이 뒤에 이어붙여 순차적으로 적용할 수 있다.

## 보충 설명과 예시

문자열은 불변이라 `replace`의 반환값을 받아야 한다.
```python
s = 'a-b-c'
print(s.replace('-', '/'))  # a/b/c
```
