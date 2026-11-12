# 포인터와 const

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

일단 const가 앞에 붙으면, 기본적으로 그 데이터가 수정 불가능하다는 의미이다.  
주소가 바뀌지 않아서가 아니라, 데이터를 건드리지 않기 때문에 `const char *`를 쓰는 것.

const char *p; // (1) "데이터"가 const: *p 수정 불가, p는 다른 곳을 가리키게 변경 가능  
char * const p; // (2) "포인터"가 const: p 재지정 불가, *p 수정 가능  
const char * const p; // (3) 둘 다 const: p 재지정 불가, *p 수정 불가

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
void print_name(const char *name) {
    printf("%s\n", name);
}
```
