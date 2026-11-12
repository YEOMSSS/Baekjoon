# stdin이 뭐냐고?

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

stdin : Standard Input (표준 입력, 보통 키보드)  
stdout : Standard Output (표준 출력, 보통 화면)  
stderr : Standard Error (에러 메시지 출력, 보통 화면)

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
char line[100];
fgets(line, sizeof line, stdin);
```
