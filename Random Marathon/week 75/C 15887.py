import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    count = 0
    results = []
    for i in range(1, N + 1):
        if arr[i] == i:
            continue

        for j in range(i, N + 1):
            if arr[j] == i:
                arr[i : j + 1] = arr[i : j + 1][::-1]
                results.append((i, j))
                break
        count += 1

    print(count)
    for result in results:
        print(*result)


main()
