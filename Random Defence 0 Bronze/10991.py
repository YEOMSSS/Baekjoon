# Authored by : marigold2003
# Date : 2026-03-21
# Link : https://www.acmicpc.net/problem/10991


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 16

# 예제대로 별을 찍으시오.


def main() -> None:

    # [Ideas]

    # 사이에 스페이스바만 넣어주면 된다.

    ##########

    N = int(input())

    for i in range(1, N + 1):
        print(" " * (N - i) + "* " * i)

    ##########

    return


# [Review]

# 별만 찍으면서 살고 싶다.


if __name__ == "__main__":
    main()
