# switch-case문

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

파이썬에 매치케이스가 있다면 c언어에는 스위치케이스가 있다.  
다만 정수형에 대해서만 가능. char는 정수형이므로 쌉가능.  

    switch(x)
    {
    case 'a':
        break;
    default:
        break;
    }
이런 느낌.

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
switch (op) {
case '+': puts("add"); break;
default: puts("other");
}
```
