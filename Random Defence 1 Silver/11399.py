# 정렬문제니까 파이썬으로.

import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    total = 0
    result = 0
    for t in arr:
        total += t
        result += total

    print(result)


main()
