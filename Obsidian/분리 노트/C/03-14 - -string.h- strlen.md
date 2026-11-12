# <string.h> strlen

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

문자열의 내용 길이를 반환한다. 배열이 얼마나 차 있는지를 반환한다고 생각하면 됨.  
널문자 \0이 나올 때까지 읽는다.  
`char arr[256] = "Hello";`
`printf("%zu\n", strlen(arr));   // 5  ('H','e','l','l','o');`

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
printf("%zu\n", strlen("abc"));
```
