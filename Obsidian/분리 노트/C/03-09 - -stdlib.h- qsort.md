# <stdlib.h> qsort

---
tags: [baekjoon, c, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/C/03 - 00. 기타]]

원문 사본: [[Obsidian/원본 - C README]]

qsort는 배열을 정렬하는 c언어의 소중한 내장함수.  
`qsort(arr, size, sizeof(int), compare);`  
여기서 compare는 직접 짜줘야한다.

    void qsort(
        void *base,            // 정렬할 '배열의 시작 주소'
        size_t nmemb,          // 원소(칸) 개수
        size_t size,           // 원소 하나의 바이트 크기(예: int면 sizeof(int))
        int (*compar)(const void*, const void*) // '두 원소를 비교'하는 함수
    );

compare는 배열에서 임의로 2개의 원소를 집어 비교한다.  
qsort는 어떤 타입의 배열이든 정렬할 수 있어야 합니다.  
그래서 원소 타입을 모르니까 → 매개변수 타입을 (const void*)로 통일해둡니다.  
비교 함수 안에서 다시 (int*)로 바꿔야 정수 값을 꺼낼 수 있습니다.  
(int*)a는 주소를 가리키고 있으니, *를 붙여 값으로 꺼낸다.  
(int\*)는 그냥 이 포인터가 int형이라는 것일 뿐이지롱.

    int compare(const void *a, const void *b) {
        int num1 = *(int*)a; // (1) a를 int*로 캐스팅 → 역참조(*)로 값 획득
        int num2 = *(int*)b; // (2) b도 동일
        if (num1 < num2) return -1; // (3) num1이 더 작으면 '앞으로'(-1)
        else if (num1 > num2) return 1; // (4) num1이 더 크면 '뒤로'(+1)
        else return 0; // (5) 같으면 0
    }

return (x > y) - (x < y); 이거로 (3, 4, 5)단계 날먹도 가능하다. (오름차순)

## 보충 설명과 예시

핵심 동작만 확인하는 짧은 예시입니다.
```c
int cmp(const void *a, const void *b) {
    return (*(const int *)a > *(const int *)b) - (*(const int *)a < *(const int *)b);
}
qsort(a, n, sizeof a[0], cmp);
```
