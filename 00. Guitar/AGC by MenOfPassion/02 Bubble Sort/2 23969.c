
#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int *arr, const int N, const int K)
{
    int cnt = 0;
    // 맨 앞에서부터 다음거랑 비교해서 판정한다.
    // 큰 반복 한번당 숫자 하나가 뒤에서부터(큰 수부터) 정렬된다.
    for (int i = 0; i < N - 1; i++)
    {
        // 반복은 큰 반복이 있던 횟수만큼 줄어든다. (-i)
        // 마지막 자리가 한칸씩 정렬되어 비교할 필요가 없어지기 때문.
        int swapped = 0;
        for (int j = 0; j < N - i - 1; j++)
        {
            // 만약 정렬된 상태라면 이번 반복에 스왑이 없을 것. 체크용.

            if (arr[j] > arr[j + 1])
            { // 현재 수와 다음 수를 비교해서 현재수가 더 크면 바꾼다.
                swap(&arr[j], &arr[j + 1]);
                cnt++;
                swapped = 1;

                // K회 바뀌면 종료하고 바뀐 값들 출력
                // 방금 비교해서 바꿨기 때문에 j, j+1 순서가 이미 오름차순이다.
                // cnt가 바뀔 때만 K에 도달했는지 확인하면 됨.
                if (cnt == K)
                { // K번 반복 종료 직후의 배열상태 출력
                    for (int i = 0; i < N; i++)
                    {
                        if (i != 0)
                            putchar(' ');
                        printf("%d", arr[i]);
                    }
                    putchar('\n');
                    return;
                }
            }
        }
        // 스왑이 없으면 정렬되었으므로 break
        if (!swapped)
            break;
    }

    // cnt가 K에 닿기 전에 이미 정렬되면 -1 출력
    printf("-1\n");
}

int main()
{
    int N, K;
    scanf("%d %d", &N, &K);

    int *nums = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &nums[i]);

    bubble_sort(nums, N, K);

    free(nums);

    return 0;
}
