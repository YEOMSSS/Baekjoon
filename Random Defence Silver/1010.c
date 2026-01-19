#include <stdio.h>

int main(void)
{
    long long dp[30][30];

    for (int i = 0; i < 30; i++)
    {
        dp[i][1] = i;
        dp[i][i] = 1;
        for (int j = 2; j < i; j++)
        {
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
        }
    }

    int T;
    scanf("%d", &T);

    while (T--)
    {
        int N, M;
        scanf("%d %d", &N, &M);
        printf("%lld\n", dp[M][N]);
    }
}

// dp는 c언어도 편하다.