# Authored by : marigold2003
# Date : 2026-11-26
# Link : https://www.acmicpc.net/problem/7891


import sys

input = sys.stdin.readline


# [Summary] Can you add this?

# 입력을 더해서 출력하라.


def main() -> None:

    # [Ideas]

    # 빠르게 날로 먹자.

    ##########

    N = int(input())

    for _ in range(N):
        print(sum(map(int, input().split())))

    ##########

    return


# [Review]

# 빠르게 처리하고 할 일을 하자.


if __name__ == "__main__":
    main()
