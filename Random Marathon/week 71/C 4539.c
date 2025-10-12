/*
1의자리부터 확인하는거다.
10으로 나눠서 나머지가 10/2보다 작으면 버리고, 크거나 같으면 올린다.
그리고 10에 10을 곱해주고 100으로 반복한다.
그 다음엔 1000으로 반복하게 된다.
숫자보다 작을 때까지만 반복한다.
*/

#include <stdio.h>

long long func(long long n)
{
    int locate = 10;
    while (n >= locate)
    {
        long long half = locate / 2;
        long long remain = n % locate;

        if (remain >= half)
            n += (locate - remain);
        else
            n -= remain;

        locate *= 10;
    }
    return n;
}

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        long long x;
        scanf("%lld", &x);

        printf("%lld\n", func(x));
    }
    return 0;
}