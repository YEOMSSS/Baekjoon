# <string.h> strcat(arr, "str");

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

strcat은 문자열을 이어붙이는 역할을 한다. arr의 가장 끝에 str을 붙여준다.  
배열의 크기를 초과하면 오류가 날 수 있다.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
char s[20] = "hi";
strcat(s, "!");
```
