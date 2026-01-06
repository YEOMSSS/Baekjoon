# https://www.acmicpc.net/problem/10815

# 그냥 set으로도 풀 수 있다.
# import sys

# input = sys.stdin.readline


# def main() -> None:
#     N = int(input())
#     haves = set(map(int, input().split()))
#     M = int(input())
#     targets = list(map(int, input().split()))
#     for t in targets:
#         print(1 if t in haves else 0, end=" ")


# main()

# 이분탐색으로 풀어볼까?
import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    haves = sorted(list(map(int, input().split())))
    M = int(input())
    targets = list(map(int, input().split()))

    for t in targets:
        left = 0
        right = N - 1

        answer = 0
        while left <= right:
            mid = (left + right) // 2
            cur = haves[mid]
            # if cur == t:
            #     answer = mid
            #     break
            if cur > t:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        if t == haves[answer]:
            print(1, end=" ")
        else:
            print(0, end=" ")


main()
