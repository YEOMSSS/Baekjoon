
#include <stdio.h>
#include <stdlib.h> // malloc, qsort, bsearch

// 배열 비교용 함수
int is_equal(int *arr1, int *arr2, int N)
{
    for (int i = 0; i < N; i++)
    {
        if (arr1[i] != arr2[i])
            return 0;
    }
    return 1;
}

// qsort compare
int compare(const void *a, const void *b)
{
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y); // 오름차순 정렬
}

int main(void)
{
    int N;
    scanf("%d", &N);

    int *arrA = malloc(N * sizeof(int));
    int *arr_sorted = malloc(N * sizeof(int)); // 정렬용 리스트
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arrA[i]);
        arr_sorted[i] = arrA[i];
    }

    int *arrB = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &arrB[i]);

    // 입력값이 동일할 경우
    if (is_equal(arrA, arrB, N))
    {
        putchar('1');

        free(arrA);
        free(arrB);
        free(arr_sorted);

        return 0;
    }

    // 정렬용 배열 오름차순 정렬
    qsort(arr_sorted, N, sizeof(int), compare);

    // positions[rank] = i는 A[i]값에 있는 값이 rank로 가야한다는 뜻.
    int *positions = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
    {
        int *p = bsearch(&arrA[i], arr_sorted, N, sizeof(int), compare);
        int rank = (int)(p - arr_sorted);
        positions[rank] = i;
    }

    // rank는 정렬된 배열에서의 인덱스이다.
    for (int i = N - 1; i >= 0; i--)
    {
        // positions[rank]는 rank번째로 큰 값이 지금 A배열 어디있는지를 알려준다.
        int target = arr_sorted[i];
        int target_index = positions[i];

        if (target_index != i)
        {
            int current = arrA[i];
            int *p_current = bsearch(&current, arr_sorted, N, sizeof(int), compare);
            int current_rank = (int)(p_current - arr_sorted);

            arrA[target_index] = current;
            arrA[i] = target;

            positions[i] = i;
            // 현재 값이 target이 있던 인덱스로 옮겨진다.
            positions[current_rank] = target_index;

            if (is_equal(arrA, arrB, N))
            {
                putchar('1');

                free(arrA);
                free(arrB);
                free(arr_sorted);

                return 0;
            }
        }
    }

    putchar('0');

    free(arrA);
    free(arrB);
    free(arr_sorted);

    return 0;
}

// 그래도 조금 더 이해한 듯??? 아님말고.
// 아 씨발, 똑같은 실수했네. 입력값이 같을수있지.