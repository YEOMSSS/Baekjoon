# Authored by : marigold2003
# Date : 2026-01-31
# Link : https://www.acmicpc.net/problem/3216

import sys

input = sys.stdin.readline


# [Summary]

# 노래의 길이와 다운로드하는데 걸리는 시간이 주어진다.
# 노래를 들으려면 다운로드가 완료되어야 하고, 다운로드 순서는 정해져 있다.
# 다운로드 도중에 노래를 재생할 것이며, 노래가 끊기지 않도록 하는 가장 빠른 타이밍은?


def main():

    # [Ideas]

    # 입력을 받는 족족 해결이 가능한 문제다.
    # 다운로드 시간을 소모한 후, 그 노래의 길이만큼 시간을 벌 수 있다.
    # 현재 다운로드 시간 - 이전 노래까지의 길이를 하면 기다려야 하는 시간이 나온다.
    # 그 차의 최댓값이 답이 되겠다.

    ##########

    N = int(input())

    result = 0
    acc_v = 0
    acc_d = 0
    for _ in range(N):
        # 노래 길이, 다운로드 시간
        D, V = map(int, input().split())

        acc_v += V
        result = max(result, acc_v - acc_d)
        acc_d += D

    print(result)

    ##########

    return


# [Review]

# 발상을 한다면 쉽게 풀 수 있다.
# 다만 발상이 조금 걸리긴 했다.
# 규칙을 찾는다는 느낌이 들었다.

# from itertools import accumulate
# 다음엔 이걸로 풀어봐야지.

if __name__ == "__main__":
    main()
