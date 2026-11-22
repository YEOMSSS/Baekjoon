# Authored by : marigold2003
# Date : 2026-11-22
# Link : https://www.acmicpc.net/problem/2445


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 8

# 5
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


def main() -> None:

    # [Ideas]

    # 인덱스별로 별 하나씩 뽑아주고...
    # 그 다음에 띄어쓰기는 n*2-1 에서 i*2빼면 될듯
    # 그리고 인덱스 넘어가면 거꾸로 뽑고

    # 아 -1이 없는 문제였네... 가운데 별이 하나가 아니라 두개였어?

    ##########

    n = int(input())

    board = []
    for i in range(1, n):
        row = "*" * i
        row += " " * (n * 2 - i * 2)
        row += "*" * i
        board.append(row)

    for row in board:
        print(row)
    print("*" * (n * 2))
    for row in board[::-1]:
        print(row)

    ##########

    return


# [Review]

# 이런 문제는 빠르게 3분컷 내고 가자.


if __name__ == "__main__":
    main()
