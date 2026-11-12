# unpacking 문법 요약

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-27 - 520. 브루트 포스 - 순열 250614 ~ 250615]]

원문 사본: [[Obsidian/원본 - Python README]]

`k, *arr = map(int, input().split())`  
\*arr은 "나머지 값을 unpack해서 리스트로 만들어줘" 라는 뜻  
3 1 2 3을 입력받아서 3, [1, 2, 3]으로 반환한다.

`a, b = [1, 2]` 일반적인 unpacking a = 1, b = 2  
`a, *b = [1, 2, 3, 4]` 나머지 전부 리스트로 a = 1, b = [2, 3, 4]  
`*a, b = [1, 2, 3]` 앞쪽 전부 리스트로 a = [1, 2], b = 3  
`a, *b, c = [1, 2, 3, 4, 5]` 양쪽 값을 분리 a = 1, b = [2, 3, 4], c = 5

## 보충 설명과 예시

별표 언패킹은 앞·뒤 일부를 분리할 때 유용하다.
```python
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)
```
