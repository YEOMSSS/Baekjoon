
// 뒤에서부터, 큰 수에서부터 정렬하는 선택정렬을 해 보자.
// 이번엔 K번 교환 후 stop한다.

#include <stdio.h>
#include <stdlib.h> // malloc

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void selection_sort(int *arr, const int N, const int K)
{
    int cnt = 0;

    for (int i = N - 1; 0 <= i; i--)
    {
        int max_idx = i;
        // 알고리즘 수업에서는 큰 것부터 끝에 가게 바꾼다.
        for (int j = i - 1; 0 <= j; j--)
        {
            if (arr[j] > arr[max_idx])
                max_idx = j;
        }
        // 겹칠 때는 교환하지 않는다.
        if (i != max_idx)
        {
            swap(&arr[i], &arr[max_idx]);
            cnt++;

            // K번 교환 후 일어날 일
            if (cnt == K)
            {
                // K번 교환이 일어난 직후의 리스트를 출력
                for (int i = 0; i < N; i++)
                    printf("%d ", arr[i]);

                return;
            }
        }
    }
    if (cnt < K)
        printf("-1");
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    int *nums = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &nums[i]);

    selection_sort(nums, N, K);

    free(nums);
    return 0;
}
