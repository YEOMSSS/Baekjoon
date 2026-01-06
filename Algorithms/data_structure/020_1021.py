import sys

input = sys.stdin.readline

from collections import deque


def main() -> None:
    N, M = map(int, input().split())
    targets = list(map(int, input().split()))

    nums = deque(range(1, N + 1))

    result = 0
    for t in targets:
        idx = nums.index(t)
        length = len(nums)
        if idx > length // 2:
            nums.rotate(length - idx)
            result += length - idx
        else:
            nums.rotate(-idx)
            result += idx

        nums.popleft()

    print(result)


main()
