# Authored by : marigold2003
# Date : 2026-02-21
# Link : https://www.acmicpc.net/problem/14613


import sys

input = sys.stdin.readline


# [Summary] 너의 티어는?

# 한판 이기면 +50점, 지면 -50점이다.
# 2000점에서 시작해서 20게임 진행할 것이다.
# 승리할 확률, 질 확률, 비길 확률이 주어질 때 (소수점 둘째자리까지)
# 각 티어에 도착할 확률을 구하시오.

# 브론즈: 1000 ~ 1499
# 실버: 1500 ~ 1999
# 골드: 2000 ~ 2499
# 플래티넘: 2500 ~ 2999
# 다이아: 3000 ~ 3499


def main() -> None:

    # [Ideas]

    # 20게임을 진행하는 모든 경우를 구해야 할 듯.

    # dp로 해서, 계속해서 쌓아가면 되지 않을까.
    # 현재 이 점수인 경우 N회에 대해 +50, -50으로 퍼트리는거지.
    # 전부 50으로 나누고 +1 -1 하자.

    # 그러면 0~80 81칸 나오고 40에서 게임 시작이다.
    # 20 ~ 29 브론즈
    # 30 ~ 39 실버
    # 40 ~ 49 골드
    # 50 ~ 59 플레
    # 60 ~ 69 다이아

    ##########

    W, L, D = map(float, input().split())

    dp = [[0 for _ in range(80 + 1)] for _ in range(20 + 1)]

    # 0게임 2000점 시작
    dp[0][40] = 1

    for i in range(1, 20 + 1):
        for s in range(81):

            if s > 0:
                dp[i][s] += dp[i - 1][s - 1] * W
            if s < 80:
                dp[i][s] += dp[i - 1][s + 1] * L
            dp[i][s] += dp[i - 1][s] * D

    for n in range(20, 70, 10):
        print(f"{sum(dp[20][n : n + 10]):.8f}")

    ##########

    return


# [Review]

# 확률이라! 재밌네.
# 배열은 더 깎기 귀찮으니까 그냥 앞뒤로 좀 남기자고.


if __name__ == "__main__":
    main()
