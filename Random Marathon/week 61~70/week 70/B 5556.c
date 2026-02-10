
/*
대각선으로 선 두개 그어보면
그 사이 행은 색이 다 똑같다.
*/

/*
#include <stdio.h>

int color(int x)
{
    x %= 3;

    if (!x)
        return 3;
    else
        return x;
}

int fold(int x, int N)
{
    return (x <= N - x + 1) ? x : N - x + 1;
}

int func(int N, int a, int b)
{
    a = fold(a, N);
    b = fold(b, N);

    if (a <= b)
        return color(a);
    else
        return color(b);
}

int main(void)
{
    int N;
    scanf("%d", &N);
    int K;
    scanf("%d", &K);

    for (int i = 0; i < K; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);

        printf("%d\n", func(N, a, b));
    }
    return 0;
    }
    */

#include <stdio.h>
int main(void)
{
    int N, K;
    scanf("%d", &N);
    scanf("%d", &K);

    for (int i = 0; i < K; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);

        if (N - a + 1 < a)
            a = N - a + 1;
        if (N - b + 1 < b)
            b = N - b + 1;

        int result;
        if (a < b)
            result = a % 3;
        else
            result = b % 3;

        printf("%d\n", (!result) ? 3 : result);
    }
    return 0;
}

// 씨발 최단거리 문제였잖아?