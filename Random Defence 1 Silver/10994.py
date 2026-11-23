# Authored by : marigold2003
# Date : 2026-11-23
# Link : https://www.acmicpc.net/problem/10994


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 19

# 3
# *********
# *       *
# * ***** *
# * *   * *
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********


def main() -> None:

    # [Ideas]

    # 인덱스를 잘 굴려보자.
    # "* "와 " *"를 잘 사용하는 게 포인트.

    ##########

    N = int(input())

    board = []
    board.append("*" * ((N - 1) * 4 + 1))

    for i in range(1, N):
        row = "* " * (i)
        row += " " * ((N - i - 1) * 4 + 1)
        row += " *" * (i)
        board.append(row)

        row = "* " * i
        row += "*" * ((N - i - 1) * 4 + 1)
        row += " *" * i
        board.append(row)

    for row in board:
        print(row)

    for row in board[-2::-1]:
        print(row)

    ##########

    return


# [Review]

# 별 찍기는 구현 재활에 좋다.


if __name__ == "__main__":
    main()
