# Authored by : marigold2003
# Date : 2026-03-09
# Link : https://www.acmicpc.net/problem/17356


import sys

input = sys.stdin.readline


# [Summary] 욱 제

# A와 B가 주어진다.
# (B-A) / 400을 M이라 한다.
# 1 / (1 + 10**M)을 구하시오.


def main() -> None:

    # [Ideas]

    # 수식을 그대로 계산하자.

    ##########

    A, B = map(int, input().split())
    M = (B - A) / 400
    answer = 1 / (1 + 10**M)

    print(answer)

    ##########

    return


# [Review]

# 하루의 마지막을 장식하자.


if __name__ == "__main__":
    main()
