#include <stdio.h>

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    int arr[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &arr[i]);

    int current = 0, next = 0;
    int cnt = 0;

    // K를 지목하거나 이미 지목한 사람을 지목하면 종료
    while (arr[current] != K && arr[current] != 0)
    {
        next = arr[current];
        arr[current] = 0;
        current = next;
        cnt++;
    }

    if (arr[current] == K)
        printf("%d", cnt + 1);
    else
        printf("-1");

    return 0;
}