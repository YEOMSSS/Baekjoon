# <string.h> strcspn

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

`string[strcspn(string, "\n")] = '\0';`
strcspn(string, "\n") → string에서 처음 \n이 나오는 위치의 인덱스를 반환.  
그 자리를 '\0'로 바꿔버림. 결과적으로 문자열에서 개행 문자가 잘려나감.

strcspn은 왼쪽부터 확인하는 놈이다.  
어차피 한줄을 읽을 때 \n은 마지막에 한번만 들어오니 rstrip처럼 쓸 수 있다.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
str[strcspn(str, "\n")] = '\0';
```
