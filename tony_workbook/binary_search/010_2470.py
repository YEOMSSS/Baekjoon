import sys

input = sys.stdin.readline


def b_search(positives: list, target: int) -> int:
    left = 0
    right = len(positives) - 1

    result = 0

    while left <= right:
        mid = (left + right) // 2

        cur = positives[mid]

        if cur >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def main() -> None:

    N = int(input())
    positives = []
    negatives = []

    for x in map(int, input().split()):
        if x >= 0:
            positives.append(x)
        else:
            negatives.append(x)

    positives.sort()
    negatives.sort()

    if not negatives:
        print(*positives[:2])
        return
    if not positives:
        print(*negatives[-2:])
        return

    result = (1000000000, 1000000000)

    if len(positives) > 1:
        if abs(sum(positives[:2])) < abs(sum(result)):
            result = tuple(positives[:2])

    if len(negatives) > 1:
        if abs(sum(negatives[-2:])) < abs(sum(result)):
            result = tuple(negatives[-2:])

    for n in negatives:
        i = b_search(positives, -n)

        current1 = (positives[i], n)
        if abs(sum(result)) > abs(sum(current1)):
            result = current1

        current2 = (positives[i - 1], n)
        if abs(sum(result)) > abs(sum(current2)):
            result = current2

    print(*sorted(result))


if __name__ == "__main__":
    main()


# 그냥 투포인터가 더 편했겠구만..
# import sys


# def requid_mix(arr):

#     start = 0
#     end = len(arr) - 1
#     done = float("inf")
#     a, b = 0, 0

#     while start < end:
#         s = arr[start] + arr[end]
#         if abs(s) <= done:
#             done = abs(s)
#             a, b = start, end

#         if s < 0:
#             start += 1
#         else:
#             end -= 1

#     print(arr[a], arr[b])


# n = int(input())
# arr = []
# arr = list(map(int, sys.stdin.readline().split(" ")))
# arr.sort()
# requid_mix(arr)
