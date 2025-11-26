import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    T = int(input())

    for _ in range(T):
        i, j, x, y = map(int, input().split())

        result = 0
        for row in range(i - 1, x):
            for col in range(j - 1, y):
                result += arr[row][col]

        print(result)


main()
