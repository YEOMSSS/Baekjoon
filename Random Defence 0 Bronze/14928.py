# Authored by : marigold2003
# Date : 2026-04-07
# Link : https://www.acmicpc.net/problem/14928


import sys

input = sys.stdin.readline


# [Summary] 큰 수 (BIG)

# N을 20000303으로 나눈 나머지를 출력하시오.
# N(<= 10**1M)


def main() -> None:

    # [Ideas]

    # 숫자 진짜 크네. 파이썬이 좋긴 좋다.

    ##########

    N = int(input())
    print(N % 20000303)

    ##########

    return


# [Review]

# 파이썬만 없었어도 난이도가 수직상승 했을텐데 말이지.


if __name__ == "__main__":
    main()
