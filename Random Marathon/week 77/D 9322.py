import sys

input = sys.stdin.readline


def main():
    T = int(input())

    for _ in range(T):
        n = int(input())

        key1 = list(input().split())
        key2 = list(input().split())

        arr = [None] * n

        for i in range(n):
            arr[i] = key1.index(key2[i])

        cipher = list(input().split())
        result = []
        for i in range(n):
            result.append(cipher[arr.index(i)])
        print(*result)


main()
