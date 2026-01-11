
#include <stdio.h>
#include <stdlib.h>

// 매 과정마다 배열 전체를 확인하는 것은 어떤 방법을 쓰더라도 통과가 어렵습니다.
// 힌트만 드리자면, 매 과정에서 바뀌는 자리는 두 개뿐인데 매번 전체를 비교할 필요가 있을까요?
// 몇 개의 수가 일치한지만 알고 있다면 그 자리를 바꾼 두 개씩의 수에 대해서만 업데이트를 해주면 되지 않을까요?

// 배열 비교용 함수
int is_equal(int *arr_A, const int *arr_B, int len)
{
    for (int i = 0; i < len; i++)
    {
        if (arr_A[i] != arr_B[i])
            return 0; // 동일하지 않음
    }
    return 1; // 전부 동일함
}

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int *arr_A, const int *arr_B, const int N)
{
    // 맨 앞에서부터 다음거랑 비교해서 판정한다.
    // 큰 반복 한번당 숫자 하나가 뒤에서부터(큰 수부터) 정렬된다.
    for (int i = 0; i < N - 1; i++)
    {
        // 반복은 큰 반복이 있던 횟수만큼 줄어든다. (-i)
        // 마지막 자리가 한칸씩 정렬되어 비교할 필요가 없어지기 때문.
        for (int j = 0; j < N - i - 1; j++)
        {
            if (arr_A[j] > arr_A[j + 1])
            { // 현재 수와 다음 수를 비교해서 현재수가 더 크면 바꾼다.
                swap(&arr_A[j], &arr_A[j + 1]);

                // 더 좋은 방법이 있을 거 같은데? 비교를 언제 어떻게 해야할까?
                if (arr_A[j] == arr_B[j]) // **바뀐 첫 자리가 같아졌을 때만 전체 비교**
                {
                    if (is_equal(arr_A, arr_B, N - i)) // 비교는 N - i칸까지만 하면 되니까.
                    {
                        putchar('1'); // 참일 때 출력
                        return;
                    }
                }
            }
        }
    }

    // 정렬 종료 후 동일 배열이 없을 경우
    putchar('0');
    return;
}

int main()
{
    int N;
    scanf("%d", &N);

    int *nums_A = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &nums_A[i]);

    int *nums_B = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &nums_B[i]);

    // 같은 입력이 들어올 수 있다.
    if (is_equal(nums_A, nums_B, N))
    {
        putchar('1');

        free(nums_A);
        free(nums_B);

        return 0;
    }

    bubble_sort(nums_A, nums_B, N);

    free(nums_A);
    free(nums_B);

    return 0;
}
