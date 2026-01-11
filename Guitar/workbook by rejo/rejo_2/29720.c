#include <stdio.h>

int main(void)
{
    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);

    int min, max;
    min = N - M * K;
    max = min + M - 1;

    if (min < 0)
    {
        min = 0;
    }
    if (max < 0)
    {
        max = 0;
    }

    printf("%d %d", min, max);

    return 0;
}
