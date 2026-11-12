# <stdio.h> sizeof

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

문자열 길이와 상관 없이 배열의 메모리 크기를 반환한다.  
`char arr[256];`
`printf("%zu\n", sizeof(arr));   // 256  (배열 전체 크기)`

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
int a[10];
int n = sizeof a / sizeof a[0];
```
