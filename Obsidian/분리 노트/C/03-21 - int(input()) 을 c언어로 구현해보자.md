# int(input()) 을 c언어로 구현해보자

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

    #include <stdio.h>
    #include <stdlib.h>

    int main(void) {
        // 동적 메모리로 입력 버퍼 준비 (파이썬 input()처럼 가변적이라 가정)
        char *arr = malloc(100);  // 최대 99글자 + '\0' 입력 가능

        // 문자열 입력 (개행\0 포함됨)
        fgets(arr, 100, stdin);

        // 문자열 → 정수 변환 (에러 체크 생략)
        int x = atoi(arr);

        printf("%d\n", x);

        free(arr);  // malloc으로 확보했으니 해제
        return 0;
    }

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
int x;
scanf("%d", &x);
```
