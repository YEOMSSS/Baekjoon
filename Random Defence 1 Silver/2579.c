/*
import sys

input = sys.stdin.readline


def main():
    N = int(input())
    scores = [int(input()) for _ in range(N)]

    if N == 1:
        print(scores[0])
        return
    if N == 2:
        print(scores[0] + scores[1])
        return

    dp = [0] * (N)

    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

    print(dp[N - 1])


main()
*/

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int scores[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &scores[i]);

    if (N == 1)
    {
        printf("%d", scores[0]);
        return 0;
    }
    if (N == 2)
    {
        printf("%d", scores[0] + scores[1]);
        return 0;
    }

    int dp[N];
    dp[0] = scores[0];
    dp[1] = scores[0] + scores[1];
    dp[2] = (scores[0] > scores[1]) ? scores[0] + scores[2] : scores[1] + scores[2];

    for (int i = 3; i < N; i++)
    {
        dp[i] = (dp[i - 3] + scores[i - 1] > dp[i - 2]) ? dp[i - 3] + scores[i - 1] + scores[i] : dp[i - 2] + scores[i];
    }

    printf("%d", dp[N - 1]);
    return 0;
}