#include <stdio.h>
#include <stdlib.h> // malloc, free

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    // malloc으로 동적 메모리에 길이가 N, M인 int배열 만들기
    int *arr_A = malloc(sizeof(int) * N);
    int *arr_B = malloc(sizeof(int) * M);

    // arr A 입력받기
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr_A[i]);
    }
    // arr B 입력받기
    for (int j = 0; j < M; j++)
    {
        scanf("%d", &arr_B[j]);
    }

    // 투 포인터 두 개 준비
    int pointer_A = 0, pointer_B = 0;

    // 끝까지 가는 애가 생기기 전까지 반복
    while (pointer_A < N && pointer_B < M)
    {
        // a랑 b가 가리키는 것 중 작은 걸 먼저 출력한 후, 포인터를 한칸 앞으로.
        if (arr_A[pointer_A] <= arr_B[pointer_B])
        {
            printf("%d ", arr_A[pointer_A]);
            pointer_A++;
        }
        else
        {
            printf("%d ", arr_B[pointer_B]);
            pointer_B++;
        }
    }

    // 끝까지 도달한 애가 뭔지 확인 후, 남은 애를 전부 출력
    while (pointer_A < N)
    {
        printf("%d ", arr_A[pointer_A]);
        pointer_A++;
    }
    while (pointer_B < M)
    {
        printf("%d ", arr_B[pointer_B]);
        pointer_B++;
    }

    free(arr_A);
    free(arr_B);

    return 0;
}

// qsort를 이용해서 python3처럼 풀어낸 경우

/*
#include <stdio.h>
#include <stdlib.h>

// qsort 비교 함수
int compare(const void *a, const void *b) {
    int num1 = *(int*)a;
    int num2 = *(int*)b;
    if (num1 < num2) return -1; // a가 b보다 작다(앞이다)
    else if (num1 > num2) return 1; // a가 b보다 크다(뒤다)
    else return 0; // 같으면 변동이 필요 없다
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int size = N + M;
    int *arr = malloc(size * sizeof(int));

    // 배열 A 입력
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    // 배열 B 입력
    for (int i = 0; i < M; i++) {
        scanf("%d", &arr[N + i]);
    }

    // qsort로 정렬
    qsort(arr, size, sizeof(int), compare);

    // 출력
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
*/