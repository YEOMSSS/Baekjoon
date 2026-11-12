# <stdio.h> fgets

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

`char arr[256];`  
`fgets(arr, sizeof(arr), stdin);`  
말 그대로 input()의 느낌이다. 문자열+개행까지 입력받는다.  
최대 size-1 글자만 읽고 마지막에 \0 자동 추가.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
char line[100];
fgets(line, sizeof line, stdin);
```
