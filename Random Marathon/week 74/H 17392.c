// 각 약속에 1씩 더해서 총 일수에서 빼주면 비는 날이 나온다.
// 비는 날을 약속의 수 + 1로 잘 나눠보자.

#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int sum = N;
    for (int i = 0; i < N; i++)
    {
        int H;
        scanf("%d", &H);
        sum += H;
    }

    // 기분이 음수인 날의 수
    int sad_days = M - sum;
    if (sad_days < 0)
        sad_days = 0;

    if (sad_days > N + 1)
    {
        long long sadness = 0;
        int temp1 = sad_days / (N + 1);

        for (int i = 1; i <= temp1; i++)
            sadness += i * i;

        sadness *= N + 1;

        temp1++;

        // 나누고 남는 날 더해주기
        int temp2 = sad_days % (N + 1);
        sadness += temp1 * temp1 * temp2;

        printf("%lld", sadness);
    }

    else
        printf("%d", sad_days);

    return 0;
}