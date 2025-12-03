import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    coords = list(map(int, input().split()))

    grade = sorted(set(coords))
    length = len(grade)
    for i in range(N):
        target = coords[i]
        left = 0
        right = length - 1

        result = 0
        while left <= right:
            mid = (left + right) // 2
            cur = grade[mid]

            if cur >= target:
                result = mid
                right = mid - 1
            else:  # cur < target
                left = mid + 1

        print(result, end=" ")


main()
