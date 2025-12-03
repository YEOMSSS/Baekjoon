# https://www.acmicpc.net/problem/2012

# 그리디같은데? 정렬한대로 1234...순서대로 등수 주면 최소일듯.

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    expectatinons = [int(input()) for _ in range(N)]
    expectatinons.sort()

    result = 0
    for i, expect in enumerate(expectatinons):
        result += abs(i + 1 - expect)

    print(result)


main()
