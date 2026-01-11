
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
// 여기에서 K번째에 바뀐 두 수를 return해야하지 않을까?
// cnt로 세면서, 만약에 최종 cnt가 K보다 작으면 -1반환해주고. 그런거
// 그냥 출력해 버리죠? 구조체를 사용하면 두개이상을 return할 수 있긴 함.
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

            if (cnt == K)
            {
                int a = arr[i];
                int b = arr[max_idx];

                if (a < b)
                    printf("%d %d", a, b);
                else
                    printf("%d %d", b, a);

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
