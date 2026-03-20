# Authored by : marigold2003
# Date : 2026-03-20
# Link : https://www.acmicpc.net/problem/28352


import sys

input = sys.stdin.readline


# [Summary] 10!

# 6주는 10!초다.
# N!이 몇주인지 구하시오.


def main() -> None:

    # [Ideas]

    # 1에 11~N을 곱하면 된다.
    # 그리고 6을 곱해주면 끝.

    ##########

    N = int(input())
    result = 1
    for i in range(11, N + 1):
        result *= i

    print(result * 6)

    ##########

    return


# [Review]

# 입력이 10부터라서 편하다.


if __name__ == "__main__":
    main()
