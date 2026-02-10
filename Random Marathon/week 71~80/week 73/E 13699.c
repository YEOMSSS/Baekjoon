
#include <stdio.h>

int main(void)
{
    // 35까지면 36칸 만들어야지......
    long long dp[36] = {0};
    dp[0] = 1;

    for (int i = 1; i < 36; i++)
    {
        for (int j = 0; j < i; j++)
        {
            dp[i] += dp[j] * dp[i - j - 1];
        }
    }

    int N;
    scanf("%d", &N);

    printf("%lld", dp[N]);

    return 0;
}