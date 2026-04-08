
// 뒤에서부터 정렬하는 선택정렬
// 입력된 배열이 선택정렬 교환 단계에 있는지 판단한다.

#include <stdio.h>
#include <stdlib.h>

// 배열 비교용 함수
int is_equal(int *arr_A, int *arr_B, int len)
{
    for (int i = 0; i < len; i++)
    {
        if (arr_A[i] != arr_B[i])
            return 0; // 동일하지 않음
    }
    return 1; // 전부 동일함
}

// 바꾸기용 함수
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

// A배열이 선택정렬되는 과정에서 B배열의 형태가 되는지 확인하기.
void selection_sort(int *arr_A, int *arr_B, const int N)
{
    for (int i = N - 1; i >= 0; i--)
    { // 가장 큰 원소의 인덱스를 갱신하는 변수
        int max_idx = i;
        for (int j = i - 1; j >= 0; j--)
        {
            if (arr_A[j] > arr_A[max_idx])
                max_idx = j;
        }

        if (i != max_idx)
        {
            swap(&arr_A[i], &arr_A[max_idx]);

            // c언어에서는 0이면 거짓, 0이 아니면 참
            if (is_equal(arr_A, arr_B, N))
            {
                putchar('1'); // 참일 때 출력
                return;
            }
        }
    }

    // 정렬 종료 후 동일 배열이 없을 경우
    putchar('0');
    return;
}

int main(void)
{ // N, arrA, arrB 받기
    int N;
    scanf("%d", &N);

    int *arr_A = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &arr_A[i]);

    int *arr_B = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &arr_B[i]);

    // 같은 입력이 들어올 수 있다.
    if (is_equal(arr_A, arr_B, N))
    {
        putchar('1');

        free(arr_A);
        free(arr_B);

        return 0;
    }

    selection_sort(arr_A, arr_B, N);

    // malloc 풀어주기
    free(arr_A);
    free(arr_B);

    return 0;
}
