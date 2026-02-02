# Authored by : marigold2003
# Date : 2026-02-02
# Link : https://www.acmicpc.net/problem/7595

import sys

input = sys.stdin.readline


# [Summary]

# 0을 입력받을 때까지 밑변이 n인 직각삼각형을 출력한다.


def main() -> None:

    # [Ideas]

    # for문으로 가볍게 처리하자.

    ##########

    while True:
        n = int(input())
        if not n:
            return

        for i in range(1, n + 1):
            print("*" * i)

    ##########

    return


# [Review]

# 이런 날먹도 필요해~~

if __name__ == "__main__":
    main()
