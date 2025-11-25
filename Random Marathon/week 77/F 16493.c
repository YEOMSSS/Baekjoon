#include <stdio.h>

int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

int knapsack(int max_weight, int n, int weights[], int values[])
{
    int dp[n + 1][max_weight + 1];
    // for (int i = 0; i <= n; i++)
    // {
    //     for (int j = 0; j <= max_weight; j++)
    //     {
    //         dp[i][j] = 0;
    //     }
    // }

    for (int i = 1; i <= n; i++)
    {
        for (int w = 1; w <= max_weight; w++)
        {
            if (weights[i - 1] <= w)
            {
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            }
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][max_weight];
}

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int days[M], pages[M];
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d", &days[i], &pages[i]);
    }

    printf("%d", knapsack(N, M, days, pages));
    return 0;
}