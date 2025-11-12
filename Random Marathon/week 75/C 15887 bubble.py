import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    count = 0
    results = []
    for i in range(1, N + 1):
        for j in range(1, N - i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                results.append((j, j + 1))
                count += 1

    print(count)
    for result in results:
        print(*result)


main()
