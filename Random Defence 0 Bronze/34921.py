# Authored by : marigold2003
# Date : 2026-04-02
# Link : https://www.acmicpc.net/problem/34921


import sys

input = sys.stdin.readline


# [Summary] 덕후

# 덕후력 P를 계산하는 수식은 다음과 같다.
# P = 10 + 2(25 - A + T)
# P가 0보다 작으면 0으로 취급한다.

# A와 T가 주어질 때, P를 계산하시오.


def main() -> None:

    # [Ideas]

    # 수식이 어렵지 않게 구현 가능하다.

    ##########

    A, T = map(int, input().split())
    P = max(0, 10 + 2 * (25 - A + T))

    print(P)

    ##########

    return


# [Review]

# 이런 문제만 풀면서 살고싶어. 하루에 천 개라도 풀 수 있어.


if __name__ == "__main__":
    main()
