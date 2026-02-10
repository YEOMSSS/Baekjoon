# 이썬이형 도와주오

import sys

input = sys.stdin.readline


def main():
    T = int(input())

    for _ in range(T):
        M, N = map(int, input().split())

        arr = [list(map(int, input().split())) for _ in range(N)]

        biggest = 0
        result = 0

        for j in range(M):
            mult = 1
            for i in range(N):
                mult *= arr[i][j]

            if j == 0:
                biggest = mult
                continue

            if biggest <= mult:
                biggest = mult
                result = j

        print(result + 1)


main()
