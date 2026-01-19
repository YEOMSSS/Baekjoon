# 3전계단 밟고 2전계단 안밞고 전계단을 밟은경우, 2전계단 밟고 전계단을 안밟은경우. 두가지.
# 이번 계단을 밟는 경우는 ...1011 or ...1101 밖에 없다는거임

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
