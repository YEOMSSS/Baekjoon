# <stdlib.h> malloc

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

`char *s = malloc(n + 1);` // 문자 n개 + '\0'
`s[n] = '\0'; ` // 직접 문자열의 끝을 표시해줘야 한다.

`int *arr = malloc(n * sizeof(int));` // n칸짜리 int 배열 만들기

`free(arr)` // 사용한 메모리를 꼭 반납해야 한다.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
int *a = malloc(n * sizeof *a);
if (a == NULL) return 1;
free(a);
```
