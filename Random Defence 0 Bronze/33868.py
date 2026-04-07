# Authored by : marigold2003
# Date : 2026-04-03
# Link : https://www.acmicpc.net/problem/33868


import sys

input = sys.stdin.readline


# [Summary] 스티커 나눠주기

# T와 B가 주어진다.
# 가장 큰 T와 가장 작은 B의 곱을 7로 나눈 나머지를 구하시오.
# 이후 1을 더해 출력하시오.


def main() -> None:

    # [Ideas]

    # 해석해놓으니까 그냥 끝나버렸네.
    # 문제가 쉬워용.

    ##########

    N = int(input())
    Tset, Bset = set(), set()
    for _ in range(N):
        t, b = map(int, input().split())
        Tset.add(t)
        Bset.add(b)

    print(max(Tset) * min(Bset) % 7 + 1)

    ##########

    return


# [Review]

# 나도 스티커 줘~~


if __name__ == "__main__":
    main()
