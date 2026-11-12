# static

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

static (함수 앞) → 이 파일 안에서만 쓸 수 있는 함수.  
여러 .c 파일을 묶어서 컴파일할 때, 함수 이름 충돌을 막아준다.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
static int count = 0;
count++;
```
