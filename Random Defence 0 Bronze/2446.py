# Authored by : marigold2003
# Date : 2026-11-24
# Link : https://www.acmicpc.net/problem/2446


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 9

# 5
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********


def main() -> None:

    # [Ideas]

    # *2 -1이다. 한눈에 보임.

    ##########

    N = int(input())

    board = []
    for i in range(N):
        row = " " * i
        row += "*" * ((N - i) * 2 - 1)
        board.append(row)

    for row in board:
        print(row)

    for row in board[-2::-1]:
        print(row)

    ##########

    return


# [Review]

# 재활용 별찍기 구현


if __name__ == "__main__":
    main()
