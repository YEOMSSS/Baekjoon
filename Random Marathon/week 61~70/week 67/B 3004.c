#include <stdio.h>

int func(const int N)
{
    int half = N / 2;

    if (N % 2 == 0)
        return (half + 1) * (half + 1);
    else
        return (half + 1) * (half + 2);
}

int main(void)
{
    int N;
    scanf("%d", &N);

    printf("%d\n", func(N));

    return 0;
}