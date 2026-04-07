# Authored by : marigold2003
# Date : 2026-03-26
# Link : https://www.acmicpc.net/problem/2443


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 6

# N(<= 100)층짜리 역피라미드를 출력하시오.


def main() -> None:

    # [Ideas]

    # N*2-1 부터 해서 출력해 내려가면 된다.
    # " "는 층만큼 있음.

    ##########

    N = int(input())

    for i in range(N):
        print(" " * i + "*" * ((N - i) * 2 - 1))

    ##########

    return


# [Review]

# 별찍기는 언제해도 재밌다.


if __name__ == "__main__":
    main()
