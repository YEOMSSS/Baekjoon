import sys

input = sys.stdin.readline


def b_search(arr, val) -> int:

    # 배열에 없을 경우 처리
    if val > arr[-1]:
        return len(arr)
    if val < arr[0]:
        return 0

    left = 0
    right = len(arr) - 1  # N

    result = 0
    while left <= right:
        mid = (left + right) // 2
        cur = arr[mid]

        if cur >= val:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def main() -> None:
    N, M = map(int, input().split())
    dots = list(map(int, input().split()))
    dots.sort()
    lines = list(tuple(map(int, input().split())) for _ in range(M))

    for first, last in lines:
        # last + 1로 이분탐색을 하면 편하다.
        print(b_search(dots, last + 1) - b_search(dots, first))


main()


# import sys

# input = sys.stdin.readline


# def b_search(arr, val, flag) -> int:

#     if val > arr[-1]:
#         return len(arr)
#     if val < arr[0]:
#         return 0

#     left = 0
#     right = len(arr) - 1  # N

#     result = 0
#     while left <= right:
#         mid = (left + right) // 2
#         cur = arr[mid]

#         if cur == val and flag:
#             result = mid + 1
#             return result

#         if cur >= val:
#             result = mid
#             right = mid - 1
#         else:
#             left = mid + 1

#     return result


# def main() -> None:
#     N, M = map(int, input().split())
#     dots = list(map(int, input().split()))
#     dots.sort()
#     lines = list(tuple(map(int, input().split())) for _ in range(M))

#     for first, last in lines:
#         print(b_search(dots, last, True) - b_search(dots, first, False))


# main()
