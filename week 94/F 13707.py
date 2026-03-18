# Authored by : marigold2003
# Date : 2026-03-18
# Link : https://www.acmicpc.net/problem/13707


import sys

input = sys.stdin.readline


# [Summary] 합분해 2

# 0 ~ N(<= 5K)의 정수 K(<= 5K)개를 이용해서
# 그 합이 N이 되는 경우의 수를 출력하시오.

# 같은 수를 여러번 사용할 수 있고,
# 덧셈의 순서가 다르면 다른 경우로 친다.


def main() -> None:

    # [Ideas]

    # 일단 브루트포스는 아님. 모든 조합을 만들 수 없음.
    # 5K**5K는 진짜 개지랄임.

    # 앞에 찾은 게 어떤 식으로 연관이 있을지 생각을 해봐야 함.

    # 2를 만드는 경우의 수는
    # K-1개로 2를 만드는 경우의 수에 0을 붙이거나
    # K개로 1을 만드는 경우의 수.
    # dp구만. 2차원 배열을 만들자.

    # K개로

    ##########

    MOD = 1_000_000_000
    N, K = map(int, input().split())

    # dp[k][n] 은 k개로 n을 만드는 경우의 수
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # n이 0이면 무조건 1 (0을 더하는 방법뿐)
    for k in range(K + 1):
        dp[k][0] = 1

    # k가 1이면 무조건 1 (n 자신 하나뿐)
    for n in range(N + 1):
        dp[1][n] = 1

    for k in range(2, K + 1):
        for n in range(1, N + 1):
            # [k-1][n]에 0 붙이기 + [k][n-1] 마지막에 1 더하기
            dp[k][n] = (dp[k - 1][n] + dp[k][n - 1]) % MOD

    print(dp[K][N])

    ##########

    return


# [Review]

# 그나마 괜찮은 dp.
# 0으로 끝나는 것 + 1 이상으로 끝나는 것이 된다.


if __name__ == "__main__":
    main()
