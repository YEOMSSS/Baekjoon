#include <stdio.h>

int func(int n)
{
    int a = n % 10;
    n /= 10;

    int prev = a - (n % 10);

    while (n)
    {
        int diff = a - (n % 10);
        a = n % 10;
        n /= 10;

        if (prev != diff)
            return 0;
    }

    return 1;
}

int main(void)
{
    int N;
    scanf("%d", &N);

    int result = 0;

    for (int i = 1; i <= N; i++)
    {
        if (func(i))
            result++;
    }
    printf("%d", result);
    return 0;
}

// 오늘 날이구나~~~