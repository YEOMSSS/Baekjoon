#include <stdio.h>

int main(void)
{
    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);

    int min = N + M, result = 0;
    for (int i = 0; i < K; i++)
    {
        int f, d;
        scanf("%d %d", &f, &d);

        int temp = f + M - d;
        if (temp < min)
        {
            min = temp;
            result = i;
        }
    }
    printf("%d", result + 1);

    return 0;
}