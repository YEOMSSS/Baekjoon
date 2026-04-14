# Authored by : marigold2003
# Date : 2026-04-14
# Link : https://www.acmicpc.net/problem/31922


import sys

input = sys.stdin.readline


# [Summary] 이 대회는 이제 제 겁니다

# A, P, C가 주어진다.
# A+C와 P중 큰 것을 구하시오.


def main() -> None:

    # [Ideas]

    # 그렇습니다. 구현하세요!

    ##########

    A, P, C = map(int, input().split())

    print(max(A + C, P))

    ##########

    return


# [Review]

# 제 마음대로 할 수 있는 겁니다.


if __name__ == "__main__":
    main()
