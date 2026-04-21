# Authored by : marigold2003
# Date : 2026-04-20
# Link : https://www.acmicpc.net/problem/20492


import sys

input = sys.stdin.readline


# [Summary] 세금

# 상금이 N원 주어진다.
# 상금의 78%와 상금의 80% + 20%의 78%를 구하시오.


def main() -> None:

    # [Ideas]

    # 경비로 인정받는게 중요하네.

    ##########

    N = int(input())

    print(N // 100 * 78, N // 100 * 80 + N // 100 * 20 // 100 * 78)

    ##########

    return


# [Review]

# 싸이버거 하나만 주십쇼


if __name__ == "__main__":
    main()
